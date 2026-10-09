# Longitudinal observation and clocks

Version: CEPB 1.0.0. Domain P assesses the prospective history of a registered lineage and implemented scope. Thirty-six calendar months is a CEPB evidence requirement, not a scientifically established time for personality maturity. Time alone earns no points.

## 1. Starting a clock

```text
lineage_t0 = max(
  actual publication and freezing time of the adopted rule,
  prospective registration of the character lineage and observation plan,
  first valid independent observation confirming the baseline and plan
)
```

The clock is not established until all three times are valid. Creating a local package or a file modification timestamp is not publication. Before actual publication, retain `rule_publication_at=null`; after publication, freeze an evidenced timestamp. Registration requires identifiable character definitions, baseline state, lineage, implemented scopes, observation plans, and change rules, rather than a list of future intentions.

The earliest version-establishment floor for CEPB-1.0.0 is `2026-10-09T15:00:00Z` (2026-10-10 00:00 in Japan). An earlier declared `rule_publication_at` is a protocol error. The floor is not proof of actual publication and does not automatically start a clock at that time. Unpublished rules retain null. Declaring a future `as_of` as the current real calendar to claim early maturity is also prohibited. Future planning dates are distinct from observed results.

Future `planned_at` values may be stored as plans. Future `observed_at`, evaluation, registration, and publication timestamps cannot be claimed as actual records. Early ratings do not treat future plans as violations or evidence missing from the window due so far.

A valid independent observation requires evidence that an independent observer checked the registered target and configuration. A developer's assertion alone cannot start the clock. Earlier logs may inform initial memories, retrospective evaluation, and current capabilities, but do not add to the new prospective period. This does not imply that the character previously did not exist, and existing memories need not be deleted.

## 2. Thirty-six UTC calendar months

Use the real UTC calendar. Add 36 calendar months at the same UTC time; if the destination month lacks the day, use its final day. For example, 2028-02-29T12:00:00Z becomes 2031-02-28T12:00:00Z. Do not replace this with 1080 days, accelerated virtual years, a changed computer clock, or parallel clone operation.

Before lineage maturity, or without a valid clock, every P item is capped at 4. Insufficient evidence remains null; a cap does not automatically award 4.

```text
Integrated time cap = 950 + 50 × 4/5 = 990
```

Under this rule, Integrated cannot reach 1000 during the first two years after starting. This is not a prediction that technology will improve slowly. The P requirement does not cap the short-term maximum of classes such as Core.

## 3. Observation plan

The standard plan registers a baseline, monthly operation/state/change records, quarterly independent checks, revisits and held-out tasks across years, and final current-capability checks. Freeze specific opportunities, targets, allowed gaps, recovery tests, and additional observations before starting. Daily user participation and continuous 24-hour operation are not universal requirements.

| Stage | Records |
|---|---|
| Start | Rules, character, lineage, implemented scopes, baseline, plan, independent observation |
| Monthly | Operation, changes, pauses, stored/missing data, pending issues, required opportunities |
| Quarterly | Samples of inputs, requests, delivery, states, environmental outcomes, independent checking |
| Revisits across years | Changed times and settings, held-out tasks, connection to the same history |
| Material change | Classification, inheritance or discontinuity, bridges, current-capability retests, new scope |
| Endpoint | Current configuration, cumulative window, scope maturity, independent ratings, gates |

The minimum observation window common to every P grade of 5 contains these **53 planned roles**. This does not create six independent histories; one window supports distinct P judgments.

| Role (machine `kind`) | Minimum | Time and independence requirements |
|---|---:|---|
| Baseline (`baseline`) | 1 | Confirm initial baseline state and registered target; both planned_at and observed_at are within [t0, t0 + 1 calendar month) |
| Monthly (`monthly`) | 36 | Distinct relative UTC calendar-month periods from t0, period_index 1–36 |
| Quarterly independent check (`quarterly_independent`) | 12 | Distinct three-calendar-month periods, period_index 1–12, each with an independent-check reference |
| Annual revisit (`annual_revisit`) | 3 | Within one calendar month after t0 + 12, 24, and 36 months; at least one uses held-out tasks |
| Final review (`final_review`) | 1 | Check current configuration, cumulative window, and unresolved issues; both planned_at and observed_at are at least 36 calendar months after the applicable origin |

Check planned and observed timestamps against registered periods. Many records within one month cannot become 36 months, nor can many checks in one quarter become 12 quarters. Roles such as the year-three revisit and endpoint may reference the same execution evidence when their distinct judgments are explained. Do not count 53 roles as 53 independent executions or histories. P4 requires the same minimum window and a bridge (`bridge`) for each certified scope. Add and track item-specific planned opportunities such as faults and recovery.

