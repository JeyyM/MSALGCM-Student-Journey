// Department / swimlane ownership — BPMN lane colors where split; Admissions uses distinct indigo in UI ([Admissions] tag vs [OAS]).

export const DEPARTMENTS = {
  applicant: {
    id: 'applicant',
    label: 'Applicant',
    short: 'Applicant',
    color: '#2563EB',
    bg: '#DBEAFE',
  },
  oas: {
    id: 'oas',
    label: 'OAS / Admissions Office',
    short: 'OAS',
    color: '#059669',
    bg: '#D1FAE5',
  },
  admissions: {
    id: 'admissions',
    label: 'Admissions Office',
    short: 'Admissions',
    color: '#4F46E5',
    bg: '#E0E7FF',
  },
  registrar: {
    id: 'registrar',
    label: 'Enrollment & Records (Registrar)',
    short: 'Registrar',
    color: '#7C3AED',
    bg: '#EDE9FE',
  },
  student: {
    id: 'student',
    label: 'Student',
    short: 'Student',
    color: '#D97706',
    bg: '#FEF3C7',
  },
  program: {
    id: 'program',
    label: 'College / Program Office',
    short: 'Program Office',
    color: '#0891B2',
    bg: '#CFFAFE',
  },
  disciplinary: {
    id: 'disciplinary',
    label: 'Disciplinary Office',
    short: 'Disciplinary',
    color: '#DC2626',
    bg: '#FEE2E2',
  },
  validation: {
    id: 'validation',
    label: 'Records / Validation System',
    short: 'Validation',
    color: '#6B7280',
    bg: '#F3F4F6',
  },
};

/** Primary owning department per status code (matches BPMN task [Tag] labels). */
export const STATE_DEPARTMENTS = {
  // Applicant — human-initiated
  A0: 'applicant',
  A1_0: 'applicant',
  A4_0: 'applicant',
  A4_1: 'applicant',
  A7_2: 'applicant',
  A8_1: 'applicant',

  // Applicant — OAS evaluation & offers
  A2_0: 'oas',
  A2_1: 'oas',
  A3_0: 'oas',
  A3_1: 'oas',
  A3_2: 'oas',
  A4_2: 'oas',
  A4_3: 'oas',
  A5_0: 'oas',
  A5_1: 'oas',
  A5_2: 'oas',
  A5_3: 'oas',
  A5_5: 'oas',

  // Admissions — acceptance & admission outcomes
  A6_0: 'admissions',
  A6_1: 'admissions',
  A7_0: 'admissions',
  A7_1: 'admissions',
  A8_0: 'admissions',

  // Student standing — registrar
  S1_0: 'registrar',
  S2_0: 'registrar',
  S2_2: 'registrar',
  S2_3: 'registrar',
  S3_1: 'registrar',
  S4_0: 'registrar',

  // Student — student-initiated
  S2_1: 'student',
  S4_1: 'student',

  // Disciplinary
  S3_2: 'disciplinary',
  S4_2: 'disciplinary',

  // Program standing
  P1_0: 'program',
  P1_1: 'program',
  P1_2: 'program',
  P1_3: 'program',
  P1_4: 'program',
  P2_0: 'program',
  P3_0: 'program',
  P3_1: 'student',
};

const CROSS_IMPACT_DEPTS = {
  handoff: 'registrar',
  'X:T001': 'registrar',
  'X:T003': 'student',
  'X:T004': 'program',
  'X:T005': 'registrar',
};

export function getDepartment(deptId) {
  return DEPARTMENTS[deptId] || DEPARTMENTS.validation;
}

export function getStateDepartment(stateId) {
  if (!stateId) return DEPARTMENTS.validation;
  return getDepartment(STATE_DEPARTMENTS[stateId] || 'validation');
}

export function getActionDepartment(action) {
  if (!action) return DEPARTMENTS.validation;
  if (action.dim === 'X') {
    return getDepartment(CROSS_IMPACT_DEPTS[action.id] || 'validation');
  }
  if (action.to) return getStateDepartment(action.to);
  return DEPARTMENTS.validation;
}

/** Infer who owned the transition between two snapshots (fallback when _action is missing). */
export function getTransitionDepartment(prev, next) {
  if (next._action) return getActionDepartment(next._action);

  if (next.applicant) {
    if (!prev || prev.applicant !== next.applicant) return getStateDepartment(next.applicant);
    return getStateDepartment(next.applicant);
  }

  if (prev?.applicant && !next.applicant) return getDepartment('registrar');

  const programChanged = prev?.program !== next.program;
  const studentChanged = prev?.student !== next.student;

  if (programChanged && !studentChanged) return getStateDepartment(next.program);
  if (studentChanged && !programChanged) return getStateDepartment(next.student);
  if (programChanged) return getStateDepartment(next.program);
  if (studentChanged) return getStateDepartment(next.student);

  return DEPARTMENTS.validation;
}

/** Legend order for footer */
export const DEPARTMENT_LEGEND = [
  'applicant',
  'oas',
  'admissions',
  'registrar',
  'student',
  'program',
  'disciplinary',
  'validation',
];
