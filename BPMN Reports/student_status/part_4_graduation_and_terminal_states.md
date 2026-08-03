# BPMN Report — Part 4: Graduation & Terminal States

**Matching files:** [`part_4_graduation_and_terminal_states.bpmn`](../BPMN%20Code/student_status/part_4_graduation_and_terminal_states.bpmn) · [`part_4_graduation_and_terminal_states.mmd`](../final%20mermaid%20code/student_status/part_4_graduation_and_terminal_states.mmd)

---

## Purpose

Models **terminal student outcomes** from an active student: graduation, voluntary exit, and disqualification.

**Status codes covered:** `S2.0` → `S4.0`, `S4.1`, `S4.2`

---

## Process summary

| From `S2.0` Active | To | Meaning |
|--------------------|-----|---------|
| All programs graduated | `S4.0` Graduated | University completion |
| University exit | `S4.1` Exited (good standing) | Voluntary departure |
| Disqualification verdict | `S4.2` Disqualified | Permanent removal |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Three terminals from S2.0 | Three end events | XOR implicit (one outcome per student) |
| S4.0 trigger | “All programs graduated” label | Cross-reference to **COMBO-T001** |
| Overlap with Part 3 S4.1/S4.2 | Part 3 from AWOL/suspension too | This slice emphasizes active-student entry |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **Enrollment & Records** | S2.0, S4.0 graduation update |
| **Student** | S4.1 exit |
| **Disciplinary Office** | S4.2 disqualification |

---

## BPMN strengths here

- Compact **outcome fan-out** from one active state — easy to present.
- Graduation path ties narrative to program completion (combined lifecycle).

## Limitations

- **S4.0** usually forced by all P3.0 — process logic split between BPMN (here) and DMN/COMBO rules.
- S4.0 marked “Terminal?” in workbook — documented as end event; confirm with stakeholders.

---

## Related diagrams

- **Cross-impact:** [cross_impact_rules](../combined_lifecycle/cross_impact_rules.md) (COMBO-T001)
- **Program side:** [part_3_graduation_and_terminal_states](../student_program_status/part_3_graduation_and_terminal_states.md)
