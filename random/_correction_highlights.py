#!/usr/bin/env python3
"""Strip all BPMN shape colors; apply light blue only to correction-changed elements.

Uses text edits on BPMNShape lines — does NOT rewrite via ElementTree (that drops bpmn: prefixes).

  python _correction_highlights.py          # apply CORRECTION_HIGHLIGHTS
  python _correction_highlights.py --reset  # strip all shape colors, no highlights
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).parent
FILL = "#DBEAFE"
STROKE = "#2563EB"

DIRS = [
    "1. applicant_status",
    "2. student_status",
    "3. student_program_status",
    "4. combined_lifecycle",
]

CORRECTION_HIGHLIGHTS: dict[str, set[str]] = {
    "1. applicant_status/part_2b_admission_results.bpmn": {"A5_1"},
    "2. student_status/part_4_graduation_and_terminal_states.bpmn": {"S4_0"},
    "4. combined_lifecycle/3. parallel_student_program_constrained_fsm.bpmn": {"P1_3"},
}

DEFAULT_HIGHLIGHTS = CORRECTION_HIGHLIGHTS

COLOR_ATTR_RE = re.compile(
    r'\s*(?:bioc:(?:fill|stroke)|color:(?:background-color|border-color))="[^"]*"'
)


def strip_shape_colors(text: str) -> str:
    def clean_shape_line(line: str) -> str:
        if "BPMNShape" not in line:
            return line
        cleaned = COLOR_ATTR_RE.sub("", line)
        return cleaned.replace("  >", ">").replace(' >', ">")

    return "\n".join(clean_shape_line(line) for line in text.splitlines())


def highlight_shapes(text: str, ids: set[str]) -> str:
    if not ids:
        return text

    out: list[str] = []
    for line in text.splitlines():
        if "BPMNShape" not in line:
            out.append(line)
            continue
        m = re.search(r'bpmnElement="([^"]+)"', line)
        if not m or m.group(1) not in ids:
            out.append(line)
            continue
        line = COLOR_ATTR_RE.sub("", line)
        if line.rstrip().endswith("/>"):
            base = line.rstrip()[:-2].rstrip()
            out.append(
                f'{base} bioc:fill="{FILL}" bioc:stroke="{STROKE}" '
                f'color:background-color="{FILL}" color:border-color="{STROKE}"/>'
            )
        elif line.rstrip().endswith(">"):
            base = line.rstrip()[:-1].rstrip()
            out.append(
                f'{base} bioc:fill="{FILL}" bioc:stroke="{STROKE}" '
                f'color:background-color="{FILL}" color:border-color="{STROKE}">'
            )
        else:
            out.append(line)
    return "\n".join(out)


def ensure_color_ns(text: str) -> str:
    if "xmlns:color=" in text and "xmlns:bioc=" in text:
        return text
    insert = (
        ' xmlns:color="http://www.omg.org/spec/BPMN/non-normative/color/1.0"'
        ' xmlns:bioc="http://bpmn.io/schema/bpmn/biocolor/1.0"'
    )
    if "<bpmn:definitions" in text:
        return text.replace("<bpmn:definitions", "<bpmn:definitions" + insert, 1)
    return text.replace("<definitions", "<definitions" + insert, 1)


def process_file(path: Path, highlights: dict[str, set[str]]) -> tuple[int, int]:
    rel = path.relative_to(ROOT).as_posix()
    highlight = highlights.get(rel, set())
    text = path.read_text(encoding="utf-8")
    text = ensure_color_ns(text)
    text = strip_shape_colors(text)
    text = highlight_shapes(text, highlight)
    path.write_text(text + ("\n" if not text.endswith("\n") else ""), encoding="utf-8")
    stripped = len(re.findall(r"BPMNShape", text))
    colored = len(highlight)
    return stripped, colored


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply or reset BPMN correction highlight colors.")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Remove all shape colors; do not apply correction highlights.",
    )
    args = parser.parse_args()
    highlights: dict[str, set[str]] = {} if args.reset else DEFAULT_HIGHLIGHTS

    total = 0
    for d in DIRS:
        for path in sorted((ROOT / d).glob("*.bpmn")):
            stripped, colored = process_file(path, highlights)
            rel = path.relative_to(ROOT)
            mark = f" ({colored} highlighted)" if colored else ""
            print(f"{rel}: {stripped} shapes{mark}")
            total += colored
    if args.reset:
        print("\nDone. All shape colors reset to default.")
    else:
        print(f"\nDone. {total} correction highlights applied.")


if __name__ == "__main__":
    main()
