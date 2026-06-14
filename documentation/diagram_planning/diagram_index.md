# Diagram Index

Planned diagrams for the applicant/student journey. **No final Mermaid files exist yet** — this index defines what to build later.

**Canonical sources:** Post-M3 WIP tabs (see [`../decisions.md`](../decisions.md)).  
**Excluded from all diagrams:** strikethrough codes, `Yes?` combinations, SAP grade thresholds until confirmed.

---

## Applicant / admission diagrams

| Diagram ID | Diagram File Name (future) | Planning File | Purpose | Source Documentation | Expected Complexity | Notes |
|---|---|---|---|---|---|---|
| APP-01 | `APP-01_account_to_submission.mmd` | [`applicant_status_part_1_account_to_submission.md`](applicant_status_part_1_account_to_submission.md) | Account creation through submitted application and requirements loop | `applicant_status_flow.md` | Low | 4 states, ~6 transitions; good first diagram |
| APP-02 | `APP-02_exam_evaluation.mmd` | [`applicant_status_part_2_evaluation_to_decision.md`](applicant_status_part_2_evaluation_to_decision.md) | Exam required/exempted, exam taken/pending, further evaluation, initial rejection | `applicant_status_flow.md` | Medium | 7 states, ~12 transitions; split exam from results |
| APP-03 | `APP-03_admission_results.mmd` | (same part 2 file, second diagram) | Offered, probationary, redirected, waitlisted, not qualified, reconsidered | `applicant_status_flow.md` | Medium | Many inbound edges; keep separate from APP-02 |
| APP-04 | `APP-04_official_acceptance.mmd` | [`applicant_status_part_3_acceptance_to_student.md`](applicant_status_part_3_acceptance_to_student.md) | Reserved, fee payment, officially/provisionally admitted, deferred, cancellations | `applicant_status_flow.md` | Medium | Includes terminal applicant outcomes |
| APP-05 | `APP-05_applicant_to_student_handoff.mmd` | (section in part 3 plan) | Cross-dimension hand-off: `A7.x` → `S1.0` / enrollment paths | `applicant_status_flow.md`, `student_status_flow.md` | Low | **Only** diagram that mixes applicant + student; minimal nodes |

**Master plan:** [`applicant_status_diagram_plan.md`](applicant_status_diagram_plan.md)  
**Transition table:** [`applicant_status_transition_table.md`](applicant_status_transition_table.md)

---

## Student status diagrams

| Diagram ID | Diagram File Name (future) | Planning File | Purpose | Source Documentation | Expected Complexity | Notes |
|---|---|---|---|---|---|---|
| STU-01 | `STU-01_active_and_enrollment.mmd` | [`student_status_part_1_active_and_enrollment.md`](student_status_part_1_active_and_enrollment.md) | `S1.0` without enrollment → `S2.0` active; residency | `student_status_flow.md` | Low | Entry from APP-05; 3–4 states |
| STU-02 | `STU-02_loa_awol_suspension.mmd` | [`student_status_part_2_loa_awol_suspension.md`](student_status_part_2_loa_awol_suspension.md) | LOA, prolonged leave, AWOL, suspension, returnee | `student_status_flow.md` | High | Most ambiguous area; validate carefully |
| STU-03 | `STU-03_exit_and_graduation.mmd` | [`student_status_part_3_exit_and_graduation.md`](student_status_part_3_exit_and_graduation.md) | Graduated, exited good standing, permanent disqualification | `student_status_flow.md` | Medium | Terminal-focused; many inbound exit edges |

**Master plan:** [`student_status_diagram_plan.md`](student_status_diagram_plan.md)  
**Transition table:** [`student_status_transition_table.md`](student_status_transition_table.md)

---

## Student program status diagrams

| Diagram ID | Diagram File Name (future) | Planning File | Purpose | Source Documentation | Expected Complexity | Notes |
|---|---|---|---|---|---|---|
| PRG-01 | `PRG-01_eligible_and_probationary.mmd` | [`student_program_status_part_1_good_standing_to_probation.md`](student_program_status_part_1_good_standing_to_probation.md) | Initial eligible/probationary; lift probation | `student_program_status_flow.md` | Low | Entry from admission offer type |
| PRG-02 | `PRG-02_snas_strict_and_ineligible.mmd` | [`student_program_status_part_2_ineligible_and_snas.md`](student_program_status_part_2_ineligible_and_snas.md) | SNAS, strict probationary (IS), ineligible | `student_program_status_flow.md` | Medium | SAP thresholds deferred per decisions |
| PRG-03 | `PRG-03_graduation_and_terminal.mmd` | [`student_program_status_part_3_graduation_and_terminal.md`](student_program_status_part_3_graduation_and_terminal.md) | Candidate, graduated, incomplete | `student_program_status_flow.md` | Low | Clear two-step graduation |

**Master plan:** [`student_program_status_diagram_plan.md`](student_program_status_diagram_plan.md)  
**Transition table:** [`student_program_status_transition_table.md`](student_program_status_transition_table.md)

---

## Combination and overview diagrams

| Diagram ID | Diagram File Name (future) | Planning File | Purpose | Source Documentation | Expected Complexity | Notes |
|---|---|---|---|---|---|---|
| COMBO-01 | *(table recommended, not Mermaid)* | [`status_combination_diagram_plan.md`](status_combination_diagram_plan.md) | Allowed/blocked student × program pairs | `status_combination_rules.md` | N/A | **Use matrix/table**; optional small flowchart for cross-impact rules only |
| LIFE-01 | `LIFE-01_high_level_overview.mmd` | [`high_level_lifecycle_diagram_plan.md`](high_level_lifecycle_diagram_plan.md) | Simplified end-to-end phases | `lifecycle_summary.md` | Low | ~6–8 composite nodes only; not every status |

**Combination impacts:** [`status_combination_transition_table.md`](status_combination_transition_table.md)

---

## Summary counts

| Category | Planned diagrams | Transition table rows (approx.) |
|---|---|---|
| Applicant (`APP-*`) | 5 | 48 (+ exclusions) |
| Student (`STU-*`) | 3 | 28 (+ exclusions) |
| Program (`PRG-*`) | 3 | 22 (+ exclusions) |
| Combination (`COMBO-*`) | 0 Mermaid / 1 table artifact | 12 cross-impact rules |
| High-level (`LIFE-*`) | 1 | 7 phase transitions |
| **Total Mermaid diagrams planned** | **12** | — |

---

## Recommended build order (later)

1. **APP-01** — simplest, validates pipeline  
2. **APP-02, APP-03, APP-04** — complete admission track  
3. **APP-05** — hand-off to student  
4. **STU-01, PRG-01** — parallel student + program entry  
5. **PRG-02, PRG-03** — academic standing completion  
6. **STU-03** — terminals (clearer than STU-02)  
7. **LIFE-01** — overview after parts exist  
8. **STU-02** — defer until LOA/AWOL questions answered  
9. **COMBO-01** — after code-scheme reconciliation (or two table versions)

## Do not create until stakeholder confirmation

| Diagram ID | Blocker |
|---|---|
| APP-03 (partial) | `APP-T032` A5.5 → A5.4 Reconsidered (Low) |
| STU-02 | LOA vs Prolonged Leave thresholds; AWOL grace period |
| COMBO-01 (canonical codes) | Combination tab uses old `S3.x` / `P1.3` numbering |
| Any diagram | Transitions marked `Unknown` in [`unclear_transitions.md`](unclear_transitions.md) |
