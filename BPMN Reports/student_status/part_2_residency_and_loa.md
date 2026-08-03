# BPMN Report — Part 2: Residency & LOA

**Matching files:** [`part_2_residency_and_loa.bpmn`](../BPMN%20Code/student_status/part_2_residency_and_loa.bpmn) · [`part_2_residency_and_loa.mmd`](../final%20mermaid%20code/student_status/part_2_residency_and_loa.mmd)

---

## Purpose

Models **active-student variants**: residency registration, leave of absence (LOA), prolonged leave, and returnee paths back to without-enrollment or active.

**Status codes covered:** `S1.0`, `S2.0`, `S2.1`, `S2.2`, `S2.3`

---

## Process summary

| Transition | Trigger | Lane |
|------------|---------|------|
| `S1.0` → `S2.0` | Enrolled / enlisted | Registrar |
| `S2.0` → `S2.1` | Registered for residency | Student |
| `S2.1` → `S2.0` | Re-enrolled | Student |
| `S2.0` → `S2.2` | LOA approved | Registrar |
| `S2.0` → `S2.3` | LOA period exceeded | Registrar |
| `S2.2` / `S2.3` → `S1.0` | Returnee approved | Registrar |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Multiple branches from S2.0 | Parallel sequence flows (no AND gateway) | Workbook allows mutually exclusive outcomes — XOR could be added |
| Returnee paths | Cross-lane back to S1.0 | Returnee processing before re-enrollment |
| Residency | Student lane userTask | Student-initiated registration |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **Student** | Residency registration, re-enrollment |
| **Enrollment & Records** | LOA approval, prolonged leave, returnee processing, S1.0/S2.0 updates |

---

## BPMN strengths here

- Shows **two-party** student administration (student requests, office approves).
- LOA exception paths visible without merging into AWOL diagram (Part 3).

## Limitations

- **S2.0 → S2.1 vs S2.2 vs S2.3** could use XOR gateway for strict BPMN semantics — omitted to match Mermaid directly.
- **Combination rules** (e.g. LOA + Ineligible program) → DMN, not here.
- Max LOA duration rules → DMN or timer events.

---

## Related diagrams

- **Previous:** [part_1_active_and_enrollment](part_1_active_and_enrollment.md)
- **Next:** [part_3_awol_suspension_and_exit](part_3_awol_suspension_and_exit.md)
