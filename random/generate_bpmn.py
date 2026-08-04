#!/usr/bin/env python3
"""Generate granular BPMN 2.0 XML with swimlanes and role assignments."""

from __future__ import annotations

import argparse
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

ROOT = Path(__file__).parent
PROTECTED_LIST = ROOT / "protected_bpmn.txt"

TASK_W, TASK_H = 150, 70
EVENT_SIZE = 36
GW_SIZE = 50
GAP_X = 100
LANE_H = 130
POOL_LABEL_W = 30
ORIGIN_X = 220
ORIGIN_Y = 80

DEFAULT_LAYOUT = {
    "lane_h": LANE_H,
    "gap_x": GAP_X,
    "row_step": 55,
    "lane_pad": 40,
    "pool_pad_x": 120,
    "pool_pad_y": 40,
}

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
L_APPLICANT_EXCEPTIONS = {
    **L_APPLICANT,
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


def n(
    nid: str,
    name: str,
    ntype: str = "task",
    lane: str = "",
    actor: str = "",
    layer: int | None = None,
    row: int = 0,
) -> dict:
    """ntype: start | end | gateway | task | user | service; row = vertical band within lane."""
    meta: dict = {"type": ntype, "name": name, "lane": lane, "actor": actor, "row": row}
    if layer is not None:
        meta["layer"] = layer
    return meta


def e(frm: str, to: str, label: str = "") -> dict:
    return {"from": frm, "to": to, "label": label}


def compute_lane_heights(nodes: dict, lane_order: list[str], layout: dict) -> dict[str, int]:
    """Expand lane height when row-offset branches need more vertical room."""
    min_h = layout["lane_h"]
    row_step = layout["row_step"]
    lane_pad = layout["lane_pad"]
    heights: dict[str, int] = {}
    for lid in lane_order:
        rows = [nodes[n].get("row", 0) for n, m in nodes.items() if m.get("lane") == lid]
        if not rows:
            heights[lid] = min_h
            continue
        span = (max(rows) - min(rows)) * row_step + TASK_H + lane_pad
        heights[lid] = max(min_h, span)
    return heights


def layout_in_lanes(
    nodes: dict,
    edges: list,
    lane_order: list[str],
    layout: dict | None = None,
) -> dict[str, tuple[int, int]]:
    """Global left-to-right layers; Y band per swimlane."""
    opts = {**DEFAULT_LAYOUT, **(layout or {})}
    lane_h_default = opts["lane_h"]
    gap_x = opts["gap_x"]
    row_step = opts["row_step"]
    lane_heights = compute_lane_heights(nodes, lane_order, opts)
    lane_index = {lid: i for i, lid in enumerate(lane_order)}
    lane_y0: dict[str, int] = {}
    y_cursor = ORIGIN_Y
    for lid in lane_order:
        lane_y0[lid] = y_cursor
        y_cursor += lane_heights[lid]

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

    for nid, meta in nodes.items():
        if meta.get("layer") is not None:
            layer[nid] = meta["layer"]
        else:
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
            meta = nodes[nid]
            lid = meta.get("lane") or lane_order[0]
            row = meta.get("row", 0)
            if row == 0:
                sub = lane_count.get(lid, 0)
                lane_count[lid] = sub + 1
            else:
                sub = 0
            lh = lane_heights.get(lid, lane_h_default)
            lane_y = lane_y0[lid] + (lh - TASK_H) // 2 + row * row_step
            x = ORIGIN_X + d * (TASK_W + gap_x) + sub * (TASK_W + 30)
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


def shape_center(nid: str, nodes: dict, positions: dict) -> tuple[float, float]:
    x, y, w, h = node_bounds(nid, nodes[nid]["type"], positions[nid])
    return x + w / 2, y + h / 2


def border_point(nid: str, toward_id: str, nodes: dict, positions: dict) -> tuple[int, int]:
    """Point on the border of nid facing toward toward_id."""
    cx, cy = shape_center(nid, nodes, positions)
    tx, ty = shape_center(toward_id, nodes, positions)
    x, y, w, h = node_bounds(nid, nodes[nid]["type"], positions[nid])
    ntype = nodes[nid]["type"]
    dx, dy = tx - cx, ty - cy
    if abs(dx) < 0.01 and abs(dy) < 0.01:
        return int(cx), int(cy)
    if ntype == "gateway":
        hw, hh = w / 2, h / 2
        scale = hw / abs(dx) if abs(dx) * hh >= abs(dy) * hw else hh / abs(dy)
        return int(round(cx + dx * scale)), int(round(cy + dy * scale))
    hw, hh = w / 2, h / 2
    if abs(dx) * hh > abs(dy) * hw:
        px = cx + (hw if dx > 0 else -hw)
        py = cy + dy * (hw / abs(dx))
        py = max(cy - hh, min(cy + hh, py))
    else:
        py = cy + (hh if dy > 0 else -hh)
        px = cx + dx * (hh / abs(dy))
        px = max(cx - hw, min(cx + hw, px))
    return int(round(px)), int(round(py))


def route_edge(from_id: str, to_id: str, nodes: dict, positions: dict) -> list[tuple[int, int]]:
    """Orthogonal waypoints from border to border."""
    sx, sy = border_point(from_id, to_id, nodes, positions)
    tx, ty = border_point(to_id, from_id, nodes, positions)
    fcx, fcy = shape_center(from_id, nodes, positions)
    tcx, tcy = shape_center(to_id, nodes, positions)
    same_lane = nodes[from_id].get("lane") == nodes[to_id].get("lane")
    backward = tcx < fcx - 15
    points: list[tuple[int, int]] = [(sx, sy)]

    if same_lane:
        if backward:
            _, fy, _, fh = node_bounds(from_id, nodes[from_id]["type"], positions[from_id])
            _, ty0, _, th = node_bounds(to_id, nodes[to_id]["type"], positions[to_id])
            by = int(max(fy + fh, ty0 + th) + 40)
            points.extend([(sx, by), (tx, by), (tx, ty)])
        elif abs(fcy - tcy) < 10:
            points.append((tx, ty))
        else:
            mid_x = int((sx + tx) / 2)
            points.extend([(mid_x, sy), (mid_x, ty), (tx, ty)])
    elif not same_lane:
        if backward:
            top_y = int(min(sy, ty) - 45)
            points.extend([(sx, top_y), (tx, top_y), (tx, ty)])
        else:
            mid_y = int((sy + ty) / 2)
            points.extend([(sx, mid_y), (tx, mid_y), (tx, ty)])
    else:
        mid_x = int((sx + tx) / 2)
        points.extend([(mid_x, sy), (mid_x, ty), (tx, ty)])
    return points


def append_color_extensions(parent: Element, fill: str, stroke: str) -> None:
    """OMG non-normative color + bpmn.io biocolor on the same element."""
    ext = SubElement(parent, "bpmn:extensionElements")
    bg = SubElement(ext, "color:background-color", {"xmlns:color": COLOR_NS})
    bg.text = fill
    border = SubElement(ext, "color:border-color", {"xmlns:color": COLOR_NS})
    border.text = stroke
    SubElement(ext, "bioc:fill", {"xmlns:bioc": BIOC_NS, "color": fill})
    SubElement(ext, "bioc:stroke", {"xmlns:bioc": BIOC_NS, "color": stroke})


def sanitize_lucid_name(name: str) -> str:
    """Lucid importer is picky about unicode punctuation in labels."""
    return name.replace("\u2014", "-").replace("[", "(").replace("]", ")")


def build_bpmn(
    process_id: str,
    process_name: str,
    lanes: dict[str, str],
    nodes: dict,
    edges: list,
    lucid_compat: bool = False,
    layout: dict | None = None,
) -> str:
    lane_order = list(lanes.keys())
    opts = {**DEFAULT_LAYOUT, **(layout or {})}
    lane_heights = compute_lane_heights(nodes, lane_order, opts)
    positions = layout_in_lanes(nodes, edges, lane_order, layout=opts)

    pool_h = sum(lane_heights.values()) + opts["pool_pad_y"]
    max_x = max(
        (
            node_bounds(nid, nodes[nid]["type"], positions[nid])[0]
            + node_bounds(nid, nodes[nid]["type"], positions[nid])[2]
            for nid in nodes
        ),
        default=ORIGIN_X + 400,
    )
    pool_w = max_x - ORIGIN_X + POOL_LABEL_W + opts["pool_pad_x"]

    defs_attrs = {
        "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xmlns:bpmn": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        "xmlns:bpmndi": "http://www.omg.org/spec/BPMN/20100524/DI",
        "xmlns:dc": "http://www.omg.org/spec/DD/20100524/DC",
        "xmlns:di": "http://www.omg.org/spec/DD/20100524/DI",
        "id": f"Definitions_{process_id}",
        "targetNamespace": "http://dlsu.edu.ph/student-journey",
    }
    if not lucid_compat:
        defs_attrs["xmlns:color"] = COLOR_NS
        defs_attrs["xmlns:bioc"] = BIOC_NS

    defs = Element("bpmn:definitions", defs_attrs)

    if not lucid_compat:
        collab = SubElement(defs, "bpmn:collaboration", {"id": f"Collaboration_{process_id}"})
        SubElement(
            collab,
            "bpmn:participant",
            {"id": f"Participant_{process_id}", "name": process_name, "processRef": process_id},
        )

    proc = SubElement(defs, "bpmn:process", {
        "id": process_id,
        "name": sanitize_lucid_name(process_name) if lucid_compat else process_name,
        "isExecutable": "false",
    })
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
        if meta.get("actor") and not lucid_compat:
            name = f"{name} [{meta['actor']}]"
        if lucid_compat:
            name = sanitize_lucid_name(name)
        attrs = {"id": nid, "name": name}
        if ntype == "start":
            el = SubElement(proc, "bpmn:startEvent", attrs)
        elif ntype == "end":
            el = SubElement(proc, "bpmn:endEvent", attrs)
        elif ntype == "gateway":
            el = SubElement(proc, "bpmn:exclusiveGateway", attrs)
        else:
            tag = "bpmn:task" if lucid_compat else task_tag(ntype)
            el = SubElement(proc, tag, attrs)
        if not lucid_compat:
            fill, stroke = node_colors(meta)
            append_color_extensions(el, fill, stroke)

    for i, edge in enumerate(edges):
        attrs = {"id": f"Flow_{i + 1}", "sourceRef": edge["from"], "targetRef": edge["to"]}
        if edge.get("label"):
            attrs["name"] = edge["label"]
        SubElement(proc, "bpmn:sequenceFlow", attrs)

    diagram = SubElement(defs, "bpmndi:BPMNDiagram", {"id": f"BPMNDiagram_{process_id}"})
    plane_element = process_id if lucid_compat else f"Collaboration_{process_id}"
    plane = SubElement(
        diagram,
        "bpmndi:BPMNPlane",
        {"id": f"BPMNPlane_{process_id}", "bpmnElement": plane_element},
    )

    if not lucid_compat:
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
            lane_band_fill = lane_fill
            lane_shape = SubElement(
                plane,
                "bpmndi:BPMNShape",
                {"id": f"Lane_{lid}_di", "bpmnElement": f"Lane_{lid}", "isHorizontal": "true"},
            )
            lane_top = ORIGIN_Y + sum(lane_heights[l] for l in lane_order[:i])
            SubElement(lane_shape, "dc:Bounds", {
                "x": str(ORIGIN_X), "y": str(lane_top),
                "width": str(pool_w - POOL_LABEL_W), "height": str(lane_heights[lid]),
            })
            append_color_extensions(lane_shape, lane_band_fill, lane_stroke)

    for nid, meta in nodes.items():
        ntype = meta["type"]
        x, y, w, h = node_bounds(nid, ntype, positions[nid])
        shape = SubElement(plane, "bpmndi:BPMNShape", {"id": f"{nid}_di", "bpmnElement": nid})
        if ntype == "gateway":
            shape.set("isMarkerVisible", "true")
        SubElement(shape, "dc:Bounds", {"x": str(x), "y": str(y), "width": str(w), "height": str(h)})
        if not lucid_compat:
            fill, stroke = node_colors(meta)
            append_color_extensions(shape, fill, stroke)

    for i, edge in enumerate(edges):
        edge_el = SubElement(plane, "bpmndi:BPMNEdge", {"id": f"Flow_{i + 1}_di", "bpmnElement": f"Flow_{i + 1}"})
        waypoints = route_edge(edge["from"], edge["to"], nodes, positions)
        for px, py in waypoints:
            SubElement(edge_el, "di:waypoint", {"x": str(px), "y": str(py)})
        label = edge.get("label")
        if label and len(waypoints) >= 2:
            mid = len(waypoints) // 2
            px = (waypoints[mid - 1][0] + waypoints[mid][0]) // 2
            py = (waypoints[mid - 1][1] + waypoints[mid][1]) // 2
            lbl_w = min(max(len(label) * 6, 56), 220)
            lbl_h = 27 if len(label) > 22 else 14
            label_el = SubElement(edge_el, "bpmndi:BPMNLabel")
            SubElement(label_el, "dc:Bounds", {
                "x": str(px - lbl_w // 2),
                "y": str(py - lbl_h - 6),
                "width": str(lbl_w),
                "height": str(lbl_h),
            })

    return prettify(defs)


def write_bpmn(
    rel_path: str,
    process_id: str,
    process_name: str,
    lanes: dict,
    nodes: dict,
    edges: list,
    lucid_compat: bool = False,
    layout: dict | None = None,
):
    out = ROOT / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    xml = build_bpmn(process_id, process_name, lanes, nodes, edges, lucid_compat=lucid_compat, layout=layout)
    if lucid_compat:
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + "\n".join(xml.split("\n")[1:])
    out.write_text(xml, encoding="utf-8")
    label = " (lucid)" if lucid_compat else ""
    print(f"  wrote {rel_path}{label}")


# Each diagram: (path, process_id, name, lanes, nodes, edges)
DIAGRAMS = [
    (
        "1. applicant_status/part_1_account_to_submission.bpmn",
        "Applicant_Part1_AccountToSubmission",
        "A — Part 1: Account to Submission",
        L_APPLICANT,
        {
            "Start": n("Start", "Account created", "start", "applicant", "Applicant", layer=0),
            "A0": n("A0", "A0 — Draft", "user", "applicant", "Applicant", layer=1),
            "A1_0": n("A1_0", "A1.0 — Submitted Form", "user", "applicant", "Applicant", layer=2),
            "GW_Req": n("GW_Req", "Requirements OK?", "gateway", "oas", "OAS", layer=3),
            "A2_1": n("A2_1", "A2.1 — Deficiencies", "service", "oas", "OAS", layer=4),
            "A2_0": n("A2_0", "A2.0 — Complete Requirements", "service", "oas", "OAS", layer=5),
            "End_Next": n("End_Next", "Continue to evaluation", "end", "oas", "OAS", layer=6),
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
        "1. applicant_status/part_2a_exam_evaluation.bpmn",
        "Applicant_Part2a_ExamEvaluation",
        "A — Part 2A: Exam & Evaluation",
        L_APPLICANT,
        {
            # OAS lane — main spine + branch tracks (row offsets reduce overlap)
            "Start": n("Start", "From A2.0 complete", "start", "oas", "OAS", layer=0),
            "GW_Init": n("GW_Init", "Initial evaluation", "gateway", "oas", "OAS", layer=1),
            "A3_0": n("A3_0", "A3.0 — Exam Required", "service", "oas", "OAS", layer=2, row=0),
            "A3_1": n("A3_1", "A3.1 — Exam Exempted", "service", "oas", "OAS", layer=2, row=-1),
            "A3_2": n("A3_2", "A3.2 — Not Qualified", "end", "oas", "OAS", layer=2, row=1),
            "GW_Exam": n("GW_Exam", "Exam outcome", "gateway", "oas", "OAS", layer=3),
            "A4_3": n("A4_3", "A4.3 — Further Evaluation", "service", "oas", "OAS", layer=6),
            "End_Results": n("End_Results", "To admission results", "end", "oas", "OAS", layer=7),
            # Applicant lane — exam path left-to-right above OAS spine
            "A4_1": n("A4_1", "A4.1 — Exam Pending", "user", "applicant", "Applicant", layer=4),
            "A4_0": n("A4_0", "A4.0 — Exam Taken", "user", "applicant", "Applicant", layer=5),
            "A4_2": n("A4_2", "A4.2 — Not Qualified (no exam)", "end", "applicant", "Applicant", layer=6),
        },
        [
            e("Start", "GW_Init"),
            e("GW_Init", "A3_0", "Exam required"),
            e("GW_Init", "A3_1", "Exam exempted"),
            e("GW_Init", "A3_2", "Failed initial eval"),
            e("GW_Init", "A4_3", "Further screening only"),
            e("A3_0", "GW_Exam"),
            e("GW_Exam", "A4_1", "Exam pending"),
            e("GW_Exam", "A4_0", "Exam taken"),
            e("GW_Exam", "A4_2", "Exam window lapsed"),
            e("A4_1", "A4_0", "Exam taken"),
            e("A4_1", "A4_2", "Exam window lapsed"),
            e("A4_0", "A4_3", "Further screening"),
            e("A3_1", "End_Results"),
            e("A4_3", "End_Results"),
        ],
        {
            "lane_h": 160,
            "gap_x": 130,
            "row_step": 72,
            "lane_pad": 50,
            "pool_pad_x": 180,
        },
    ),
    (
        "1. applicant_status/part_2b_admission_results.bpmn",
        "Applicant_Part2b_AdmissionResults",
        "A — Part 2B: Admission Results",
        L_APPLICANT,
        {
            "Start": n("Start", "After evaluation", "start", "oas", "OAS", layer=0),
            "GW_Decision": n("GW_Decision", "Admission decision", "gateway", "oas", "OAS", layer=1),
            # Gateway branches — stacked vertically at one column
            "A5_1": n("A5_1", "A5.1 — Probationary", "service", "oas", "OAS", layer=2, row=-2),
            "A5_2": n("A5_2", "A5.2 — Redirected", "service", "oas", "OAS", layer=2, row=-1),
            "A5_3": n("A5_3", "A5.3 — Waitlisted", "service", "oas", "OAS", layer=2, row=0),
            "A5_5": n("A5_5", "A5.5 — Not Qualified", "end", "oas", "OAS", layer=2, row=1),
            # Main spine — offered hub (also waitlist upgrade target)
            "A5_0": n("A5_0", "A5.0 — Offered", "service", "oas", "OAS", layer=3),
            "End_Accept": n("End_Accept", "Continue to acceptance", "end", "applicant", "Applicant", layer=4),
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
        {
            "lane_h": 160,
            "gap_x": 130,
            "row_step": 72,
            "lane_pad": 50,
            "pool_pad_x": 180,
        },
    ),
    (
        "1. applicant_status/part_3_acceptance_to_student.bpmn",
        "Applicant_Part3_AcceptanceToStudent",
        "A — Part 3: Acceptance to Student",
        L_APPLICANT_REG,
        {
            "Start": n("Start", "Admission offer", "start", "applicant", "Applicant", layer=0),
            "A6_0": n("A6_0", "A6.0 — Reserved", "service", "oas", "Admissions", layer=1),
            "GW_Req": n("GW_Req", "Requirements complete?", "gateway", "oas", "Admissions", layer=2),
            "A7_1": n("A7_1", "A7.1 — Provisionally Admitted", "service", "oas", "Admissions", layer=3, row=-1),
            "A7_0": n("A7_0", "A7.0 — Officially Admitted", "service", "oas", "Admissions", layer=4),
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "registrar", "Registrar", layer=5),
            "End_Student": n("End_Student", "Student status continues", "end", "registrar", "Registrar", layer=6),
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
        {
            "lane_h": 150,
            "gap_x": 130,
            "row_step": 65,
            "lane_pad": 45,
            "pool_pad_x": 180,
        },
    ),
    (
        "1. applicant_status/part_4_terminal_or_exception_states.bpmn",
        "Applicant_Part4_TerminalExceptions",
        "A — Part 4: Terminal & Exception States",
        L_APPLICANT_EXCEPTIONS,
        {
            # Eval lane — early rejection terminals (reference, no inter-flows)
            "A3_2": n("A3_2", "A3.2 — Not Qualified (initial)", "end", "eval", "OAS Eval", layer=0),
            "A4_2": n("A4_2", "A4.2 — Not Qualified (no exam)", "end", "eval", "OAS Eval", layer=1),
            "A5_5": n("A5_5", "A5.5 — Not Qualified", "end", "eval", "OAS Eval", layer=2),
            # OAS lane — acceptance-phase exceptions
            "A6_0": n("A6_0", "A6.0 — Reserved", "service", "oas", "Admissions", layer=0),
            "A6_1": n("A6_1", "A6.1 — Cancelled (non-payment)", "end", "oas", "Admissions", layer=1, row=1),
            "A7_0": n("A7_0", "A7.0 — Officially Admitted", "service", "oas", "Admissions", layer=2),
            "A7_1": n("A7_1", "A7.1 — Provisionally Admitted", "service", "oas", "Admissions", layer=3),
            "A8_0": n("A8_0", "A8.0 — Cancelled (no reqs)", "end", "oas", "Admissions", layer=4),
            # Applicant lane — deferral & withdrawal
            "A7_2": n("A7_2", "A7.2 — Deferred", "user", "applicant", "Applicant", layer=1),
            "A8_1": n("A8_1", "A8.1 — Cancelled (withdrawal)", "end", "applicant", "Applicant", layer=4),
        },
        [
            e("A6_0", "A6_1", "Did not pay fee"),
            e("A6_0", "A7_2", "Did not enroll"),
            e("A7_1", "A8_0", "1 year lapsed"),
            e("A7_0", "A8_1", "Withdrew"),
            e("A7_1", "A8_1", "Withdrew"),
        ],
        {
            "lane_h": 150,
            "gap_x": 130,
            "row_step": 65,
            "lane_pad": 45,
            "pool_pad_x": 160,
        },
    ),
    (
        "2. student_status/part_1_active_and_enrollment.bpmn",
        "Student_Part1_ActiveEnrollment",
        "S — Part 1: Active & Enrollment",
        L_STUDENT,
        {
            "Start": n("Start", "Officially admitted (A7.x)", "start", "registrar", "Registrar", layer=0),
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "registrar", "Registrar", layer=1),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "registrar", "Registrar", layer=2),
            "End_Next": n("End_Next", "Continues in Parts 2–4", "end", "registrar", "Registrar", layer=3),
        },
        [
            e("Start", "S1_0"),
            e("S1_0", "S2_0", "Enrolled / enlisted"),
            e("S2_0", "End_Next"),
        ],
        {
            "lane_h": 150,
            "gap_x": 130,
            "row_step": 65,
            "lane_pad": 45,
            "pool_pad_x": 180,
        },
    ),
    (
        "2. student_status/part_2_residency_and_loa.bpmn",
        "Student_Part2_ResidencyLOA",
        "S — Part 2: Residency & LOA",
        L_STUDENT,
        {
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "registrar", "Registrar", layer=0),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "registrar", "Registrar", layer=2),
            "S2_2": n("S2_2", "S2.2 — Under LOA", "service", "registrar", "Registrar", layer=4, row=-1),
            "S2_3": n("S2_3", "S2.3 — Prolonged Leave", "service", "registrar", "Registrar", layer=5, row=1),
            "S2_1": n("S2_1", "S2.1 — Residency", "user", "student", "Student", layer=6),
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
        {
            "lane_h": 160,
            "gap_x": 150,
            "row_step": 75,
            "lane_pad": 50,
            "pool_pad_x": 200,
        },
    ),
    (
        "2. student_status/part_3_awol_suspension_and_exit.bpmn",
        "Student_Part3_AWOLSuspensionExit",
        "S — Part 3: AWOL, Suspension & Exit",
        L_STUDENT_ADMIN,
        {
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "registrar", "Registrar", layer=0),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "registrar", "Registrar", layer=2),
            "S3_2": n("S3_2", "S3.2 — Suspended", "service", "disciplinary", "Disciplinary", layer=3),
            "S3_1": n("S3_1", "S3.1 — AWOL", "service", "registrar", "Registrar", layer=4),
            "S4_1": n("S4_1", "S4.1 — Exited (good standing)", "end", "student", "Student", layer=5),
            "S4_2": n("S4_2", "S4.2 — Disqualified", "end", "disciplinary", "Disciplinary", layer=5),
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
        {
            "lane_h": 160,
            "gap_x": 150,
            "row_step": 75,
            "lane_pad": 50,
            "pool_pad_x": 200,
        },
    ),
    (
        "2. student_status/part_4_graduation_and_terminal_states.bpmn",
        "Student_Part4_GraduationTerminal",
        "S — Part 4: Graduation & Terminal",
        L_STUDENT_ADMIN,
        {
            "S2_0": n("S2_0", "S2.0 — Active", "service", "registrar", "Registrar", layer=0),
            "S4_0": n("S4_0", "S4.0 — Graduated", "end", "registrar", "Registrar", layer=2),
            "S4_1": n("S4_1", "S4.1 — Exited (good standing)", "end", "student", "Student", layer=3),
            "S4_2": n("S4_2", "S4.2 — Disqualified", "end", "disciplinary", "Disciplinary", layer=4),
        },
        [
            e("S2_0", "S4_0", "All programs graduated"),
            e("S2_0", "S4_1", "University exit"),
            e("S2_0", "S4_2", "Disqualification"),
        ],
        {
            "lane_h": 160,
            "gap_x": 150,
            "row_step": 75,
            "lane_pad": 50,
            "pool_pad_x": 200,
        },
    ),
    (
        "3. student_program_status/part_1_good_standing_and_probation.bpmn",
        "Program_Part1_GoodStandingProbation",
        "P — Part 1: Good Standing & Probation",
        L_PROGRAM,
        {
            "Start_N": n("Start_N", "Normal admission", "start", "program", "Program Office", layer=0, row=-1),
            "Start_P": n("Start_P", "Probationary offer", "start", "program", "Program Office", layer=0, row=1),
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program", "Program Office", layer=2),
            "P1_1": n("P1_1", "P1.1 — Probationary", "service", "program", "Program Office", layer=3),
            "End_Next": n("End_Next", "Continues in Parts 2–3", "end", "program", "Program Office", layer=5),
        },
        [
            e("Start_N", "P1_0"),
            e("Start_P", "P1_1"),
            e("P1_0", "P1_1", "Standards not met"),
            e("P1_1", "P1_0", "Probation lifted"),
            e("P1_0", "End_Next"),
        ],
        {
            "lane_h": 160,
            "gap_x": 150,
            "row_step": 75,
            "lane_pad": 50,
            "pool_pad_x": 200,
        },
    ),
    (
        "3. student_program_status/part_2_snas_sap_and_ineligible.bpmn",
        "Program_Part2_SNASSAPIneligible",
        "P — Part 2: SNAS, SAP & Ineligible",
        L_PROGRAM,
        {
            "P1_1": n("P1_1", "P1.1 — Probationary", "service", "program", "Program Office", layer=0),
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program", "Program Office", layer=2),
            "P1_3": n("P1_3", "P1.3 — Strict Probation (IS)", "service", "program", "Program Office", layer=3, row=1),
            "P1_2": n("P1_2", "P1.2 — SNAS", "service", "program", "Program Office", layer=4, row=-1),
            "P1_4": n("P1_4", "P1.4 — Ineligible", "end", "program", "Program Office", layer=6),
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
        {
            "lane_h": 160,
            "gap_x": 150,
            "row_step": 75,
            "lane_pad": 50,
            "pool_pad_x": 200,
        },
    ),
    (
        "3. student_program_status/part_3_graduation_and_terminal_states.bpmn",
        "Program_Part3_GraduationTerminal",
        "P — Part 3: Graduation & Terminal",
        L_PROGRAM,
        {
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program", "Program Office", layer=0),
            "P2_0": n("P2_0", "P2.0 — Candidate for Graduation", "service", "program", "Program Office", layer=2),
            "P3_1": n("P3_1", "P3.1 — Incomplete", "end", "student", "Student", layer=3),
            "P3_0": n("P3_0", "P3.0 — Graduated", "end", "program", "Program Office", layer=4),
        },
        [
            e("P1_0", "P2_0", "Graduation check passed"),
            e("P2_0", "P3_0", "Commencement + 1 week"),
            e("P1_0", "P3_1", "University exit"),
            e("P2_0", "P3_1", "University exit"),
        ],
        {
            "lane_h": 160,
            "gap_x": 150,
            "row_step": 75,
            "lane_pad": 50,
            "pool_pad_x": 200,
        },
    ),
    (
        "4. combined_lifecycle/1. high_level_lifecycle_overview.bpmn",
        "Combined_HighLevelOverview",
        "Combined — High-Level Lifecycle Overview",
        L_OVERVIEW,
        {
            "Start": n("Start", "Start", "start", "applicant", "Applicant", layer=0),
            "APPLICANT": n("APPLICANT", "Applicant phase (A0–A5.x)", "user", "applicant", "Applicant", layer=1),
            "ACCEPTED": n("ACCEPTED", "Accepted (A6.0–A7.x)", "service", "admissions", "Admissions", layer=2),
            "ACTIVE": n("ACTIVE", "Active Student (S1.0–S2.x)", "service", "student_lane", "Enrollment", layer=3),
            "DISRUPT": n("DISRUPT", "LOA / AWOL / Suspended", "service", "student_lane", "Enrollment", layer=4, row=1),
            "PROGRAM": n("PROGRAM", "Program Standing (P1.0–P2.0)", "service", "program_lane", "Program Office", layer=4),
            "OUTCOME": n("OUTCOME", "Graduation / Exit / Terminal", "service", "outcome", "University", layer=5),
            "End": n("End", "Terminal", "end", "outcome", "University", layer=6),
        },
        [
            e("Start", "APPLICANT"),
            e("APPLICANT", "ACCEPTED", "Admitted / reserved"),
            e("APPLICANT", "OUTCOME", "Rejected / cancelled"),
            e("ACCEPTED", "ACTIVE", "Becomes student, enrolls"),
            e("ACTIVE", "DISRUPT", "Leave / absence / discipline"),
            e("DISRUPT", "ACTIVE", "Returnee re-enrolls"),
            e("ACTIVE", "OUTCOME", "Graduate or exit"),
            e("ACTIVE", "PROGRAM", "Academic standing tracked per program"),
            e("PROGRAM", "OUTCOME", "All programs graduated"),
            e("OUTCOME", "End"),
        ],
        {
            "lane_h": 150,
            "gap_x": 140,
            "row_step": 70,
            "lane_pad": 45,
            "pool_pad_x": 240,
        },
    ),
    (
        "4. combined_lifecycle/2. applicant_to_student_bridge.bpmn",
        "Combined_ApplicantToStudentBridge",
        "Combined — Applicant to Student Bridge",
        L_COMBINED,
        {
            "A7_0": n("A7_0", "A7.0 — Officially Admitted", "service", "admissions", "Admissions", layer=0, row=-1),
            "A7_1": n("A7_1", "A7.1 — Provisionally Admitted", "service", "admissions", "Admissions", layer=0, row=1),
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "student_lane", "Registrar", layer=2),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "student_lane", "Registrar", layer=4),
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program_lane", "Program Office", layer=4),
            "P1_1": n("P1_1", "P1.1 — Probationary", "service", "program_lane", "Program Office", layer=5),
        },
        [
            e("A7_0", "S1_0", "Becomes student"),
            e("A7_1", "S1_0", "Becomes student (provisional)"),
            e("S1_0", "S2_0", "Enrolled / enlisted"),
            e("S1_0", "P1_0", "Normal admission"),
            e("S1_0", "P1_1", "Probationary offer"),
        ],
        {
            "lane_h": 160,
            "gap_x": 150,
            "row_step": 75,
            "lane_pad": 50,
            "pool_pad_x": 220,
        },
    ),
    (
        "4. combined_lifecycle/3. parallel_student_program_constrained_fsm.bpmn",
        "Combined_ParallelStudentProgramFSM",
        "Combined — Parallel Student × Program FSM",
        L_COMBINED,
        {
            "Start": n("Start", "Admitted from A7.x", "start", "admissions", "Admissions", layer=0),
            "S1_0": n("S1_0", "S1.0 — Without Enrollment", "service", "student_lane", "Registrar", layer=1),
            "S2_0": n("S2_0", "S2.0 — Active", "service", "student_lane", "Registrar", layer=2),
            "S2_2": n("S2_2", "S2.2 — Under LOA", "service", "student_lane", "Registrar", layer=4, row=-1),
            "S3_1": n("S3_1", "S3.1 — AWOL", "service", "student_lane", "Registrar", layer=4, row=1),
            "S4_1": n("S4_1", "S4.1 — Exited", "end", "student_lane", "Registrar", layer=5),
            "S4_0": n("S4_0", "S4.0 — Graduated", "end", "student_lane", "Registrar", layer=7),
            "P1_0": n("P1_0", "P1.0 — Eligible", "service", "program_lane", "Program Office", layer=1),
            "P1_1": n("P1_1", "P1.1 — Probationary", "service", "program_lane", "Program Office", layer=2),
            "P1_2": n("P1_2", "P1.2 — SNAS", "service", "program_lane", "Program Office", layer=3, row=-1),
            "P1_4": n("P1_4", "P1.4 — Ineligible", "service", "program_lane", "Program Office", layer=4, row=1),
            "P2_0": n("P2_0", "P2.0 — Candidacy", "service", "program_lane", "Program Office", layer=5),
            "P3_0": n("P3_0", "P3.0 — Graduated", "end", "program_lane", "Program Office", layer=6),
            "P3_1": n("P3_1", "P3.1 — Incomplete", "end", "program_lane", "Program Office", layer=5, row=1),
            "VALID": n("VALID", "V(S,P) validation layer", "service", "validation", "Records System", layer=3),
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
            e("P3_0", "S4_0", "COMBO-T001 (All Programs Graduated)"),
            e("S4_1", "P3_1", "COMBO-T003 (Exit Forces Incomplete)"),
            e("P1_4", "S1_0", "COMBO-T004 (Ineligible + Shift Pending)"),
            e("S1_0", "S2_0", "COMBO-T005 (Shift Approved)"),
        ],
        {
            "lane_h": 150,
            "gap_x": 140,
            "row_step": 72,
            "lane_pad": 48,
            "pool_pad_x": 240,
        },
    ),
    (
        "4. combined_lifecycle/4. cross_impact_rules.bpmn",
        "Combined_CrossImpactRules",
        "Combined — Cross-Impact Rules (COMBO-T001–T005)",
        L_CROSS,
        {
            "T001_Trig": n("T001_Trig", "All programs → P3.0 Graduated", "service", "program_lane", "Program Office", layer=0, row=0),
            "T001_Eff": n("T001_Eff", "COMBO-T001: Student → S4.0", "service", "student_lane", "Registrar", layer=2, row=0),
            "T003_Trig": n("T003_Trig", "Student exit, program active", "user", "student_lane", "Student", layer=0, row=1),
            "T003_Eff": n("T003_Eff", "COMBO-T003: Program → P3.1", "service", "program_lane", "Program Office", layer=2, row=1),
            "T004_Trig": n("T004_Trig", "P1.4 Ineligible + shift pending", "service", "program_lane", "Program Office", layer=0, row=2),
            "T004_Eff": n("T004_Eff", "COMBO-T004: Student → S1.0", "service", "student_lane", "Registrar", layer=2, row=2),
            "T005_Eff": n("T005_Eff", "COMBO-T005: Shift approved → S2.0", "service", "student_lane", "Registrar", layer=4, row=2),
        },
        [
            e("T001_Trig", "T001_Eff", "forces"),
            e("T003_Trig", "T003_Eff", "forces"),
            e("T004_Trig", "T004_Eff", "forces"),
            e("T004_Eff", "T005_Eff", "shift approved"),
        ],
        {
            "lane_h": 180,
            "gap_x": 150,
            "row_step": 80,
            "lane_pad": 55,
            "pool_pad_x": 220,
        },
    ),
    (
        "4. combined_lifecycle/5. student_status_vs_program_status_interaction.bpmn",
        "Combined_StudentProgramInteraction",
        "Combined — Student vs Program Interaction",
        L_CROSS,
        {
            "PALL": n("PALL", "All programs → P3.0 Graduated", "service", "program_lane", "Program Office", layer=0, row=0),
            "SGRAD": n("SGRAD", "Student → S4.0 Graduated", "service", "student_lane", "Registrar", layer=2, row=0),
            "SEXIT": n("SEXIT", "Student exit, program active", "user", "student_lane", "Student", layer=0, row=1),
            "PINC": n("PINC", "Program → P3.1 Incomplete", "service", "program_lane", "Program Office", layer=2, row=1),
            "PINE": n("PINE", "P1.4 Ineligible + shift pending", "service", "program_lane", "Program Office", layer=0, row=2),
            "SAWE": n("SAWE", "Student → S1.0 Without Enrollment", "service", "student_lane", "Registrar", layer=2, row=2),
            "SACT": n("SACT", "Student → S2.0 Active", "service", "student_lane", "Registrar", layer=4, row=2),
        },
        [
            e("PALL", "SGRAD", "forces"),
            e("SEXIT", "PINC", "forces"),
            e("PINE", "SAWE", "forces"),
            e("SAWE", "SACT", "shift approved"),
        ],
        {
            "lane_h": 180,
            "gap_x": 150,
            "row_step": 80,
            "lane_pad": 55,
            "pool_pad_x": 220,
        },
    ),
]


