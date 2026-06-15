# Combined Lifecycle Diagrams

Simplified cross-dimension diagrams. These intentionally **do not** show every status code — they show broad phases and the relationships between the three dimensions. For full detail, see the per-dimension folders.

## Files

| File | Machine type | Purpose |
|---|---|---|
| [`high_level_lifecycle_overview.md`](high_level_lifecycle_overview.md) | `flowchart TD` | End-to-end phases: applicant → student → graduation/exit |
| [`applicant_to_student_bridge.md`](applicant_to_student_bridge.md) | `stateDiagram-v2` | The hand-off: admission `A7.x` → student `S1.0`/`S2.0` + initial program status |
| [`student_status_vs_program_status_interaction.md`](student_status_vs_program_status_interaction.md) | `flowchart TD` + tables | How Student Status and Program Status relate (parallel dimensions) and allowed/blocked combinations |
| [`parallel_student_program_constrained_fsm.md`](parallel_student_program_constrained_fsm.md) | `flowchart TB` | **Integrated model:** parallel Student + Program FSMs, validation matrix layer, COMBO cross-impacts |

## Why these use overviews / tables

- The **high-level overview** is a process narrative, so a `flowchart TD` reads better than a strict FSM.
- The **bridge** is a genuine state hand-off, so it uses `stateDiagram-v2` but stays minimal.
- The **interaction** file uses tables for the 91-pairing combination matrix (a graph would be unreadable) plus a tiny flowchart for the three forced cross-impacts.

## Important caveat

The combination data uses a **legacy code scheme** (`S3.x` exits, `P1.3 = Ineligible`) that differs from the canonical per-dimension diagrams. This is flagged in the interaction file and must be reconciled before the combination map is treated as authoritative.
