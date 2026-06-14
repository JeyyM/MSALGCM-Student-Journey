# Status Combination Transition Table

**Purpose:** This table documents **cross-dimension impacts** — when a change in one status *drives* or *constrains* another. These are **not** single-dimension state transitions; most are validation rules or forced updates.

**Sources:**  
- [`../status_combination_rules.md`](../status_combination_rules.md) (combination tab — **legacy code scheme**)  
- [`../decisions.md`](../decisions.md) (canonical codes for new diagrams; legacy for COMBO matrix until reconciled)

---

## Cross-impact rules (canonical codes where possible)

| Transition ID | From (Student) | From (Program) | To (Student) | To (Program) | Trigger/Event | Conditions | Source | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| COMBO-T001 | S2.0 Active | P3.0 Graduated | S4.0 Graduated | P3.0 Graduated | All programs graduated | Program status of all programs is Graduated | student_status_flow.md § S4.0 | High | Student status driven by program |
| COMBO-T002 | S2.0 Active | P3.0 Graduated (one of many) | S2.0 Active | P3.0 Graduated | Partial graduation | Multi-program; not all programs graduated | status_combination_rules.md | Medium | Stay Active until all P3.0 |
| COMBO-T003 | S2.0 Active | P1.0/P1.1/P1.2 Eligible/Prob/SNAS | S4.1 Exited | P3.1 Incomplete | University exit | Exit while active academic standing | status_combination_rules.md § AX10–AZ10 | High | Program → Incomplete on exit |
| COMBO-T004 | S2.0 Active | P1.4 Ineligible | S1.0 Active - Without Enrollment | P1.4 Ineligible | Ineligible + shift pending | Waiting for shift approval | status_combination_rules.md § E10 | High | Student status driven by ineligible+shift |
| COMBO-T005 | S1.0 Active - Without Enrollment | P1.4 Ineligible | S2.0 Active | P1.0/P1.1 (new program) | Shift approved | Shift application approved | status_combination_rules.md § E10 | Medium | Implied second half |
| COMBO-T006 | S2.0 Active | P2.0 Candidate | S4.1 Exited | P2.0 or P3.1 | Exit while candidate | Low likelihood | status_combination_rules.md § BB10 | Medium | Combination allows Exited + Candidate |
| COMBO-T007 | Any Active | P1.4 Ineligible | S2.0 Active | P1.4 Ineligible | Multi-program ineligible | Allowed only if other programs not Ineligible | status_combination_rules.md § M10 | High | Validation rule |
| COMBO-T008 | S2.2 Under LOA | P1.4 Ineligible | — | — | Blocked combination | Not allowed | status_combination_rules.md | High | **No** — do not depict as valid state pair |

---

## Validation rules (allowed / blocked pairs) — canonical student × program

Use **matrix rows**, not Mermaid edges. Sample of high-value rules:

| Rule ID | Student Code | Program Code | Allowed? | Scenario | Certainty | Diagram approach |
|---|---|---|---|---|---|---|
| COMBO-R001 | S1.0 | P1.0 | Yes | Admitted, not enrolled, eligible | High | Table only |
| COMBO-R002 | S1.0 | P1.1 | Yes | Probationary offer | High | Table only |
| COMBO-R003 | S1.0 | P1.2 SNAS | No | — | High | Table only |
| COMBO-R004 | S2.0 | P3.0 | No | Graduated program forces student change | High | Cross-impact COMBO-T001 |
| COMBO-R005 | S4.0 Graduated | P3.0 | Yes | Only valid graduate pair (combo tab: S3.0+P3.0) | High | Reconcile codes first |
| COMBO-R006 | S2.2 | P1.1 | Yes | Notes #3 vs combo tab conflict | Medium | Table; note uncertainty |
| COMBO-R007 | S2.1 | P1.1/P1.2/P1.4 | Yes? | Deferred per decisions.md | **Low** | **Exclude** until confirmed |

---

## Legacy combination tab mapping (for COMBO-01 matrix artifact only)

When reproducing the **original combination tab**, use this mapping — **not** for canonical STU/PRG diagrams:

| Combination tab code | Canonical equivalent (approx.) |
|---|---|
| S3.0 Inactive - Graduated | S4.0 Graduated |
| S3.1 Inactive - AWOL | S3.1 Inactive - AWOL |
| S3.2 Inactive - Exited | S4.1 Exited on Good Standing (partial) |
| S3.3 Inactive - Suspended | S3.2 Inactive - Suspended |
| P1.3 Ineligible (combo tab) | P1.4 Ineligible (canonical) |
| (no Strict Probationary in combo) | P1.3 Strict Probationary — **gap** |

---

## Transitions excluded from future diagrams

| Possible Transition | Reason Excluded | What Needs Confirmation |
|---|---|---|
| Full 91-cell combination as Mermaid | Unreadable; use table | Code scheme reconciliation |
| All `Yes?` pairs as valid edges | Deferred per decisions.md | Stakeholder confirmation |
| LOA + Probationary as forbidden edge | Combo says Yes; Notes #3 tentative No | Which source wins? |
| Strict Probationary combinations | Not in combination tab | Regenerate combo tab |

## Recommended artifact for COMBO-01

**Primary:** Markdown validation matrix (regenerated with canonical codes).  
**Optional secondary:** Small `flowchart TD` with 4–5 nodes showing COMBO-T001, T003, T004 only — not the full grid.
