#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "generated" / "evidence_matrix.csv"
MECHANISMS = ROOT / "generated" / "mechanisms.json"
GLOSSARY = ROOT / "content" / "mechanism-glossary.json"
OUT_EN = ROOT / "RANKING_GUIDE.en.md"
OUT_ZH = ROOT / "RANKING_GUIDE.zh-CN.md"

def clean(x) -> str:
    return str(x if x is not None else "").replace("|", "\\|").replace("\n", " ").strip()

def effect_text(r: dict[str, str]) -> str:
    metric = clean(r.get("effect_metric", ""))
    value = clean(r.get("effect_value", ""))
    lo = clean(r.get("ci_low", ""))
    hi = clean(r.get("ci_high", ""))
    if lo and hi:
        return f"{metric} = {value} [{lo}, {hi}]"
    return f"{metric} = {value}"

def evidence_size(r: dict[str, str]) -> str:
    parts = []
    if clean(r.get("k", "")):
        parts.append(f"k={clean(r['k'])}")
    if clean(r.get("n", "")):
        parts.append(f"n={clean(r['n'])}")
    return ", ".join(parts) if parts else "—"

with MATRIX.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
mechanisms = json.loads(MECHANISMS.read_text(encoding="utf-8"))
glossary = json.loads(GLOSSARY.read_text(encoding="utf-8"))

mechanism_ids = {m["id"] for m in mechanisms}
missing = sorted(mechanism_ids - set(glossary))
if missing:
    raise SystemExit(f"Missing bilingual glossary entries: {missing}")

by_mechanism = defaultdict(list)
for r in rows:
    by_mechanism[r["mechanism_id"]].append(r)

layer_en = {
    "causal": "Causal intervention evidence",
    "prospective": "Prospective prediction",
    "association": "Association",
    "mediation": "Mediation",
}
layer_zh = {
    "causal": "因果干预证据",
    "prospective": "前瞻预测证据",
    "association": "相关性证据",
    "mediation": "中介机制证据",
}

en = [
"# Behavior MetaRank — Ranking Interpretation Guide",
"",
"> Human-readable guide generated from the live MetaRank evidence base and the curated bilingual mechanism glossary.",
"",
"## Quick start",
"",
"Use [RANKING.md](RANKING.md) for the live leaderboards. Use this guide to understand what the coefficients mean, what each mechanism means, and what you should **not** infer from the ranking.",
"",
"Three rules matter most:",
"",
"1. **Compare ranks only inside the same leaderboard.** An OR, RR, d/g, and r are different statistical quantities.",
"2. **A larger effect estimate is not automatically a universally better intervention.** Domains, populations, baseline rates, intervention intensity, study quality, and follow-up differ.",
"3. **Causal evidence and association are not interchangeable.** A strong correlation can be useful for prediction without proving that changing the factor will change behavior.",
"",
"## Evidence layers",
"",
"| Layer | Meaning | What it can support |",
"|---|---|---|",
"| Causal | Usually randomized or quasi-experimental manipulation/intervention evidence | Strongest basis here for asking whether changing something changes behavior |",
"| Prospective | The factor is measured before later behavior | Temporal prediction; stronger than cross-sectional association, but not necessarily causal |",
"| Association | The factor and behavior vary together | Relationship/prediction, not causal direction |",
"| Mediation | Tests whether an intervention changes a mechanism and that mechanism carries change into behavior | Closest to identifying *how* an intervention works |",
"",
"## How to read the coefficients",
"",
"### r — correlation",
"",
"- Range: -1 to +1.",
"- Positive values mean higher levels of the factor tend to occur with more of the outcome; negative values mean the opposite.",
"- Very rough conventions sometimes call around .10 small, .30 moderate, and .50 large, but context matters.",
"- **r is not a percentage and does not by itself establish causation.**",
"",
"### d / Hedges g — standardized mean difference",
"",
"- Expresses a difference between groups in standard-deviation units.",
"- d = 0.50 means the groups differ by about half a standard deviation on the coded outcome.",
"- Hedges g is a closely related standardized effect with a small-sample correction.",
"- Rough conventions of .20/.50/.80 as small/moderate/large can be useful orientation, not universal cutoffs.",
"- **d = 0.70 does not mean a 70% improvement.**",
"",
"### OR — odds ratio",
"",
"- OR = 1 means equal odds between groups.",
"- OR > 1 means higher odds of the outcome in the intervention/exposed group; OR < 1 means lower odds.",
"- OR = 1.87 means the **odds** are 87% higher, not necessarily that the probability is 87% higher.",
"- Odds ratios can look larger than probability differences when the outcome is common.",
"",
"### RR — risk ratio / relative risk",
"",
"- RR = 1 means equal probability/risk.",
"- RR = 1.62 means the outcome probability is 1.62 times the comparison group, i.e. 62% higher on a relative scale.",
"- RR is usually easier to interpret than OR, but still does not tell you the absolute probability change without a baseline rate.",
"",
"### 95% confidence interval (CI)",
"",
"- The CI shows uncertainty around the estimate.",
"- For r and d/g, an interval crossing 0 includes the conventional no-effect value.",
"- For OR and RR, an interval crossing 1 includes the conventional no-effect value.",
"- Narrower intervals usually mean more precision, but quality and bias still matter.",
"",
"### k and n",
"",
"- n is the participant count when available.",
"- k is the number of studies, comparisons, or effect sizes as reported by the source synthesis. Its exact meaning can vary by meta-analysis, so inspect the row notes before comparing k across mechanisms.",
"",
"## How to interpret a rank",
"",
"A rank is a **position among the evidence currently ingested into that specific leaderboard**, not a universal truth about human behavior. Rank #1 can change when new meta-analyses are added, when a construct is split, when a better behavior-specific estimate replaces a composite outcome, or when MetaRank later introduces quality/uncertainty weighting.",
"",
"## Mechanism guide",
"",
]

