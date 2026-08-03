# BPMN Report — Part 1: Account to Submission

**Matching files:** [`part_1_account_to_submission.bpmn`](../BPMN%20Code/applicant_status/part_1_account_to_submission.bpmn) · [`part_1_account_to_submission.mmd`](../final%20mermaid%20code/applicant_status/part_1_account_to_submission.mmd)

---

## Purpose

Models the **first segment of the admission funnel**: from applicant account creation through form submission and requirements checking, ending when the file is complete enough to enter evaluation (Part 2A).

**Status codes covered:** `A0` → `A1.0` → `A2.0` / `A2.1`

---

## Process summary

| Step | Status | Who acts |
|------|--------|----------|
| Account created | (start) | Applicant |
| Draft application | `A0` | Applicant |
| Submit form | `A1.0` | Applicant |
| Requirements check | Gateway | OAS / Admissions |
| Complete requirements | `A2.0` | OAS (records completeness) |
| Deficiencies | `A2.1` | OAS (flags missing items) |
| Resubmit loop | `A2.1` → `A2.0` | Applicant fixes → OAS re-checks |
| OAS resubmit request | `A2.0` → `A2.1` | OAS sends back complete file |
| Proceed to evaluation | (end) | OAS |

---

## BPMN modeling choices

| Source (Mermaid) | BPMN element | Notes |
|------------------|--------------|-------|
| `[*] --> A0` | Start event → User task | Applicant-initiated journey |
| State boxes | User / service tasks | Applicant tasks = **userTask**; OAS status updates = **serviceTask** |
| Requirements branch | Exclusive gateway (XOR) | Complete vs deficiencies |
| Resubmit loop | Backward sequence flow | BPMN allows loops; not a separate “exception subprocess” to keep diagram small |
| `[*]` exit to Part 2 | End event | Boundary between diagram parts |

---

## Swimlanes

| Lane | Shapes | Responsibility |
|------|--------|----------------|
| **Applicant** | Start, A0, A1.0 | Account, draft, submit, fix deficiencies |
| **OAS / Admissions Office** | Gateway, A2.0, A2.1, End | Review requirements, assign status, release to evaluation |

---

## BPMN strengths here

- Clear **hand-off** from Applicant lane to OAS lane at submission (`A1.0` → gateway).
- **Resubmit loop** (`A2.0` ↔ `A2.1`) is visible as a business exception path with labeled flows (“OAS requires resubmit”, “Requirements completed”).
- Granular single-purpose diagram stays readable at checkpoint scale.

## Limitations

- **State vs activity:** In the workbook, `A2.0` is a *status the applicant holds*; in BPMN it appears as a task “Complete Requirements.” This is intentional simplification — the report should state that statuses are modeled as milestones.
- **Time rules** (e.g. submission within 3 terms) are not encoded — would need timer events or DMN.
- **No DMN** for “what counts as complete requirements” — rules stay in documentation.

---

## Related diagrams

- **Previous:** (entry point)
- **Next:** [part_2a_exam_evaluation](part_2a_exam_evaluation.md) — begins from `A2.0` complete
