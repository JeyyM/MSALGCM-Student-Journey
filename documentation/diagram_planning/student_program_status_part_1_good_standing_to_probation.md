# Diagram Plan: PRG-01 — Eligible and Probationary

## Purpose

Program entry and early academic standing: initial Eligible or Probationary (from admission offer), and probation lifted back to Eligible.

## Source Files

- [`../student_program_status_flow.md`](../student_program_status_flow.md)
- [`student_program_status_transition_table.md`](student_program_status_transition_table.md)

## Included States

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| `[*]` | `[*]` | Program start | Start | |
| P1.0 | P1_0 | P1.0 - Eligible | Active | Normal admission |
| P1.1 | P1_1 | P1.1 - Probationary | Active | From A5.1 offer |

## Included Transitions

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| PRG-T001 | `[*]` | P1_0 | Normal admission | High | |
| PRG-T002 | `[*]` | P1_1 | Probationary admission offer | High | From A5.1 |
| PRG-T012 | P1_0 | P1_1 | Academic standards not met | Medium | |
| PRG-T013 | P1_1 | P1_0 | Probation lifted | Medium | End of AY |

## Excluded States or Transitions

| Item | Reason |
|---|---|
| P1.2, P1.3, P1.4 | PRG-02 |
| P2.0, P3.x | PRG-03 |
| PRG-T020 (SNAS → Probationary) | Medium — PRG-02 |

## Diagram Boundaries

**Includes:** Start → P1.0/P1.1 and P1.0 ↔ P1.1.  
**Excludes:** SNAS, SAP, ineligible, graduation.

## Recommended Mermaid Type

`stateDiagram-v2`

## Complexity Safeguards

- 2–3 states — minimal diagram; good early build candidate alongside APP-01.

## Open Questions

- Split PRG-T012 triggers in caption (new vs old student)?
