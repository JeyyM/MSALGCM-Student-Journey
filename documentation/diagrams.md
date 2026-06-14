# All Diagrams

All Mermaid diagrams for the DLSU applicant/student journey, collected in one place. Each uses `stateDiagram-v2`. Because Mermaid cannot draw double-circle "accepting" states, **terminal states are labeled `[TERMINAL]`** in their node text.

> Diagrams reflect the **Post-M3 WIP (canonical)** tabs. Transitions are derived from the matrices' "allowed previous status" relationships and condition rows; some directions are interpretations (see the per-flow docs and [`open_questions.md`](open_questions.md)).

---

## 1. Applicant / Admission Application Status flow

```mermaid
stateDiagram-v2
    [*] --> A0
    A0: A0 - Draft
    A1_0: A1.0 - Submitted Form
    A2_0: A2.0 - Submitted (Complete Reqs)
    A2_1: A2.1 - Submitted (Deficiencies)
    A3_0: A3.0 - Exam Required
    A3_1: A3.1 - Exam Exempted
    A3_2: A3.2 - Not Qualified (initial eval) [TERMINAL]
    A4_0: A4.0 - Exam Taken
    A4_1: A4.1 - Exam Pending
    A4_2: A4.2 - Not Qualified (no exam) [TERMINAL]
    A4_3: A4.3 - Further Evaluation Required
    A5_0: A5.0 - Offered
    A5_1: A5.1 - Offered - Probationary
    A5_2: A5.2 - Offered - Redirected
    A5_3: A5.3 - Waitlisted
    A5_4: A5.4 - Reconsidered
    A5_5: A5.5 - Not Qualified [TERMINAL]
    A6_0: A6.0 - Reserved
    A6_1: A6.1 - Cancelled (no acceptance fee) [TERMINAL]
    A7_0: A7.0 - Officially Admitted [TERMINAL -> Student]
    A7_1: A7.1 - Provisionally Admitted
    A7_2: A7.2 - Deferred
    A8_0: A8.0 - Cancelled (no reqs) [TERMINAL]
    A8_1: A8.1 - Cancelled - Withdrawal

    A0 --> A1_0: submitted
    A1_0 --> A2_0: requirements complete
    A1_0 --> A2_1: deficiencies
    A2_1 --> A2_0: resubmitted
    A2_0 --> A2_1: resubmission required
    A2_0 --> A3_0: exam required
    A2_0 --> A3_1: exam exempted
    A2_0 --> A3_2: not qualified (initial)
    A3_0 --> A4_0: exam taken
    A3_0 --> A4_1: exam pending
    A3_0 --> A4_2: no slots / lapsed
    A4_1 --> A4_0: exam taken
    A4_1 --> A4_2: lapsed
    A4_0 --> A4_3: further screening
    A2_0 --> A4_3: exam not required
    A3_1 --> A5_0: within cutoff
    A4_0 --> A5_0: within cutoff
    A4_3 --> A5_0: passed further eval
    A5_3 --> A5_0: slot opened
    A4_0 --> A5_1: probationary offer
    A4_3 --> A5_1: probationary offer
    A4_0 --> A5_2: redirected
    A3_1 --> A5_2: redirected
    A4_3 --> A5_2: redirected
    A4_0 --> A5_3: waitlisted
    A3_1 --> A5_3: waitlisted
    A4_3 --> A5_3: waitlisted
    A4_0 --> A5_5: outside cutoff
    A3_1 --> A5_5: outside cutoff
    A4_3 --> A5_5: outside cutoff
    A5_5 --> A5_4: appeal reconsidered
    A5_0 --> A6_0: fee paid/waived
    A5_1 --> A6_0: fee paid/waived
    A5_2 --> A6_0: fee paid/waived
    A5_4 --> A6_0: fee paid/waived
    A5_0 --> A6_1: did not pay
    A5_1 --> A6_1: did not pay
    A5_2 --> A6_1: did not pay
    A5_4 --> A6_1: did not pay
    A6_0 --> A7_0: reqs complete
    A6_0 --> A7_1: reqs pending
    A7_1 --> A7_0: reqs completed
    A6_0 --> A7_2: did not enroll
    A7_1 --> A8_0: 1 yr lapsed, no reqs
    A7_0 --> A8_1: withdrew in term
    A7_1 --> A8_1: withdrew in term
    A7_0 --> [*]: becomes Student (S1.0)
    A3_2 --> [*]
    A4_2 --> [*]
    A5_5 --> [*]
    A6_1 --> [*]
    A8_0 --> [*]
```

---

## 2. Student Status flow

