# Glossary — Codes, Acronyms, and Terms

Definitions are drawn from the workbook only. Where the workbook does not clearly define a term, it is marked **"Meaning inferred from context"** or **"Definition unclear from workbook."**

> **Note on code schemes:** Two different code schemes for student statuses and program statuses appear in the workbook. The **canonical** scheme below comes from the Post-M3 WIP status tabs. The combination tab uses an older scheme (noted where relevant). See [`README.md`](README.md) assumption #6.

---

## Applicant / Admission Application Status codes (`A*`)

Canonical source: `SEP 19 Post-M3 WIP - Applicant/StudentStatuses`.

| Code | Meaning (Admission Application Status) | Category | Notes / uncertainty |
|---|---|---|---|
| A0 | Draft | Applicant Status | Application started but not submitted. |
| A1.0 | Submitted Form | Applicant Status | Application form submitted. |
| A2.0 | Submitted - with Complete Requirements | Applicant Status | Mandatory admission requirements complete. |
| A2.1 | Submitted - with Deficiencies | Applicant Status | Pending requirements / asked to resubmit. |
| A3.0 | Exam Required | Applicant Status | Admission exam required by strand/program. |
| A3.1 | Exam Exempted | Applicant Status | Applicant exempted from the admission exam. |
| A3.2 | Not Qualified - Did not pass initial evaluation | Applicant Status (Terminal) | Terminal rejection at initial evaluation. |
| A3.3 | Exam Not Required | Applicant Status | **Deprecated** — struck through in M3; removed in Post-M3. |
| A4.0 | Exam Taken | Applicant Status | Applicant has taken the admission exam. |
| A4.1 | Exam Pending | Applicant Status | Has not yet taken; slots/reschedule window still open. |
| A4.2 | Not Qualified - Did not take Admission Exam | Applicant Status (Terminal) | Terminal; no slots / period lapsed. |
| A4.3 | Further Evaluation Required | Applicant Status | Exam not required, or further screening (interview, etc.) needed. |
| A5.0 | Offered | Applicant Status | Scores within cutoff / passed further evaluation. |
| A5.1 | Offered - Probationary | Applicant Status | **IS/GS/SOL only** (excludes UG). Offer with extra requirements → program P1.1. |
| A5.2 | Offered - Redirected | Applicant Status | Qualified for a different strand/program than applied for. |
| A5.3 | Waitlisted | Applicant Status | Qualified but no slot; may be considered if others decline. |
| A5.4 | Reconsidered | Applicant Status | Re-evaluated after an appeal. |
| A5.5 | Not Qualified | Applicant Status (Terminal) | Scores outside cutoff for any strand/program. |
| A6.0 | Reserved | Applicant Status | Official Acceptance Fee paid or waived; acceptance period open. |
| A6.1 | Cancelled - Due to non-payment of official acceptance fee | Applicant Status (Terminal) | M3 wording was "reservation fee"; renamed in Post-M3. |
| A7.0 | Officially Admitted | Applicant Status (Terminal) | Mandatory requirements for official acceptance complete. Hand-off to Student Status. |
| A7.1 | Provisionally Admitted | Applicant Status | Requirements for official acceptance not yet complete. |
| A7.2 | Deferred | Applicant Status | Did not enroll; offer/late-enrollment lapsed. |
| A8.0 | Cancelled - Due to non-submission of Mandatory Requirements for Official Acceptance | Applicant Status (Terminal) | 1 year from admission term lapsed. |
| A8.1 | Cancelled - Withdrawal from University | Applicant Status | Student enrolled in admission term then withdrew. |
| A9.0 | Inactive | Applicant Status | **Deprecated** — struck through in M3; Post-M3 note says "We will no longer have Inactive status." |

---

## Student Status codes (`S*`)

Canonical source: `SEP 19 Post-M3 WIP - StudentStatuses`.

| Code | Meaning (Student Status) | Category | Notes / uncertainty |
|---|---|---|---|
| S1.0 | Active - Without Enrollment | Student Status | Admitted/returnee but not yet enrolled. |
| S2.0 | Active | Student Status | Enrolled / enlisted student in good activity. |
| S2.1 | Active - Residency | Student Status | Registered for Residency activity. UG/GS/SOL only. |
| S2.2 | Active - Under LOA | Student Status | On an approved leave of absence within the max period. |
| S2.3 | Inactive - Prolonged Leave | Student Status | **New in Post-M3** (yellow highlight). LOA beyond max / last enrollment > 6 trimesters ago. |
| S3.1 | Inactive - AWOL | Student Status | Did not enroll and did not file LOA (Absent WithOut Leave). |
| S3.2 | Inactive - Suspended | Student Status | Disciplinary verdict given. |
| S4.0 | Graduated | Student Status | All program statuses are Graduated. |
| S4.1 | Exited on Good Standing | Student Status (Terminal) | University exit submitted, in good standing. |
| S4.2 | Exited - Permanent Disqualification | Student Status (Terminal) | Disciplinary verdict: non-readmission, dismissal/exclusion, or expulsion. |
| S3.5 | Exited - Under Exclusion | Student Status (Terminal) | **Deprecated** — struck through in M3; consolidated into S4.2 in Post-M3. |
| S3.6 | Exited - Expelled | Student Status (Terminal) | **Deprecated** — struck through in M3; consolidated into S4.2. |
| S3.7 | Inactive - Transferred | Student Status (Terminal) | **Deprecated** — struck through in M3. |

