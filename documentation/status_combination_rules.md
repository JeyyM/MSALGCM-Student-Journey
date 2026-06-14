# Student Status × Student Program Status — Combination Rules

**Source:** `SEP 19 - Student/StudentProgramStatusesCombination`.

This tab enumerates every pairing of a **Student Status** with a **Student Program Status** and marks whether the combination is allowed: `Yes`, `Yes?` (allowed but flagged uncertain — yellow highlight), or `No`. Scenario notes explain the interesting cases.

> **Code-scheme caveat (read first).** This tab uses an **older code scheme** that does *not* match the canonical status tabs:
> - **Student statuses:** `S3.0 Inactive - Graduated`, `S3.1 Inactive - AWOL`, `S3.2 Inactive - Exited`, `S3.3 Inactive - Suspended`, `S3.4 Under Non-readmission`, `S3.5 Under Exclusion`, `S3.6 Expelled`, `S3.7 Transferred`. (The canonical Student tab uses `S3.2 = Suspended`, `S4.x = Graduated/Exited`.)
> - **Program statuses:** `P1.2 = SNAS`, **`P1.3 = Ineligible`** (no Strict Probationary). (The canonical Program tab uses `P1.3 = Strict Probationary`, `P1.4 = Ineligible`.)
>
> The labels below are reproduced exactly as in this tab. Reconciling these schemes is an open item — see [`open_questions.md`](open_questions.md).

---

## Why treat Student Status and Student Program Status separately?

