# Mermaid Diagrams — DLSU Applicant/Student Journey

This folder contains the **final Mermaid diagrams** for the applicant/student lifecycle, rendered as finite-state-machine–style diagrams. They are generated from the planning layer in [`../diagram_planning/`](../diagram_planning/README.md), which is the source of truth for states, transitions, and certainty.

## What this folder contains

| Subfolder | Scope | Machine type |
|---|---|---|
| [`applicant_status/`](applicant_status/README.md) | Admission application statuses (`A*`) | `stateDiagram-v2` |
| [`student_status/`](student_status/README.md) | Student statuses (`S*`) | `stateDiagram-v2` |
| [`student_program_status/`](student_program_status/README.md) | Academic program statuses (`P*`) | `stateDiagram-v2` |
| [`combined_lifecycle/`](combined_lifecycle/README.md) | Cross-dimension overviews | `flowchart TD` + `stateDiagram-v2` |
| [`validation/`](validation/diagram_validation_report.md) | QA report + open questions | — |

Plus [`diagram_creation_notes.md`](diagram_creation_notes.md) describing decisions made while drawing.

## Why diagrams are split into smaller parts

The full lifecycle has ~40 statuses across three dimensions with many conditional transitions. One giant diagram would be unreadable and would hide incorrect edges. Instead, each diagram covers **one lifecycle segment** (8–12 states, ≤15–20 transitions) and is understandable on its own. Larger areas are split into numbered parts.

## Why `stateDiagram-v2` is the main type

The spreadsheet is fundamentally about **states, allowed previous statuses, transitions, triggers, and terminal states** — i.e. a finite state machine. `stateDiagram-v2` maps directly onto that:

- A status = a state
- A trigger/event = a transition (arrow)
- A terminal status = a state with no outgoing transitions, routed to `[*]`

## When `flowchart TD` is used instead

Only for **broad process overviews** where formal state semantics would mislead:

- [`combined_lifecycle/high_level_lifecycle_overview.md`](combined_lifecycle/high_level_lifecycle_overview.md)
- [`combined_lifecycle/parallel_student_program_constrained_fsm.md`](combined_lifecycle/parallel_student_program_constrained_fsm.md) — integrated parallel FSM + combination-tab validation
- [`combined_lifecycle/student_status_vs_program_status_interaction.md`](combined_lifecycle/student_status_vs_program_status_interaction.md) (the two dimensions run in parallel, not as one sequence)

## How to read terminal states

Mermaid has no double-circle accepting state, so terminal states are marked **`[Terminal]`** inside the label and routed to `[*]`:

```text
state "S4.1 - Exited on Good Standing [Terminal]" as S4_1
S4_1 --> [*]
```

`S4.0 - Graduated` is labeled **`[Alumni may continue]`** because the workbook does not mark the *student* status Graduated as terminal — graduates may re-enroll (e.g. BS→MS). See [`../executive_defaults.md`](../executive_defaults.md).

## How to read tentative transitions

Low-certainty edges that are still shown carry **`[Tentative]`** in the label, e.g.:

```text
S3_2 --> S2_0: Suspension served [Tentative]
```

`Unknown`-certainty transitions are **not drawn** at all — they are listed in each file's *Excluded or Unclear Transitions* table and in [`validation/unresolved_diagram_questions.md`](validation/unresolved_diagram_questions.md).

## Where to find validation

- [`validation/diagram_validation_report.md`](validation/diagram_validation_report.md) — per-file QA matrix and Ready / Needs Review / Needs Stakeholder Confirmation status.
- [`validation/unresolved_diagram_questions.md`](validation/unresolved_diagram_questions.md) — questions that could change diagram correctness.

## Which diagrams to review first

1. [`applicant_status/applicant_status_part_1_account_to_submission.md`](applicant_status/applicant_status_part_1_account_to_submission.md) — simplest, validates the style.
2. [`student_program_status/student_program_status_part_1_good_standing_and_probation.md`](student_program_status/student_program_status_part_1_good_standing_and_probation.md)
3. [`combined_lifecycle/high_level_lifecycle_overview.md`](combined_lifecycle/high_level_lifecycle_overview.md) — orients the rest.

Diagrams flagged **Needs Stakeholder Confirmation** (notably student LOA/AWOL/suspension and the combination map) should be reviewed against [`../open_questions.md`](../open_questions.md) before being treated as authoritative.

## Ground rules applied

Per [`../decisions.md`](../decisions.md): strikethrough codes excluded; `Yes?`/needs-confirmation items deferred; Post-M3 WIP preferred (legacy codes only inside the combination map, flagged). No detailed diagram mixes `A*`, `S*`, and `P*` — only the combined-lifecycle overviews do, deliberately.