def normalize_rel_path(path: str) -> str:
    return path.replace("\\", "/").lstrip("/")


def load_protected_paths() -> set[str]:
    """Paths listed in protected_bpmn.txt are skipped unless --force is used."""
    if not PROTECTED_LIST.exists():
        return set()
    protected: set[str] = set()
    for line in PROTECTED_LIST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        protected.add(normalize_rel_path(line))
    return protected


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate BPMN 2.0 XML from generate_bpmn.py specs.")
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="PATH",
        help="Regenerate only this diagram (repeatable). Example: --only \"1. applicant_status/part_1_account_to_submission.bpmn\"",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite files listed in protected_bpmn.txt",
    )
    args = parser.parse_args()

    only_filter = {normalize_rel_path(p) for p in args.only}
    protected = set() if args.force else load_protected_paths()

    print("Generating BPMN files with swimlanes...")
    if protected:
        print(f"  Skipping {len(protected)} protected file(s) — see protected_bpmn.txt")
    if only_filter:
        print(f"  Regenerating only: {', '.join(sorted(only_filter))}")

    written = 0
    skipped_protected = 0
    skipped_filter = 0

    for item in DIAGRAMS:
        layout = None
        if len(item) == 7:
            rel, pid, pname, lanes, nodes, edges, layout = item
        else:
            rel, pid, pname, lanes, nodes, edges = item

        rel_norm = normalize_rel_path(rel)
        if only_filter and rel_norm not in only_filter:
            skipped_filter += 1
            continue
        if rel_norm in protected:
            print(f"  skip (protected): {rel}")
            skipped_protected += 1
            continue

        write_bpmn(rel, pid, pname, lanes, nodes, edges, layout=layout)
        lucid_rel = f"lucid_import/{rel}"
        write_bpmn(lucid_rel, pid, pname, lanes, nodes, edges, lucid_compat=True, layout=layout)
        written += 1

    print(
        f"Done — wrote {written} diagram(s) (+ Lucid copies) in {ROOT}"
        f" | skipped protected: {skipped_protected}, skipped by --only filter: {skipped_filter}"
    )


if __name__ == "__main__":
    main()
