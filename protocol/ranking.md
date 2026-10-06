# Ranking protocol — v0

Behavior MetaRank v0 deliberately avoids a single global score.

## Why

The evidence base currently mixes correlations, standardized mean differences, odds ratios, risk ratios, different evidence layers, different behavioral domains, and some outcomes that are not behavior at all.

Ranking raw effect_value across those categories would be statistically invalid.

## v0 eligibility

A synthesis can enter a leaderboard only when:
1. its outcome is explicitly classified as direct_behavior;
2. it has a numeric effect estimate;
3. its evidence layer and metric group match a defined leaderboard.

Nonbehavior outcomes such as intention, identity, or habit strength are excluded.
Composite outcomes that mix behavior with attitudes or intentions are also excluded.

## v0 leaderboards

The current engine produces separate leaderboards for:
- causal standardized mean differences;
- causal odds ratios;
- causal risk ratios;
- prospective correlations;
- association correlations.

Within a leaderboard, entries are sorted by the native effect estimate.

## What v0 does NOT claim

Rank v0 is not a universal ranking of what changes behavior most.

Even within the same metric, behavioral domains, baseline risks, intervention intensity, heterogeneity, study quality, and intervention composition differ.

Therefore v0 is a transparent descriptive leaderboard of currently ingested syntheses.

## Planned next versions

A publication-quality global rank would require:
1. effect-size harmonization with explicit assumptions;
2. study-overlap correction;
3. risk-of-bias and review-quality weights;
4. domain-breadth and replication handling;
5. uncertainty-aware ranking;
6. sensitivity analysis over scoring choices;
7. separate predictive and causal ranks even after harmonization.
