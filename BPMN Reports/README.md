# BPMN Reports — Student Journey Matrix

Analysis and reporting for the **BPMN 2.0** models derived from the DLSU Student Journey Matrix. Each report matches a diagram in [`BPMN Code/`](../BPMN%20Code/) and the original Mermaid source in [`final mermaid code/`](../final%20mermaid%20code/) — same folders, same file names (`.md` here, `.bpmn` there).

---

## Why BPMN for this project

The Student Journey Matrix describes **who moves through which status, triggered by which event, under which office’s responsibility**. BPMN is a good fit because it models:

- **Process flow** — ordered steps and hand-offs between parties
- **Swimlanes** — Applicant, OAS/Admissions, Registrar, Program Office, etc.
- **Decision points** — exclusive gateways (XOR) for evaluation branches
- **Start / end events** — journey entry and terminal outcomes

What BPMN does **not** replace in this project:

- **DMN** — the combination tab V(S,P) is decision-table logic, not process flow (see DMN deliverable separately)
- **Full state-machine semantics** — our status codes behave like an FSM; we represent states as **tasks** in BPMN for readability, which is a deliberate modeling choice

---

## Conversion pipeline

```
Excel / documentation  →  Mermaid (.mmd)  →  BPMN 2.0 XML (.bpmn)  →  These reports (.md)
                         final mermaid code    BPMN Code              BPMN Reports
```

Generation script: [`BPMN Code/generate_bpmn.py`](../BPMN%20Code/generate_bpmn.py)

---

## Notation mapping (Mermaid → BPMN)

| Mermaid (source) | BPMN (this project) | Rationale |
|------------------|---------------------|-----------|
| State box (`A2.0`, `S2.0`, …) | **Task** (user or service) | Status = achieved milestone; lane shows who owns the update |
| `[*]` entry | **Start event** | Journey begins or diagram boundary |
| Terminal state | **End event** | No further transitions in this slice |
| Branching transitions | **Exclusive gateway (XOR)** | Mutually exclusive outcomes (e.g. exam required vs exempted) |
| Arrow label | **Sequence flow** name | Preserves workbook transition trigger text |
| Parallel S/P tracks | **Separate swimlanes** | Student and Program dimensions run in parallel |

---

## Swimlane color legend

| Lane | Color | Role |
|------|-------|------|
| Applicant | Blue | Account, application, exam, fees |
| OAS / Admissions | Green | Requirements, evaluation, offers |
| Registrar / Enrollment | Purple | Student record, enrollment status |
| Student | Amber | Student-initiated actions post-admission |
| Program Office | Cyan | Academic standing per program |
| Disciplinary | Red | Suspension, disqualification |
| Validation | Gray | V(S,P) combination checks |
| Gateways | Yellow | Decision points |
| Start / End | Green / Red tint | Entry and terminal |

Colors embed in BPMN XML for **BPMN.io** / **Camunda**; **Lucidchart** may strip them on import.

---

## Report index (17 diagrams)

### Applicant status (`A` codes)

| Report | BPMN | Summary |
|--------|------|---------|
| [part_1_account_to_submission](applicant_status/part_1_account_to_submission.md) | [`.bpmn`](../BPMN%20Code/applicant_status/part_1_account_to_submission.bpmn) | A0 → A2.x account and submission |
| [part_2a_exam_evaluation](applicant_status/part_2a_exam_evaluation.md) | [`.bpmn`](../BPMN%20Code/applicant_status/part_2a_exam_evaluation.bpmn) | A2.0 → A4.x evaluation & exam |
| [part_2b_admission_results](applicant_status/part_2b_admission_results.md) | [`.bpmn`](../BPMN%20Code/applicant_status/part_2b_admission_results.bpmn) | Admission decision A5.x |
| [part_3_acceptance_to_student](applicant_status/part_3_acceptance_to_student.md) | [`.bpmn`](../BPMN%20Code/applicant_status/part_3_acceptance_to_student.bpmn) | A5.x → A7.x → S1.0 bridge |
| [part_4_terminal_or_exception_states](applicant_status/part_4_terminal_or_exception_states.md) | [`.bpmn`](../BPMN%20Code/applicant_status/part_4_terminal_or_exception_states.bpmn) | Cancellations, deferrals, dead ends |

### Student status (`S` codes)

