// Combination validation layer: given a (Student, Program) pair, is it legal?
// Derived from documentation/status_combination_rules.md, mapped to canonical codes.
// Returns { status: 'valid' | 'invalid' | 'uncertain', reason }.
// NOTE: the source combination tab uses a legacy code scheme; mappings flagged
// 'uncertain' are where the workbook itself defers (the "Yes?" cells) or where
// legacy/canonical reconciliation is still open.

import { STATES } from './lifecycle.js';

// Explicit overrides keyed by `${studentCode}|${programCode}` (dotted codes).
const RULES = {
  // Graduated student must pair with a graduated program.
  'S4.0|P3.0': { status: 'valid', reason: 'Graduated student with a graduated program — the consistent end pair.' },

  // Exited students: program should be Incomplete (exit converts active standing).
  'S4.1|P3.1': { status: 'valid', reason: 'Exited (good standing); active program standing converts to Incomplete.' },
  'S4.2|P3.1': { status: 'valid', reason: 'Exited (disqualification); program standing converts to Incomplete.' },

  // Without-enrollment blocks.
  'S1.0|P1.2': { status: 'invalid', reason: 'A without-enrollment student cannot be SNAS.' },
  'S1.0|P2.0': { status: 'invalid', reason: 'Cannot be a graduation candidate before enrolling.' },
  'S1.0|P3.0': { status: 'invalid', reason: 'A without-enrollment student cannot have a graduated program.' },
  'S1.0|P3.1': { status: 'invalid', reason: 'A without-enrollment student should not have an Incomplete program.' },

  // Active student vs graduated program.
  'S2.0|P3.0': { status: 'invalid', reason: 'A graduated program should drive the student to Graduated (S4.0).' },

  // LOA + Ineligible explicitly disallowed.
  'S2.2|P1.4': { status: 'invalid', reason: 'Ineligible program standing is not allowed while on LOA.' },

  // Deferred / uncertain "Yes?" cells in the workbook.
  'S2.1|P1.1': { status: 'uncertain', reason: 'Residency × Probationary is flagged "Yes?" (needs confirmation).' },
  'S2.1|P1.2': { status: 'uncertain', reason: 'Residency × SNAS is flagged "Yes?" (needs confirmation).' },
  'S2.1|P1.4': { status: 'uncertain', reason: 'Residency × Ineligible is flagged "Yes?" (needs confirmation).' },
  'S2.2|P1.2': { status: 'uncertain', reason: 'LOA × SNAS is flagged "Yes?" (needs confirmation).' },
  'S2.2|P2.0': { status: 'uncertain', reason: 'LOA × Candidate for Graduation is flagged "Yes?" (needs confirmation).' },
  'S3.2|P2.0': { status: 'uncertain', reason: 'Suspended × Candidate for Graduation is flagged "Yes?" (needs confirmation).' },
};

export function validateCombination(studentId, programId) {
  if (!studentId || !programId) {
    return { status: 'na', reason: 'Not yet a student — combination not applicable.' };
  }
  const s = STATES[studentId];
  const p = STATES[programId];
  const key = `${s.code}|${p.code}`;
  if (RULES[key]) return RULES[key];

  // General rules when no explicit override exists.
  // Graduated student must have graduated program.
  if (s.code === 'S4.0' && p.code !== 'P3.0') {
    return { status: 'invalid', reason: 'A graduated student must have a graduated program (P3.0).' };
  }
  // Exited students should pair with Incomplete (or Graduated if they finished first).
  if ((s.code === 'S4.1' || s.code === 'S4.2')) {
    if (p.code === 'P3.0') return { status: 'uncertain', reason: 'Exited after graduating — verify ordering.' };
    if (p.code !== 'P3.1') return { status: 'invalid', reason: 'An exited student should have an Incomplete program (P3.1).' };
  }
  // Graduated program but student not graduated/exited.
  if (p.code === 'P3.0' && !['S4.0', 'S4.1', 'S4.2'].includes(s.code)) {
    return { status: 'invalid', reason: 'A graduated program should move the student to Graduated/Exited.' };
  }
  // Incomplete program but student still active.
  if (p.code === 'P3.1' && ['S1.0', 'S2.0', 'S2.1'].includes(s.code)) {
    return { status: 'invalid', reason: 'An Incomplete program implies the student has exited.' };
  }

  // Default: the two dimensions are independent and the pair is allowed.
  return { status: 'valid', reason: 'Independent dimensions — combination allowed.' };
}

export const VALIDITY_META = {
  valid: { label: 'Valid pairing', color: '#10b981' },
  invalid: { label: 'Invalid pairing', color: '#ef4444' },
  uncertain: { label: 'Needs confirmation', color: '#f59e0b' },
  na: { label: 'Not applicable', color: '#64748b' },
};
