# Diagram Plan: STU-01 — Active and Enrollment

## Purpose

Show normal student activity after admission: without enrollment → active enrolled → residency cycle.

## Source Files

- [`../student_status_flow.md`](../student_status_flow.md)
- [`student_status_transition_table.md`](student_status_transition_table.md)
- [`applicant_status_part_3_acceptance_to_student.md`](applicant_status_part_3_acceptance_to_student.md) (entry from APP-05)

## Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| S1.0 | S1_0 | S1.0 - Active - Without Enrollment | Active | Entry from A7.x |
| S2.0 | S2_0 | S2.0 - Active | Active | |
| S2.1 | S2_1 | S2.1 - Active - Residency | Active | UG/GS/SOL only |

## Included Transitions

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| STU-T001 / APP-T048 | A7_0 | S1_0 | Admitted (not enrolled) | High | Shown only if STU-01 includes entry; else start at S1_0 |
| STU-T010 | S1_0 | S2_0 | Enrolled / enlisted | High | |
| STU-T011 | S2_0 | S2_1 | Registered for residency | High | |
| STU-T012 | S2_1 | S2_0 | Re-enrolled | Medium | |
| STU-T040 | S2_0 | S2_0 | Term break (not enrolled yet) | Medium | **Optional** self-loop — use note instead if cluttered |

## Excluded States or Transitions

| Item | Reason |
|---|---|
| S2.2, S2.3, S3.x, S4.x | STU-02, STU-03 |
| STU-T020 (S1_0 → AWOL) | Medium — defer to STU-02 |

## Diagram Boundaries

**Includes:** S1.0 ↔ S2.0 ↔ S2.1 core enrollment path.  
**Excludes:** Leave, AWOL, exit, graduation.

## Recommended Mermaid Type

`stateDiagram-v2`

## Complexity Safeguards

- 3 states (+ optional `[*]` from admission) — minimal.
- Omit STU-T040 self-loop in v1 diagram; describe in caption.

## Open Questions

- Include admission entry node or assume STU-01 starts at S1_0 only?
