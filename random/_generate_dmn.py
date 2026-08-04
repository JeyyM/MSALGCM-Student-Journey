#!/usr/bin/env python3
"""Generate / refresh DMN decision tables from canonical BPMN + combination matrix CSV.

Each transition DMN includes a Rationale column for stakeholder review.
Run from repo root: python "BPMN Code/_generate_dmn.py"
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).parent
REPO = ROOT.parent
CSV_MATRIX = REPO / "documentation/workbook_patches/combination_matrix_post_m3.csv"

# ── Manual supplements (cross-part handoffs, corrections, insight) ──────────
# Key: bpmn stem → list of (current, event, next, rationale)
MANUAL_RULES: dict[str, list[tuple[str, str, str, str]]] = {
    "part_2a_exam_evaluation": [
        (
            "A4.0 — Exam Taken [Applicant]",
            "Evaluation complete (no further screening)",
            "-> Part 2B: Admission Decision",
            "Exam path to admission results when OAS does not require A4.3.",
        ),
    ],
    "part_2b_admission_results": [
        (
            "(from Part 2A evaluation)",
            "Within cutoff",
            "A5.0 — Offered [OAS]",
            "Admission decision gateway outcome — within cutoff score.",
        ),
        (
            "(from Part 2A evaluation)",
            "Probationary",
            "A5.1 — Probationary (IS/GS/SOL) [OAS]",
            "IS/GS/SOL only per workbook A5.1 level scope (correction #24).",
        ),
        (
            "(from Part 2A evaluation)",
            "Redirected",
            "A5.2 — Redirected [OAS]",
            "Redirected to another program/strand.",
        ),
        (
            "(from Part 2A evaluation)",
            "Waitlisted",
            "A5.3 — Waitlisted [OAS]",
            "No immediate slot; may convert when slot opens.",
        ),
        (
            "(from Part 2A evaluation)",
            "Outside cutoff",
            "A5.5 — Not Qualified [OAS] (terminal)",
            "Terminal rejection; A5.4 Reconsidered appeal intentionally omitted (decisions.md).",
        ),
        (
            "A5.3 — Waitlisted [OAS]",
            "Slot opened",
            "A5.0 — Offered [OAS]",
            "Waitlist conversion to formal offer.",
        ),
        (
            "A5.0 — Offered [OAS]",
            "(proceed to acceptance)",
            "-> Part 3: Acceptance",
            "Offer acknowledged; continues to Official Acceptance fee (A6.0).",
        ),
        (
            "A5.1 — Probationary (IS/GS/SOL) [OAS]",
            "Offer received",
            "-> Part 3: Acceptance",
            "Probationary offer accepted; maps to program P1.1 at bridge.",
        ),
        (
            "A5.2 — Redirected [OAS]",
            "Offer received",
            "-> Part 3: Acceptance",
            "Redirected offer accepted.",
        ),
    ],
    "part_3_acceptance_to_student": [
        (
            "-> Part 3: Acceptance (from A5.x offer)",
            "Official Acceptance fee paid/waived",
            "A6.0 — Reserved [Admissions]",
            "Post-M3: Official Acceptance / acceptance fee (not M3 Enrollment Reservation Fee).",
        ),
    ],
    "part_2_residency_and_loa": [
        (
            "S2.0 — Active [Registrar]",
            "LOA max exceeded / last enrollment > 6 trimesters",
            "S2.3 — Prolonged Leave [Registrar]",
            "Post-M3 S2.3; inferred pair rules in combination matrix (#15).",
        ),
        (
            "S2.2 — Under LOA [Registrar]",
            "Returnee approved",
            "S1.0 — Without Enrollment [Registrar]",
            "Returnee re-enters without enrollment before S2.0.",
        ),
    ],
    "part_4_graduation_and_terminal_states": [
        (
            "S2.0 — Active [Registrar]",
            "All programs graduated",
            "S4.0 — Graduated (Alumni may continue) [Registrar]",
            "Workbook omits TERMINAL on S4.0; alumni/BS→MS may re-enroll (executive default #7).",
        ),
    ],
    "3. parallel_student_program_constrained_fsm": [
        (
            "Admitted from A7.x [Admissions]",
            "(default)",
            "S1.0 — Without Enrollment [Registrar]",
            "Hand-off from applicant A7.x admission.",
        ),
        (
            "P1.4 — Ineligible + shift pending [Program Office]",
            "forces (COMBO-T004)",
            "S1.0 — Without Enrollment [Registrar]",
            "Cross-dimension: ineligible program triggers shift → without enrollment.",
        ),
        (
            "All programs → P3.0 Graduated [Program Office]",
            "forces (COMBO-T001)",
            "S4.0 — Graduated (Alumni may continue) [Registrar]",
            "Cross-dimension: all programs graduated → student S4.0.",
        ),
    ],
}

SKIP_BPMN_PARSE: set[str] = {"part_2b_admission_results"}

HANDOFF_REPLACEMENTS = {
    "Continue to evaluation [OAS]": "-> Part 2A: Initial Evaluation",
    "To admission results [OAS]": "-> Part 2B: Admission Decision",
    "Continue to acceptance [Applicant]": "-> Part 3: Acceptance",
    "Continues in Parts 2–4 [Registrar]": "-> Parts 2–4 (student lifecycle)",
    "Continues in Parts 2–3 [Program Office]": "-> Parts 2–3 (program lifecycle)",
}

GATEWAY_AS_ABSTRACT = {
    "Admission decision [OAS]": "(from Part 2A evaluation)",
    "Requirements OK? [OAS]": "(requirements check)",
    "Requirements complete? [Admissions]": "(requirements check)",
    "Initial evaluation [OAS]": "A2.0 — Complete Requirements [OAS]",
    "Exam outcome [OAS]": "A3.0 — Exam Required [OAS]",
}

# Override labels parsed from BPMN (corrections)
LABEL_OVERRIDES: dict[str, str] = {
    "A5_1": "A5.1 — Probationary (IS/GS/SOL) [OAS]",
    "S4_0": "S4.0 — Graduated (Alumni may continue) [Registrar]",
}

DEFAULT_RATIONALE = "Derived from canonical BPMN sequence flow."


@dataclass
class Rule:
    current: str
    event: str
    nxt: str
    rationale: str = DEFAULT_RATIONALE
    src_id: str = ""
    tgt_id: str = ""


@dataclass
class DecisionSpec:
    decision_id: str
    decision_name: str
    input1_label: str = "Current State"
    input1_var: str = "current_state"
    input2_label: str = "Event / Outcome"
    input2_var: str = "event"
    output1_label: str = "Next State"
    output1_name: str = "next_state"
    rules: list[Rule] = field(default_factory=list)


@dataclass
class DmnSpec:
    rel_path: str  # e.g. "1. applicant_status/DMN ....dmn"
    def_id: str
    name: str
    namespace: str
    decisions: list[DecisionSpec]


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def q(text: str) -> str:
    return f'"{esc(text)}"'


def normalize_rule(rule: Rule) -> Rule:
    rule.current = GATEWAY_AS_ABSTRACT.get(rule.current, rule.current)
    rule.nxt = HANDOFF_REPLACEMENTS.get(rule.nxt, rule.nxt)
    if "Gateway" in rule.current:
        rule.current = "(decision gateway)"
    return rule


def parse_bpmn_transitions(bpmn_path: Path) -> list[Rule]:
    stem = bpmn_path.stem
    text = bpmn_path.read_text(encoding="utf-8")

    names: dict[str, str] = {}
    for tag in ("serviceTask", "userTask", "startEvent", "endEvent", "exclusiveGateway"):
        for m in re.finditer(
            rf'<bpmn:{tag}\s+id="([^"]+)"\s+name="([^"]*)"',
            text,
        ):
            eid, label = m.group(1), m.group(2)
            names[eid] = LABEL_OVERRIDES.get(eid) or label or eid

    rules: list[Rule] = []
    if stem not in SKIP_BPMN_PARSE:
        flow_re = re.compile(
            r'<bpmn:sequenceFlow\s+id="[^"]+"'
            r'(?:\s+name="([^"]*)")?'
            r'[^>]*sourceRef="([^"]+)"\s+targetRef="([^"]+)"'
            r'|<bpmn:sequenceFlow\s+id="[^"]+"'
            r'[^>]*sourceRef="([^"]+)"\s+targetRef="([^"]+)"'
            r'(?:\s+name="([^"]*)")?'
        )
        for m in flow_re.finditer(text):
            if m.group(2):
                event, src, tgt = m.group(1) or "(transition)", m.group(2), m.group(3)
            else:
                src, tgt, event = m.group(4), m.group(5), m.group(6) or "(transition)"
            cur = names.get(src, src)
            nxt = names.get(tgt, tgt)
            rules.append(Rule(cur, event, nxt, src_id=src, tgt_id=tgt))

    for cur, event, nxt, rationale in MANUAL_RULES.get(stem, []):
        rules.append(Rule(cur, event, nxt, rationale))

    seen: dict[tuple[str, str, str], Rule] = {}
    for r in rules:
        normalize_rule(r)
        seen[(r.current, r.event, r.nxt)] = r
    return list(seen.values())


def is_s_axis(rule: Rule) -> bool:
    if rule.src_id.startswith("S") or rule.src_id == "Start":
        return rule.tgt_id.startswith("S") or rule.tgt_id == "Start"
    if rule.current.startswith("Admitted") or rule.current.startswith("All programs"):
        return True
    if "COMBO-T004" in rule.event or "COMBO-T001" in rule.event:
        return True
    return False


def is_p_axis(rule: Rule) -> bool:
    if rule.src_id.startswith("P") or rule.src_id.startswith("Activity"):
        return rule.tgt_id.startswith("P") or rule.tgt_id.startswith("Activity")
    if rule.current.startswith("S1.0") and rule.tgt_id.startswith("P"):
        return True  # initial pairing at admission
    if "COMBO-T003" in rule.rationale or "University exit" in rule.event:
        return rule.tgt_id.startswith("P") or "P3.1" in rule.nxt
    return False


def parallel_fsm_decisions(bpmn_rel: str) -> tuple[DecisionSpec, DecisionSpec]:
    path = ROOT / bpmn_rel
    all_rules = parse_bpmn_transitions(path)
    s_rules = [r for r in all_rules if is_s_axis(r)]
    p_rules = [r for r in all_rules if is_p_axis(r)]
    p_rules = [r for r in p_rules if "VALID" not in r.tgt_id and "VALID" not in r.src_id]

    # Prefer manual COMBO rules over parsed duplicates
    def dedupe_combo(rules: list[Rule]) -> list[Rule]:
        out: dict[tuple[str, str], Rule] = {}
        for r in rules:
            key = (r.current, r.event)
            if key in out and "COMBO" in out[key].rationale and "Derived" in r.rationale:
                continue
            if key in out and "Derived" in out[key].rationale and "COMBO" in r.rationale:
                out[key] = r
            else:
                out[key] = r
        return list(out.values())

    s_rules = dedupe_combo(s_rules)

    s_spec = DecisionSpec(
        "decision_axis_S_student_status_part3",
        "Student-Status Axis (S) — Parallel FSM",
        input1_label="Current S-State",
        input1_var="current_S_state",
        output1_label="Next S-State",
        output1_name="next_S_state",
        rules=sorted(s_rules, key=lambda r: (r.current, r.event)),
    )
    p_spec = DecisionSpec(
        "decision_axis_P_program_status_part3",
        "Program-Status Axis (P) — Parallel FSM",
        input1_label="Current P-State",
        input1_var="current_P_state",
        output1_label="Next P-State",
        output1_name="next_P_state",
        rules=sorted(p_rules, key=lambda r: (r.current, r.event)),
    )
    return s_spec, p_spec


def rules_from_bpmn(bpmn_rel: str, decision_id: str, decision_name: str, **kw) -> DecisionSpec:
    path = ROOT / bpmn_rel
    rules = [Rule(r.current, r.event, r.nxt, r.rationale) for r in parse_bpmn_transitions(path)]
    rules.sort(key=lambda r: (r.current, r.event))
    return DecisionSpec(decision_id, decision_name, rules=rules, **kw)


def render_decision_table(prefix: str, spec: DecisionSpec) -> str:
    lines = [
        f'  <decision id="{spec.decision_id}" name="{esc(spec.decision_name)}">',
        f'    <decisionTable id="dt_{prefix}" hitPolicy="UNIQUE">',
        f'      <input id="in1_{prefix}" label="{esc(spec.input1_label)}">',
        f'        <inputExpression id="in1e_{prefix}" typeRef="string">',
        f"          <text>{spec.input1_var}</text>",
        "        </inputExpression>",
        "      </input>",
        f'      <input id="in2_{prefix}" label="{esc(spec.input2_label)}">',
        f'        <inputExpression id="in2e_{prefix}" typeRef="string">',
        f"          <text>{spec.input2_var}</text>",
        "        </inputExpression>",
        "      </input>",
        f'      <output id="out1_{prefix}" label="{esc(spec.output1_label)}" name="{spec.output1_name}" typeRef="string"/>',
        f'      <output id="out2_{prefix}" label="Rationale" name="rationale" typeRef="string"/>',
    ]
    for i, rule in enumerate(spec.rules, 1):
        rid = f"row_{prefix}_{i}"
        lines.extend(
            [
                f'      <rule id="{rid}">',
                f"        <inputEntry id=\"{rid}_i1\"><text>{q(rule.current)}</text></inputEntry>",
                f"        <inputEntry id=\"{rid}_i2\"><text>{q(rule.event)}</text></inputEntry>",
                f"        <outputEntry id=\"{rid}_o1\"><text>{q(rule.nxt)}</text></outputEntry>",
                f"        <outputEntry id=\"{rid}_o2\"><text>{q(rule.rationale)}</text></outputEntry>",
                "      </rule>",
            ]
        )
    lines.extend(["    </decisionTable>", "  </decision>"])
    return "\n".join(lines)


def render_dmn(spec: DmnSpec) -> str:
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<definitions xmlns="https://www.omg.org/spec/DMN/20191111/MODEL/"',
        '             xmlns:dmndi="https://www.omg.org/spec/DMN/20191111/DMNDI/"',
        '             xmlns:dc="http://www.omg.org/spec/DMN/20180521/DC/"',
        f'             id="{spec.def_id}"',
        f'             name="{esc(spec.name)}"',
        f'             namespace="{spec.namespace}">',
    ]
    for dec in spec.decisions:
        prefix = dec.decision_id.replace("decision_", "")
        parts.append(render_decision_table(prefix, dec))
    parts.append("</definitions>")
    return "\n".join(parts) + "\n"


def cross_impact_rules(decision_id: str, decision_name: str, combo_prefix: bool) -> DecisionSpec:
    if combo_prefix:
        rows = [
            (
                "All programs → P3.0 Graduated [Program Office]",
                "forces",
                "COMBO-T001: Student → S4.0 Graduated (Alumni may continue) [Registrar]",
                "When every program is P3.0, student becomes S4.0 (non-terminal for re-enrollment).",
            ),
            (
                "Student exit, program active [Student]",
                "forces",
                "COMBO-T003: Program → P3.1 Incomplete [Program Office]",
                "University exit while program still active sets program to Incomplete.",
            ),
            (
                "P1.4 Ineligible + shift pending [Program Office]",
                "forces",
                "COMBO-T004: Student → S1.0 Without Enrollment [Registrar]",
                "Ineligible triggers shift process; student returns to Without Enrollment.",
            ),
            (
                "COMBO-T004: Student → S1.0 [Registrar]",
                "shift approved",
                "COMBO-T005: Shift approved → S2.0 Active [Registrar]",
                "Approved shift re-activates student for new program enrollment.",
            ),
        ]
    else:
        rows = [
            (
                "All programs → P3.0 Graduated [Program Office]",
                "forces",
                "Student → S4.0 Graduated (Alumni may continue) [Registrar]",
                "Cross-dimension graduation trigger (COMBO-T001).",
            ),
            (
                "Student exit, program active [Student]",
                "forces",
                "Program → P3.1 Incomplete [Program Office]",
                "Exit forces incomplete program (COMBO-T003).",
            ),
            (
                "P1.4 Ineligible + shift pending [Program Office]",
                "forces",
                "Student → S1.0 Without Enrollment [Registrar]",
                "Ineligible + shift pending (COMBO-T004). Uses P1.4 not legacy P1.3.",
            ),
            (
                "Student → S1.0 Without Enrollment [Registrar]",
                "shift approved",
                "Student → S2.0 Active [Registrar]",
                "Shift approved (COMBO-T005).",
            ),
        ]
    return DecisionSpec(
        decision_id,
        decision_name,
        input1_label="Triggering Condition",
        input1_var="triggering_condition",
        input2_label="Rule / Approval Event",
        input2_var="rule_event",
        output1_label="Forced Outcome",
        output1_name="forced_outcome",
        rules=[Rule(*r) for r in rows],
    )


def high_level_rules() -> DecisionSpec:
    rows = [
        ("(start)", "(default)", "Applicant phase (A0–A5.x) [Applicant]", "Entry into admission application lifecycle."),
        (
            "Accepted (A6.0–A7.x) [Admissions]",
            "Becomes student",
            "Active Student (S1.0–S2.x) [Enrollment]",
            "Hand-off at Official Admission; student may enroll from S1.0.",
        ),
        (
            "LOA / AWOL / Suspended [Enrollment]",
            "Returnee re-enrolls",
            "Active Student (S1.0–S2.x) [Enrollment]",
            "Returnee path restores active university standing.",
        ),
        (
            "Active Student (S1.0–S2.x) [Enrollment]",
            "Graduate or exit",
            "Graduation / Exit / Terminal [University]",
            "University-level exit or graduation outcome.",
        ),
        (
            "Active Student (S1.0–S2.x) [Enrollment]",
            "Academic standing",
            "Program Standing (P1.0–P2.0) [Program Office]",
            "Program dimension tracked in parallel (see combination matrix).",
        ),
        (
            "Program Standing (P1.0–P2.0) [Program Office]",
            "All programs graduated",
            "Graduation / Exit / Terminal [University]",
            "COMBO-T001 when all programs reach P3.0.",
        ),
        (
            "Graduation / Exit / Terminal [University]",
            "(default)",
            "Terminal [University]",
            "S4.1/S4.2 are hard terminals; S4.0 allows alumni continuation.",
        ),
    ]
    return DecisionSpec(
        "decision_phase_1_high_level_lifecycle",
        "Lifecycle Phase — Part 1: High-Level Overview",
        input1_label="Current Phase",
        input1_var="current_phase",
        input2_label="Event / Outcome",
        input2_var="event",
        output1_label="Next Phase",
        output1_name="next_phase",
        rules=[Rule(*r) for r in rows],
    )


def combination_matrix_decision() -> DecisionSpec:
    rules: list[Rule] = []
    with CSV_MATRIX.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            s, p = row["StudentCode"], row["ProgramCode"]
            allowed = row["Allowed"].upper()
            reason = row["ScenarioReason"]
            rules.append(
                Rule(
                    s,
                    p,
                    allowed,
                    reason,
                )
            )
    return DecisionSpec(
        "decision_combination_matrix_validation",
        "Student × Program Combination Validation (Post-M3)",
        input1_label="Student Status Code",
        input1_var="student_code",
        input2_label="Program Status Code",
        input2_var="program_code",
        output1_label="Allowed",
        output1_name="allowed",
        rules=rules,
    )


def build_specs() -> list[DmnSpec]:
    specs: list[DmnSpec] = []

    applicant = [
        (
            "part_1_account_to_submission",
            "DMN applicant_status part_1_account_to_submission.dmn",
            "decision_applicant_status_part_1_account_to_submission",
            "Applicant Status — Part 1: Account to Submission",
        ),
        (
            "part_2a_exam_evaluation",
            "DMN applicant_status part_2a_exam_evaluation.dmn",
            "decision_applicant_status_part_2a_exam_evaluation",
            "Applicant Status — Part 2A: Exam & Evaluation",
        ),
        (
            "part_2b_admission_results",
            "DMN applicant_status part_2b_admission_results.dmn",
            "decision_applicant_status_part_2b_admission_results",
            "Applicant Status — Part 2B: Admission Results",
        ),
        (
            "part_3_acceptance_to_student",
            "DMN applicant_status part_3_acceptance_to_student.dmn",
            "decision_applicant_status_part_3_acceptance_to_student",
            "Applicant Status — Part 3: Acceptance to Student",
        ),
        (
            "part_4_terminal_or_exception_states",
            "DMN applicant_status part_4_terminal_or_exception_states.dmn",
            "decision_applicant_status_part_4_terminal_or_exception_states",
            "Applicant Status — Part 4: Terminal & Exception States",
        ),
    ]
    for stem, dmn_name, dec_id, dec_name in applicant:
        slug = stem.replace(".", "_")
        specs.append(
            DmnSpec(
                f"1. applicant_status/{dmn_name}",
                f"def_applicant_status_{slug}",
                dmn_name.replace(".dmn", ""),
                f"https://studentjourneymatrix.local/applicant_{slug}",
                [rules_from_bpmn(f"1. applicant_status/{stem}.bpmn", dec_id, dec_name)],
            )
        )

    student = [
        ("part_1_active_and_enrollment", "Part 1: Active & Enrollment"),
        ("part_2_residency_and_loa", "Part 2: Residency & LOA"),
        ("part_3_awol_suspension_and_exit", "Part 3: AWOL, Suspension & Exit"),
        ("part_4_graduation_and_terminal_states", "Part 4: Graduation & Terminal"),
    ]
    for stem, title in student:
        slug = stem.replace(".", "_")
        dec_id = f"decision_student_status_{slug}"
        dmn_name = f"DMN student_status {stem}.dmn"
        specs.append(
            DmnSpec(
                f"2. student_status/{dmn_name}",
                f"def_student_status_{slug}",
                dmn_name.replace(".dmn", ""),
                f"https://studentjourneymatrix.local/student_{slug}",
                [rules_from_bpmn(f"2. student_status/{stem}.bpmn", dec_id, f"Student Status — {title}")],
            )
        )

    program = [
        ("part_1_good_standing_and_probation", "Part 1: Good Standing & Probation"),
        ("part_2_snas_sap_and_ineligible", "Part 2: SNAS, SAP & Ineligible"),
        ("part_3_graduation_and_terminal_states", "Part 3: Graduation & Terminal"),
    ]
    for stem, title in program:
        slug = stem.replace(".", "_")
        dec_id = f"decision_program_status_{slug}"
        dmn_name = f"DMN student_program_status {stem}.dmn"
        specs.append(
            DmnSpec(
                f"3. student_program_status/{dmn_name}",
                f"def_program_status_{slug}",
                dmn_name.replace(".dmn", ""),
                f"https://studentjourneymatrix.local/program_{slug}",
                [rules_from_bpmn(f"3. student_program_status/{stem}.bpmn", dec_id, f"Program Status — {title}")],
            )
        )

    # Parallel FSM — two axes in one file
    s_spec, p_spec = parallel_fsm_decisions(
        "4. combined_lifecycle/3. parallel_student_program_constrained_fsm.bpmn"
    )

    specs.extend(
        [
            DmnSpec(
                "4. combined_lifecycle/DMN applicant_status 1__high_level_lifecycle_overview.dmn",
                "def_1__high_level_lifecycle_overview",
                "DMN applicant_status 1__high_level_lifecycle_overview",
                "https://studentjourneymatrix.local/1__high_level_lifecycle_overview",
                [high_level_rules()],
            ),
            DmnSpec(
                "4. combined_lifecycle/DMN applicant_status 2__applicant_to_student_bridge.dmn",
                "def_2__applicant_to_student_bridge",
                "DMN applicant_status 2__applicant_to_student_bridge",
                "https://studentjourneymatrix.local/2__applicant_to_student_bridge",
                [
                    rules_from_bpmn(
                        "4. combined_lifecycle/2. applicant_to_student_bridge.bpmn",
                        "decision_status_2_applicant_to_student_bridge",
                        "Applicant-to-Student Bridge — Part 2",
                    )
                ],
            ),
            DmnSpec(
                "4. combined_lifecycle/DMN applicant_status 3__parallel_student_program_constrained_fsm.dmn",
                "def_3__parallel_student_program_constrained_fsm",
                "DMN applicant_status 3__parallel_student_program_constrained_fsm",
                "https://studentjourneymatrix.local/3__parallel_student_program_constrained_fsm",
                [s_spec, p_spec],
            ),
            DmnSpec(
                "4. combined_lifecycle/DMN applicant_status 4__cross_impact_rules.dmn",
                "def_4__cross_impact_rules",
                "DMN applicant_status 4__cross_impact_rules",
                "https://studentjourneymatrix.local/4__cross_impact_rules",
                [cross_impact_rules("decision_cross_impact_rules_part4", "Cross-Impact (COMBO) Rules — Part 4", True)],
            ),
            DmnSpec(
                "4. combined_lifecycle/DMN applicant_status 5__student_status_vs_program_status_interaction.dmn",
                "def_5__student_status_vs_program_status_interaction",
                "DMN applicant_status 5__student_status_vs_program_status_interaction",
                "https://studentjourneymatrix.local/5__student_status_vs_program_status_interaction",
                [
                    cross_impact_rules(
                        "decision_cross_impact_rules_part5",
                        "Student-Status vs Program-Status Interaction — Part 5",
                        False,
                    )
                ],
            ),
            DmnSpec(
                "4. combined_lifecycle/DMN applicant_status 6__combination_matrix_validation.dmn",
                "def_6__combination_matrix_validation",
                "DMN applicant_status 6__combination_matrix_validation",
                "https://studentjourneymatrix.local/6__combination_matrix_validation",
                [combination_matrix_decision()],
            ),
        ]
    )
    return specs


def apply_part2b_label_fix(rules: list[Rule]) -> None:
    for r in rules:
        if "A5.1" in r.current and "(IS/GS/SOL)" not in r.current:
            r.current = "A5.1 — Probationary (IS/GS/SOL) [OAS]"
        if r.nxt.startswith("A5.1") and "(IS/GS/SOL)" not in r.nxt:
            r.nxt = "A5.1 — Probationary (IS/GS/SOL) [OAS]"


def main() -> None:
    written = 0
    for spec in build_specs():
        for dec in spec.decisions:
            apply_part2b_label_fix(dec.rules)
        out = ROOT / spec.rel_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_dmn(spec), encoding="utf-8")
        rule_count = sum(len(d.rules) for d in spec.decisions)
        print(f"{spec.rel_path}: {len(spec.decisions)} decision(s), {rule_count} rules")
        written += 1
    print(f"\nDone. {written} DMN files written.")


if __name__ == "__main__":
    main()
