# Construct clustering protocol

Behavior MetaRank uses **research-driven clustering**, not a closed candidate mechanism list.

## Discovery anchors

Two sources currently anchor construct discovery and clustering:

1. Cane, O'Connor & Michie (2012), *Validation of the Theoretical Domains Framework* (doi:10.1186/1748-5908-7-37). Experts sorted 112 theoretical constructs; fuzzy cluster analysis supported 14 higher-order domains.
2. Albarracín, Fayaz-Farkhad & Granados Samayoa (2024), *Determinants of behaviour and their efficacy as targets of behavioural change interventions* (doi:10.1038/s44159-024-00305-0). This review synthesized multidisciplinary meta-analyses and compared determinants and intervention targets.

These are discovery/crosswalk anchors, not a finite ontology. New mechanisms can enter MetaRank even when neither source names them.

## Merge rule

Two labels share one mechanism folder only when the literature treats them as estimates of the same underlying construct or when a quantitative synthesis explicitly pools them under one estimand.

Similarity in ordinary language is not enough.

## Split rule

Keep constructs separate when theories assign them different causal roles, measures operationalize them differently, interventions can change one without necessarily changing the other, existing meta-analyses estimate them separately, or pooling would make the estimand ambiguous.

Example: self-efficacy and perceived competence are linked under a capability-belief family but remain separate.

## Subtype rule

A folder may temporarily contain named subtypes when the best available quantitative synthesis pools them. Subtypes remain explicit and should split once enough evidence supports separate estimates.

Example: social norms can temporarily include descriptive, injunctive, and subjective norms while retaining those subtype labels.

## Technique versus determinant

MetaRank permits both psychological determinants/states and self-regulation mechanisms. They must be labeled by family and their estimands kept explicit. A behavior-change technique should not be silently interpreted as a latent psychological state.

## Higher-order frameworks are crosswalks, not pooling instructions

TDF domains help detect synonyms and neighboring constructs, but membership in one TDF domain does not automatically justify statistical pooling.

## Outcome discipline

Every synthesis must state its outcome. An identity-to-intention estimate must never be ranked as though it were identity-to-behavior.

## Prior art

Albarracín et al. (2024) already produced a broad quantitative ranking of individual and social-structural intervention targets. Behavior MetaRank therefore does not claim to be the first ranking project.

Its intended differentiators are:
- living and continuously updateable;
- one mechanism per version-controlled folder;
- machine-readable source and synthesis records;
- explicit separation of association, prospective, causal, and mediation evidence;
- reproducible regeneration of cross-mechanism tables;
- transparent construct clustering and sensitivity analysis.
