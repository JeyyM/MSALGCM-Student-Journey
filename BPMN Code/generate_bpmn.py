#!/usr/bin/env python3
"""Generate granular BPMN 2.0 XML with swimlanes and role assignments."""

from __future__ import annotations
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

ROOT = Path(__file__).parent

TASK_W, TASK_H = 150, 70
EVENT_SIZE = 36
GW_SIZE = 50
GAP_X = 100
LANE_H = 130
POOL_LABEL_W = 30
ORIGIN_X = 220
ORIGIN_Y = 80

# Reusable lane sets
L_APPLICANT = {
    "applicant": "Applicant",
    "oas": "OAS / Admissions Office",
}
L_APPLICANT_REG = {
    **L_APPLICANT,
    "registrar": "University Records (Registrar)",
}
L_APPLICANT_FULL = {
    **L_APPLICANT_REG,
    "eval": "OAS / Evaluation",
}
L_STUDENT = {
    "student": "Student",
    "registrar": "Enrollment & Records",
}
L_STUDENT_ADMIN = {
    "student": "Student",
    "registrar": "Enrollment & Records",
    "disciplinary": "Disciplinary Office",
}
L_PROGRAM = {
    "program": "College / Program Office",
    "student": "Student",
}
L_COMBINED = {
    "admissions": "Admissions Office",
    "student_lane": "Student (University Standing)",
    "program_lane": "Program Office (Academic Standing)",
    "validation": "Records / Validation System",
}
L_CROSS = {
    "program_lane": "Program Office",
    "student_lane": "Student Records",
}
L_OVERVIEW = {
    "applicant": "Applicant / Prospective Student",
    "admissions": "Admissions Office",
    "student_lane": "Student Life & Enrollment",
    "program_lane": "Program / Academic Affairs",
    "outcome": "University Outcome",
}

# (fill, border) hex colors keyed by lane id
LANE_COLORS: dict[str, tuple[str, str]] = {
    "applicant": ("#DBEAFE", "#2563EB"),
    "oas": ("#D1FAE5", "#059669"),
    "admissions": ("#D1FAE5", "#059669"),
    "registrar": ("#EDE9FE", "#7C3AED"),
    "eval": ("#FFE4E6", "#E11D48"),
    "student": ("#FEF3C7", "#D97706"),
    "student_lane": ("#FEF3C7", "#D97706"),
    "disciplinary": ("#FEE2E2", "#DC2626"),
    "program": ("#CFFAFE", "#0891B2"),
    "program_lane": ("#CFFAFE", "#0891B2"),
    "validation": ("#F3F4F6", "#6B7280"),
    "outcome": ("#E5E7EB", "#374151"),
}
GATEWAY_COLOR = ("#FEF9C3", "#CA8A04")
START_COLOR = ("#DCFCE7", "#16A34A")
END_COLOR = ("#FEE2E2", "#DC2626")
LANE_BG_ALPHA = ("#FAFAFA", "#CBD5E1")  # default lane band tint

COLOR_NS = "http://www.omg.org/spec/BPMN/non-normative/color/1.0"
BIOC_NS = "http://bpmn.io/schema/bpmn/biocolor/1.0"


def prettify(elem: Element) -> str:
    return minidom.parseString(tostring(elem, encoding="unicode")).toprettyxml(indent="  ")


def n(nid: str, name: str, ntype: str = "task", lane: str = "", actor: str = "") -> dict:
    """ntype: start | end | gateway | task | user | service"""
    return {"type": ntype, "name": name, "lane": lane, "actor": actor}


def e(frm: str, to: str, label: str = "") -> dict:
    return {"from": frm, "to": to, "label": label}


def layout_in_lanes(nodes: dict, edges: list, lane_order: list[str]) -> dict[str, tuple[int, int]]:
    """Global left-to-right layers; Y band per swimlane."""
    lane_index = {lid: i for i, lid in enumerate(lane_order)}

    outgoing: dict[str, list] = {nid: [] for nid in nodes}
    incoming: dict[str, int] = {nid: 0 for nid in nodes}
    for edge in edges:
        outgoing[edge["from"]].append(edge)
        incoming[edge["to"]] += 1

    starts = [nid for nid, meta in nodes.items() if meta["type"] == "start"]
    if not starts:
        starts = [nid for nid, c in incoming.items() if c == 0]
    if not starts:
        starts = [next(iter(nodes))]

    layer: dict[str, int] = {}
    queue = [(s, 0) for s in starts]
    seen: set[str] = set()
    while queue:
        nid, depth = queue.pop(0)
        if nid in seen:
            layer[nid] = max(layer.get(nid, 0), depth)
            continue
        seen.add(nid)
        layer[nid] = depth
        for edge in outgoing.get(nid, []):
            queue.append((edge["to"], depth + 1))

    for nid in nodes:
        layer.setdefault(nid, 0)

    # Break ties within the same layer using stable node order
    by_layer: dict[int, list[str]] = {}
    for nid, d in layer.items():
        by_layer.setdefault(d, []).append(nid)
    for d in by_layer:
        by_layer[d].sort(key=lambda x: (lane_index.get(nodes[x].get("lane", ""), 0), x))

    positions: dict[str, tuple[int, int]] = {}
    for d in sorted(by_layer):
        lane_count: dict[str, int] = {}
        for nid in by_layer[d]:
            lid = nodes[nid].get("lane") or lane_order[0]
            sub = lane_count.get(lid, 0)
            lane_count[lid] = sub + 1
            li = lane_index.get(lid, 0)
            lane_y = ORIGIN_Y + li * LANE_H + (LANE_H - TASK_H) // 2
            x = ORIGIN_X + d * (TASK_W + GAP_X) + sub * (TASK_W + 30)
            positions[nid] = (x, lane_y)
    return positions


