#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MECHANISMS = ROOT / "mechanisms"
GENERATED = ROOT / "generated"
MANUSCRIPT = ROOT / "paper" / "manuscript.md"

LAYERS = ("association", "prospective", "causal", "mediation")
REQ_MECH = ("id", "name", "family", "definition", "status", "updated_at", "syntheses")
REQ_SYN = (
    "id", "layer", "outcome", "behavior_domain", "design", "effect_metric",
    "effect_value", "source_ids", "notes"
)
PAPER_FIELDS = [
    "mechanism_id", "source_id", "title", "year", "doi", "url",
    "study_type", "evidence_layer", "behavior_domain", "effect_metric",
    "effect_value", "ci_low", "ci_high", "k", "n", "notes"
]


def die(msg: str) -> None:
    raise SystemExit(f"BUILD ERROR: {msg}")


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        die(f"{path}: invalid JSON: {e}")


def validate_mechanism(folder: Path, data: dict[str, Any]) -> None:
    missing = [k for k in REQ_MECH if k not in data]
    if missing:
        die(f"{folder}: missing mechanism keys: {missing}")
    if data["id"] != folder.name:
        die(f"{folder}: id {data['id']!r} must equal folder name {folder.name!r}")
    if not isinstance(data["syntheses"], list):
        die(f"{folder}: syntheses must be a list")
    for i, syn in enumerate(data["syntheses"]):
        missing = [k for k in REQ_SYN if k not in syn]
        if missing:
            die(f"{folder}: syntheses[{i}] missing keys: {missing}")
        if syn["layer"] not in LAYERS:
            die(f"{folder}: syntheses[{i}] invalid layer {syn['layer']!r}")


def mechanism_folders() -> list[Path]:
    return sorted(
        p for p in MECHANISMS.iterdir()
        if p.is_dir() and not p.name.startswith("_")
    )


def load_papers(folder: Path, mechanism_id: str) -> list[dict[str, str]]:
    path = folder / "papers.csv"
    if not path.exists():
        die(f"{folder}: papers.csv is required")
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        headers = set(reader.fieldnames or [])
        required = set(PAPER_FIELDS) - {"mechanism_id"}
        missing_headers = required - headers
        if missing_headers:
            die(f"{path}: missing columns: {sorted(missing_headers)}")
        rows = list(reader)
    out = []
    for row in rows:
        row = dict(row)
        row["mechanism_id"] = mechanism_id
        out.append({k: row.get(k, "") for k in PAPER_FIELDS})
    return out


def fmt_num(x: Any) -> str:
    if x is None or x == "":
        return "—"
    if isinstance(x, float):
        return f"{x:.3f}".rstrip("0").rstrip(".")
    return str(x)


def build_markdown(mechanisms: list[dict[str, Any]]) -> str:
    rows = []
    for m in mechanisms:
        by_layer = {layer: [] for layer in LAYERS}
        for syn in m["syntheses"]:
            val = f"{syn['effect_metric']}={fmt_num(syn['effect_value'])}"
            domain = syn.get("behavior_domain") or ""
            outcome = syn.get("outcome") or ""
            by_layer[syn["layer"]].append(f"{val} → {outcome} ({domain})")
        rows.append(
            "| {name} | {assoc} | {pros} | {causal} | {med} |".format(
                name=m["name"],
                assoc="<br>".join(by_layer["association"]) or "—",
                pros="<br>".join(by_layer["prospective"]) or "—",
                causal="<br>".join(by_layer["causal"]) or "—",
                med="<br>".join(by_layer["mediation"]) or "—",
            )
        )
    header = (
        "| Mechanism | Association | Prospective | Causal | Mediation |\n"
        "|---|---|---|---|---|"
    )
    return header + ("\n" + "\n".join(rows) if rows else "\n")


def update_manuscript(table: str) -> None:
    start = "<!-- AUTO:MECHANISM_TABLE:START -->"
    end = "<!-- AUTO:MECHANISM_TABLE:END -->"
    text = MANUSCRIPT.read_text(encoding="utf-8")
    if start not in text or end not in text:
        die(f"{MANUSCRIPT}: auto-generation markers missing")
    before, rest = text.split(start, 1)
    _, after = rest.split(end, 1)
    MANUSCRIPT.write_text(before + start + "\n" + table + "\n" + end + after, encoding="utf-8")


def main() -> None:
    GENERATED.mkdir(exist_ok=True)
    mechanisms: list[dict[str, Any]] = []
    synth_rows: list[dict[str, Any]] = []
    paper_rows: list[dict[str, str]] = []
    seen_syn: set[str] = set()

    for folder in mechanism_folders():
        path = folder / "mechanism.json"
        if not path.exists():
            die(f"{folder}: mechanism.json is required")
        data = read_json(path)
        validate_mechanism(folder, data)
        mechanisms.append(data)

        papers = load_papers(folder, data["id"])
        source_ids = {r["source_id"] for r in papers}
        paper_rows.extend(papers)

        for syn in data["syntheses"]:
            key = f"{data['id']}::{syn['id']}"
            if key in seen_syn:
                die(f"duplicate synthesis id: {key}")
            seen_syn.add(key)

            missing_sources = [s for s in syn["source_ids"] if s not in source_ids]
            if missing_sources:
                die(f"{folder}: synthesis {syn['id']} references unknown sources {missing_sources}")

            synth_rows.append({
                "mechanism_id": data["id"],
                "mechanism_name": data["name"],
                "mechanism_family": data["family"],
                **{k: syn.get(k) for k in (
                    "id", "layer", "outcome", "behavior_domain", "design", "effect_metric",
                    "effect_value", "ci_low", "ci_high", "k", "n", "notes"
                )},
                "source_ids": ";".join(syn["source_ids"]),
            })

    (GENERATED / "mechanisms.json").write_text(
        json.dumps(mechanisms, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )

    synth_fields = [
        "mechanism_id", "mechanism_name", "mechanism_family", "id", "layer", "outcome", "behavior_domain",
        "design", "effect_metric", "effect_value", "ci_low", "ci_high",
        "k", "n", "source_ids", "notes"
    ]
    with (GENERATED / "evidence_matrix.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=synth_fields)
        w.writeheader()
        w.writerows(synth_rows)

    with (GENERATED / "papers.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=PAPER_FIELDS)
        w.writeheader()
        w.writerows(paper_rows)

    update_manuscript(build_markdown(mechanisms))
    print(f"Built {len(mechanisms)} mechanisms, {len(synth_rows)} syntheses, {len(paper_rows)} paper records.")


if __name__ == "__main__":
    main()
