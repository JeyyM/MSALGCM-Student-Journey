// Post-M3 canonical (S × P) combination matrix — 10 student × 8 program = 80 cells.
// Regenerated from legacy combo tab with code migration (corrections.txt #1–#4, #28).
// Authority: Post-M3 WIP tabs + decisions.md Rule 2 (former "Yes?" → No until confirmed).
// See documentation/status_combination_rules.md and documentation/executive_defaults.md.

/** @typedef {'yes'|'no'} Allow */

/** @type {Record<string, { allow: Allow, reason: string }>} */
export const COMBINATION_MATRIX = {
  // ── S1.0 Without Enrollment ──
  'S1.0|P1.0': { allow: 'yes', reason: 'Admitted/returnee; eligible program standing before enrollment.' },
  'S1.0|P1.1': { allow: 'yes', reason: 'Probationary admission offer (A5.1) before first enrollment.' },
  'S1.0|P1.2': { allow: 'no', reason: 'SNAS requires enrolled academic activity.' },
  'S1.0|P1.3': { allow: 'no', reason: 'Strict Probationary (IS SAP) follows enrollment and prior P1.1.' },
  'S1.0|P1.4': { allow: 'yes', reason: 'Ineligible on program; shift pending → S1.0 (COMBO-T004).' },
  'S1.0|P2.0': { allow: 'no', reason: 'Cannot be a graduation candidate before enrolling.' },
  'S1.0|P3.0': { allow: 'no', reason: 'Without enrollment cannot have a graduated program.' },
  'S1.0|P3.1': { allow: 'no', reason: 'Without enrollment should not have an incomplete program.' },

  // ── S2.0 Active ──
  'S2.0|P1.0': { allow: 'yes', reason: 'Normal enrolled student in good standing.' },
  'S2.0|P1.1': { allow: 'yes', reason: 'Active with academic warning.' },
  'S2.0|P1.2': { allow: 'yes', reason: 'Active with SNAS standing.' },
  'S2.0|P1.3': { allow: 'yes', reason: 'Active IS student on Strict Probationary (SAP).' },
  'S2.0|P1.4': { allow: 'yes', reason: 'Allowed when another program is not Ineligible (multi-program).' },
  'S2.0|P2.0': { allow: 'yes', reason: 'Active graduation candidate.' },
  'S2.0|P3.0': { allow: 'no', reason: 'Graduated program should drive student to S4.0 (COMBO-T001).' },
  'S2.0|P3.1': { allow: 'no', reason: 'Incomplete program implies exit, not active enrollment.' },

  // ── S2.1 Residency ──
  'S2.1|P1.0': { allow: 'yes', reason: 'Residency student in good program standing.' },
  'S2.1|P1.1': { allow: 'no', reason: 'Legacy "Yes?" — treated as No per decisions.md Rule 2.' },
  'S2.1|P1.2': { allow: 'no', reason: 'Legacy "Yes?" — treated as No per decisions.md Rule 2.' },
  'S2.1|P1.3': { allow: 'no', reason: 'Legacy "Yes?" (Ineligible) — No; Strict Probationary unlikely during residency.' },
  'S2.1|P1.4': { allow: 'no', reason: 'Legacy "Yes?" — treated as No per decisions.md Rule 2.' },
  'S2.1|P2.0': { allow: 'no', reason: 'Residency activity excludes candidacy for graduation.' },
  'S2.1|P3.0': { allow: 'no', reason: 'Graduated program incompatible with active residency.' },
  'S2.1|P3.1': { allow: 'no', reason: 'Incomplete program incompatible with active residency.' },

  // ── S2.2 Under LOA ──
  'S2.2|P1.0': { allow: 'yes', reason: 'LOA retains prior eligible standing.' },
  'S2.2|P1.1': { allow: 'yes', reason: 'Legacy combo Yes; Notes #3 tentative No — kept Yes pending stakeholder (#5).' },
  'S2.2|P1.2': { allow: 'no', reason: 'Legacy "Yes?" — treated as No per decisions.md Rule 2.' },
  'S2.2|P1.3': { allow: 'no', reason: 'Strict Probationary requires active IS enrollment track.' },
  'S2.2|P1.4': { allow: 'no', reason: 'Ineligible not allowed while on LOA.' },
  'S2.2|P2.0': { allow: 'no', reason: 'Legacy "Yes?" — treated as No per decisions.md Rule 2.' },
  'S2.2|P3.0': { allow: 'no', reason: 'Graduated program incompatible with LOA.' },
  'S2.2|P3.1': { allow: 'no', reason: 'Incomplete program incompatible with LOA.' },

  // ── S2.3 Prolonged Leave (new — inferred from AWOL pattern, #15) ──
  'S2.3|P1.0': { allow: 'yes', reason: 'Prolonged leave retains last eligible standing (inferred).' },
  'S2.3|P1.1': { allow: 'yes', reason: 'Retains probationary standing while inactive (inferred).' },
  'S2.3|P1.2': { allow: 'yes', reason: 'Retains SNAS standing while inactive (inferred).' },
  'S2.3|P1.3': { allow: 'no', reason: 'Strict Probationary requires active IS enrollment (inferred).' },
  'S2.3|P1.4': { allow: 'yes', reason: 'Ineligible may persist while on prolonged leave.' },
  'S2.3|P2.0': { allow: 'no', reason: 'Cannot be graduation candidate while on prolonged leave.' },
  'S2.3|P3.0': { allow: 'no', reason: 'Graduated program incompatible with prolonged leave.' },
  'S2.3|P3.1': { allow: 'no', reason: 'Incomplete implies exit, not prolonged leave alone.' },

  // ── S3.1 AWOL ──
  'S3.1|P1.0': { allow: 'yes', reason: 'AWOL retains last eligible standing.' },
  'S3.1|P1.1': { allow: 'yes', reason: 'AWOL retains probationary standing.' },
  'S3.1|P1.2': { allow: 'yes', reason: 'AWOL retains SNAS standing.' },
  'S3.1|P1.3': { allow: 'yes', reason: 'AWOL retains Strict Probationary standing.' },
  'S3.1|P1.4': { allow: 'yes', reason: 'AWOL may coexist with Ineligible (legacy P1.3→P1.4).' },
  'S3.1|P2.0': { allow: 'no', reason: 'AWOL cannot be graduation candidate.' },
  'S3.1|P3.0': { allow: 'no', reason: 'Graduated program should drive S4.0, not AWOL.' },
  'S3.1|P3.1': { allow: 'no', reason: 'Incomplete implies exit path, not AWOL alone.' },

  // ── S3.2 Suspended ──
  'S3.2|P1.0': { allow: 'yes', reason: 'Suspension retains eligible standing.' },
  'S3.2|P1.1': { allow: 'yes', reason: 'Suspension retains probationary standing.' },
  'S3.2|P1.2': { allow: 'yes', reason: 'Suspension retains SNAS standing.' },
  'S3.2|P1.3': { allow: 'yes', reason: 'Suspension retains Strict Probationary standing.' },
  'S3.2|P1.4': { allow: 'yes', reason: 'Suspension may coexist with Ineligible.' },
  'S3.2|P2.0': { allow: 'no', reason: 'Legacy "Yes?" — treated as No per decisions.md Rule 2.' },
  'S3.2|P3.0': { allow: 'no', reason: 'Graduated program should drive S4.0.' },
  'S3.2|P3.1': { allow: 'no', reason: 'Incomplete implies exit, not suspension alone.' },

  // ── S4.0 Graduated (was legacy S3.0) ──
  'S4.0|P1.0': { allow: 'no', reason: 'Graduated student cannot have active academic standings.' },
  'S4.0|P1.1': { allow: 'no', reason: 'Graduated student cannot be probationary.' },
  'S4.0|P1.2': { allow: 'no', reason: 'Graduated student cannot be SNAS.' },
  'S4.0|P1.3': { allow: 'no', reason: 'Graduated student cannot be Strict Probationary.' },
  'S4.0|P1.4': { allow: 'no', reason: 'Graduated student cannot be Ineligible.' },
  'S4.0|P2.0': { allow: 'no', reason: 'Graduated student cannot be candidacy.' },
  'S4.0|P3.0': { allow: 'yes', reason: 'Primary graduated pair (COMBO-T001).' },
  'S4.0|P3.1': { allow: 'no', reason: 'Graduated student should not have incomplete program.' },

  // ── S4.1 Exited Good Standing (was legacy S3.2 Exited) ──
  'S4.1|P1.0': { allow: 'no', reason: 'Exit converts active standing to Incomplete (COMBO-T003).' },
  'S4.1|P1.1': { allow: 'no', reason: 'Exit converts probationary to Incomplete.' },
  'S4.1|P1.2': { allow: 'no', reason: 'Exit converts SNAS to Incomplete.' },
  'S4.1|P1.3': { allow: 'no', reason: 'Exit converts Strict Probationary to Incomplete.' },
  'S4.1|P1.4': { allow: 'yes', reason: 'Exit after Ineligible (legacy Yes).' },
  'S4.1|P2.0': { allow: 'yes', reason: 'Exit after candidacy (legacy Yes; low likelihood).' },
  'S4.1|P3.0': { allow: 'no', reason: 'If program Graduated, student should be S4.0.' },
  'S4.1|P3.1': { allow: 'yes', reason: 'Exit with incomplete program (COMBO-T003).' },

  // ── S4.2 Permanent Disqualification (was legacy S3.4–S3.7) ──
  'S4.2|P1.0': { allow: 'no', reason: 'Terminal exit — only Incomplete program allowed.' },
  'S4.2|P1.1': { allow: 'no', reason: 'Terminal exit — only Incomplete program allowed.' },
  'S4.2|P1.2': { allow: 'no', reason: 'Terminal exit — only Incomplete program allowed.' },
  'S4.2|P1.3': { allow: 'no', reason: 'Terminal exit — only Incomplete program allowed.' },
  'S4.2|P1.4': { allow: 'no', reason: 'Terminal exit — only Incomplete program allowed.' },
  'S4.2|P2.0': { allow: 'no', reason: 'Terminal exit — only Incomplete program allowed.' },
  'S4.2|P3.0': { allow: 'no', reason: 'Terminal exit — only Incomplete program allowed.' },
  'S4.2|P3.1': { allow: 'yes', reason: 'Only valid pairing for permanent disqualification exit.' },
};

