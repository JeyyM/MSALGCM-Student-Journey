# The Student Journey at DLSU — How the Statuses Flow

This report explains, in plain language, how a person moves through the University's records — from the moment they apply, to becoming a student, to how they are doing in their program, and finally to how they leave (by graduating or exiting). It also explains how the diagrams in this folder fit together.

Think of it as a map of someone's whole journey, told in four connected sections.

---

## The big picture

Every person in the system is really moving through **one long journey**, but we track it in **four sections** because different offices care about different parts:

1. **Application & Admission** — "Are you getting into DLSU?"
2. **Student Standing** — "Are you currently an active student in the University?"
3. **Program Standing** — "How are you doing academically in your specific program?"
4. **Outcome** — "How did the journey end — graduated, or left?"

The first section happens **before** you are a student. Once you are admitted, sections 2 and 3 happen **at the same time** (in parallel): you always have a University-level standing *and* an academic standing, and they can change independently. Section 4 is simply how the story ends.

A "status" is just a labeled stage in the journey (for example, *Submitted Form* or *Active* or *Graduated*). Each status has a short code (like `A1.0` or `S2.0`) so staff can refer to them precisely. An **arrow** between two statuses means "this event moves you from one stage to the next."

---

## Section 1 — Application & Admission (the `A` codes)

This is the admission funnel: everything from creating an applicant account to officially getting in (or being turned away).

**The normal path, step by step:**

1. **Draft (`A0`)** — the applicant makes an account and starts an application.
2. **Submitted Form (`A1.0`)** — they submit the application.
3. **Complete Requirements (`A2.0`)** — all required documents are in. (If something is missing, they sit at **Deficiencies (`A2.1`)** until they fix it. The admissions office can also send a complete application back for re-submission.)
4. **Evaluation** — the office reviews the file. The applicant is told they either need to take the entrance exam (**`A3.0`**), are exempted from it (**`A3.1`**), or did not pass the initial review (**`A3.2`**, a dead end).
5. **The exam** — those who must take it become **Exam Taken (`A4.0`)**, **Exam Pending (`A4.1`)** while waiting, or **missed the exam (`A4.2`, a dead end)**. Some files need **Further Evaluation (`A4.3`)** like an interview or portfolio.
6. **Results** — the decision comes out: **Offered (`A5.0`)**, **Offered with conditions / Probationary (`A5.1`)**, **Redirected to another program (`A5.2`)**, **Waitlisted (`A5.3`)**, or **Not Qualified (`A5.5`, a dead end)**. A rejected applicant can sometimes appeal and be **Reconsidered (`A5.4`)**.
7. **Accepting the offer** — paying or waiving the acceptance fee makes them **Reserved (`A6.0`)**. Not paying in time cancels the offer (**`A6.1`**).
8. **Getting in** — once final requirements are done, they become **Officially Admitted (`A7.0`)** — or **Provisionally Admitted (`A7.1`)** if a few requirements are still pending.

**The hand-off:** "Officially/Provisionally Admitted" is the finish line for the *application* — but it is also the **start line for being a student**. At that moment the person becomes a student with the status **Active - Without Enrollment (`S1.0`)**. This is the bridge into Section 2.

A few applications end early without admission — deferral (`A7.2`), expired provisional admission (`A8.0`), or withdrawal (`A8.1`).

> **Diagrams:** `applicant_status/part_1` (account → submission), `part_2a` (exam & evaluation), `part_2b` (admission results), `part_3` (acceptance → becoming a student), `part_4` (all the dead ends and cancellations in one place).

---

## Section 2 — Student Standing (the `S` codes)

This is the person's **standing in the University as a whole** — not their grades, but whether they are an active, enrolled, on-leave, or departed student.

- **Active - Without Enrollment (`S1.0`)** — admitted (or returning) but not yet enrolled for the term.
- **Active (`S2.0`)** — the normal, enrolled student. This is the "home base" that most other statuses branch off from.
- **Active - Residency (`S2.1`)** — registered for a residency activity (e.g. thesis), for graduate-level students.
- **Active - Under LOA (`S2.2`)** — on an approved leave of absence within the allowed limit.
- **Inactive - Prolonged Leave (`S2.3`)** — a leave that ran longer than the maximum.
- **Inactive - AWOL (`S3.1`)** — did not enroll and did not file for leave.
- **Inactive - Suspended (`S3.2`)** — a disciplinary suspension.

**How it ends:** the student either **Graduates (`S4.0`)**, **Exits in good standing (`S4.1`)**, or is **permanently disqualified (`S4.2`)**. A student on leave, AWOL, or suspended can come back ("returnee") and re-enter the cycle.

> **Diagrams:** `student_status/part_1` (active & enrollment), `part_2` (residency & leave), `part_3` (AWOL, suspension & exit), `part_4` (graduation & terminal states).

