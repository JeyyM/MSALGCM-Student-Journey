// Authoritative status model for the DLSU applicant/student/program lifecycle.
// Source: documentation/applicant_status_flow.md, student_status_flow.md,
// student_program_status_flow.md, and the final mermaid code diagrams.
// Codes use canonical Post-M3 WIP scheme. IDs use underscores (A2_0) to stay key-safe;
// `code` is the human-facing dotted form (A2.0).

export const DIMENSIONS = {
  A: { key: 'A', label: 'Applicant', color: '#6366f1' },
  S: { key: 'S', label: 'Student Status', color: '#0ea5e9' },
  P: { key: 'P', label: 'Program Status', color: '#10b981' },
  X: { key: 'X', label: 'Cross-impact', color: '#f59e0b' },
};

// The 4 sections the user asked to always surface.
export const SECTIONS = [
  { id: 'applicant', label: 'Application & Admission', dim: 'A' },
  { id: 'student', label: 'Student Standing', dim: 'S' },
  { id: 'program', label: 'Program Standing', dim: 'P' },
  { id: 'outcome', label: 'Outcome', dim: 'X' },
];

// kind: start | transitional | terminal | handoff
export const STATES = {
  // ---------- Applicant (A) ----------
  A0: { id: 'A0', code: 'A0', dim: 'A', kind: 'start', label: 'Draft', desc: 'Applicant account created; application drafted (not submitted).' },
  A1_0: { id: 'A1_0', code: 'A1.0', dim: 'A', kind: 'transitional', label: 'Submitted Form', desc: 'Application submitted (within the last 3 terms).' },
  A2_0: { id: 'A2_0', code: 'A2.0', dim: 'A', kind: 'transitional', label: 'Submitted - Complete Requirements', desc: 'Mandatory requirements completed.' },
  A2_1: { id: 'A2_1', code: 'A2.1', dim: 'A', kind: 'transitional', label: 'Submitted - Deficiencies', desc: 'Pending requirements OR OAS/OASIS requires resubmission.' },
  A3_0: { id: 'A3_0', code: 'A3.0', dim: 'A', kind: 'transitional', label: 'Exam Required', desc: 'Strand/program requires an admission exam.' },
  A3_1: { id: 'A3_1', code: 'A3.1', dim: 'A', kind: 'transitional', label: 'Exam Exempted', desc: 'Evaluated by OAS/OASIS and exempted from the exam.' },
  A3_2: { id: 'A3_2', code: 'A3.2', dim: 'A', kind: 'terminal', label: 'Not Qualified (initial eval)', desc: 'Rejected before exam; no forward path.' },
  A4_0: { id: 'A4_0', code: 'A4.0', dim: 'A', kind: 'transitional', label: 'Exam Taken', desc: 'Applicant has taken the admission exam.' },
  A4_1: { id: 'A4_1', code: 'A4.1', dim: 'A', kind: 'transitional', label: 'Exam Pending', desc: 'Must take exam; not yet taken; slots/window still open.' },
  A4_2: { id: 'A4_2', code: 'A4.2', dim: 'A', kind: 'terminal', label: 'Not Qualified (no exam)', desc: 'Exam not taken; slots/reschedule window lapsed.' },
  A4_3: { id: 'A4_3', code: 'A4.3', dim: 'A', kind: 'transitional', label: 'Further Evaluation Required', desc: 'Exam not required OR further screening (interview, publication).' },
  A5_0: { id: 'A5_0', code: 'A5.0', dim: 'A', kind: 'transitional', label: 'Offered', desc: 'Test scores within cutoff OR passed further evaluation.' },
  A5_1: { id: 'A5_1', code: 'A5.1', dim: 'A', kind: 'transitional', label: 'Offered - Probationary', desc: 'Offered with additional requirements to maintain stay (IS/GS/SOL).' },
  A5_2: { id: 'A5_2', code: 'A5.2', dim: 'A', kind: 'transitional', label: 'Offered - Redirected', desc: 'Qualified for a different strand/program in DLSU.' },
  A5_3: { id: 'A5_3', code: 'A5.3', dim: 'A', kind: 'transitional', label: 'Waitlisted', desc: 'Qualified but no slots; may be considered if others decline.' },
  A5_5: { id: 'A5_5', code: 'A5.5', dim: 'A', kind: 'terminal', label: 'Not Qualified', desc: 'Test scores outside cutoff for any strand/program.' },
  A6_0: { id: 'A6_0', code: 'A6.0', dim: 'A', kind: 'transitional', label: 'Reserved', desc: 'Official Acceptance Fee paid or waived; acceptance period open.' },
  A6_1: { id: 'A6_1', code: 'A6.1', dim: 'A', kind: 'terminal', label: 'Cancelled - non-payment of fee', desc: 'Admission term lapsed without paying the acceptance fee.' },
  A7_0: { id: 'A7_0', code: 'A7.0', dim: 'A', kind: 'handoff', label: 'Officially Admitted', desc: 'Requirements complete; becomes a Student (hand-off to S1.0).' },
  A7_1: { id: 'A7_1', code: 'A7.1', dim: 'A', kind: 'handoff', label: 'Provisionally Admitted', desc: 'Admitted with requirements still pending (hand-off to S1.0).' },
  A7_2: { id: 'A7_2', code: 'A7.2', dim: 'A', kind: 'terminal', label: 'Deferred', desc: 'Did not enroll; late-enrollment period lapsed.' },
  A8_0: { id: 'A8_0', code: 'A8.0', dim: 'A', kind: 'terminal', label: 'Cancelled - non-submission of reqs', desc: 'Provisional admission expired after 1 year.' },
  A8_1: { id: 'A8_1', code: 'A8.1', dim: 'A', kind: 'terminal', label: 'Cancelled - Withdrawal', desc: 'Enrolled in admission term then withdrew.' },

  // ---------- Student Status (S) ----------
  S1_0: { id: 'S1_0', code: 'S1.0', dim: 'S', kind: 'transitional', label: 'Active - Without Enrollment', desc: 'Admitted/returnee, not yet enrolled.' },
  S2_0: { id: 'S2_0', code: 'S2.0', dim: 'S', kind: 'transitional', label: 'Active', desc: 'The normal enrolled/enlisted student.' },
  S2_1: { id: 'S2_1', code: 'S2.1', dim: 'S', kind: 'transitional', label: 'Active - Residency', desc: 'Registered for Residency activity (UG/GS/SOL).' },
  S2_2: { id: 'S2_2', code: 'S2.2', dim: 'S', kind: 'transitional', label: 'Active - Under LOA', desc: 'Approved leave of absence within the maximum.' },
  S2_3: { id: 'S2_3', code: 'S2.3', dim: 'S', kind: 'transitional', label: 'Inactive - Prolonged Leave', desc: 'Leave beyond the maximum / long absence (Post-M3).' },
  S3_1: { id: 'S3_1', code: 'S3.1', dim: 'S', kind: 'transitional', label: 'Inactive - AWOL', desc: 'Did not enroll and did not file LOA.' },
  S3_2: { id: 'S3_2', code: 'S3.2', dim: 'S', kind: 'transitional', label: 'Inactive - Suspended', desc: 'Disciplinary suspension.' },
  S4_0: { id: 'S4_0', code: 'S4.0', dim: 'S', kind: 'terminal', label: 'Graduated', desc: 'All programs graduated. Alumni may continue (non-terminal for new enrollment per executive default #7).' },
  S4_1: { id: 'S4_1', code: 'S4.1', dim: 'S', kind: 'terminal', label: 'Exited on Good Standing', desc: 'Left the University voluntarily in good standing.' },
  S4_2: { id: 'S4_2', code: 'S4.2', dim: 'S', kind: 'terminal', label: 'Exited - Permanent Disqualification', desc: 'Disciplinary dismissal / exclusion / expulsion.' },

  // ---------- Program Status (P) ----------
  P1_0: { id: 'P1_0', code: 'P1.0', dim: 'P', kind: 'transitional', label: 'Eligible', desc: 'Good academic standing in the program.' },
  P1_1: { id: 'P1_1', code: 'P1.1', dim: 'P', kind: 'transitional', label: 'Probationary', desc: 'Academic warning / probationary admission.' },
  P1_2: { id: 'P1_2', code: 'P1.2', dim: 'P', kind: 'transitional', label: 'SNAS', desc: 'Subject to Non-Academic Status / academic warning.' },
  P1_3: { id: 'P1_3', code: 'P1.3', dim: 'P', kind: 'transitional', label: 'Strict Probationary (IS only)', desc: 'SAP — was probationary and standards still not complied.' },
  P1_4: { id: 'P1_4', code: 'P1.4', dim: 'P', kind: 'terminal', label: 'Ineligible', desc: 'Program/strand retention rules breached.' },
  P2_0: { id: 'P2_0', code: 'P2.0', dim: 'P', kind: 'transitional', label: 'Candidate for Graduation', desc: 'Graduation eligibility rules complied.' },
  P3_0: { id: 'P3_0', code: 'P3.0', dim: 'P', kind: 'terminal', label: 'Graduated', desc: 'Graduated (1 week after commencement).' },
  P3_1: { id: 'P3_1', code: 'P3.1', dim: 'P', kind: 'terminal', label: 'Incomplete', desc: 'University Exit submitted while program active.' },
};

