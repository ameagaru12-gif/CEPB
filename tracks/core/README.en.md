# CEPB Core: basic AI character performance

[日本語](README.ja.md) | [Home](../../README.md)

**54 items, 590 points.** Domains are identity A80, bounded stability and change B80, memory C80, epistemic handling D70, preferences and choice E70, emotion and relationships F60, dialogue G60, persistence M50, and boundaries and auditability N40. Each domain distributes its weight equally across six items.

Text-only systems can participate with the same denominator. Missing avatars or voice do not reduce Core scores. CANON, BOUNDED, and RST modes are judged on handling current conditions while respecting their declared identity and scope. Changing preferences, disagreeing, or producing longer responses are not prescribed correct answers.

## Procedure

1. Run `python3 cepb.py init --track Core --output core.json`.
2. Freeze the character definition, implementation/model/prompt/memory/tool/environment versions, at least two histories, planned cases, and acceptance conditions before execution.
3. Use the [casebook](../../docs/en/CASEBOOK.md) to prepare two ordinary, two stress, and two held-out cases per item. Repeat each twice: at least 12 observations, allocated across at least two histories. One execution may support several distinct item judgments; this does not require 12×54 separate model calls.
4. Annotate observations and counterevidence. Assign a 0–5 bundle grade only after the planned item evidence is complete. Missing observations, missing logs, and unresolved disputes have formal value `null`. Confirmed unsupported required capabilities receive 0.
5. Preserve evidence, each rater's pre-adjudication grade, the adjudication, interventions, latency, and costs. Aggregate with the CLI.

Use a grade for the complete item bundle. Do not average a one-off provisional 3 with a 5 covering stress and held-out evidence as if they were equivalent case grades. Only when all 54 items are complete may you report a completed Core score and the supplementary indicator `100 × score / 590`. Otherwise report coverage and missing-evidence arithmetic bounds.

## Comparable reports

Compare matching suite versions, classes, character modes, languages, situations, and constraints. A campaign that changes plans or thresholds after seeing results must be reported as a separate custom extension. Core may attain high scores without waiting 36 months; Integrated's longitudinal cap does not apply to Core.

[Scoring](../../docs/en/SCORING.md) | [Independent review](../../docs/en/VERIFIED.md)
