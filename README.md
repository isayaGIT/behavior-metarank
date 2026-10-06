# Behavior MetaRank

An open, machine-readable evidence base for psychological and behavioral mechanisms related to human behavior.

## Core idea

- One mechanism = one folder.
- Each mechanism folder is self-contained: definition, aliases, source papers, and extracted effect estimates.
- mechanisms/ is the source of truth.
- scripts/build.py discovers mechanism folders automatically. There is no hard-coded candidate mechanism list.
- Generated evidence tables are rebuilt from all currently present mechanism folders.
- Association, prospective prediction, causal intervention, and mediation evidence are kept separate rather than collapsed prematurely into one score.

## Repository layout

mechanisms/<mechanism-id>/ contains mechanism.json, papers.csv, and notes.md.
scripts/build.py validates and scans all mechanisms.
generated/ contains machine-readable master outputs.
paper/manuscript.md contains an auto-generated evidence table.
protocol/ contains review, inclusion, and extraction rules.

## Evidence layers

1. association — cross-sectional / observational association.
2. prospective — longitudinal prediction where the mechanism precedes behavior.
3. causal — randomized or quasi-experimental manipulation evidence.
4. mediation — evidence that mechanism change mediates behavior change.

These are intentionally not treated as interchangeable effect sizes.

## Build

Run: python3 scripts/build.py

The build fails on invalid mechanism folders so generated outputs do not silently drift.

## Contributing a mechanism

Copy mechanisms/_template/ to mechanisms/<mechanism-id>/, fill in the files, then run the build.

A new mechanism becomes part of the master evidence base because its folder exists and validates, not because it was pre-registered in a candidate list.
