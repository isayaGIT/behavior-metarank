#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "generated" / "evidence_matrix.csv"
OUT = ROOT / "generated" / "rankings"
OUT.mkdir(parents=True, exist_ok=True)

BUCKET_ORDER = [
    ("causal", "smd"),
    ("causal", "odds_ratio"),
    ("causal", "risk_ratio"),
    ("prospective", "correlation"),
    ("association", "correlation"),
]

def as_float(x: str):
    try:
        return float(x)
    except Exception:
        return None

with MATRIX.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

eligible = []
excluded = []
for r in rows:
    ok = str(r.get("rank_eligible", "")).lower() in {"true", "1", "yes"}
    if ok:
        eligible.append(r)
    else:
        excluded.append(r)

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
for layer, group in BUCKET_ORDER:
    bucket = [r for r in eligible if r.get("layer")==layer and r.get("rank_metric_group")==group]
    bucket = [r for r in bucket if as_float(r.get("effect_value","")) is not None]
    bucket.sort(key=lambda r: as_float(r["effect_value"]), reverse=True)

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

print(f"Rank v0: {len(eligible)} eligible syntheses, {len(excluded)} excluded syntheses, {len(index_rows)} ranked rows.")
