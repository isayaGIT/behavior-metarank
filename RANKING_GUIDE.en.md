# Behavior MetaRank — Ranking Interpretation Guide

> Human-readable guide generated from the live MetaRank evidence base and the curated bilingual mechanism glossary.

## Quick start

Use [RANKING.md](RANKING.md) for the live leaderboards. Use this guide to understand what the coefficients mean, what each mechanism means, and what you should **not** infer from the ranking.

Three rules matter most:

1. **Compare ranks only inside the same leaderboard.** An OR, RR, d/g, and r are different statistical quantities.
2. **A larger effect estimate is not automatically a universally better intervention.** Domains, populations, baseline rates, intervention intensity, study quality, and follow-up differ.
3. **Causal evidence and association are not interchangeable.** A strong correlation can be useful for prediction without proving that changing the factor will change behavior.

## Evidence layers

| Layer | Meaning | What it can support |
|---|---|---|
| Causal | Usually randomized or quasi-experimental manipulation/intervention evidence | Strongest basis here for asking whether changing something changes behavior |
| Prospective | The factor is measured before later behavior | Temporal prediction; stronger than cross-sectional association, but not necessarily causal |
| Association | The factor and behavior vary together | Relationship/prediction, not causal direction |
| Mediation | Tests whether an intervention changes a mechanism and that mechanism carries change into behavior | Closest to identifying *how* an intervention works |

## How to read the coefficients

### r — correlation

- Range: -1 to +1.
- Positive values mean higher levels of the factor tend to occur with more of the outcome; negative values mean the opposite.
- Very rough conventions sometimes call around .10 small, .30 moderate, and .50 large, but context matters.
- **r is not a percentage and does not by itself establish causation.**

### d / Hedges g — standardized mean difference

- Expresses a difference between groups in standard-deviation units.
- d = 0.50 means the groups differ by about half a standard deviation on the coded outcome.
- Hedges g is a closely related standardized effect with a small-sample correction.
- Rough conventions of .20/.50/.80 as small/moderate/large can be useful orientation, not universal cutoffs.
- **d = 0.70 does not mean a 70% improvement.**

### OR — odds ratio

- OR = 1 means equal odds between groups.
- OR > 1 means higher odds of the outcome in the intervention/exposed group; OR < 1 means lower odds.
- OR = 1.87 means the **odds** are 87% higher, not necessarily that the probability is 87% higher.
- Odds ratios can look larger than probability differences when the outcome is common.

### RR — risk ratio / relative risk

- RR = 1 means equal probability/risk.
- RR = 1.62 means the outcome probability is 1.62 times the comparison group, i.e. 62% higher on a relative scale.
- RR is usually easier to interpret than OR, but still does not tell you the absolute probability change without a baseline rate.

### 95% confidence interval (CI)

- The CI shows uncertainty around the estimate.
- For r and d/g, an interval crossing 0 includes the conventional no-effect value.
- For OR and RR, an interval crossing 1 includes the conventional no-effect value.
- Narrower intervals usually mean more precision, but quality and bias still matter.

### k and n

- n is the participant count when available.
- k is the number of studies, comparisons, or effect sizes as reported by the source synthesis. Its exact meaning can vary by meta-analysis, so inspect the row notes before comparing k across mechanisms.

## How to interpret a rank

A rank is a **position among the evidence currently ingested into that specific leaderboard**, not a universal truth about human behavior. Rank #1 can change when new meta-analyses are added, when a construct is split, when a better behavior-specific estimate replaces a composite outcome, or when MetaRank later introduces quality/uncertainty weighting.

## Mechanism guide

### 1. Accessibility / convenience

**Plain meaning:** Make the behavior easier to carry out by removing practical barriers such as distance, scheduling, delivery friction, or service availability.

**Interpretation caution:** This is about practical access, not price. A service can be affordable but still difficult to reach.

**Current MetaRank evidence:**

- **Causal intervention evidence:** OR = 1.74 [1.35, 2.26] → vaccination uptake (vaccination); k=223, n=6243118; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/accessibility/](mechanisms/accessibility/)

### 2. Affordability

**Plain meaning:** Reduce the money someone must spend to perform a behavior or obtain a service.

**Interpretation caution:** Affordability reduces the cost of acting; it is different from paying someone a reward for acting.

**Current MetaRank evidence:**

- **Causal intervention evidence:** OR = 1.87 [1.47, 2.4] → vaccination uptake (vaccination); k=223, n=6243118; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/affordability/](mechanisms/affordability/)

### 3. Anticipated regret

**Plain meaning:** Before deciding, imagine how much you might regret doing—or not doing—the behavior later.

**Interpretation caution:** The current MetaRank evidence is correlational, so it shows association rather than proven causal leverage.

**Current MetaRank evidence:**

- **Association:** r = 0.29 → health behavior (health behaviors); k=81, n=45618; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/anticipated-regret/](mechanisms/anticipated-regret/)

