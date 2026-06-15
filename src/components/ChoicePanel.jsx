import { STATES, DIMENSIONS } from '../data/lifecycle.js';

const GROUP_ORDER = ['A', 'S', 'P', 'X'];

export default function ChoicePanel({ actions, onChoose, current }) {
  const inApplicant = !!current.applicant;
  const reachedEnd = !inApplicant && current.student && STATES[current.student].kind === 'terminal';

  const grouped = GROUP_ORDER.map((dim) => ({
    dim,
    items: actions.filter((a) => a.dim === dim),
  })).filter((g) => g.items.length > 0);

  return (
    <section className="panel choice-panel">
      <header className="panel__header">
        <h2>Choose the next event</h2>
        <span className="panel__hint">Only valid transitions from the current status are shown</span>
      </header>

      {actions.length === 0 && (
        <p className="choice-empty">
          {reachedEnd
            ? 'This is a terminal outcome — the journey has ended. Undo or reset to explore another path.'
            : 'No further transitions available from here.'}
        </p>
      )}

      {grouped.map((group) => {
        const dim = DIMENSIONS[group.dim];
        return (
          <div key={group.dim} className="choice-group">
            <h3 className="choice-group__title" style={{ color: dim.color }}>
              <span className="choice-group__chip" style={{ background: dim.color }} />
              {dim.label} {group.dim === 'X' ? 'events' : 'transitions'}
            </h3>
            <div className="choice-grid">
              {group.items.map((action) => {
                const target = action.to ? STATES[action.to] : null;
                return (
                  <button
                    key={action.id}
                    className="choice"
                    style={{ '--dim-color': dim.color }}
                    onClick={() => onChoose(action)}
                  >
                    <span className="choice__label">{action.label}</span>
                    {target && (
                      <span className="choice__target">
                        → {target.code} {target.label}
                      </span>
                    )}
                  </button>
                );
              })}
            </div>
          </div>
        );
      })}
    </section>
  );
}
