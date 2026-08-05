# MSALGCM — Student Lifecycle Status Model

BPMN + DMN deliverables and an interactive validator for the DLSU applicant / student / program status lifecycle (Post-M3 WIP workbook).

## Repository layout

| Folder / file | Contents |
|---|---|
| **`BPMN and DMN Files/`** | **Submission diagrams** — 17 BPMN process models + 18 DMN decision tables (folders 1–4) |
| **`src/`** | React app — Student Lifecycle Validator (deployed to Vercel) |
| **`final mermaid code/`** | Source `.mmd` diagrams for draw.io + plain-language flow report |
| **`CSC615M Student_Applicant Journey Matrix …xlsx`** | Original Student Journey Matrix workbook |

### BPMN and DMN Files structure

| Folder | BPMN | DMN |
|---|---|---|
| `1. applicant_status/` | 5 | 5 |
| `2. student_status/` | 4 | 4 |
| `3. student_program_status/` | 3 | 3 |
| `4. combined_lifecycle/` | 5 | 6 |

Open `.bpmn` and `.dmn` files in [BPMN.io](https://bpmn.io), Camunda Modeler, or Signavio.

## Student Lifecycle Validator (web app)

Interactive **choose-your-own-adventure** tool for staff to walk the status model and validate it against real cases.

- Start at **A0 Draft** and click only the events valid from the current status
- **Always-visible** applicant / student / program status panel with department badges
- **Combination validity** badge for parallel `(S, P)` pairings
- **4-section stepper**: Application → Student → Program → Outcome
- **Undo**, **Redo**, **Reset**, and clickable **journey trail**

### Run locally

```bash
npm install
npm run dev
```

Open http://localhost:5173

### Deploy (Vercel)

Connect this repo to Vercel — no root directory override needed. Vercel detects Vite and uses:

- **Build:** `npm run build`
- **Output:** `dist`

### App data sources

- `src/data/lifecycle.js` — states and transitions (A / S / P + COMBO)
- `src/data/combinations.js` — validation matrix logic
- `src/data/combinationMatrix.js` — Post-M3 10×8 combination matrix

## Further reading

See [`final mermaid code/README.md`](final%20mermaid%20code/README.md) for a plain-language report of how the four lifecycle sections connect.
