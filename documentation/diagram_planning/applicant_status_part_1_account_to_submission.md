# Diagram Plan: APP-01 — Account to Submission

## Purpose

Show the earliest admission funnel: account creation, draft, submission, and the requirements complete/deficiencies loop. **Does not** include exam, results, or acceptance.

## Source Files

- [`../applicant_status_flow.md`](../applicant_status_flow.md)
- [`applicant_status_transition_table.md`](applicant_status_transition_table.md) — APP-T001 through APP-T006

## Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| `[*]` | `[*]` | Start | Start | |
| A0 | A0 | A0 - Draft | Transitional | |
| A1.0 | A1_0 | A1.0 - Submitted Form | Transitional | |
| A2.0 | A2_0 | A2.0 - Submitted - Complete Requirements | Transitional | Exit boundary to APP-02 |
| A2.1 | A2_1 | A2.1 - Submitted - Deficiencies | Transitional | |

## Included Transitions

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| APP-T001 | `[*]` | A0 | Account created | High | |
| APP-T002 | A0 | A1_0 | Application submitted | High | "Within 3 terms" in table |
| APP-T003 | A1_0 | A2_0 | Requirements complete | High | |
| APP-T004 | A1_0 | A2_1 | Deficiencies found | High | |
| APP-T005 | A2_1 | A2_0 | Requirements completed | High | Loop |
| APP-T006 | A2_0 | A2_1 | Resubmission required | High | Exception loop |

## Excluded States or Transitions

| Item | Reason Excluded |
|---|---|
| A3.x, A4.x, A5.x, A6.x, A7.x, A8.x | Belong to later diagrams |
| APP-T007+ | Out of scope |

## Diagram Boundaries

**Includes:** A0 → A1.0 → (A2.0 ↔ A2.1).  
**Excludes:** Exam evaluation onward. Outbound edge from A2_0 to APP-02 may be shown as a note or dashed "continues in APP-02" in overview docs only — not required in APP-01 final diagram.

## Recommended Mermaid Type

```text
stateDiagram-v2
```

## Complexity Safeguards

- 4 states + start — well under limits.
- Bidirectional A2_0 ↔ A2_1 is the only loop; keep labels short.

## Open Questions

- Confirm "submitted within last 3 terms" (APP-T002) is enforced — note on transition table only, not on arrow.
