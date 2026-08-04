# Student Status × Student Program Status — Combination Rules

**Canonical source (in-repo):** `src/data/combinationMatrix.js` and `documentation/workbook_patches/combination_matrix_post_m3.csv`

**Regenerated:** Post-M3 WIP codes (corrections.txt items 1–4, 28). Replaces the legacy combination tab scheme documented below for archival reference only.

> **Import into Excel:** See [`workbook_patches/README.md`](workbook_patches/README.md).

---

## Why treat Student Status and Program Status separately?

From the Notes tab (#3): *"Student Status and Student Program Status — recommendation is to treat these separately."* The combination matrix is a **validation layer** on top of two parallel FSMs (see `final mermaid code/combined_lifecycle/parallel_student_program_constrained_fsm.mmd`).

---

## Canonical code scheme (Post-M3)

**Student (10):** S1.0, S2.0, S2.1, S2.2, S2.3, S3.1, S3.2, S4.0, S4.1, S4.2

**Program (8):** P1.0, P1.1, P1.2, P1.3 (Strict Probationary, IS only), P1.4 (Ineligible), P2.0, P3.0, P3.1

**Matrix size:** 10 × 8 = **80 cells** (full CSV export).

### Legacy → Post-M3 migration

| Legacy (old combo tab) | Post-M3 (canonical) |
|------------------------|---------------------|
| S3.0 Inactive - Graduated | S4.0 Graduated |
| S3.2 Inactive - Exited | S4.1 Exited on Good Standing |
| S3.3 Inactive - Suspended | S3.2 Inactive - Suspended |
| S3.4–S3.7 terminal exits | S4.2 Exited - Permanent Disqualification |
| P1.3 Ineligible | **P1.4** Ineligible |
| *(none)* | **P1.3** Strict Probationary (IS only) |

---

## Cross-impact rules (unchanged)

| Rule | Trigger | Effect |
|------|---------|--------|
| COMBO-T001 | All programs → P3.0 | Student → S4.0 Graduated |
| COMBO-T003 | Student exit (S4.1) while program active | Program → P3.1 Incomplete |
| COMBO-T004 | P1.4 Ineligible + shift pending | Student → S1.0 Without Enrollment |
| COMBO-T005 | Shift approved | Student S1.0 → S2.0 Active |

P1.4 remains **terminal on the program**; shift is a cross-dimension process (corrections #10).

---

## Key valid pairs (examples)

- `S2.0 Active + P1.0 Eligible` — normal enrollment
- `S2.0 Active + P1.3 Strict Probationary` — IS SAP while enrolled
- `S4.0 Graduated + P3.0 Graduated` — primary end pair (COMBO-T001)
- `S3.1 AWOL + P1.0/P1.1/P1.2/P1.3/P1.4` — retains last academic standing

## Key invalid pairs (examples)

- `S1.0 Without Enrollment + P2.0 Candidate` — not enrolled
- `S2.0 Active + P3.0 Graduated` — graduated program forces S4.0
- `S2.2 Under LOA + P1.4 Ineligible` — explicitly blocked
- `S4.2 Permanent Disqualification + anything except P3.1` — terminal exit

## Executive defaults for uncertain cells

Former **Yes?** cells → **No** per `decisions.md` Rule 2. Exception documented: `S2.2 × P1.1` kept **Yes** pending stakeholder (#5). See [`executive_defaults.md`](executive_defaults.md).

---

## Full matrix

The complete 80-cell matrix with scenario notes is in:

- **CSV:** [`workbook_patches/combination_matrix_post_m3.csv`](workbook_patches/combination_matrix_post_m3.csv)
- **JS (validator):** [`../src/data/combinationMatrix.js`](../src/data/combinationMatrix.js)

---

## Archived — legacy combination tab (pre-regeneration)

<details>
<summary>Old scheme (do not use for new work)</summary>

The former `SEP 19 - Student/StudentProgramStatusesCombination` tab used S3.0 Graduated, S3.2 Exited, P1.3 Ineligible, and omitted S2.3, P1.3 Strict Probationary, and S4.x codes. That content is preserved in git history and the original workbook export. **Do not mix** legacy codes with Post-M3 diagrams or the validator.

</details>
