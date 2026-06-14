# Applicant Status Transition Table

**Source:** `SEP 19 Post-M3 WIP - Applicant/StudentStatuses` (canonical).  
**Reference:** [`../applicant_status_flow.md`](../applicant_status_flow.md)  
**Excluded codes:** `A3.3`, `A9.0` (per [`../decisions.md`](../decisions.md))

Directions are **inferred forward** from allowed-previous statuses and activity/condition rows unless explicitly documented as reverse.

---

## Normal transitions

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| APP-T001 | `[*]` | Start | A0 | Draft | Account created | Application drafted (not submitted) | applicant_status_flow.md § table A0 | High | Entry point |
| APP-T002 | A0 | Draft | A1.0 | Submitted Form | Application submitted | Form submitted within last 3 terms | applicant_status_flow.md § A1.0 | High | |
| APP-T003 | A1.0 | Submitted Form | A2.0 | Submitted - Complete Requirements | Requirements completed | Mandatory requirements for admission application completed | applicant_status_flow.md § A2.0 | High | |
| APP-T004 | A1.0 | Submitted Form | A2.1 | Submitted - Deficiencies | Pending requirements | Mandatory requirements pending | applicant_status_flow.md § A2.1 | High | |
| APP-T005 | A2.1 | Submitted - Deficiencies | A2.0 | Submitted - Complete Requirements | Requirements completed | Resubmission / completion | applicant_status_flow.md § A2.0 allowed previous | High | Loop |
| APP-T006 | A2.0 | Submitted - Complete Requirements | A2.1 | Submitted - Deficiencies | Resubmission required | OAS/OASIS requires resubmit OR pending requirements | applicant_status_flow.md § A2.1 | High | Exception loop |
| APP-T007 | A2.0 | Submitted - Complete Requirements | A3.0 | Exam Required | Exam required | Evaluated by OAS/OASIS AND applicant must undergo exam | applicant_status_flow.md § A3.0 | High | |
| APP-T008 | A2.0 | Submitted - Complete Requirements | A3.1 | Exam Exempted | Exam exempted | Evaluated by OAS/OASIS AND applicant exempted from exam | applicant_status_flow.md § A3.1 | High | |
| APP-T009 | A2.0 | Submitted - Complete Requirements | A3.2 | Not Qualified (initial eval) | Failed initial evaluation | Evaluated by OAS/OASIS AND not qualified for admission | applicant_status_flow.md § A3.2 | High | **Terminal** |
| APP-T010 | A3.0 | Exam Required | A4.0 | Exam Taken | Exam taken | Applicant has taken admission exam | applicant_status_flow.md § A4.0 | High | |
| APP-T011 | A3.0 | Exam Required | A4.1 | Exam Pending | Exam not yet taken | Must undergo exam AND not taken AND slots/window open | applicant_status_flow.md § A4.1 | High | |
| APP-T012 | A3.0 | Exam Required | A4.2 | Not Qualified (no exam) | Exam window lost | Not taken AND no slots / reschedule period lapsed | applicant_status_flow.md § A4.2 | High | **Terminal** |
| APP-T013 | A4.1 | Exam Pending | A4.0 | Exam Taken | Exam taken | Applicant has taken admission exam | applicant_status_flow.md § A4.0 allowed previous | High | |
| APP-T014 | A4.1 | Exam Pending | A4.2 | Not Qualified (no exam) | Exam window lost | Not taken AND no slots / period lapsed | applicant_status_flow.md § A4.2 | High | **Terminal** |
| APP-T015 | A2.0 | Submitted - Complete Requirements | A4.3 | Further Evaluation Required | Exam not required | Exam not required by program | applicant_status_flow.md § A4.3 | High | One of two triggers for A4.3 |
| APP-T016 | A4.0 | Exam Taken | A4.3 | Further Evaluation Required | Further screening | Interview/publication/etc. required | applicant_status_flow.md § A4.3 | Medium | Also from exam path |
| APP-T017 | A3.1 | Exam Exempted | A5.0 | Offered | Admission results | Scores within cutoff | applicant_status_flow.md § A5.0 | High | |
| APP-T018 | A4.0 | Exam Taken | A5.0 | Offered | Admission results | Scores within cutoff | applicant_status_flow.md § A5.0 | High | |
| APP-T019 | A4.3 | Further Evaluation Required | A5.0 | Offered | Passed further evaluation | Passed further evaluation | applicant_status_flow.md § A5.0 | High | |
| APP-T020 | A5.3 | Waitlisted | A5.0 | Offered | Slot opened | Applicant considered when others decline | applicant_status_flow.md § typical journey | Medium | Implied by waitlist description |
| APP-T021 | A4.0 | Exam Taken | A5.1 | Offered - Probationary | Probationary offer | Additional requirements to maintain stay | applicant_status_flow.md § A5.1 | High | IS/GS/SOL only |
| APP-T022 | A4.3 | Further Evaluation Required | A5.1 | Offered - Probationary | Probationary offer | Additional requirements to maintain stay | applicant_status_flow.md § A5.1 | High | |
| APP-T023 | A4.0 | Exam Taken | A5.2 | Offered - Redirected | Redirected offer | Qualified for different strand/program | applicant_status_flow.md § A5.2 | High | |
| APP-T024 | A3.1 | Exam Exempted | A5.2 | Offered - Redirected | Redirected offer | Qualified for different strand/program | applicant_status_flow.md § A5.2 | High | |
| APP-T025 | A4.3 | Further Evaluation Required | A5.2 | Offered - Redirected | Redirected offer | Qualified for different strand/program | applicant_status_flow.md § A5.2 | High | |
| APP-T026 | A4.0 | Exam Taken | A5.3 | Waitlisted | Waitlisted | Qualified but no slots | applicant_status_flow.md § A5.3 | High | |
| APP-T027 | A3.1 | Exam Exempted | A5.3 | Waitlisted | Waitlisted | Qualified but no slots | applicant_status_flow.md § A5.3 | High | |
| APP-T028 | A4.3 | Further Evaluation Required | A5.3 | Waitlisted | Waitlisted | Qualified but no slots | applicant_status_flow.md § A5.3 | High | |
| APP-T029 | A4.0 | Exam Taken | A5.5 | Not Qualified | Failed cutoff | Scores outside cutoff for any strand/program | applicant_status_flow.md § A5.5 | High | **Terminal** (see APP-T032 exception) |
| APP-T030 | A3.1 | Exam Exempted | A5.5 | Not Qualified | Failed cutoff | Scores outside cutoff | applicant_status_flow.md § A5.5 | High | **Terminal** |
| APP-T031 | A4.3 | Further Evaluation Required | A5.5 | Not Qualified | Failed cutoff | Scores outside cutoff | applicant_status_flow.md § A5.5 | High | **Terminal** |
| APP-T033 | A5.0 | Offered | A6.0 | Reserved | Official acceptance | Period not lapsed AND (fee paid OR waived) | applicant_status_flow.md § A6.0 | High | |
| APP-T034 | A5.1 | Offered - Probationary | A6.0 | Reserved | Official acceptance | Same as APP-T033 | applicant_status_flow.md § A6.0 | High | |
| APP-T035 | A5.2 | Offered - Redirected | A6.0 | Reserved | Official acceptance | Same as APP-T033 | applicant_status_flow.md § A6.0 | High | |
| APP-T037 | A5.0 | Offered | A6.1 | Cancelled (no fee) | Non-payment | End of admission term AND fee not paid | applicant_status_flow.md § A6.1 | High | **Terminal** |
| APP-T038 | A5.1 | Offered - Probationary | A6.1 | Cancelled (no fee) | Non-payment | Same as APP-T037 | applicant_status_flow.md § A6.1 | High | **Terminal** |
| APP-T039 | A5.2 | Offered - Redirected | A6.1 | Cancelled (no fee) | Non-payment | Same as APP-T037 | applicant_status_flow.md § A6.1 | High | **Terminal** |
| APP-T041 | A6.0 | Reserved | A7.0 | Officially Admitted | Requirements complete | Was Reserved AND mandatory reqs for official acceptance completed | applicant_status_flow.md § A7.0 | High | **Terminal for admission app** |
| APP-T042 | A6.0 | Reserved | A7.1 | Provisionally Admitted | Requirements pending | Was Reserved AND mandatory reqs not completed | applicant_status_flow.md § A7.1 | High | |
| APP-T043 | A7.1 | Provisionally Admitted | A7.0 | Officially Admitted | Requirements completed | Mandatory reqs for official acceptance completed | applicant_status_flow.md § A7.0 allowed previous | Medium | A7.1 also listed as own previous |
| APP-T045 | A7.1 | Provisionally Admitted | A8.0 | Cancelled (no reqs) | Requirements deadline | 1 year from admission term AND reqs not completed | applicant_status_flow.md § A8.0 | High | **Terminal** |
| APP-T046 | A7.0 | Officially Admitted | A8.1 | Cancelled - Withdrawal | Withdrew | Enrolled in admission term AND withdrew within term | applicant_status_flow.md § A8.1 | High | |
| APP-T047 | A7.1 | Provisionally Admitted | A8.1 | Cancelled - Withdrawal | Withdrew | Same as APP-T046 | applicant_status_flow.md § A8.1 | High | |

