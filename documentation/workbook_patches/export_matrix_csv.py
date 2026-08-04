#!/usr/bin/env python3
"""Export combinationMatrix.js to CSV for Excel import."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
js = (ROOT / "src/data/combinationMatrix.js").read_text(encoding="utf-8")
pattern = re.compile(
    r"'([^']+)\|([^']+)': \{ allow: '([^']+)', reason: '((?:\\'|[^'])*)' \}"
)
rows = [(m.group(1), m.group(2), m.group(3).upper(), m.group(4).replace("\\'", "'")) for m in pattern.finditer(js)]
out = ROOT / "documentation/workbook_patches/combination_matrix_post_m3.csv"
out.parent.mkdir(parents=True, exist_ok=True)
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["StudentCode", "ProgramCode", "Allowed", "ScenarioReason"])
    w.writerows(rows)
print(f"Wrote {len(rows)} rows to {out}")
