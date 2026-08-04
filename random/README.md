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

## BPMN Modeler in Cursor / VS Code

If the file opens in [demo.bpmn.io](https://demo.bpmn.io) but Cursor shows:

`No editor found for id: file:///...part_1_account_to_submission.bpmn`

that is **not a bad BPMN file** — Cursor lost the link to the BPMN extension for that tab.

**Fix (in order):**

1. **Close** the broken tab (do not click “Try again” in a loop).
2. `Ctrl+Shift+P` → **Developer: Reload Window**
3. In Explorer, **right-click** the `.bpmn` file → **Open With…** → **BPMN Modeler** (Miragon) or **BPMN.io Editor**
4. If those are missing, install an extension (see `.vscode/extensions.json`):
   - [BPMN Modeler](https://marketplace.visualstudio.com/items?itemName=miragon-gmbh.vs-code-bpmn-modeler) (Miragon)
   - [BPMN.io Editor](https://marketplace.visualstudio.com/items?itemName=bpmn-io.vs-code-bpmn-io) (lighter alternative)
5. Check **Output → bpmn.modeler** for extension errors after reopening.

**Important:** If the Modeler tab failed once, saving from that tab can write a stripped ~8 KB file (no colors). After reload, if the file looks too small (~150 lines instead of ~210), regenerate:

```bash
python "BPMN Code/generate_bpmn.py" --only "1. applicant_status/part_1_account_to_submission.bpmn" --force
```

Then reload the window again before opening.

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

## Protecting manual edits in BPMN Modeler

**Problem:** The `.bpmn` files in `1.`–`4.` folders are **your source of truth** (hand-edited in BPMN Modeler). `generate_bpmn.py` can overwrite every diagram it knows about — and the **Cursor agent has been running it** after layout changes, which reverted manual work even when you never ran the script yourself.

**All 17 canonical diagrams are now listed in [`protected_bpmn.txt`](protected_bpmn.txt)** so agent or script runs skip them by default. A project rule in `.cursor/rules/bpmn-manual-edits.mdc` tells the agent not to regenerate unless you ask.

**Three ways to stay safe:**

### 1. Protection list (recommended)

After you finish hand-tuning a diagram, add its path to [`protected_bpmn.txt`](protected_bpmn.txt):

```text
1. applicant_status/part_1_account_to_submission.bpmn
2. student_status/part_2_residency_and_loa.bpmn
```

Then run the generator normally — listed files are **skipped**:

```bash
python "BPMN Code/generate_bpmn.py"
```

To regenerate a protected file anyway: remove it from the list, or use `--force`.

### 2. Regenerate only one diagram

When changing layout in `generate_bpmn.py` for a **single** file, use `--only` so other diagrams are untouched:

```bash
python "BPMN Code/generate_bpmn.py" --only "3. student_program_status/part_2_snas_sap_and_ineligible.bpmn"
```

### 3. Keep a manual copy folder

Copy polished files to e.g. `BPMN Code/manual_published/` and treat that folder as read-only for the generator. The generator never writes there unless you add those paths to `DIAGRAMS`.

**Also:** commit to git or use Cursor **Local History** (Timeline) before bulk regenerates.

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

See **Protecting manual edits** above before running. Options:

| Command | Effect |
|---------|--------|
| `python generate_bpmn.py` | Regenerate all **non-protected** diagrams |
| `python generate_bpmn.py --only "path/to/file.bpmn"` | Regenerate **one** diagram only |
| `python generate_bpmn.py --force` | Ignore `protected_bpmn.txt` |

## DMN decision tables (18 files)

Companion **DMN 1.3** decision tables live beside their BPMN diagrams. Each transition table has a **Rationale** column explaining business context, corrections, and COMBO references.

| Folder | DMN file(s) | Purpose |
|--------|-------------|---------|
| `1. applicant_status/` | 5 × `DMN applicant_status part_*.dmn` | Applicant state transitions |
| `2. student_status/` | 4 × `DMN student_status part_*.dmn` | Student standing transitions |
| `3. student_program_status/` | 3 × `DMN student_program_status part_*.dmn` | Program standing transitions |
| `4. combined_lifecycle/` | `1__` … `6__` DMN files | Overview, bridge, parallel FSM (S+P axes), COMBO rules, **80-cell combination matrix** |

Regenerate after BPMN or matrix changes:

```bash
python "BPMN Code/_generate_dmn.py"
```

Source of truth for combination validation: `documentation/workbook_patches/combination_matrix_post_m3.csv`.

**Note:** DMN files are **not wired** to BPMN via `businessRuleTask` / `decisionRef` yet — they are tabular reference/decision specs aligned with the diagrams. Wire them in Camunda when moving to execution.
