import { STATES, DIMENSIONS } from '../data/lifecycle.js';

function snapshotLabel(snap) {
  if (snap.applicant) {
    const s = STATES[snap.applicant];
    return { dim: 'A', text: `${s.code} ${s.label}` };
  }
  const st = snap.student ? STATES[snap.student] : null;
  const pr = snap.program ? STATES[snap.program] : null;
  return {
    dim: 'S',
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
          const { dim, text } = snapshotLabel(snap);
          const isCurrent = i === index;
          const isFuture = i > index;
          return (
            <li key={i} className={`trail__item ${isCurrent ? 'trail__item--current' : ''} ${isFuture ? 'trail__item--future' : ''}`}>
              <button className="trail__btn" onClick={() => jumpTo(i)} style={{ '--dim-color': DIMENSIONS[dim].color }}>
                <span className="trail__via">{snap.via}</span>
                <span className="trail__state">{text}</span>
              </button>
            </li>
          );
        })}
      </ol>
    </section>
  );
}
