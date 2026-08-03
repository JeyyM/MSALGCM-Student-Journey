# BPMN Report — Student vs Program Interaction

**Matching files:** [`student_status_vs_program_status_interaction.bpmn`](../BPMN%20Code/combined_lifecycle/student_status_vs_program_status_interaction.bpmn) · [`student_status_vs_program_status_interaction.mmd`](../final%20mermaid%20code/combined_lifecycle/student_status_vs_program_status_interaction.mmd)

---

## Purpose

Models the **four cross-dimension forcing rules** from the combination tab — when a change in one track **requires** a change in the other. Same logical content as `cross_impact_rules` without COMBO-T00x labels in shape names.

---

## Rules modeled

| Trigger | Effect |
|---------|--------|
| All programs → P3.0 Graduated | Student → S4.0 Graduated |
| Student exit while program active | Program → P3.1 Incomplete |
| P1.4 Ineligible + shift pending | Student → S1.0 Without Enrollment |
| Shift approved | Student → S2.0 Active |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Mermaid `forces` edges | Cross-lane sequence flows | Synchronous impact, not message-based |
| Two lanes only | Program Office · Student Records | Minimal cross-impact view |
| No validation matrix | Only forced updates | Full V(S,P) → DMN |

---

## Swimlanes

| Lane | Role in cross-impact |
|------|----------------------|
| **Program Office** | Graduation complete, ineligible triggers |
| **Student Records** | Graduated student update, exit, shift paths |

---

## BPMN strengths here

- Makes **exception to independence** explicit — most S/P pairs are independent; these four are not.
- Small enough for slide alongside DMN combination table.

## Limitations

- **Cannot express 91-cell matrix** — BPMN impractical for full combination tab; DMN required.
- Sequence flow direction is **cause → effect** but workbook may allow ordering debates (e.g. exit before P3.1) — document as business rule.
- Student-initiated exit shown in student lane; program incomplete in program lane — timing not strict BPMN.

---

## Related diagrams

- **Labeled COMBO rules:** [cross_impact_rules](cross_impact_rules.md)
- **Full parallel model:** [parallel_student_program_constrained_fsm](parallel_student_program_constrained_fsm.md)
- **DMN:** combination tab (separate deliverable)