export const STUDENT_CODES = ['S1.0', 'S2.0', 'S2.1', 'S2.2', 'S2.3', 'S3.1', 'S3.2', 'S4.0', 'S4.1', 'S4.2'];
export const PROGRAM_CODES = ['P1.0', 'P1.1', 'P1.2', 'P1.3', 'P1.4', 'P2.0', 'P3.0', 'P3.1'];

/** Legacy combo-tab code map for workbook migration */
export const LEGACY_CODE_MAP = {
  student: {
    'S3.0 Inactive - Graduated': 'S4.0 Graduated',
    'S3.2 Inactive - Exited': 'S4.1 Exited on Good Standing',
    'S3.3 Inactive - Suspended': 'S3.2 Inactive - Suspended',
    'S3.4 Inactive - Under Non-readmission': 'S4.2 Exited - Permanent Disqualification',
    'S3.5 Inactive - Under Exclusion': 'S4.2 Exited - Permanent Disqualification',
    'S3.6 Inactive - Expelled': 'S4.2 Exited - Permanent Disqualification',
    'S3.7 Inactive - Transferred': 'S4.2 Exited - Permanent Disqualification',
  },
  program: {
    'P1.3 Ineligible (legacy combo)': 'P1.4 Ineligible',
    'P1.3 Strict Probationary (new)': 'P1.3 Strict Probationary (IS only)',
  },
};
