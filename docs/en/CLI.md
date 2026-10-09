# CLI: validating and aggregating declarations

Python 3.10 or later is sufficient; only the standard library is used. The CLI does not call models, audio services, embeddings or the network. Run the following commands from the package's `CEPB` directory. On Windows, replace `python` with `py` if needed.

```console
python cepb.py init --track Quick --output runs/my-character/run.json
python cepb.py validate runs/my-character/run.json
python cepb.py score runs/my-character/run.json --json runs/my-character/report.json --markdown runs/my-character/report.en.md --lang en
```

This is a **tool for checking and aggregating human-declared ratings and evidence**. It does not grade anchor meanings, establish a character's existence or consciousness, verify evidence truth, identify real human participants, or establish reviewer independence. `independently_reviewed` is a declared verification status. Output `certification_issued` is always `false`.

## 1. Initialization and paths

`init` creates every required item as `unobserved`, with `score=null` and `provisional_score=null`. It also creates unfilled `evidence/*.md` placeholders for the character definition, system manifest and disclosure. The existence of a placeholder does not prove observation, registration or review. Edit all declarations, including `frozen_before_execution`, to describe what actually happened.

Tracks are `Quick`, `Core`, `Voice`, `Avatar`, `Multimodal`, `World` and `Integrated`. Changing a track name or its required IDs does not convert a run to another track. `templates/*.run.json` show initialized runs; `templates/*_bundle.json` show incomplete bundle shapes. Fill actual records before using them for formal ratings.

Command paths are relative to the working directory. Evidence references inside JSON are relative to the **directory containing run.json**. Absolute local files and HTTPS URLs are also accepted. Local references are checked for file existence; HTTPS references receive syntax checks only. Nothing is downloaded or checked for content truth.

`init` refuses an existing run path. `score` refuses existing outputs, an output equal to the input run, or identical JSON and Markdown output paths. Choose new filenames. Omit both output options to print the JSON report to standard output.

## 2. Run declarations

Required information includes the campaign ID, framework and suite versions, track, actual UTC `as_of`, character definition, system manifest, prospective protocol, lineage, verification status, gates, and all required items. Use full IDs such as `CEPB_A1`. The supported versions are `CEPB-1.0.0` and `CEPB-SUITE-1.0.0`.

Save dates as ISO UTC timestamps ending in `Z` or `+00:00`, for example `2026-10-10T00:00:00Z`. `as_of` cannot be later than the actual UTC time when the CLI runs. Actual observation, registration and publication clocks cannot exceed `as_of`. Simulated time, imagined dates, and self-reported ISO strings do not prove real elapsed time or independence.

This rule version has an earliest possible version floor of `2026-10-09T15:00:00Z`. Earlier `rule_publication_at` values are errors. **The floor is not evidence of actual publication.** Leave `rule_publication_at=null` until real publication exists.

`verification` is either `self_reported` or `independently_reviewed`. The latter needs at least two distinct reviewer IDs, disclosure and a review-report reference, but the CLI does not certify those reviewers' independence.

## 3. Statuses and Quick

| status | Meaning and score |
|---|---|
| `scored` | Declared completed rating; formal tracks require bundles |
| `unsupported` | Evidence-backed declaration that the capability is unsupported; integer `score=0` |
| `unobserved` | Not observed; formal score null |
| `log_missing` | Required logs absent; formal score null |
| `system_failed` | Observation could not run; formal score null |
| `disputed` | Unresolved judgment; formal score null |
| `not_applicable` | Applicability declaration; does not remove the fixed track denominator |
| `plan_error` / `protocol_error` | Plan or procedural inconsistency; formal score null |

For unresolved formal items use `score=null`, retaining local candidates in `provisional_score`. Distinguish an observed zero, an unsupported zero, and missing null. Scores must be finite 0–5; bundle and rater scores are integers. The equal-weight mean of multiple completed bundles may be fractional. Booleans, NaN, Infinity, out-of-range values and duplicate IDs are rejected.

Quick is an 18-item diagnostic. It uses `provisional_score` when present, otherwise `score` as a diagnostic candidate. If both are supplied they must agree. Candidates need reasons and evidence references. Outputs are the candidate mean, item coverage and missing-value bounds over the fixed 18 items. Each `formal_score` is null, as are formal points and weighted coverage. Quick is not converted to Core590 or Integrated1000.

## 4. A–N behavioral bundles

Formal items use `kind=behavioral` in `bundles`. Prospectively plan two ordinary, two stress and two heldout cases, each with two repeats: at least 12 observations and two distinct history IDs. A case's condition and history must remain fixed across repeats. Missing, extra or duplicate cases, unknown outcomes and missing evidence do not complete a bundle.

`case_results.outcome` is `pass`, `partial`, `fail` or `unknown`. Humans judge anchors and preregistered tolerances. The code does not interpret meaning; it checks procedural caps on the declared rating.

| Declared stage | Additional mechanical conditions |
|---|---|
| 0–2 | All planned observations complete; humans judge the semantic stage |
| 3 | All ordinary observations pass |
| 4 | All ordinary and stress observations pass |
| 5 | All 12 pass, two distinct raters, independent check, and declared heldout secrecy with evidence |

Preserve raw `rater_scores`. If a raw rater score differs from the final bundle score, an `adjudication_ref` is required. Unresolved disagreement yields `disputed` and formal null. The final item score must equal the mean of its completed bundles.

## 5. O human-presence bundles

