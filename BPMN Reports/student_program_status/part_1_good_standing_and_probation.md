# BPMN Report — Part 1: Good Standing & Probation

**Matching files:** [`part_1_good_standing_and_probation.bpmn`](../BPMN%20Code/student_program_status/part_1_good_standing_and_probation.bpmn) · [`part_1_good_standing_and_probation.mmd`](../final%20mermaid%20code/student_program_status/part_1_good_standing_and_probation.mmd)

---

## Purpose

Models **initial and ongoing program academic standing** between eligible and probationary — including admission-driven entry points.

**Status codes covered:** `P1.0`, `P1.1`

---

## Process summary

| Entry | Status | Meaning |
|-------|--------|---------|
| Normal admission | `P1.0` Eligible | Good standing |
| Probationary offer (A5.1) | `P1.1` Probationary | Conditional admission standing |
| Standards not met | `P1.0` → `P1.1` | Moved to probation |
| Probation lifted | `P1.1` → `P1.0` | Returned to eligible |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Two `[*]` entries in Mermaid | Two start events | Normal vs probationary admission |
| Bidirectional P1.0 ↔ P1.1 | Loop sequence flows | Year-end re-evaluation pattern |
| Program office only | Single primary lane + student lane unused | Office-driven academic standing |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **College / Program Office** | All standing assignments and reviews |

---

## BPMN strengths here

- **Dual start events** mirror two admission paths from [applicant_to_student_bridge](../combined_lifecycle/applicant_to_student_bridge.md).
- Simple loop readable for non-technical stakeholders.

## Limitations

- **Grade calculation rules** → DMN, not BPMN.
- Link from `A5.1` offer is narrative — traceability via bridge diagram.
- SNAS/SAP/ineligible deferred to Part 2.

---

## Related diagrams

- **Bridge:** [applicant_to_student_bridge](../combined_lifecycle/applicant_to_student_bridge.md)
- **Next:** [part_2_snas_sap_and_ineligible](part_2_snas_sap_and_ineligible.md)
