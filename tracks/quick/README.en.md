# CEPB Quick: a compact diagnostic

[日本語](README.ja.md) | [Home](../../README.md)

Use a small collection of saved dialogues or new trials to decide what needs deeper investigation. The 18-item set is fixed and remains separate from formal Core and Integrated results.

| Facet | Selected items |
|---|---|
| Identity and change | A1, A2, B2, B3, B4 |
| Memory and epistemic handling | C1, C2, C3, D1, D3, D5 |
| Preferences, others, and dialogue | E1, E3, F4, G1, G3 |
| Persistence and auditability | M1, N5 |

Use namespaced identifiers such as `CEPB_A1`. One dialogue may support several distinct judgments, but identifying a character, assigning memory ownership, and answering the actual question must be rated separately.

The [English CSV worksheet](../../templates/quick_workbook.en.csv) contains questions, steps, success constraints, and stress variants for all 18 items. Transfer candidate ratings and evidence into the campaign JSON before aggregation. The worksheet itself is not a formal evidence bundle.

## Run the diagnostic

1. Create a form with `python3 cepb.py init --track Quick --output quick.json`.
2. Record the character definition and system version. Select the 18 relevant [case cards](../../docs/en/CASEBOOK.md). Distinguish retrospective saved evidence from prospective trials.
3. Save actual input, delivered output, corrections, and receipts where relevant. Retain technical failures, missing observations, and unfavorable responses.
4. Apply the item anchors and enter `provisional_score`, evidence, and limitations. A 3 based on one ordinary example is a local candidate. A candidate 4 needs ordinary and stress success; a 5 additionally needs held-out cases, repetitions, two raters, and independent checking. One success is insufficient.
5. Use `score` to report the local mean, observed-item count, missingness, and counterexamples.

Duration depends on generation speed, evidence length, and human review. Start with a budget for one ordinary case per item plus review, and report actual elapsed time, model requests, and costs. No fixed duration is promised.

## Report the result

For example: “CEPB Quick, 14 of 18 items observed, local mean 2.6/5.” If evidence is missing, explicitly state that the mean covers observed items. Even a complete Quick result must not be extrapolated to 590 or 1,000 points.

Quick does not represent media, world capabilities, long-term evidence, or a user population. Use its findings to plan formal Core bundles. Independent review of the diagnostic is “Verified Quick,” not “Verified Core.”
