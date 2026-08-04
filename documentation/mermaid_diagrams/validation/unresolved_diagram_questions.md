# Unresolved Diagram Questions

Questions that could change the correctness of the Mermaid diagrams. Grouped by area; each notes the affected diagram file(s). Source: [`../../diagram_planning/unclear_transitions.md`](../../diagram_planning/unclear_transitions.md) and [`../../open_questions.md`](../../open_questions.md).

## Applicant diagrams

| # | Question | Affected diagram(s) | Current handling |
|---|---|---|---|
| 1 | Is `A5.5 Not Qualified` truly terminal, or should an appeal (`A5.4 Reconsidered`) branch before rejection? | part_2, part_4 | Appeal loop excluded (Low) |
| 2 | Can enrollment in the admission term move `A7.0/A7.1` **directly** to `S2.0`, skipping `S1.0`? | part_3, bridge | Direct edge omitted; only via S1.0 |
| 3 | What student status is assigned on admission cancellation (`A8.0`, `A8.1`)? | part_4 | Cross-dimension edge omitted |
| 4 | Is `A4.3 Further Evaluation Required` one status or two (exam-not-required vs further screening)? | part_2 | Modeled as one state |
| 5 | Can a deferred applicant (`A7.2`) re-enter the funnel? | part_4 | Drawn non-terminal; no re-entry edge |

## Student status diagrams

| # | Question | Affected diagram(s) | Current handling |
|---|---|---|---|
| 6 | Does `S2.2 Under LOA` escalate directly to `S2.3 Prolonged Leave`, or do both originate only from `S2.0`? | part_2 | Both from S2.0; S2.2→S2.3 excluded (Low) |
| 7 | Can a `S2.1 Residency` student file LOA (`S2.1 → S2.2`)? | part_2 | Excluded (Unknown) |
| 8 | Exact return paths: does a returnee always re-enter at `S1.0`? Does a suspended student return to `S2.0` or `S1.0`? | part_2, part_3 | Returnee→S1.0 and Suspended→S2.0 marked **[Tentative]** |
| 9 | Do residency/LOA/prolonged-leave states feed AWOL and suspension identically to `S2.0`? | part_3 | Only `S2.0` (and `S3.1`) sources drawn |
| 10 | Can a suspended student exit on **good standing** (`S3.2 → S4.1`)? | part_3 | In allowed-previous; collapsed/noted |
| 11 | Is `S4.0 Graduated` actually terminal, or do graduates continue (BS→MS, alumni)? | part_4 | Labeled `[Alumni may continue]` (executive default) |
| 12 | Should "Graduated with clearance hold" be a separate status? | part_4 | Not modeled |
| 13 | Do `S2.2`/`S2.3 LOA` students keep campus/SLC access? | part_2 | Not a transition; noted only |

## Student program status diagrams

| # | Question | Affected diagram(s) | Current handling |
|---|---|---|---|
| 14 | What are the exact SAP grade criteria (workbook flags "below 75 needs to be updated")? | part_2 | No numeric threshold on arrows |
| 15 | Does a failing SAP (`P1.3`) student map to `P1.4 Ineligible` ("asked to withdraw")? | part_2 | Drawn as Medium edge |
| 16 | Can warning standings (`P1.1/P1.2/P1.3`) become `P2.0 Candidate`, or only `P1.0`? | part_3 | Only `P1.0 → P2.0` drawn |
| 17 | Is there a revert path if the final graduation check fails (`P2.0 → P1.0`)? | part_3 | Excluded (Unknown) |
| 18 | Does `P1.2 SNAS` transition to `P1.1 Probationary`? | part_2 | Excluded; noted (Medium) |

## Combination / cross-dimension

| # | Question | Affected diagram(s) | Current handling |
|---|---|---|---|
| 19 | When will the combination tab be regenerated with **canonical** codes (`P1.3 = Strict Probationary`, `S4.x` exits)? | interaction, parallel FSM | **Done in-repo** (`combination_matrix_post_m3.csv`); Excel import pending |
| 20 | Is `S2.2 Under LOA` + `P1.1 Probationary` allowed (combo tab: Yes; Notes #3: tentatively No)? | interaction | **Yes** in in-repo matrix (executive default) |
| 21 | Are the `Yes?` pairs (Residency×Probationary/SNAS/Ineligible, LOA×SNAS/Candidate, Suspended×Candidate) allowed? | interaction | **No** in in-repo matrix (former Yes? → No) |
| 22 | Is the Exit → `P3.1 Incomplete` update automatic or manual? | interaction, program part_3 | Drawn as forced impact |

## Scope questions (affect whether statuses exist at all)

| # | Question | Affected diagram(s) | Current handling |
|---|---|---|---|
| 23 | Should scholarship, exchange, cross-enrollee, transferee, minor, shifting be statuses or separate processes? | all | Treated as non-statuses (excluded) |
| 24 | Are deprecated codes (`A3.3`, `A9.0`, `S3.5–S3.7`, program `Under Evaluation`) fully retired? | all | Excluded |

## How these map to status

- Questions **8, 14–15** drive the **Needs Review** ratings on program part_2 and student part_4 / bridge.
- Questions **6–13, 19–21** drive the **Needs Stakeholder Confirmation** ratings on student part_2/part_3 and the interaction file.
- Resolving these should be done **before** the affected diagrams are treated as authoritative or used to generate a data model.
