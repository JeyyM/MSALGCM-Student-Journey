# Diagram Plan: PRG-02 — SNAS, Strict Probationary, and Ineligible

## Purpose

Academic warning and removal paths: SNAS, Strict Probationary (IS only), and terminal Ineligible.

## Source Files

- [`../student_program_status_flow.md`](../student_program_status_flow.md)
- [`student_program_status_transition_table.md`](student_program_status_transition_table.md)

## Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| P1.0 | P1_0 | P1.0 - Eligible | Active | Entry from PRG-01 |
| P1.1 | P1_1 | P1.1 - Probationary | Active | Entry from PRG-01 |
| P1.2 | P1_2 | P1.2 - SNAS | Active | |
| P1.3 | P1_3 | P1.3 - Strict Probationary (IS only) | Active | Post-M3 — keep |
| P1.4 | P1_4 | P1.4 - Ineligible [Terminal] | Terminal | |

## Included Transitions

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| PRG-T010 | P1_0 | P1_2 | SNAS criteria reached | High | |
| PRG-T011 | P1_2 | P1_0 | SNAS criteria not reached | High | |
| PRG-T014 | P1_1 | P1_3 | Strict probation (IS) | Medium | No numeric threshold on arrow |
| PRG-T015 | P1_3 | P1_0 | Criteria met — eligible | Medium | |
| PRG-T016 | P1_0 | P1_4 | Retention rules breached | High | |
| PRG-T017 | P1_1 | P1_4 | Retention rules breached | High | |
| PRG-T018 | P1_2 | P1_4 | Retention rules breached | High | |
| PRG-T019 | P1_3 | P1_4 | Retention / SAP failure | Medium | |

## Excluded States or Transitions

| Item | Reason |
|---|---|
| PRG-T060 | Low — SAP threshold deferred |
| PRG-T020 | Medium — optional v2 |

## Diagram Boundaries

**Includes:** P1.0/P1.1 ↔ P1.2 ↔ P1.3 → P1.4.  
**Excludes:** Graduation (PRG-03). Link to COMBO-T004 (ineligible + shift) in caption only.

## Recommended Mermaid Type

`stateDiagram-v2`

## Complexity Safeguards

- 5 states — at limit; P1_4 is single terminal sink — good hub pattern.
- Label P1_3 with "(IS only)" always.

## Open Questions

- SAP grade criteria (deferred) — do not put on diagram edge.
