# Diagram Creation Notes

Decisions and simplifications made while turning the planning layer into final Mermaid diagrams. Read alongside [`../diagram_planning/`](../diagram_planning/README.md).

## Sources of truth (in order)

1. [`../diagram_planning/`](../diagram_planning/README.md) transition tables (`APP-T###`, `STU-T###`, `PRG-T###`, `COMBO-T###`)
2. [`../decisions.md`](../decisions.md) (include/exclude rules)
3. The narrative flow docs (`../applicant_status_flow.md`, etc.) for context

## Syntax conventions used

- All states declared with `state "Code - Name" as ID` so IDs are Mermaid-safe (no dots/spaces/slashes).
- Code `A1.0` → ID `A1_0`, `S2.3` → `S2_3`, `P1.4` → `P1_4`.
- Terminal states carry `[Terminal]` in the label and route to `[*]`.
- `S4.0 Graduated` carries `[Terminal?]` (student-status Graduated is not explicitly terminal in the workbook).
- Tentative (Low-certainty but shown) edges carry `[Tentative]` in the transition label.
- `Unknown`-certainty transitions are never drawn.

## Certainty handling

| Certainty | In diagram? | How |
|---|---|---|
| High | Yes | Normal edge |
| Medium | Yes | Normal edge (noted in Transition Details) |
| Low | Only if planning marked safe | `[Tentative]` label |
| Unknown | No | Listed in Excluded/Unclear table |

## Readability simplifications

- **Applicant results (APP-02 part 2):** the offer-result diagram is drawn from the representative entry state `A4.0 Exam Taken`. The alternate entries `A3.1 Exam Exempted` and `A4.3 Further Evaluation Required` feed the *same* result set (per `APP-T017/T019/T024/T025/T027/T028/T030/T031`); this is stated in Reader Notes rather than drawn, to avoid ~15 crossing edges.
- **Multi-source exits:** in student and program terminal diagrams, exits that originate from many states (e.g. University Exit → `S4.1`, or any standing → `P3.1 Incomplete`) are drawn from the primary source and annotated "also from …" to keep the graph clean. Full lists remain in the transition tables.
- **Self-loops** (e.g. `S2.0` term-break grace, `P1.x` persistence) are omitted from the drawn graph and described in Reader Notes; they do not change reachability.

## Excluded globally

- Strikethrough codes: `A3.3`, `A9.0`, `S3.5`, `S3.6`, `S3.7`, program `Under Evaluation`.
- `Yes?` combination pairs and SAP numeric thresholds (deferred).
- Reconsidered appeal loop (`A5.5 → A5.4`, `APP-T032/T036/T040`) — Low certainty, not drawn.
- `STU-T051` (Residency → LOA) and `PRG-T061/T062` — Unknown, not drawn.

## Cross-dimension policy

Detailed `A*`/`S*`/`P*` diagrams never mix dimensions. Crossing only appears in:
- `applicant_status/...part_3...` (ends at the single hand-off node `S1.0`)
- `combined_lifecycle/applicant_to_student_bridge.md`
- `combined_lifecycle/high_level_lifecycle_overview.md`
- `combined_lifecycle/student_status_vs_program_status_interaction.md`

## Combination rules

Rendered primarily as **tables**, not a graph (91+ pairings, plus a legacy-vs-canonical code mismatch). A small `flowchart TD` shows only the three forced cross-impacts (`COMBO-T001/T003/T004`).
