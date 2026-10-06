#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "generated" / "evidence_matrix.csv"
OUT = ROOT / "generated" / "rankings"
HUMAN = ROOT / "RANKING.md"
OUT.mkdir(parents=True, exist_ok=True)

BUCKETS = [
    ("causal", "smd", "Causal — standardized effects"),
    ("causal", "odds_ratio", "Causal — odds ratios"),
    ("causal", "risk_ratio", "Causal — risk ratios"),
    ("prospective", "correlation", "Prospective prediction — correlations"),
    ("association", "correlation", "Association — correlations"),
]

def as_float(x: str):
    try:
        return float(x)
    except Exception:
        return None

def clean(x: str) -> str:
    return str(x or "").replace("|", "\\|").replace("\n", " ").strip()

def effect_text(r: dict[str, str]) -> str:
    metric = clean(r.get("effect_metric", ""))
    value = clean(r.get("effect_value", ""))
    lo = clean(r.get("ci_low", ""))
    hi = clean(r.get("ci_high", ""))
    if lo and hi:
        return f"{metric} = {value} [{lo}, {hi}]"
    return f"{metric} = {value}"

with MATRIX.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

eligible = []
excluded = []
for r in rows:
    ok = str(r.get("rank_eligible", "")).lower() in {"true", "1", "yes"}
    (eligible if ok else excluded).append(r)

ex_fields = [
    "mechanism_id","mechanism_name","id","layer","outcome","effect_metric",
    "effect_value","rank_target","rank_exclusion_reason"
]
with (OUT / "excluded.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ex_fields)
    w.writeheader()
    for r in excluded:
        w.writerow({k:r.get(k,"") for k in ex_fields})

index_rows = []
bucket_rows: dict[tuple[str, str], list[dict[str, str]]] = {}

for layer, group, _title in BUCKETS:
    bucket = [r for r in eligible if r.get("layer")==layer and r.get("rank_metric_group")==group]
    bucket = [r for r in bucket if as_float(r.get("effect_value","")) is not None]
    bucket.sort(key=lambda r: as_float(r["effect_value"]), reverse=True)
    bucket_rows[(layer, group)] = bucket

    filename = f"{layer}__{group}.csv"
    fields = [
        "rank","mechanism_id","mechanism_name","synthesis_id","effect_metric","effect_value",
        "ci_low","ci_high","outcome","behavior_domain","k","n","source_ids","notes"
    ]
    with (OUT / filename).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, r in enumerate(bucket, 1):
            row = {
                "rank": i,
                "mechanism_id": r["mechanism_id"],
                "mechanism_name": r["mechanism_name"],
                "synthesis_id": r["id"],
                "effect_metric": r["effect_metric"],
                "effect_value": r["effect_value"],
                "ci_low": r.get("ci_low",""),
                "ci_high": r.get("ci_high",""),
                "outcome": r["outcome"],
                "behavior_domain": r["behavior_domain"],
                "k": r.get("k",""),
                "n": r.get("n",""),
                "source_ids": r.get("source_ids",""),
                "notes": r.get("notes",""),
            }
            w.writerow(row)
            index_rows.append({
                "leaderboard": filename,
                "rank": i,
                "mechanism_id": r["mechanism_id"],
                "mechanism_name": r["mechanism_name"],
                "effect_metric": r["effect_metric"],
                "effect_value": r["effect_value"],
                "outcome": r["outcome"],
                "behavior_domain": r["behavior_domain"],
            })

idx_fields = ["leaderboard","rank","mechanism_id","mechanism_name","effect_metric","effect_value","outcome","behavior_domain"]
with (OUT / "index.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=idx_fields)
    w.writeheader()
    w.writerows(index_rows)

# Deterministic human-readable report.
mechanism_count = len({r["mechanism_id"] for r in rows})
lines = [
    "# Behavior MetaRank — Live Ranking",
    "",
    "> This file is generated automatically by scripts/rank.py from the current mechanism evidence. Do not edit it by hand.",
    "",
    f"Current coverage: **{mechanism_count} mechanisms**, **{len(rows)} syntheses**, **{len(eligible)} ranking-eligible direct-behavior syntheses**, and **{len(excluded)} excluded syntheses**.",
    "",
    "## How to read this",
    "",
    "MetaRank v0 does **not** compute one global score. Effect metrics and evidence designs are kept separate. A larger number only means a higher position **within the same leaderboard**; it does not mean that an OR of 1.8 is directly larger than a d of 0.6 or an r of 0.4.",
    "",
    "Only syntheses classified as direct behavior outcomes enter these leaderboards. Intention, identity, habit-strength, and mixed composite outcomes are excluded until a valid behavior-specific estimate is available.",
    "",
]

for layer, group, title in BUCKETS:
    bucket = bucket_rows[(layer, group)]
    lines += [f"## {title}", ""]
    if not bucket:
        lines += ["No eligible syntheses yet.", ""]
        continue
    lines += [
        "| Rank | Mechanism | Effect | Outcome | Domain | Evidence size |",
        "|---:|---|---:|---|---|---|",
    ]
    for i, r in enumerate(bucket, 1):
        k = clean(r.get("k",""))
        n = clean(r.get("n",""))
        size_parts = []
        if k:
            size_parts.append(f"k={k}")
        if n:
            size_parts.append(f"n={n}")
        size = ", ".join(size_parts) if size_parts else "—"
        mechanism_link = f"[{clean(r['mechanism_name'])}](mechanisms/{clean(r['mechanism_id'])}/)"
        lines.append(
            f"| {i} | {mechanism_link} | {effect_text(r)} | "
            f"{clean(r['outcome'])} | {clean(r['behavior_domain'])} | {size} |"
        )
    lines.append("")

lines += [
    "## Excluded from direct-behavior ranking",
    "",
    "These syntheses remain in the evidence base but are not allowed into the direct-behavior leaderboard.",
    "",
]
if excluded:
    lines += [
        "| Mechanism | Effect | Outcome | Reason |",
        "|---|---:|---|---|",
    ]
    for r in excluded:
        mechanism_link = f"[{clean(r['mechanism_name'])}](mechanisms/{clean(r['mechanism_id'])}/)"
        lines.append(
            f"| {mechanism_link} | {effect_text(r)} | {clean(r['outcome'])} | "
            f"{clean(r.get('rank_exclusion_reason',''))} |"
        )
else:
    lines.append("None.")

lines += [
    "",
    "## Methodological status",
    "",
    "This is Rank v0: a descriptive, metric-specific leaderboard. A publication-quality cross-metric rank still requires effect-size harmonization, overlap correction, risk-of-bias assessment, domain/replication handling, uncertainty-aware ranking, and sensitivity analysis.",
    "",
    "Detailed rules: [protocol/ranking.md](protocol/ranking.md)",
    "",
]

HUMAN.write_text("\n".join(lines), encoding="utf-8")

print(f"Rank v0: {len(eligible)} eligible syntheses, {len(excluded)} excluded syntheses, {len(index_rows)} ranked rows.")
print(f"Wrote human-readable ranking: {HUMAN}")
