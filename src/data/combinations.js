// Combination validation: given (Student, Program) pair codes, is it legal?
// Full Post-M3 matrix in combinationMatrix.js (corrections.txt Phase 2).

import { STATES } from './lifecycle.js';
import { COMBINATION_MATRIX } from './combinationMatrix.js';

export function validateCombination(studentId, programId) {
  if (!studentId || !programId) {
    return { status: 'na', reason: 'Not yet a student — combination not applicable.' };
  }
  const s = STATES[studentId];
  const p = STATES[programId];
  if (!s || !p) {
    return { status: 'na', reason: 'Unknown status code.' };
  }

  const key = `${s.code}|${p.code}`;
  const row = COMBINATION_MATRIX[key];
  if (row) {
    if (row.allow === 'yes') {
      return { status: 'valid', reason: row.reason };
    }
    if (row.reason.includes('Yes?"') || row.reason.includes('"Yes?"')) {
      return { status: 'uncertain', reason: row.reason };
    }
    if (row.reason.includes('pending stakeholder')) {
      return { status: 'uncertain', reason: row.reason };
    }
    return { status: 'invalid', reason: row.reason };
  }

  return { status: 'valid', reason: 'Independent dimensions — combination allowed (default).' };
}

export const VALIDITY_META = {
  valid: { label: 'Valid pairing', color: '#10b981' },
  invalid: { label: 'Invalid pairing', color: '#ef4444' },
  uncertain: { label: 'Needs confirmation', color: '#f59e0b' },
  na: { label: 'Not applicable', color: '#64748b' },
};
