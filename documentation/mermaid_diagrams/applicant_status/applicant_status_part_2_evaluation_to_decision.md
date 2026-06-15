# Applicant Status — Part 2: Evaluation to Decision

## Purpose

Covers the middle of the admission funnel in **two diagrams**: (2A) requirements/exam evaluation, and (2B) admission results (offers, redirect, waitlist, rejection). Split into two because combining all of `A2.0`–`A5.5` would exceed the readable state/transition limits.

## Machine Type

Finite State Machine / State Transition System using Mermaid `stateDiagram-v2`.

Both diagrams are status machines: each box is an admission status and each arrow is a triggered transition.

## Source Planning Files

- [`../../diagram_planning/applicant_status_transition_table.md`](../../diagram_planning/applicant_status_transition_table.md) (APP-T007–APP-T031)
- [`../../diagram_planning/applicant_status_part_2_evaluation_to_decision.md`](../../diagram_planning/applicant_status_part_2_evaluation_to_decision.md)

---

## Diagram 2A — Requirements & Exam Evaluation

```mermaid
stateDiagram-v2
    state "A2.0 - Submitted - Complete Requirements" as A2_0
    state "A3.0 - Exam Required" as A3_0
    state "A3.1 - Exam Exempted" as A3_1
    state "A3.2 - Not Qualified (initial eval) [Terminal]" as A3_2
    state "A4.0 - Exam Taken" as A4_0
    state "A4.1 - Exam Pending" as A4_1
    state "A4.2 - Not Qualified (no exam) [Terminal]" as A4_2
    state "A4.3 - Further Evaluation Required" as A4_3

    A2_0 --> A3_0: Exam required
    A2_0 --> A3_1: Exam exempted
    A2_0 --> A3_2: Failed initial evaluation
    A2_0 --> A4_3: Exam not required
    A3_0 --> A4_0: Exam taken
    A3_0 --> A4_1: Exam pending
    A3_0 --> A4_2: Exam window lapsed
    A4_1 --> A4_0: Exam taken
    A4_1 --> A4_2: Exam window lapsed
    A4_0 --> A4_3: Further screening
    A3_1 --> [*]: To admission results
    A4_3 --> [*]: To admission results
    A3_2 --> [*]
    A4_2 --> [*]
```

## Diagram 2B — Admission Results

Shows admission results from **three entry paths** per the workbook: `A3.1 Exam Exempted` (skips exam), `A4.0 Exam Taken`, and `A4.3 Further Evaluation Required`. Note: `A5.1 Probationary` is **not** reachable from `A3.1` — only from `A4.0` or `A4.3`.

```mermaid
stateDiagram-v2
    direction LR

    state "After evaluation" as eval {
        direction TB
        state "A3.1 - Exam Exempted" as A3_1
        state "A4.0 - Exam Taken" as A4_0
        state "A4.3 - Further Evaluation Required" as A4_3
    }

    state "Admission results" as results {
        direction TB
        state "A5.0 - Offered" as A5_0
        state "A5.1 - Offered - Probationary" as A5_1
        state "A5.2 - Offered - Redirected" as A5_2
        state "A5.3 - Waitlisted" as A5_3
        state "A5.5 - Not Qualified [Terminal]" as A5_5
    }

    A3_1 --> A5_0: Scores within cutoff
    A3_1 --> A5_2: Redirected
    A3_1 --> A5_3: Waitlisted
    A3_1 --> A5_5: Outside cutoff
    A4_0 --> A5_0: Scores within cutoff
    A4_0 --> A5_1: Probationary offer
    A4_0 --> A5_2: Redirected
    A4_0 --> A5_3: Waitlisted
    A4_0 --> A5_5: Outside cutoff
    A4_3 --> A5_0: Passed further evaluation
    A4_3 --> A5_1: Probationary offer
    A4_3 --> A5_2: Redirected
    A4_3 --> A5_3: Waitlisted
    A4_3 --> A5_5: Outside cutoff
    A5_3 --> A5_0: Slot opened
    A5_5 --> [*]
```

## States Included