---

## Section 3 — Program Standing (the `P` codes)

This runs **alongside** Section 2 and answers a different question: **how is the student doing academically inside a specific program?** (A student can be in more than one program, so this is tracked per program.)

- **Eligible (`P1.0`)** — good academic standing.
- **Probationary (`P1.1`)** — a warning level; must meet certain conditions.
- **SNAS (`P1.2`)** — another academic-warning level.
- **Strict Probationary (`P1.3`)** — a stricter warning (specific to certain levels).
- **Ineligible (`P1.4`)** — failed the program's retention rules; can no longer continue in that program.
- **Candidate for Graduation (`P2.0`)** — on track and cleared to graduate.
- **Graduated (`P3.0`)** — finished the program.
- **Incomplete (`P3.1`)** — the program ended without finishing (for example, because the student left the University).

The warning levels can move up and down: a probationary student who improves goes back to eligible; one who keeps struggling can become ineligible.

> **Diagrams:** `student_program_status/part_1` (good standing & probation), `part_2` (SNAS, strict probation & ineligible), `part_3` (graduation & terminal states).

---

## How the four sections connect

This is the part that often confuses people, so here it is simply:

**1. The bridge (Application → Student).**
Getting admitted (`A7.0`/`A7.1`) automatically makes the person a student (`S1.0`) and gives their program a starting standing (`P1.0 Eligible`, or `P1.1 Probationary` if the offer was a probationary one). After that, the admission section is finished.

**2. Two tracks running at once.**
Once someone is a student, **Student Standing (Section 2) and Program Standing (Section 3) move independently and at the same time.** For example, a student can be `Active` in the University while being `Probationary` in their program. Most of the time, one does not control the other.

**3. Only some combinations are allowed.**
Because the two tracks are independent, we have to say which *pairs* make sense and which do not. For example:
- `Active` + `Probationary` — fine.
- `Without Enrollment` + `Candidate for Graduation` — **not allowed** (you can't be cleared to graduate before you've even enrolled).
- `Active` + `Graduated` — **not allowed** (finishing the program should move the student to Graduated).

This list of allowed/blocked pairs is the **validation layer**. It is kept as a table rather than a diagram because there are dozens of combinations.

**4. A few events force both tracks to update together.**
In a handful of special cases, a change in one track *forces* a change in the other. These are the only true crossover rules:

| When this happens | This is forced |
|---|---|
| All of a student's programs reach **Graduated** | The student becomes **Graduated (`S4.0`)** |
| A student **exits** while a program is still active | That program becomes **Incomplete (`P3.1`)** |
| A program becomes **Ineligible** and the student files to shift | The student becomes **Without Enrollment (`S1.0`)** while waiting |
| The shift is **approved** | The student becomes **Active (`S2.0`)** again in the new program |

> **Diagrams:** `combined_lifecycle/high_level_lifecycle_overview` (the whole journey at a glance), `applicant_to_student_bridge` (the hand-off), `student_status_vs_program_status_interaction` (the parallel tracks + allowed pairs), `parallel_student_program_constrained_fsm` (the full integrated picture), and `cross_impact_rules` (just the four crossover rules above).

---

## Section 4 — Outcome

Every journey ends in one of a few ways:

- **Graduated** — completed the program(s) and the University standing becomes Graduated.
- **Exited on good standing** — left voluntarily, in good standing.
- **Permanently disqualified** — left due to a disciplinary decision.
- **Cancelled / not admitted** — the journey ended back in the admission section (rejected, lapsed, or withdrawn).

---

## A quick map of all the diagrams

| Section | Diagrams (in this folder) | What they show |
|---|---|---|
| 1. Application & Admission | `applicant_status/part_1` … `part_4` | The full admission funnel and its dead ends |
| 2. Student Standing | `student_status/part_1` … `part_4` | University-level standing over time |
| 3. Program Standing | `student_program_status/part_1` … `part_3` | Academic standing within a program |
| Connections | `combined_lifecycle/…` | The hand-off, the two parallel tracks, allowed pairs, and crossover rules |

**How to read any diagram:** each **box** is a status (a stage), and each **arrow** is the event that moves you from one status to the next. A **solid** arrow stays within one section; a **dotted** arrow in the combined diagrams crosses between the Student and Program tracks. Boxes marked *Terminal* are end points.

---

## Appendix — viewing the diagrams

The files in this folder are written in **Mermaid**, a simple text format for diagrams. To view or edit one:

1. Open [diagrams.net (draw.io)](https://app.diagrams.net).
2. Go to **Arrange → Insert → Advanced → Mermaid…**
3. Open any `.mmd` file, copy all of its text, paste it in, and insert.

For the deeper write-ups behind each diagram, see the `documentation/` folder in this project (full status tables, the complete list of allowed combinations, and open questions still awaiting confirmation).
