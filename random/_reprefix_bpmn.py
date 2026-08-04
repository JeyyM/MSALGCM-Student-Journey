#!/usr/bin/env python3
"""Restore bpmn: prefixed XML format required by Miragon BPMN Modeler."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parent
DIRS = [
    "1. applicant_status",
    "2. student_status",
    "3. student_program_status",
    "4. combined_lifecycle",
]

BPMN_TAGS = (
    "collaboration",
    "participant",
    "process",
    "laneSet",
    "lane",
    "flowNodeRef",
    "sequenceFlow",
    "serviceTask",
    "userTask",
    "task",
    "manualTask",
    "scriptTask",
    "sendTask",
    "receiveTask",
    "businessRuleTask",
    "startEvent",
    "endEvent",
    "exclusiveGateway",
    "parallelGateway",
    "inclusiveGateway",
    "extensionElements",
    "incoming",
    "outgoing",
    "documentation",
)


def reprefix(content: str) -> str:
    if "<bpmn:definitions" in content:
        return content

    content = content.replace(
        "<?xml version='1.0' encoding='UTF-8'?>",
        '<?xml version="1.0" encoding="UTF-8"?>',
    )

    content = re.sub(
        r"<definitions\s+xmlns=\"http://www\.omg\.org/spec/BPMN/20100524/MODEL\"",
        '<bpmn:definitions xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
        'xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"',
        content,
        count=1,
    )

    for tag in BPMN_TAGS:
        content = re.sub(rf"<({tag})([\s/>])", rf"<bpmn:\1\2", content)
        content = re.sub(rf"</({tag})>", rf"</bpmn:\1>", content)

    content = content.replace("</definitions>", "</bpmn:definitions>")
    return content


def main() -> None:
    for d in DIRS:
        for path in sorted((ROOT / d).glob("*.bpmn")):
            original = path.read_text(encoding="utf-8")
            fixed = reprefix(original)
            if fixed != original:
                path.write_text(fixed, encoding="utf-8")
                print(f"fixed {path.relative_to(ROOT)}")
    print("done")


if __name__ == "__main__":
    main()
