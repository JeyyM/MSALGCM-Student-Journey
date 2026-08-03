# BPMN Code — Student Journey (converted from Mermaid)

Granular BPMN 2.0 XML files matching every diagram in `final mermaid code/`. Each file is kept small so it stays readable at a glance in Lucidchart, BPMN.io, or Camunda Modeler.

**Analysis & reporting:** see [`BPMN Reports/`](../BPMN%20Reports/) — same folder structure, `.md` files explaining modeling choices per diagram.

## How to import into Lucidchart

1. **+ New → Import**
2. Upload any `.bpmn` file from this folder
3. Rearrange if auto-layout needs tweaking; restyle tasks/events as needed

## How to open in BPMN.io

1. Go to [demo.bpmn.io](https://demo.bpmn.io/)
2. **Open File** → choose a `.bpmn` file

## Folder map (17 diagrams = 17 Mermaid sources)

| Folder | BPMN file | Mermaid source |
|--------|-----------|----------------|
| **applicant_status/** | | |
| | `part_1_account_to_submission.bpmn` | `part_1_account_to_submission.mmd` |
| | `part_2a_exam_evaluation.bpmn` | `part_2a_exam_evaluation.mmd` |
| | `part_2b_admission_results.bpmn` | `part_2b_admission_results.mmd` |
| | `part_3_acceptance_to_student.bpmn` | `part_3_acceptance_to_student.mmd` |
| | `part_4_terminal_or_exception_states.bpmn` | `part_4_terminal_or_exception_states.mmd` |
| **student_status/** | | |
| | `part_1_active_and_enrollment.bpmn` | `part_1_active_and_enrollment.mmd` |
| | `part_2_residency_and_loa.bpmn` | `part_2_residency_and_loa.mmd` |
| | `part_3_awol_suspension_and_exit.bpmn` | `part_3_awol_suspension_and_exit.mmd` |
| | `part_4_graduation_and_terminal_states.bpmn` | `part_4_graduation_and_terminal_states.mmd` |
| **student_program_status/** | | |
| | `part_1_good_standing_and_probation.bpmn` | `part_1_good_standing_and_probation.mmd` |
| | `part_2_snas_sap_and_ineligible.bpmn` | `part_2_snas_sap_and_ineligible.mmd` |
| | `part_3_graduation_and_terminal_states.bpmn` | `part_3_graduation_and_terminal_states.mmd` |
| **combined_lifecycle/** | | |
| | `high_level_lifecycle_overview.bpmn` | `high_level_lifecycle_overview.mmd` |
| | `applicant_to_student_bridge.bpmn` | `applicant_to_student_bridge.mmd` |
| | `student_status_vs_program_status_interaction.bpmn` | `student_status_vs_program_status_interaction.mmd` |
| | `cross_impact_rules.bpmn` | `cross_impact_rules.mmd` |
| | `parallel_student_program_constrained_fsm.bpmn` | `parallel_student_program_constrained_fsm.mmd` |

## Notation used

| Mermaid concept | BPMN element |
|-----------------|--------------|
| Status / state box | **Task** (labeled with code, e.g. `A2.0 — Complete Requirements`) |
| `[*]` start | **Start event** |
| Terminal state | **End event** |
| Decision branch | **Exclusive gateway** (XOR) |
| Transition label | **Sequence flow** name |

## Swimlanes & responsibilities

Every diagram uses a **pool with horizontal swimlanes**. Each shape sits in the lane of the responsible party:

| Lane | Typical responsibility |
|------|------------------------|
| **Applicant** | Account, submission, exam attendance, fee payment, withdrawal |
| **OAS / Admissions Office** | Requirements review, evaluation, offers, admission decisions |
| **University Records (Registrar)** | Student record creation, enrollment status updates |
| **Student** | Enrollment actions, LOA/residency requests, voluntary exit |
| **Enrollment & Records** | LOA processing, AWOL, active standing updates |
| **Disciplinary Office** | Suspension, permanent disqualification |
| **College / Program Office** | Academic standing, SNAS, probation, graduation candidacy |
| **Records / Validation System** | V(S,P) combination checks |

Task types indicate who initiates the step:

- **User task** — human-initiated (Applicant / Student)
- **Service task** — office or system status update

Regenerate after edits: `python "BPMN Code/generate_bpmn.py"`

## Colors

Shapes are colored by **swimlane responsibility** using standard BPMN color extensions:

| Lane | Fill | Meaning |
|------|------|---------|
| Applicant | Blue | Applicant / student-initiated steps |
| OAS / Admissions | Green | Admissions office actions |
| Registrar / Enrollment | Purple | University records & enrollment |
| Student | Amber | Student-initiated (post-admission) |
| Program Office | Cyan | Academic / program standing |
| Disciplinary | Red | Suspension / disqualification |
| Validation | Gray | V(S,P) combination checks |
| Gateways | Yellow | Decision points |
| Start / End events | Green / Red tint | Process start & terminal |

**Where colors appear:**
- **BPMN.io** and **Camunda Modeler** — colors import correctly (re-import a fresh `.bpmn` file).
- **Lucidchart** — often **strips BPMN color metadata** on import; you may need to color lanes manually in Lucid, or open in BPMN.io first and export as PNG/SVG for slides.

## Regenerate

If Mermaid sources change, edit `generate_bpmn.py` and run:

```bash
python "BPMN Code/generate_bpmn.py"
```

## DMN

Decision logic (combination tab V(S,P)) is **not** in this folder — use BPMN.io DMN or see `final mermaid code/lucidchart_import/dmn_combination_sample.csv`.
