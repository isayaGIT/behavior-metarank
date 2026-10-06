# Behavior MetaRank — Ranking 解读指南（中文）

> 本文件由当前 MetaRank 数据库和人工维护的双语机制词典自动生成，用来帮助人类读懂榜单，而不是只看一堆统计数字。

## 先看这三条

实时排名看 [RANKING.md](RANKING.md)。这份指南主要回答三个问题：系数是什么意思、每个机制到底是什么、排名不能被误读成什么。

最重要的三条规则：

1. **只能在同一个榜单内部比较名次。** OR、RR、d/g、r 不是同一种统计量。
2. **效应值更大，不等于在所有场景里都更值得用。** 行为领域、人群、基线概率、干预强度、研究质量、随访长度都可能不同。
3. **因果证据和相关性不能混为一谈。** 一个因素与行为高度相关，可能很适合预测，但不代表主动改变它就一定会造成行为改变。

## 证据层级怎么理解

| 层级 | 意思 | 能支持什么结论 |
|---|---|---|
| Causal 因果 | 通常来自随机或准随机的干预/操纵 | 当前最接近“改变这个东西，会不会改变行为” |
| Prospective 前瞻 | 先测因素，再观察未来行为 | 能支持时间顺序上的预测，但仍不一定是因果 |
| Association 相关 | 因素和行为一起变化 | 说明有关联或预测力，不能确定因果方向 |
| Mediation 中介 | 检验“干预先改变机制，机制再带来行为改变” | 最接近回答“这个干预到底为什么有效” |

## 系数怎么读

### r — 相关系数

- 范围是 -1 到 +1。
- 正数表示因素越高，结果通常也越高；负数表示反方向。
- 很粗略地，有时会把 .10 看成小、.30 看成中等、.50 看成较大，但具体领域差异很大。
- **r 不是百分比，也不能单靠它证明因果。**

### d / Hedges g — 标准化均值差

- 把组间差异换算成“标准差单位”。
- d = 0.50 可以理解为：两组在该结果上的平均差异大约是半个标准差。
- Hedges g 与 d 很接近，只是对小样本偏差做了修正。
- .20/.50/.80 常被当作小/中/大的粗略参考，但不是自然法则。
- **d = 0.70 绝对不是“提升了 70%”。**

### OR — Odds Ratio，优势比

- OR = 1 表示两组 odds 一样。
- OR > 1 表示干预/暴露组出现该结果的 odds 更高；OR < 1 则更低。
- OR = 1.87 表示 **odds 高 87%**，不是说发生概率一定高 87%。
- 当一个结果本身很常见时，OR 往往比直觉上的概率差异显得更大。

### RR — Risk Ratio / Relative Risk，相对风险

- RR = 1 表示两组发生概率相同。
- RR = 1.62 表示目标结果的相对发生概率是对照组的 1.62 倍，也就是相对高 62%。
- 但如果不知道基线概率，仍然不知道绝对增加了多少个百分点。

### 95% CI — 95% 置信区间

- CI 表示估计值的不确定范围。
- 对 r 和 d/g 来说，如果区间跨过 0，就包含传统意义上的“无效应值”。
- 对 OR 和 RR 来说，如果区间跨过 1，就包含传统意义上的“无效应值”。
- 区间更窄通常代表估计更精确，但仍然要考虑偏倚和研究质量。

### k 和 n

- n 通常是参与者人数。
- k 可能代表研究数、比较数或 effect size 数量，具体取决于原 meta-analysis。**不同论文里的 k 不一定完全是同一个概念**，所以跨机制比较 k 时要看 notes。

## 排名到底代表什么

一个名次只表示：**在当前已经被 MetaRank 收录、并且属于同一个统计榜单的证据里，它现在排在这个位置。** 它不是“人类行为机制的终极排名”。未来新增 meta-analysis、把某个大构念拆成子构念、换成更直接的 behavior outcome、或引入质量/不确定性权重后，排名都可能变化。

## 逐个机制解读

### 1. 可及性 / 便利性（Accessibility / convenience）

**通俗理解：** 通过减少距离、预约、配送、服务可获得性等现实阻碍，让目标行为更容易真正做出来。