From the Notes tab (#3):
> *"Student Status and Student Program Status — recommendation is to treat these separately."* Meaning the Student Status code is distinct from the Student Program Status code, and *"one may or may not impact the other."* *"There are allowed and not allowed combinations… For example, a student cannot have an 'Under LOA' student status and a 'Probationary' program status (not sure about this specific example)."*

The rationale:
- A student's **University-level standing** (active, on leave, suspended, exited) and their **academic standing in a program** (eligible, probationary, graduated) are genuinely independent concerns. A student can be `Active` while `Probationary`, or `Suspended` while still academically `Eligible`.
- Keeping them as separate codes avoids a combinatorial explosion of merged statuses and lets each dimension be driven by its own process (enrollment/discipline/leave vs grades/retention).
- But not *every* pairing makes sense (e.g. an `Inactive - Graduated` student cannot simultaneously be `Probationary`), so this tab acts as the **validation matrix** layered on top of the two independent dimensions.

---

## Full combination matrix

Legend: **Yes** = allowed · **Yes?** = allowed but flagged uncertain · **No** = not allowed.

| Student Status Code | Student Status | Program Status Code | Program Status | Allowed? | Scenario / Reason |
|---|---|---|---|---|---|
| S1.0 | Active - Without Enrollment | P1.0 | Eligible | Yes | |
| S1.0 | Active - Without Enrollment | P1.1 | Probationary | Yes | Admission Application status was Offered - Probationary. |
| S1.0 | Active - Without Enrollment | P1.2 | SNAS | No | |
| S1.0 | Active - Without Enrollment | P1.3 | Ineligible | Yes | "Ineligible to Program" triggers change to "Active - Without Enrollment" while waiting for a shift application to be approved; when approved, student becomes "Active." |
| S1.0 | Active - Without Enrollment | P2.0 | Candidate for Graduation | No | |
| S1.0 | Active - Without Enrollment | P3.0 | Graduated | No | |
| S1.0 | Active - Without Enrollment | P3.1 | Incomplete | No | |
| S2.0 | Active | P1.0 | Eligible | Yes | |
| S2.0 | Active | P1.1 | Probationary | Yes | |
| S2.0 | Active | P1.2 | SNAS | Yes | |
| S2.0 | Active | P1.3 | Ineligible | Yes | Possible only when the student has other programs where the program status is not "Ineligible." |
| S2.0 | Active | P2.0 | Candidate for Graduation | Yes | |
| S2.0 | Active | P3.0 | Graduated | No | |
| S2.0 | Active | P3.1 | Incomplete | No | |
| S2.1 | Active - Residency | P1.0 | Eligible | Yes | |
| S2.1 | Active - Residency | P1.1 | Probationary | **Yes?** | Flagged uncertain. |
| S2.1 | Active - Residency | P1.2 | SNAS | **Yes?** | Flagged uncertain. |
| S2.1 | Active - Residency | P1.3 | Ineligible | **Yes?** | Flagged uncertain. |
| S2.1 | Active - Residency | P2.0 | Candidate for Graduation | No | |
| S2.1 | Active - Residency | P3.0 | Graduated | No | |
| S2.1 | Active - Residency | P3.1 | Incomplete | No | |
| S2.2 | Active - Under LOA | P1.0 | Eligible | Yes | |
| S2.2 | Active - Under LOA | P1.1 | Probationary | Yes | (Contrast with Notes #3's tentative example that LOA+Probationary might not be allowed — here it is marked Yes.) |
| S2.2 | Active - Under LOA | P1.2 | SNAS | **Yes?** | Flagged uncertain. |
| S2.2 | Active - Under LOA | P1.3 | Ineligible | No | |
| S2.2 | Active - Under LOA | P2.0 | Candidate for Graduation | **Yes?** | Flagged uncertain. |
| S2.2 | Active - Under LOA | P3.0 | Graduated | No | |
| S2.2 | Active - Under LOA | P3.1 | Incomplete | No | |
| S3.0 | Inactive - Graduated | P1.0 | Eligible | No | |
| S3.0 | Inactive - Graduated | P1.1 | Probationary | No | |
| S3.0 | Inactive - Graduated | P1.2 | SNAS | No | |
| S3.0 | Inactive - Graduated | P1.3 | Ineligible | No | |
| S3.0 | Inactive - Graduated | P2.0 | Candidate for Graduation | No | |
| S3.0 | Inactive - Graduated | P3.0 | Graduated | Yes | The only valid pairing for a Graduated student. |
| S3.0 | Inactive - Graduated | P3.1 | Incomplete | No | |
| S3.1 | Inactive - AWOL | P1.0 | Eligible | Yes | |
| S3.1 | Inactive - AWOL | P1.1 | Probationary | Yes | |
| S3.1 | Inactive - AWOL | P1.2 | SNAS | Yes | |
| S3.1 | Inactive - AWOL | P1.3 | Ineligible | Yes | |
| S3.1 | Inactive - AWOL | P2.0 | Candidate for Graduation | No | |
| S3.1 | Inactive - AWOL | P3.0 | Graduated | No | |
| S3.1 | Inactive - AWOL | P3.1 | Incomplete | No | |
| S3.2 | Inactive - Exited | P1.0 | Eligible | No | If student is Eligible then Exited, program status changes to Incomplete. |
| S3.2 | Inactive - Exited | P1.1 | Probationary | No | If Probationary then Exited, program status changes to Incomplete. |
| S3.2 | Inactive - Exited | P1.2 | SNAS | No | If SNAS then Exited, program status changes to Incomplete. |
| S3.2 | Inactive - Exited | P1.3 | Ineligible | Yes | Student is tagged Ineligible then decided to Exit. |
| S3.2 | Inactive - Exited | P2.0 | Candidate for Graduation | Yes | Candidate for Graduation then decided to Exit. Low likelihood but possible. |
| S3.2 | Inactive - Exited | P3.0 | Graduated | No | If program status is Graduated, student status changes to Inactive - Graduated. |
| S3.2 | Inactive - Exited | P3.1 | Incomplete | Yes | |
| S3.3 | Inactive - Suspended | P1.0 | Eligible | Yes | |
| S3.3 | Inactive - Suspended | P1.1 | Probationary | Yes | |
| S3.3 | Inactive - Suspended | P1.2 | SNAS | Yes | |
| S3.3 | Inactive - Suspended | P1.3 | Ineligible | Yes | |
| S3.3 | Inactive - Suspended | P2.0 | Candidate for Graduation | **Yes?** | Flagged uncertain. |
| S3.3 | Inactive - Suspended | P3.0 | Graduated | No | If program status is Graduated, student status changes to Inactive - Graduated. |
| S3.3 | Inactive - Suspended | P3.1 | Incomplete | No | |
| S3.4 | Inactive - Under Non-readmission (Terminal) | P1.0–P2.0 | Eligible … Candidate | No | All non-terminal program statuses disallowed. |
| S3.4 | Inactive - Under Non-readmission (Terminal) | P3.0 | Graduated | No | |
| S3.4 | Inactive - Under Non-readmission (Terminal) | P3.1 | Incomplete | Yes | Only valid pairing. |
| S3.5 | Inactive - Under Exclusion (Terminal) | P1.0–P3.0 | Eligible … Graduated | No | |
| S3.5 | Inactive - Under Exclusion (Terminal) | P3.1 | Incomplete | Yes | Only valid pairing. |
| S3.6 | Inactive - Expelled (Terminal) | P1.0–P3.0 | Eligible … Graduated | No | |
| S3.6 | Inactive - Expelled (Terminal) | P3.1 | Incomplete | Yes | Only valid pairing. |
| S3.7 | Inactive - Transferred (Terminal) | P1.0–P3.0 | Eligible … Graduated | No | |
| S3.7 | Inactive - Transferred (Terminal) | P3.1 | Incomplete | Yes | Only valid pairing. |

---

## Patterns and key takeaways

### Examples of valid combinations
- `S2.0 Active + P1.0 Eligible` — the normal, healthy enrolled student.
- `S2.0 Active + P1.1 Probationary` / `+ P1.2 SNAS` — enrolled student with academic warnings.
- `S2.0 Active + P1.3 Ineligible` — allowed **only if** the student has *other* programs that are not Ineligible (multi-program students).
- `S3.1 AWOL + P1.0/P1.1/P1.2/P1.3` — an absent student retains whatever academic standing they last held.
- `S3.0 Inactive - Graduated + P3.0 Graduated` — the consistent end-state for a graduate.
- Every terminal exit status (`S3.4`–`S3.7`) pairs **only** with `P3.1 Incomplete`.

### Examples of invalid combinations
- `S1.0 Active - Without Enrollment + P2.0 Candidate for Graduation` — you cannot be a graduation candidate before enrolling.
- `S2.0 Active + P3.0 Graduated` — once a program is Graduated, the student status should become `Inactive - Graduated`, not stay Active.
- `S3.2 Exited + P1.0 Eligible` (or Probationary/SNAS) — exiting converts the program status to `Incomplete`, so an active academic standing cannot coexist with Exited.
- `S2.2 Under LOA + P1.3 Ineligible` — Ineligible is not allowed while on LOA.

### Cases where one status forces the other (cross-impact)
- **Graduated:** when a program reaches `P3.0 Graduated`, the **student status** is driven to `Inactive - Graduated` (`S3.0`). (Cells `BC10`, `BK10`.)
- **Exit:** when a student exits with an active academic standing (Eligible/Probationary/SNAS), the **program status** is driven to `P3.1 Incomplete`. (Cells `AX10`–`AZ10`.)
- **Ineligible + shift:** an `Ineligible` program status pushes the **student status** to `Active - Without Enrollment` while a shift application is pending; on approval it returns to `Active`. (Cell `E10`.)

### Cases where the two stay independent (separate)
- **Suspended / AWOL students keep their academic standing.** `S3.1 AWOL` and `S3.3 Suspended` allow the full range of active program standings (Eligible → Ineligible) — the University-level disruption does not erase the program-level academic standing.
- **Active students span all academic standings.** `S2.0 Active` is valid with Eligible, Probationary, SNAS, Ineligible (multi-program), and Candidate for Graduation — the two dimensions vary independently during normal enrollment.

### The "Yes?" (uncertain) cells to confirm
`S2.1 Residency × {Probationary, SNAS, Ineligible}`, `S2.2 Under LOA × {SNAS, Candidate for Graduation}`, and `S3.3 Suspended × Candidate for Graduation` are all marked **`Yes?`** (yellow) — explicitly flagged by the authors as needing confirmation.