def node_bounds(nid: str, ntype: str, pos: tuple[int, int]) -> tuple[int, int, int, int]:
    x, y = pos
    if ntype in ("start", "end"):
        return x, y, EVENT_SIZE, EVENT_SIZE
    if ntype == "gateway":
        return x, y - (GW_SIZE - TASK_H) // 2, GW_SIZE, GW_SIZE
    return x, y, TASK_W, TASK_H


def task_tag(ntype: str) -> str:
    if ntype == "user":
        return "bpmn:userTask"
    if ntype == "service":
        return "bpmn:serviceTask"
    return "bpmn:task"


def node_colors(meta: dict) -> tuple[str, str]:
    ntype = meta["type"]
    if ntype == "gateway":
        return GATEWAY_COLOR
    if ntype == "start":
        return START_COLOR
    if ntype == "end":
        return END_COLOR
    lane = meta.get("lane", "")
    return LANE_COLORS.get(lane, ("#FFFFFF", "#64748B"))


def append_color_extensions(parent: Element, fill: str, stroke: str) -> None:
    """OMG non-normative color + bpmn.io biocolor on the same element."""
    ext = SubElement(parent, "bpmn:extensionElements")
    bg = SubElement(ext, "color:background-color", {"xmlns:color": COLOR_NS})
    bg.text = fill
    border = SubElement(ext, "color:border-color", {"xmlns:color": COLOR_NS})
    border.text = stroke
    SubElement(ext, "bioc:fill", {"xmlns:bioc": BIOC_NS, "color": fill})
    SubElement(ext, "bioc:stroke", {"xmlns:bioc": BIOC_NS, "color": stroke})


