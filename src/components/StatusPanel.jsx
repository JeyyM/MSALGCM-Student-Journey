import { STATES, DIMENSIONS } from '../data/lifecycle.js';
import { getStateDepartment } from '../data/departments.js';
import { validateCombination } from '../data/combinations.js';
import ValidityBadge from './ValidityBadge.jsx';
import DepartmentBadge from './DepartmentBadge.jsx';

function StatusCard({ stateId, dimKey, muted }) {
  const dim = DIMENSIONS[dimKey];
  if (!stateId) {
    return (
      <div className="status-card status-card--empty">
        <span className="status-card__dim">{dim.label}</span>
        <span className="status-card__placeholder">Not reached yet</span>
      </div>
    );
  }
  const s = STATES[stateId];
  const dept = getStateDepartment(stateId);
  return (
    <div
      className={`status-card ${muted ? 'status-card--muted' : ''} ${s.kind === 'terminal' ? 'status-card--terminal' : ''}`}
      style={{ '--dept-color': dept.color, '--dept-bg': dept.bg }}
    >
      <div className="status-card__meta">
        <span className="status-card__dim">{dim.label}</span>
        <div className="status-card__badges">
          {s.kind === 'terminal' && <span className="status-card__tag">Terminal</span>}
          {s.kind === 'handoff' && <span className="status-card__tag status-card__tag--handoff">Hand-off</span>}
          <DepartmentBadge dept={dept} size="sm" />
        </div>
      </div>
      <span className="status-card__code">{s.code}</span>
      <span className="status-card__name">{s.label}</span>
      <span className="status-card__desc">{s.desc}</span>
    </div>
  );
}

export default function StatusPanel({ current }) {
  const inApplicant = !!current.applicant;
  const combo = validateCombination(current.student, current.program);

  return (
    <section className="panel status-panel">
      <header className="panel__header">
        <h2>Current status</h2>
      </header>

      {inApplicant ? (
        <StatusCard stateId={current.applicant} dimKey="A" />
      ) : (
        <>
          <div className="status-pair">
            <StatusCard stateId={current.student} dimKey="S" />
            <span className="status-pair__amp">running in parallel</span>
            <StatusCard stateId={current.program} dimKey="P" />
          </div>
          <ValidityBadge result={combo} />
        </>
      )}
    </section>
  );
}
