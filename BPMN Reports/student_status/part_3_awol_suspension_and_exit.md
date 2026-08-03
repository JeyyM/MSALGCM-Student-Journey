# BPMN Report — Part 3: AWOL, Suspension & Exit

**Matching files:** [`part_3_awol_suspension_and_exit.bpmn`](../BPMN%20Code/student_status/part_3_awol_suspension_and_exit.bpmn) · [`part_3_awol_suspension_and_exit.mmd`](../final%20mermaid%20code/student_status/part_3_awol_suspension_and_exit.mmd)

---

## Purpose

Models **disruption and exit** at university level: AWOL, disciplinary suspension, voluntary exit, and permanent disqualification.

**Status codes covered:** `S1.0`, `S2.0`, `S3.1`, `S3.2`, `S4.1`, `S4.2`

---

## Process summary

| Transition | Trigger | Lane |
|------------|---------|------|
| `S2.0` → `S3.1` | No enroll, no LOA | Registrar (AWOL detection) |
| `S3.1` → `S1.0` | Returnee approved | Registrar |
| `S2.0` → `S3.2` | Disciplinary suspension | Disciplinary |
| `S3.2` → `S2.0` | Suspension served | Disciplinary |
| → `S4.1` | University exit (good standing) | Student / Registrar |
| → `S4.2` | Disqualification | Disciplinary |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Disciplinary paths | **Disciplinary Office** lane | Third party beyond enrollment |
| AWOL | Registrar service tasks | System-driven status |
| Exit good standing | End event in Student lane | Student-initiated exit |
| Disqualification | End event in Disciplinary lane | Terminal disciplinary outcome |

---

## Swimlanes

| Lane | Responsibility |
|------|----------------|
| **Enrollment & Records** | AWOL, returnee, active standing |
| **Student** | Voluntary exit (S4.1) |
| **Disciplinary Office** | Suspension, disqualification |

---

## BPMN strengths here

- **Three lanes** reflect real organizational boundaries — strong checkpoint example for “BPMN captures responsibility.”
- Links to **COMBO-T003** (exit forces P3.1) in [cross_impact_rules](../combined_lifecycle/cross_impact_rules.md).

## Limitations

- Exit while program active triggers program update — shown in combined diagrams, not isolated here.
- Returnee from AWOL marked tentative in workbook — noted in narrative, not as BPMN annotation.
- Appeal / reinstatement subprocesses not expanded.

---

## Related diagrams

- **Previous:** [part_2_residency_and_loa](part_2_residency_and_loa.md)
- **Cross-impact:** [cross_impact_rules](../combined_lifecycle/cross_impact_rules.md)
- **Next:** [part_4_graduation_and_terminal_states](part_4_graduation_and_terminal_states.md)
