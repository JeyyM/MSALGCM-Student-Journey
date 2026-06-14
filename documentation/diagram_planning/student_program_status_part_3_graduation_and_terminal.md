# Diagram Plan: PRG-03 — Graduation and Terminal Program Outcomes

## Purpose

Two-step graduation (Candidate → Graduated) and Incomplete on university exit.

## Source Files

- [`../student_program_status_flow.md`](../student_program_status_flow.md)
- [`student_program_status_transition_table.md`](student_program_status_transition_table.md)

## Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| P1.0 | P1_0 | P1.0 - Eligible | Active | Entry (only documented path to P2.0) |
| P2.0 | P2_0 | P2.0 - Candidate for Graduation | Active | |
| P3.0 | P3_0 | P3.0 - Graduated [Terminal] | Terminal | |
| P3.1 | P3_1 | P3.1 - Incomplete [Terminal] | Terminal | |

## Included Transitions

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| PRG-T030 | P1_0 | P2_0 | First graduation check passed | High | |
| PRG-T031 | P2_0 | P3_0 | Final check + commencement | High | |
| PRG-T040 | P1_0 | P3_1 | University exit | High | |
| PRG-T044 | P2_0 | P3_1 | University exit | High | |

## Optional collapsed edges (caption only for v1)

PRG-T041, T042, T043 from P1_1, P1_2, P1_3 → P3_1 — **High** per table; add in v2 or footnote "also from P1.1/P1.2/P1.3."

## Excluded States or Transitions

| Item | Reason |
|---|---|
| PRG-T062 (Probationary → P2.0) | Unknown |
| PRG-T061 (P2_0 revert) | Unknown |
| P3_0 → alumni actions | Not in matrix |

## Diagram Boundaries

**Includes:** Graduation chain and exit-incomplete from P1_0 (and P2_0).  
**Excludes:** Link to STU-T028 (all P3.0 → S4.0) — reference COMBO-T001 in caption.

## Recommended Mermaid Type

`stateDiagram-v2`

## Complexity Safeguards

- 4 states, 4–7 edges — clear linear graduation spine + exit branch.

## Open Questions

- Include all exit sources to P3_1 in v1 or footnote only?
