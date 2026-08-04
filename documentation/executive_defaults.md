# Executive Defaults (Corrections Implementation)

These defaults apply **where stakeholders have not yet confirmed**, so diagrams, the validator, and documentation can proceed without inventing new statuses. Each item cites the corrections.txt number and can be reversed when stakeholders decide otherwise.

> **Principle:** Prefer Post-M3 WIP + `decisions.md` Rule 2 (defer uncertain → **No**). Do not add statuses, thresholds, or processes not in the workbook.

---

## Stakeholder / deferred items

| # | Topic | Executive default | Rationale |
|---|--------|-------------------|-----------|
| 5 | LOA + Probationary | **Keep Yes** for `S2.2 × P1.1` in combo matrix; document Notes #3 conflict | Legacy combo explicitly Yes; changing to No would be a policy call |
| 7 | S4.0 terminal? | **Non-terminal for enrollment**; label **"Graduated [Alumni may continue]"** in diagrams | Workbook omits TERMINAL; supports BS/MS/alumni without inventing a new status |
| 8 | A5.4 → A5.5 appeal | **No appeal loop** in diagrams (per decisions.md Rule 2) | Mermaid/BPMN already omit A5.4; workbook allowed-previous is suspect |
| 16 | "Yes?" combo cells | **No** until confirmed | decisions.md Rule 2 — already applied in Post-M3 matrix |
| 17 | SAP grade threshold | **Parameter / TODO** — no numeric threshold in diagrams | Workbook note says "below 75 needs to be updated" |
| 18 | SNAS expansion | **Operational label only** in diagrams; glossary notes "expansion TBD" | No invented acronym expansion |
| 19 | LOA campus access | **Out of scope** for FSM; document as access attribute | Not a status transition |
| 20 | Clearance hold on Graduated | **Attribute `clearance_hold`**, not a status | Notes #7 recommendation |
| 21 | BS/MS post-graduation | **Linked to #7** — S4.0 non-terminal for enrollment | Defer ladderized rules until program office confirms |

---

## Inferred (not in legacy combo tab)

| # | Topic | Executive default | Rationale |
|---|--------|-------------------|-----------|
| 3 | Missing student rows in combo | **Full 10×8 matrix** added (see `combination_matrix_post_m3.csv`) | S2.3, S3.2, S4.x blocks derived from Post-M3 + legacy patterns |
| 15 | S2.3 Prolonged Leave pairs | **Mirror S3.1 AWOL** (retain P1.0–P1.4 except P2.0/P3.x) | Prolonged leave is inactive but retains last academic standing |
| 4 | P1.3 Strict Probationary pairs | **Yes** when S2.0/S3.1/S3.2; **No** when S1.0/S2.1/S2.2/S2.3/residency/LOA | IS SAP requires active enrollment track |
| 24 | A5.1 UG exclusion | **Annotate "(IS/GS/SOL only)"** on A5.1 in Mermaid/BPMN | Workbook levels column; UG excluded |

---

## Workbook-only (documented, not modeled)

| # | Action |
|---|--------|
| 6 | Revise Notes #1 taxonomy to match Post-M3 (see `workbook_patches/README.md`) |
| 11–14, 22–23, 25–27 | Patch instructions in `workbook_patches/README.md` |
| 25–26 | Typo/date fixes in Excel when next edited |

---

## Code migration (legacy → Post-M3)

| Legacy (combo tab) | Post-M3 (canonical) |
|--------------------|---------------------|
| S3.0 Inactive - Graduated | S4.0 Graduated |
| S3.2 Inactive - Exited | S4.1 Exited on Good Standing |
| S3.3 Inactive - Suspended | S3.2 Inactive - Suspended |
| S3.4–S3.7 terminal exits | S4.2 Exited - Permanent Disqualification |
| P1.3 Ineligible | **P1.4** Ineligible |
| *(new)* | **P1.3** Strict Probationary (IS only) |

See `src/data/combinationMatrix.js` → `LEGACY_CODE_MAP`.
