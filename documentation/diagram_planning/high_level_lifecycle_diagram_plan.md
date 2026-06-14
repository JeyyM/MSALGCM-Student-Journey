# Diagram Plan: LIFE-01 — High-Level Lifecycle Overview

## Purpose

Single **simplified** overview diagram showing broad phases only — not every status code. For onboarding and executive summary.

## Source Files

- [`../lifecycle_summary.md`](../lifecycle_summary.md)
- All transition tables (phase boundaries only)

## Included States (composite phases)

| Phase ID | Mermaid ID | Label | Type | Maps to (reference only) |
|---|---|---|---|---|
| Start | `[*]` | Start | Start | |
| Applicant | PHASE_APPLICANT | Applicant | Transitional | A0–A8.x |
| Accepted | PHASE_ACCEPTED | Accepted Applicant | Transitional | A6.0–A7.x → S1.0 |
| ActiveStudent | PHASE_ACTIVE | Active Student | Active | S2.0, S2.1 |
| ProgramStanding | PHASE_PROGRAM | Program Standing | Active | P1.x, P2.0 |
| Disruption | PHASE_DISRUPT | LOA / AWOL / Suspended | Inactive | S2.2, S2.3, S3.x |
| Outcome | PHASE_OUTCOME | Graduation / Exit / Terminal | Terminal | S4.x, P3.x, P1.4 |

## Included Transitions

| Transition ID | From | To | Label | Certainty | Notes |
|---|---|---|---|---|---|
| LIFE-T001 | `[*]` | PHASE_APPLICANT | Apply to university | High | |
| LIFE-T002 | PHASE_APPLICANT | PHASE_ACCEPTED | Admitted / reserved | High | Collapses A5–A7 |
| LIFE-T003 | PHASE_ACCEPTED | PHASE_ACTIVE | Enrolled | High | S1.0 → S2.0 |
| LIFE-T004 | PHASE_ACTIVE | PHASE_PROGRAM | Academic standing tracked | High | Parallel dimension — use note |
| LIFE-T005 | PHASE_ACTIVE | PHASE_DISRUPT | Leave / absence / discipline | Medium | Optional branch |
| LIFE-T006 | PHASE_DISRUPT | PHASE_ACTIVE | Returnee re-enrolls | Medium | |
| LIFE-T007 | PHASE_ACTIVE | PHASE_OUTCOME | Graduate or exit | High | |
| LIFE-T008 | PHASE_APPLICANT | PHASE_OUTCOME | Rejected / cancelled | High | Terminal applicant paths |

## Excluded States or Transitions

| Item | Reason |
|---|---|
| Individual A*, S*, P* codes | Detail diagrams |
| Reconsidered, SAP thresholds | Unclear |
| Combination matrix | COMBO table |

## Diagram Boundaries

**Includes:** 6–8 composite nodes maximum.  
**Excludes:** All detail from APP/STU/PRG parts.

## Recommended Mermaid Type

```text
stateDiagram-v2
```

Alternative: `flowchart LR` for left-to-right timeline feel — document choice at generation time.

## Complexity Safeguards

- **Hard cap: 8 nodes.**
- Label parallel Program Standing as note: *"runs in parallel with Active Student — see PRG-* diagrams"*
- Do not draw bidirectional coupling between PHASE_ACTIVE and PHASE_PROGRAM except LIFE-T004 as annotated edge.

## Open Questions

- Show PHASE_DISRUPT as optional subgraph or separate LIFE-02 later?
- Include deferred/cancelled applicant path to PHASE_OUTCOME?

## Example structure (not final Mermaid)

```text
[*] --> PHASE_APPLICANT
PHASE_APPLICANT --> PHASE_ACCEPTED
PHASE_APPLICANT --> PHASE_OUTCOME : rejected
PHASE_ACCEPTED --> PHASE_ACTIVE
PHASE_ACTIVE --> PHASE_OUTCOME
```

*(Syntax illustration only — not the deliverable diagram.)*
