import { useLifecycleMachine } from './hooks/useLifecycleMachine.js';
import { DEPARTMENTS, DEPARTMENT_LEGEND } from './data/departments.js';
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
        {DEPARTMENT_LEGEND.map((id) => {
          const d = DEPARTMENTS[id];
          return (
            <span className="legend" key={id}>
              <i style={{ background: d.color }} /> {d.label}
            </span>
          );
        })}
        <span className="legend legend--note">Post-M3 codes · combination matrix validates S×P pairs</span>
      </footer>
    </div>
  );
}