Do not substitute the behavioral 12-case protocol for O. Use `kind=human_presence` and `rubric_id=CEPB-O-0.1`. Plan at least one condition in each ordinary/stress/heldout stratum and at least 12 distinct human participants per stratum. The same 12 people may participate in all strata. Preserve every planned participant×condition raw integer rating of 1–7 and its evidence.

For multiple conditions, first take each participant×stratum median; then calculate stratum medians and the proportion of participant summaries at least 5. The overall median for stages 0–2 gives equal weight to participant×stratum summaries. Extra conditions do not give a stratum more weight.

| Stage | Highest stage meeting numeric and evidence conditions |
|---|---|
| 0 | No higher stage qualifies and overall median≤2 |
| 1 | No higher stage qualifies and 2<overall median<4 |
| 2 | No higher stage qualifies and overall median≥4 |
| 3 | Ordinary median≥5 and support proportion≥2/3 |
| 4 | The same conditions in ordinary and stress |
| 5 | Every stratum median≥6 and support proportion≥0.8, two raters, independent check and heldout secrecy evidence |

High raw ratings alone do not establish 5. If additional stage-5 evidence is absent but all stage-4 conditions hold, 4 is appropriate. O3 requires actual revisits on different UTC dates at least 24 hours apart. For O6, store raw break ratings in `raw_ratings` and separate positive post-repair ratings in `repair_ratings`. Break ratings use `8−x` to align direction; reversal alone does not establish repair. Both channels must cover the full plan. At stage 3 or higher both channels must meet the corresponding stratum thresholds.

`calibration_ref` refers to question-comprehension and operational-procedure records. Its existence does not establish empirical or scientific calibration. These thresholds and the 12-person minimum are CEPB operational rules, not validated psychological scales or guarantees of power or representativeness. See [SCORING](SCORING.md).

## 6. P cumulative-window bundles

P rates one cumulative observation window, not an average of monthly scores. The lineage origin is `max(rule publication, registration, first independent observation)`. Each P4 scope also includes `implemented_at`, using the maximum of four clocks. If any required clock is null, the origin is unavailable and formal P is null. Before 36 **calendar months** from each required origin the cap is 4, but 4 is never automatic. Overclaiming a cap yields `protocol_error` and formal null; it is not clamped.

`required_observations` include unique ID, `kind`, `planned_at`, `observed_at`, `status`, `clock=utc_calendar` and evidence. A planned window endpoint and `planned_at` may be future dates. Future opportunities count as neither success nor missing past observations. Stages 0–4 may be rated when all observations planned through `as_of` are complete. An observed `outcome=fail` remains an observation; it differs from observation-impossible `status=failed`.

Every P stage 5 requires 53 judgment roles: one baseline, 36 distinct monthly periods, 12 independent quarterly periods, three annual revisits and one final review. Monthly buckets are relative calendar months from the origin; quarterly buckets span three months; annual revisits occur within one calendar month from origin+12/24/36 months. Use `period_index`. Every quarterly record needs an independent-check reference, and at least one annual revisit needs `heldout=true`. P4 adds the same window and a bridge for every declared scope. For stage 5, both baseline planned and observed clocks lie in the first calendar month from each origin; both final-review clocks are at or after origin+36 calendar months. Reusing evidence across judgment roles does not create more independent sources or histories.

Clock and role checks do not establish P anchor meanings. Humans must judge failures, gaps, repair and bridges to the current configuration. See [LONGITUDINAL](LONGITUDINAL.md).

## 7. Aggregation, gates and exit codes

Formal tracks assign each item its domain weight divided by six. `known_points` include completed items only. `official_score` receives the completed declared total only when all required items are complete. Despite the field name, it is not third-party certification. Missing items remain in the fixed track denominator, with lower and upper bounds. These are arithmetic missing-value bounds, not confidence intervals or probabilities of attainment.

`item_coverage` (also the compatibility field `coverage`) is known item count divided by required count. `weighted_coverage` is the sum of known item weights divided by the fixed track maximum. Evidence-backed unsupported zero belongs to the known set. Quick weighted coverage is null.

Required gates are `identity_evidence,persistence,scope,procedure` for Core/Voice/Avatar/Multimodal; World adds `world_connection`; Integrated also adds `longitudinal`. Unresolved, unassessed or absent required gates block full-attainment eligibility but are reported separately from declared item points. `clear` is a declaration, not proof that truth has been verified. Eligibility uses unrounded values and the tool issues no certification.

| Exit code | Meaning |
|---|---|
| 0 | No procedural errors; unobserved, missing or incomplete items may remain |
| 1 | Validation or aggregation found procedural errors; score still writes a diagnostic report |
| 2 | Fatal JSON, argument or output-path error |

`validate` returning `valid=true` does not prove meaning, evidence truth or formal completeness. Inspect `issues` with severity `missing`, item `formal_status` and null values. JSON Schemas describe shapes; the standard-library CLI uses its own validation code for planned coverage, references, clocks and arithmetic.

## 8. Fictional examples and tests

```console
python cepb.py validate examples/synthetic_core_complete.json
python cepb.py score examples/synthetic_quick_partial.json
python cepb.py score examples/synthetic_integrated_partial.json --markdown runs/synthetic.partial.en.md --lang en
python -m unittest discover -s tests -p "test_*.py" -v
```

All `examples/synthetic_*.json` records are invented. They contain no real character observations, human ratings, independent reviews or elapsed longitudinal study. Core590 demonstrates arithmetic; the Integrated example leaves O/P unobserved. Mature1000 tests inject hypothetical clocks to check rule arithmetic, not present attainment. Do not copy private conversations or participant information into public examples.