def build_bpmn(
    process_id: str,
    process_name: str,
    lanes: dict[str, str],
    nodes: dict,
    edges: list,
) -> str:
    lane_order = list(lanes.keys())
    positions = layout_in_lanes(nodes, edges, lane_order)

    pool_h = len(lane_order) * LANE_H + 40
    max_x = max(
        (
            node_bounds(nid, nodes[nid]["type"], positions[nid])[0]
            + node_bounds(nid, nodes[nid]["type"], positions[nid])[2]
            for nid in nodes
        ),
        default=ORIGIN_X + 400,
    )
    pool_w = max_x - ORIGIN_X + POOL_LABEL_W + 120

    defs = Element(
        "bpmn:definitions",
        {
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "xmlns:bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL",
            "xmlns:bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI",
            "xmlns:dc": "http://www.omg.org/spec/DD/20100524/DC",
            "xmlns:di": "http://www.omg.org/spec/DD/20100524/DI",
            "xmlns:color": COLOR_NS,
            "xmlns:bioc": BIOC_NS,
            "id": f"Definitions_{process_id}",
            "targetNamespace": "http://dlsu.edu.ph/student-journey",
        },
    )

    collab = SubElement(defs, "bpmn:collaboration", {"id": f"Collaboration_{process_id}"})
    participant = SubElement(
        collab,
        "bpmn:participant",
        {"id": f"Participant_{process_id}", "name": process_name, "processRef": process_id},
    )

    proc = SubElement(defs, "bpmn:process", {"id": process_id, "name": process_name, "isExecutable": "false"})
    lane_set = SubElement(proc, "bpmn:laneSet", {"id": f"LaneSet_{process_id}"})

    lane_nodes: dict[str, list[str]] = {lid: [] for lid in lane_order}
    for nid, meta in nodes.items():
        lid = meta.get("lane") or lane_order[0]
        lane_nodes.setdefault(lid, []).append(nid)

    for lid, lname in lanes.items():
        lane_el = SubElement(lane_set, "bpmn:lane", {"id": f"Lane_{lid}", "name": lname})
        for nid in lane_nodes.get(lid, []):
            SubElement(lane_el, "bpmn:flowNodeRef").text = nid

    for nid, meta in nodes.items():
        ntype = meta["type"]
        name = meta.get("name", nid)
        attrs = {"id": nid, "name": name}
        if meta.get("actor"):
            attrs["name"] = f"{name} [{meta['actor']}]"
        fill, stroke = node_colors(meta)
        if ntype == "start":
            el = SubElement(proc, "bpmn:startEvent", attrs)
        elif ntype == "end":
            el = SubElement(proc, "bpmn:endEvent", attrs)
        elif ntype == "gateway":
            el = SubElement(proc, "bpmn:exclusiveGateway", attrs)
        else:
            el = SubElement(proc, task_tag(ntype), attrs)
        append_color_extensions(el, fill, stroke)

    for i, edge in enumerate(edges):
        attrs = {"id": f"Flow_{i + 1}", "sourceRef": edge["from"], "targetRef": edge["to"]}
        if edge.get("label"):
            attrs["name"] = edge["label"]
        SubElement(proc, "bpmn:sequenceFlow", attrs)

    diagram = SubElement(defs, "bpmndi:BPMNDiagram", {"id": f"BPMNDiagram_{process_id}"})
    plane = SubElement(
        diagram,
        "bpmndi:BPMNPlane",
        {"id": f"BPMNPlane_{process_id}", "bpmnElement": f"Collaboration_{process_id}"},
    )

    pool_shape = SubElement(
        plane,
        "bpmndi:BPMNShape",
        {"id": f"Participant_{process_id}_di", "bpmnElement": f"Participant_{process_id}", "isHorizontal": "true"},
    )
    SubElement(pool_shape, "dc:Bounds", {
        "x": str(ORIGIN_X - POOL_LABEL_W), "y": str(ORIGIN_Y - 20),
        "width": str(pool_w), "height": str(pool_h),
    })

    for i, (lid, lname) in enumerate(lanes.items()):
        lane_fill, lane_stroke = LANE_COLORS.get(lid, LANE_BG_ALPHA)
        # Very light lane band — ~15% tint of lane color blended toward white
        lane_band_fill = lane_fill
        lane_shape = SubElement(
            plane,
            "bpmndi:BPMNShape",
            {"id": f"Lane_{lid}_di", "bpmnElement": f"Lane_{lid}", "isHorizontal": "true"},
        )
        SubElement(lane_shape, "dc:Bounds", {
            "x": str(ORIGIN_X), "y": str(ORIGIN_Y + i * LANE_H),
            "width": str(pool_w - POOL_LABEL_W), "height": str(LANE_H),
        })
        append_color_extensions(lane_shape, lane_band_fill, lane_stroke)

    for nid, meta in nodes.items():
        ntype = meta["type"]
        x, y, w, h = node_bounds(nid, ntype, positions[nid])
        shape = SubElement(plane, "bpmndi:BPMNShape", {"id": f"{nid}_di", "bpmnElement": nid})
        if ntype == "gateway":
            shape.set("isMarkerVisible", "true")
        SubElement(shape, "dc:Bounds", {"x": str(x), "y": str(y), "width": str(w), "height": str(h)})
        fill, stroke = node_colors(meta)
        append_color_extensions(shape, fill, stroke)

    def center(nid: str) -> tuple[int, int]:
        x, y, w, h = node_bounds(nid, nodes[nid]["type"], positions[nid])
        return x + w // 2, y + h // 2

    for i, edge in enumerate(edges):
        edge_el = SubElement(plane, "bpmndi:BPMNEdge", {"id": f"Flow_{i + 1}_di", "bpmnElement": f"Flow_{i + 1}"})
        sx, sy = center(edge["from"])
        tx, ty = center(edge["to"])
        SubElement(edge_el, "di:waypoint", {"x": str(sx), "y": str(sy)})
        if sy != ty:
            mid_x = (sx + tx) // 2
            SubElement(edge_el, "di:waypoint", {"x": str(mid_x), "y": str(sy)})
            SubElement(edge_el, "di:waypoint", {"x": str(mid_x), "y": str(ty)})
        SubElement(edge_el, "di:waypoint", {"x": str(tx), "y": str(ty)})

    return prettify(defs)


def write_bpmn(rel_path: str, process_id: str, process_name: str, lanes: dict, nodes: dict, edges: list):
    out = ROOT / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_bpmn(process_id, process_name, lanes, nodes, edges), encoding="utf-8")
    print(f"  wrote {rel_path}")


