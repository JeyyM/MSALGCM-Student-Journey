import { useLifecycleMachine } from './hooks/useLifecycleMachine.js';
import PhaseStepper from './components/PhaseStepper.jsx';
import StatusPanel from './components/StatusPanel.jsx';
import ChoicePanel from './components/ChoicePanel.jsx';
import HistoryTrail from './components/HistoryTrail.jsx';

export default function App() {
  const machine = useLifecycleMachine();

  return (
    <div className="app">
      <header className="app__bar">
        <div className="app__title">
          <h1>Student Lifecycle Validator</h1>
          <p>Walk the applicant → student → program status model to validate it against real cases.</p>
        </div>
        <div className="app__controls">
          <button className="ctrl" onClick={machine.undo} disabled={!machine.canUndo} title="Undo last action">
            ↶ Undo
          </button>
          <button className="ctrl" onClick={machine.redo} disabled={!machine.canRedo} title="Redo">
            ↷ Redo
          </button>
          <button className="ctrl ctrl--danger" onClick={machine.reset} title="Restart from A0 Draft">
            ⟲ Reset
          </button>
        </div>
      </header>

      <PhaseStepper activeSections={machine.activeSections} />

      <main className="app__grid">
        <div className="app__left">
          <StatusPanel current={machine.current} />
          <ChoicePanel actions={machine.actions} onChoose={machine.apply} current={machine.current} />
        </div>
        <aside className="app__right">
          <HistoryTrail history={machine.history} index={machine.index} jumpTo={machine.jumpTo} />
        </aside>
      </main>

      <footer className="app__foot">
        <span className="legend"><i style={{ background: '#6366f1' }} /> Applicant</span>
        <span className="legend"><i style={{ background: '#0ea5e9' }} /> Student status</span>
        <span className="legend"><i style={{ background: '#10b981' }} /> Program status</span>
        <span className="legend"><i style={{ background: '#f59e0b' }} /> Cross-impact</span>
        <span className="legend legend--note">Codes follow the canonical Post-M3 WIP scheme.</span>
      </footer>
    </div>
  );
}
