# BPMN Report — Cross-Impact Rules (COMBO-T001–T005)

**Matching files:** [`cross_impact_rules.bpmn`](../BPMN%20Code/combined_lifecycle/cross_impact_rules.bpmn) · [`cross_impact_rules.mmd`](../final%20mermaid%20code/combined_lifecycle/cross_impact_rules.mmd)

---

## Purpose

Documents the **named crossover transitions** from the Student Journey Matrix combination analysis — explicit COMBO rule IDs for traceability to `documentation/status_combination_rules.md` and the lifecycle validator.

---

## Rules (COMBO IDs)

| ID | Trigger | Effect |
|----|---------|--------|
| **COMBO-T001** | All programs P3.0 Graduated | Student S4.0 Graduated |
| **COMBO-T003** | Student university exit, program still active | Program P3.1 Incomplete |
| **COMBO-T004** | P1.4 Ineligible + shift application pending | Student S1.0 Without Enrollment |
| **COMBO-T005** | Shift approved | Student S2.0 Active |

*(COMBO-T002 not used in current model set — reserved in workbook.)*

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| COMBO labels on flows | Sequence flow names + task names | Audit trail to documentation |
| T004 → T005 chain | Sequential service tasks | Shift workflow stub |
| Subset of parallel FSM | Standalone for minimal draw.io/BPMN insert | Per Mermaid file comment |

---

## Swimlanes

| Lane | COMBO roles |
|------|-------------|
| **Program Office** | T001 trigger, T003 effect, T004 trigger |
| **Student Records** | T001 effect, T003 trigger, T004/T005 effects |

---

## BPMN strengths here

- **Named rules** support academic write-up: “BPMN shows process hand-offs; DMN validates all other pairs.”
- Minimal diagram for handouts.

## Limitations

- Not a substitute for **DMN V(S,P)** — only forced pairs.
- Executable BPMN would need business rule tasks calling DMN for non-forced validation before each transition.
- T002 gap should be noted in open questions if workbook adds it later.

---

## Related diagrams

- **Unlabeled version:** [student_status_vs_program_status_interaction](student_status_vs_program_status_interaction.md)
- **Integrated:** [parallel_student_program_constrained_fsm](parallel_student_program_constrained_fsm.md)

## DMN pairing

All **non-COMBO** (S,P) pairs → decision table **ValidateCombination**; COMBO rules can be **override rows** in same DMN or separate decision.
