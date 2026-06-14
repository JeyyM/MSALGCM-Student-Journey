# Diagram Plan: APP-04 & APP-05 — Acceptance and Applicant-to-Student Hand-off

## Purpose

Two diagrams:

1. **APP-04** — Official acceptance: Reserved through admitted, provisional, deferred, and terminal cancellations.
2. **APP-05** — Minimal cross-dimension hand-off from admission complete to student entry (`S1.0`).

Entry assumed from **A5.0 / A5.1 / A5.2** (and optionally A5.4 if ever confirmed) from APP-03.

## Source Files

- [`../applicant_status_flow.md`](../applicant_status_flow.md)
- [`../student_status_flow.md`](../student_status_flow.md) (APP-05 only)
- [`applicant_status_transition_table.md`](applicant_status_transition_table.md)
- [`student_status_transition_table.md`](student_status_transition_table.md) — STU-T001, T002

---

## APP-04: Official Acceptance

### Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| A6.0 | A6_0 | A6.0 - Reserved | Transitional | |
| A6.1 | A6_1 | A6.1 - Cancelled (no acceptance fee) [Terminal] | Terminal | |
| A7.0 | A7_0 | A7.0 - Officially Admitted [Terminal for admission] | Terminal | Hand-off |
| A7.1 | A7_1 | A7.1 - Provisionally Admitted | Transitional | |
| A7.2 | A7_2 | A7.2 - Deferred | Transitional | |
| A8.0 | A8_0 | A8.0 - Cancelled (no reqs) [Terminal] | Terminal | |
| A8.1 | A8_1 | A8.1 - Cancelled - Withdrawal | Transitional | |

### Included Transitions

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| APP-T033–T035 | A5_x | A6_0 | Official acceptance fee paid/waived | High | Inbound from APP-03 |
| APP-T037–T039 | A5_x | A6_1 | Did not pay fee | High | Terminals |
| APP-T041 | A6_0 | A7_0 | Requirements complete | High | |
| APP-T042 | A6_0 | A7_1 | Requirements pending | High | |
| APP-T043 | A7_1 | A7_0 | Requirements completed | Medium | |
| APP-T045 | A7_1 | A8_0 | 1 year lapsed | High | Terminal |
| APP-T046 | A7_0 | A8_1 | Withdrew in admission term | High | |
| APP-T047 | A7_1 | A8_1 | Withdrew in admission term | High | |

### Excluded from APP-04 (final)

| Item | Reason |
|---|---|
| APP-T052 (A6_0 → A7_2) | Medium; references S1.0 — defer to APP-05 or STU-01 |
| APP-T050, T051 (direct S2.0) | Medium duplicate-column issue |

### APP-04 Boundaries

**Includes:** A6.0 through A8.1.  
**Excludes:** Student lifecycle beyond hand-off node A7_0/A7_1.

---

## APP-05: Applicant → Student Hand-off

### Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| A7.0 | A7_0 | A7.0 - Officially Admitted | Terminal (admission) | From APP-04 |
| A7.1 | A7_1 | A7.1 - Provisionally Admitted | Transitional | Optional entry |
| S1.0 | S1_0 | S1.0 - Active - Without Enrollment | Active | Primary hand-off |
| S2.0 | S2_0 | S2.0 - Active | Active | **Exclude** unless APP-T050 confirmed |

### Included Transitions

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| APP-T048 | A7_0 | S1_0 | Becomes student (not enrolled) | High | **Primary edge** |
| APP-T049 | A7_1 | S1_0 | Provisional → student | High | |
| STU-T010 | S1_0 | S2_0 | Enrolled / enlisted | High | Bridge to STU-01 |

### Excluded

| Item | Reason |
|---|---|
| APP-T050, T051 | Direct A7.x → S2.0 — Medium; defer |
| Program status P1.0/P1.1 | Separate PRG-01 entry |

### APP-05 Boundaries

**Only diagram** that mixes `A*` and `S*` (except LIFE-01 overview). Keep to **3–4 nodes**.

## Recommended Mermaid Type

`stateDiagram-v2`

## Complexity Safeguards

- APP-04: 7 states, ~12 transitions — acceptable.
- APP-05: 3–4 states max.
- Do not add P1.0/P1.1 on APP-05 — link in documentation text to PRG-01.

## Open Questions

- A7.1 self-loop (APP-T061) — omit from diagram.
- A6.0 → A7.2 deferral without S1.0 path — confirm before adding.
- A8.0 student status mapping — not in Post-M3 hand-off table clearly.
