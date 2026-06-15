# MSALGCM — Student Lifecycle Status Model

Documentation and an interactive validator for the DLSU applicant / student / program status lifecycle (Post-M3 WIP workbook).

## Repository layout

| Folder | Contents |
|---|---|
| **`src/`** | React app — Student Lifecycle Validator (deployed to Vercel) |
| **`documentation/`** | Full analysis, flow docs, diagram planning, Mermaid markdown |
| **`final mermaid code/`** | Copy-paste `.mmd` diagrams for draw.io + layman flow report |

## Student Lifecycle Validator (web app)

Interactive **choose-your-own-adventure** tool for staff to walk the status model and validate it against real cases.

- Start at **A0 Draft** and click only the events valid from the current status
- **Always-visible** applicant / student / program status panel
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

Canonical docs: `documentation/` and `final mermaid code/`.

## Documentation

See [`documentation/README.md`](documentation/README.md) for the full workbook analysis, status tables, combination rules, and diagram index.

See [`final mermaid code/README.md`](final%20mermaid%20code/README.md) for a plain-language report of how the four lifecycle sections connect.
