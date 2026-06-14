# Student Status Transition Table

**Source:** `SEP 19 Post-M3 WIP - StudentStatuses` (canonical).  
**Reference:** [`../student_status_flow.md`](../student_status_flow.md)  
**Excluded codes:** `S3.5`, `S3.6`, `S3.7` (per [`../decisions.md`](../decisions.md))

Forward directions inferred from allowed-previous statuses unless explicitly documented.

---

## Entry transitions (from admission)

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| STU-T001 | A7.0 | Officially Admitted | S1.0 | Active - Without Enrollment | Official acceptance complete | Admission application was Reserved; not yet enrolled | student_status_flow.md § S1.0 | High | Cross-dimension; see APP-T048 |
| STU-T002 | A7.1 | Provisionally Admitted | S1.0 | Active - Without Enrollment | Provisional admission | Same as STU-T001 | student_status_flow.md § S1.0 | High | |
| STU-T003 | A6.0 | Reserved | S1.0 | Active - Without Enrollment | Reserved status | "Admission Application Status was Reserved" OR returnee | student_status_flow.md § S1.0 activities | Medium | Reserved also maps to admitted path |

---

## Normal transitions

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| STU-T010 | S1.0 | Active - Without Enrollment | S2.0 | Active | Enrolled / enlisted | Student is enrolled OR enlisted | student_status_flow.md § S2.0 | High | |
| STU-T011 | S2.0 | Active | S2.1 | Active - Residency | Residency registration | Registered for Residency activity; UG/GS/SOL | student_status_flow.md § S2.1 | High | |
| STU-T012 | S2.1 | Active - Residency | S2.0 | Active | Re-enrolled | Return to normal enrollment | student_status_flow.md § S2.0 allowed previous S2.1 | Medium | Implied reverse |
| STU-T013 | S2.0 | Active | S2.2 | Active - Under LOA | LOA filed (within max) | Filed LOA AND period ≤ max AND last enrollment ≤ 6 trimesters ago | student_status_flow.md § S2.2 | High | |
| STU-T014 | S2.0 | Active | S2.3 | Inactive - Prolonged Leave | LOA exceeds limits | Filed LOA AND period > max AND last enrollment > 6 trimesters ago | student_status_flow.md § S2.3 | High | Post-M3 new status |
| STU-T015 | S2.2 | Active - Under LOA | S1.0 | Active - Without Enrollment | Returnee approved | Approved as returnee | student_status_flow.md § S1.0 allowed previous S2.2 | Medium | Reverse of STU-T013 |
| STU-T016 | S2.3 | Inactive - Prolonged Leave | S1.0 | Active - Without Enrollment | Returnee approved | Approved as returnee | student_status_flow.md § S1.0 allowed previous S2.3 | Medium | |
| STU-T017 | S3.1 | Inactive - AWOL | S1.0 | Active - Without Enrollment | Returnee approved | Approved as returnee | student_status_flow.md § S1.0 allowed previous S3.1 | Medium | |
| STU-T018 | S2.0 | Active | S3.1 | Inactive - AWOL | Did not enroll, no LOA | Did not enroll AND did not file LOA AND LOA period lapsed AND last enrollment ≤ 6 trimesters | student_status_flow.md § S3.1 | High | |
| STU-T019 | S2.1 | Active - Residency | S3.1 | Inactive - AWOL | Did not enroll, no LOA | Same as STU-T018 | student_status_flow.md § S3.1 allowed previous S2.1 | Medium | AWOL from residency |
| STU-T020 | S1.0 | Active - Without Enrollment | S3.1 | Inactive - AWOL | Did not enroll, no LOA | Same as STU-T018 | student_status_flow.md § S3.1 allowed previous S1.0 | Medium | Never enrolled → AWOL |
| STU-T021 | S2.0 | Active | S3.2 | Inactive - Suspended | Disciplinary verdict | Disciplinary verdict given | student_status_flow.md § S3.2 | High | |
| STU-T022 | S2.1 | Active - Residency | S3.2 | Inactive - Suspended | Disciplinary verdict | Disciplinary verdict given | student_status_flow.md § S3.2 | Medium | |
| STU-T023 | S1.0 | Active - Without Enrollment | S3.2 | Inactive - Suspended | Disciplinary verdict | Disciplinary verdict given | student_status_flow.md § S3.2 | Medium | |
| STU-T024 | S2.2 | Active - Under LOA | S3.2 | Inactive - Suspended | Disciplinary verdict | Disciplinary verdict given | student_status_flow.md § S3.2 | Medium | |
| STU-T025 | S3.1 | Inactive - AWOL | S3.2 | Inactive - Suspended | Disciplinary verdict | Disciplinary verdict given | student_status_flow.md § S3.2 | Medium | |
| STU-T026 | S2.3 | Inactive - Prolonged Leave | S3.2 | Inactive - Suspended | Disciplinary verdict | Disciplinary verdict given | student_status_flow.md § S3.2 | Medium | |
| STU-T027 | S3.2 | Inactive - Suspended | S2.0 | Active | Suspension served | Re-enrollment after suspension | student_status_flow.md § S2.0 allowed previous S3.2 | Medium | Implied recovery |
| STU-T028 | S2.0 | Active | S4.0 | Graduated | All programs graduated | Program status of all programs is Graduated | student_status_flow.md § S4.0 | High | Cross-dimension trigger |
| STU-T029 | S2.0 | Active | S4.1 | Exited on Good Standing | University exit | University Exit submitted | student_status_flow.md § S4.1 | High | **Terminal** |
| STU-T030 | S2.1 | Active - Residency | S4.1 | Exited on Good Standing | University exit | University Exit submitted | student_status_flow.md § S4.1 | High | **Terminal** |
| STU-T031 | S1.0 | Active - Without Enrollment | S4.1 | Exited on Good Standing | University exit | University Exit submitted | student_status_flow.md § S4.1 | Medium | |
| STU-T032 | S2.2 | Active - Under LOA | S4.1 | Exited on Good Standing | University exit | University Exit submitted | student_status_flow.md § S4.1 | High | **Terminal** |
| STU-T033 | S2.3 | Inactive - Prolonged Leave | S4.1 | Exited on Good Standing | University exit | University Exit submitted | student_status_flow.md § S4.1 | High | **Terminal** |
| STU-T034 | S3.1 | Inactive - AWOL | S4.1 | Exited on Good Standing | University exit | University Exit submitted | student_status_flow.md § S4.1 | High | **Terminal** |
| STU-T035 | S3.2 | Inactive - Suspended | S4.1 | Exited on Good Standing | University exit | University Exit submitted | student_status_flow.md § S4.1 | Medium | Unusual but allowed previous |
| STU-T036 | S2.0 | Active | S4.2 | Exited - Permanent Disqualification | Disciplinary exit | Verdict: non-readmission, dismissal, exclusion, or expulsion | student_status_flow.md § S4.2 | High | **Terminal** |
| STU-T037 | S3.2 | Inactive - Suspended | S4.2 | Exited - Permanent Disqualification | Disciplinary exit | Same as STU-T036 | student_status_flow.md § S4.2 | High | **Terminal** |

