# Workbook Patch Guide

Instructions for applying `corrections.txt` items to **Applicant_Student Status.xlsx** when you next edit it. The Excel file is not in this repo; these patches are the authoritative target state.

**Already done in-repo (no Excel needed):**

- Post-M3 combination matrix → `combination_matrix_post_m3.csv` (80 cells)
- Validator → `src/data/combinationMatrix.js`
- Diagrams → `final mermaid code/` + `BPMN Code/` folders 1–4
- Executive defaults → `documentation/executive_defaults.md`

---

## Phase 2 — Combination tab regeneration (items 1, 2, 3, 4, 9, 10, 28)

**Sheet:** `SEP 19 - Student/StudentProgramStatusesCombination`

1. Add banner row: *"Regenerated against Post-M3 codes — see documentation/status_combination_rules.md"*
2. **Student columns** — use all Post-M3 codes:
   - S1.0, S2.0, S2.1, S2.2, **S2.3**, S3.1, **S3.2**, **S4.0**, **S4.1**, **S4.2**
   - Remove/replace legacy S3.0 Graduated → **S4.0**
   - Remove S3.2 Exited → **S4.1**; S3.3 Suspended → **S3.2**
   - Collapse S3.4–S3.7 → **S4.2** only
3. **Program columns** — use Post-M3 codes:
   - P1.0, P1.1, P1.2, **P1.3 Strict Probationary (IS only)**, **P1.4 Ineligible**, P2.0, P3.0, P3.1
   - Migrate every legacy **P1.3 = Ineligible** cell to **P1.4**
4. Import **`combination_matrix_post_m3.csv`** (StudentCode × ProgramCode × Allowed × ScenarioReason)
5. Re-validate cross-impact scenarios E10 (shift) → reference **P1.4**, not legacy P1.3
6. Replace all **Yes?** with **No** (or stakeholder-confirmed Yes) per `executive_defaults.md` #16

---

## Phase 3 — Workbook prose / archive (items 6, 11–15, 22–27)

| Item | Tab / location | Patch |
|------|----------------|-------|
| 6 | Notes #1 | Align Active/Inactive taxonomy with Post-M3: Active = S1.x, S2.0–S2.2; Inactive = S2.3, S3.x, S4.x |
| 11 | M3 archive tabs | Banner: *"Superseded — see Post-M3 WIP"* |
| 12 | M3 Applicant | Strike full A9.0 column; note *"A3.3, A9.0 removed in Post-M3"* |
| 13 | M3 / combo | Remove S3.5–S3.7 references; use S4.2 |
| 14 | docs | Legacy map in `status_combination_rules.md` (done in-repo) |
| 15 | Student tab + combo | Confirm S2.3 entry rule with stakeholders; add S2.3 block to combo (CSV has inferred pairs) |
| 22 | Applicant tab | One A7.0 → S1.0; enrollment S1.0 → S2.0 separate (see Mermaid bridge) |
| 23 | Applicant rows 8–9 | Note: *"No student status until A7.0/A7.1"* for A7.2 |
| 24 | Applicant A5.1 | Add level note: IS/GS/SOL only (diagrams already annotated) |
| 25 | Contents | Update date vs tab names |
| 26 | Post-M3 Applicant | Fix typo *Combinaiton* → *Combination* |
| 27 | Post-M3 Applicant row 6 | Move/comment struck Active/Inactive row |

---

## Phase 1 — Stakeholder sign-off (items 5, 7, 8, 16–21)

See **`documentation/executive_defaults.md`** for interim defaults applied in diagrams/validator until confirmed.

---

## Importing the CSV into Excel

1. Open a new sheet or replace the combo matrix body (keep headers).
2. Data → Get Data → From Text/CSV → `combination_matrix_post_m3.csv`
3. Pivot or VLOOKUP into the existing Yes/No grid layout if needed.
4. Yellow-highlight cells that still say *pending stakeholder* (S2.2×P1.1 only).

Run `python documentation/workbook_patches/export_matrix_csv.py` to regenerate the CSV after editing `combinationMatrix.js`.
