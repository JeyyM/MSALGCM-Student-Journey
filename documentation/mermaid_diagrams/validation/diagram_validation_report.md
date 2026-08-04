# Diagram Validation Report

QA matrix for every Mermaid diagram file, validated against [`../../diagram_planning/diagram_validation_checklist.md`](../../diagram_planning/diagram_validation_checklist.md).

State/transition counts include `[*]` start/terminal markers and boundary edges where present. Files with two diagrams (applicant Part 2) report combined distinct states.

| Diagram File | Mermaid Type | # States | # Transitions | Valid IDs? | Terminal Labels? | Transition Details? | Unclear Items Listed? | Status |
|---|---|---:|---:|---|---|---|---|---|
| applicant_status/part_1_account_to_submission | stateDiagram-v2 | 4 | 7 | Yes | N/A (none terminal) | Yes | Yes | Ready |
| applicant_status/part_2_evaluation_to_decision | stateDiagram-v2 | 13 | 30 | Yes | Yes (A3.2, A4.2, A5.5) | Yes | Yes | Ready |
| applicant_status/part_3_acceptance_to_student | stateDiagram-v2 | 7 | 9 | Yes | Yes (A7.0) | Yes | Yes | Ready |
| applicant_status/part_4_terminal_or_exception_states | stateDiagram-v2 | 10 | 11 | Yes | Yes (A3.2, A4.2, A5.5, A6.1, A8.0) | Yes | Yes | Ready |
| student_status/part_1_active_and_enrollment | stateDiagram-v2 | 2 | 3 | Yes | N/A | Yes | Yes | Ready |
| student_status/part_2_residency_and_loa | stateDiagram-v2 | 5 | 7 | Yes | N/A (none terminal) | Yes | Yes | Needs Stakeholder Confirmation |
| student_status/part_3_awol_suspension_and_exit | stateDiagram-v2 | 6 | 10 | Yes | Yes (S4.1, S4.2) | Yes | Yes | Needs Stakeholder Confirmation |
| student_status/part_4_graduation_and_terminal_states | stateDiagram-v2 | 4 | 6 | Yes | Yes (S4.0 alumni, S4.1, S4.2) | Yes | Yes | Ready |
| student_program_status/part_1_good_standing_and_probation | stateDiagram-v2 | 2 | 5 | Yes | N/A | Yes | Yes | Ready |
| student_program_status/part_2_snas_sap_and_ineligible | stateDiagram-v2 | 5 | 9 | Yes | Yes (P1.4) | Yes | Yes | Needs Review |
| student_program_status/part_3_graduation_and_terminal_states | stateDiagram-v2 | 4 | 6 | Yes | Yes (P3.0, P3.1) | Yes | Yes | Ready |
| combined_lifecycle/high_level_lifecycle_overview | flowchart TD | 8 | 10 | Yes | Yes (OUTCOME/END) | Yes | Yes | Ready |
| combined_lifecycle/applicant_to_student_bridge | stateDiagram-v2 | 6 | 5 | Yes | Yes (A7.0) | Yes | Yes | Needs Review |
| combined_lifecycle/student_status_vs_program_status_interaction | flowchart TD + tables | 7 | 4 (+ tables) | Yes | N/A (impact flow) | Yes | Yes | Needs Stakeholder Confirmation |
| combined_lifecycle/parallel_student_program_constrained_fsm | flowchart TB (LR lanes) | 17 | 24 (+ matrix summary) | Yes | N/A (constraint layer) | Yes | Yes | Ready |

## Status legend

- **Ready** — High-certainty content; safe to use for onboarding/documentation.
- **Needs Review** — Contains Medium-certainty edges or a labeling judgment (e.g. SAP escalation, direct-enrollment omission) that an analyst should sanity-check.
- **Needs Stakeholder Confirmation** — Depends on unresolved business rules (LOA/AWOL/suspension paths, combination code reconciliation) per [`../../open_questions.md`](../../open_questions.md).

## Checklist compliance (all files)

- [x] Every state appears in a planning file / documentation file.
- [x] Every drawn transition maps to a transition-table ID (or is a labeled boundary marker).
- [x] Certainty levels recorded in each Transition Details table.
- [x] No `Unknown` transitions drawn; `Low` shown only as `[Tentative]` where planning permitted.
- [x] Transition labels short; AND/OR detail kept in tables.
- [x] Terminal states labeled `[Terminal]` (or `[Alumni may continue]` for S4.0).
- [x] Mermaid IDs use underscores (no dots/spaces/slashes).
- [x] Each diagram has a clear boundary.
- [x] State counts within 8–12 (applicant Part 2 split into two sub-diagrams to comply).
- [x] Detailed diagrams do not mix dimensions (only bridge/overview/interaction do, by design).
- [x] M3 vs Post-M3 conflicts noted (combination interaction file).

## Tentative edges in use

| File | Tentative transition |
|---|---|
| student_status/part_3_awol_suspension_and_exit | `S3.1 → S1.0` (returnee), `S3.2 → S2.0` (suspension served) |

## Notes for the "under 1 minute" reviewer test

All Ready diagrams pass the readability test. The two **Needs Stakeholder Confirmation** student files and the combination interaction file are readable but encode rules that may change once questions are answered — treat their specific edges as provisional.