```mermaid
stateDiagram-v2
    [*] --> S1_0: Officially Admitted (from A7.0)
    S1_0: S1.0 - Active - Without Enrollment
    S2_0: S2.0 - Active
    S2_1: S2.1 - Active - Residency
    S2_2: S2.2 - Active - Under LOA
    S2_3: S2.3 - Inactive - Prolonged Leave
    S3_1: S3.1 - Inactive - AWOL
    S3_2: S3.2 - Inactive - Suspended
    S4_0: S4.0 - Graduated
    S4_1: S4.1 - Exited on Good Standing [TERMINAL]
    S4_2: S4.2 - Exited - Permanent Disqualification [TERMINAL]

    S1_0 --> S2_0: enrolled / enlisted
    S2_0 --> S2_1: registered for Residency
    S2_1 --> S2_0: re-enrolled
    S2_0 --> S2_2: filed LOA (within max)
    S2_2 --> S1_0: returnee approved
    S2_0 --> S2_3: LOA beyond max / >6 trimesters
    S2_3 --> S1_0: returnee approved
    S2_0 --> S3_1: did not enroll, no LOA
    S2_1 --> S3_1: did not enroll, no LOA
    S1_0 --> S3_1: did not enroll, no LOA
    S3_1 --> S1_0: returnee approved
    S2_0 --> S3_2: disciplinary suspension
    S3_2 --> S2_0: suspension served / re-enrolled
    S2_0 --> S4_0: all programs Graduated
    S2_0 --> S4_1: University Exit (good standing)
    S2_1 --> S4_1: University Exit (good standing)
    S2_2 --> S4_1: University Exit (good standing)
    S2_3 --> S4_1: University Exit (good standing)
    S3_1 --> S4_1: University Exit (good standing)
    S3_2 --> S4_1: University Exit (good standing)
    S2_0 --> S4_2: dismissal / exclusion / expulsion
    S3_2 --> S4_2: dismissal / exclusion / expulsion
    S4_0 --> [*]
    S4_1 --> [*]
    S4_2 --> [*]
```

---

## 3. Student Program Status flow

```mermaid
stateDiagram-v2
    [*] --> P1_0: enrolled (normal)
    [*] --> P1_1: enrolled (probationary offer)
    P1_0: P1.0 - Eligible
    P1_1: P1.1 - Probationary
    P1_2: P1.2 - SNAS
    P1_3: P1.3 - Strict Probationary (IS only)
    P1_4: P1.4 - Ineligible [TERMINAL]
    P2_0: P2.0 - Candidate for Graduation
    P3_0: P3.0 - Graduated [TERMINAL]
    P3_1: P3.1 - Incomplete [TERMINAL]

    P1_0 --> P1_2: SNAS criteria reached
    P1_2 --> P1_0: SNAS criteria not reached
    P1_0 --> P1_1: academic standards not complied
    P1_1 --> P1_0: probation requirements complied
    P1_1 --> P1_3: probationary last AY, still failing (IS)
    P1_3 --> P1_0: criteria met to be Eligible
    P1_0 --> P1_4: retention rules breached
    P1_1 --> P1_4: retention rules breached
    P1_2 --> P1_4: retention rules breached
    P1_3 --> P1_4: retention rules breached
    P1_0 --> P2_0: graduation eligibility (first check)
    P2_0 --> P3_0: final check + commencement
    P1_0 --> P3_1: University Exit submitted
    P1_1 --> P3_1: University Exit submitted
    P1_2 --> P3_1: University Exit submitted
    P1_3 --> P3_1: University Exit submitted
    P2_0 --> P3_1: University Exit submitted
    P1_4 --> [*]
    P3_0 --> [*]
    P3_1 --> [*]
```

---

## 4. Combined high-level lifecycle flow

A simplified, end-to-end view across all three tracks. Composite states group the detailed statuses above.

```mermaid
stateDiagram-v2
    [*] --> Admission

    state Admission {
        [*] --> A0c
        A0c: Draft / Submitted / Evaluated
        Exam: Exam Required / Taken / Pending
        Results: Admission Results (Offered / Waitlist / Redirect)
        Accept: Reserved -> Officially Admitted
        Reject: Not Qualified / Cancelled [TERMINAL]
        A0c --> Exam
        A0c --> Results
        Exam --> Results
        Results --> Accept
        Results --> Reject
        Accept --> [*]
        Reject --> [*]
    }

    Admission --> StudentLife: Officially Admitted (A7.0)

    state StudentLife {
        [*] --> AWE
        AWE: S1.0 Active - Without Enrollment
        Active: S2.0 Active (+ Residency)
        Leave: Under LOA / Prolonged Leave / AWOL / Suspended
        AWE --> Active: enrolled
        Active --> Leave: LOA / no enroll / discipline
        Leave --> AWE: returnee approved
        Leave --> Active: re-enrolled
    }

    state ProgramStanding {
        [*] --> Standing
        Standing: Eligible / Probationary / SNAS / Strict Probationary
        Standing --> Ineligible: retention rules breached [TERMINAL]
        Standing --> Candidate: graduation first check
        Candidate: Candidate for Graduation
    }

    StudentLife --> ProgramStanding: runs in parallel (per program)

    ProgramStanding --> Graduated: final check
    Graduated: P3.0 / S4.0 Graduated [TERMINAL]
    StudentLife --> Exited: University Exit
    Exited: Exited (Good Standing / Permanent Disqualification) [TERMINAL]
    ProgramStanding --> Incomplete: exit before completion
    Incomplete: P3.1 Incomplete [TERMINAL]

    Graduated --> [*]
    Exited --> [*]
    Incomplete --> [*]
```

> **Note on the combined diagram:** `StudentLife` (student status) and `ProgramStanding` (program status) are *parallel* dimensions per the workbook's "treat separately" recommendation — the arrow between them denotes "run in parallel," not a single transition. Only certain pairings are valid; see [`status_combination_rules.md`](status_combination_rules.md).