| Code | Mermaid ID | Label | Type | Notes |
|---|---|---|---|---|
| A2.0 | A2_0 | A2.0 - Submitted - Complete Requirements | Transitional | Entry from Part 1 |
| A3.0 | A3_0 | A3.0 - Exam Required | Transitional | |
| A3.1 | A3_1 | A3.1 - Exam Exempted | Transitional | Entry to results (exam exempted; no A5.1) |
| A3.2 | A3_2 | A3.2 - Not Qualified (initial eval) | Terminal | |
| A4_0 | A4_0 | A4.0 - Exam Taken | Transitional | Entry to results (with exam) |
| A4.1 | A4_1 | A4.1 - Exam Pending | Transitional | |
| A4.2 | A4_2 | A4.2 - Not Qualified (no exam) | Terminal | |
| A4.3 | A4_3 | A4.3 - Further Evaluation Required | Transitional | Entry to results (further eval) |
| A5.0 | A5_0 | A5.0 - Offered | Transitional | Boundary to Part 3 |
| A5.1 | A5_1 | A5.1 - Offered - Probationary | Transitional | IS/GS/SOL; → program Probationary |
| A5.2 | A5_2 | A5.2 - Offered - Redirected | Transitional | |
| A5.3 | A5_3 | A5.3 - Waitlisted | Transitional | |
| A5.5 | A5_5 | A5.5 - Not Qualified | Terminal | |

## Transition Details

| Transition | Short Label | Full Condition / Explanation | Certainty |
|---|---|---|---|
| A2_0 → A3_0 | Exam required | Evaluated by OAS/OASIS AND exam required by strand/program | High |
| A2_0 → A3_1 | Exam exempted | Evaluated by OAS/OASIS AND applicant exempted | High |
| A2_0 → A3_2 | Failed initial evaluation | Evaluated by OAS/OASIS AND not qualified | High |
| A2_0 → A4_3 | Exam not required | Program does not require an exam | High |
| A3_0 → A4_0 | Exam taken | Applicant has taken the admission exam | High |
| A3_0 → A4_1 | Exam pending | Must undergo exam AND not yet taken AND slots/window open | High |
| A3_0 → A4_2 | Exam window lapsed | Not taken AND no slots / reschedule period lapsed | High |
| A4_1 → A4_0 | Exam taken | Applicant takes the exam during the pending window | High |
| A4_1 → A4_2 | Exam window lapsed | Window/slots lost | High |
| A4_0 → A4_3 | Further screening | Strand/program requires interview/publication/etc. | Medium |
| A3_1 → A5_0 | Scores within cutoff | Exam exempted; scores within cutoff | High |
| A3_1 → A5_2 | Redirected | Exam exempted; qualified for different program | High |
| A3_1 → A5_3 | Waitlisted | Exam exempted; qualified but no slots | High |
| A3_1 → A5_5 | Outside cutoff | Exam exempted; scores outside cutoff | High |
| A4_0 → A5_0 | Scores within cutoff | Test scores within cutoff | High |
| A4_0 → A5_1 | Probationary offer | Additional requirements to maintain stay | High |
| A4_0 → A5_2 | Redirected | Qualified for a different strand/program | High |
| A4_0 → A5_3 | Waitlisted | Qualified but no slots | High |
| A4_0 → A5_5 | Outside cutoff | Scores outside cutoff for any strand/program | High |
| A4_3 → A5_0 | Passed further evaluation | Passed further evaluation / screening | High |
| A4_3 → A5_1 | Probationary offer | Additional requirements to maintain stay | High |
| A4_3 → A5_2 | Redirected | Qualified for a different strand/program | High |
| A4_3 → A5_3 | Waitlisted | Qualified but no slots | High |
| A4_3 → A5_5 | Outside cutoff | Scores outside cutoff | High |
| A5_3 → A5_0 | Slot opened | Waitlisted applicant considered when others decline | Medium |

## Excluded or Unclear Transitions

| Possible Transition | Reason Not Included | What Needs Confirmation |
|---|---|---|
| A3_1 → A5_1 Probationary | Not in workbook allowed-previous for A5.1 | Confirm exempted applicants can never get probationary offer |
| A5_5 → A5_4 Reconsidered | Low certainty; revives a terminal state | Whether appeal should branch before A5.5 |
| A4_3 dual trigger (exam-not-required vs further screening) | Two triggers collapsed to one state | Whether these are truly one status |

## Reader Notes

- **`A3.1` and `A4.3` outbound edges** are now shown explicitly in Diagram 2B (previously omitted for legibility, which made `A3.1` look like a dead end). Diagram 2A uses boundary markers (`To admission results`) for the same paths.
- **`A5.1 Probationary`** is reachable from `A4.0` and `A4.3` only — not from `A3.1 Exam Exempted` (per allowed-previous on the Post-M3 tab).
- Terminal states `A3.2`, `A4.2`, `A5.5` are repeated in Part 4 where all terminal/exception states are collected.