zh = [
"# Behavior MetaRank — Ranking 解读指南（中文）",
"",
"> 本文件由当前 MetaRank 数据库和人工维护的双语机制词典自动生成，用来帮助人类读懂榜单，而不是只看一堆统计数字。",
"",
"## 先看这三条",
"",
"实时排名看 [RANKING.md](RANKING.md)。这份指南主要回答三个问题：系数是什么意思、每个机制到底是什么、排名不能被误读成什么。",
"",
"最重要的三条规则：",
"",
"1. **只能在同一个榜单内部比较名次。** OR、RR、d/g、r 不是同一种统计量。",
"2. **效应值更大，不等于在所有场景里都更值得用。** 行为领域、人群、基线概率、干预强度、研究质量、随访长度都可能不同。",
"3. **因果证据和相关性不能混为一谈。** 一个因素与行为高度相关，可能很适合预测，但不代表主动改变它就一定会造成行为改变。",
"",
"## 证据层级怎么理解",
"",
"| 层级 | 意思 | 能支持什么结论 |",
"|---|---|---|",
"| Causal 因果 | 通常来自随机或准随机的干预/操纵 | 当前最接近“改变这个东西，会不会改变行为” |",
"| Prospective 前瞻 | 先测因素，再观察未来行为 | 能支持时间顺序上的预测，但仍不一定是因果 |",
"| Association 相关 | 因素和行为一起变化 | 说明有关联或预测力，不能确定因果方向 |",
"| Mediation 中介 | 检验“干预先改变机制，机制再带来行为改变” | 最接近回答“这个干预到底为什么有效” |",
"",
"## 系数怎么读",
"",
"### r — 相关系数",
"",
"- 范围是 -1 到 +1。",
"- 正数表示因素越高，结果通常也越高；负数表示反方向。",
"- 很粗略地，有时会把 .10 看成小、.30 看成中等、.50 看成较大，但具体领域差异很大。",
"- **r 不是百分比，也不能单靠它证明因果。**",
"",
"### d / Hedges g — 标准化均值差",
"",
"- 把组间差异换算成“标准差单位”。",
"- d = 0.50 可以理解为：两组在该结果上的平均差异大约是半个标准差。",
"- Hedges g 与 d 很接近，只是对小样本偏差做了修正。",
"- .20/.50/.80 常被当作小/中/大的粗略参考，但不是自然法则。",
"- **d = 0.70 绝对不是“提升了 70%”。**",
"",
"### OR — Odds Ratio，优势比",
"",
"- OR = 1 表示两组 odds 一样。",
"- OR > 1 表示干预/暴露组出现该结果的 odds 更高；OR < 1 则更低。",
"- OR = 1.87 表示 **odds 高 87%**，不是说发生概率一定高 87%。",
"- 当一个结果本身很常见时，OR 往往比直觉上的概率差异显得更大。",
"",
"### RR — Risk Ratio / Relative Risk，相对风险",
"",
"- RR = 1 表示两组发生概率相同。",
"- RR = 1.62 表示目标结果的相对发生概率是对照组的 1.62 倍，也就是相对高 62%。",
"- 但如果不知道基线概率，仍然不知道绝对增加了多少个百分点。",
"",
"### 95% CI — 95% 置信区间",
"",
"- CI 表示估计值的不确定范围。",
"- 对 r 和 d/g 来说，如果区间跨过 0，就包含传统意义上的“无效应值”。",
"- 对 OR 和 RR 来说，如果区间跨过 1，就包含传统意义上的“无效应值”。",
"- 区间更窄通常代表估计更精确，但仍然要考虑偏倚和研究质量。",
"",
"### k 和 n",
"",
"- n 通常是参与者人数。",
"- k 可能代表研究数、比较数或 effect size 数量，具体取决于原 meta-analysis。**不同论文里的 k 不一定完全是同一个概念**，所以跨机制比较 k 时要看 notes。",
"",
"## 排名到底代表什么",
"",
"一个名次只表示：**在当前已经被 MetaRank 收录、并且属于同一个统计榜单的证据里，它现在排在这个位置。** 它不是“人类行为机制的终极排名”。未来新增 meta-analysis、把某个大构念拆成子构念、换成更直接的 behavior outcome、或引入质量/不确定性权重后，排名都可能变化。",
"",
"## 逐个机制解读",
"",
]

