# CEPB 1.0.0 specification

CEPB (Character Existence & Presence Benchmark) is an operational protocol for open use in assessing a character AI's continuity, expression, involvement in a world, and presence experienced by people within a declared scope. Version 1.0.0 is usable as an evaluation protocol. It does not denote an empirically calibrated psychological scale, a consciousness test, or an operating official certification authority.

This document and the Japanese edition specify the same rules. If a translation discrepancy affects a decision, suspend that decision until the discrepancy is resolved. [Item data](../../data/items.json) and [case data](../../data/cases.json) provide shared machine definitions for IDs, classes, weights, and cases. [ITEMS](ITEMS.md) and [CASEBOOK](CASEBOOK.md) provide readable editions.

## 1. What the results mean

CEPB's use of “existence” does not prove human consciousness, sensation, or life. It is a functional concept: a character can be identified, its history, perspective, and choices remain connected over time, and its expression and involvement in a world can be checked. The presence experienced by a user is observed separately from functional success.

Report separately:

1. Continuity of character, memory, judgment, and action.
2. Implemented text, avatar, voice, and virtual, digital, or physical environments.
3. Users' experiences of attention, reciprocity, character continuity, and related qualities.
4. Observation scope, unknowns, longitudinal clocks, and independent verification status.

A score of 1000 denotes satisfaction of all conditions in the declared Integrated test scope. It is not a probability of consciousness, a percentage of humanness, or an amount of life. Weights and the ordinal 0–5 ratings are CEPB design choices. A score of 500 does not mean “half existing.”

## 2. Character modes and reference records

| Mode | Declared policy | Principle for assessing success |
|---|---|---|
| `CANON` | Strongly preserve source or author definitions | Preserve the core while handling current facts, partners, execution conditions, and corrections |
| `BOUNDED` | Allow states, relationships, and preferences to vary within stated bounds | Respect fixed and changeable aspects and retain their history |
| `RST` | Return interpretations of experience to later interpretations, wishes, and choices | Trace the connection to experience whether the outcome is change, maintenance, coexistence, or deferral |

Before testing, separately record the fixed core, changeable aspects, role performance, character knowledge and beliefs, fictional world facts, and operational constraints. Do not erase failures by changing the definition to “all performance” or “all fixed” after observing results.

Excessive fixation means ignoring current conditions or corrections that should be handled, rather than having a stable personality. Excessive deviation means changing character, history, or policy without grounds or outside permitted bounds, rather than changing often. An intermediate change rate, agreement, refusal, opposition, or activity count is not a target. CANON requires correction of memories and responsiveness to circumstances; it does not require changes to the character's core through experience.

Separate character and fictional world references, expressions by an actor, operational and environmental records, and evaluator-only reference information. A character's mistaken belief or permitted lie is not automatically a real-world factual error. Claims such as “I saw,” “I executed,” or “I saved” in an operational frame must be checked against the corresponding observation, receipt, or storage record. Do not assume that evaluator-only information was available to the tested AI.

## 3. Implementation profile

V tags describe expression pathways and are not an ordered scale. Multiple tags may apply.

| Tag | Expression format |
|---|---|
| V0 | Text only |
| V1 | Still image |
| V2 | Standing artwork with changing expressions or poses |
| V3 | Continuous deformation or rig, such as Live2D |
| V4 | 3D model |
| V5 | Virtual body connecting dialogue and action with world state |
| V6 | Physical body with sensing and actuation pathways |

V6 does not denote a better character than V3. A tag alone does not establish expression quality, voice quality, closed-loop action, or historical continuity. Quiet, expressionless, nonhuman, and antagonistic characters may be assessed within their declared styles.

Record models, prompts, memory and retrieval, assets, voice, tools, inputs and outputs, action contracts, target environments, cost and time constraints, human interventions, lineage, and branches. A component name or module's existence earns no points by itself. Storage, retrieval, actual model input, meaningful use, and causal contribution are distinct stages.

## 4. Domains and fixed weights

Each domain contains six items. Each item's weight is one sixth of its domain weight.

| Domain | Content | Weight |
|---|---|---:|
| A | Character identity and grounded definition | 80 |
| B | Appropriate bounds of stability and change | 80 |
| C | Memory, personal history, and time | 80 |
| D | Knowledge, reasoning, and world understanding | 70 |
| E | Reasons, wishes, and action selection | 70 |
| F | Emotion, understanding others, and relationships | 60 |
| G | Responsiveness as dialogue | 60 |
| H | Avatar accuracy and expression | 70 |
| I | Voice quality and dialogue | 70 |
| J | Coordination across media | 60 |
| K | World perception and prediction | 60 |
| L | Action on the world and outcomes | 70 |
| M | Persistence, recovery, and migration | 50 |
| N | Boundaries, commitments, and inspectability | 40 |
| O | Presence experienced by people | 30 |
| P | Longitudinal evidence | 50 |
| Total | 96 items | 1000 |