# Each diagram: (path, process_id, name, lanes, nodes, edges)
DIAGRAMS = [
    (
        "applicant_status/part_1_account_to_submission.bpmn",
        "Applicant_Part1_AccountToSubmission",
        "A — Part 1: Account to Submission",
        L_APPLICANT,
        {
            "Start": n("Start", "Account created", "start", "applicant", "Applicant"),
            "A0": n("A0", "A0 — Draft", "user", "applicant", "Applicant"),
            "A1_0": n("A1_0", "A1.0 — Submitted Form", "user", "applicant", "Applicant"),
            "GW_Req": n("GW_Req", "Requirements OK?", "gateway", "oas", "OAS"),
            "A2_0": n("A2_0", "A2.0 — Complete Requirements", "service", "oas", "OAS"),
            "A2_1": n("A2_1", "A2.1 — Deficiencies", "service", "oas", "OAS"),
            "End_Next": n("End_Next", "Continue to evaluation", "end", "oas", "OAS"),
        },
        [
            e("Start", "A0", "Account created"),
            e("A0", "A1_0", "Application submitted"),
            e("A1_0", "GW_Req"),
            e("GW_Req", "A2_0", "Complete"),
            e("GW_Req", "A2_1", "Deficiencies"),
            e("A2_1", "A2_0", "Requirements completed"),
            e("A2_0", "A2_1", "OAS requires resubmit"),
            e("A2_0", "End_Next", "Proceed"),
        ],
    ),
    (
        "applicant_status/part_2a_exam_evaluation.bpmn",
        "Applicant_Part2a_ExamEvaluation",
        "A — Part 2A: Exam & Evaluation",
        L_APPLICANT,
        {
            "Start": n("Start", "From A2.0 complete", "start", "oas", "OAS"),
            "GW_Init": n("GW_Init", "Initial evaluation", "gateway", "oas", "OAS"),
            "A3_0": n("A3_0", "A3.0 — Exam Required", "service", "oas", "OAS"),
            "A3_1": n("A3_1", "A3.1 — Exam Exempted", "service", "oas", "OAS"),
            "A3_2": n("A3_2", "A3.2 — Not Qualified", "end", "oas", "OAS"),
            "A4_3": n("A4_3", "A4.3 — Further Evaluation", "service", "oas", "OAS"),
            "GW_Exam": n("GW_Exam", "Exam outcome", "gateway", "oas", "OAS"),
            "A4_0": n("A4_0", "A4.0 — Exam Taken", "user", "applicant", "Applicant"),
            "A4_1": n("A4_1", "A4.1 — Exam Pending", "user", "applicant", "Applicant"),
            "A4_2": n("A4_2", "A4.2 — Not Qualified (no exam)", "end", "applicant", "Applicant"),
            "End_Results": n("End_Results", "To admission results", "end", "oas", "OAS"),
        },
        [
            e("Start", "GW_Init"),
            e("GW_Init", "A3_0", "Exam required"),
            e("GW_Init", "A3_1", "Exam exempted"),
            e("GW_Init", "A3_2", "Failed initial eval"),
            e("GW_Init", "A4_3", "Further screening only"),
            e("A3_0", "GW_Exam"),
            e("GW_Exam", "A4_0", "Exam taken"),
            e("GW_Exam", "A4_1", "Exam pending"),
            e("GW_Exam", "A4_2", "Exam window lapsed"),
            e("A4_1", "A4_0", "Exam taken"),
            e("A4_1", "A4_2", "Exam window lapsed"),
            e("A4_0", "A4_3", "Further screening"),
            e("A3_1", "End_Results"),
            e("A4_3", "End_Results"),
        ],
    ),
    (
        "applicant_status/part_2b_admission_results.bpmn",
        "Applicant_Part2b_AdmissionResults",
        "A — Part 2B: Admission Results",
        L_APPLICANT,
        {
            "Start": n("Start", "After evaluation", "start", "oas", "OAS"),
            "GW_Decision": n("GW_Decision", "Admission decision", "gateway", "oas", "OAS"),
            "A5_0": n("A5_0", "A5.0 — Offered", "service", "oas", "OAS"),
            "A5_1": n("A5_1", "A5.1 — Probationary", "service", "oas", "OAS"),
            "A5_2": n("A5_2", "A5.2 — Redirected", "service", "oas", "OAS"),
            "A5_3": n("A5_3", "A5.3 — Waitlisted", "service", "oas", "OAS"),
            "A5_5": n("A5_5", "A5.5 — Not Qualified", "end", "oas", "OAS"),
            "End_Accept": n("End_Accept", "Continue to acceptance", "end", "applicant", "Applicant"),
        },
        [
            e("Start", "GW_Decision"),
            e("GW_Decision", "A5_0", "Within cutoff"),
            e("GW_Decision", "A5_1", "Probationary"),
            e("GW_Decision", "A5_2", "Redirected"),
            e("GW_Decision", "A5_3", "Waitlisted"),
            e("GW_Decision", "A5_5", "Outside cutoff"),
            e("A5_3", "A5_0", "Slot opened"),
            e("A5_0", "End_Accept", "Offer received"),
            e("A5_1", "End_Accept", "Offer received"),
            e("A5_2", "End_Accept", "Offer received"),
        ],
    ),
    (
        "applicant_status/part_3_acceptance_to_student.bpmn",
        "Applicant_Part3_AcceptanceToStudent",
        "A — Part 3: Acceptance to Student",
        L_APPLICANT_REG,
        {
            "Start": n("Start", "Admission offer", "start", "applicant", "Applicant"),
            "A6_0": n("A6_0", "A6.0 — Reserved", "service", "oas", "Admissions"),
            "GW_Req": n("GW_Req", "Requirements complete?", "gateway", "oas", "Admissions"),
            "A7_0": n("A7_0", "A7.0 — Officially Admitted", "service", "oas", "Admissions"),
            "A7_1": n("A7_1", "A7.1 — Provisionally Admitted", "service", "oas", "Admissions"),
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "registrar", "Registrar"),
            "End_Student": n("End_Student", "Student status continues", "end", "registrar", "Registrar"),
        },
        [
            e("Start", "A6_0", "Acceptance fee paid/waived"),
            e("A6_0", "GW_Req"),
            e("GW_Req", "A7_0", "Complete"),
            e("GW_Req", "A7_1", "Pending"),
            e("A7_1", "A7_0", "Requirements completed"),
            e("A7_0", "S1_0", "Becomes student"),
            e("A7_1", "S1_0", "Becomes student (provisional)"),
            e("S1_0", "End_Student"),
        ],
    ),
    (
        "applicant_status/part_4_terminal_or_exception_states.bpmn",
        "Applicant_Part4_TerminalExceptions",
        "A — Part 4: Terminal & Exception States",
        L_APPLICANT_FULL,
        {
            "A6_0": n("A6_0", "A6.0 — Reserved", "service", "oas", "Admissions"),
            "A7_0": n("A7_0", "A7.0 — Officially Admitted", "service", "oas", "Admissions"),
            "A7_1": n("A7_1", "A7.1 — Provisionally Admitted", "service", "oas", "Admissions"),
            "A6_1": n("A6_1", "A6.1 — Cancelled (non-payment)", "end", "oas", "Admissions"),
            "A7_2": n("A7_2", "A7.2 — Deferred", "service", "applicant", "Applicant"),
            "A8_0": n("A8_0", "A8.0 — Cancelled (no reqs)", "end", "oas", "Admissions"),
            "A8_1": n("A8_1", "A8.1 — Cancelled (withdrawal)", "end", "applicant", "Applicant"),
            "A3_2": n("A3_2", "A3.2 — Not Qualified (initial)", "end", "eval", "OAS Eval"),
            "A4_2": n("A4_2", "A4.2 — Not Qualified (no exam)", "end", "eval", "OAS Eval"),
            "A5_5": n("A5_5", "A5.5 — Not Qualified", "end", "eval", "OAS Eval"),
        },
        [
            e("A6_0", "A6_1", "Did not pay fee"),
            e("A6_0", "A7_2", "Did not enroll"),
            e("A7_1", "A8_0", "1 year lapsed"),
            e("A7_0", "A8_1", "Withdrew"),
            e("A7_1", "A8_1", "Withdrew"),
        ],
    ),
    (
        "student_status/part_1_active_and_enrollment.bpmn",
        "Student_Part1_ActiveEnrollment",
        "S — Part 1: Active & Enrollment",
        L_STUDENT,
        {
            "Start": n("Start", "Officially admitted (A7.x)", "start", "registrar", "Registrar"),
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "registrar", "Registrar"),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "registrar", "Registrar"),
            "End_Next": n("End_Next", "Continues in Parts 2–4", "end", "registrar", "Registrar"),
        },
        [
            e("Start", "S1_0"),
            e("S1_0", "S2_0", "Enrolled / enlisted"),
            e("S2_0", "End_Next"),
        ],
    ),
    (
        "student_status/part_2_residency_and_loa.bpmn",
        "Student_Part2_ResidencyLOA",
        "S — Part 2: Residency & LOA",
        L_STUDENT,
        {
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "registrar", "Registrar"),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "registrar", "Registrar"),
            "S2_1": n("S2_1", "S2.1 — Residency", "user", "student", "Student"),
            "S2_2": n("S2_2", "S2.2 — Under LOA", "service", "registrar", "Registrar"),
            "S2_3": n("S2_3", "S2.3 — Prolonged Leave", "service", "registrar", "Registrar"),
        },
        [
            e("S1_0", "S2_0", "Enrolled / enlisted"),
            e("S2_0", "S2_1", "Registered for residency"),
            e("S2_1", "S2_0", "Re-enrolled"),
            e("S2_0", "S2_2", "LOA approved"),
            e("S2_0", "S2_3", "LOA period exceeded"),
            e("S2_2", "S1_0", "Returnee approved"),
            e("S2_3", "S1_0", "Returnee approved"),
        ],
    ),
    (
        "student_status/part_3_awol_suspension_and_exit.bpmn",
        "Student_Part3_AWOLSuspensionExit",
        "S — Part 3: AWOL, Suspension & Exit",
        L_STUDENT_ADMIN,
        {
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "registrar", "Registrar"),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "registrar", "Registrar"),
            "S3_1": n("S3_1", "S3.1 — AWOL", "service", "registrar", "Registrar"),
            "S3_2": n("S3_2", "S3.2 — Suspended", "service", "disciplinary", "Disciplinary"),
            "S4_1": n("S4_1", "S4.1 — Exited (good standing)", "end", "student", "Student"),
            "S4_2": n("S4_2", "S4.2 — Disqualified", "end", "disciplinary", "Disciplinary"),
        },
        [
            e("S2_0", "S3_1", "Did not enroll, no LOA"),
            e("S3_1", "S1_0", "Returnee approved"),
            e("S2_0", "S3_2", "Disciplinary suspension"),
            e("S3_2", "S2_0", "Suspension served"),
            e("S2_0", "S4_1", "University exit"),
            e("S3_1", "S4_1", "University exit"),
            e("S2_0", "S4_2", "Disqualification"),
            e("S3_2", "S4_2", "Disqualification"),
        ],
    ),
    (
        "student_status/part_4_graduation_and_terminal_states.bpmn",
        "Student_Part4_GraduationTerminal",
        "S — Part 4: Graduation & Terminal",
        L_STUDENT_ADMIN,
        {
            "S2_0": n("S2_0", "S2.0 — Active", "service", "registrar", "Registrar"),
            "S4_0": n("S4_0", "S4.0 — Graduated", "end", "registrar", "Registrar"),
            "S4_1": n("S4_1", "S4.1 — Exited (good standing)", "end", "student", "Student"),
            "S4_2": n("S4_2", "S4.2 — Disqualified", "end", "disciplinary", "Disciplinary"),
        },
        [
            e("S2_0", "S4_0", "All programs graduated"),
            e("S2_0", "S4_1", "University exit"),
            e("S2_0", "S4_2", "Disqualification"),
        ],
    ),
    (
        "student_program_status/part_1_good_standing_and_probation.bpmn",
        "Program_Part1_GoodStandingProbation",
        "P — Part 1: Good Standing & Probation",
        L_PROGRAM,
        {
            "Start_N": n("Start_N", "Normal admission", "start", "program", "Program Office"),
            "Start_P": n("Start_P", "Probationary offer", "start", "program", "Program Office"),
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program", "Program Office"),
            "P1_1": n("P1_1", "P1.1 — Probationary", "service", "program", "Program Office"),
            "End_Next": n("End_Next", "Continues in Parts 2–3", "end", "program", "Program Office"),
        },
        [
            e("Start_N", "P1_0"),
            e("Start_P", "P1_1"),
            e("P1_0", "P1_1", "Standards not met"),
            e("P1_1", "P1_0", "Probation lifted"),
            e("P1_0", "End_Next"),
        ],
    ),
    (
        "student_program_status/part_2_snas_sap_and_ineligible.bpmn",
        "Program_Part2_SNASSAPIneligible",
        "P — Part 2: SNAS, SAP & Ineligible",
        L_PROGRAM,
        {
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program", "Program Office"),
            "P1_1": n("P1_1", "P1.1 — Probationary", "service", "program", "Program Office"),
            "P1_2": n("P1_2", "P1.2 — SNAS", "service", "program", "Program Office"),
            "P1_3": n("P1_3", "P1.3 — Strict Probation (IS)", "service", "program", "Program Office"),
            "P1_4": n("P1_4", "P1.4 — Ineligible", "end", "program", "Program Office"),
        },
        [
            e("P1_0", "P1_2", "SNAS criteria reached"),
            e("P1_2", "P1_0", "SNAS criteria not reached"),
            e("P1_1", "P1_3", "Strict probation (IS)"),
            e("P1_3", "P1_0", "Criteria met"),
            e("P1_0", "P1_4", "Retention breached"),
            e("P1_1", "P1_4", "Retention breached"),
            e("P1_2", "P1_4", "Retention breached"),
            e("P1_3", "P1_4", "SAP failure"),
        ],
    ),
    (
        "student_program_status/part_3_graduation_and_terminal_states.bpmn",
        "Program_Part3_GraduationTerminal",
        "P — Part 3: Graduation & Terminal",
        L_PROGRAM,
        {
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program", "Program Office"),
            "P2_0": n("P2_0", "P2.0 — Candidate for Graduation", "service", "program", "Program Office"),
            "P3_0": n("P3_0", "P3.0 — Graduated", "end", "program", "Program Office"),
            "P3_1": n("P3_1", "P3.1 — Incomplete", "end", "student", "Student"),
        },
        [
            e("P1_0", "P2_0", "Graduation check passed"),
            e("P2_0", "P3_0", "Commencement + 1 week"),
            e("P1_0", "P3_1", "University exit"),
            e("P2_0", "P3_1", "University exit"),
        ],
    ),
    (
        "combined_lifecycle/high_level_lifecycle_overview.bpmn",
        "Combined_HighLevelOverview",
        "Combined — High-Level Lifecycle Overview",
        L_OVERVIEW,
        {
            "Start": n("Start", "Start", "start", "applicant", "Applicant"),
            "APPLICANT": n("APPLICANT", "Applicant phase (A0–A5.x)", "user", "applicant", "Applicant"),
            "ACCEPTED": n("ACCEPTED", "Accepted (A6.0–A7.x)", "service", "admissions", "Admissions"),
            "ACTIVE": n("ACTIVE", "Active Student (S1.0–S2.x)", "service", "student_lane", "Enrollment"),
            "PROGRAM": n("PROGRAM", "Program Standing (P1.0–P2.0)", "service", "program_lane", "Program Office"),
            "DISRUPT": n("DISRUPT", "LOA / AWOL / Suspended", "service", "student_lane", "Enrollment"),
            "OUTCOME": n("OUTCOME", "Graduation / Exit / Terminal", "service", "outcome", "University"),
            "End": n("End", "Terminal", "end", "outcome", "University"),
        },
        [
            e("Start", "APPLICANT"),
            e("APPLICANT", "ACCEPTED", "Admitted / reserved"),
            e("APPLICANT", "OUTCOME", "Rejected / cancelled"),
            e("ACCEPTED", "ACTIVE", "Becomes student"),
            e("ACTIVE", "DISRUPT", "Leave / discipline"),
            e("DISRUPT", "ACTIVE", "Returnee re-enrolls"),
            e("ACTIVE", "OUTCOME", "Graduate or exit"),
            e("ACTIVE", "PROGRAM", "Academic standing"),
            e("PROGRAM", "OUTCOME", "All programs graduated"),
            e("OUTCOME", "End"),
        ],
    ),
    (
        "combined_lifecycle/applicant_to_student_bridge.bpmn",
        "Combined_ApplicantToStudentBridge",
        "Combined — Applicant to Student Bridge",
        L_COMBINED,
        {
            "A7_0": n("A7_0", "A7.0 — Officially Admitted", "service", "admissions", "Admissions"),
            "A7_1": n("A7_1", "A7.1 — Provisionally Admitted", "service", "admissions", "Admissions"),
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "student_lane", "Registrar"),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "student_lane", "Registrar"),
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program_lane", "Program Office"),
            "P1_1": n("P1_1", "P1.1 — Probationary", "service", "program_lane", "Program Office"),
        },
        [
            e("A7_0", "S1_0", "Becomes student"),
            e("A7_1", "S1_0", "Becomes student (provisional)"),
            e("S1_0", "S2_0", "Enrolled / enlisted"),
            e("S1_0", "P1_0", "Normal admission"),
            e("S1_0", "P1_1", "Probationary offer"),
        ],
    ),
    (
        "combined_lifecycle/student_status_vs_program_status_interaction.bpmn",
        "Combined_StudentProgramInteraction",
        "Combined — Student vs Program Interaction",
        L_CROSS,
        {
            "PALL": n("PALL", "All programs → P3.0 Graduated", "service", "program_lane", "Program Office"),
            "SGRAD": n("SGRAD", "Student → S4.0 Graduated", "service", "student_lane", "Registrar"),
            "SEXIT": n("SEXIT", "Student exit, program active", "user", "student_lane", "Student"),
            "PINC": n("PINC", "Program → P3.1 Incomplete", "service", "program_lane", "Program Office"),
            "PINE": n("PINE", "P1.4 Ineligible + shift pending", "service", "program_lane", "Program Office"),
            "SAWE": n("SAWE", "Student → S1.0 Without Enrollment", "service", "student_lane", "Registrar"),
            "SACT": n("SACT", "Student → S2.0 Active", "service", "student_lane", "Registrar"),
        },
        [
            e("PALL", "SGRAD", "forces"),
            e("SEXIT", "PINC", "forces"),
            e("PINE", "SAWE", "forces"),
            e("SAWE", "SACT", "shift approved"),
        ],
    ),
    (
        "combined_lifecycle/cross_impact_rules.bpmn",
        "Combined_CrossImpactRules",
        "Combined — Cross-Impact Rules (COMBO-T001–T005)",
        L_CROSS,
        {
            "T001_Trig": n("T001_Trig", "All programs → P3.0 Graduated", "service", "program_lane", "Program Office"),
            "T001_Eff": n("T001_Eff", "COMBO-T001: Student → S4.0", "service", "student_lane", "Registrar"),
            "T003_Trig": n("T003_Trig", "Student exit, program active", "user", "student_lane", "Student"),
            "T003_Eff": n("T003_Eff", "COMBO-T003: Program → P3.1", "service", "program_lane", "Program Office"),
            "T004_Trig": n("T004_Trig", "P1.4 Ineligible + shift pending", "service", "program_lane", "Program Office"),
            "T004_Eff": n("T004_Eff", "COMBO-T004: Student → S1.0", "service", "student_lane", "Registrar"),
            "T005_Eff": n("T005_Eff", "COMBO-T005: Shift approved → S2.0", "service", "student_lane", "Registrar"),
        },
        [
            e("T001_Trig", "T001_Eff", "forces"),
            e("T003_Trig", "T003_Eff", "forces"),
            e("T004_Trig", "T004_Eff", "forces"),
            e("T004_Eff", "T005_Eff", "shift approved"),
        ],
    ),
    (
        "combined_lifecycle/parallel_student_program_constrained_fsm.bpmn",
        "Combined_ParallelStudentProgramFSM",
        "Combined — Parallel Student × Program FSM",
        L_COMBINED,
        {
            "Start": n("Start", "Admitted from A7.x", "start", "admissions", "Admissions"),
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "student_lane", "Registrar"),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "student_lane", "Registrar"),
            "S2_2": n("S2_2", "S2.2 — Under LOA", "service", "student_lane", "Registrar"),
            "S3_1": n("S3_1", "S3.1 — AWOL", "service", "student_lane", "Registrar"),
            "S4_0": n("S4_0", "S4.0 — Graduated", "end", "student_lane", "Registrar"),
            "S4_1": n("S4_1", "S4.1 — Exited", "end", "student_lane", "Registrar"),
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program_lane", "Program Office"),
            "P1_1": n("P1_1", "P1.1 — Probationary", "service", "program_lane", "Program Office"),
            "P1_2": n("P1_2", "P1.2 — SNAS", "service", "program_lane", "Program Office"),
            "P1_4": n("P1_4", "P1.4 — Ineligible", "service", "program_lane", "Program Office"),
            "P2_0": n("P2_0", "P2.0 — Candidacy", "service", "program_lane", "Program Office"),
            "P3_0": n("P3_0", "P3.0 — Graduated", "end", "program_lane", "Program Office"),
            "P3_1": n("P3_1", "P3.1 — Incomplete", "end", "program_lane", "Program Office"),
            "VALID": n("VALID", "V(S,P) validation layer", "service", "validation", "Records System"),
        },
        [
            e("Start", "S1_0"),
            e("S1_0", "S2_0", "enrolled"),
            e("S2_0", "S2_2", "LOA approved"),
            e("S2_0", "S3_1", "no enroll, no LOA"),
            e("S2_2", "S1_0", "returnee"),
            e("S3_1", "S1_0", "returnee"),
            e("S2_0", "S4_1", "exit"),
            e("P1_0", "P1_2", "SNAS"),
            e("P1_2", "P1_0", "cleared"),
            e("P1_1", "P1_0", "met requirements"),
            e("P1_0", "P1_4", "retention breach"),
            e("P1_0", "P2_0", "grad check"),
            e("P2_0", "P3_0", "commencement"),
            e("S2_0", "VALID"),
            e("P1_0", "VALID"),
            e("S1_0", "P1_0", "initial pairing"),
            e("S1_0", "P1_1", "probationary offer"),
            e("P3_0", "S4_0", "COMBO-T001"),
            e("S4_1", "P3_1", "COMBO-T003"),
            e("P1_4", "S1_0", "COMBO-T004"),
            e("S1_0", "S2_0", "COMBO-T005"),
        ],
    ),
]


def main():
    print("Generating BPMN files with swimlanes...")
    for rel, pid, pname, lanes, nodes, edges in DIAGRAMS:
        write_bpmn(rel, pid, pname, lanes, nodes, edges)
    print(f"Done — {len(DIAGRAMS)} diagrams in {ROOT}")


if __name__ == "__main__":
    main()