// Each transition: { from, to, label, dim }
export const TRANSITIONS = [
  // Applicant
  ['A0', 'A1_0', 'Application submitted'],
  ['A1_0', 'A2_0', 'Requirements complete'],
  ['A1_0', 'A2_1', 'Deficiencies found'],
  ['A2_1', 'A2_0', 'Requirements completed'],
  ['A2_0', 'A2_1', 'OAS requires resubmit'],
  ['A2_0', 'A3_0', 'Exam required'],
  ['A2_0', 'A3_1', 'Exam exempted'],
  ['A2_0', 'A3_2', 'Failed initial evaluation'],
  ['A2_0', 'A4_3', 'Exam not required'],
  ['A3_0', 'A4_0', 'Exam taken'],
  ['A3_0', 'A4_1', 'Exam pending'],
  ['A3_0', 'A4_2', 'No slots / window lapsed'],
  ['A4_1', 'A4_0', 'Exam taken'],
  ['A4_1', 'A4_2', 'Window lapsed'],
  ['A4_0', 'A4_3', 'Further screening'],
  ['A3_1', 'A5_0', 'Scores within cutoff'],
  ['A3_1', 'A5_2', 'Redirected'],
  ['A3_1', 'A5_3', 'Waitlisted'],
  ['A3_1', 'A5_5', 'Outside cutoff'],
  ['A4_0', 'A5_0', 'Scores within cutoff'],
  ['A4_0', 'A5_1', 'Probationary offer'],
  ['A4_0', 'A5_2', 'Redirected'],
  ['A4_0', 'A5_3', 'Waitlisted'],
  ['A4_0', 'A5_5', 'Outside cutoff'],
  ['A4_3', 'A5_0', 'Passed further evaluation'],
  ['A4_3', 'A5_1', 'Probationary offer'],
  ['A4_3', 'A5_2', 'Redirected'],
  ['A4_3', 'A5_3', 'Waitlisted'],
  ['A4_3', 'A5_5', 'Outside cutoff'],
  ['A5_3', 'A5_0', 'Slot opened'],
  ['A5_0', 'A6_0', 'Acceptance fee paid/waived'],
  ['A5_1', 'A6_0', 'Acceptance fee paid/waived'],
  ['A5_2', 'A6_0', 'Acceptance fee paid/waived'],
  ['A5_0', 'A6_1', 'Did not pay (lapsed)'],
  ['A5_1', 'A6_1', 'Did not pay (lapsed)'],
  ['A5_2', 'A6_1', 'Did not pay (lapsed)'],
  ['A6_0', 'A7_0', 'Requirements complete'],
  ['A6_0', 'A7_1', 'Requirements pending'],
  ['A7_1', 'A7_0', 'Requirements completed'],
  ['A6_0', 'A7_2', 'Did not enroll (deferred)'],
  ['A7_1', 'A8_0', '1 year lapsed, no requirements'],
  ['A7_0', 'A8_1', 'Withdrew in admission term'],
  ['A7_1', 'A8_1', 'Withdrew in admission term'],

  // Student
  ['S1_0', 'S2_0', 'Enrolled / enlisted'],
  ['S2_0', 'S2_1', 'Registered for residency'],
  ['S2_1', 'S2_0', 'Re-enrolled'],
  ['S2_0', 'S2_2', 'Filed LOA (within max)'],
  ['S2_2', 'S1_0', 'Returnee approved'],
  ['S2_0', 'S2_3', 'LOA beyond max / >6 trimesters'],
  ['S2_3', 'S1_0', 'Returnee approved'],
  ['S2_0', 'S3_1', 'Did not enroll, no LOA'],
  ['S2_1', 'S3_1', 'Did not enroll, no LOA'],
  ['S1_0', 'S3_1', 'Did not enroll, no LOA'],
  ['S3_1', 'S1_0', 'Returnee approved'],
  ['S2_0', 'S3_2', 'Disciplinary suspension'],
  ['S3_2', 'S2_0', 'Suspension served / re-enrolled'],
  ['S2_0', 'S4_1', 'University exit (good standing)'],
  ['S2_1', 'S4_1', 'University exit (good standing)'],
  ['S2_2', 'S4_1', 'University exit (good standing)'],
  ['S2_3', 'S4_1', 'University exit (good standing)'],
  ['S3_1', 'S4_1', 'University exit (good standing)'],
  ['S3_2', 'S4_1', 'University exit (good standing)'],
  ['S2_0', 'S4_2', 'Disqualification verdict'],
  ['S3_2', 'S4_2', 'Disqualification verdict'],

  // Program
  ['P1_0', 'P1_2', 'SNAS criteria reached'],
  ['P1_2', 'P1_0', 'SNAS criteria not reached'],
  ['P1_0', 'P1_1', 'Academic standards not met'],
  ['P1_1', 'P1_0', 'Probation lifted'],
  ['P1_1', 'P1_3', 'Strict probation (IS)'],
  ['P1_3', 'P1_0', 'Criteria met - eligible'],
  ['P1_0', 'P1_4', 'Retention rules breached'],
  ['P1_1', 'P1_4', 'Retention rules breached'],
  ['P1_2', 'P1_4', 'Retention rules breached'],
  ['P1_3', 'P1_4', 'Retention / SAP failure'],
  ['P1_0', 'P2_0', 'Graduation check passed'],
  ['P2_0', 'P3_0', 'Commencement + 1 week'],
].map(([from, to, label]) => ({ from, to, label, dim: STATES[from].dim }));

// Build adjacency lookup: stateId -> [transition]
export const OUTGOING = TRANSITIONS.reduce((acc, t) => {
  (acc[t.from] = acc[t.from] || []).push(t);
  return acc;
}, {});

export const isTerminal = (id) => id && STATES[id].kind === 'terminal';
export const isHandoff = (id) => id && STATES[id].kind === 'handoff';
