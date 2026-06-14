# Go-Forward Decisions (for building the model / app)

These are the working rules agreed for **future implementation** (data model, app, etc.). They do **not** change the rest of the `documentation/` folder, which intentionally keeps the *complete* record — including deprecated and uncertain items — so we don't lose history. This file is the filter to apply when we turn that record into something real.

> Status: working agreement. Revisit if stakeholders answer the items in [`open_questions.md`](open_questions.md).

---

## Rule 1 — Strikethrough items are excluded

Anything struck through in the workbook is **dropped** from the model going forward. Concretely, do **not** include:

| Dimension | Excluded (struck-through) item | Notes |
|---|---|---|
| Applicant | `A3.3 Exam Not Required` | Folded away; exam-not-required is handled via `A4.3 Further Evaluation Required`. |
| Applicant | `A9.0 Inactive` + the whole "Applicant Status: Active/Inactive" row | Per the tab note, there is no Inactive applicant status; those conditions are only for data-purge. |
| Student | `S3.5 Exited - Under Exclusion` | Consolidated into `S4.2 Exited - Permanent Disqualification`. |
| Student | `S3.6 Exited - Expelled` | Consolidated into `S4.2`. |
| Student | `S3.7 Inactive - Transferred` | Removed; "Transferee" is a *type*, not a status. |
| Program | `Under Evaluation` (M3 `P1.4`) + the shifting-application activity | Shifting is a *process* ("Manage Shifting Application"), not a status. |

## Rule 2 — "Needs confirmation" items are excluded (deferred)

Items the authors explicitly flagged as uncertain are **left out until confirmed**. Concretely:

| Where | Item | How to treat for now |
|---|---|---|
| Combination tab | The `Yes?` cells: `S2.1 Residency × {Probationary, SNAS, Ineligible}`, `S2.2 Under LOA × {SNAS, Candidate for Graduation}`, `S3.3 Suspended × Candidate for Graduation` | Treat as **not allowed** (do not model as valid combinations) until confirmed. |
| Program tab | SAP grade threshold ("below 75 needs to be updated") and the "kindly confirm if correct" Grade 1/2/3 example | Do not hard-code the threshold; leave it as a parameter / TODO. |
| Anywhere | Items raised in [`open_questions.md`](open_questions.md) | Defer; don't bake unconfirmed assumptions into the schema. |

### Clarification — "new" highlights are NOT "needs confirmation"
Some cells are highlighted simply because they are **newly added in the cleaned-up (Post-M3) tabs**, not because they're uncertain. These are **kept** (they are part of the latest canonical model, per Rule 3):

- `S2.3 Inactive - Prolonged Leave` — **keep.**
- `P1.3 Strict Probationary` (IS only) — **keep.**

> If you actually want these two treated as "needs confirmation / exclude" too, say so and they'll be moved into Rule 2.

## Rule 3 — Conflicts: prefer the latest, unless it cascades

When tabs disagree:

1. **Default: use the latest (Post-M3 WIP) version.** Examples already adopted:
   - Terminology: **Official Acceptance** / **Official Acceptance Fee** (not the M3 "Official Confirmation" / "Enrollment Reservation Fee").
   - Student exits consolidated into `S4.0 Graduated`, `S4.1 Exited on Good Standing`, `S4.2 Exited - Permanent Disqualification`.
   - Program statuses: `P1.0 Eligible`, `P1.1 Probationary`, `P1.2 SNAS`, `P1.3 Strict Probationary`, `P1.4 Ineligible`, `P2.0 Candidate for Graduation`, `P3.0 Graduated`, `P3.1 Incomplete`.

2. **Exception: if adopting the latest would cause cascading breakage, keep the older scheme** (favor internal consistency over freshness).
   - **Known cascade — program-status code numbering.** The combination tab (`SEP 19 - Student/StudentProgramStatusesCombination`) is built on the *older* numbering where `P1.2 = SNAS` and **`P1.3 = Ineligible`** (no Strict Probationary code). Re-numbering to the new `P1.3 = Strict Probationary` / `P1.4 = Ineligible` breaks every reference in that tab.
     - **Decision:** until the combination tab is regenerated against the new codes, **keep the old numbering when working *with the combination matrix*** so its rows stay valid. Use the new numbering everywhere else. Reconcile both into one scheme as a dedicated task (tracked in `open_questions.md` #11, #36).
   - **Known cascade — older student exit codes (`S3.0`–`S3.7`) in the combination tab.** The combination tab also uses the old student-status codes (`S3.0 Graduated`, `S3.2 Exited`, `S3.3 Suspended`, etc.). Same rule: keep them old *within that matrix* until it's regenerated; use the canonical `S*` codes everywhere else.

> Rule of thumb: "latest wins" for individual values/labels; "don't half-migrate" for code schemes that other tabs depend on — migrate the whole web at once or not at all.

---

## Quick reference — what survives into the model

**Applicant (A):** A0, A1.0, A2.0, A2.1, A3.0, A3.1, A3.2, A4.0, A4.1, A4.2, A4.3, A5.0, A5.1, A5.2, A5.3, A5.4, A5.5, A6.0, A6.1, A7.0, A7.1, A7.2, A8.0, A8.1.
~~A3.3, A9.0~~ (excluded).

**Student (S):** S1.0, S2.0, S2.1, S2.2, S2.3, S3.1, S3.2, S4.0, S4.1, S4.2.
~~S3.5, S3.6, S3.7~~ (excluded; merged into S4.2 / dropped).

**Program (P):** P1.0, P1.1, P1.2, P1.3, P1.4, P2.0, P3.0, P3.1.
~~Under Evaluation~~ (excluded).

**Deferred (not modeled until confirmed):** all `Yes?` combinations, SAP grade thresholds, and everything in `open_questions.md`.
