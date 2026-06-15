# Diagram Plan: Applicant Status (Master)

## Purpose

Master blueprint for splitting the admission application lifecycle (`A*` codes) into **five** readable diagrams (APP-01 through APP-05). This file coordinates the part plans; it does not contain Mermaid output.

## Source Files

- [`../applicant_status_flow.md`](../applicant_status_flow.md)
- [`applicant_status_transition_table.md`](applicant_status_transition_table.md)
- [`../decisions.md`](../decisions.md)
- [`unclear_transitions.md`](unclear_transitions.md)

## Diagram parts

| Part file | Diagram ID | States (approx.) | Transitions (approx.) |
|---|---|---|---|
| [`applicant_status_part_1_account_to_submission.md`](applicant_status_part_1_account_to_submission.md) | APP-01 | 4 | 6 |
| [`applicant_status_part_2_evaluation_to_decision.md`](applicant_status_part_2_evaluation_to_decision.md) | APP-02, APP-03 | 8 + 8 (13 combined) | 14 + 16 (30 combined) |
| [`applicant_status_part_3_acceptance_to_student.md`](applicant_status_part_3_acceptance_to_student.md) | APP-04, APP-05 | 8 + 3 | 12 + 3 |

## Excluded globally (all applicant diagrams)

| Item | Reason |
|---|---|
| `A3.3`, `A9.0` | Strikethrough — [`../decisions.md`](../decisions.md) |
| APP-T032, T036, T040 (Reconsidered) | Low certainty — defer |
| Applicant Active/Inactive row | Deprecated |

## Recommended Mermaid Type

`stateDiagram-v2` for all APP-* diagrams.

## Complexity Safeguards

- Maximum **12 states** per diagram (APP-03 may split offer results if crowded).
- Maximum **20 transitions** per diagram.
- APP-02 and APP-03 share a source file but produce **two separate** `.mmd` files.
- Only APP-05 crosses into `S*` codes (minimal hand-off).

## Open Questions

See part files and [`unclear_transitions.md`](unclear_transitions.md) — especially reconsideration loop, A7.1 provisioning, and direct A7.x → S2.0 enrollment.
