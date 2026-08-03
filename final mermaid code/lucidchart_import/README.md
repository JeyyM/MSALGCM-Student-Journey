# Lucidchart import — Student Journey diagrams

Lucidchart accepts diagram **code** in two practical ways for this project:

| Method | Format | Best for |
|--------|--------|----------|
| **Paste on canvas** | Mermaid (`.mmd` files here) | Fast, editable shapes; good for flow overview and parallel lanes |
| **File import** | BPMN 2.0 XML (`.bpmn` file here) | Assignment BPMN deliverable in Lucid’s BPMN shape library |
| **Manual table** | CSV (`dmn_combination_sample.csv`) | DMN-style decision table — Lucid has **no DMN import**; draw a table or use [BPMN.io](https://demo.bpmn.io/dmn) for real DMN |

## Paste Mermaid into Lucidchart

1. Open a Lucidchart document.
2. Open one of the `.mmd` files below and **copy the entire contents** (no markdown fences).
3. **Paste directly onto the canvas** (not into a text box).
4. Lucid converts the syntax into native, editable shapes.
5. Rearrange, color lanes, and add BPMN task/event icons from the shape library if your course requires strict BPMN notation.

**Tip:** Start with `01_high_level_overview.mmd`, then add detail diagrams on separate pages.

## Import BPMN XML

1. In Lucidchart: **+ New → Import**.
2. Upload `admission_process.bpmn`.
3. Only standard BPMN 2.0 content is preserved; restyle pools/tasks as needed.

## DMN (combination validation)

For the Aug 5 assignment you need **BPMN + DMN**. Lucid can show a decision **table as a grid**, but not DMN XML.

- Use `dmn_combination_sample.csv` to build a table shape in Lucid, **or**
- Model the full matrix in BPMN.io / Camunda Modeler and export screenshots + `.dmn` for submission.

## Files

| File | Content |
|------|---------|
| `01_high_level_overview.mmd` | End-to-end lifecycle (Applicant → Student → Outcome) |
| `02_applicant_account_to_submission.mmd` | A0 → A2.x submission funnel |
| `03_applicant_evaluation_and_results.mmd` | A2.0 → A5.x with decision gateways |
| `04_applicant_acceptance_to_student.mmd` | A5.x → A7.x → S1.0 bridge |
| `05_parallel_student_program.mmd` | Parallel S/P FSM + validation layer |
| `admission_process.bpmn` | Simplified BPMN 2.0 for Lucid import |
| `dmn_combination_sample.csv` | Sample V(S,P) rules for a Lucid table |

Source diagrams: `../` (canonical Mermaid in `final mermaid code/`).
