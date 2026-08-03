# BPMN Report — Part 3: Graduation & Terminal States

**Matching files:** [`part_3_graduation_and_terminal_states.bpmn`](../BPMN%20Code/student_program_status/part_3_graduation_and_terminal_states.bpmn) · [`part_3_graduation_and_terminal_states.mmd`](../final%20mermaid%20code/student_program_status/part_3_graduation_and_terminal_states.mmd)

---

## Purpose

Models **program completion paths**: graduation candidacy, graduated, and incomplete (exit while program unfinished).

**Status codes covered:** `P1.0`, `P2.0`, `P3.0`, `P3.1`

---

## Process summary

| Transition | Meaning |
|------------|---------|
| `P1.0` → `P2.0` | First graduation check passed |
| `P2.0` → `P3.0` | Commencement + 1 week — **graduated** |
| `P1.0` / `P2.0` → `P3.1` | University exit — **incomplete** |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Happy path chain | Linear service tasks | Eligible → candidacy → graduated |
| Exit from two states | Two flows to P3.1 end | Exit can occur before or after candidacy |
| P3.0 terminal | End event | Program complete |
| Student lane for exit | User-initiated incomplete | Links to student exit in S track |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **College / Program Office** | Graduation checks, P2.0, P3.0 |
| **Student** | University exit triggering P3.1 |

---

## BPMN strengths here

- Clear **happy path vs exit path** split for program lifecycle end.
- P3.0 graduation connects to **COMBO-T001** (force S4.0) in combined reports.

## Limitations

- **Commencement timing rule** (“+ 1 week”) on sequence flow label only — not a timer event.
- Multi-program students (several P tracks) not expanded — one program per diagram instance.
- Graduation clearance checklist → subprocess or DMN in fuller model.

---

## Related diagrams

- **Previous:** [part_2_snas_sap_and_ineligible](part_2_snas_sap_and_ineligible.md)
- **Student graduation:** [part_4_graduation_and_terminal_states](../student_status/part_4_graduation_and_terminal_states.md)
- **COMBO-T001:** [cross_impact_rules](../combined_lifecycle/cross_impact_rules.md)
