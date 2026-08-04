import { useReducer, useMemo, useCallback } from 'react';
import { STATES, OUTGOING, isTerminal, isHandoff } from '../data/lifecycle.js';

const INITIAL_SNAPSHOT = { applicant: 'A0', student: null, program: null, via: 'Start' };

function reducer(state, action) {
  switch (action.type) {
    case 'APPLY': {
      const current = state.history[state.index];
      const next = {
        ...current,
        ...action.changes,
        via: action.label,
        _action: action.meta,
      };
      const history = state.history.slice(0, state.index + 1).concat(next);
      return { history, index: history.length - 1 };
    }
    case 'UNDO':
      return { ...state, index: Math.max(0, state.index - 1) };
    case 'REDO':
      return { ...state, index: Math.min(state.history.length - 1, state.index + 1) };
    case 'JUMP':
      return { ...state, index: Math.max(0, Math.min(state.history.length - 1, action.index)) };
    case 'RESET':
      return { history: [INITIAL_SNAPSHOT], index: 0 };
    default:
      return state;
  }
}

// Compute the list of choose-your-own-adventure actions available from a snapshot.
function computeActions(current, pastSnapshots) {
  const actions = [];
  const { applicant, student, program } = current;

  // ----- Applicant phase -----
  if (applicant) {
    if (isHandoff(applicant)) {
      // Detect a probationary offer earlier in the path -> initial program standing.
      const wasProbationary = pastSnapshots.some((s) => s.applicant === 'A5_1');
      actions.push({
        id: 'handoff',
        dim: 'X',
        label: `Registrar: officially admitted → S1.0${wasProbationary ? ' + P1.1 Probationary' : ' + P1.0 Eligible'}`,
        changes: { applicant: null, student: 'S1_0', program: wasProbationary ? 'P1_1' : 'P1_0' },
      });
    }
    if (!isTerminal(applicant)) {
      (OUTGOING[applicant] || []).forEach((t) => {
        actions.push({
          id: `A:${t.from}->${t.to}`,
          dim: 'A',
          label: t.label,
          to: t.to,
          changes: { applicant: t.to },
        });
      });
    }
    return actions;
  }

  // ----- Student + Program phases (parallel) -----
  if (student && !isTerminal(student)) {
    (OUTGOING[student] || []).forEach((t) => {
      actions.push({
        id: `S:${t.from}->${t.to}`,
        dim: 'S',
        label: t.label,
        to: t.to,
        changes: { student: t.to },
      });
    });
  }
  if (program && !isTerminal(program)) {
    (OUTGOING[program] || []).forEach((t) => {
      actions.push({
        id: `P:${t.from}->${t.to}`,
        dim: 'P',
        label: t.label,
        to: t.to,
        changes: { program: t.to },
      });
    });
  }

  // ----- Cross-impact (COMBO) actions -----
  const studentActive = student && !isTerminal(student);
  if (program === 'P3_0' && studentActive && student !== 'S4_0') {
    actions.push({
      id: 'X:T001',
      dim: 'X',
      label: 'COMBO-T001 · All programs graduated → Student Graduated (S4.0)',
      changes: { student: 'S4_0' },
    });
  }
  if (studentActive && program && ['P1_0', 'P1_1', 'P1_2', 'P1_3', 'P2_0'].includes(program)) {
    actions.push({
      id: 'X:T003',
      dim: 'X',
      label: 'COMBO-T003 · University exit → Exited (S4.1) + Program Incomplete (P3.1)',
      changes: { student: 'S4_1', program: 'P3_1' },
    });
  }
  if (program === 'P1_4' && studentActive && student !== 'S1_0') {
    actions.push({
      id: 'X:T004',
      dim: 'X',
      label: 'COMBO-T004 · Ineligible + shift pending → Without Enrollment (S1.0)',
      changes: { student: 'S1_0' },
    });
  }
  if (program === 'P1_4' && student === 'S1_0') {
    actions.push({
      id: 'X:T005',
      dim: 'X',
      label: 'COMBO-T005 · Shift approved → Active (S2.0) + new program Eligible (P1.0)',
      changes: { student: 'S2_0', program: 'P1_0' },
    });
  }

  return actions;
}

export function useLifecycleMachine() {
  const [state, dispatch] = useReducer(reducer, { history: [INITIAL_SNAPSHOT], index: 0 });
  const current = state.history[state.index];

  const pastSnapshots = useMemo(
    () => state.history.slice(0, state.index + 1),
    [state.history, state.index]
  );

  const actions = useMemo(
    () => computeActions(current, pastSnapshots),
    [current, pastSnapshots]
  );

  const apply = useCallback(
    (action) =>
      dispatch({
        type: 'APPLY',
        changes: action.changes,
        label: action.label,
        meta: { id: action.id, dim: action.dim, to: action.to ?? null },
      }),
    []
  );
  const undo = useCallback(() => dispatch({ type: 'UNDO' }), []);
  const redo = useCallback(() => dispatch({ type: 'REDO' }), []);
  const reset = useCallback(() => dispatch({ type: 'RESET' }), []);
  const jumpTo = useCallback((index) => dispatch({ type: 'JUMP', index }), []);

  // Determine which of the 4 sections is/are currently active.
  let activeSections;
  if (current.applicant) {
    activeSections = ['applicant'];
  } else if (current.student && isTerminal(current.student)) {
    activeSections = ['outcome'];
  } else {
    activeSections = ['student', 'program'];
  }

  return {
    current,
    actions,
    history: state.history,
    index: state.index,
    canUndo: state.index > 0,
    canRedo: state.index < state.history.length - 1,
    activeSections,
    apply,
    undo,
    redo,
    reset,
    jumpTo,
  };
}
