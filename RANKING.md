# Behavior MetaRank — Live Ranking

> This file is generated automatically by scripts/rank.py from the current mechanism evidence. Do not edit it by hand.

Need help reading the coefficients or understanding each mechanism? See [中文解读](RANKING_GUIDE.zh-CN.md) or [English guide](RANKING_GUIDE.en.md).

Current coverage: **23 mechanisms**, **27 syntheses**, **23 ranking-eligible direct-behavior syntheses**, and **4 excluded syntheses**.

## How to read this

MetaRank v0 does **not** compute one global score. Effect metrics and evidence designs are kept separate. A larger number only means a higher position **within the same leaderboard**; it does not mean that an OR of 1.8 is directly larger than a d of 0.6 or an r of 0.4.

Only syntheses classified as direct behavior outcomes enter these leaderboards. Intention, identity, habit-strength, and mixed composite outcomes are excluded until a valid behavior-specific estimate is available.

## Causal — standardized effects

| Rank | Mechanism | Effect | Outcome | Domain | Evidence size |
|---:|---|---:|---|---|---|
| 1 | [Punishment](mechanisms/punishment/) | d = 0.7 [0.6, 0.8] | cooperation | social dilemmas | k=126 |
| 2 | [Default options](mechanisms/default-options/) | d = 0.68 [0.53, 0.83] | uptake of preselected option / choice | consumer, environmental, health and other decisions | k=58, n=73675 |
| 3 | [Prompts and reminders](mechanisms/prompts-reminders/) | Hedges_g_model = 0.67 [0.44, 0.9] | pro-environmental behavior | pro-environmental behavior | k=114 |
| 4 | [Implementation intentions](mechanisms/implementation-intentions/) | d = 0.65 | goal attainment / behavior | multiple | k=94 |
| 5 | [Autonomous motivation](mechanisms/autonomous-motivation/) | d = 0.47 [0.32, 0.62] | behavior | health behaviors | k=18, n=5063 |
| 6 | [Self-efficacy](mechanisms/self-efficacy/) | d = 0.47 | behavior | health behaviors | — |
| 7 | [Behavioral attitudes](mechanisms/behavioral-attitudes/) | d = 0.38 | behavior | health behaviors | — |
| 8 | [Behavioral intentions](mechanisms/intentions/) | d = 0.36 | behavior | multiple | k=47 |
| 9 | [Social norms](mechanisms/social-norms/) | d = 0.36 | behavior | health behaviors | — |
| 10 | [Goal setting](mechanisms/goal-setting/) | d = 0.34 [0.28, 0.41] | behavior | multiple | k=384, n=16523 |
| 11 | [Perceived competence](mechanisms/perceived-competence/) | d = 0.34 [0.22, 0.47] | behavior | health behaviors | k=13, n=3667 |
| 12 | [Self-monitoring of behavior](mechanisms/self-monitoring/) | Hedges_g = 0.32 [0.14, 0.5] | reduced total sedentary time | sedentary behavior | k=19, n=2800 |
| 13 | [Risk appraisal](mechanisms/risk-appraisal/) | d = 0.23 | behavior | multiple health and risk behaviors | k=93 |

## Causal — odds ratios

| Rank | Mechanism | Effect | Outcome | Domain | Evidence size |
|---:|---|---:|---|---|---|
| 1 | [Affordability](mechanisms/affordability/) | OR = 1.87 [1.47, 2.4] | vaccination uptake | vaccination | k=223, n=6243118 |
| 2 | [Accessibility / convenience](mechanisms/accessibility/) | OR = 1.74 [1.35, 2.26] | vaccination uptake | vaccination | k=223, n=6243118 |
| 3 | [Social support](mechanisms/social-support/) | OR = 1.66 [1.24, 2.22] | antiretroviral therapy adherence | HIV treatment adherence | k=17, n=4110 |
| 4 | [Financial incentives](mechanisms/financial-incentives/) | OR = 1.53 [1.05, 2.23] | habitual health behavior change at up to 18 months | smoking, eating, alcohol, physical activity | k=34 |
| 5 | [Prompts and reminders](mechanisms/prompts-reminders/) | OR = 1.36 [1.22, 1.5] | vaccination uptake | vaccination | k=223, n=6243118 |
| 6 | [Education / information provision](mechanisms/education-information/) | OR = 1.33 [1.19, 1.49] | vaccination uptake | vaccination | k=223, n=6243118 |

## Causal — risk ratios

| Rank | Mechanism | Effect | Outcome | Domain | Evidence size |
|---:|---|---:|---|---|---|
| 1 | [Financial incentives](mechanisms/financial-incentives/) | RR = 1.62 [1.38, 1.91] | healthy behavior change | smoking, screening/vaccination, physical activity | k=16 |

## Prospective prediction — correlations

No eligible syntheses yet.

## Association — correlations

| Rank | Mechanism | Effect | Outcome | Domain | Evidence size |
|---:|---|---:|---|---|---|
| 1 | [Habit / behavioral automaticity](mechanisms/habit/) | r = 0.46 | behavior | nutrition, physical activity, active travel | k=23 |
| 2 | [Anticipated regret](mechanisms/anticipated-regret/) | r = 0.29 | health behavior | health behaviors | k=81, n=45618 |
| 3 | [Trust in healthcare professionals](mechanisms/trust-healthcare-professional/) | r = 0.14 [0.1, 0.19] | health behavior | clinical health behaviors | — |

## Excluded from direct-behavior ranking

These syntheses remain in the evidence base but are not allowed into the direct-behavior leaderboard.

| Mechanism | Effect | Outcome | Reason |
|---|---:|---|---|
| [Fear appeals](mechanisms/fear-appeals/) | d = 0.29 [0.22, 0.35] | attitude / intention / behavior composite | Primary effect combines attitude, intention, and behavior outcomes. |
| [Identity / self-identity](mechanisms/identity/) | r = 0.47 | behavioral intention | Outcome is behavioral intention, not behavior. |
| [Identity / self-identity](mechanisms/identity/) | r = 0.55 | habit strength | Outcome is habit strength, not behavior. |
| [Identity / self-identity](mechanisms/identity/) | Hedges_g = 0.18 | identity | Outcome is identity itself, not behavior. |

## Methodological status

This is Rank v0: a descriptive, metric-specific leaderboard. A publication-quality cross-metric rank still requires effect-size harmonization, overlap correction, risk-of-bias assessment, domain/replication handling, uncertainty-aware ranking, and sensitivity analysis.

Detailed rules: [protocol/ranking.md](protocol/ranking.md)
