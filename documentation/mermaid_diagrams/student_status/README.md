# Student Status Diagrams

Finite-state-machine diagrams for the student lifecycle (`S*` codes), covering a person's overall standing in the University after admission. Source: [`../../diagram_planning/student_status_transition_table.md`](../../diagram_planning/student_status_transition_table.md).

## Parts

| File | Segment | States |
|---|---|---|
| [`student_status_part_1_active_and_enrollment.md`](student_status_part_1_active_and_enrollment.md) | Admission hand-off → active enrolled | S1.0, S2.0 |
| [`student_status_part_2_residency_and_loa.md`](student_status_part_2_residency_and_loa.md) | Residency, LOA, prolonged leave, returnee | S2.0, S2.1, S2.2, S2.3, S1.0 |
| [`student_status_part_3_awol_suspension_and_exit.md`](student_status_part_3_awol_suspension_and_exit.md) | AWOL, suspension, exits | S2.0, S1.0, S3.1, S3.2, S4.1, S4.2 |
| [`student_status_part_4_graduation_and_terminal_states.md`](student_status_part_4_graduation_and_terminal_states.md) | Graduation and all terminal student outcomes | S2.0, S4.0, S4.1, S4.2 |

## Normal vs exception movement

- **Normal/active movement** lives in Parts 1–2 (enrollment, residency, approved leave).
- **Exception/exit movement** lives in Parts 3–4 (AWOL, suspension, graduation, exits).

## Excluded across all student diagrams

- `S3.5 Exited - Under Exclusion`, `S3.6 Exited - Expelled`, `S3.7 Inactive - Transferred` — strikethrough; consolidated into `S4.2` or dropped.
- `STU-T050` (S2.2 → S2.3) Low and `STU-T051` (S2.1 → S2.2) Unknown — not drawn.

## Confirmation needed

Part 2 and Part 3 depend on LOA/AWOL/suspension rules that are flagged in [`../../open_questions.md`](../../open_questions.md). Returnee and suspension-return edges are **Medium/Tentative**. Review before treating as authoritative.
