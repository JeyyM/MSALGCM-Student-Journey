# BPMN Report — Part 2: SNAS, SAP & Ineligible

**Matching files:** [`part_2_snas_sap_and_ineligible.bpmn`](../BPMN%20Code/student_program_status/part_2_snas_sap_and_ineligible.bpmn) · [`part_2_snas_sap_and_ineligible.mmd`](../final%20mermaid%20code/student_program_status/part_2_snas_sap_and_ineligible.mmd)

---

## Purpose

Models **academic warning and removal paths**: SNAS, strict probation (IS/SAP), and terminal ineligible standing.

**Status codes covered:** `P1.0`, `P1.1`, `P1.2`, `P1.3`, `P1.4`

---

## Process summary

| Transition | Meaning |
|------------|---------|
| `P1.0` ↔ `P1.2` | SNAS criteria reached / cleared |
| `P1.1` → `P1.3` | Strict probation (IS) |
| `P1.3` → `P1.0` | Criteria met |
| Any → `P1.4` | Retention / SAP failure — **terminal** |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Multiple paths to P1.4 | Converging flows to one end event | Retention breach from any standing |
| P1.4 terminal | End event | Program-level removal |
| IS-only P1.3 | Label on flow | Segment rule in sequence flow name |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **College / Program Office** | All academic standing updates |

---

## BPMN strengths here

- **Convergence to ineligible** shows one terminal outcome from many sources — good for retention policy discussion.
- SNAS recovery loop matches workbook re-evaluation cycle.

## Limitations

- **SNAS/SAP numeric thresholds** → DMN decision table.
- **COMBO-T004** (ineligible + shift → S1.0) in [cross_impact_rules](../combined_lifecycle/cross_impact_rules.md), not here.
- IS-only rule for P1.3 not enforceable in standard BPMN without conditional sequence flows (would need formal expressions).

---

## Related diagrams

- **Previous:** [part_1_good_standing_and_probation](part_1_good_standing_and_probation.md)
- **Cross-impact:** [cross_impact_rules](../combined_lifecycle/cross_impact_rules.md)
- **Next:** [part_3_graduation_and_terminal_states](part_3_graduation_and_terminal_states.md)
