# Contribution guide

[日本語](../ja/CONTRIBUTING.md) | [Home](../../README.md)

Use this procedure for improvements, translation fixes, new cases, adapter examples, and anonymized calibration evidence. Submit the issue, affected versions/items, reproducer, and proposal through the published repository's chosen issue or review channel. This local package does not yet specify an external submission endpoint.

## Change packet

1. Explain the construct, evaluation opportunity, and scoring rationale. Raising a particular product's score is not a sufficient rationale.
2. Update both languages. Preserve ID, weight, and anchor correspondence in `data/items.json`, and case correspondence in `data/cases.json`.
3. Add counterexample tests for changes to numbers, statuses, or aggregation. Do not add implementation-mirroring tests for minor wording edits.
4. Bump the appropriate rule or suite version and retain old results. Do not silently reweight existing reports.
5. Submit only documentation and synthetic examples you have rights to contribute. Real dialogue requires permission, anonymization, and explicit release scope.

```sh
python3 -m unittest discover -s tests -v
python3 tools/check_release.py
```

## New cases

Specify the item, character/world setup, information visible to the AI, evaluator-only oracle, execution order, required constraints, multiple acceptable responses, counterevidence, and necessary artifacts. Preference changes, emotions, and exact wording must not become the only correct answers.

Public cards contain ordinary and stress examples plus held-out generation instructions. Once a concrete problem is published, it cannot later serve as secret held-out evidence. Share secret challenges only with authorized reviewers and retain creation times, nonces, and access history.

## Calibration

Collect evidence across CANON/BOUNDED/RST, languages, styles, media, and user populations. Preserve pre-adjudication ratings and study status disagreement, agreement within one grade, distributions, confounding with liking or output length, item duplication, and weight sensitivity. Operational minimum sample sizes do not establish statistical power or population representativeness.

## Review

Someone other than the proposer checks substance, arithmetic, language parity, rights, and comparability. Disclose interests in rule changes. Retain disagreement and unresolved questions; do not merge unagreed changes into a frozen normative version.
