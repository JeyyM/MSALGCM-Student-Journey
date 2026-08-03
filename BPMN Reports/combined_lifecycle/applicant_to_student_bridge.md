# BPMN Report — Applicant to Student Bridge

**Matching files:** [`applicant_to_student_bridge.bpmn`](../BPMN%20Code/combined_lifecycle/applicant_to_student_bridge.bpmn) · [`applicant_to_student_bridge.mmd`](../final%20mermaid%20code/combined_lifecycle/applicant_to_student_bridge.mmd)

---

## Purpose

Models the **critical hand-off** when admission completes and **both** university student status and initial program standing are assigned — the join point between `A*`, `S*`, and `P*` tracks.

**Status codes covered:** `A7.0`, `A7.1`, `S1.0`, `S2.0`, `P1.0`, `P1.1`

---

## Process summary

| Step | Codes | Lane |
|------|-------|------|
| Official / provisional admit | A7.0 / A7.1 | Admissions |
| Create student without enrollment | S1.0 | Student (University Standing) |
| Enroll | S2.0 | Student lane |
| Normal program standing | P1.0 | Program Office |
| Probationary program standing | P1.1 | Program Office (from A5.1 path) |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Mermaid dotted S→P | Sequence flows from S1.0 to P1.0/P1.1 | Cross-lane initialization |
| Three dimensions in one pool | Admissions + Student + Program lanes | **Multi-track** without separate pools |
| No gateway on P1.0 vs P1.1 | Two outgoing flows from S1.0 | Admission type determines path (could add XOR + DMN) |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **Admissions Office** | Final admit statuses |
| **Student (University Standing)** | S1.0, S2.0 |
| **Program Office (Academic Standing)** | Initial P1.0 or P1.1 |

---

## BPMN strengths here

- Best diagram for explaining **“one person, two parallel standings.”**
- Shows admissions **ends** where student + program **begin**.
- Ideal for linking BPMN process to future DMN (probationary vs normal initial P).

## Limitations

- **Mutually exclusive** P1.0 vs P1.1 should use XOR gateway in strict BPMN — two flows from S1.0 imply both possible without formal condition.
- Enrollment (S2.0) and program init could happen in either order in reality — sequence simplified.
- Validator app encodes this as separate state updates — BPMN is narrative not executable here.

---

## Related diagrams

- **Admission detail:** [part_3_acceptance_to_student](../applicant_status/part_3_acceptance_to_student.md)
- **Student enrollment:** [part_1_active_and_enrollment](../student_status/part_1_active_and_enrollment.md)
- **Program start:** [part_1_good_standing_and_probation](../student_program_status/part_1_good_standing_and_probation.md)
