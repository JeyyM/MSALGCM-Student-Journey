# Diagram Plan: Student Status (Master)

## Purpose

Coordinate **three** student-status diagrams (STU-01 through STU-03) covering `S*` codes after admission hand-off.

## Source Files

- [`../student_status_flow.md`](../student_status_flow.md)
- [`student_status_transition_table.md`](student_status_transition_table.md)
- [`../decisions.md`](../decisions.md)

## Diagram parts

| Part file | Diagram ID | Focus |
|---|---|---|
| [`student_status_part_1_active_and_enrollment.md`](student_status_part_1_active_and_enrollment.md) | STU-01 | S1.0, S2.0, S2.1 |
| [`student_status_part_2_loa_awol_suspension.md`](student_status_part_2_loa_awol_suspension.md) | STU-02 | S2.2, S2.3, S3.1, S3.2, returnee |
| [`student_status_part_3_exit_and_graduation.md`](student_status_part_3_exit_and_graduation.md) | STU-03 | S4.0, S4.1, S4.2 |

## Excluded globally

| Item | Reason |
|---|---|
| S3.5, S3.6, S3.7 | Strikethrough |
| STU-T050, T051 | Low/Unknown |
| Graduated-with-clearance-hold | Not modeled |

## Recommended Mermaid Type

`stateDiagram-v2`

## Build order

STU-01 first (links from APP-05), then STU-03, then **STU-02 last** (most unclear).

## Open Questions

See [`unclear_transitions.md`](unclear_transitions.md) — LOA/AWOL/suspension return paths.