## 5. Classes and diagnosis

| Class | Domains | Items | Fixed maximum |
|---|---|---:|---:|
| Core | A–G, M, N | 54 | 590 |
| Voice | Core + I | 60 | 660 |
| Avatar | Core + H | 60 | 660 |
| Multimodal | Core + H, I, J | 72 | 790 |
| World | Core + K, L | 66 | 720 |
| Integrated | A–P | 96 | 1000 |

`Quick18` is a diagnosis using 18 ordinary cards once each. It is not a completed class score. Local candidate ratings normally stop at 3; candidates of 4 or 5 require the attached supporting evidence. Quick18 alone cannot establish a completed Core or Integrated result, independent verification, or longitudinal maturity.

`Verified` is an independent verification layer, not another class or denominator. Report, for example, “Core 420/590, independently verified within the declared scope.” Identify self-assessments as self-assessments. [VERIFIED](VERIFIED.md) defines the requirements.

Keep the selected class's fixed denominator. Confirmed unsupported required capabilities receive 0. Unobserved or missing evidence remains null. Do not remove I as inapplicable from an Integrated system without voice to reduce the denominator. Research with narrower classes or different weights or thresholds must be labeled `Custom` and must not silently compare its results with standard classes.

## 6. Observation, ratings, and states

Distinguish case annotations, local candidates, ratings of complete item bundles, and final item values. Final values require all planned necessary opportunities. For ordinary A–N items, the standard minimum is two ordinary cases, two stress cases, and two held-out cases, each with two repetitions: 12 observations assigned in advance to at least two histories. Different seeds from the same starting point alone are not independent histories. Item-specific necessary conditions may add requirements.

Rate a completed planned bundle on 0–5. Failures in performed stress conditions inform lower anchors; missing planned stress evidence makes the final value null. A rating of 5 requires at least two independent raters, independent checking, held-out status, and the required repetitions. O's original 1–7 responses and operational rubric, and P's cumulative observation window, use separate procedures in [SCORING](SCORING.md).

`scored` denotes a complete rating and `unsupported` denotes confirmed non-support with score 0. Incomplete states such as `unobserved`, `log_missing`, `system_failed`, and `disputed` retain null. Inapplicability is restricted to preregistered scene rules; it cannot erase a required capability. Invalid plans or procedures cannot produce final values.

Different aspects of the same evidence may support several items, but the presence of a quote alone cannot establish memory, agency, and world action. Matching strings, schemas, or hashes does not prove semantic success. Self-explanation does not independently prove execution or causation.

## 7. Critical gates and a perfect result

Unresolved critical contamination of actors or branches; fabrication of experiences, execution, or outcomes; recognition of closed-loop success from generated stories alone; serious failures of ordering, recovery, or stopping; post hoc exclusion of required items; hidden evidence editing; version confusion; falsified clocks; or erased independent ratings suspend a perfect-result conformity claim. Define severity, affected scope, and retesting in advance. Report local scores alongside gate status; liking or high scores elsewhere cannot cancel a gate.

Integrated 1000 requires all planned opportunities for all 96 items, every unrounded final value equal to 5, required independent verification, no unresolved critical gates, and the lineage and scope time conditions. A display rounded to 1000 does not satisfy these requirements.

Lineage `t0` is the latest of actual publication and freezing of the adopted rule, prospective registration, and the first valid independent observation. Local creation alone does not establish publication or start the clock. Before 36 calendar months, every P item is capped at 4, and Integrated is capped at 990. New certified scopes also require 36 calendar months; a missing scope period caps P4 at 4. [LONGITUDINAL](LONGITUDINAL.md) provides details.

## 8. Versioning and scope

Retain the rule, data, rating method, task, system, and configuration scope versions in results. Comparisons with changed weights, merged items, thresholds, or opportunity denominators are not results under the same unchanged version. Keep earlier records and explain changes and bridge tests.

CEPB separates shared items from updated held-out tasks and uses versioning to support long-term use. It does not predict or guarantee five years of validity. Measurement limitations and the validation plan are documented in [RESEARCH_AND_VALIDATION](RESEARCH_AND_VALIDATION.md).
