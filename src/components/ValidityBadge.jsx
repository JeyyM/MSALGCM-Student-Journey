import { VALIDITY_META } from '../data/combinations.js';

export default function ValidityBadge({ result }) {
  if (!result || result.status === 'na') return null;
  const meta = VALIDITY_META[result.status];
  return (
    <div className={`validity validity--${result.status}`}>
      <span className="validity__dot" style={{ background: meta.color }} />
      <div className="validity__text">
        <strong>{meta.label}</strong>
        <span>{result.reason}</span>
      </div>
    </div>
  );
}
