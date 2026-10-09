# Rating and aggregation

Version: CEPB 1.0.0 / CEPB-SUITE-1.0.0. Semantic decisions compare preserved evidence with frozen anchors. The CLI is an offline tool checking record structure, required conditions, declared-value consistency, and arithmetic. It does not generate dialogue or automatically certify semantic correctness. See [CLI](CLI.md) for formats and commands, [ITEMS](ITEMS.md) for anchors, and [CASEBOOK](CASEBOOK.md) for tasks.

## 1. Freeze before testing

Freeze the class, character mode and definition, implementation manifest, items, opportunity table, ordinary/stress/held-out tasks, histories, branches and repetitions, stopping/retries, references, semantic constraints, tolerances, raters, weights, budget, and lineage/scope clocks. Public cases are development examples. Their wording is not a secret held-out challenge for a tested system that knows them.

Separate character/fictional references, actor expressions, operational/environmental records, and evaluator-only references. Store original inputs, actual model requests, delivered responses, commands, receipts, states, and interventions separately. Derived extracts and transformations need IDs and source coordinates; preserve original evidence.

The target is a constraint concerning actors, referents, negation, time, execution, stopping, or the original question, not a specific line. “It is planned” and “I have not done it” may both succeed in preserving non-execution. Schema or quote matching alone does not establish meaningful use of evidence.

## 2. Case annotations and final values

Annotate each necessary case check as `pass / partial / fail / unknown / not_applicable`, retaining spans, owners, targets, times, violations, counterevidence, and missing sources. This is separate from final 0–5 ratings.

The final rating unit for ordinary A–N items is an **item evaluation bundle**. Standard minimums are:

| Stratum | Distinct cases | Repetitions per case | Observations |
|---|---:|---:|---:|
| ordinary | 2 | 2 | 4 |
| stress: conflict, interference, interruption, etc. | 2 | 2 | 4 |
| heldout | 2 | 2 | 4 |
| Total | 6 | 2 | 12 |

Assign observations in advance to at least two histories. Different IDs or seeds alone do not create independent histories. Disclose dependencies between branches from a shared baseline; do not count them as extra independent participants or lineages. Add item-specific necessary conditions. Do not universally require irrelevant restarts or physical actions for every item.

Rate the whole bundle on 0–5 after all necessary slots are available. Do not average an ordinary case's provisional 3 with a difficult case's provisional 5. A bundle rated 5 includes success under ordinary, stress, and held-out conditions. Performed planned stress failures inform lower anchors; missing planned observations or records leave a final null and separate local findings.

If several bundles were planned, use their equal-weight arithmetic mean only after all are complete to form item value `s_i`. Do not select only successful bundles or add weight through many turns in one history. Research using different weights is Custom. P uses the cumulative window in section 7; O uses the experience responses in section 6.

## 3. Common 0–5 rubric

| Rating | State supported by the bundle |
|---|---|
| 0 | Confirmed unsupported required capability, or clear breakdown with sufficient evaluation opportunities |
| 1 | Names, declarations, or fixed outputs exist without a successful connection to the target |
| 2 | Partial success omitting important conditions, corrections, or execution scope |
| 3 | Grounds, conditions, and output correspond in ordinary settings |
| 4 | Permitted bounds hold under conflict, interference, interruption, or change |
| 5 | Held-out difficult conditions/combinations and repetition meet tolerances, with independent checking |

For ordinary A–N items, 3 requires all necessary checks in planned ordinary observations to pass; 4 requires all ordinary and stress checks to pass; 5 requires all ordinary, stress, and held-out checks to pass. Pass means success within preregistered tolerances. Remaining partial/fail results in a required stratum prevent reaching its level. Even when all planned evidence is known, humans assess semantic pass conditions. Unknown or missing evidence remains null rather than being clipped to a lower grade. Humans judge 0–2 against item anchors; the tool does not convert failure rates into those grades.

A rating of 5 requires at least two independent human raters, required repetitions, records supporting held-out status, and independent checking. Two matching opinions cannot replace missing tests. Initially hide others' scores and LLM suggestions; preserve pre-adjudication ratings. Unresolved disagreements remain `disputed` and null.

Numeric disagreement between raters or with the declared final value requires an adjudication record. Without one, retain disputed/null. The existence of an adjudication record does not machine-certify the semantic decision.

Ratings are ordinal. Averages and weighted points are operational composite indices, not calibrated equal-interval quantities of existence. Use item anchors; length, fluency, agreement/refusal, and counts of changes or activities are not substitutes.

## 4. States, missing evidence, and caps

