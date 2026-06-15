import { SECTIONS } from '../data/lifecycle.js';

export default function PhaseStepper({ activeSections }) {
  return (
    <ol className="stepper" aria-label="Lifecycle sections">
      {SECTIONS.map((section, i) => {
        const isActive = activeSections.includes(section.id);
        const activeIdx = SECTIONS.findIndex((s) => activeSections.includes(s.id));
        const isDone = i < activeIdx;
        return (
          <li
            key={section.id}
            className={`step ${isActive ? 'step--active' : ''} ${isDone ? 'step--done' : ''}`}
          >
            <span className="step__index">{isDone ? '✓' : i + 1}</span>
            <span className="step__label">{section.label}</span>
          </li>
        );
      })}
    </ol>
  );
}
