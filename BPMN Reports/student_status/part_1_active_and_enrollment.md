# BPMN Report — Part 1: Active & Enrollment

**Matching files:** [`part_1_active_and_enrollment.bpmn`](../BPMN%20Code/student_status/part_1_active_and_enrollment.bpmn) · [`part_1_active_and_enrollment.mmd`](../final%20mermaid%20code/student_status/part_1_active_and_enrollment.mmd)

---

## Purpose

Models the **first student-status transition** after admission: from without enrollment to active enrolled student.

**Status codes covered:** `S1.0` → `S2.0`

---

## Process summary

| Step | Status | Lane |
|------|--------|------|
| Admitted (from A7.x) | Start | Registrar |
| Without enrollment | `S1.0` | Registrar |
| Enroll / enlist | → `S2.0` Active | Registrar |
| Continue to Parts 2–4 | End | Registrar |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Hand-off from A7.x | Start event in Registrar lane | Admission complete; student record exists |
| Enrollment action | Labeled sequence flow | Student action triggers registrar update |
| Single linear path | No gateway | Simplest student diagram — good BPMN baseline |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **Enrollment & Records** | All shapes — system-of-record updates for S codes |

*(Student lane appears in Part 2 when student-initiated actions matter.)*

---

## BPMN strengths here

- Minimal diagram shows BPMN can represent **simple state promotion** cleanly.
- Clear entry from admission bridge ([part_3](../applicant_status/part_3_acceptance_to_student.md)).

## Limitations

- **Student as actor** for enrollment is implied, not a separate lane — could add Student userTask “Enroll in classes” → serviceTask S2.0 in a refined version.
- **Parallel P1.x** program standing starts in [applicant_to_student_bridge](../combined_lifecycle/applicant_to_student_bridge.md).

---

## Related diagrams

- **Previous:** [part_3_acceptance_to_student](../applicant_status/part_3_acceptance_to_student.md)
- **Next:** [part_2_residency_and_loa](part_2_residency_and_loa.md)
