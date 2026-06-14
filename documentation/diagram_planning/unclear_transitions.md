# Unclear Transitions — Master List

Master register of ambiguous transitions across all lifecycle areas. **Do not draw these as High-certainty Mermaid edges** until resolved.

Related: [`../open_questions.md`](../open_questions.md), [`../decisions.md`](../decisions.md)

---

## Applicant / admission

| Area | Possible Transition | Why It Is Unclear | Risk If Diagrammed Incorrectly | Question for Stakeholders |
|---|---|---|---|---|
| Applicant | `A5.5 Not Qualified` → `A5.4 Reconsidered` | Only allowed previous for A5.4 is terminal A5.5; revives dead end | Shows false appeal path or wrong terminal semantics | Is A5.5 truly terminal, or should appeal branch before rejection? |
| Applicant | `A5.4` → `A6.0` / `A6.1` | Depends on reconsideration loop | Incorrect acceptance/cancellation paths | Same as above |
| Applicant | `A7.1` → `A7.1` (self) | A7.1 listed as own allowed previous | Infinite provisional state unclear | How many re-check cycles for provisional admission? |
| Applicant | `A7.1` → `A7.0` | Medium certainty; dual role of A7.1 | Wrong official acceptance timing | Exact rule when provisional becomes official? |
| Applicant | `A6.0` → `A7.2 Deferred` | Condition references student S1.0 + did not enroll | Deferral shown from wrong applicant state | Does deferral require prior S1.0, or only Reserved? |
| Applicant | `A7.0`/`A7.1` → `S2.0 Active` (direct) | Matrix duplicates columns for S1.0 vs S2.0 | Skips "without enrollment" state | Single hand-off: always S1.0 first, or direct S2.0 if enrolled? |
| Applicant | `A2.0` → `A4.3` vs `A4.0` → `A4.3` | Two triggers ("exam not required" vs "further screening") | Merges distinct evaluation paths | One status or two? |
| Applicant | `A5.3 Waitlisted` → `A5.0 Offered` | Implied by waitlist note, not explicit previous | Missing or wrong waitlist escape | Formal transition when slot opens? |
| Applicant | Terminal rejection → new `A0` | Not in matrix | Dead-end vs re-application unclear | New application after A5.5/A3.2? |

---

## M3 vs Post-M3 WIP conflicts

| Area | Possible Transition | Why It Is Unclear | Risk If Diagrammed Incorrectly | Question for Stakeholders |
|---|---|---|---|---|
| Cross | Official Confirmation → Official Acceptance labels | Terminology rename | Wrong process names in training materials | Final official name for fee and period? |
| Applicant | Reservation fee → Official Acceptance fee | Same process, renamed | Wrong business rule labels | Confirm A6.1 wording |
| Student | Separate Exclusion/Expelled/Transferred → `S4.2` | M3 had S3.5–S3.7; Post-M3 consolidated | Loses disciplinary granularity | Is S4.2 sufficient for all exit types? |
| Program | `P1.3` Ineligible (old) vs Strict Probationary (new) | Code renumbering | Wrong academic standing in diagrams | When will combination tab be regenerated? |
| Student | `S3.0 Graduated` (combo) vs `S4.0 Graduated` (canonical) | Code scheme mismatch | Inconsistent graduate state across docs | Single graduate student code? |

---

## Student status — LOA, AWOL, enrollment

| Area | Possible Transition | Why It Is Unclear | Risk If Diagrammed Incorrectly | Question for Stakeholders |
|---|---|---|---|---|
| Student | `S2.0 Active` → `S2.0` (term-break grace) | Self-loop with complex AND condition | Hides AWOL deadline or overstates stability | Exact end of grace vs late enrollment? |
| Student | `S2.0` → `S3.1 AWOL` vs stay `S2.0` during breaks | Competing conditions on S2.0 | Student appears AWOL too early or never AWOL | When exactly does AWOL trigger? |
| Student | `S2.0` → `S2.3 Prolonged Leave` vs `S2.2` → `S2.3` | Both LOA paths implied; workbook starts from S2.0 for S2.3 | Wrong LOA escalation path | Does prolonged leave require passing through S2.2? |
| Student | `S2.2 Under LOA` vs `S2.3 Prolonged Leave` threshold | "Max LOA" vs "6 trimesters" AND logic | Misclassified leave type | Are both conditions required (AND)? |
| Student | `S1.0` → `S3.1 AWOL` | Allowed previous includes S1.0 | Never-enrolled confused with AWOL | AWOL from S1.0 vs from S2.0 — same rules? |
| Student | `S2.1 Residency` → `S3.1 AWOL` | Allowed previous S2.1 for S3.1 | Residency absence mis-modeled | AWOL rules during residency? |
| Student | `S3.2 Suspended` → `S2.0` vs `S1.0` | Only S2.0 lists S3.2 as previous | Wrong return path after suspension | Returnee flow after suspension? |
| Student | `S2.2`/`S2.3`/`S3.1` → `S1.0` returnee | Reverse-engineered from allowed previous | Return shown without approval gate | What triggers "approved as returnee"? |

---

## Student status — exit, graduation, access

