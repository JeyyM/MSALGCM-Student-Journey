# Student Program Status Diagrams

Finite-state-machine diagrams for academic standing within a program (`P*` codes), tracked **per program**. Source: [`../../diagram_planning/student_program_status_transition_table.md`](../../diagram_planning/student_program_status_transition_table.md).

These use the **canonical** Post-M3 codes: `P1.3 = Strict Probationary`, `P1.4 = Ineligible`.

## Parts

| File | Segment | States |
|---|---|---|
| [`student_program_status_part_1_good_standing_and_probation.md`](student_program_status_part_1_good_standing_and_probation.md) | Entry; eligible ↔ probationary | P1.0, P1.1 |
| [`student_program_status_part_2_snas_sap_and_ineligible.md`](student_program_status_part_2_snas_sap_and_ineligible.md) | SNAS, Strict Probationary (SAP, IS), Ineligible | P1.0–P1.4 |
| [`student_program_status_part_3_graduation_and_terminal_states.md`](student_program_status_part_3_graduation_and_terminal_states.md) | Candidate → Graduated; Incomplete | P1.0, P2.0, P3.0, P3.1 |

## Excluded across all program diagrams

- `Under Evaluation` (M3 shifting status) — strikethrough; shifting is a process.
- SAP numeric grade thresholds ("below 75") — deferred; not placed on arrows.
- `PRG-T061` (P2.0 → P1.0) and `PRG-T062` (P1.1 → P2.0) — Unknown; not drawn.

## Note on Strict Probationary

`P1.3 Strict Probationary` is **IS only** and is labeled as such on the state. Its grade criteria are unconfirmed (see [`../../open_questions.md`](../../open_questions.md)).