> **Older combination-tab scheme (do not mix with the above):** In `SEP 19 - Student/StudentProgramStatusesCombination`, codes are: `S1.0 Active - Without Enrollment`, `S2.0 Active`, `S2.1 Active - Residency`, `S2.2 Active - Under LOA`, `S3.0 Inactive - Graduated`, `S3.1 Inactive - AWOL`, `S3.2 Inactive - Exited`, `S3.3 Inactive - Suspended`, `S3.4 Inactive - Under Non-readmission`, `S3.5 Inactive - Under Exclusion`, `S3.6 Inactive - Expelled`, `S3.7 Inactive - Transferred`.

---

## Student Program Status codes (`P*`)

Canonical source: `SEP 26 Post-M3 WIP - StudentProgramStatuses`.

| Code | Meaning (Student Program Status) | Category | Notes / uncertainty |
|---|---|---|---|
| P1.0 | Eligible | Program Status | In good academic standing to continue in the program. |
| P1.1 | Probationary | Program Status | Did not fully meet academic requirements; on probation. |
| P1.2 | SNAS | Program Status | "SNAS criteria reached." Acronym not expanded in workbook (see SNAS below). |
| P1.3 | Strict Probationary | Program Status | **IS only** (yellow highlight). Probationary in prior AY + did not meet strict-probation criteria. = SAP in handbook. |
| P1.4 | Ineligible | Program Status (Terminal) | Program/strand retention rules breached. |
| P2.0 | Candidate for Graduation | Program Status | Passed first graduation eligibility check. |
| P3.0 | Graduated | Program Status (Terminal) | Passed final check; ~1 week after commencement. |
| P3.1 | Incomplete | Program Status (Terminal) | University exit submitted before completing the program. |
| — | Under Evaluation | Program Status | **Deprecated** — appeared as `P1.4 Under Evaluation` in M3 (shifting application), struck through; removed in Post-M3. |

> **Code-numbering (resolved in-repo):** The combination matrix has been regenerated against Post-M3 codes in `combination_matrix_post_m3.csv`. Legacy combo tab used P1.3 = Ineligible; canonical uses P1.3 = Strict Probationary, P1.4 = Ineligible. See `status_combination_rules.md`.

---

## Process / Time Period values

| Term | Meaning (from workbook) | Category |
|---|---|---|
| Admission Application | Process period while the applicant fills out/submits the application | Process |
| Admission Exam | Period covering the admission exam | Process |
| Admission Evaluation | Further evaluation of the application | Process |
| Admission Results | Period when admission results are released | Process |
| Official Acceptance | Period for paying the acceptance fee / submitting acceptance requirements (M3 called it "Official Confirmation") | Process |
| Enrollment during Admission Term/Semester | Enrollment window in the admission term | Process |
| Manage Grades | Process that drives the Eligible program status | Process |
| Manage Student Success | Process that drives SNAS / Ineligible transitions | Process |
| Determine Student Retention in a Program | Sub-process for retention decisions | Process |
| Assess Graduation Eligibility (First / Final Check) | Two-step graduation check (Candidate → Graduated) | Process |
| Manage Exit from the University | Process covering suspensions/exits (REC-0052) | Process |
| Leave of absence application | Process for LOA → Under LOA / Prolonged Leave | Process |

---

## Acronyms and key terms

