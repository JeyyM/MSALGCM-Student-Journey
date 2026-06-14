# Diagram Plan: STU-02 — LOA, AWOL, and Suspension

## Purpose

Show leave-of-absence, prolonged leave, AWOL, suspension, and returnee paths. **Highest uncertainty** — validate with stakeholders before final Mermaid.

## Source Files

- [`../student_status_flow.md`](../student_status_flow.md)
- [`student_status_transition_table.md`](student_status_transition_table.md)
- [`unclear_transitions.md`](unclear_transitions.md)

## Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| S2.0 | S2_0 | S2.0 - Active | Active | Hub state |
| S1.0 | S1_0 | S1.0 - Active - Without Enrollment | Active | Returnee target |
| S2.2 | S2_2 | S2.2 - Active - Under LOA | Active | On approved LOA |
| S2.3 | S2_3 | S2.3 - Inactive - Prolonged Leave | Inactive | Post-M3 — keep |
| S3.1 | S3_1 | S3.1 - Inactive - AWOL | Inactive | |
| S3.2 | S3_2 | S3.2 - Inactive - Suspended | Inactive | |

## Included Transitions (High certainty only for v1)

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| STU-T013 | S2_0 | S2_2 | LOA approved (within max) | High | |
| STU-T014 | S2_0 | S2_3 | LOA exceeds limits | High | |
| STU-T018 | S2_0 | S3_1 | Did not enroll; no LOA | High | |
| STU-T021 | S2_0 | S3_2 | Disciplinary suspension | High | |
| STU-T027 | S3_2 | S2_0 | Suspension served | Medium | |
| STU-T015 | S2_2 | S1_0 | Returnee approved | Medium | |
| STU-T016 | S2_3 | S1_0 | Returnee approved | Medium | |
| STU-T017 | S3_1 | S1_0 | Returnee approved | Medium | |

## Excluded States or Transitions (v1 final diagram)

| Item | Reason |
|---|---|
| STU-T050 (S2_2 → S2_3) | Low |
| STU-T051 (S2_1 → S2_2) | Unknown |
| STU-T019, T020 (Residency/S1_0 → AWOL) | Medium — optional v2 |
| STU-T040 (S2_0 self-loop) | Medium — use footnote |

## Diagram Boundaries

**Includes:** Disruptions from S2_0 and return to S1_0.  
**Excludes:** S2_1 residency (except as optional AWOL source in v2), S4.x exits (STU-03).

## Recommended Mermaid Type

`stateDiagram-v2` — if too many cross-links, split into:
- STU-02a: LOA / Prolonged Leave
- STU-02b: AWOL / Suspension

## Complexity Safeguards

- 6 states — at limit; consider STU-02a/02b split if >15 edges.
- Do **not** diagram LOA campus access on this chart.
- Returnee edges (Medium) — use dashed style or `[Tentative]` in draft only.

## Open Questions

- LOA vs Prolonged Leave: both from S2_0 only?
- AWOL grace period vs STU-T040 self-loop
- Suspension return: S1_0 or S2_0?
- **Defer final diagram** until [`unclear_transitions.md`](unclear_transitions.md) LOA section answered
