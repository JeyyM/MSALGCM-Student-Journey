# Diagram Plan: APP-02 & APP-03 — Evaluation Through Admission Results

## Purpose

Two diagrams from one planning file:

1. **APP-02** — Requirements evaluation and exam path (A2.0 through A4.x, plus A3.2 terminal).
2. **APP-03** — Admission results (A5.x) including offers, waitlist, and rejection terminals.

Entry assumed from **A2.0** (complete requirements) from APP-01.

## Source Files

- [`../applicant_status_flow.md`](../applicant_status_flow.md)
- [`applicant_status_transition_table.md`](applicant_status_transition_table.md)

---

## APP-02: Exam and Evaluation

### Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| A2.0 | A2_0 | A2.0 - Submitted - Complete Requirements | Transitional | Entry from APP-01 |
| A3.0 | A3_0 | A3.0 - Exam Required | Transitional | |
| A3.1 | A3_1 | A3.1 - Exam Exempted | Transitional | Exit to APP-03 |
| A3.2 | A3_2 | A3.2 - Not Qualified (initial eval) [Terminal] | Terminal | |
| A4.0 | A4_0 | A4.0 - Exam Taken | Transitional | Exit to APP-03 |
| A4.1 | A4_1 | A4.1 - Exam Pending | Transitional | |
| A4.2 | A4_2 | A4.2 - Not Qualified (no exam) [Terminal] | Terminal | |
| A4.3 | A4_3 | A4.3 - Further Evaluation Required | Transitional | Exit to APP-03 |

### Included Transitions (APP-02)

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| APP-T007 | A2_0 | A3_0 | Exam required | High | |
| APP-T008 | A2_0 | A3_1 | Exam exempted | High | |
| APP-T009 | A2_0 | A3_2 | Failed initial evaluation | High | Terminal |
| APP-T010 | A3_0 | A4_0 | Exam taken | High | |
| APP-T011 | A3_0 | A4_1 | Exam pending | High | |
| APP-T012 | A3_0 | A4_2 | Exam window lapsed | High | Terminal |
| APP-T013 | A4_1 | A4_0 | Exam taken | High | |
| APP-T014 | A4_1 | A4_2 | Exam window lapsed | High | Terminal |
| APP-T015 | A2_0 | A4_3 | Exam not required | High | |
| APP-T016 | A4_0 | A4_3 | Further screening required | Medium | |

**Optional:** APP-T060 self-loop on A4_1 — omit unless needed.

### APP-02 Boundaries

**Includes:** Evaluation and exam only.  
**Excludes:** A5.x results (APP-03). Outbound: A3_1, A4_0, A4_3 → APP-03 (document as boundary note, not edges within APP-02).

---

## APP-03: Admission Results

### Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| A5.0 | A5_0 | A5.0 - Offered | Transitional | Exit to APP-04 |
| A5.1 | A5_1 | A5.1 - Offered - Probationary | Transitional | IS/GS/SOL |
| A5.2 | A5_2 | A5.2 - Offered - Redirected | Transitional | |
| A5.3 | A5_3 | A5.3 - Waitlisted | Transitional | |
| A5.5 | A5_5 | A5.5 - Not Qualified [Terminal] | Terminal | |
| A5.4 | A5_4 | A5.4 - Reconsidered | Transitional | **Exclude unless Tentative** |
| (entry) | — | From A3_1 / A4_0 / A4_3 | — | — | Shown as inbound only |

### Included Transitions (APP-03) — High/Medium only

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| APP-T017 | A3_1 | A5_0 | Offered | High | Inbound from APP-02 |
| APP-T018 | A4_0 | A5_0 | Offered | High | |
| APP-T019 | A4_3 | A5_0 | Passed further evaluation | High | |
| APP-T020 | A5_3 | A5_0 | Slot opened | Medium | |
| APP-T021 | A4_0 | A5_1 | Probationary offer | High | |
| APP-T022 | A4_3 | A5_1 | Probationary offer | High | |
| APP-T023–T028 | various | A5_2/A5_3 | Redirected / Waitlisted | High | See transition table |
| APP-T029–T031 | various | A5_5 | Not qualified | High | Terminals |

### Excluded from APP-03 (final diagram)

| Item | Reason |
|---|---|
| APP-T032, T036, T040 | Low — Reconsidered loop |
| A6.x, A7.x | APP-04 |

### APP-03 Boundaries

**Includes:** All A5.x decision outcomes.  
**Excludes:** Official acceptance (APP-04). Many inbound edges — consider **grouping** inbound as "From evaluation (APP-02)" pseudo-note to reduce clutter.

## Recommended Mermaid Type

`stateDiagram-v2` for both.

## Complexity Safeguards

- APP-02: 8 states — at limit; do not add A5 preview nodes.
- APP-03: collapse inbound from A3_1/A4_0/A4_3 into **three labeled entry points** max, or use a composite `EVAL_DONE` node (overview style only — document choice in validation checklist).

## Open Questions

- A4.3 dual trigger (APP-T015 vs T016) — one node or split?
- APP-T020 waitlist → offered — include as Medium or wait for confirmation?
- A5.4 Reconsidered — excluded by default per decisions.