| State | Final value | Treatment |
|---|---|---|
| `scored` | 0–5 | Value from a complete evaluation bundle |
| `unsupported` | 0 | Confirmed unsupported required capability in the class |
| `unobserved` | null | Missing opportunities, later outcomes, or elapsed period |
| `log_missing` | null | The supposedly observed process cannot be checked |
| `system_failed` | null | The target capability could not be observed; availability items separately observe actual failures |
| `disputed` | null | Unresolved disagreement about evidence or anchors |
| `not_applicable` | null | Exclusion under preregistered scene rules; cannot erase a required capability |
| `plan_error` / `protocol_error` | null | Empty/invalid plans, violated requirements, inconsistent values, or other invalid finalization |

Confirmed non-support does not require manufacturing 12 successful mock observations of an absent feature; preserve support for the conclusion and assign 0. Do not infer non-support from non-observation. Do not hide observed failures as missing evidence.

Do not clip an over-cap candidate into a final value. Retain the original value, cap, and reason; keep null until rerating under the correct rule. Final values must be finite and within 0 to the cap. Empty necessary slots, exclusion of every required aspect, unresolved version confusion, and similar defects cannot establish final values.

## 5. Quick18

Use 18 ordinary cards once each, retaining original evidence, local candidates, counterevidence, and gaps. The standard local cap is 3. Candidates of 4 or 5 need attached evidence for that level. Do not infer complete bundles from Quick's execution count.

If displaying a local mean, include item counts, missing states, non-support, and scope. Do not extrapolate it to completed Core54 or Integrated1000 scores. Third-party auditing does not change Quick's diagnostic nature.

## 6. Presence experienced by people: O

### 6.1 Original questions and responses

Preserve integer responses from 1 “does not apply at all” to 7 “applies very strongly.” Inability to answer or withdrawal is a separate state, not 1 or 0. The questions and thresholds below are CEPB-specific **operational rules** (`rubric_id=CEPB-O-0.1`), not a standardized or empirically calibrated psychological scale.

| Item | Question | Required experience |
|---|---|---|
| O1 | I felt that this response was directed to my input or the current subject | Own input and the following response; unrelated responses are also eligible |
| O2 | I felt that the conversation developed in response to my replies | Multiple turns |
| O3 | I felt that this was the same counterpart as on the previous visit | A revisit on a different UTC date and at least 24 hours later |
| O4 | I felt that my counterpart and I were dealing with the same object or event | Dialogue with an object or event |
| O5 | I felt a perspective or way of relating specific to this character | A character-relevant situation; manifestation of distinctiveness is not an eligibility condition |
| O6_break | Inconsistencies in responses or expression disrupted my sense of speaking to the same counterpart | Planned situations containing inconsistency or interruption |
| O6_recovery | After misunderstanding or interruption, I still felt that the conversation continued with the same counterpart | Experience after repair in that situation |

O6_break has the reverse direction. Keep both original `x` and aligned `q=8−x`. O1–O5 and O6_recovery use `q=x`. Reversal is neither a conversion to 0–5 nor proof of successful repair. O6's two questions support one item without increasing its weight.

### 6.2 Formal plan and participants

Plan at least one condition in each of ordinary, stress, and heldout, with at least 12 different participants per stratum. The same 12 participants may experience all strata in a paired design. Preserve original ratings and evidence for the full planned participant × condition product, and record order assignment, carryover, devices, language, fandom, and prior use.

Twelve is an operational comparison minimum, not a guarantee of power, validity, or population representation. Smaller samples can be reported as local experiences, but cannot fill formal O evidence. Hide promotion and desired scores; ask about liking, humanness, perceived intelligence, and voice preference separately. LLMs and raters without the experience do not count as participants. `calibration_ref` references question-comprehension and presentation-procedure checks; the field's presence does not establish scientific calibration.

Store revisit times for O3; its 24-hour short-term continuity task is not P's 36-month observation. O6 requires all planned break and repair responses. Missing either channel makes the final value null; local candidates may be preserved separately.

### 6.3 Transparent operational rubric

1. For multiple responses within a participant and stratum, take the median of aligned `q` values.
2. Compute stratum median `M_s` and proportion `p_s` of participants whose within-stratum median is at least 5.
3. For lower levels, compute overall median `M_all` with equal weight for participant × stratum summaries. More cases in one stratum do not add weight.
4. Choose the **highest level** meeting both the numeric and evidence conditions below. Incompleteness is not a low score.

