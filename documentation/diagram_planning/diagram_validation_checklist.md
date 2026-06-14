# Diagram Validation Checklist

Complete this checklist **before** generating any Mermaid diagram from the planning layer.

---

## Source and scope

- [ ] Every state in the diagram exists in the documentation and is **not** excluded by [`../decisions.md`](../decisions.md).
- [ ] Every transition exists in the relevant `*_transition_table.md` with a **Transition ID**.
- [ ] Every transition has a **certainty** level recorded in the table.
- [ ] No `Low` or `Unknown` transition is included unless the diagram plan explicitly marks it **Tentative**.
- [ ] The diagram has a clear **boundary** documented in the part plan (Included / Excluded sections).
- [ ] The diagram does **not** mix unrelated lifecycle areas (applicant + student + program) unless it is `APP-05` or `LIFE-01`.

## Labels and readability

- [ ] Transition labels are **short and readable** (see [`naming_conventions.md`](naming_conventions.md)).
- [ ] Complex AND/OR conditions are in transition table **Conditions** columns, not on arrows.
- [ ] Terminal states are clearly labeled `[Terminal]` in state names.
- [ ] Mermaid state IDs use underscores, not dots (`A1_0` not `A1.0`).

## Complexity limits

- [ ] The diagram has **no more than 8–12 states** unless the part plan justifies an exception.
- [ ] The diagram has **no more than 15–20 transitions** unless the part plan justifies an exception.
- [ ] Cross-links that would clutter the graph are split into another diagram (see [`diagram_index.md`](diagram_index.md)).

## Conflicts and uncertainty

- [ ] M3 vs Post-M3 WIP conflicts are noted (Post-M3 WIP preferred per decisions).
- [ ] Items in [`unclear_transitions.md`](unclear_transitions.md) affecting this diagram are either excluded or marked Tentative.
- [ ] Combination-tab legacy codes are not used in canonical student/program diagrams.

## Cross-reference

- [ ] Transition IDs in the diagram plan match the transition table.
- [ ] Open Questions in the part plan have been reviewed; unresolved items are not drawn as High-certainty edges.

---

## Final reviewer question

> **Would a person unfamiliar with the spreadsheet understand this diagram in under 1 minute?**

If **no**, simplify labels, reduce states, or split into another diagram.

---

## Sign-off template (optional)

| Field | Value |
|---|---|
| Diagram ID | |
| Planning file reviewed | |
| Transition table reviewed | |
| Validator | |
| Date | |
| Tentative edges included? | Yes / No — list Transition IDs |
| Ready for Mermaid generation? | Yes / No |