for idx, mechanism in enumerate(sorted(mechanisms, key=lambda m: m["name"].lower()), 1):
    mid = mechanism["id"]
    g = glossary[mid]
    mech_rows = by_mechanism.get(mid, [])

    en += [
        f"### {idx}. {g['en_name']}",
        "",
        f"**Plain meaning:** {g['en_plain']}",
        "",
        f"**Interpretation caution:** {g['en_caution']}",
        "",
        "**Current MetaRank evidence:**",
        "",
    ]
    zh += [
        f"### {idx}. {g['zh_name']}（{g['en_name']}）",
        "",
        f"**通俗理解：** {g['zh_plain']}",
        "",
        f"**解读提醒：** {g['zh_caution']}",
        "",
        "**当前 MetaRank 证据：**",
        "",
    ]

    if not mech_rows:
        en += ["- No synthesis currently ingested.", ""]
        zh += ["- 当前还没有已收录的 synthesis。", ""]
        continue

    for r in mech_rows:
        eligible = str(r.get("rank_eligible", "")).lower() in {"true","1","yes"}
        en_status = "eligible for direct-behavior ranking" if eligible else f"excluded from direct-behavior ranking: {clean(r.get('rank_exclusion_reason',''))}"
        zh_status = "可进入 direct-behavior 排名" if eligible else f"不进入 direct-behavior 排名：{clean(r.get('rank_exclusion_reason',''))}"
        en.append(
            f"- **{layer_en.get(r['layer'], r['layer'])}:** {effect_text(r)} → "
            f"{clean(r['outcome'])} ({clean(r['behavior_domain'])}); "
            f"{evidence_size(r)}; {en_status}."
        )
        zh.append(
            f"- **{layer_zh.get(r['layer'], r['layer'])}：** {effect_text(r)} → "
            f"{clean(r['outcome'])}（{clean(r['behavior_domain'])}）；"
            f"{evidence_size(r)}；{zh_status}。"
        )

    en += [f"- Mechanism source folder: [mechanisms/{mid}/](mechanisms/{mid}/)", ""]
    zh += [f"- 机制原始资料目录：[mechanisms/{mid}/](mechanisms/{mid}/)", ""]

en += [
"## Bottom line",
"",
"MetaRank is most useful when you ask two separate questions: **What is strongly associated with behavior?** and **What has strong evidence that changing it changes behavior?** Those are different rankings. The project intentionally preserves that distinction.",
"",
]
zh += [
"## 最后怎么用这个项目",
"",
"最有价值的用法是把两个问题分开问：**什么东西和行为关系最强？** 以及 **什么东西被主动改变以后，最有证据会造成行为改变？** 这是两个不同的排行榜。MetaRank 现在就是故意不把它们混成一个分数。",
"",
]

OUT_EN.write_text("\n".join(en), encoding="utf-8")
OUT_ZH.write_text("\n".join(zh), encoding="utf-8")
print(f"Wrote {OUT_EN.name} and {OUT_ZH.name} for {len(mechanisms)} mechanisms.")