---

## Self-loops and grace-period behavior

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| STU-T040 | S2.0 | Active | S2.0 | Active | Term break grace | Is Active AND during term/semester breaks until last day of late enrollment AND did not enroll | student_status_flow.md § S2.0 | Medium | Optional in diagram; explains pre-AWOL period |

---

## Disputed / low-certainty transitions

| Transition ID | From Code | From Label | To Code | To Label | Trigger/Event | Conditions | Source Section/File | Certainty | Notes |
|---|---|---|---|---|---|---|---|---|---|
| STU-T050 | S2.2 | Active - Under LOA | S2.3 | Inactive - Prolonged Leave | LOA duration exceeded | LOA filing but duration/max/trimester rules | student_status_flow.md edge cases | **Low** | Workbook shows both from S2.0; LOA→Prolonged path unclear |
| STU-T051 | S2.1 | Active - Residency | S2.2 | Active - Under LOA | LOA from residency | Not documented | student_status_flow.md | **Unknown** | No allowed previous; **do not diagram** |
| STU-T052 | S4.0 | Graduated | `[*]` | End | Journey complete | — | student_status_flow.md edge cases | Medium | S4.0 not labeled terminal in tab |

---

## Transitions excluded from future diagrams

| Possible Transition | Reason Excluded | What Needs Confirmation |
|---|---|---|
| Any → `S3.5`/`S3.6`/`S3.7` | Strikethrough / deprecated | Consolidated into S4.2 or dropped |
| `S2.2` → `S2.3` (STU-T050) | Low certainty; both may originate from S2.0 | Does LOA ever transition to Prolonged Leave directly? |
| `S2.1` → `S2.2` (STU-T051) | Unknown | Residency + LOA interaction |
| `S3.2` → `S1.0` returnee | Not in allowed previous | Suspension return path: S1.0 or S2.0 only? |
| Graduated with clearance hold | Not modeled | Separate status? (Notes #7) |
| `S4.0` → further enrollment (BS/MS) | Notes #6 open | Post-graduation student status |
