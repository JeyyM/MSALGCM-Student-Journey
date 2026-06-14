# Applicant / Admission Application Status Diagrams

Finite-state-machine diagrams for the admission funnel (`A*` codes). Source: [`../../diagram_planning/applicant_status_transition_table.md`](../../diagram_planning/applicant_status_transition_table.md).

## Parts

| File | Segment | States |
|---|---|---|
| [`applicant_status_part_1_account_to_submission.md`](applicant_status_part_1_account_to_submission.md) | Account → draft → submission → requirements loop | A0, A1.0, A2.0, A2.1 |
| [`applicant_status_part_2_evaluation_to_decision.md`](applicant_status_part_2_evaluation_to_decision.md) | Requirements/exam evaluation, then admission results | A2.0–A4.3, A5.0–A5.5 (two diagrams) |
| [`applicant_status_part_3_acceptance_to_student.md`](applicant_status_part_3_acceptance_to_student.md) | Offer → reserved → admitted → student hand-off | A5.x, A6.0, A7.0, A7.1, S1.0 |
| [`applicant_status_part_4_terminal_or_exception_states.md`](applicant_status_part_4_terminal_or_exception_states.md) | Rejections, cancellations, deferral, withdrawal | A3.2, A4.2, A5.5, A6.1, A7.2, A8.0, A8.1 |

## Excluded across all applicant diagrams

- `A3.3 Exam Not Required`, `A9.0 Inactive` — strikethrough/deprecated.
- `A5.4 Reconsidered` and its edges — Low certainty (appeal revives a terminal state).

## Reading order

Part 1 → Part 2 → Part 3 → Part 4. Part 3 ends at the hand-off into Student Status; the full student lifecycle continues in [`../student_status/`](../student_status/README.md).