**解读提醒：** 它讲的是“做不做得到、方不方便”，不是“贵不贵”。一个服务可以很便宜，但仍然很难获得。

**当前 MetaRank 证据：**

- **因果干预证据：** OR = 1.74 [1.35, 2.26] → vaccination uptake（vaccination）；k=223, n=6243118；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/accessibility/](mechanisms/accessibility/)

### 2. 可负担性（Affordability）

**通俗理解：** 降低执行某个行为或获得某项服务需要付出的直接金钱成本。

**解读提醒：** 它是“让行动更便宜”，不是“做了以后给你钱”；后者属于 financial incentives。

**当前 MetaRank 证据：**

- **因果干预证据：** OR = 1.87 [1.47, 2.4] → vaccination uptake（vaccination）；k=223, n=6243118；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/affordability/](mechanisms/affordability/)

### 3. 预期后悔（Anticipated regret）

**通俗理解：** 在做决定之前，先想到未来如果做了或没做这件事，自己可能会有多后悔。

**解读提醒：** MetaRank 目前收录的是相关性证据，因此它说明“有关联”，还不能直接说预期后悔本身造成了行为改变。

**当前 MetaRank 证据：**

- **相关性证据：** r = 0.29 → health behavior（health behaviors）；k=81, n=45618；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/anticipated-regret/](mechanisms/anticipated-regret/)

### 4. 自主性动机（Autonomous motivation）

**通俗理解：** 因为这件事是自己认同、主动选择、觉得有意义，所以愿意行动，而不是主要因为外界或内在压力逼着自己做。

**解读提醒：** 它强调的是“为什么想做”的动机质量，不等同于单纯的 intention 强弱。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.47 [0.32, 0.62] → behavior（health behaviors）；k=18, n=5063；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/autonomous-motivation/](mechanisms/autonomous-motivation/)

### 5. 行为态度（Behavioral attitudes）

**通俗理解：** 一个人觉得“做这个具体行为”到底是好还是坏、值得还是不值得、有益还是有害。

**解读提醒：** 这里指的是对具体行为本身的评价，不是对某个人、机构或话题的一般态度。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.38 → behavior（health behaviors）；—；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/behavioral-attitudes/](mechanisms/behavioral-attitudes/)

### 6. 行为意图（Behavioral intentions）

**通俗理解：** 一个人有意识地表达“我准备做、我打算做某个行为”的承诺或准备程度。

**解读提醒：** 想做不等于真的做。MetaRank 会把普通 intention 与 implementation intention 分开。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.36 → behavior（multiple）；k=47；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/intentions/](mechanisms/intentions/)

### 7. 默认选项（Default options）

**通俗理解：** 预先替人选好一个选项；如果对方不主动修改，就自动采用这个选择。

**解读提醒：** 默认选项属于 choice architecture。效果会受到场景、默认选项代表的含义以及退出成本影响。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.68 [0.53, 0.83] → uptake of preselected option / choice（consumer, environmental, health and other decisions）；k=58, n=73675；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/default-options/](mechanisms/default-options/)

### 8. 教育 / 信息提供（Education / information provision）

**通俗理解：** 给人提供事实、解释或教育材料，让其更了解目标行为以及相关选择。

**解读提醒：** “提供信息的干预有效”不等于已经证明“知识增加”就是导致行为改变的那个中介机制。

**当前 MetaRank 证据：**

- **因果干预证据：** OR = 1.33 [1.19, 1.49] → vaccination uptake（vaccination）；k=223, n=6243118；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/education-information/](mechanisms/education-information/)

### 9. 恐惧诉求（Fear appeals）

**通俗理解：** 通过强调威胁、危险或令人害怕的后果，试图推动人采取行动。

**解读提醒：** MetaRank 当前这条效应把态度、意图和行为混合在一起，所以没有进入 direct-behavior 排名。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.29 [0.22, 0.35] → attitude / intention / behavior composite（predominantly health and safety behaviors）；k=248, n=27372；不进入 direct-behavior 排名：Primary effect combines attitude, intention, and behavior outcomes.。
- 机制原始资料目录：[mechanisms/fear-appeals/](mechanisms/fear-appeals/)

