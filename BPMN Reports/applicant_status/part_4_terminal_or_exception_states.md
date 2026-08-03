# BPMN Report — Part 4: Terminal & Exception States

**Matching files:** [`part_4_terminal_or_exception_states.bpmn`](../BPMN%20Code/applicant_status/part_4_terminal_or_exception_states.bpmn) · [`part_4_terminal_or_exception_states.mmd`](../final%20mermaid%20code/applicant_status/part_4_terminal_or_exception_states.mmd)

---

## Purpose

Consolidates **non-happy-path and terminal admission outcomes** that can occur from reserved, admitted, or evaluation stages — cancellations, deferrals, and qualification dead ends.

**Status codes covered:** `A3.2`, `A4.2`, `A5.5`, `A6.1`, `A7.2`, `A8.0`, `A8.1` (plus context from `A6.0`, `A7.0`, `A7.1`)

---

## Process summary

| From | Trigger | To (terminal / exception) |
|------|---------|---------------------------|
| `A6.0` Reserved | Non-payment | `A6.1` Cancelled |
| `A6.0` Reserved | Did not enroll | `A7.2` Deferred |
| `A7.1` Provisional | 1 year, no reqs | `A8.0` Cancelled |
| `A7.0` / `A7.1` | Withdrawal | `A8.1` Cancelled |
| (evaluation) | Failed / no exam / not qualified | `A3.2`, `A4.2`, `A5.5` |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Multiple disconnected terminals in Mermaid | One diagram, multiple end events | Exception catalog pattern |
| Evaluation terminals | **OAS / Evaluation** lane | Separates eval dead ends from admissions ops |
| Applicant-initiated | Deferral, withdrawal in Applicant lane | User responsibility visible |
| No single start | Entry from mid-process states | Snapshot model, not full replay from A0 |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **Applicant** | Defer, withdraw |
| **Admissions Office** | Reserved/admitted cancellations |
| **OAS / Evaluation** | Qualification dead ends (A3.2, A4.2, A5.5) |

---

## BPMN strengths here

- **End events** give a clear visual language for “journey stops here.”
- Three lanes separate *who caused* the terminal outcome (applicant vs office vs evaluation).
- Complements happy-path parts 1–3 without cluttering them.

## Limitations

- Not a connected process from start to finish — **intentionally** an exception map.
- Timer-based rules (fee deadline, 1-year provisional) need **timer boundary events** in a fuller BPMN — omitted for checkpoint scope.
- Could be modeled as **event subprocesses** attached to Part 3 tasks in a mega-diagram — rejected for readability.

---

## Related diagrams

- **Happy path:** [part_1](part_1_account_to_submission.md) – [part_3](part_3_acceptance_to_student.md)
- **Overview:** [high_level_lifecycle_overview](../combined_lifecycle/high_level_lifecycle_overview.md)
