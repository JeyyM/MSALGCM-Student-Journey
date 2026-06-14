# Diagram Plan: Student Program Status (Master)

## Purpose

Coordinate **three** program-status diagrams (PRG-01 through PRG-03) for canonical `P*` codes.

## Source Files

- [`../student_program_status_flow.md`](../student_program_status_flow.md)
- [`student_program_status_transition_table.md`](student_program_status_transition_table.md)
- [`../decisions.md`](../decisions.md)

## Diagram parts

| Part file | Diagram ID | Focus |
|---|---|---|
| [`student_program_status_part_1_good_standing_to_probation.md`](student_program_status_part_1_good_standing_to_probation.md) | PRG-01 | P1.0, P1.1 entry and lift |
| [`student_program_status_part_2_ineligible_and_snas.md`](student_program_status_part_2_ineligible_and_snas.md) | PRG-02 | P1.2, P1.3, P1.4 |
| [`student_program_status_part_3_graduation_and_terminal.md`](student_program_status_part_3_graduation_and_terminal.md) | PRG-03 | P2.0, P3.0, P3.1 |

## Excluded globally

| Item | Reason |
|---|---|
| Under Evaluation | Strikethrough |
| PRG-T060 SAP numeric threshold | Deferred |
| PRG-T061, T062 | Unknown |

## Recommended Mermaid Type

`stateDiagram-v2`

## Open Questions

- P1.3 IS-only — annotate on state label
- SAP failure → P1.4 vs voluntary withdraw