### 4. Autonomous motivation

**Plain meaning:** Act because the goal feels personally chosen, meaningful, or aligned with your values—not mainly because of pressure.

**Interpretation caution:** This is motivation quality, not simply how strongly you intend to act.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.47 [0.32, 0.62] → behavior (health behaviors); k=18, n=5063; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/autonomous-motivation/](mechanisms/autonomous-motivation/)

### 5. Behavioral attitudes

**Plain meaning:** How positively or negatively a person evaluates doing the specific behavior—whether it seems good, useful, worthwhile, pleasant, or harmful.

**Interpretation caution:** This is attitude toward the behavior itself, not a broad attitude toward a person, institution, or topic.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.38 → behavior (health behaviors); —; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/behavioral-attitudes/](mechanisms/behavioral-attitudes/)

### 6. Behavioral intentions

**Plain meaning:** A conscious commitment or stated readiness to perform a behavior.

**Interpretation caution:** Wanting or intending to act is not identical to acting; MetaRank keeps intention effects separate from implementation-intention effects.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.36 → behavior (multiple); k=47; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/intentions/](mechanisms/intentions/)

### 7. Default options

**Plain meaning:** Preselect one option so it happens automatically unless the person actively changes it.

**Interpretation caution:** Defaults are a choice-architecture intervention. Their effect can depend heavily on context and on what the default signals.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.68 [0.53, 0.83] → uptake of preselected option / choice (consumer, environmental, health and other decisions); k=58, n=73675; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/default-options/](mechanisms/default-options/)

### 8. Education / information provision

**Plain meaning:** Give people facts, explanations, or educational material that may help them make or carry out a behavioral choice.

**Interpretation caution:** An education intervention is not the same as proving that measured knowledge is the causal mediator.

**Current MetaRank evidence:**

- **Causal intervention evidence:** OR = 1.33 [1.19, 1.49] → vaccination uptake (vaccination); k=223, n=6243118; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/education-information/](mechanisms/education-information/)

### 9. Fear appeals

**Plain meaning:** Use messages that deliberately emphasize threat or frightening consequences in order to motivate action.

**Interpretation caution:** The current effect in MetaRank combines attitudes, intentions, and behavior, so it is excluded from the direct-behavior leaderboard.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.29 [0.22, 0.35] → attitude / intention / behavior composite (predominantly health and safety behaviors); k=248, n=27372; excluded from direct-behavior ranking: Primary effect combines attitude, intention, and behavior outcomes..
- Mechanism source folder: [mechanisms/fear-appeals/](mechanisms/fear-appeals/)

### 10. Financial incentives

**Plain meaning:** Offer money or another material financial reward contingent on performing the target behavior or reaching an outcome.

**Interpretation caution:** Effects may weaken after incentives stop, and OR/RR estimates should not be compared numerically with d or r.

**Current MetaRank evidence:**

- **Causal intervention evidence:** RR = 1.62 [1.38, 1.91] → healthy behavior change (smoking, screening/vaccination, physical activity); k=16; eligible for direct-behavior ranking.
- **Causal intervention evidence:** OR = 1.53 [1.05, 2.23] → habitual health behavior change at up to 18 months (smoking, eating, alcohol, physical activity); k=34; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/financial-incentives/](mechanisms/financial-incentives/)

### 11. Goal setting

**Plain meaning:** Specify a concrete target or standard to work toward, such as a behavioral amount, frequency, or outcome.

**Interpretation caution:** A goal says what you want to achieve; it does not by itself specify the cue-response plan used in implementation intentions.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.34 [0.28, 0.41] → behavior (multiple); k=384, n=16523; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/goal-setting/](mechanisms/goal-setting/)

### 12. Habit / behavioral automaticity

**Plain meaning:** A behavior becomes increasingly automatic because the same response has been repeated in recurring contexts or cues.

**Interpretation caution:** The current rank is association-only; habit may both influence behavior and partly reflect repeated past behavior.

**Current MetaRank evidence:**

- **Association:** r = 0.46 → behavior (nutrition, physical activity, active travel); k=23; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/habit/](mechanisms/habit/)

### 13. Identity / self-identity

**Plain meaning:** Represent a behavior, role, or goal as part of who you are—for example, “I am someone who exercises” rather than only “I want to exercise.”

**Interpretation caution:** MetaRank currently has identity-to-intention, identity-to-habit, and intervention-to-identity evidence, but no eligible direct identity-to-behavior effect in the leaderboard yet.

**Current MetaRank evidence:**

- **Association:** r = 0.47 → behavioral intention (multiple); k=40, n=11607; excluded from direct-behavior ranking: Outcome is behavioral intention, not behavior..
- **Association:** r = 0.55 → habit strength (health behaviors); n=13340; excluded from direct-behavior ranking: Outcome is habit strength, not behavior..
- **Causal intervention evidence:** Hedges_g = 0.18 → identity (physical activity); k=40, n=4939; excluded from direct-behavior ranking: Outcome is identity itself, not behavior..
- Mechanism source folder: [mechanisms/identity/](mechanisms/identity/)