| Term / Acronym | Meaning | Category | Notes / uncertainty |
|---|---|---|---|
| IS | Integrated School | Acronym (Level) | Confirmed by note "for IS, Probationary is applicable to both new and old students." |
| UG | Undergraduate | Acronym (Level) | Meaning inferred from context (appears as `IS/UG/GS/SOL`). |
| GS | Graduate School | Acronym (Level) | Meaning inferred from context. |
| SOL | School of Law | Acronym (Level) | Meaning inferred from context. |
| AY | Academic Year | Acronym | Used in "Probationary in previous academic year," "End of Previous AY." |
| LOA | Leave of Absence | Acronym / Condition | Student files for LOA → Under LOA (S2.2) or Prolonged Leave (S2.3). |
| AWOL | Absent WithOut Leave | Acronym / Status | Did not enroll and did not file LOA (S3.1). |
| SNAS | (Acronym not expanded in workbook) | Program Status / Acronym | **Definition unclear from workbook.** Defined only operationally: a status reached when "SNAS criteria reached." Commonly understood at DLSU as a student-success/academic-warning status; exact expansion not stated here. |
| SAP / Strict Academic Probation | "Strict Academic Probation (SAP)" — full name in the IS Student Handbook | Condition / Program Status | Notes: SAP is for "old students" only; modeled as `P1.3 Strict Probationary`. |
| OAS / OASIS | Office handling admission applications & requirements evaluation | Acronym / Process | Appears as "evaluated by OAS/OASIS," "OAS/OASIS requires applicant to resubmit." Exact office name not expanded; **inferred** to be the admissions office (commonly Office of Admissions and Scholarships / OASIS at DLSU). |
| SLC | System/platform a student accesses (campus + SLC system) | Acronym / System | **Definition unclear from workbook.** Notes say "If Active, student has access to campus and SLC system." Likely a student learning/portal system; not expanded. |
| REC-0052 | Reference number for "Exit from the University" | Process reference | Notes: "Exit from the University (REC-0052)" and "Manage Exit from the University." A process/record identifier. |
| REF-0002 | Reference number under which statuses are documented | Process reference | Notes: "scholarship statuses will not be documented under REF-0002." Identifier of this status documentation effort. Meaning inferred from context. |
| M3 | A working session / milestone label (e.g. "Sep19, M3") | Process label | Used in tab names. Exact expansion not given; treated as a meeting/milestone tag. |
| Official Acceptance | Process/period and the act of formally accepting an admission offer | Process / Condition | Post-M3 term; replaced M3's "Official Confirmation." |
| Official Acceptance Fee | Fee paid to confirm acceptance of the offer | Condition | Post-M3 term; replaced M3's "Enrollment Reservation Fee." Non-payment → A6.1 Cancelled. |
| Admission Term / Semester | The term/semester the applicant was admitted for | Time Period | Reference point for enrollment, deferral, and cancellation deadlines. |
| Terminal State | A status from which there is no forward transition (end of a lifecycle branch) | Condition | Labeled in-cell as "TERMINAL STATE." |
| Residency | A status for students registered for the Residency Activity (UG/GS/SOL) | Student Status | `S2.1 Active - Residency`. Typically thesis/dissertation residency; specifics not detailed. |
| Good Standing | A student "standing" reflecting acceptable academic/disciplinary/financial state | Condition | Notes: an Active student should have a "standing"; Good vs Bad/Poor. Also `S4.1 Exited on Good Standing`. |
| Clearance Hold | A hold placed/lifted as an outcome of conditions | Condition | Notes #4: "placing/lifting of a clearance hold is an outcome of the conditions." Open question whether "Graduated but with Clearance Hold" is a separate status. |
| Ineligible | Program status when retention rules are breached (terminal) | Program Status | `P1.4`. |
| Candidate for Graduation | Program status after passing the first graduation eligibility check | Program Status | `P2.0`. |
| Graduated | Terminal status; program (P3.0) and/or student (S4.0) fully completed | Program / Student Status | Student `S4.0` triggered when all programs are `P3.0 Graduated`. |
| Incomplete | Terminal program status when the student exits before completing the program | Program Status | `P3.1`. |
| Strand | A senior-high/track grouping that may require an exam or have cutoff scores | Term | Used alongside "Program" in exam/cutoff conditions. Meaning inferred from context. |
| Block Enrolled | Enrolled as part of a fixed block of subjects | Condition | "Student was Block Enrolled" appears in official-acceptance conditions. |
| Returnee | A student approved to return (re-enter Active - Without Enrollment) | Condition | "Student approved as returnee" → S1.0. |
| Enlisted | Reserved/registered for subjects (distinct from fully enrolled) | Condition | "Student is enlisted" is an OR condition for Active (S2.0). |
| Block / Disciplinary verdict | Decision from a disciplinary process | Condition | Drives Suspended (S3.2) and Exited - Permanent Disqualification (S4.2). |
| CHED Data Element Manual | External reference (Commission on Higher Education) | Reference | Notes tab references "Status as a student in good standing," "Status as a recipient of financial aid." |

### Active vs Inactive taxonomy (Post-M3, corrections #6)

| Bucket | Includes | Excludes |
|--------|----------|----------|
| **Active** (university activity) | S1.0 Without Enrollment, S2.0 Active, S2.1 Residency, S2.2 Under LOA | S2.3, S3.x, S4.x |
| **Inactive** | S2.3 Prolonged Leave, S3.1 AWOL, S3.2 Suspended, S4.0 Graduated, S4.1/S4.2 Exited | S2.2 Under LOA (classified Active-Under LOA on Post-M3 matrix) |

Notes tab #1 legacy wording grouped LOA/Graduated under Inactive; **Post-M3 matrix labels take precedence** per `decisions.md` Rule 3.

---

## Terms explicitly **not** modeled as statuses (per Notes tab #5)

These were considered but decided to be **types/processes**, not statuses:

| Item | Decision in workbook |
|---|---|
| Scholar / Scholarship | Will have a status but inside a scholarship *process*; not affecting access; **not documented under REF-0002**. |
| Foreign exchange (inbound/outbound) | Not a status — a *type* of student/enrollee ("On exchange program? Yes/No"). |
| Cross-enrollee | Not a status — a *type* of student/enrollee. |
| Transferee | Not a status — a *type* of student/enrollee. |
| Shifting | Handled via "Manage Shifting Application" *process*. |
| Optional Minor Program | Handled via "Apply for an Optional Minor Program" *process*. |
