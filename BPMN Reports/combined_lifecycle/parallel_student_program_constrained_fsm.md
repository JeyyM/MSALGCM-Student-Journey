# BPMN Report — Parallel Student × Program FSM

**Matching files:** [`parallel_student_program_constrained_fsm.bpmn`](../BPMN%20Code/combined_lifecycle/parallel_student_program_constrained_fsm.bpmn) · [`parallel_student_program_constrained_fsm.mmd`](../final%20mermaid%20code/combined_lifecycle/parallel_student_program_constrained_fsm.mmd)

---

## Purpose

**Integrated BPMN** for post-admission lifecycle: Student FSM and Program FSM as **parallel swimlanes**, plus a **validation layer** stub and COMBO cross-impact flows. Closest BPMN representation of the “constrained product automaton” concept from the Mermaid source.

---

## Architecture (three layers)

| Layer | BPMN representation |
|-------|---------------------|
| **Student FSM** | Student lane: S1.0 → S2.0 → LOA/AWOL/exit/graduate |
| **Program FSM** | Program lane: P1.x → P2.0 → P3.x |
| **Validation** | Validation lane: V(S,P) service task |
| **Cross-impact** | Inter-lane flows (COMBO-T001, T003, T004, T005) |

---

## Key transitions

**Student lane:** enroll, LOA, AWOL, returnee, exit, graduated (S4.0)  
**Program lane:** SNAS, probation recovery, retention breach, graduation candidacy, commencement  
**Cross-lane:** initial S1.0→P pairing, COMBO rules, S2.0/P1.0→VALID feeds  

---

## BPMN modeling choices

| Source | BPMN | Notes |
|--------|------|-------|
| Mermaid subgraphs | Swimlanes | TB layout in Mermaid → horizontal lanes in BPMN |
| Dotted COMBO edges | Cross-lane sequence flows | Labeled with COMBO-T00x |
| Matrix summary in Mermaid | Single VALID task | **DMN holds detail** — BPMN points to it |
| Parallel independence | No parallel gateway | Two lanes run conceptually in parallel; not BPMN AND-split |

---

## Swimlanes

| Lane | Content |
|------|---------|
| **Admissions Office** | Start from A7.x admit |
| **Student (University Standing)** | S* transitions |
| **Program Office (Academic Standing)** | P* transitions |
| **Records / Validation System** | V(S,P) check |

---

## BPMN strengths here

- **Richest single diagram** for explaining Student Journey Matrix structure post-admission.
- Shows where **BPMN ends** and **DMN begins** (validation task).
- COMBO rules visible in context of full FSMs.

## Limitations (key write-up material)

| Issue | Explanation |
|-------|-------------|
| **True parallelism** | BPMN parallel gateway splits one token; here two dimensions are **persistent state**, not a one-shot fork. Swimlanes are the workaround. |
| **91-cell matrix** | Cannot draw as BPMN edges — use **DMN decision table**. |
| **State = task** | Same simplification as all section diagrams. |
| **Layout complexity** | Largest BPMN file — may need manual tidy after Lucid import. |
| **Executable process** | Model is **descriptive** (`isExecutable="false"`), not deployment-ready. |

---

## Related diagrams

- **Section detail:** all `student_status/` and `student_program_status/` reports
- **COMBO only:** [cross_impact_rules](cross_impact_rules.md)
- **Validator app:** `src/data/combinations.js` (runtime V(S,P))
- **DMN:** recommended companion artifact for checkpoint

---

## Recommended narrative for checkpoint

> “We model the Student Journey as **parallel BPMN lanes** for university standing and program standing, with **DMN** validating whether a given (S,P) pair is allowed. **Four COMBO rules** are modeled as cross-lane process steps; everything else is either independent or validated by the decision table.”