### 14. Implementation intentions

**Plain meaning:** Create an if–then rule that links a specific cue to a specific response: “If X happens, then I will do Y.”

**Interpretation caution:** This is more specific than ordinary intention; it programs when or under what cue the behavior should occur.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.65 → goal attainment / behavior (multiple); k=94; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/implementation-intentions/](mechanisms/implementation-intentions/)

### 15. Perceived competence

**Plain meaning:** The feeling that you are effective and capable at carrying out the target behavior.

**Interpretation caution:** It overlaps with self-efficacy but comes from a different theoretical tradition; MetaRank does not pool them automatically.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.34 [0.22, 0.47] → behavior (health behaviors); k=13, n=3667; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/perceived-competence/](mechanisms/perceived-competence/)

### 16. Prompts and reminders

**Plain meaning:** Place an external cue at the right moment so the intended behavior comes back into attention.

**Interpretation caution:** A reminder changes salience at the moment of action; it is different from teaching new information or creating an internal if–then plan.

**Current MetaRank evidence:**

- **Causal intervention evidence:** Hedges_g_model = 0.67 [0.44, 0.9] → pro-environmental behavior (pro-environmental behavior); k=114; eligible for direct-behavior ranking.
- **Causal intervention evidence:** OR = 1.36 [1.22, 1.5] → vaccination uptake (vaccination); k=223, n=6243118; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/prompts-reminders/](mechanisms/prompts-reminders/)

### 17. Punishment

**Plain meaning:** Attach a negative consequence to noncooperation or an undesired behavior.

**Interpretation caution:** The current high-ranked estimate comes from experimental social dilemmas; it should not be generalized directly to legal punishment or everyday self-punishment.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.7 [0.6, 0.8] → cooperation (social dilemmas); k=126; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/punishment/](mechanisms/punishment/)

### 18. Risk appraisal

**Plain meaning:** Assess how likely and how serious a threat or harmful outcome seems before deciding what to do.

**Interpretation caution:** Risk appraisal is the psychological appraisal itself; fear appeals are messages designed to change such appraisals or emotions.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.23 → behavior (multiple health and risk behaviors); k=93; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/risk-appraisal/](mechanisms/risk-appraisal/)

### 19. Self-efficacy

**Plain meaning:** Believe that you can successfully execute the specific actions required by the target behavior.

**Interpretation caution:** Self-efficacy is task-specific capability belief, not generic self-esteem or positive thinking.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.47 → behavior (health behaviors); —; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/self-efficacy/](mechanisms/self-efficacy/)

### 20. Self-monitoring of behavior

**Plain meaning:** Track or record your own behavior so that what you are actually doing becomes visible and can be regulated.

**Interpretation caution:** Many self-monitoring interventions are multicomponent, so the causal effect of self-monitoring alone can be less certain than the trial-level intervention effect.

**Current MetaRank evidence:**

- **Causal intervention evidence:** Hedges_g = 0.32 [0.14, 0.5] → reduced total sedentary time (sedentary behavior); k=19, n=2800; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/self-monitoring/](mechanisms/self-monitoring/)

### 21. Social norms

**Plain meaning:** Perceptions about what other people do or what other people approve of.

**Interpretation caution:** Descriptive norms (what others do) and injunctive norms (what others approve) may differ and may later be split into separate MetaRank mechanisms.

**Current MetaRank evidence:**

- **Causal intervention evidence:** d = 0.36 → behavior (health behaviors); —; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/social-norms/](mechanisms/social-norms/)

### 22. Social support

**Plain meaning:** Receive practical, informational, emotional, or tangible help from other people that makes the target behavior easier to carry out.

**Interpretation caution:** The current causal estimate is domain-specific to HIV treatment adherence, so it is not a universal social-support effect.

**Current MetaRank evidence:**

- **Causal intervention evidence:** OR = 1.66 [1.24, 2.22] → antiretroviral therapy adherence (HIV treatment adherence); k=17, n=4110; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/social-support/](mechanisms/social-support/)

### 23. Trust in healthcare professionals

**Plain meaning:** Trust that a clinician or healthcare professional is competent, honest, and acting in the patient's interest.

**Interpretation caution:** Current evidence is correlational and specific to clinical relationships; it is not the same as generalized or institutional trust.

**Current MetaRank evidence:**

- **Association:** r = 0.14 [0.1, 0.19] → health behavior (clinical health behaviors); —; eligible for direct-behavior ranking.
- Mechanism source folder: [mechanisms/trust-healthcare-professional/](mechanisms/trust-healthcare-professional/)

## Bottom line

MetaRank is most useful when you ask two separate questions: **What is strongly associated with behavior?** and **What has strong evidence that changing it changes behavior?** Those are different rankings. The project intentionally preserves that distinction.
