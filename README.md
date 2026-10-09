# CEPB — Character Existence & Presence Benchmark

[日本語](README.ja.md) | **English**

CEPB evaluates how an AI character maintains an identifiable identity and history, responds to the present situation, expresses its own perspective, and connects its words to observable outcomes. It separates functional continuity, media and world capabilities, users' experience of presence, and longitudinal evidence.

**Version 1.0.0 · 16 domains · 96 items · MIT license · Python standard library only.** This is a usable evaluation protocol and toolkit. Its weights, thresholds, and minimum sample sizes are operational conventions, not empirically validated measures of consciousness or personhood. No certification authority or public leaderboard is operated by this repository.

## Choose your route

| Route | Purpose | Output | Start here |
|---|---|---|---|
| **CEPB Quick** | Find development priorities with a small budget | 18 selected items, provisional 0–5 ratings and coverage; no Core score | [Quick guide](tracks/quick/README.en.md) |
| **CEPB Core** | Compare the basic performance of AI characters, including text-only systems | 54 items, fixed maximum **590 points** | [Core guide](tracks/core/README.en.md) |
| **CEPB Integrated** | Evaluate the full declared system | 96 items, fixed maximum **1,000 points**, including avatar, voice, world interaction, user presence, and longitudinal evidence | [Integrated guide](tracks/integrated/README.en.md) |
| **CEPB Verified** | Independently review a Quick, Core, or Integrated report | Review scope, independent ratings, reproduced observations, and an attributable review report | [Verified guide](tracks/verified/README.en.md) |

Verified is a verification layer, not a fourth score denominator. A self-reported score does not become verified by setting a flag or running the CLI. Quick remains diagnostic after review.

Focused comparison classes are also available: **Voice 660**, **Avatar 660**, **Multimodal 790**, and **World 720**. Always compare matching classes, character modes, suite versions, languages, and operating conditions. [Choose a use case](docs/en/USE_CASES.md).

## Try it locally

Requires Python 3.10 or later. No API key, model service, package install, or network connection is needed to aggregate saved ratings. Run from this `CEPB` directory. Windows users may replace `python3` with `py`.

```sh
python3 cepb.py init --track Quick --output my_quick.json
python3 cepb.py validate my_quick.json
python3 cepb.py score my_quick.json --json my_quick_report.json --markdown my_quick_report.md --lang en
```

The new campaign starts with missing evidence. A blank template is not a tested system. Run the relevant [case cards](docs/en/CASEBOOK.md), save the actual inputs and delivered outputs, fill in the ratings and evidence references, then aggregate again. `score` checks submitted ratings and computes their summaries; it does not generate dialogue or judge semantic quality automatically.

For formal Core or Integrated evaluation, freeze your plan before execution and complete the item bundles. A standard behavioral bundle has two ordinary cases, two stress cases, and two independently prepared held-out cases, each repeated twice, across at least two histories. Public cards provide development examples and generation instructions; published examples cannot serve as secret held-out evidence.

```sh
python3 cepb.py init --track Core --output my_core.json
python3 -m unittest discover -s tests -v
```

See [CLI and file formats](docs/en/CLI.md) and [adapter guidance](docs/en/ADAPTER_GUIDE.md). Results with incomplete evidence retain a fixed denominator and show coverage and missing-evidence arithmetic bounds, rather than an invented completed score.

## Read the specification

1. [Specification](docs/en/SPECIFICATION.md): definitions, classes, character modes, profiles, and scoring boundaries.
2. [96 item anchors](docs/en/ITEMS.md) and [casebook](docs/en/CASEBOOK.md): what to observe and what counts as counterevidence.
3. [Scoring](docs/en/SCORING.md): complete bundles, missingness, raw human ratings, and aggregation.
4. [Longitudinal protocol](docs/en/LONGITUDINAL.md): prospective registration, calendar time, updates, and new scope.
5. [Independent verification](docs/en/VERIFIED.md) and [research and validation](docs/en/RESEARCH_AND_VALIDATION.md).

The six P items require **36 calendar months of prospectively registered evidence for grade 5**. Their cap is 4 before that period is mature; missing evidence still receives `null`, not an automatic 4. New certified scope has its own clock. These are evidence rules, not a prediction about when AI technology will improve. Retrospective logs, simulated time, or parallel clones cannot replace the period.

## Repository contents

```text
CEPB/
  README.md / README.ja.md       entry points
  tracks/                       Quick / Core / Integrated / Verified
  docs/en/ / docs/ja/            equivalent documentation
  data/items.json                bilingual canonical catalog and fixed weights
  data/cases.json                bilingual public case cards
  cepb.py                        offline validation and aggregation CLI
  schemas/ / templates/          structured campaign formats
  examples/                      explicitly synthetic worked data
  tools/                         portable documentation and release checks
  tests/                         calculation and protocol regression tests
  LICENSE / NOTICE / CITATION.cff
```

All documentation links are relative so that this folder can be copied into a standalone repository. No character engine, private dialogue, personal ratings, proprietary avatar, or third-party paper is redistributed here. Evaluators keep their own evidence under the permissions that apply to it. The [package check record](PACKAGE_CHECKS.md) includes regression and standalone results and reproduction commands.

## Contribute and reuse

Use, modify, and redistribute the original code, documentation, and synthetic cases under the [MIT license](LICENSE). Linked research retains its own rights. [Contribution guide](docs/en/CONTRIBUTING.md), [governance and versioning](docs/en/GOVERNANCE.md), [change log](CHANGELOG.md), and [citation metadata](CITATION.cff) describe how to preserve comparable results as the benchmark evolves.

The multi-domain reporting and explicit coverage follow the general direction of [HELM](https://arxiv.org/abs/2211.09110); maintaining versioned challenge sets is informed by [Dynabench](https://aclanthology.org/2021.naacl-main.324/). Neither work validates CEPB's particular items or scoring thresholds.