---

## Cross-dimension transitions (applicant → student)

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| APP-T048 | A7.0 | Officially Admitted | S1.0 | Active - Without Enrollment | Admission complete | Not yet enrolled | applicant_status_flow.md § hand-off | High | For APP-05 diagram |
| APP-T049 | A7.1 | Provisionally Admitted | S1.0 | Active - Without Enrollment | Provisional admission | Not yet enrolled | applicant_status_flow.md § hand-off | High | |
| APP-T050 | A7.0 | Officially Admitted | S2.0 | Active | Enrolled in admission term | Block enrolled / confirmed enrollment | applicant_status_flow.md § hand-off | Medium | Duplicate column encoding in matrix |
| APP-T051 | A7.1 | Provisionally Admitted | S2.0 | Active | Enrolled in admission term | Same as APP-T050 | applicant_status_flow.md § hand-off | Medium | Confirm single source of truth |
| APP-T052 | A6.0 | Reserved | A7.2 | Deferred | Did not enroll | Student was S1.0 AND did not enroll; late enrollment lapsed | applicant_status_flow.md § A7.2 | Medium | References student status |

---

## Exception / disputed transitions

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| APP-T032 | A5.5 | Not Qualified | A5.4 | Reconsidered | Appeal | Did not qualify AND reconsidered after appeal | applicant_status_flow.md § A5.4 | **Low** | Revives terminal; **exclude from final diagram** unless confirmed |
| APP-T036 | A5.4 | Reconsidered | A6.0 | Reserved | Official acceptance | Fee paid/waived | applicant_status_flow.md § A6.0 allowed previous | **Low** | Depends on APP-T032 |
| APP-T040 | A5.4 | Reconsidered | A6.1 | Cancelled (no fee) | Non-payment | End of term AND no fee | applicant_status_flow.md § A6.1 | **Low** | Depends on APP-T032 |

