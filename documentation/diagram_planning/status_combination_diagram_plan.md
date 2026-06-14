# Diagram Plan: Status Combination (COMBO-01)

## Purpose

Plan how to represent **Student Status × Student Program Status** rules. **Primary recommendation: use a table/matrix, not Mermaid**, for the full combination grid.

Optional small diagram for **cross-impact rules only** (when one status forces another).

## Source Files

- [`../status_combination_rules.md`](../status_combination_rules.md)
- [`status_combination_transition_table.md`](status_combination_transition_table.md)
- [`../decisions.md`](../decisions.md)

## Recommended artifacts

| Artifact | Format | When |
|---|---|---|
| COMBO-01-full | Markdown table (canonical codes) | After code reconciliation |
| COMBO-01-legacy | Markdown table (combo tab codes) | Until reconciliation — per cascade rule |
| COMBO-01-impacts | `flowchart TD` or 5-node `stateDiagram-v2` | Optional; COMBO-T001–T004 only |

## Why not full Mermaid

- 91+ pairings — unreadable as graph.
- Code scheme mismatch (legacy vs canonical).
- Validation is binary (allowed/blocked), not sequential flow.

## Optional impact diagram — included nodes

| Node ID | Label | Type |
|---|---|---|
| S2_0 | S2.0 - Active | Student |
| P3_0 | P3.0 - Graduated | Program |
| S4_0 | S4.0 - Graduated | Student |
| S4_1 | S4.1 - Exited | Student |
| P3_1 | P3.1 - Incomplete | Program |

## Optional impact transitions

| Transition ID | Label | Certainty |
|---|---|---|
| COMBO-T001 | All programs P3.0 → S4.0 | High |
| COMBO-T003 | Exit + active program → P3.1 | High |
| COMBO-T004 | Ineligible + shift → S1.0 | High |

## Excluded from any COMBO diagram

| Item | Reason |
|---|---|
| All `Yes?` pairs | Deferred per decisions.md |
| Full grid as edges | Unreadable |
| Mixed legacy/canonical codes in one diagram | Cascade conflict |

## Diagram Boundaries

**Includes:** At most 5–7 nodes showing **forced updates** between dimensions.  
**Excludes:** Full combination matrix.

## Recommended Mermaid Type

**Table first.** If diagram: `flowchart TD` ( clearer for cross-dimension causality than stateDiagram-v2 ).

## Complexity Safeguards

- Do not draw 91 edges.
- Regenerate combination table with canonical codes before COMBO-01-full.

## Open Questions

- Reconcile combination tab before any COMBO artifact?
- LOA + Probationary: combo Yes vs Notes #3 tentative No

## Open Questions

See [`unclear_transitions.md`](unclear_transitions.md) — combination section.
