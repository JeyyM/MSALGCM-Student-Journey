# BPMN Report — High-Level Lifecycle Overview

**Matching files:** [`high_level_lifecycle_overview.bpmn`](../BPMN%20Code/combined_lifecycle/high_level_lifecycle_overview.bpmn) · [`high_level_lifecycle_overview.mmd`](../final%20mermaid%20code/combined_lifecycle/high_level_lifecycle_overview.mmd)

---

## Purpose

**Executive-level BPMN** spanning the full journey: applicant → accepted → active student ↔ program standing → disruption → outcome. Used for checkpoint “big picture” before drilling into granular parts.

---

## Process summary

| Phase | BPMN task (summary) | Lane |
|-------|---------------------|------|
| Applicant | A0–A5.x funnel | Applicant |
| Accepted | A6.0–A7.x | Admissions |
| Active student | S1.0–S2.x | Student Life & Enrollment |
| Program standing | P1.0–P2.0 (parallel) | Program / Academic Affairs |
| Disruption | LOA / AWOL / suspended | Student Life & Enrollment |
| Outcome | Graduate / exit / terminal | University Outcome |

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Mermaid dotted S↔P link | Sequence flow Active → Program | Shows parallel concern; not true BPMN parallel gateway |
| Re-entry Disrupt → Active | Returnee loop | Life-cycle recovery |
| Five swimlanes | One pool, horizontal lanes | Maximum overview without 17-diagram detail |
| Abstract task names | Aggregated status ranges | Readability over code-level precision |

---

## Swimlanes

| Lane | Scope |
|------|-------|
| Applicant / Prospective Student | Pre-admission |
| Admissions Office | Offer through admit |
| Student Life & Enrollment | S codes, disruption |
| Program / Academic Affairs | P codes |
| University Outcome | Terminal states |

---

## BPMN strengths here

- **Single-slide narrative** for milestone presentation.
- Swimlanes show **four organizational concerns** plus outcome.
- Entry point for explaining why granular diagrams exist (Parts 1–4).

## Limitations

- **No status codes** at step level — must link to section BPMN files.
- Parallel S/P not formally concurrent in BPMN token semantics.
- Combination validation omitted — see [parallel_student_program_constrained_fsm](parallel_student_program_constrained_fsm.md) and DMN.

---

## Related diagrams

- **All section parts** under `applicant_status/`, `student_status/`, `student_program_status/`
- **Detail bridge:** [applicant_to_student_bridge](applicant_to_student_bridge.md)