### 10. 金钱激励（Financial incentives）

**通俗理解：** 把金钱或具有货币价值的奖励与目标行为或目标结果绑定：做到了，就获得奖励。

**解读提醒：** 激励停止以后效果可能减弱；而且 OR/RR 不能直接和 d 或 r 比数字大小。

**当前 MetaRank 证据：**

- **因果干预证据：** RR = 1.62 [1.38, 1.91] → healthy behavior change（smoking, screening/vaccination, physical activity）；k=16；可进入 direct-behavior 排名。
- **因果干预证据：** OR = 1.53 [1.05, 2.23] → habitual health behavior change at up to 18 months（smoking, eating, alcohol, physical activity）；k=34；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/financial-incentives/](mechanisms/financial-incentives/)

### 11. 目标设定（Goal setting）

**通俗理解：** 明确一个要达到的具体标准，例如行为次数、数量、时间或结果目标。

**解读提醒：** Goal setting 主要回答“我要达到什么”；它不等于 implementation intention 那种“如果 X 出现，我就做 Y”的执行规则。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.34 [0.28, 0.41] → behavior（multiple）；k=384, n=16523；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/goal-setting/](mechanisms/goal-setting/)

### 12. 习惯 / 行为自动化（Habit / behavioral automaticity）

**通俗理解：** 同一个行为在相似情境或线索下反复发生后，逐渐变成不用太多思考就会自动触发的反应。

**解读提醒：** 目前进入的是相关性榜单。习惯可能推动未来行为，但习惯强度本身也可能反映过去已经重复过很多次的行为。

**当前 MetaRank 证据：**

- **相关性证据：** r = 0.46 → behavior（nutrition, physical activity, active travel）；k=23；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/habit/](mechanisms/habit/)

### 13. 身份认同 / 自我身份（Identity / self-identity）

**通俗理解：** 把某种行为、角色或目标纳入“我是谁”的自我概念，例如不是只说“我想运动”，而是“我是一个会运动的人”。

**解读提醒：** 目前仓库里有 identity→intention、identity→habit，以及 intervention→identity 的证据，但还没有一条合格的 identity→behavior 直接效应进入榜单。

**当前 MetaRank 证据：**

- **相关性证据：** r = 0.47 → behavioral intention（multiple）；k=40, n=11607；不进入 direct-behavior 排名：Outcome is behavioral intention, not behavior.。
- **相关性证据：** r = 0.55 → habit strength（health behaviors）；n=13340；不进入 direct-behavior 排名：Outcome is habit strength, not behavior.。
- **因果干预证据：** Hedges_g = 0.18 → identity（physical activity）；k=40, n=4939；不进入 direct-behavior 排名：Outcome is identity itself, not behavior.。
- 机制原始资料目录：[mechanisms/identity/](mechanisms/identity/)

### 14. 执行意图 / If–Then 计划（Implementation intentions）

**通俗理解：** 把一个具体线索和一个具体行动绑定成规则：“如果 X 出现，那么我就做 Y。”

**解读提醒：** 它比普通 intention 更具体：不仅想做，而且提前规定在什么线索出现时执行什么动作。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.65 → goal attainment / behavior（multiple）；k=94；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/implementation-intentions/](mechanisms/implementation-intentions/)

### 15. 感知胜任感（Perceived competence）

**通俗理解：** 一个人觉得自己在执行某个目标行为时是有能力、有效率、做得到的。

**解读提醒：** 它与 self-efficacy 很接近，但理论来源和测量传统并不完全相同，因此 MetaRank 暂时不把两者直接合并。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.34 [0.22, 0.47] → behavior（health behaviors）；k=13, n=3667；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/perceived-competence/](mechanisms/perceived-competence/)

### 16. 提示与提醒（Prompts and reminders）

**通俗理解：** 在行动机会出现时给一个外部线索，让目标行为重新进入注意力，例如通知、提示牌、短信提醒。

**解读提醒：** 提醒主要改变当下的注意力和显著性；它不同于教育信息，也不同于自己预先写好的 if–then 计划。

**当前 MetaRank 证据：**

