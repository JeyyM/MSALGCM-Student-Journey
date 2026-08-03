# BPMN Report — Part 2A: Exam & Evaluation

**Matching files:** [`part_2a_exam_evaluation.bpmn`](../BPMN%20Code/applicant_status/part_2a_exam_evaluation.bpmn) · [`part_2a_exam_evaluation.mmd`](../final%20mermaid%20code/applicant_status/part_2a_exam_evaluation.mmd)

---

## Purpose

Models **OAS initial evaluation** after requirements are complete, including exam routing, exam outcomes, and further screening — ending at states that feed **Part 2B (admission results)**.

**Status codes covered:** `A3.0`, `A3.1`, `A3.2`, `A4.0`, `A4.1`, `A4.2`, `A4.3`

---

## Process summary

| Branch | Path | Owner |
|--------|------|-------|
| Exam required | `A3.0` → exam gateway → `A4.0` / `A4.1` / `A4.2` | OAS assigns; Applicant takes exam |
| Exam exempted | `A3.1` → end | OAS |
| Failed initial eval | `A3.2` (terminal) | OAS |
| Further screening only | `A4.3` → end | OAS |
| Further after exam | `A4.0` → `A4.3` | OAS |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Multiple exits from `A2.0` | XOR gateway “Initial evaluation” | Mutually exclusive OAS decisions |
| Exam sub-path | Second XOR “Exam outcome” | Taken / pending / lapsed |
| Terminal `A3.2`, `A4.2` | End events | Dead ends in admission |
| `A3.1`, `A4.3` → Part 2B | End event “To admission results” | Diagram boundary |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **OAS / Admissions Office** | Evaluation decisions, exempt/reject/further screening |
| **Applicant** | Take exam (`A4.0`), wait (`A4.1`), miss window (`A4.2`) |

---

## BPMN strengths here

- **Two decision gateways** mirror the workbook’s evaluation then exam phases without merging unrelated branches.
- **Terminal end events** make dead-end statuses visually distinct from forward paths.
- Cross-lane flows (OAS assigns exam → Applicant takes it) show real process collaboration.

## Limitations

- **Exam scheduling / slots** (business rules) not modeled — would need DMN or subprocess.
- **A4.1 → A4.0** loop (pending then taken) is correct but layout may overlap in auto-import tools.
- **A5.x results** deliberately in Part 2B to keep this diagram granular.

---

## Related diagrams

- **Previous:** [part_1_account_to_submission](part_1_account_to_submission.md)
- **Next:** [part_2b_admission_results](part_2b_admission_results.md)
