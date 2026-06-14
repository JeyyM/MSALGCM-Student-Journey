# DLSU Applicant / Student Journey Matrix — Documentation

This folder documents the workbook:

> `CSC615M Student_Applicant Journey Matrix [WORKING DRAFT] Applicant_Student Status.xlsx`

The workbook is a **working draft status matrix** that models the full lifecycle of a person interacting with De La Salle University (DLSU), from the moment they create an admission applicant account, through admission, enrollment, academic standing, leaves/exits, and finally graduation or other terminal outcomes.

It is a design / business-analysis artifact (not a database). Each tab is a matrix where **columns are individual statuses** and **rows are attributes** of those statuses (allowed previous status, applicable level, process/time period, activities/events, AND/OR conditions, etc.).

> **Important:** This documentation is descriptive. It reflects what the spreadsheet says, including its inconsistencies and unfinished sections. Where the workbook is ambiguous, this is explicitly flagged rather than guessed. The original workbook was **not** modified.

---

## What the workbook is about

The workbook breaks a person's relationship with the University into **four distinct status dimensions** that can change independently:

| Dimension | Question it answers | Example values |
|---|---|---|
| **Applicant / Admission Application Status** | "Where is this person in the *admission* pipeline?" | Draft, Submitted Form, Exam Required, Offered, Reserved, Officially Admitted |
| **Student Status** | "What is this person's overall standing *as a student* in the University?" | Active, Active - Without Enrollment, Active - Residency, Active - Under LOA, Inactive - AWOL, Inactive - Suspended, Graduated, Exited |
| **Student Program Status** | "How is this student doing inside their *academic program*?" | Eligible, Probationary, SNAS, Strict Probationary, Ineligible, Candidate for Graduation, Graduated, Incomplete |
| **Student + Student Program Status combination** | "Which pairings of the two student dimensions are *valid* together?" | e.g. `Active + Probationary` = allowed; `Under LOA + Candidate for Graduation` = not allowed |

The key conceptual point (stated explicitly in the Notes tab) is that **Student Status and Student Program Status are tracked separately** — one may or may not affect the other, and only certain combinations of the two are valid.

---

## The four status dimensions explained

### 1. Applicant / Admission Application Status (`A*` codes)
Describes the **admission funnel**: account creation → drafting an application → submitting → requirements/exam evaluation → admission results (offer/waitlist/redirect/reject) → reservation/official acceptance → officially admitted. It ends either in a terminal rejection/cancellation, or it "hands off" into a Student Status once the person is admitted and starts enrolling. This is an applicant-facing concept and largely disappears once the person becomes an enrolled student.

### 2. Student Status (`S*` codes)
Describes the person's **overall life as a student** once admitted: whether they are actively enrolled, on residency, on leave (LOA), absent without leave (AWOL), suspended, graduated, or have exited the University. It is essentially "is this student active or inactive, and why?"

### 3. Student Program Status (`P*` codes)
Describes the student's **academic standing within a specific academic program**: eligible to continue, on probation, on SNAS, on strict probation, ineligible (dropped from program), candidate for graduation, graduated, or incomplete. A student can be enrolled in more than one program, so this status is **per program**. Academic Standing directly drives this dimension.

### 4. Student + Student Program Status combinations
A cross-tab that enumerates every pairing of a Student Status with a Student Program Status and marks whether the pairing is allowed (`Yes` / `Yes?` / `No`), with scenario notes for the interesting cases.

---

## How the lifecycle generally flows

```
APPLICANT (A* codes)                STUDENT (S* + P* codes)
───────────────────────             ──────────────────────────────────────
account → draft → submit            Officially/Provisionally Admitted
   → requirements/exam              → Active - Without Enrollment (S1.0)
   → admission results              → enrolls → Active (S2.0) + Eligible (P1.0)
   → Offered → Reserved             → academic standing changes program status
   → Officially Admitted  ───────►  → LOA / Residency / AWOL / Suspended
                                     → Candidate for Graduation → Graduated
                                     → or Exited / Ineligible / Incomplete (terminal)
```

In words:

1. A person becomes an **applicant** and moves through the admission pipeline.
2. On **Official Acceptance / admission**, the admission application reaches a terminal "Officially Admitted" state and the person gains a **Student Status** (initially `Active - Without Enrollment`).
3. When they **enroll**, they become `Active` and their program(s) get a **Student Program Status** (normally `Eligible`, or `Probationary` if admitted on probation).
4. During their stay, Student Status shifts among Active / Residency / LOA / AWOL / Suspended depending on enrollment, leaves, and discipline; Student Program Status shifts among Eligible / Probationary / SNAS / Strict Probationary / Ineligible depending on academic performance.
5. The journey ends at a **terminal state**: Graduated, Exited (good standing or disqualification), Ineligible, Incomplete, or a cancelled/withdrawn admission.

A full plain-English walkthrough is in [`lifecycle_summary.md`](lifecycle_summary.md).

---

## The tabs (from the `Contents` tab)