| Report | BPMN | Summary |
|--------|------|---------|
| [part_1_active_and_enrollment](student_status/part_1_active_and_enrollment.md) | [`.bpmn`](../BPMN%20Code/student_status/part_1_active_and_enrollment.bpmn) | S1.0 → S2.0 enrollment |
| [part_2_residency_and_loa](student_status/part_2_residency_and_loa.md) | [`.bpmn`](../BPMN%20Code/student_status/part_2_residency_and_loa.bpmn) | Residency, LOA, prolonged leave |
| [part_3_awol_suspension_and_exit](student_status/part_3_awol_suspension_and_exit.md) | [`.bpmn`](../BPMN%20Code/student_status/part_3_awol_suspension_and_exit.bpmn) | AWOL, suspension, exit |
| [part_4_graduation_and_terminal_states](student_status/part_4_graduation_and_terminal_states.md) | [`.bpmn`](../BPMN%20Code/student_status/part_4_graduation_and_terminal_states.bpmn) | Graduation and terminal S codes |

### Program status (`P` codes)

| Report | BPMN | Summary |
|--------|------|---------|
| [part_1_good_standing_and_probation](student_program_status/part_1_good_standing_and_probation.md) | [`.bpmn`](../BPMN%20Code/student_program_status/part_1_good_standing_and_probation.bpmn) | P1.0 ↔ P1.1 |
| [part_2_snas_sap_and_ineligible](student_program_status/part_2_snas_sap_and_ineligible.md) | [`.bpmn`](../BPMN%20Code/student_program_status/part_2_snas_sap_and_ineligible.bpmn) | SNAS, SAP, ineligible |
| [part_3_graduation_and_terminal_states](student_program_status/part_3_graduation_and_terminal_states.md) | [`.bpmn`](../BPMN%20Code/student_program_status/part_3_graduation_and_terminal_states.bpmn) | Graduation candidacy → P3.x |

### Combined lifecycle

| Report | BPMN | Summary |
|--------|------|---------|
| [high_level_lifecycle_overview](combined_lifecycle/high_level_lifecycle_overview.md) | [`.bpmn`](../BPMN%20Code/combined_lifecycle/high_level_lifecycle_overview.bpmn) | End-to-end journey |
| [applicant_to_student_bridge](combined_lifecycle/applicant_to_student_bridge.md) | [`.bpmn`](../BPMN%20Code/combined_lifecycle/applicant_to_student_bridge.bpmn) | A7.x → S1.0 / P1.x hand-off |
| [student_status_vs_program_status_interaction](combined_lifecycle/student_status_vs_program_status_interaction.md) | [`.bpmn`](../BPMN%20Code/combined_lifecycle/student_status_vs_program_status_interaction.bpmn) | Cross-impact rules |
| [cross_impact_rules](combined_lifecycle/cross_impact_rules.md) | [`.bpmn`](../BPMN%20Code/combined_lifecycle/cross_impact_rules.bpmn) | COMBO-T001–T005 |
| [parallel_student_program_constrained_fsm](combined_lifecycle/parallel_student_program_constrained_fsm.md) | [`.bpmn`](../BPMN%20Code/combined_lifecycle/parallel_student_program_constrained_fsm.bpmn) | Parallel S/P + validation |

---

## Overall BPMN assessment (for Project 1 Part 2)

### What BPMN captures well

1. **Multi-party workflows** — admission involves Applicant + OAS + Registrar; swimlanes make ownership visible.
2. **Decision branching** — exam required / exempted / not qualified maps cleanly to XOR gateways.
3. **Granular readability** — 17 small diagrams instead of one unreadable mega-diagram.
4. **Tool interchange** — `.bpmn` imports into Lucidchart, BPMN.io, Camunda for review and presentation.

### Challenges and workarounds

| Challenge | Workaround used |
|-----------|-----------------|
| Source is a **state machine**, not a classic business process | Model each **status as a task**; sequence flows = transitions; accept that “being in A2.0” is shown as completing an “A2.0” task |
| **Parallel** Student + Program tracks | Separate swimlanes in combined diagrams; no single-token BPMN semantics |
| **91-cell combination matrix** | Not drawn as BPMN edges; delegated to **DMN** + validation lane stub |
| **Cross-dimension forcing rules** (COMBO-T00x) | Shown as inter-lane sequence flows in combined diagrams; full matrix still in DMN |
| **Loops** (A2.0 ↔ A2.1 resubmit) | Modeled as sequence flows back to earlier task; layout may need manual tidy in Lucid |
| **Lucid strips colors** | Use BPMN.io for colored export, or manual styling in Lucid |

### Recommended pairing with DMN

| BPMN element | DMN companion |
|--------------|---------------|
| Task “Validate V(S,P) combination” | Decision table: inputs = S code, P code; output = Valid / Invalid / Yes? |
| Gateway “Admission decision” | Optional DMN for cutoff/probationary rules; gateway alone is sufficient at checkpoint level |

---

## How to use these reports

- **Milestone checkpoint** — open the report + BPMN file for the section you are presenting.
- **Write-up (b.1 challenges / b.2 recommendations)** — pull from “BPMN strengths & limitations” in each report and the overall assessment above.
- **Traceability** — each report links to Mermaid source, BPMN XML, and workbook status codes.
