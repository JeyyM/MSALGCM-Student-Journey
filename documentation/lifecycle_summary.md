# Lifecycle Summary — The Full Journey in Plain English

This document explains the entire applicant → student journey for someone who has **never** seen the spreadsheet. It walks through the journey in 12 stages, using the workbook's actual status codes but explaining everything in ordinary language.

> **Mental model.** Think of three "tracks" that a person moves along, one after another but with some overlap:
> 1. **Admission track** (`A*` codes) — getting into the University.
> 2. **Student track** (`S*` codes) — being a student in the University.
> 3. **Program track** (`P*` codes) — academic standing inside a degree program (one per program).
>
> The admission track hands off to the student track at "Officially Admitted," and the student/program tracks then run side by side until graduation or exit.

---

## Stage 1 — Applicant account creation
A prospective student creates an **Admission Applicant account**. At this point there is no active application yet. (In the earlier draft this was an "Inactive" applicant state; the cleaned-up version drops the Active/Inactive applicant label entirely and treats the absence of an application simply as a starting point.)

## Stage 2 — Application draft
The applicant starts filling out the admission application but has not submitted it. **Status: `A0 Draft`.**

## Stage 3 — Application submission
The applicant submits the form (valid if submitted within the last 3 terms). **Status: `A1.0 Submitted Form`.** The admissions office (OAS/OASIS) then checks the supporting requirements:
- All requirements present → **`A2.0 Submitted - with Complete Requirements`.**
- Something missing or a resubmission is requested → **`A2.1 Submitted - with Deficiencies`** (and back to `A2.0` once fixed).

## Stage 4 — Requirements evaluation
OAS/OASIS evaluates the application and requirements. Three outcomes:
- The program/strand **requires an exam** → **`A3.0 Exam Required`.**
- The applicant is **exempted** from the exam → **`A3.1 Exam Exempted`.**
- The applicant **fails the initial evaluation** → **`A3.2 Not Qualified - Did not pass initial evaluation`** (a dead end / terminal state).

## Stage 5 — Exam required / pending / taken / not required
If an exam is required:
- Applicant takes it → **`A4.0 Exam Taken`.**
- Hasn't taken it yet but slots/reschedule window are open → **`A4.1 Exam Pending`.**
- Misses it (no slots / window lapsed) → **`A4.2 Not Qualified - Did not take Admission Exam`** (terminal).

If an exam isn't required, or further screening (interview, portfolio, etc.) is needed → **`A4.3 Further Evaluation Required`.**

## Stage 6 — Offer / admission results
Once results are released, the applicant lands in one of:
- **`A5.0 Offered`** — scores within the cutoff, or passed further evaluation.
- **`A5.1 Offered - Probationary`** — admitted but with extra requirements to keep their place (this later becomes a **Probationary** academic standing).
- **`A5.2 Offered - Redirected`** — didn't qualify for their choice but qualified for another program.
- **`A5.3 Waitlisted`** — qualified, but no slot yet; may get in if others decline.
- **`A5.5 Not Qualified`** — outside the cutoff (terminal). An appeal can move them to **`A5.4 Reconsidered`**.

## Stage 7 — Official acceptance
The applicant confirms their place:
- Pays (or is waived) the **Official Acceptance Fee** within the acceptance period → **`A6.0 Reserved`.** (Earlier draft called this the "Enrollment Reservation Fee" / "Official Confirmation.")
- Doesn't pay in time → **`A6.1 Cancelled - Due to non-payment of official acceptance fee`** (terminal).

Then they submit the **mandatory requirements for official acceptance**:
- Complete → **`A7.0 Officially Admitted`** (terminal *for the admission application*).
- Not yet complete → **`A7.1 Provisionally Admitted`** (they can still finish them).
- Provisional but never finish within 1 year → **`A8.0 Cancelled - non-submission of requirements`** (terminal).

**This is the hand-off point:** becoming Officially/Provisionally Admitted gives the person their first **Student Status**.

## Stage 8 — Transition into student status
On official/provisional admission, the person becomes a student with **Student Status `S1.0 Active - Without Enrollment`** — they're admitted but haven't enrolled in classes yet. Their program(s) start with **`P1.0 Eligible`** (or **`P1.1 Probationary`** if they were given a probationary offer).

