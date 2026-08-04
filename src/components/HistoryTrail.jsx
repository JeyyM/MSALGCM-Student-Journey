import { STATES } from '../data/lifecycle.js';
import { DEPARTMENTS, getTransitionDepartment } from '../data/departments.js';
import DepartmentBadge from './DepartmentBadge.jsx';

function snapshotLabel(snap) {
  if (snap.applicant) {
    const s = STATES[snap.applicant];
    return { text: `${s.code} ${s.label}` };
  }
  const st = snap.student ? STATES[snap.student] : null;
  const pr = snap.program ? STATES[snap.program] : null;
  return {
    text: `${st ? st.code : '—'} / ${pr ? pr.code : '—'}`,
  };
}

export default function HistoryTrail({ history, index, jumpTo }) {
  return (
    <section className="panel history-panel">
      <header className="panel__header">
        <h2>Journey trail</h2>
        <span className="panel__hint">Click any step to backtrack to it</span>
      </header>
      <ol className="trail">
        {history.map((snap, i) => {
          const { text } = snapshotLabel(snap);
          const isCurrent = i === index;
          const isFuture = i > index;
          const dept = i > 0 ? getTransitionDepartment(history[i - 1], snap) : DEPARTMENTS.validation;
          const showBadge = i > 0;
          return (
            <li
              key={i}
              className={`trail__item ${isCurrent ? 'trail__item--current' : ''} ${isFuture ? 'trail__item--future' : ''}`}
            >
              <button
                className="trail__btn"
                onClick={() => jumpTo(i)}
                style={{ '--dept-color': dept.color, '--dept-bg': dept.bg }}
              >
                <span className="trail__head">
                  <span className="trail__via">{snap.via}</span>
                  {showBadge && <DepartmentBadge dept={dept} size="xs" />}
                </span>
                <span className="trail__state">{text}</span>
              </button>
            </li>
          );
        })}
      </ol>
    </section>
  );
}
