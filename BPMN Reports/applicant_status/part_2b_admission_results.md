# BPMN Report — Part 2B: Admission Results

**Matching files:** [`part_2b_admission_results.bpmn`](../BPMN%20Code/applicant_status/part_2b_admission_results.bpmn) · [`part_2b_admission_results.mmd`](../final%20mermaid%20code/applicant_status/part_2b_admission_results.mmd)

---

## Purpose

Models the **admission decision** after evaluation: offer types, waitlist, and rejection — from any qualifying entry state (`A3.1`, `A4.0`, `A4.3` collapsed to a single start).

**Status codes covered:** `A5.0`, `A5.1`, `A5.2`, `A5.3`, `A5.5`

---

## Process summary

| Outcome | Status | Meaning |
|---------|--------|---------|
| Within cutoff | `A5.0` Offered | Standard admission offer |
| Probationary | `A5.1` | Offer with academic conditions |
| Redirected | `A5.2` | Alternate program offer |
| Waitlisted | `A5.3` | Qualified, no slot yet |
| Outside cutoff | `A5.5` | Terminal — not qualified |
| Slot opened | `A5.3` → `A5.0` | Waitlist promotion |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Three entry states in Mermaid | Single start “After evaluation” | Boundary simplification; entries documented in Part 2A |
| Decision outcomes | XOR gateway “Admission decision” | Classic BPMN decision pattern |
| Waitlist loop | `A5.3` → `A5.0` | Event-driven promotion |
| Offers → acceptance | End event in Applicant lane | Hand-off to Part 3 |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **OAS / Admissions Office** | Decision gateway, all A5.x status assignments |
| **Applicant** | Receives offer (end event → Part 3 acceptance) |

---

## BPMN strengths here

- **Single decision gateway** is ideal checkpoint material for “BPMN + DMN” discussion — gateway could call a DMN table for cutoff logic.
- Waitlist re-entry is a clear exception path without extra notation.
- All offer types visible at one glance.

## Limitations

- **A5.4 Reconsidered** (appeal) not in this granular slice — add in extended model or Part 4.
- Cutoff scores, strand rules → **DMN**, not drawn here.
- Merged entry from `A3.1`/`A4.0`/`A4.3` loses per-path labels; traceability in Part 2A report.

---

## Related diagrams

- **Previous:** [part_2a_exam_evaluation](part_2a_exam_evaluation.md)
- **Next:** [part_3_acceptance_to_student](part_3_acceptance_to_student.md)

## DMN pairing (recommended)

Optional decision table: **Admission Decision** — inputs: scores, program, strand; outputs: A5.0 / A5.1 / A5.2 / A5.3 / A5.5.