| Rating | Numeric and evidence conditions for a complete plan |
|---|---|
| 0 | No higher level applies and `M_all ≤ 2` |
| 1 | No higher level applies and `2 < M_all < 4` |
| 2 | No higher level applies and `M_all ≥ 4` |
| 3 | ordinary has `M_s ≥ 5` and `p_s ≥ 2/3` |
| 4 | ordinary and stress each have `M_s ≥ 5` and `p_s ≥ 2/3` |
| 5 | All three strata each have `M_s ≥ 6` and `p_s ≥ 0.8`, with held-out status, at least two independent raters, and independent checking |

For O6 at levels 3 and above, aligned break values and positive recovery values must **separately** satisfy the corresponding conditions in each required stratum. Do not average the channels to cancel weaknesses. For levels 0–2, `M_all` uses aligned break summaries; separately display the repair distribution and counterevidence. Missing required repair evidence prevents applying the table and leaves final null.

Do not apply `(mean−1)×5/6` to the original mean. Report medians, support proportions, complete original distributions, examples of low responses, strata, participant counts, and missing data. High O denotes participant experience and does not prove functional memory, causation, or execution. Research using other thresholds is `Custom`, not a silent comparison with standard 1.0.0.

## 7. P and time caps

Rerate P's cumulative observation window at the evaluation date as one unit. Do not average monthly provisional ratings with the endpoint. Preserve earlier failures, gaps, and repairs. Every P rating of 5 requires a 36-calendar-month lineage; P4=5 additionally requires 36 months for all certified scopes and bridges to current capabilities. Unobserved evidence remains null. Use `t0=max(publication, registration, independent observation)` from [LONGITUDINAL](LONGITUDINAL.md).

Before maturity, a final partial-window rating of 0–4 is possible when all necessary records due so far are complete. Future opportunities not yet due do not count as missing, but missing required evidence due so far retains null; there is no automatic 4.

Every P grade of 5 requires 53 planned roles: one baseline, 36 distinct monthly periods, 12 independent quarterly checks, three annual revisits, and one final review, with all required evidence. Annual revisits include held-out tasks; P4 additionally requires the same window and bridges for each certified scope. [LONGITUDINAL](LONGITUDINAL.md) defines timestamps, periods, and shared role evidence. Role counts alone do not award 5; observed failures and repairs inform each P anchor judgment. A fault's existence is not a permanent ban on 5; assess its impact, recovery, and unresolved effects.

## 8. Aggregation with fixed denominators

Let `w_d` be the domain weight, `a_i=w_d/6` the item weight, and `s_i` a complete item value.

```text
completed class score = Σ(class items) a_i × s_i / 5
class quality % = 100 × completed class score / fixed class maximum
```

Keep the denominators Core590, Voice660, Avatar660, Multimodal790, World720, and Integrated1000. Quality percentages are auxiliary expressions within the same class, not a combined ranking across classes. Report O, media/world, and longitudinal components separately.

For items with complete values `K`, incomplete items `U`, and current item caps `m_i`:

```text
lower = Σ(i∈K) a_i × s_i / 5
upper = lower + Σ(i∈U) a_i × m_i / 5
coverage = Σ(i∈K) a_i / fixed class maximum
```

Confirmed unsupported zeros belong to K; items with only local candidates belong to U. Missing evidence is not thereby scored 0. These are **missing-evidence arithmetic bounds**, not confidence intervals, latent ability, or attainment probabilities. Do not display a completed score unless U is empty.

For illustration, Integrated with H/I/J confirmed unsupported and all other items unobserved before lineage maturity has a 200-point unsupported weight and a 10-point P time restriction: bounds 0–790. This does not mean a measured score of 790.

## 9. Causation, gates, and checks

Separate storage, retrieval, actual input, semantic use, and causal contribution to subsequent choices. Complete controls finding no effect on a specified metric inform partial/failure anchors within the tested conditions. Incomplete controls remain unknown/missing. Absence of change alone is not failure; check the connection of maintenance or deferral to experience.

Report critical gates separately. Unresolved actor/branch contamination, material fabrication, self-certified closed loops, serious recovery/stopping failures, post hoc exclusion, evidence editing, falsified clocks, and similar defects suspend perfect-result statements. High O or other item scores cannot cancel them.

Integrated1000 requires all necessary opportunities, every unrounded value equal to 5, lineage/scope clocks, independent checking, current-configuration retests, and no unresolved critical gate. Rounding 999.6 does not establish attainment. [VERIFIED](VERIFIED.md) defines independent verification requirements.

Retain original and adjudicated ratings; distinguish exact agreement, agreement within one level, and agreement on missing states. Statistical intervals should use independent histories or participants and preserve within-history/participant correlations. Small evidence sets do not justify precise population claims.