| Area | Possible Transition | Why It Is Unclear | Risk If Diagrammed Incorrectly | Question for Stakeholders |
|---|---|---|---|---|
| Student | `S2.0` → `S4.0 Graduated` | Trigger is all programs P3.0; S4.0 not labeled terminal | Alumni/BS-MS continuation blocked or allowed wrongly | Is S4.0 terminal? BS/MS after one program graduates? |
| Student | Graduated with clearance hold | Notes #7 — not a status | Missing hold state or false simplicity | Separate status or attribute? |
| Student | `S2.2 Under LOA` campus/SLC access | Notes #8 — Active implies full access; LOA policy open | Wrong access control design | LOA students: full, limited, or no access? |
| Student | `S3.2 Suspended` → `S4.1` good standing exit | Allowed previous includes S3.2 for S4.1 | Exit while suspended shown as normal | Can suspended students exit on good standing? |
| Student | `S4.1` vs `S4.2` from same sources | Many shared allowed previous statuses | Wrong terminal exit type | What distinguishes voluntary exit vs disciplinary? |

---

## Student program status

| Area | Possible Transition | Why It Is Unclear | Risk If Diagrammed Incorrectly | Question for Stakeholders |
|---|---|---|---|---|
| Program | `P1.1` → `P1.3 Strict Probationary` | SAP "below 75" not finalized | Wrong probation escalation | Exact SAP grade criteria? |
| Program | `P1.3` → `P1.4 Ineligible` on SAP fail | Notes say "asked to withdraw" → should be ineligible | SAP failure shown as voluntary exit | Confirm SAP fail → Ineligible |
| Program | `P1.1` new student vs old student rules | Future-state vs handbook rules | Wrong probation assignment | Who gets P1.1 and when? |
| Program | `P1.2 SNAS` → `P1.1 Probationary` | Allowed previous on P1.1 includes SNAS | SNAS/probation boundary blurred | SNAS vs Probationary relationship? |
| Program | `P1.1`/`P1.2`/`P1.3` → `P2.0 Candidate` | P2.0 previous is only P1.0 | Graduation from non-eligible standings | Can probationary/SNAS graduate candidacy? |
| Program | `P2.0` → revert if final check fails | Not documented | One-way graduation arrow wrong | Failed final check path? |

---

## Student status vs program status dependencies

| Area | Possible Transition | Why It Is Unclear | Risk If Diagrammed Incorrectly | Question for Stakeholders |
|---|---|---|---|---|
| Combo | `S2.2 Under LOA` + `P1.1 Probationary` | Notes #3 tentative No; combo tab Yes | Invalid pair allowed in system | Which is authoritative? |
| Combo | `S2.1 Residency` + `{P1.1, P1.2, P1.4}` | Yes? cells deferred | Residency academic pairs wrong | Confirm residency combinations |
| Combo | `S2.2` + `P1.2 SNAS` / `P2.0 Candidate` | Yes? deferred | LOA + academic warning pairs wrong | Allowed during LOA? |
| Combo | `P3.0 Graduated` → `S4.0` vs combo `S3.0` | Code + naming mismatch | Graduate validation breaks | Reconcile before COMBO diagram |
| Combo | Exit + active program → `P3.1 Incomplete` | Documented as scenario, not matrix row | Exit leaves program in wrong state | Automatic vs manual update? |
| Combo | Ineligible + shift → `S1.0` | Scenario in E10 | Shift workflow incomplete in status model | Full shift state machine? |

---

## AND/OR logic hard to interpret

| Area | Possible Transition | Why It Is Unclear | Risk If Diagrammed Incorrectly | Question for Stakeholders |
|---|---|---|---|---|
| Applicant | `A6.0 Reserved` fee logic | AND/OR stacking: period not lapsed AND (paid OR waived) | Wrong reserved eligibility | Confirm grouping |
| Applicant | `A4.3 Further Evaluation` green block | Fee paid/waived + did not enroll + validity lapsed (M column) | Overlap with admission results path | Is this A4.3 or A5.x path? |
| Student | `S3.1 AWOL` four AND conditions | Multiple stacked ANDs | AWOL too rare or too common | All four required? |
| Student | `S2.3` three AND conditions | LOA max + trimester count | Prolonged leave mis-triggered | Exact thresholds |
| Program | `P1.1` multiple OR entry triggers | Admission probationary OR old student OR failed standards | Single arrow hides branches | Split triggers in UI? |

---

## Terminal states with possible administrative actions

| Area | Possible Transition | Why It Is Unclear | Risk If Diagrammed Incorrectly | Question for Stakeholders |
|---|---|---|---|---|
| Applicant | Terminal `A3.2`/`A4.2`/`A5.5`/`A6.1`/`A8.0` | Terminal for application, not person | No re-entry shown | Re-apply as new applicant? |
| Applicant | `A7.0` terminal but person continues | Hand-off to student | Admission "end" confused with journey end | Label as admission-terminal only |
| Program | `P1.4 Ineligible` with shift process | Terminal for program, not person | Student appears fully exited | Shift vs exit workflow |
| Student | `S4.2 Permanent Disqualification` | Terminal; no return documented | False recovery path | Any appeal/reinstatement? |
| Program | `P3.0 Graduated` one week after commencement | Timing rule | Early/late graduation status | Exact job schedule? |

---

## Summary: do not diagram yet (Unknown / Low only)

| Transition ID(s) | Topic |
|---|---|
| APP-T032, T036, T040 | Reconsidered appeal loop |
| APP-T050, T051, T052 | Enrollment/deferral hand-offs |
| STU-T050, T051 | LOA → Prolonged Leave; Residency → LOA |
| STU-T052 | S4.0 terminal semantics |
| PRG-T060 | SAP numeric threshold |
| PRG-T061, T062 | Graduation from non-P1.0 |
| COMBO-R007 + all `Yes?` pairs | Combination uncertainty |