| Group | Tab | Workbook's own description | Treated here as |
|---|---|---|---|
| (Admission) Applicant Statuses | `SEP 19 M3 - Applicant/StudentStatuses` | "tab discussed and edited during Sep19, M3" | Earlier draft |
| (Admission) Applicant Statuses | `SEP 19 Post-M3 WIP - Applicant/StudentStatuses` | "cleaned up version of above tab" | **Canonical (newer)** |
| Student Statuses | `SEP 19 M3 - StudentStatuses` | "tab discussed and edited during Sep19, M3" | Earlier draft |
| Student Statuses | `SEP 19 Post-M3 WIP - StudentStatuses` | "cleaned up version of above tab, and discussed and edited in Oct9, M3" | **Canonical (newer)** |
| Student Program Statuses | `SEP 26 M3 - StudentProgramStatuses` | "tab discussed and edited during Sep26, M3" | Earlier draft |
| Student Program Statuses | `SEP 26 Post-M3 WIP - StudentProgramStatuses` | "cleaned up version of above tab, and discussed and edited in Oct9, M3" | **Canonical (newer)** |
| Combination | `SEP 19 - Student/StudentProgramStatusesCombination` | (no description) | Reference (uses an older code scheme — see note below) |
| — | `SEP 19 - Notes` | (no description) | Background notes & open questions |

> **Naming note:** Excel truncates long tab names internally (e.g. `SEP 19 M3 - ApplicantStudentSta`), but the human-facing names in the `Contents` tab are the full ones shown above.

### Draft vs cleaned-up (WIP) versions

The workbook itself labels the **"Post-M3 WIP"** tabs as *"cleaned up version of the above tab."* These cleaned-up tabs are also the ones highlighted (cream/yellow fill) on the `Contents` tab and were further discussed on Oct 9. Following the analysis rules, **the Post-M3 WIP tabs are treated as canonical** wherever they conflict with the earlier M3 tabs. The earlier M3 tabs are retained mainly to show history and struck-through (deprecated) items. The most important M3 → Post-M3 changes are summarized in each flow document and in [`open_questions.md`](open_questions.md).

---

## Major assumptions made while interpreting the workbook

These assumptions were necessary to produce coherent documentation. They should be confirmed with stakeholders.

1. **Matrix orientation.** Each column = one status; the attribute rows above/below it (Allowed Previous, Applicable Levels, Process/Time Period, Activities/Events) all describe that same column's status. AND/OR cells stack vertically *under* the activity they connect.
2. **Post-M3 WIP wins.** Where M3 and Post-M3 disagree, the Post-M3 WIP values are authoritative, per the workbook's own labeling and the task instructions.
3. **Strikethrough = removed/deprecated.** Cells formatted with strikethrough (e.g. M3 statuses `Exited - Under Exclusion`, `Exited - Expelled`, `Inactive - Transferred`, `Under Evaluation`, `Exam Not Required`, and the entire "Applicant Status: Active/Inactive" row) are treated as **dropped** in the cleaned-up direction.
4. **Yellow / green highlights = newly added or "needs confirmation."** Yellow-filled cells (e.g. `Inactive - Prolonged Leave`, `Strict Probationary`, and the `Yes?` combination cells) are treated as recent additions or items the authors flagged as uncertain.
5. **"Officially Admitted" is the hand-off point.** The admission application reaching `A7.0 Officially Admitted` (terminal for the admission application) is the same event that gives the person Student Status `S1.0 Active - Without Enrollment`. The two dimensions overlap only at this hand-off.
6. **The combination tab uses an older code scheme.** The `SEP 19 - Student/StudentProgramStatusesCombination` tab encodes student statuses as `S3.0…S3.7` (Graduated/AWOL/Exited/Suspended/Non-readmission/Exclusion/Expelled/Transferred) and program statuses where `P1.3 = Ineligible`. This does **not** match the canonical Student Status tab (`S3.1 = AWOL`, `S4.x = Graduated/Exited`) nor the canonical Program Status tab (`P1.3 = Strict Probationary`, `P1.4 = Ineligible`). It is treated as an older, not-yet-reconciled mapping and flagged throughout.
7. **"Initial status" as a program start.** In the cleaned-up program tab, `Eligible` and `Probationary` list "Initial status" as an allowed previous, interpreted to mean the first program status assigned at enrollment (no prior program status).
8. **Levels abbreviations.** `IS/UG/GS/SOL` are taken to mean Integrated School / Undergraduate / Graduate School / School of Law (see [`glossary.md`](glossary.md)); only `IS` (Integrated School) is treated as fully certain from context, the rest are inferred.

---

## Document index

| File | Purpose |
|---|---|
| [`README.md`](README.md) | This overview |
| [`glossary.md`](glossary.md) | All codes, acronyms, and terms with meanings |
| [`applicant_status_flow.md`](applicant_status_flow.md) | Admission/applicant status flow + diagram |
| [`student_status_flow.md`](student_status_flow.md) | Student status lifecycle + diagram + edge cases |
| [`student_program_status_flow.md`](student_program_status_flow.md) | Academic program status flow + current/future-state notes |
| [`status_combination_rules.md`](status_combination_rules.md) | Allowed/blocked Student × Program combinations |
| [`lifecycle_summary.md`](lifecycle_summary.md) | Plain-English end-to-end walkthrough |
| [`open_questions.md`](open_questions.md) | Questions for stakeholders, grouped by topic |
| [`diagrams.md`](diagrams.md) | All Mermaid diagrams collected together |
| [`decisions.md`](decisions.md) | Go-forward rules for building the model/app (what to include, conflict handling) |
| [`diagram_planning/`](diagram_planning/README.md) | **Diagram planning layer** — transition tables and blueprints |
| [`mermaid_diagrams/`](mermaid_diagrams/README.md) | **Final Mermaid diagrams** — FSM-style diagrams by dimension + validation report |