If a planned check is missing, retain the affected judgment as unobserved and perform additional checks under the plan. Do not fill gaps with success. Record resumption and repair without erasing failures. Do not expand allowed gaps after observing results to declare completeness.

A record state such as `failed` meaning inability to observe is distinct from an observed unsuccessful outcome. Preserve the latter as an observed outcome=fail with original evidence and ratings, rather than hiding it as missing/null. Counts of 53 roles and a valid clock alone do not award 5; assess their results against P1–P6 anchors.

## 4. Rerating P

For P, the cumulative observation window at the evaluation date is one final rating unit. Do not average early provisional ratings capped at 4 with an endpoint rating of 5. Preserve earlier ratings, and rerate the window including failures, gaps, and repairs at the endpoint. The same 36 months is not six independent histories; explain the distinct judgments for P1–P6.

Reaching 36 calendar months does not automatically award P=5 or Integrated=1000. Missing planned observation, independent checking, or final-configuration evidence leaves null. Performed observations that fail the requirement inform lower anchors and are distinct from missing evidence.

Before maturity, P can receive a final partial-window rating of 0–4 when all records planned through the evaluation date are complete, according to the evidence and anchors. Opportunities not yet due are not missing evidence in the current partial window. An invalid clock or missing evidence due so far retains null; a complete partial window does not automatically receive 4.

## 5. Releases and lineages

| Lineage policy | Changes |
|---|---|
| `FIXED_RELEASE` | Assess a specified implementation/model/contract release. Material changes create a new fixed release without automatic inheritance |
| `MAINTAINED_LINEAGE` | Assess continuity of a character and memory lineage. Preserve maintenance, inheritance, gaps, and bridges; retest current capabilities |

Thirty-six months of a maintained lineage does not mean the latest LLM itself was tested for 36 months. Report current capabilities separately from elapsed lineage history.

| Change | Clock and checking requirements |
|---|---|
| Bug fixes within the same scope, costumes or assets | May inherit lineage t0 with recorded changes and bridges; retest affected capabilities |
| Model or other maintenance preserving input/output and world scope | MAINTAINED_LINEAGE may inherit with bridges and current-capability retests; FIXED_RELEASE becomes a new release |
| First addition of voice, body, physical action, or an environment scope | Add a clock for the implemented new scope's registration and independent observation |
| Material replacement or severing of character, owner, or memory lineage | Restart the affected lineage; retain earlier records retrospectively without adding periods |

Do not reset every clock for every routine fix. Inheritance rests on bridges for owner, character, memory, semantic state, and action contracts rather than name equality. Missing bridge evidence remains unverified.

## 6. New-scope clocks

Define scope through implemented inputs/outputs, action contracts, and target worlds, not tags alone. Registering a planned future robot does not start its clock.

```text
scope_t0 = max(
  actual publication and freezing time of the adopted rule,
  implementation time of the new scope,
  prospective registration time of the new scope,
  first valid independent observation of its implemented range
)
```

If any of the four timestamps is missing, the scope clock is not established. The start cannot precede publication of the adopted rule. When certification includes a new scope, P4=5 requires 36 calendar months for that scope too. Even after lineage maturity, an immature required scope caps P4 at 4; the initial Integrated weights then cap the total at approximately 998.33.

```text
1000 − (50/6)/5 = 998.333...
earliest perfect-result eligibility = max(lineage_t0, all required scope_t0) + 36 calendar months
```

This is the earliest possible date if all other conditions are met, not a promised perfect-result date. Adding voice in month 35 caps P4 for a voice-inclusive result until 36 calendar months after the addition. Results for the earlier scope excluding voice may be retained separately.

Separate shared pre-branch history from branch-specific later history. Do not add clone counts or elapsed periods from other sessions. Identify each branch's clock, memory, and interventions; do not mix other characters' or owners' records as shared experience.

## 7. Time evidence and perfect-result statements

Combine append-only records, external time records, hashes, independent challenges, and witnessed samples. A hash timestamp supports existence of data by a time; it does not prove truth, execution, or continuous operation. If original evidence is audited with restricted access, disclose the checked scope and access limitations.

Integrated 1000 requires every unrounded value to be 5, all planned opportunities, maturity of the lineage and every required scope, current-configuration checks, required independent verification, and cleared critical gates. Display rounding, local clocks, or importing old logs cannot establish a perfect-result conformity claim. See [VERIFIED](VERIFIED.md) for independent checking and [SCORING](SCORING.md) for ratings.
