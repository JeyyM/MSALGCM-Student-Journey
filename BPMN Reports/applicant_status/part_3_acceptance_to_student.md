# BPMN Report — Part 3: Acceptance to Student

**Matching files:** [`part_3_acceptance_to_student.bpmn`](../BPMN%20Code/applicant_status/part_3_acceptance_to_student.bpmn) · [`part_3_acceptance_to_student.mmd`](../final%20mermaid%20code/applicant_status/part_3_acceptance_to_student.mmd)

---

## Purpose

Models **offer acceptance through official admission** and the **bridge into student records** — the critical hand-off from `A*` codes to `S*` codes.

**Status codes covered:** `A6.0`, `A7.0`, `A7.1`, `S1.0`

---

## Process summary

| Step | Status | Lane |
|------|--------|------|
| Pay / waive acceptance fee | → `A6.0` Reserved | Applicant → Admissions |
| Final requirements check | Gateway | Admissions |
| Officially admitted | `A7.0` | Admissions |
| Provisionally admitted | `A7.1` | Admissions |
| Provisional → official | `A7.1` → `A7.0` | Admissions |
| Student record created | `S1.0` Without Enrollment | Registrar |
| Continue student lifecycle | (end) | Registrar |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| A5.x offers (Part 2B) | Start event “Admission offer” | Cross-diagram entry |
| Fee payment | User-initiated → service task A6.0 | Applicant acts; system updates |
| Requirements gateway | XOR in Admissions lane | Complete vs pending |
| A7 → S1.0 | Cross-lane sequence flow | **Process hand-off** between pools of responsibility |
| Three swimlanes | Applicant · Admissions · Registrar | First diagram with Registrar lane |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **Applicant** | Acceptance fee, trigger start |
| **Admissions Office** | Reserve seat, verify requirements, admit |
| **University Records (Registrar)** | Create student status `S1.0` |

---

## BPMN strengths here

- Demonstrates **multi-department hand-off** — core BPMN value for the Student Journey Matrix.
- **Three lanes** without overcrowding; suitable for Lucid/BPMN.io presentation.
- Clear narrative: admission *ends* at student record *begins*.

## Limitations

- **Simultaneous P1.0/P1.1 assignment** shown in [applicant_to_student_bridge](../combined_lifecycle/applicant_to_student_bridge.md), not here — keeps applicant BPMN section focused.
- Payment timers (lapse → A6.1) in [part_4_terminal_or_exception_states](part_4_terminal_or_exception_states.md).
- Cross-pool messaging (BPMN message flows) not used — sequence flow across lanes within one pool is sufficient at this granularity.

---

## Related diagrams

- **Previous:** [part_2b_admission_results](part_2b_admission_results.md)
- **Bridge detail:** [applicant_to_student_bridge](../combined_lifecycle/applicant_to_student_bridge.md)
- **Next (student):** [part_1_active_and_enrollment](../student_status/part_1_active_and_enrollment.md)