- **因果干预证据：** Hedges_g_model = 0.67 [0.44, 0.9] → pro-environmental behavior（pro-environmental behavior）；k=114；可进入 direct-behavior 排名。
- **因果干预证据：** OR = 1.36 [1.22, 1.5] → vaccination uptake（vaccination）；k=223, n=6243118；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/prompts-reminders/](mechanisms/prompts-reminders/)

### 17. 惩罚（Punishment）

**通俗理解：** 把负面后果与不合作或不希望出现的行为绑定，使该行为需要付出代价。

**解读提醒：** 当前排名较高的证据主要来自实验室 social dilemma；不能直接外推到法律处罚，更不能理解成“对自己越狠越有效”。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.7 [0.6, 0.8] → cooperation（social dilemmas）；k=126；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/punishment/](mechanisms/punishment/)

### 18. 风险评估（Risk appraisal）

**通俗理解：** 在行动前判断某种风险有多可能发生、后果有多严重，以及这个风险对自己意味着什么。

**解读提醒：** Risk appraisal 是人的心理判断；fear appeal 是一种试图改变这种判断或情绪的沟通干预，两者不是同一个东西。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.23 → behavior（multiple health and risk behaviors）；k=93；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/risk-appraisal/](mechanisms/risk-appraisal/)

### 19. 自我效能（Self-efficacy）

**通俗理解：** 相信自己有能力把目标行为需要的具体动作真正执行出来。

**解读提醒：** Self-efficacy 是针对具体任务的能力信念，不等于一般性的自信、自尊或“积极想一想”。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.47 → behavior（health behaviors）；—；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/self-efficacy/](mechanisms/self-efficacy/)

### 20. 行为自我监测（Self-monitoring of behavior）

**通俗理解：** 记录、观察自己的真实行为，让“我到底做了多少、什么时候做”变得可见，从而便于调整。

**解读提醒：** 很多 self-monitoring 研究同时包含其他干预成分，所以随机试验能证明整个方案有效，不一定能完全拆出“记录本身”的独立因果效应。

**当前 MetaRank 证据：**

- **因果干预证据：** Hedges_g = 0.32 [0.14, 0.5] → reduced total sedentary time（sedentary behavior）；k=19, n=2800；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/self-monitoring/](mechanisms/self-monitoring/)

### 21. 社会规范（Social norms）

**通俗理解：** 一个人对“别人通常怎么做”或者“别人认为应该怎么做”的感知。

**解读提醒：** 描述性规范（别人实际怎么做）和命令性规范（别人赞成什么）可能并不相同，未来可能会在 MetaRank 里拆成两个机制。

**当前 MetaRank 证据：**

- **因果干预证据：** d = 0.36 → behavior（health behaviors）；—；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/social-norms/](mechanisms/social-norms/)

### 22. 社会支持（Social support）

**通俗理解：** 从他人那里得到实际帮助、信息、情绪支持或物质资源，让目标行为更容易完成。

**解读提醒：** 当前因果估计来自 HIV 治疗依从性，不能直接当成“社会支持对所有行为都有同样大小的效果”。

**当前 MetaRank 证据：**

- **因果干预证据：** OR = 1.66 [1.24, 2.22] → antiretroviral therapy adherence（HIV treatment adherence）；k=17, n=4110；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/social-support/](mechanisms/social-support/)

### 23. 对医疗专业人员的信任（Trust in healthcare professionals）

**通俗理解：** 相信医生或其他医疗专业人员有能力、诚实，并且会以患者利益为出发点。

**解读提醒：** 当前是相关性证据，而且针对临床关系；它不等于一般社会信任或对机构制度的信任。

**当前 MetaRank 证据：**

- **相关性证据：** r = 0.14 [0.1, 0.19] → health behavior（clinical health behaviors）；—；可进入 direct-behavior 排名。
- 机制原始资料目录：[mechanisms/trust-healthcare-professional/](mechanisms/trust-healthcare-professional/)

## 最后怎么用这个项目

最有价值的用法是把两个问题分开问：**什么东西和行为关系最强？** 以及 **什么东西被主动改变以后，最有证据会造成行为改变？** 这是两个不同的排行榜。MetaRank 现在就是故意不把它们混成一个分数。
