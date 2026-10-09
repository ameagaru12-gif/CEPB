# Governance, versions, and publication

[日本語](../ja/GOVERNANCE.md) | [Home](../../README.md)

CEPB supplies a reusable specification and code. This local package does not claim an existing governing board, certification authority, reviewer registry, registered trademark, or public leaderboard. A standalone publication should identify maintainers, proposal and appeal channels, rights holders, and the actual publication time.

## Version roles

| Version | Example | Controls |
|---|---|---|
| Rules | `CEPB-1.0.0` | Constructs, weights, denominators, missingness, caps, full attainment |
| Suite | `CEPB-SUITE-1.0.0` | Cases, minimum repeats, held-out generation, operational thresholds |
| System | Implementation/configuration hashes | Model, prompt, memory, media, actions, environment |
| Campaign | Unique campaign ID | Frozen plan, execution, ratings, report |

A patch addresses score-preserving wording or tool fixes; a minor version adds separate extensions or auxiliary functions without changing existing scores; a major version changes their meaning, denominator, or required evidence. If a bug fix changes an old aggregate, retain the original and rationale, and issue a derived corrected report.

## Preserve comparison for at least five years

- Anchor: retain 1.0 constructs, weights, and comparison opportunities.
- Frontier: add annual stress and held-out challenges under separate suite versions.
- Extension: describe new media, bodies, and operating conditions in separate classes with separate denominators.

Do not move criteria after the fact to prevent full attainment. Bridge versions by evaluating the same system under both, and retain old results. Review saturation, rater agreement, language/population bias, duplicate items, and media/liking confounds at least annually. This is a maintenance policy intended to support five or more years of use, not a guarantee of future validity or non-saturation.

## Canonical data and language parity

`data/items.json` is canonical for IDs, weights, and track membership. Refer to the matching versions of SCORING, LONGITUDINAL, and VERIFIED for their rules. Japanese and English have equal standing; do not create language-specific numerical rules. Record contradictions and hold affected completed results or verification claims pending a versioned correction.

The CLI implements the rules; implementation bugs do not define new ones. Evidence truthfulness and reviewer independence require evidence inspection and independent checking.

## Standalone publication

Copy this folder alone into a standalone repository and run tests and release checks. Include README, LICENSE, NOTICE, CITATION, both languages, canonical data, templates, synthetic examples, tools, and tests. Exclude real dialogue, personal data, models, secret challenges, API keys, and private runs.

External publication, repository creation, and uploading are not part of this local package creation. After actual publication, record its time and frozen-version hash in prospective plans. Do not substitute the local creation date for publication, registration, or independent observation.
