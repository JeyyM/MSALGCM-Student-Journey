# Diagram Plan: STU-03 — Exit and Graduation

## Purpose

Show terminal and near-terminal student outcomes: graduated, exited on good standing, permanent disqualification. Many inbound edges from active/inactive states.

## Source Files

- [`../student_status_flow.md`](../student_status_flow.md)
- [`student_status_transition_table.md`](student_status_transition_table.md)

## Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| S2.0 | S2_0 | S2.0 - Active | Active | Primary source |
| S4.0 | S4_0 | S4.0 - Graduated | Inactive | Not labeled terminal in tab — use `[Terminal?]` in label |
| S4.1 | S4_1 | S4.1 - Exited on Good Standing [Terminal] | Terminal | |
| S4.2 | S4_2 | S4.2 - Exited - Permanent Disqualification [Terminal] | Terminal | |

## Included Transitions

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| STU-T028 | S2_0 | S4_0 | All programs graduated | High | Triggered by P3.0 on all programs |
| STU-T029 | S2_0 | S4_1 | University exit submitted | High | |
| STU-T036 | S2_0 | S4_2 | Disciplinary disqualification | High | |
| STU-T037 | S3_2 | S4_2 | Disciplinary disqualification | High | |

## Optional inbound edges (collapse for readability)

Document in table but **group** in diagram as "From other student states" unless full diagram needed:

| Transition ID | From | To | Label | Certainty |
|---|---|---|---|---|
| STU-T030–T035 | S2_1, S1_0, S2_2, S2_3, S3_1, S3_2 | S4_1 | University exit | High/Medium |

**Recommendation:** STU-03 v1 shows only S2_0 → S4.x plus note: "Same exit transitions from S2_2, S2_3, S3_1, S3_2, S2_1 per transition table."

## Excluded States or Transitions

| Item | Reason |
|---|---|
| Clearance-hold graduated | Not modeled |
| S4_0 → further study | Open question Notes #6 |
| S3.5–S3.7 | Deprecated |

## Diagram Boundaries

**Includes:** Outcomes S4.0, S4.1, S4.2 and primary triggers.  
**Excludes:** Program graduation detail (PRG-03); combination rules.

## Recommended Mermaid Type

`stateDiagram-v2`

## Complexity Safeguards

- 4–5 nodes in v1 (hub S2_0 + 3 terminals).
- Collapse multi-source exit edges per recommendation above.

## Open Questions

- Label S4_0 as `[Terminal]` or `[Terminal?]`?
- Show COMBO-T001 dependency on P3.0 in caption only?
