# Diagram Planning Layer

This folder prepares **future Mermaid diagrams** for the DLSU applicant/student journey. It does **not** contain final diagrams yet.

## Purpose

The full lifecycle is too large and too conditional for one giant Mermaid graph. A single diagram would likely be unreadable and may encode incorrect transitions (especially where the workbook only lists *allowed previous statuses*, not explicit forward arrows).

This planning layer exists to:

1. **Split** the lifecycle into small, focused diagrams (typically 8–12 states each).
2. **Back every arrow** with a transition table row (ID, trigger, conditions, certainty).
3. **Flag uncertainty** before anything is drawn.
4. **Apply go-forward rules** from [`../decisions.md`](../decisions.md) (exclude strikethrough, defer needs-confirmation, prefer Post-M3 WIP unless cascading).

## How transition tables support correctness

Each major area has a transition table file:

| File | Scope |
|---|---|
| [`applicant_status_transition_table.md`](applicant_status_transition_table.md) | Admission application statuses (`A*`) |
| [`student_status_transition_table.md`](student_status_transition_table.md) | Student statuses (`S*`) |
| [`student_program_status_transition_table.md`](student_program_status_transition_table.md) | Program statuses (`P*`) |
| [`status_combination_transition_table.md`](status_combination_transition_table.md) | Cross-dimension impacts (not full state flows) |

**Workflow:** define transitions in tables first → assign to diagram parts → validate with [`diagram_validation_checklist.md`](diagram_validation_checklist.md) → only then generate Mermaid in a future `documentation/diagrams/` (or similar) step.

## How future Mermaid files should be generated

1. Pick a diagram from [`diagram_index.md`](diagram_index.md) (e.g. `APP-01`).
2. Open the matching **part plan** (e.g. `applicant_status_part_1_account_to_submission.md`).
3. Pull transitions from the transition table by **Transition ID**.
4. Apply [`naming_conventions.md`](naming_conventions.md) for state IDs and labels.
5. Exclude any transition marked `Low` or `Unknown` unless explicitly marked **tentative** in the plan.
6. Complete [`diagram_validation_checklist.md`](diagram_validation_checklist.md).
7. Write the Mermaid file (suggested location: `documentation/diagrams/` — not created yet).

## Files to review before creating any diagram

| Order | File | Why |
|---|---|---|
| 1 | [`../decisions.md`](../decisions.md) | What to include/exclude |
| 2 | Relevant `*_transition_table.md` | Source of truth for arrows |
| 3 | Relevant `*_part_*.md` or `*_diagram_plan.md` | Boundaries and state lists |
| 4 | [`unclear_transitions.md`](unclear_transitions.md) | Do not diagram unresolved items |
| 5 | [`naming_conventions.md`](naming_conventions.md) | ID/label rules |
| 6 | [`diagram_validation_checklist.md`](diagram_validation_checklist.md) | Pre-flight checks |

## Safeguards (summary)

See also section 9 in the task spec and each diagram plan's **Complexity Safeguards**:

- No single "everything diagram."
- Do not connect states just because they appear adjacent in the spreadsheet.
- Do not assume chronological flow without trigger or allowed-previous support.
- Keep AND/OR detail in tables, not on arrow labels.
- Do not hide uncertainty.
- Do not mix applicant, student, and program dimensions except in `LIFE-01` overview.
- Prefer a **table/matrix** over Mermaid when the artifact is a combination grid.

## Related documentation

| Document | Role |
|---|---|
| [`../applicant_status_flow.md`](../applicant_status_flow.md) | Applicant narrative + reference |
| [`../student_status_flow.md`](../student_status_flow.md) | Student narrative + reference |
| [`../student_program_status_flow.md`](../student_program_status_flow.md) | Program narrative + reference |
| [`../status_combination_rules.md`](../status_combination_rules.md) | Combination matrix |
| [`../open_questions.md`](../open_questions.md) | Stakeholder questions |