---

## Self-loops (status may persist)

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| APP-T060 | A4.1 | Exam Pending | A4.1 | Exam Pending | Awaiting exam | Slots/window still open; exam not yet taken | applicant_status_flow.md § A4.1 | Medium | Optional in diagram |
| APP-T061 | A7.1 | Provisionally Admitted | A7.1 | Provisionally Admitted | Awaiting requirements | A7.1 listed as allowed previous for A7.1 | applicant_status_flow.md § A7.1 | Medium | Optional self-loop |

---

## Transitions excluded from future diagrams

| Possible Transition | Reason Excluded | What Needs Confirmation |
|---|---|---|
| Any → `A3.3` Exam Not Required | Strikethrough / deprecated | N/A — dropped |
| Any → `A9.0` Inactive | Strikethrough / deprecated | Data purge only |
| `A5.5` → `A5.4` → `A6.x` (APP-T032, T036, T040) | Low certainty; terminal revival | Is A5.5 truly terminal? Appeal path? |
| `A6.0` → `A7.2` without S1.0 context (APP-T052) | Cross-dimension; student status precondition unclear | Exact deferral trigger |
| `A7.0`/`A7.1` → `S2.0` direct (APP-T050, T051) | Medium; matrix duplicate columns | One enrollment hand-off model |
| `A8.0` → student `S4.0` mapping | M3-era mapping in hand-off table; unclear in Post-M3 | Confirm cancellation student status |
| Re-application after terminal rejection | Not in matrix | New application vs revive old? |
