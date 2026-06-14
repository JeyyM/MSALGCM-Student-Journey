# Student Program Status Transition Table

**Source:** `SEP 26 Post-M3 WIP - StudentProgramStatuses` (canonical).  
**Reference:** [`../student_program_status_flow.md`](../student_program_status_flow.md)  
**Excluded:** `Under Evaluation` / shifting-as-status (per [`../decisions.md`](../decisions.md))

Uses **canonical** program codes: `P1.3 = Strict Probationary`, `P1.4 = Ineligible`.

---

## Entry transitions

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| PRG-T001 | `[*]` | Program start (normal) | P1.0 | Eligible | Initial enrollment | Normal admission; "Initial status" | student_program_status_flow.md § P1.0 | High | |
| PRG-T002 | `[*]` | Program start (probationary offer) | P1.1 | Probationary | Probationary admission | Admission Application status was Offered - Probationary | student_program_status_flow.md § P1.1 | High | Tied to A5.1 |

---

## Normal academic-standing transitions

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| PRG-T010 | P1.0 | Eligible | P1.2 | SNAS | SNAS criteria reached | Manage Student Success / retention assessment | student_program_status_flow.md § P1.2 | High | |
| PRG-T011 | P1.2 | SNAS | P1.0 | Eligible | SNAS criteria not reached | SNAS criteria not reached | student_program_status_flow.md § P1.0 allowed previous | High | Recovery |
| PRG-T012 | P1.0 | Eligible | P1.1 | Probationary | Academic standards not met | Old student AND academic standards not complied OR probation requirements not complied | student_program_status_flow.md § P1.1 | Medium | Multiple triggers |
| PRG-T013 | P1.1 | Probationary | P1.0 | Eligible | Probation lifted | Criteria met to lift probationary status (Background notes) | student_program_status_flow.md Background § 2.d | Medium | End-of-AY re-evaluation |
| PRG-T014 | P1.1 | Probationary | P1.3 | Strict Probationary | SAP (IS) | Was Probationary previous AY AND strict requirements not complied; IS only | student_program_status_flow.md § P1.3 | Medium | SAP threshold deferred |
| PRG-T015 | P1.3 | Strict Probationary | P1.0 | Eligible | SAP criteria met | Criteria met to be Eligible (Background notes) | student_program_status_flow.md Background § 2.d | Medium | IS only |
| PRG-T016 | P1.0 | Eligible | P1.4 | Ineligible | Retention breached | End of term/semester AND program/strand retention rules breached | student_program_status_flow.md § P1.4 | High | **Terminal** |
| PRG-T017 | P1.1 | Probationary | P1.4 | Ineligible | Retention breached | Same as PRG-T016 | student_program_status_flow.md § P1.4 | High | **Terminal** |
| PRG-T018 | P1.2 | SNAS | P1.4 | Ineligible | Retention breached | Same as PRG-T016 | student_program_status_flow.md § P1.4 | High | **Terminal** |
| PRG-T019 | P1.3 | Strict Probationary | P1.4 | Ineligible | Retention breached OR SAP failure | Rules breached; notes say SAP fail "should be ineligible" | student_program_status_flow.md § P1.4 + Background | Medium | **Terminal** |
| PRG-T020 | P1.2 | SNAS | P1.1 | Probationary | Academic standards not met | "Initial status or SNAS" as previous for P1.1 | student_program_status_flow.md § P1.1 | Medium | SNAS → Probationary path implied |

---

## Graduation transitions

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| PRG-T030 | P1.0 | Eligible | P2.0 | Candidate for Graduation | First graduation check | Graduation eligibility rules complied | student_program_status_flow.md § P2.0 | High | Only P1.0 as explicit previous |
| PRG-T031 | P2.0 | Candidate for Graduation | P3.0 | Graduated | Final graduation check | Rules complied AND 1 week after commencement (attendance not required) | student_program_status_flow.md § P3.0 | High | **Terminal** |

---

## Exit / incomplete transitions

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| PRG-T040 | P1.0 | Eligible | P3.1 | Incomplete | University exit | University Exit submitted | student_program_status_flow.md § P3.1 | High | **Terminal** |
| PRG-T041 | P1.1 | Probationary | P3.1 | Incomplete | University exit | University Exit submitted | student_program_status_flow.md § P3.1 | High | **Terminal** |
| PRG-T042 | P1.2 | SNAS | P3.1 | Incomplete | University exit | University Exit submitted | student_program_status_flow.md § P3.1 | High | **Terminal** |
| PRG-T043 | P1.3 | Strict Probationary | P3.1 | Incomplete | University exit | University Exit submitted | student_program_status_flow.md § P3.1 | High | **Terminal** |
| PRG-T044 | P2.0 | Candidate for Graduation | P3.1 | Incomplete | University exit | University Exit submitted | student_program_status_flow.md § P3.1 | High | **Terminal** |

---

## Self-loops (optional in diagrams)

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| PRG-T050 | P1.0 | Eligible | P1.0 | Eligible | Ongoing good standing | SNAS criteria not reached; grades managed | student_program_status_flow.md § P1.0 process | Medium | Usually omitted from diagrams |
| PRG-T051 | P1.1 | Probationary | P1.1 | Probationary | Ongoing probation | Within AY before re-evaluation | student_program_status_flow.md | Medium | Optional |

---

## Disputed / deferred transitions

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| PRG-T060 | P1.1 | Probationary | P1.3 | Strict Probationary | SAP grade criteria | "Below 75" threshold | student_program_status_flow.md Background | **Low** | Threshold not finalized — defer detail |
| PRG-T061 | P2.0 | Candidate for Graduation | P1.0 | Eligible | Graduation check failed | Not documented | — | **Unknown** | **Do not diagram** |
| PRG-T062 | P1.1 | Probationary | P2.0 | Candidate for Graduation | Graduation while probationary | P2.0 previous is only P1.0 | student_program_status_flow.md § P2.0 | **Unknown** | **Do not diagram** |

---

## Transitions excluded from future diagrams

| Possible Transition | Reason Excluded | What Needs Confirmation |
|---|---|---|
| Any → `Under Evaluation` | Strikethrough / deprecated | Shifting is a process |
| SAP numeric thresholds on arrows | Deferred per decisions.md | Grade criteria for SAP |
| `P1.1`/`P1.2`/`P1.3` → `P2.0` | P2.0 allowed previous is only P1.0 | Can non-eligible standings become candidate? |
| `P3.0` → anything | Terminal | Alumni / second degree handling |
| Old combo-tab `P1.3 = Ineligible` | Code scheme cascade | Reconcile before COMBO diagrams |