If they never enroll and the late-enrollment window lapses → **`A7.2 Deferred`.** If they enroll but then withdraw during the admission term → **`A8.1 Cancelled - Withdrawal from University`.**

## Stage 9 — Enrollment / active student
When the student **enrolls or enlists**, their Student Status becomes **`S2.0 Active`** — the normal state of a student with full campus and SLC system access. Special active variants:
- **`S2.1 Active - Residency`** — registered for a Residency activity (UG/GS/SOL only; e.g. thesis residency).
- A student who hasn't enrolled yet but is still inside the late-enrollment grace period stays `Active`.

## Stage 10 — Academic program standing
Side by side with the student status, each program carries an **academic standing**, driven by grades and retention rules:
- **`P1.0 Eligible`** — good standing.
- **`P1.1 Probationary`** — didn't fully meet academic requirements; on probation.
- **`P1.2 SNAS`** — reached the "SNAS" academic-warning criteria.
- **`P1.3 Strict Probationary` (SAP)** — was probationary last year and still didn't meet criteria (IS only).
- **`P1.4 Ineligible`** — breached retention rules; removed from the program (terminal).

A student can recover (e.g. SNAS back to Eligible, probation lifted) or decline (probation → strict probation → ineligible) at end-of-year re-evaluations.

## Stage 11 — LOA / AWOL / suspension / exit cases
Life events change the **student status** without necessarily changing the program standing:
- **Files an LOA within the limit** → **`S2.2 Active - Under LOA`.**
- **LOA runs too long** (beyond max / >6 trimesters since last enrollment) → **`S2.3 Inactive - Prolonged Leave`.**
- **Doesn't enroll and doesn't file LOA** → **`S3.1 Inactive - AWOL`.**
- **Disciplinary suspension** → **`S3.2 Inactive - Suspended`.**
- **Returns from leave/AWOL** → back to `S1.0 Active - Without Enrollment`, then enrolls again.
- **Voluntary exit in good standing** → **`S4.1 Exited on Good Standing`** (terminal).
- **Disciplinary dismissal/exclusion/expulsion** → **`S4.2 Exited - Permanent Disqualification`** (terminal).

When a student exits with an active academic standing, the program standing flips to **`P3.1 Incomplete`** (terminal).

## Stage 12 — Graduation eligibility, then graduation or terminal exit
Toward the end of a program:
- Passing the **first graduation eligibility check** → program status **`P2.0 Candidate for Graduation`.**
- Passing the **final check** (about a week after commencement) → **`P3.0 Graduated`** (terminal).
- When **all** of a student's programs are Graduated, their student status becomes **`S4.0 Graduated`** (and, in the combination tab's wording, `Inactive - Graduated`).

The journey therefore ends in one of these **terminal outcomes:**

| Outcome | Codes |
|---|---|
| Graduated | `P3.0 Graduated` (program) → `S4.0 Graduated` (student) |
| Left in good standing | `S4.1 Exited on Good Standing` |
| Disciplinary disqualification | `S4.2 Exited - Permanent Disqualification` |
| Removed from program academically | `P1.4 Ineligible` |
| Exited mid-program | `P3.1 Incomplete` |
| Admission never completed | `A3.2`, `A4.2`, `A5.5`, `A6.1`, `A8.0` |

---

## One-paragraph version
A person creates an applicant account, drafts and submits an admission application, has their requirements and (if needed) exam evaluated, and receives an admission result — an offer, a probationary or redirected offer, a waitlist, or a rejection. If offered, they reserve their slot by paying the acceptance fee and submitting requirements, becoming **Officially Admitted**, which turns them into a student (`Active - Without Enrollment`). Once they enroll they are **Active**, and each of their programs gets an academic standing (Eligible, Probationary, SNAS, Strict Probationary, or Ineligible). Over time their student status may move through Residency, LOA, Prolonged Leave, AWOL, or Suspension, while their program standing tracks their grades. Eventually each program reaches Candidate for Graduation and then Graduated; when all programs are graduated the student is **Graduated**. Alternatively the journey ends in a terminal exit — good-standing exit, permanent disqualification, academic ineligibility, or an incomplete program.

> For the precise conditions, allowed transitions, edge cases, and unresolved questions behind each stage, see the per-dimension documents and [`open_questions.md`](open_questions.md).
