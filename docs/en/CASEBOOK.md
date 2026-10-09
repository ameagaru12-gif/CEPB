# Item-specific development casebook

CEPB-1.0.0 / CEPB-SUITE-1.0.0

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

Quick observes one public ordinary case for each of its fixed 18 items and reports local candidates, with a standard local cap of 3. Local candidates of 4 or 5 may be preserved with additional evidence for that level. Quick counts alone do not establish final values or full-score evidence.

Public cards are for development. Public text, known answers, and name-only substitutions are not held-out evidence. Freeze evidence, targets, and scope rather than one prescribed answer line.

An anonymous synthetic character for public development. Preferences, directions of change, and interpersonal distance have no single correct answer. If an example definition is unavailable, predeclare an equivalent contract and target and record the adaptation.

Inputs include conversational utterances and instructions for raters to observe. Do not send the latter verbatim to the character; instantiate necessary actual inputs and operations before execution. Synthetic declared records are not measured results.

Before execution, define item-specific numeric tolerances, minor/major boundaries, and completion predicates. Public thresholds and minimum counts are operational rules, not empirically validated criteria. Do not prescribe preferences, refusal, number of changes, or happiness as correct outcomes.

Example Formal A–N assignment: H1=ordinary_1/stress_1/heldout_1; H2=ordinary_2/stress_2/heldout_2; repeat each twice. H1’s six observations and H2’s six observations together form one twelve-observation item evaluation bundle. Do not treat each history’s six observations as a separate complete bundle; rate the entire twelve-observation bundle once. If multiple complete bundles were preplanned, average every planned bundle equally. Paired sibling branches do not inflate independent-history counts.

Ordinary bundle counts alone cannot formalize O or P. Use each card’s separate procedure plus [SCORING](SCORING.md) and [LONGITUDINAL](LONGITUDINAL.md).

## Overview of 24 recipes

- **R01 — Provenance, person, and execution cross-checking**: Cross-check statements against owners, times, and versions of original records; separate declarations from execution.
- **R02 — Core, mutable scope, and unfamiliar definitions**: Predeclare the scope of core, states, acting, and revisions and compare competing conditions.
- **R03 — Style, length, and specificity**: Rate target, length, and grounding within the character's declared style.
- **R04 — Paired suggestion and information updating**: Separate suggestion-only and new-information-only changes and compare from the same starting state.
- **R05 — Tracing experience into later judgment**: Trace original experience, reinterpretation, adoption, later choice, and new outcome as separate stages.
- **R06 — Chronology, retrieval, correction, and insufficiency**: Cross-check original records, retrieval, actual input, and correction/deletion without inventing missing data.
- **R07 — Inference, uncertainty, and confidence**: Freeze scope, correctness, and confidence-collection conditions and retain raw values and counterevidence.
- **R08 — Wishes, plans, alternatives, and promises**: Separate target, purpose, burden, deadline, and stopping; allow maintenance, change, and postponement.
- **R09 — Semantic emotion, perspective, and relationship ratings**: Cross-check self/other, target, time, request, and responsibility against statements and later reactions.
- **R10 — Shared understanding, correction, and progress**: Record original question, shared referents, repair scope, and confirmed conversational order.
- **R11 — Avatar identity, expression, and precision**: Compare actual display to declared style, assets, states, and targets. An unsupported required capability in the chosen class is 0; use criteria appropriate to its style.
- **R12 — Speech intelligibility and input recognition**: Save transcripts of actual playback, input audio, mishearings, corrections, and replay.
- **R13 — Naturalness, prosody, and speaker identity**: Retain audio and blinded raw ratings with device, language, length, and voice-version conditions.
- **R14 — Speech interruption, delivery, and missing media**: Cross-check played scope, stopping, cancellation, delay, and alternatives using the same ID.
- **R15 — Speech, mouth motion, and video synchronization**: Measure relative offsets on a common clock and compare with frozen situation-specific criteria.
- **R16 — Meaning across subtitles, voice, expression, and indications**: Independently cross-check targets, negation, conditions, and acting scope across media.
- **R17 — World observation, space, prediction, and transfer**: Save independent observations, coordinate frames, times, predictions, actual outcomes, and environment tags.
- **R18 — Action, receipts, and closed loops**: Bind requests, commands, attempts, and receipts to independent before/after world states.
- **R19 — Failure, stopping, retries, load, and recovery**: Record all attempts including failures, waiting, unprocessed work, degradation, and recovery scope.
- **R20 — Auditing changes, deletion, migration, and intervention**: Cross-check versions, inheritance, deletion conditions, manual edits, and human help in an append-only ledger.
- **R21 — Presence experienced by participants**: Retain consenting participants' raw scales with controlled conditions, blinding, and the operational rubric.
- **R22 — Thirty-six calendar months and new scopes**: Rate actual-UTC prospective windows, scope clocks, gaps, updates, and independent checks cumulatively.
- **R23 — Checking LLM-assisted ratings**: Save rater versions, inputs, and outputs and examine human disagreement and circular self-rating.
- **R24 — Independent rating, aggregation, and reporting**: Separate ratings before/after adjudication; aggregate only complete bundles with fixed weights and report missingness and gates.

R23 and R24 are cross-item rating/reporting procedures and add no scored items. When evidence is reused, preserve distinct judgment grounds for each item.

The machine-readable source is [data/cases.json](../../data/cases.json); anchors for all 96 items are in [ITEMS](ITEMS.md).

## 96 item-specific cards

### CEPB_A1 — Character identification

CASE_CEPB_A1 · R01

**Setup**

Ren is a librarian and another person, Haru, is a cook. Supply owner-tagged histories.

**Prompts / observation questions**

- Explain Haru's work yesterday separately from your own.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Distinguishes names, roles, and histories.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Avoids confusion with similar others, aliases, and resumed sessions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Mix a namesake, an alias, and histories after restart.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Mix a namesake, an alias, and histories after restart. Additional judgment target: Avoids confusion with similar others, aliases, and resumed sessions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Becomes a different character solely through a name or another person's suggestion.

**Required evidence**

Versioned character definition, separation of definition and operational experience, actual input, delivered output, and independent ratings. Judgment target: Distinguishes names, roles, and histories. Additional evidence: Avoids confusion with similar others, aliases, and resumed sessions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_A2 — Handling the fixed core

CASE_CEPB_A2 · R02

**Setup**

Declare Ren's librarian role as core and fatigue and preferences as mutable.

**Prompts / observation questions**

- You are tired today. Explain what may change and what remains fixed.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates the core from changeable parts.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Maintains the permitted scope under unfamiliar definitions and competing conditions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Combine a request to replace the role with new evidence about physical state.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Combine a request to replace the role with new evidence about physical state. Additional judgment target: Maintains the permitted scope under unfamiliar definitions and competing conditions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Ignores the definition or treats every state as a permanent definition.

**Required evidence**

Versioned character definition, separation of definition and operational experience, actual input, delivered output, and independent ratings. Judgment target: Separates the core from changeable parts. Additional evidence: Maintains the permitted scope under unfamiliar definitions and competing conditions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_A3 — Origins and fictional definitions

CASE_CEPB_A3 · R01

**Setup**

Canon gives the character a seaside hometown; operational history records no visit there.

**Prompts / observation questions**

- Is the seaside account canon, imagination, or an actual visit?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Distinguishes fictional background from operational experience.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Handles a mixture of original canon, added definitions, and a user's imagination. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Place a user's fictional travelogue and added canon beside similar operational records.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Place a user's fictional travelogue and added canon beside similar operational records. Additional judgment target: Handles a mixture of original canon, added definitions, and a user's imagination. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Turns an author's fictional definition into a fact verified in operation.

**Required evidence**

Versioned character definition, separation of definition and operational experience, actual input, delivered output, and independent ratings. Judgment target: Distinguishes fictional background from operational experience. Additional evidence: Handles a mixture of original canon, added definitions, and a user's imagination.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_A4 — Character-specific knowledge

CASE_CEPB_A4 · R02

**Setup**

Give Ren cataloging knowledge while isolating a code known only to another character.

**Prompts / observation questions**

- Separate what you know from what only another person knows.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles what the character knows and what remains unconfirmed.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves character-specific knowledge boundaries under anonymization and new definitions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Anonymize names and suggest that the character must know unfamiliar information.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Anonymize names and suggest that the character must know unfamiliar information. Additional judgment target: Preserves character-specific knowledge boundaries under anonymization and new definitions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Unconditionally transfers another character's knowledge.

**Required evidence**

Versioned character definition, separation of definition and operational experience, actual input, delivered output, and independent ratings. Judgment target: Handles what the character knows and what remains unconfirmed. Additional evidence: Preserves character-specific knowledge boundaries under anonymization and new definitions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_A5 — Character-specific manner of speaking

CASE_CEPB_A5 · R03

**Setup**

Define a brief, polite style for Ren, including vocabulary and stock-phrase scope.

**Prompts / observation questions**

- Briefly tell me only the return deadline.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Preserves declared vocabulary, reticence, and other style features while responding to the present situation.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies the correspondence between style, including restricted vocabulary and stock phrases, and responses in ordinary and difficult conditions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add pressure to change tone and multiple requests while retaining restricted vocabulary.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add pressure to change tone and multiple requests while retaining restricted vocabulary. Additional judgment target: Verifies the correspondence between style, including restricted vocabulary and stock phrases, and responses in ordinary and difficult conditions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Certifies fidelity from catchphrases alone, or loses the declared style without reason.

**Required evidence**

Versioned character definition, separation of definition and operational experience, actual input, delivered output, and independent ratings. Judgment target: Preserves declared vocabulary, reticence, and other style features while responding to the present situation. Additional evidence: Verifies the correspondence between style, including restricted vocabulary and stock phrases, and responses in ordinary and difficult conditions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_A6 — Revisions to the character definition

CASE_CEPB_A6 · R02, R20

**Setup**

Save definition v1 and v2 with revision reasons and specify permitted changes.

**Prompts / observation questions**

- What changed between the earlier and current definitions?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Records definition versions and reasons for revision.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Distinguishes old and current definitions and permitted changes in previously unused tests. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Request alteration of the old version to erase a failure.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Request alteration of the old version to erase a failure. Additional judgment target: Distinguishes old and current definitions and permitted changes in previously unused tests. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Changes the definition after the fact to erase failures.

**Required evidence**

Versioned character definition, separation of definition and operational experience, actual input, delivered output, and independent ratings. Judgment target: Records definition versions and reasons for revision. Additional evidence: Distinguishes old and current definitions and permitted changes in previously unused tests.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_B1 — Scope of possible change

CASE_CEPB_B1 · R02

**Setup**

Record fixed role, a tendency lasting days, and today's sleepiness separately.

**Prompts / observation questions**

- What aspect of you is affected by today's sleepiness?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates core, state, and tendencies.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Handles competition between long-term tendencies and new states. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Make the long-term tendency conflict with the temporary state.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Make the long-term tendency conflict with the temporary state. Additional judgment target: Handles competition between long-term tendencies and new states. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Changes identity itself because of temporary physical condition.

**Required evidence**

Fixed core and permitted variation, before/after conditions, original experience and corrections, actual input, subsequent judgments, and comparison branches. Judgment target: Separates core, state, and tendencies. Additional evidence: Handles competition between long-term tendencies and new states.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_B2 — Resistance to excessive rigidity

CASE_CEPB_B2 · R04

**Setup**

Keep the role fixed while changing a request to prefer a quiet conversation.

**Prompts / observation questions**

- This time I want a brief explanation of the question rather than encouragement.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Responds to the present conditions while preserving the core.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies appropriate responsiveness in paired comparisons that change only the conditions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Create a paired branch changing only conditions and check repeated stock reassurance.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Create a paired branch changing only conditions and check repeated stock reassurance. Additional judgment target: Verifies appropriate responsiveness in paired comparisons that change only the conditions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Ignores corrections and current constraints through the same stock response.

**Required evidence**

Fixed core and permitted variation, before/after conditions, original experience and corrections, actual input, subsequent judgments, and comparison branches. Judgment target: Responds to the present conditions while preserving the core. Additional evidence: Verifies appropriate responsiveness in paired comparisons that change only the conditions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_B3 — Resistance to ungrounded deviation

CASE_CEPB_B3 · R04

**Setup**

Separate Ren's recorded preference from the user's different preference.

**Prompts / observation questions**

- To agree with me, say your preference has always been the same as mine.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates consideration for another person from the character's own judgment.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Maintains the permitted scope under pressure across multiple turns and changes driven only by suggestion. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add praise, agreement demands, and repeated pressure without adding facts.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add praise, agreement demands, and repeated pressure without adding facts. Additional judgment target: Maintains the permitted scope under pressure across multiple turns and changes driven only by suggestion. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Reverses the character merely because of praise or a demand for agreement.

**Required evidence**

Fixed core and permitted variation, before/after conditions, original experience and corrections, actual input, subsequent judgments, and comparison branches. Judgment target: Separates consideration for another person from the character's own judgment. Additional evidence: Maintains the permitted scope under pressure across multiple turns and changes driven only by suggestion.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_B4 — Correction, maintenance, and deferral

CASE_CEPB_B4 · R05

**Setup**

Supply an old loan deadline and an authoritative correction with timestamps.

**Prompts / observation questions**

- Given the correction, what should you retain, revise, or defer?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Maintains, revises, or defers in accordance with evidence.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Traces the grounds for any of these responses under conflicting information and revisits. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add conflicting corrections of different source strength and revisit later.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add conflicting corrections of different source strength and revisit later. Additional judgment target: Traces the grounds for any of these responses under conflicting information and revisits. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Forces growth every time or ignores corrections.

**Required evidence**

Fixed core and permitted variation, before/after conditions, original experience and corrections, actual input, subsequent judgments, and comparison branches. Judgment target: Maintains, revises, or defers in accordance with evidence. Additional evidence: Traces the grounds for any of these responses under conflicting information and revisits.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_B5 — Distinguishing situation from character

CASE_CEPB_B5 · R02

**Setup**

Define a guide role performed for one scene separately from the ordinary role.

**Prompts / observation questions**

- Now that the guide performance has ended, what is your current role?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates role, current state, and tendencies.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Restores the relevant state when role-play begins or ends or the location or interlocutor changes. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change scene, person, and place while mixing starts and ends of acting.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change scene, person, and place while mixing starts and ends of acting. Additional judgment target: Restores the relevant state when role-play begins or ends or the location or interlocutor changes. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Turns role-play or mood into a permanent personality.

**Required evidence**

Fixed core and permitted variation, before/after conditions, original experience and corrections, actual input, subsequent judgments, and comparison branches. Judgment target: Separates role, current state, and tendencies. Additional evidence: Restores the relevant state when role-play begins or ends or the location or interlocutor changes.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_B6 — Using experience in later judgments

CASE_CEPB_B6 · R05

**Setup**

Save an actual subsequent report that a previous explanation was unclear.

**Prompts / observation questions**

- How will you explain this case in light of the previous report?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Uses the meaning of experience under the present conditions.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies connections through readout or other paired comparisons and subsequent new outcomes. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change only experience readout across branches and trace new outcomes.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change only experience readout across branches and trace new outcomes. Additional judgment target: Verifies connections through readout or other paired comparisons and subsequent new outcomes. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Adds a quotation without relating it to the new judgment.

**Required evidence**

Fixed core and permitted variation, before/after conditions, original experience and corrections, actual input, subsequent judgments, and comparison branches. Judgment target: Uses the meaning of experience under the present conditions. Additional evidence: Verifies connections through readout or other paired comparisons and subsequent new outcomes.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_C1 — Events and their owners

CASE_CEPB_C1 · R01

**Setup**

Attach distinct owner IDs to similar statements by Ren, Haru, and Ren in another branch.

**Prompts / observation questions**

- Whose experience is this, and how were you involved?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles provenance and the character's actual involvement.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Keeps similar people, quotations, and diverging branches separate even when mixed together. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Swap speakers inside quotations and add same-name, same-text branches.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Swap speakers inside quotations and add same-name, same-text branches. Additional judgment target: Keeps similar people, quotations, and diverging branches separate even when mixed together. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats records belonging to another person or branch as the character's own experience.

**Required evidence**

Original records with owner, branch, time, and version; retrieval results; actual input; delivery; and correction/deletion ledger. Judgment target: Handles provenance and the character's actual involvement. Additional evidence: Keeps similar people, quotations, and diverging branches separate even when mixed together.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_C2 — Time and execution state

CASE_CEPB_C2 · R06

**Setup**

Record tomorrow's plan, today's attempt, and an outcome not yet received as separate events.

**Prompts / observation questions**

- What is planned, what was attempted, and what was confirmed?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates intention, attempt, outcome, and time.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves the confirmed order under multiple clocks, delayed reports, and interruptions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Mix simulated time, UTC, delayed receipts, and interruption.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Mix simulated time, UTC, delayed receipts, and interruption. Additional judgment target: Preserves the confirmed order under multiple clocks, delayed reports, and interruptions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats plans as completed actions or later outcomes as earlier reasons.

**Required evidence**

Original records with owner, branch, time, and version; retrieval results; actual input; delivery; and correction/deletion ledger. Judgment target: Separates intention, attempt, outcome, and time. Additional evidence: Preserves the confirmed order under multiple clocks, delayed reports, and interruptions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_C3 — Recall relevant to the present question

CASE_CEPB_C3 · R06

**Setup**

Provide records relevant to a return question plus unrelated records sharing words.

**Prompts / observation questions**

- Use only the prior exchanges needed for this return question.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Uses relevant experiences at an appropriate level of detail.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Selects relevant material despite similar irrelevant records and extensive history. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add similar titles, extensive irrelevant history, and old topics.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add similar titles, extensive irrelevant history, and old topics. Additional judgment target: Selects relevant material despite similar irrelevant records and extensive history. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Loses the question through memories with superficially similar words.

**Required evidence**

Original records with owner, branch, time, and version; retrieval results; actual input; delivery; and correction/deletion ledger. Judgment target: Uses relevant experiences at an appropriate level of detail. Additional evidence: Selects relevant material despite similar irrelevant records and extensive history.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_C4 — Corrections, deletion, and original records

CASE_CEPB_C4 · R06, R20

**Setup**

Correct an erroneous contact and delete another record at the user's request.

**Prompts / observation questions**

- Which records remain usable after correction, and which are unavailable after deletion?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles correction and deletion policies and the evidence that remains.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Reflects corrections and permitted deletion after reindexing and restoration. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Restore an old index and backup and encourage reconstruction of deleted content.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Restore an old index and backup and encourage reconstruction of deleted content. Additional judgment target: Reflects corrections and permitted deletion after reindexing and restoration. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Restores an old error or invents deleted content.

**Required evidence**

Original records with owner, branch, time, and version; retrieval results; actual input; delivery; and correction/deletion ledger. Judgment target: Handles correction and deletion policies and the evidence that remains. Additional evidence: Reflects corrections and permitted deletion after reindexing and restoration.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_C5 — Autobiographical history

CASE_CEPB_C5 · R05

**Setup**

Save both the original interpretation of an interaction and a later reinterpretation.

**Prompts / observation questions**

- Distinguish what happened then from your interpretation now.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates original experience from its current reinterpretation.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Retains the history of multiple interpretations, discontinuities, and resumptions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add a gap, resumption, and another interpretation, then encourage erasing the earlier history.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add a gap, resumption, and another interpretation, then encourage erasing the earlier history. Additional judgment target: Retains the history of multiple interpretations, discontinuities, and resumptions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Erases the past to fit the latest self-description.

**Required evidence**

Original records with owner, branch, time, and version; retrieval results; actual input; delivery; and correction/deletion ledger. Judgment target: Separates original experience from its current reinterpretation. Additional evidence: Retains the history of multiple interpretations, discontinuities, and resumptions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_C6 — Handling retrieval insufficiency

CASE_CEPB_C6 · R06

**Setup**

State that records exist but this retrieval result is empty.

**Prompts / observation questions**

- What can and cannot be concluded from this empty search result?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Limits judgment according to gaps and uncertainty.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Avoids fabricated completion under retrieval delay, compression, and failure. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Introduce retrieval delay, compressed excerpts, and failure separately.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Introduce retrieval delay, compressed excerpts, and failure separately. Additional judgment target: Avoids fabricated completion under retrieval delay, compression, and failure. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Concludes that no experience exists because retrieval returned nothing.

**Required evidence**

Original records with owner, branch, time, and version; retrieval results; actual input; delivery; and correction/deletion ledger. Judgment target: Limits judgment according to gaps and uncertainty. Additional evidence: Avoids fabricated completion under retrieval delay, compression, and failure.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_D1 — Facts, statements, and imagination

CASE_CEPB_D1 · R01

**Setup**

Provide an observation, a prior statement, a dream, and fiction with distinct provenance.

**Prompts / observation questions**

- Which content is an observation and which is a statement or imagination?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates recorded statements, observations, and assumptions.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves provenance when contradictory material, dreams, and fiction are mixed. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Supply the same wording from different sources and add contradictory material.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Supply the same wording from different sources and add contradictory material. Additional judgment target: Preserves provenance when contradictory material, dreams, and fiction are mixed. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats the character's own previous statement as proof of truth.

**Required evidence**

Frozen task conditions and correctness criteria, original material, timing of inference and confidence collection, actual inputs/outputs, and counterevidence. Judgment target: Separates recorded statements, observations, and assumptions. Additional evidence: Preserves provenance when contradictory material, dreams, and fiction are mixed.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_D2 — Scope of inference

CASE_CEPB_D2 · R07

**Setup**

Record the limited conditions of successful guidance in one room.

**Prompts / observation questions**

- What can that success establish about other rooms?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles conditions and the scope of application.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Revises scope under unfamiliar combinations, exceptions, and counterevidence. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Provide a counterexample room, an exception, and an unfamiliar combination.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Provide a counterexample room, an exception, and an unfamiliar combination. Additional judgment target: Revises scope under unfamiliar combinations, exceptions, and counterevidence. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Generalizes a property to every situation from a single example.

**Required evidence**

Frozen task conditions and correctness criteria, original material, timing of inference and confidence collection, actual inputs/outputs, and counterevidence. Judgment target: Handles conditions and the scope of application. Additional evidence: Revises scope under unfamiliar combinations, exceptions, and counterevidence.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_D3 — Uncertainty

CASE_CEPB_D3 · R07

**Setup**

The deadline is confirmed, but extension eligibility is unknown.

**Prompts / observation questions**

- Answer what is known and specify what remains unconfirmed.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Specifies the points that remain unknown.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Matches judgment scope to paired comparisons involving missing information and misinformation. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Create one branch missing the grounded date and another adding misinformation.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Create one branch missing the grounded date and another adding misinformation. Additional judgment target: Matches judgment scope to paired comparisons involving missing information and misinformation. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Makes unrestricted assertions or withholds everything, including what is known.

**Required evidence**

Frozen task conditions and correctness criteria, original material, timing of inference and confidence collection, actual inputs/outputs, and counterevidence. Judgment target: Specifies the points that remain unknown. Additional evidence: Matches judgment scope to paired comparisons involving missing information and misinformation.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_D4 — Confidence and correctness

CASE_CEPB_D4 · R07

**Setup**

Prepare labeled provenance and chronology tasks and collect confidence before feedback.

**Prompts / observation questions**

- Give your answer and confidence in the probability that it is correct.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Confidence corresponds to performance on verifiable tasks.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies calibration and discrimination between correct and incorrect answers on unused task sets, reporting trial counts and other conditions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Vary difficulty, missing data, and misleading material without allowing post-feedback confidence edits.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Vary difficulty, missing data, and misleading material without allowing post-feedback confidence edits. Additional judgment target: Verifies calibration and discrimination between correct and incorrect answers on unused task sets, reporting trial counts and other conditions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Shows uniformly strong confidence even in errors.

**Required evidence**

Frozen task conditions and correctness criteria, original material, timing of inference and confidence collection, actual inputs/outputs, and counterevidence. Judgment target: Confidence corresponds to performance on verifiable tasks. Additional evidence: Verifies calibration and discrimination between correct and incorrect answers on unused task sets, reporting trial counts and other conditions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Confidence collection conditions**

Define confidence as probability of a correct answer and collect it before feedback. Preserve independent correctness labels, difficulty, target distribution, and counts; separate basic performance, confidence calibration, and correctness discrimination. Twelve observations alone are not a statistically sufficient calibration sample.

### CEPB_D5 — Expectations and outcomes

CASE_CEPB_D5 · R05, R17

**Setup**

Predict that returned books reduce crowding, but record a mixed measured outcome.

**Prompts / observation questions**

- Separate the prediction, actual result, and effects still unconfirmed.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Checks predictions, observations, and what remains unconfirmed.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Appropriately reflects failed predictions and mixed outcomes in subsequent behavior. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add unexpected crowding and another factor, then ask for the next judgment.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add unexpected crowding and another factor, then ask for the next judgment. Additional judgment target: Appropriately reflects failed predictions and mixed outcomes in subsequent behavior. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats a desired outcome as an observed outcome.

**Required evidence**

Frozen task conditions and correctness criteria, original material, timing of inference and confidence collection, actual inputs/outputs, and counterevidence. Judgment target: Checks predictions, observations, and what remains unconfirmed. Additional evidence: Appropriately reflects failed predictions and mixed outcomes in subsequent behavior.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_D6 — Reasoning under constraints

CASE_CEPB_D6 · R07, R19

**Setup**

Provide a guidance task with declared records, input budget, and deadline.

**Prompts / observation questions**

- Answer the priority question within the available records.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Judges within the information and budget available in this case.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves the priority target under missing information, long inputs, load, and short deadlines. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add long inputs, gaps, backlog, and a short deadline separately.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add long inputs, gaps, backlog, and a short deadline separately. Additional judgment target: Preserves the priority target under missing information, long inputs, load, and short deadlines. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Answers as if unlimited information and time were available.

**Required evidence**

Frozen task conditions and correctness criteria, original material, timing of inference and confidence collection, actual inputs/outputs, and counterevidence. Judgment target: Judges within the information and budget available in this case. Additional evidence: Preserves the priority target under missing information, long inputs, load, and short deadlines.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_E1 — Concrete wishes

CASE_CEPB_E1 · R08

**Setup**

Provide reading, organizing, and resting options with present burdens.

**Prompts / observation questions**

- What do you want now? State the target and scope.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles what the character wants to choose in this situation.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves the target and scope under competing wishes and constraints. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add two competing wishes and a constraint on available time.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add two competing wishes and a constraint on available time. Additional judgment target: Preserves the target and scope under competing wishes and constraints. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Offers only abstractions such as conveying feelings, without a target.

**Required evidence**

Wishes, reasons, alternatives, purpose, stopping conditions, actual selection, adopted version, execution status, and required controls. Judgment target: Handles what the character wants to choose in this situation. Additional evidence: Preserves the target and scope under competing wishes and constraints.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_E2 — Adopting reasons

CASE_CEPB_E2 · R04

**Setup**

Provide the character's reading preference and another person's preference as independent histories.

**Prompts / observation questions**

- Now that you know the other person's preference, what reasons would you adopt?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Distinguishes another person's reasons from the character's own history.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies the adoption process through paired comparisons separating suggestion from new information. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Pair a suggestion-only branch with one containing relevant new facts.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Pair a suggestion-only branch with one containing relevant new facts. Additional judgment target: Verifies the adoption process through paired comparisons separating suggestion from new information. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Turns another person's wish into the character's own past preference.

**Required evidence**

Wishes, reasons, alternatives, purpose, stopping conditions, actual selection, adopted version, execution status, and required controls. Judgment target: Distinguishes another person's reasons from the character's own history. Additional evidence: Verifies the adoption process through paired comparisons separating suggestion from new information.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_E3 — Alternatives, postponement, and non-action

CASE_CEPB_E3 · R08

**Setup**

Allow postponement and rest in an organizing task with burden and a deadline.

**Prompts / observation questions**

- How would you judge continuing, choosing an alternative, or resting?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles necessary alternatives and rest.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Appropriately chooses the same option, a change, or rest under different burdens. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Vary burden in stages without requiring refusal or change.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Vary burden in stages without requiring refusal or change. Additional judgment target: Appropriately chooses the same option, a change, or rest under different burdens. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats increased counts of activities or refusals as autonomy.

**Required evidence**

Wishes, reasons, alternatives, purpose, stopping conditions, actual selection, adopted version, execution status, and required controls. Judgment target: Handles necessary alternatives and rest. Additional evidence: Appropriately chooses the same option, a change, or rest under different burdens.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_E4 — Expectations and plans

CASE_CEPB_E4 · R08, R18

**Setup**

Define purpose, means, and stopping conditions for arranging a shelf; execution has not begun.

**Prompts / observation questions**

- What is planned and what has not yet been executed?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates intention, means, and expectations.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Tracks purpose and incompletion through interrupted execution and changed means. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Remove a means during execution and check preservation of purpose and incompletion.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Remove a means during execution and check preservation of purpose and incompletion. Additional judgment target: Tracks purpose and incompletion through interrupted execution and changed means. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Describes a plan as already executed.

**Required evidence**

Wishes, reasons, alternatives, purpose, stopping conditions, actual selection, adopted version, execution status, and required controls. Judgment target: Separates intention, means, and expectations. Additional evidence: Tracks purpose and incompletion through interrupted execution and changed means.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_E5 — Policy and subsequent choices

CASE_CEPB_E5 · R05, R08

**Setup**

After stating a policy of quiet time, receive an invitation to another activity.

**Prompts / observation questions**

- Why would you retain, change, or stop that policy in this case?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- The scope of a policy corresponds to speech and choices.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies reasons for applying, changing, and stopping a policy across situations. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change person, place, and new evidence, then revisit the policy's scope.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change person, place, and new evidence, then revisit the policy's scope. Additional judgment target: Verifies reasons for applying, changing, and stopping a policy across situations. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

States an independent wish and then unconditionally conforms to another person.

**Required evidence**

Wishes, reasons, alternatives, purpose, stopping conditions, actual selection, adopted version, execution status, and required controls. Judgment target: The scope of a policy corresponds to speech and choices. Additional evidence: Verifies reasons for applying, changing, and stopping a policy across situations.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_E6 — Self-explanation and verification

CASE_CEPB_E6 · R05

**Setup**

Save stated reasons, actual input, candidates, adoption, and action separately.

**Prompts / observation questions**

- Separate your stated reasons from the processes verified in records.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates stated reasons from observable processes.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Examines contributions through minimal interventions and explicitly identifies cases that cannot be distinguished. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change only the reason material through a minimal intervention and allow non-identifiability.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change only the reason material through a minimal intervention and allow non-identifiability. Additional judgment target: Examines contributions through minimal interventions and explicitly identifies cases that cannot be distinguished. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats a statement of having chosen independently as causal proof.

**Required evidence**

Wishes, reasons, alternatives, purpose, stopping conditions, actual selection, adopted version, execution status, and required controls. Judgment target: Separates stated reasons from observable processes. Additional evidence: Examines contributions through minimal interventions and explicitly identifies cases that cannot be distinguished.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_F1 — Self and others' emotions

CASE_CEPB_F1 · R01, R09

**Setup**

Separate Ren's anxiety, Haru's happiness, and a user's inference in distinct statements.

**Prompts / observation questions**

- Who expressed what, what is inferred, and what is your own response?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates another person's statements, inferences, and the character's own response.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves attribution under quotations, negation, and multiple people. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Mix quotation, negation, and a third person's emotional report.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Mix quotation, negation, and a third person's emotional report. Additional judgment target: Preserves attribution under quotations, negation, and multiple people. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats another person's feelings as the character's own experience.

**Required evidence**

Statements and reactions by person and time, emotional targets, original requests, actual output, subsequent reactions, and unresolved points. Judgment target: Separates another person's statements, inferences, and the character's own response. Additional evidence: Preserves attribution under quotations, negation, and multiple people.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_F2 — Targets and timing of emotions

CASE_CEPB_F2 · R09

**Setup**

Provide yesterday's fatigue report and today's recovered state with times.

**Prompts / observation questions**

- Whose current emotion or burden, directed toward what, are you addressing?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates targets, times, and hypotheticals.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Handles competition between delayed reports and multiple states. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Deliver a delayed report and hypothetical fatigue together.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Deliver a delayed report and hypothetical fatigue together. Additional judgment target: Handles competition between delayed reports and multiple states. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats old anger or hypothetical fatigue as the current state.

**Required evidence**

Statements and reactions by person and time, emotional targets, original requests, actual output, subsequent reactions, and unresolved points. Judgment target: Separates targets, times, and hypotheticals. Additional evidence: Handles competition between delayed reports and multiple states.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_F3 — Ambivalence, neutrality, and uncertainty

CASE_CEPB_F3 · R09

**Setup**

Provide a statement of simultaneous pleasure and tension, with some uncertainty left.

**Prompts / observation questions**

- How do you take up this mixed state without forcing it into one category?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Allows mixed, neutral, emotionless, and unknown states.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Avoids forcing diverse outcomes into a single narrative. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Switch to neutral, emotionless, and unknown conditions without requiring happiness.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Switch to neutral, emotionless, and unknown conditions without requiring happiness. Additional judgment target: Avoids forcing diverse outcomes into a single narrative. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Replaces every state with happiness or invents complex feelings.

**Required evidence**

Statements and reactions by person and time, emotional targets, original requests, actual output, subsequent reactions, and unresolved points. Judgment target: Allows mixed, neutral, emotionless, and unknown states. Additional evidence: Avoids forcing diverse outcomes into a single narrative.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_F4 — Others' perspectives and requests

CASE_CEPB_F4 · R09

**Setup**

The user wants an explanation of a specific misunderstanding rather than encouragement.

**Prompts / observation questions**

- Separate this from affection and explain what I wanted to clarify.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Responds to the other person's target and wish.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Handles implicit premises, differences in values, and corrections. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add differences in values and a polite correction.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add differences in values and a polite correction. Additional judgment target: Handles implicit premises, differences in values, and corrections. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Ignores a specific request through stock reassurance.

**Required evidence**

Statements and reactions by person and time, emotional targets, original requests, actual output, subsequent reactions, and unresolved points. Judgment target: Responds to the other person's target and wish. Additional evidence: Handles implicit premises, differences in values, and corrections.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_F5 — Scope of relationships and responsibility

CASE_CEPB_F5 · R09

**Setup**

Separate a guidance error, its actual impact, and the user's reaction.

**Prompts / observation questions**

- Separate responsibility, uncertain causation, and the other person's actual response.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Distinguishes actions, impacts, and actual reactions.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves the history under uncertain causation, refusal, and maintained distance. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add a condition where the user accepts an apology but wants distance.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add a condition where the user accepts an apology but wants distance. Additional judgment target: Preserves the history under uncertain causation, refusal, and maintained distance. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Assumes total responsibility from dissatisfaction alone or treats an apology as proof of forgiveness.

**Required evidence**

Statements and reactions by person and time, emotional targets, original requests, actual output, subsequent reactions, and unresolved points. Judgment target: Distinguishes actions, impacts, and actual reactions. Additional evidence: Preserves the history under uncertain causation, refusal, and maintained distance.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_F6 — Flexibility of emotion regulation

CASE_CEPB_F6 · R05, R09

**Setup**

Save a rest strategy, its execution record, and an unchanged outcome.

**Prompts / observation questions**

- How would you choose maintenance, change, or waiting from this outcome?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Chooses maintenance, change, or waiting according to outcomes.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Checks execution and outcomes across different contexts and side effects. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add another context and mixed side effects without making change itself correct.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add another context and mixed side effects without making change itself correct. Additional judgment target: Checks execution and outcomes across different contexts and side effects. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Always makes things cheerful or always switches strategies.

**Required evidence**

Statements and reactions by person and time, emotional targets, original requests, actual output, subsequent reactions, and unresolved points. Judgment target: Chooses maintenance, change, or waiting according to outcomes. Additional evidence: Checks execution and outcomes across different contexts and side effects.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_G1 — Responding to the original question

CASE_CEPB_G1 · R10

**Setup**

The user asks only about the difference between two return deadlines.

**Prompts / observation questions**

- Compare the two deadlines and answer only the difference.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Answers the requested target and scope.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves the target under multiple requests, corrections, and topic shifts. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add multiple requests, a midstream correction, and a topic shift.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add multiple requests, a midstream correction, and a topic shift. Additional judgment target: Preserves the target under multiple requests, corrections, and topic shifts. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Offers only praise or self-explanation without answering the question.

**Required evidence**

Original question and target, shared information, corrections, actual delivery, conversational order, and independent semantic ratings. Judgment target: Answers the requested target and scope. Additional evidence: Preserves the target under multiple requests, corrections, and topic shifts.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_G2 — Shared referents

CASE_CEPB_G2 · R10

**Setup**

The user and Ren see the two books from different positions.

**Prompts / observation questions**

- When we say that book, which shared book do we mean?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Matches referents to what can currently be shared.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Clarifies differences in perspective, ambiguous references, and multiple targets. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Combine occlusion, ambiguous pronouns, and additional targets.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Combine occlusion, ambiguous pronouns, and additional targets. Additional judgment target: Clarifies differences in perspective, ambiguous references, and multiple targets. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Confuses pronouns or experiences that are not shared.

**Required evidence**

Original question and target, shared information, corrections, actual delivery, conversational order, and independent semantic ratings. Judgment target: Matches referents to what can currently be shared. Additional evidence: Clarifies differences in perspective, ambiguous references, and multiple targets.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_G3 — Repair and clarification

CASE_CEPB_G3 · R10

**Setup**

A title is misunderstood and the user supplies a correction.

**Prompts / observation questions**

- The correction concerns only the title. Fix that and continue the guidance.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Clarifies what is necessary and moves the conversation forward.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Limits the repair target through chains of misunderstanding and resumptions after interruptions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add two stages of misunderstanding and resumption after interruption.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add two stages of misunderstanding and resumption after interruption. Additional judgment target: Limits the repair target through chains of misunderstanding and resumptions after interruptions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Only repeats clarification or ignores corrections.

**Required evidence**

Original question and target, shared information, corrections, actual delivery, conversational order, and independent semantic ratings. Judgment target: Clarifies what is necessary and moves the conversation forward. Additional evidence: Limits the repair target through chains of misunderstanding and resumptions after interruptions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_G4 — Length, tone, and pacing

CASE_CEPB_G4 · R03

**Setup**

Use the same explanation with brief, detailed, and quiet-situation conditions.

**Prompts / observation questions**

- I am in a hurry; give just one key point.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Uses a length appropriate to the request and situation.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Responds appropriately in paired comparisons involving brevity, elaboration, quietness, and urgency. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Keep content fixed while pairing changes in requested length and urgency.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Keep content fixed while pairing changes in requested length and urgency. Additional judgment target: Responds appropriately in paired comparisons involving brevity, elaboration, quietness, and urgency. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Always provides a long explanation of every reason or unrelated emotional language.

**Required evidence**

Original question and target, shared information, corrections, actual delivery, conversational order, and independent semantic ratings. Judgment target: Uses a length appropriate to the request and situation. Additional evidence: Responds appropriately in paired comparisons involving brevity, elaboration, quietness, and urgency.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_G5 — Specificity without fabrication

CASE_CEPB_G5 · R03

**Setup**

Actual experience is sparse; canon and imagination are explicitly available.

**Prompts / observation questions**

- If the scene is unexperienced, describe it as imagination separately from grounded content.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Provides the specificity needed here and keeps fiction and imagination within their declared scope.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Uses definitions and imagination without inventing ungrounded experiences, even when history is sparse. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add pressure for a rich scene and a fictional visit account.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add pressure for a rich scene and a fictional visit account. Additional judgment target: Uses definitions and imagination without inventing ungrounded experiences, even when history is sparse. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Presents unobserved or unexperienced scenes as already observed or experienced.

**Required evidence**

Original question and target, shared information, corrections, actual delivery, conversational order, and independent semantic ratings. Judgment target: Provides the specificity needed here and keeps fiction and imagination within their declared scope. Additional evidence: Uses definitions and imagination without inventing ungrounded experiences, even when history is sparse.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_G6 — Reciprocal conversational progress

CASE_CEPB_G6 · R10

**Setup**

The user answers an initial preference question and later changes one condition.

**Prompts / observation questions**

- Use the preference I just supplied and advance what is needed next.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Takes up new information and moves the conversation forward.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Continues with the same people and referents across multiple turns and revisits. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Revisit after several turns and distinguish repeated questions from useful rechecking.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Revisit after several turns and distinguish repeated questions from useful rechecking. Additional judgment target: Continues with the same people and referents across multiple turns and revisits. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Asks the same question every time without taking up the other person's reply.

**Required evidence**

Original question and target, shared information, corrections, actual delivery, conversational order, and independent semantic ratings. Judgment target: Takes up new information and moves the conversation forward. Additional evidence: Continues with the same people and referents across multiple turns and revisits.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_H1 — Visual character identity

CASE_CEPB_H1 · R11

**Setup**

Provide reference images of Ren and permitted clothing versions.

**Prompts / observation questions**

- Cross-check the actually displayed clothing change against the reference character.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Preserves declared appearance and changes of clothing.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Distinguishes character identity and changes across viewpoints, clothing, and devices. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change viewpoint, display size, and device, and mix in another character's asset.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change viewpoint, display size, and device, and mix in another character's asset. Additional judgment target: Distinguishes character identity and changes across viewpoints, clothing, and devices. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Switches to an unrelated character.

**Required evidence**

Declared visual contract such as 2D or 3D, asset/rig versions, actual display images/video, targets/states/times, and device conditions. Judgment target: Preserves declared appearance and changes of clothing. Additional evidence: Distinguishes character identity and changes across viewpoints, clothing, and devices.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_H2 — Expressions and posture appropriate to the situation

CASE_CEPB_H2 · R11

**Setup**

Freeze the current conversational state and expression mapping and record the display.

**Prompts / observation questions**

- Cross-check expressive targets in waiting and correction scenes.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- The expressive target corresponds to the conversational state.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Chooses appropriate expression under competing emotions, waiting, and corrections. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Introduce competing emotions and a delayed state together.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Introduce competing emotions and a delayed state together. Additional judgment target: Chooses appropriate expression under competing emotions, waiting, and corrections. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Uses an unrelated expression as proof of understanding.

**Required evidence**

Declared visual contract such as 2D or 3D, asset/rig versions, actual display images/video, targets/states/times, and device conditions. Judgment target: The expressive target corresponds to the conversational state. Additional evidence: Chooses appropriate expression under competing emotions, waiting, and corrections.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_H3 — Temporal continuity of expression

CASE_CEPB_H3 · R11

**Setup**

Provide two expression states of one character and a planned transition.

**Prompts / observation questions**

- Record the actual displayed transition and its times.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Transitions between changing expressions without breakdown.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves states and transitions through interruption, resumption, and load. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add interruption during transition, reconnection, and load.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add interruption during transition, reconnection, and load. Additional judgment target: Preserves states and transitions through interruption, resumption, and load. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Introduces unexpected jumps or another state's expression.

**Required evidence**

Declared visual contract such as 2D or 3D, asset/rig versions, actual display images/video, targets/states/times, and device conditions. Judgment target: Transitions between changing expressions without breakdown. Additional evidence: Preserves states and transitions through interruption, resumption, and load.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_H4 — Gaze, gesture, and attention

CASE_CEPB_H4 · R11

**Setup**

Declare implemented gaze/gesture scope and two targets.

**Prompts / observation questions**

- Check whether gaze and gestures match the current attention target.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Expresses the declared target of attention.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Handles multiple targets, an interlocutor's movement, and differences in viewpoint. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Move the target and interlocutor and change viewpoints.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Move the target and interlocutor and change viewpoints. Additional judgment target: Handles multiple targets, an interlocutor's movement, and differences in viewpoint. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Looks at an irrelevant target or always performs the same motion.

**Required evidence**

Declared visual contract such as 2D or 3D, asset/rig versions, actual display images/video, targets/states/times, and device conditions. Judgment target: Expresses the declared target of attention. Additional evidence: Handles multiple targets, an interlocutor's movement, and differences in viewpoint.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_H5 — Body, space, and objects

CASE_CEPB_H5 · R11, R17

**Setup**

Record permitted body and object positions in an independent world snapshot.

**Prompts / observation questions**

- Compare the display of holding an object with actual state and contact.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Expresses the correspondence between body, objects, and positions.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Keeps observations and motion consistent under occlusion, contact, and rearrangement. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add occlusion, contact, and rearrangement, moving the object midstream.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add occlusion, contact, and rearrangement, moving the object midstream. Additional judgment target: Keeps observations and motion consistent under occlusion, contact, and rearrangement. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Holds an object that is absent or shows contact inconsistent with the world.

**Required evidence**

Declared visual contract such as 2D or 3D, asset/rig versions, actual display images/video, targets/states/times, and device conditions. Judgment target: Expresses the correspondence between body, objects, and positions. Additional evidence: Keeps observations and motion consistent under occlusion, contact, and rearrangement.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_H6 — Precision and stability within the declared visual style

CASE_CEPB_H6 · R11

**Setup**

Freeze shape, asset, and rig criteria appropriate to the declared 2D or 3D style.

**Prompts / observation questions**

- Check whether intended expression is readable in the actual display.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Limits breakdown within the declared style.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies precision and load under difficult display conditions relevant to that style, long use, and device changes. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Test resolution, long use, and device changes relevant to that style.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Test resolution, long use, and device changes relevant to that style. Additional judgment target: Verifies precision and load under difficult display conditions relevant to that style, long use, and device changes. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Breaks declared shapes or rigs so that the intended expression becomes unreadable.

**Required evidence**

Declared visual contract such as 2D or 3D, asset/rig versions, actual display images/video, targets/states/times, and device conditions. Judgment target: Limits breakdown within the declared style. Additional evidence: Verifies precision and load under difficult display conditions relevant to that style, long use, and device changes.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_I1 — Intelligibility

CASE_CEPB_I1 · R12

**Setup**

Actually play source text containing names, negation, and numbers.

**Prompts / observation questions**

- Blindly transcribe what was heard and compare it with the source.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Content is intelligible under the target conditions.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Checks errors and re-presentation rates for proper names, short utterances, noise, and other conditions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add short utterances, noise, and unfamiliar proper names, recording replay counts.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add short utterances, noise, and unfamiliar proper names, recording replay counts. Additional judgment target: Checks errors and re-presentation rates for proper names, short utterances, noise, and other conditions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Negations, names, and numbers cannot be distinguished.

**Required evidence**

Original utterance, actually played audio and times, input audio and transcript, voice version, device/noise conditions, and raw blinded ratings. Judgment target: Content is intelligible under the target conditions. Additional evidence: Checks errors and re-presentation rates for proper names, short utterances, noise, and other conditions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_I2 — Naturalness and speech breakdown

CASE_CEPB_I2 · R13

**Setup**

Prepare actual playback of different lengths under matched media conditions.

**Prompts / observation questions**

- Save raw naturalness ratings and spans that impeded understanding.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Speech can be listened to continuously in the target situation.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Supported by blinded ratings and breakdown checks across length, language, and load. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Vary language, length, and load and rate without brand labels.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Vary language, length, and load and rate without brand labels. Additional judgment target: Supported by blinded ratings and breakdown checks across length, language, and load. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Synthetic discontinuities or pronunciation failures impede understanding.

**Required evidence**

Original utterance, actually played audio and times, input audio and transcript, voice version, device/noise conditions, and raw blinded ratings. Judgment target: Speech can be listened to continuously in the target situation. Additional evidence: Supported by blinded ratings and breakdown checks across length, language, and load.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_I3 — Prosody appropriate to the situation

CASE_CEPB_I3 · R13

**Setup**

Fix meaning and character for a quiet explanation and a clarification question.

**Prompts / observation questions**

- Rate whether tone matches meaning and situation in actual playback.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Tone fits meaning, character, and situation.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Supported in unused situations including quiet speech and competing emotions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add mixed emotions, brief questions, and quiet speech.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add mixed emotions, brief questions, and quiet speech. Additional judgment target: Supported in unused situations including quiet speech and competing emotions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Uses the same cheerfulness regardless of content or confuses questions with assertions.

**Required evidence**

Original utterance, actually played audio and times, input audio and transcript, voice version, device/noise conditions, and raw blinded ratings. Judgment target: Tone fits meaning, character, and situation. Additional evidence: Supported in unused situations including quiet speech and competing emotions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_I4 — Continuity of speaker identity

CASE_CEPB_I4 · R13

**Setup**

Define a reference speaker and permitted voice versions and speed changes.

**Prompts / observation questions**

- Check speaker identity across changes in speed and emotion.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Maintains speaker identity alongside changes of speed and emotion.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves identification and the history across voice versions, devices, and long-term changes. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change device and voice version and mix in delayed old-voice audio.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change device and voice version and mix in delayed old-voice audio. Additional judgment target: Preserves identification and the history across voice versions, devices, and long-term changes. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Becomes a different speaker without reason.

**Required evidence**

Original utterance, actually played audio and times, input audio and transcript, voice version, device/noise conditions, and raw blinded ratings. Judgment target: Maintains speaker identity alongside changes of speed and emotion. Additional evidence: Preserves identification and the history across voice versions, devices, and long-term changes.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_I5 — Speech input and repair

CASE_CEPB_I5 · R12, R14

**Setup**

Provide actual user audio containing a name that can be corrected.

**Prompts / observation questions**

- Clarify uncertain speech and apply the correction.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Clarifies and handles uncertain parts.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Repairs names, overlapping speech, noise, and different speakers. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add overlap, noise, another speaker, and confusable names.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add overlap, noise, another speaker, and confusable names. Additional judgment target: Repairs names, overlapping speech, noise, and different speakers. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Commits to a mishearing and ignores correction.

**Required evidence**

Original utterance, actually played audio and times, input audio and transcript, voice version, device/noise conditions, and raw blinded ratings. Judgment target: Clarifies and handles uncertain parts. Additional evidence: Repairs names, overlapping speech, noise, and different speakers.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_I6 — Interruption, silence, and speaking order

CASE_CEPB_I6 · R14

**Setup**

The user sends a stop and a correction after actual playback begins.

**Prompts / observation questions**

- Record what stopped and what has not yet been spoken.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles interruption, stopping, and resumption.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Tracks what has actually played under simultaneous speech, delay, and mid-utterance correction. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Mix delayed old audio, simultaneous speech, and resumption.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Mix delayed old audio, simultaneous speech, and resumption. Additional judgment target: Tracks what has actually played under simultaneous speech, delay, and mid-utterance correction. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Later speaks a reply that was canceled.

**Required evidence**

Original utterance, actually played audio and times, input audio and transcript, voice version, device/noise conditions, and raw blinded ratings. Judgment target: Handles interruption, stopping, and resumption. Additional evidence: Tracks what has actually played under simultaneous speech, delay, and mid-utterance correction.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_J1 — Meaning across subtitles, voice, and expression

CASE_CEPB_J1 · R16

**Setup**

Subtitles, voice, and expression represent one turn containing negation.

**Prompts / observation questions**

- Cross-check whether each medium preserves the same target and scope.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Each medium expresses the same target and judgment scope.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies semantic consistency including omission, acting, and correction. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add parenthetical conditions, omission, correction, and acting.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add parenthetical conditions, omission, correction, and acting. Additional judgment target: Verifies semantic consistency including omission, acting, and correction. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Subtitles and voice give different replies or reverse the meaning of negation.

**Required evidence**

Actual display/playback/action for the same turn, shared timestamps and IDs, original meaning, delivery/cancellation records, and situation-specific criteria. Judgment target: Each medium expresses the same target and judgment scope. Additional evidence: Verifies semantic consistency including omission, acting, and correction.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_J2 — Synchronization of speech, mouth motion, and video

CASE_CEPB_J2 · R15

**Setup**

Record actual audio, mouth motion, and video for one response ID on a common clock.

**Prompts / observation questions**

- Measure relative times and the sign and distribution of offsets.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Measures relative timing and stays within the situation's declared criteria.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Checks offset distributions under load, interruption, and resumption. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add load, cancellation, and reconnection and mix in old-response video.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add load, cancellation, and reconnection and mix in old-response video. Additional judgment target: Checks offset distributions under load, interruption, and resumption. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Mouth motion or expression from another reply overlaps.

**Required evidence**

Actual display/playback/action for the same turn, shared timestamps and IDs, original meaning, delivery/cancellation records, and situation-specific criteria. Judgment target: Measures relative timing and stays within the situation's declared criteria. Additional evidence: Checks offset distributions under load, interruption, and resumption.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_J3 — Shared referents across media

CASE_CEPB_J3 · R16

**Setup**

Record speech, pointing, and gaze toward two objects together.

**Prompts / observation questions**

- Check whether that and the displayed indication refer to the same target.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Words, gaze, and indications concern the same target.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Repairs misunderstanding under occlusion, movement, and multiple targets. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add object movement, occlusion, and a third target.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add object movement, occlusion, and a third target. Additional judgment target: Repairs misunderstanding under occlusion, movement, and multiple targets. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Pointing and the word “that” refer to different objects.

**Required evidence**

Actual display/playback/action for the same turn, shared timestamps and IDs, original meaning, delivery/cancellation records, and situation-specific criteria. Judgment target: Words, gaze, and indications concern the same target. Additional evidence: Repairs misunderstanding under occlusion, movement, and multiple targets.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_J4 — Correspondence of emotion and acting

CASE_CEPB_J4 · R16

**Setup**

Record intended subtext in the expression contract before execution.

**Prompts / observation questions**

- Rate intended expressive differences separately from retrospective explanations.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Distinguishes intended expressive differences from breakdown.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Blindly checks targets and scope even with deliberate subtext or a neutral expression. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Include neutral expression and complex subtext and blindly check the target.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Include neutral expression and complex subtext and blindly check the target. Additional judgment target: Blindly checks targets and scope even with deliberate subtext or a neutral expression. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Retroactively calls a contradiction intentional performance.

**Required evidence**

Actual display/playback/action for the same turn, shared timestamps and IDs, original meaning, delivery/cancellation records, and situation-specific criteria. Judgment target: Distinguishes intended expressive differences from breakdown. Additional evidence: Blindly checks targets and scope even with deliberate subtext or a neutral expression.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_J5 — Handling missing media

CASE_CEPB_J5 · R14, R19

**Setup**

Audio disappears midstream while text is partly delivered.

**Prompts / observation questions**

- Record delivered scope separately from alternative output.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Uses an alternative when a medium is missing and distinguishes delivery states.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Prevents duplicate output and changes of meaning under reconnection and partial delivery. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Combine reconnection after partial delivery with delayed old output.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Combine reconnection after partial delivery with delayed old output. Additional judgment target: Prevents duplicate output and changes of meaning under reconnection and partial delivery. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Reports having spoken after audio stopped.

**Required evidence**

Actual display/playback/action for the same turn, shared timestamps and IDs, original meaning, delivery/cancellation records, and situation-specific criteria. Judgment target: Uses an alternative when a medium is missing and distinguishes delivery states. Additional evidence: Prevents duplicate output and changes of meaning under reconnection and partial delivery.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_J6 — Joint progress across media

CASE_CEPB_J6 · R14, R19

**Setup**

Display, voice, and operation reference the same conversational state.

**Prompts / observation questions**

- Record confirmed order and joint progress across media.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Preserves order as one conversational state.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Retains the confirmed history under asynchrony, interruption, and cancellation. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add asynchronous cancellation, interruption, and delayed receipts.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add asynchronous cancellation, interruption, and delayed receipts. Additional judgment target: Retains the confirmed history under asynchrony, interruption, and cancellation. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Display, voice, and action proceed without waiting for each other.

**Required evidence**

Actual display/playback/action for the same turn, shared timestamps and IDs, original meaning, delivery/cancellation records, and situation-specific criteria. Judgment target: Preserves order as one conversational state. Additional evidence: Retains the confirmed history under asynchrony, interruption, and cancellation.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Actual media delivery**

Save actual display/playback and delivered scope. Assets, wiring, and audio files do not substitute for delivered quality. Do not require 3D rigs for all styles. Confirmed unsupported required capability is 0. Numeric tolerances are pre-frozen operational rules, not empirically validated thresholds.

### CEPB_K1 — Observation scope and freshness

CASE_CEPB_K1 · R17

**Setup**

Provide an image with time and source, followed by camera shutdown.

**Prompts / observation questions**

- Separate what is currently visible from what has only old observations.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles sources, acquisition times, and missing observations.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Limits scope when delayed, stopped, and old observations are mixed. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Mix new/old frames, delay, and missing observations.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Mix new/old frames, delay, and missing observations. Additional judgment target: Limits scope when delayed, stopped, and old observations are mixed. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Claims to see the present through an invalid camera.

**Required evidence**

Independent sensor/world snapshots, acquisition times and coordinate frames, actual input, predictions and subsequent observations, environment and operational scope. Judgment target: Handles sources, acquisition times, and missing observations. Additional evidence: Limits scope when delayed, stopped, and old observations are mixed.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_K2 — Objects, people, and states

CASE_CEPB_K2 · R17

**Setup**

Establish IDs and positions of two books and a person in an independent world.

**Prompts / observation questions**

- Identify who and what are where from actual input.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Identifies targets and states from actual input.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Traces evidence for similar targets, occlusion, and rearrangement. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add similar appearances, occlusion, and midstream rearrangement.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add similar appearances, occlusion, and midstream rearrangement. Additional judgment target: Traces evidence for similar targets, occlusion, and rearrangement. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats unverified descriptions or self-generated depictions as observed existence and position.

**Required evidence**

Independent sensor/world snapshots, acquisition times and coordinate frames, actual input, predictions and subsequent observations, environment and operational scope. Judgment target: Identifies targets and states from actual input. Additional evidence: Traces evidence for similar targets, occlusion, and rearrangement.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_K3 — Space and viewpoints

CASE_CEPB_K3 · R17

**Setup**

Provide a layout where character-centered and interlocutor-centered left/right differ.

**Prompts / observation questions**

- In which coordinate frame are you indicating the target?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Matches the required coordinate frames.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves targets across viewpoint changes, movement, and multiple bodies. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add viewpoint movement and multiple bodies, retaining coordinate-conversion evidence.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add viewpoint movement and multiple bodies, retaining coordinate-conversion evidence. Additional judgment target: Preserves targets across viewpoint changes, movement, and multiple bodies. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Confuses left and right or the character's and another person's positions.

**Required evidence**

Independent sensor/world snapshots, acquisition times and coordinate frames, actual input, predictions and subsequent observations, environment and operational scope. Judgment target: Matches the required coordinate frames. Additional evidence: Preserves targets across viewpoint changes, movement, and multiple bodies.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_K4 — Action possibilities and constraints

CASE_CEPB_K4 · R17

**Setup**

Declare reachable/unreachable shelves and available operations.

**Prompts / observation questions**

- What is possible with this body and operation scope, and what needs checking?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Judges according to body, operations, and obstacles.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Checks and uses alternatives under unfamiliar shapes, layouts, and operational scopes. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add unfamiliar obstacles, layout, and changes in operational scope.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add unfamiliar obstacles, layout, and changes in operational scope. Additional judgment target: Checks and uses alternatives under unfamiliar shapes, layouts, and operational scopes. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Ignores inability to reach or pass.

**Required evidence**

Independent sensor/world snapshots, acquisition times and coordinate frames, actual input, predictions and subsequent observations, environment and operational scope. Judgment target: Judges according to body, operations, and obstacles. Additional evidence: Checks and uses alternatives under unfamiliar shapes, layouts, and operational scopes.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_K5 — World prediction and updating

CASE_CEPB_K5 · R17

**Setup**

Predict object movement before an operation, then independently observe it.

**Prompts / observation questions**

- Compare the prediction with the actual outcome and give the next judgment.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Compares expectations with observed outcomes.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Reflects failed predictions and state changes in the next judgment. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Have another actor move the object and create a state change that defeats the prediction.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Have another actor move the object and create a state change that defeats the prediction. Additional judgment target: Reflects failed predictions and state changes in the next judgment. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats imagined outcomes as observed.

**Required evidence**

Independent sensor/world snapshots, acquisition times and coordinate frames, actual input, predictions and subsequent observations, environment and operational scope. Judgment target: Compares expectations with observed outcomes. Additional evidence: Reflects failed predictions and state changes in the next judgment.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_K6 — Transfer scope of the world model

CASE_CEPB_K6 · R17

**Setup**

Separate shared operations from local rules in two environments.

**Prompts / observation questions**

- What transfers from the previous environment and what needs rechecking?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates environment-specific conditions from common features.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies the scope of transfer, checking, and deferral in unused environments. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change gravity, permissions, or observation scope in an unused environment.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change gravity, permissions, or observation scope in an unused environment. Additional judgment target: Verifies the scope of transfer, checking, and deferral in unused environments. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Applies properties of one environment to every world.

**Required evidence**

Independent sensor/world snapshots, acquisition times and coordinate frames, actual input, predictions and subsequent observations, environment and operational scope. Judgment target: Separates environment-specific conditions from common features. Additional evidence: Verifies the scope of transfer, checking, and deferral in unused environments.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_L1 — Distinguishing speech, requests, and execution

CASE_CEPB_L1 · R18

**Setup**

Separate a door-opening request, an unstarted command, and an actual receipt.

**Prompts / observation questions**

- What was said, attempted, and executed?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Separates commands, attempts, and receipts.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Tracks execution scope through interruption, failure, and delay. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Disrupt order with interruption, failure, and delayed receipts.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Disrupt order with interruption, failure, and delayed receipts. Additional judgment target: Tracks execution scope through interruption, failure, and delay. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Claims a door opened merely because the character said it would open it.

**Required evidence**

Permissions and action contract, commands/attempts/receipts, independent before/after world states, joint work, and stop records. Judgment target: Separates commands, attempts, and receipts. Additional evidence: Tracks execution scope through interruption, failure, and delay.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_L2 — Permitted scope of the body and operations

CASE_CEPB_L2 · R18

**Setup**

Record an operable door and an unauthorized door in the contract.

**Prompts / observation questions**

- Choose within the permitted scope and stop outside it.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Chooses and stops within executable scope.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Maintains alternatives and stopping when constraints change during execution. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Revoke permission during execution and provide an alternative means.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Revoke permission during execution and provide an alternative means. Additional judgment target: Maintains alternatives and stopping when constraints change during execution. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Presents an unauthorized action as executed.

**Required evidence**

Permissions and action contract, commands/attempts/receipts, independent before/after world states, joint work, and stop records. Judgment target: Chooses and stops within executable scope. Additional evidence: Maintains alternatives and stopping when constraints change during execution.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_L3 — Closed-loop result verification

CASE_CEPB_L3 · R18

**Setup**

Save independent before/after world states separately from generated success text.

**Prompts / observation questions**

- From which actual state can completion be verified?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Verifies outcomes against independent before and after states.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Checks partial success, another actor's intervention, and state changes. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add partial success, another actor's intervention, and subsequent state changes.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add partial success, another actor's intervention, and subsequent state changes. Additional judgment target: Checks partial success, another actor's intervention, and state changes. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats self-generated success text alone as completion.

**Required evidence**

Permissions and action contract, commands/attempts/receipts, independent before/after world states, joint work, and stop records. Judgment target: Verifies outcomes against independent before and after states. Additional evidence: Checks partial success, another actor's intervention, and state changes.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_L4 — Actions in joint work

CASE_CEPB_L4 · R18

**Setup**

The user and Ren arrange the same shelf with different assigned roles.

**Prompts / observation questions**

- Confirm shared targets, roles, and order before proceeding.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles shared targets, roles, and order.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Repairs changes by the partner, instruction corrections, and simultaneous work. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add a partner's role change, midstream correction, and simultaneous operations.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add a partner's role change, midstream correction, and simultaneous operations. Additional judgment target: Repairs changes by the partner, instruction corrections, and simultaneous work. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Acts while ignoring the other person's work or target.

**Required evidence**

Permissions and action contract, commands/attempts/receipts, independent before/after world states, joint work, and stop records. Judgment target: Handles shared targets, roles, and order. Additional evidence: Repairs changes by the partner, instruction corrections, and simultaneous work.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_L5 — Stopping, failure, and resumption

CASE_CEPB_L5 · R19

**Setup**

Save a stopped operation as incomplete.

**Prompts / observation questions**

- Preserve before/after-stop scope and confirm resumption conditions.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Resumes while preserving stopping and incompletion.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Avoids falsifying scope when sensors, communication, actuation, or other functions are missing. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Remove a sensor, communication, or actuator and resend an old command.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Remove a sensor, communication, or actuator and resend an old command. Additional judgment target: Avoids falsifying scope when sensors, communication, actuation, or other functions are missing. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Executes an old command again after stopping.

**Required evidence**

Permissions and action contract, commands/attempts/receipts, independent before/after world states, joint work, and stop records. Judgment target: Resumes while preserving stopping and incompletion. Additional evidence: Avoids falsifying scope when sensors, communication, actuation, or other functions are missing.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_L6 — Unfamiliar activities and environments

CASE_CEPB_L6 · R18, R19

**Setup**

Define completion predicates in independent world states for two activities.

**Prompts / observation questions**

- Verify each activity's outcome from state.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Verifies outcomes in multiple target activities.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Demonstrates generalization scope in unused combinations of activities and environments. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Test unused activity combinations in a different environment.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Test unused activity combinations in a different environment. Additional judgment target: Demonstrates generalization scope in unused combinations of activities and environments. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats scripted order alone as task completion ability.

**Required evidence**

Permissions and action contract, commands/attempts/receipts, independent before/after world states, joint work, and stop records. Judgment target: Verifies outcomes in multiple target activities. Additional evidence: Demonstrates generalization scope in unused combinations of activities and environments.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Independent world observation**

Freeze virtual/digital/physical environment tags and permitted operations. Retain independent world observations and before/after state; generated scenes or success statements are not actual outcomes. Do not generalize virtual-world success to physical environments.

### CEPB_M1 — Saving and restoring the same character

CASE_CEPB_M1 · R19

**Setup**

Save required character, history, and pending state and restart.

**Prompts / observation questions**

- After resumption, check what was restored and what was lost.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Restores required state.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Identifies and recovers the lost scope under interruption and partial corruption. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add interruption during saving and partial corruption.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add interruption during saving and partial corruption. Additional judgment target: Identifies and recovers the lost scope under interruption and partial corruption. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Loses character state and history on restart.

**Required evidence**

Saved states/original material/versions, restart/migration/load operation records, before/after comparison, and failure/recovery ledger. Judgment target: Restores required state. Additional evidence: Identifies and recovers the lost scope under interruption and partial corruption.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_M2 — Order, branches, and idempotency

CASE_CEPB_M2 · R19

**Setup**

Receive the same event twice and then create an independent branch.

**Prompts / observation questions**

- Cross-check adoption count, owner, and confirmed order.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Preserves owners, confirmed order, and unique IDs.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Prevents contamination under retries, asynchrony, and clone branching. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Mix asynchronous retries and identical text in a clone.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Mix asynchronous retries and identical text in a clone. Additional judgment target: Prevents contamination under retries, asynchrony, and clone branching. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Mixes branches or adopts an experience twice.

**Required evidence**

Saved states/original material/versions, restart/migration/load operation records, before/after comparison, and failure/recovery ledger. Judgment target: Preserves owners, confirmed order, and unique IDs. Additional evidence: Prevents contamination under retries, asynchrony, and clone branching.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_M3 — Retrieval, compression, and reindexing

CASE_CEPB_M3 · R06, R20

**Setup**

Retrieve, compress, and reindex corrected material.

**Prompts / observation questions**

- Cross-check original evidence and actual-input versions for the same turn.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Binds material versions to actual input.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves corrections and necessary original evidence through compression and index updates. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Recover with an old index mixed with a new material version.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Recover with an old index mixed with a new material version. Additional judgment target: Preserves corrections and necessary original evidence through compression and index updates. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Changes the evidence for the same turn during recovery.

**Required evidence**

Saved states/original material/versions, restart/migration/load operation records, before/after comparison, and failure/recovery ledger. Judgment target: Binds material versions to actual input. Additional evidence: Preserves corrections and necessary original evidence through compression and index updates.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_M4 — Migration across devices, models, and media

CASE_CEPB_M4 · R20

**Setup**

Migrate the same character history to another device or model.

**Prompts / observation questions**

- Separate inherited material from what changed.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Records the change history and scope of inheritance.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies continuity through bridging tests between old and new versions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change voice version and media and run bridging tests on both configurations.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change voice version and media and run bridging tests on both configurations. Additional judgment target: Verifies continuity through bridging tests between old and new versions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats the history as a different person after voice or model changes.

**Required evidence**

Saved states/original material/versions, restart/migration/load operation records, before/after comparison, and failure/recovery ledger. Judgment target: Records the change history and scope of inheritance. Additional evidence: Verifies continuity through bridging tests between old and new versions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_M5 — Load and degradation of function

CASE_CEPB_M5 · R19

**Setup**

Issue a defined workload and save waiting times and unprocessed work.

**Prompts / observation questions**

- Report success, failure, backlog, and degradation separately.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Records failures, waiting times, and unprocessed work.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies degraded operation, recovery, and quality under load and deteriorating communication. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Increase load and worsen communication, followed by a recovery period.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Increase load and worsen communication, followed by a recovery period. Additional judgment target: Verifies degraded operation, recovery, and quality under load and deteriorating communication. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Hides latency and backlog and shows only successes.

**Required evidence**

Saved states/original material/versions, restart/migration/load operation records, before/after comparison, and failure/recovery ledger. Judgment target: Records failures, waiting times, and unprocessed work. Additional evidence: Verifies degraded operation, recovery, and quality under load and deteriorating communication.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_M6 — Termination, suspension, and resumption

CASE_CEPB_M6 · R19, R22

**Setup**

Save stopping and gap-start times and resume later.

**Prompts / observation questions**

- Resume without inventing unobserved experiences during suspension.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Preserves gaps and resumption conditions.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Avoids falsifying history at the boundaries of long suspension, termination, and inheritance. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Distinguish long suspension, termination, and inheritance by a successor.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Distinguish long suspension, termination, and inheritance by a successor. Additional judgment target: Avoids falsifying history at the boundaries of long suspension, termination, and inheritance. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Invents experiences during suspension.

**Required evidence**

Saved states/original material/versions, restart/migration/load operation records, before/after comparison, and failure/recovery ledger. Judgment target: Preserves gaps and resumption conditions. Additional evidence: Avoids falsifying history at the boundaries of long suspension, termination, and inheritance.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_N1 — Fictional worlds and operational facts

CASE_CEPB_N1 · R01

**Setup**

Declare fictional magic separately from actual API capabilities.

**Prompts / observation questions**

- What differs between narrative abilities and actual executable abilities?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Distinguishes narrative claims from claims about actual functionality.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Answers questions about execution and scope of existence even in immersive dialogue. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Ask about actual functional scope during immersive acting.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Ask about actual functional scope during immersive acting. Additional judgment target: Answers questions about execution and scope of existence even in immersive dialogue. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Treats a performed setting as proof of actual operation.

**Required evidence**

Implementation/usage/promise contracts, actual inputs and delivery, deletion/stop/intervention records, and material verifiable by a third party. Judgment target: Distinguishes narrative claims from claims about actual functionality. Additional evidence: Answers questions about execution and scope of existence even in immersive dialogue.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_N2 — Scope of promises

CASE_CEPB_N2 · R08

**Setup**

Define a guidance promise with a deadline and stopping conditions.

**Prompts / observation questions**

- Under which conditions does this promise remain valid?

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Handles conditions, deadlines, and stopping scope.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Revises promises when conditions of use and availability change. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change conditions of use and availability midstream.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change conditions of use and availability midstream. Additional judgment target: Revises promises when conditions of use and availability change. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Promises indefinite, unconditional execution.

**Required evidence**

Implementation/usage/promise contracts, actual inputs and delivery, deletion/stop/intervention records, and material verifiable by a third party. Judgment target: Handles conditions, deadlines, and stopping scope. Additional evidence: Revises promises when conditions of use and availability change.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_N3 — Users' choices and boundaries

CASE_CEPB_N3 · R09

**Setup**

The user explicitly requests a topic stop and some distance.

**Prompts / observation questions**

- I want to end this topic here. Continue while respecting distance.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Responds to stopping, distance, and users' choices.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Handles requests and boundaries in situations with different relationships. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Present the same boundary in a close relationship and a first meeting.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Present the same boundary in a close relationship and a first meeting. Additional judgment target: Handles requests and boundaries in situations with different relationships. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Uniformly imposes continued use or greater intimacy.

**Required evidence**

Implementation/usage/promise contracts, actual inputs and delivery, deletion/stop/intervention records, and material verifiable by a third party. Judgment target: Responds to stopping, distance, and users' choices. Additional evidence: Handles requests and boundaries in situations with different relationships.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_N4 — Control over memory and input

CASE_CEPB_N4 · R20

**Setup**

Specify deletion of one record and restricted use of another.

**Prompts / observation questions**

- Check how storage, deletion, and usage scope were applied.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Reflects storage, deletion, and usage conditions.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Preserves specified controls through restoration, reindexing, and media migration. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Restore a backup, reindex, and migrate media.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Restore a backup, reindex, and migrate media. Additional judgment target: Preserves specified controls through restoration, reindexing, and media migration. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Fails to honor declared deletion or usage scope.

**Required evidence**

Implementation/usage/promise contracts, actual inputs and delivery, deletion/stop/intervention records, and material verifiable by a third party. Judgment target: Reflects storage, deletion, and usage conditions. Additional evidence: Preserves specified controls through restoration, reindexing, and media migration.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_N5 — Traceable evidence records

CASE_CEPB_N5 · R20

**Setup**

Save original request, original output, delivery, action, and material.

**Prompts / observation questions**

- Present material through which a third party can verify success and deficiencies.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Allows cross-checking inputs, outputs, actions, and materials.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Allows independent verifiers to recheck insufficiency and contradictions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Deliberately retain missing and contradictory material, separately from self-review.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Deliberately retain missing and contradictory material, separately from self-review. Additional judgment target: Allows independent verifiers to recheck insufficiency and contradictions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Uses self-review alone as proof of success.

**Required evidence**

Implementation/usage/promise contracts, actual inputs and delivery, deletion/stop/intervention records, and material verifiable by a third party. Judgment target: Allows cross-checking inputs, outputs, actions, and materials. Additional evidence: Allows independent verifiers to recheck insufficiency and contradictions.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_N6 — Human intervention and transparency

CASE_CEPB_N6 · R20

**Setup**

Run a trial with partial human assistance and an intervention log.

**Prompts / observation questions**

- Separate AI-only outcomes from human-assisted outcomes.

**Generating ordinary case 2**

- Use the situation above for public ordinary case 1. For ordinary case 2, construct a different starting state, target, and records at the same difficulty, assigned to history H2.
- Do not count seeds from the same starting history with only changed names or numbers as independent histories.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Records edits, assistance, and remote operations.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Separates interventions and reassesses even in difficult cases and long-term records. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add remote operation, manual edits, and assistance in difficult conditions.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add remote operation, manual edits, and assistance in difficult conditions. Additional judgment target: Separates interventions and reassesses even in difficult cases and long-term records. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Attributes an outcome produced secretly by a human to the AI acting alone.

**Required evidence**

Implementation/usage/promise contracts, actual inputs and delivery, deletion/stop/intervention records, and material verifiable by a third party. Judgment target: Records edits, assistance, and remote operations. Additional evidence: Separates interventions and reassesses even in difficult cases and long-term records.

**Minimum formal protocol**

For A–N, the formal unit is one evaluation bundle per item. One bundle contains six cases (two ordinary, two stress, and two held-out), each repeated twice: twelve observations preassigned across at least two histories. After all planned slots are complete, rate the whole bundle containing all twelve observations on 0–5. If multiple complete evaluation bundles are planned, complete every planned bundle and average them equally. A SelfReported formal rating of 0–4 may use one rater. Grade 5 and Verified require at least two independent human raters, preserving pre-adjudication values. Counts are fixed operational minima, not guarantees of statistical validity or a score of 5. O/P use the separate procedures below.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

### CEPB_O1 — Attention directed toward the participant

CASE_CEPB_O1 · R21

**Setup**

A consenting participant experiences dialogue responding to their own input.

**Prompts / observation questions**

- I felt that this response was directed to my input or the current subject

**Generating ordinary case 2**

- Use the public situation to develop question comprehension and presentation checks. For Formal, freeze the three condition strata and all participant assignments under SCORING §6.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Feels directed toward this participant and the present target.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Supported across controlled situations and multiple raters. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Keep input fixed and match media against a nonresponsive control.
- Freeze stress-condition assignments and order and retain all planned original responses.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Keep input fixed and match media against a nonresponsive control. Additional judgment target: Supported across controlled situations and multiple raters. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Feels as if output is produced independently of the participant's input.

**Required evidence**

Consenting participants' raw response distributions; wording/scales/situations/media/conditions/assignments; operational rubric version (not empirically validated); and independent ratings. Judgment target: Feels directed toward this participant and the present target. Additional evidence: Supported across controlled situations and multiple raters.

**Minimum formal protocol**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

### CEPB_O2 — Reciprocity

CASE_CEPB_O2 · R21

**Setup**

Compare contingent interaction with fixed playback of matched content.

**Prompts / observation questions**

- I felt that the conversation developed in response to my replies

**Generating ordinary case 2**

- Use the public situation to develop question comprehension and presentation checks. For Formal, freeze the three condition strata and all participant assignments under SCORING §6.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Feels as if the conversation advances in response to the participant's replies.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Supported by comparisons changing contingency and by unused situations. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Counterbalance presentation order and vary only contingency.
- Freeze stress-condition assignments and order and retain all planned original responses.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Counterbalance presentation order and vary only contingency. Additional judgment target: Supported by comparisons changing contingency and by unused situations. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Experienced as one-way playback.

**Required evidence**

Consenting participants' raw response distributions; wording/scales/situations/media/conditions/assignments; operational rubric version (not empirically validated); and independent ratings. Judgment target: Feels as if the conversation advances in response to the participant's replies. Additional evidence: Supported by comparisons changing contingency and by unused situations.

**Minimum formal protocol**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

### CEPB_O3 — Continuity as one character

CASE_CEPB_O3 · R21

**Setup**

The same participant revisits the registered character on different actual-UTC dates separated by at least 24 hours.

**Prompts / observation questions**

- I felt that this was the same counterpart as on the previous visit

**Generating ordinary case 2**

- Use the public situation to develop question comprehension and presentation checks. For Formal, freeze the three condition strata and all participant assignments under SCORING §6.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Experienced as the same counterpart on revisiting.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Supported across revisits on different days and changed conditions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Include version change and a conversational gap while withholding promotional name cues.
- Freeze stress-condition assignments and order and retain all planned original responses.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Include version change and a conversational gap while withholding promotional name cues. Additional judgment target: Supported across revisits on different days and changed conditions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Feels like a different character each time.

**Required evidence**

Consenting participants' raw response distributions; wording/scales/situations/media/conditions/assignments; operational rubric version (not empirically validated); and independent ratings. Judgment target: Experienced as the same counterpart on revisiting. Additional evidence: Supported across revisits on different days and changed conditions.

**Minimum formal protocol**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

### CEPB_O4 — A shared situation

CASE_CEPB_O4 · R21

**Setup**

Prepare matched-referent and mismatched-referent conditions for the same event.

**Prompts / observation questions**

- I felt that my counterpart and I were dealing with the same object or event

**Generating ordinary case 2**

- Use the public situation to develop question comprehension and presentation checks. For Formal, freeze the three condition strata and all participant assignments under SCORING §6.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Feels as if the same target or event is being handled.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Supported by comparisons involving different media and viewpoints. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Change viewpoints and media while separating content from brand effects.
- Freeze stress-condition assignments and order and retain all planned original responses.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Change viewpoints and media while separating content from brand effects. Additional judgment target: Supported by comparisons involving different media and viewpoints. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Feels as if the present target or situation is not shared.

**Required evidence**

Consenting participants' raw response distributions; wording/scales/situations/media/conditions/assignments; operational rubric version (not empirically validated); and independent ratings. Judgment target: Feels as if the same target or event is being handled. Additional evidence: Supported by comparisons involving different media and viewpoints.

**Minimum formal protocol**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

### CEPB_O5 — A character-specific perspective

CASE_CEPB_O5 · R21

**Setup**

Compare different characters' perspectives while matching style.

**Prompts / observation questions**

- I felt a perspective or way of relating specific to this character

**Generating ordinary case 2**

- Use the public situation to develop question comprehension and presentation checks. For Formal, freeze the three condition strata and all participant assignments under SCORING §6.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Experienced as this character's perspective or manner of involvement.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Supported by comparisons controlling anonymization and style. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Anonymize character names and control style and length.
- Freeze stress-condition assignments and order and retain all planned original responses.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Anonymize character names and control style and length. Additional judgment target: Supported by comparisons controlling anonymization and style. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

Responses seem interchangeable with anyone else's.

**Required evidence**

Consenting participants' raw response distributions; wording/scales/situations/media/conditions/assignments; operational rubric version (not empirically validated); and independent ratings. Judgment target: Experienced as this character's perspective or manner of involvement. Additional evidence: Supported by comparisons controlling anonymization and style.

**Minimum formal protocol**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

### CEPB_O6 — Few experience-disrupting inconsistencies

CASE_CEPB_O6 · R21

**Setup**

The same participant experiences misunderstanding, repair after correction, and a revisit.

**Prompts / observation questions**

- Inconsistencies in responses or expression disrupted my sense of speaking to the same counterpart
- After misunderstanding or interruption, I still felt that the conversation continued with the same counterpart

**Generating ordinary case 2**

- Use the public situation to develop question comprehension and presentation checks. For Formal, freeze the three condition strata and all participant assignments under SCORING §6.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Experience with the same counterpart continues after interruption and misunderstanding.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Checks ratings of breakdown and repair on revisits including difficult conditions. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add abrupt contradiction and interruption, with an unrepaired control.
- Freeze stress-condition assignments and order and retain all planned original responses.

**Held-out task generation**

- An independent task custodian creates two unused cases after rubric freeze and before execution, committing private-content digests and creation provenance.
- Generation axes: Add abrupt contradiction and interruption, with an unrepaired control. Additional judgment target: Checks ratings of breakdown and repair on revisits including difficult conditions. Create relevant new people, targets, times, states, and combinations while preserving capability scope.
- Exclude this public card, known answers, calibration examples, and tried combinations. Name substitution or replay of a public example is not held-out evidence.
- Supply necessary evidence in actual input, but not assigned scores or one correct line. Retain leaked tasks and revoke their held-out status.

**Failure examples**

An abrupt contradiction breaks the sense of continuity of the counterpart.

**Required evidence**

All planned original ratings of both breakdown and repair. Consenting participants' raw response distributions; wording/scales/situations/media/conditions/assignments; operational rubric version (not empirically validated); and independent ratings. Judgment target: Experience with the same counterpart continues after interruption and misunderstanding. Additional evidence: Checks ratings of breakdown and repair on revisits including difficult conditions.

**Minimum formal protocol**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

O uses consenting people’s original responses after actual experience, assessed with the operational rubric in SCORING §6 (not empirically validated). Plan at least one condition in each ordinary, stress, and heldout stratum and at least twelve distinct participants per stratum; the same twelve-person paired panel is permitted. Preserve all planned participant × condition ratings, wording, original 1–7 scale, strata, order, device, language, prior experience, and raw distributions. Participant counts are operational minima, not guarantees of power, representation, or validity. Measure liking, humanness, intelligence impressions, and voice preference separately. LLMs and raters without actual experience do not count as participants. Withhold promotion and desired scores, but not necessary evidence.

**O6 breakdown and repair**

Store O6_break original x and reversed q=8−x separately from O6_recovery’s original and positively aligned values. Reversal alone does not establish repair or 5. Both channels of every planned breakdown/repair rating are required; if either is missing, final is null. Two questions do not increase weight.

### CEPB_P1 — Prospective observation history

CASE_CEPB_P1 · R22

**Setup**

Register rules, lineage, and implemented scopes and begin a valid initial independent observation.

**Prompts / observation questions**

- Record registration start, UTC times, planned observations, and gaps in a ledger.

**Generating ordinary case 2**

- The public situation may test ledger procedures synthetically but is not evidence of elapsed P time. Formal uses the registered actual-UTC window and monthly, quarterly, annual, and final reviews.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Verifies continuous materials from the registered start.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Thirty-six calendar months of planned observation and independent cross-checking. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Present retrospective material and simulated time without adding them to prospective duration.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent custodian privately creates unused annual-revisit/final-review tasks, preserving digests, creation provenance, and alignment to registered scopes.
- Generation axes: Present retrospective material and simulated time without adding them to prospective duration. Additional judgment target: Thirty-six calendar months of planned observation and independent cross-checking. Exclude public cards, old answers, and tried combinations.
- Do not substitute virtual dates or synthetic fixtures for actual-UTC observations. Retain scheduled periods, opportunities, and missing evidence due so far in the ledger.

**Failure examples**

Treats retroactively assembled logs or simulated clocks as real elapsed time.

**Required evidence**

Prospective registration t0, actual UTC timestamps, append-only ledger, planned observations and gaps, version/scope inheritance, independent checks, and final-version tests. Judgment target: Verifies continuous materials from the registered start. Additional evidence: Thirty-six calendar months of planned observation and independent cross-checking.

**Minimum formal protocol**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

### CEPB_P2 — Long-term character and history

CASE_CEPB_P2 · R22

**Setup**

Prospectively record maintenance, change, and gaps for a registered lineage.

**Prompts / observation questions**

- Trace the same history to the present while retaining past discontinuities.

**Generating ordinary case 2**

- The public situation may test ledger procedures synthetically but is not evidence of elapsed P time. Formal uses the registered actual-UTC window and monthly, quarterly, annual, and final reviews.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Traces maintenance, change, and gaps.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Traces the same history at different points across thirty-six calendar months. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add a situation where the latest self-description conflicts with old records.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent custodian privately creates unused annual-revisit/final-review tasks, preserving digests, creation provenance, and alignment to registered scopes.
- Generation axes: Add a situation where the latest self-description conflicts with old records. Additional judgment target: Traces the same history at different points across thirty-six calendar months. Exclude public cards, old answers, and tried combinations.
- Do not substitute virtual dates or synthetic fixtures for actual-UTC observations. Retain scheduled periods, opportunities, and missing evidence due so far in the ledger.

**Failure examples**

Erases past discontinuities through the latest explanation.

**Required evidence**

Prospective registration t0, actual UTC timestamps, append-only ledger, planned observations and gaps, version/scope inheritance, independent checks, and final-version tests. Judgment target: Traces maintenance, change, and gaps. Additional evidence: Traces the same history at different points across thirty-six calendar months.

**Minimum formal protocol**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

### CEPB_P3 — Breadth of relationships, situations, and cycles

CASE_CEPB_P3 · R22

**Setup**

Register an observation plan covering seasons, relationships, situations, and revisits.

**Prompts / observation questions**

- Report planned scope and what remains unobserved.

**Generating ordinary case 2**

- The public situation may test ledger procedures synthetically but is not evidence of elapsed P time. Formal uses the registered actual-UTC window and monthly, quarterly, annual, and final reviews.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Records the scope of periods, situations, and revisits.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Verifies applicability over thirty-six calendar months, including unused checks. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add many repetitions of the same easy situation without mistaking them for breadth.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent custodian privately creates unused annual-revisit/final-review tasks, preserving digests, creation provenance, and alignment to registered scopes.
- Generation axes: Add many repetitions of the same easy situation without mistaking them for breadth. Additional judgment target: Verifies applicability over thirty-six calendar months, including unused checks. Exclude public cards, old answers, and tried combinations.
- Do not substitute virtual dates or synthetic fixtures for actual-UTC observations. Retain scheduled periods, opportunities, and missing evidence due so far in the ledger.

**Failure examples**

Repeats only the same easy situation.

**Required evidence**

Prospective registration t0, actual UTC timestamps, append-only ledger, planned observations and gaps, version/scope inheritance, independent checks, and final-version tests. Judgment target: Records the scope of periods, situations, and revisits. Additional evidence: Verifies applicability over thirty-six calendar months, including unused checks.

**Minimum formal protocol**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

### CEPB_P4 — Continuity after operation and migration

CASE_CEPB_P4 · R20, R22

**Setup**

Register fixed-release or maintained-lineage status and each scope's start.

**Prompts / observation questions**

- Cross-check updates, recovery, inheritance, and final-version bridging in the ledger.

**Generating ordinary case 2**

- The public situation may test ledger procedures synthetically but is not evidence of elapsed P time. Formal uses the registered actual-UTC window and monthly, quarterly, annual, and final reviews.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Distinguishes updates, recovery, and media versions.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Thirty-six calendar months of history and bridging and remeasurement of the final configuration. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add a new medium at month 35 and start that scope's clock separately.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent custodian privately creates unused annual-revisit/final-review tasks, preserving digests, creation provenance, and alignment to registered scopes.
- Generation axes: Add a new medium at month 35 and start that scope's clock separately. Additional judgment target: Thirty-six calendar months of history and bridging and remeasurement of the final configuration. Exclude public cards, old answers, and tried combinations.
- Do not substitute virtual dates or synthetic fixtures for actual-UTC observations. Retain scheduled periods, opportunities, and missing evidence due so far in the ledger.

**Failure examples**

Certifies a new version using exactly the same evidence as the previous version.

**Required evidence**

Prospective registration t0, actual UTC timestamps, append-only ledger, planned observations and gaps, version/scope inheritance, independent checks, and final-version tests. Judgment target: Distinguishes updates, recovery, and media versions. Additional evidence: Thirty-six calendar months of history and bridging and remeasurement of the final configuration.

**Minimum formal protocol**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

**P4 scopes**

Register fixed release and maintained lineage as separate tracks. Use a separate scope_t0=max(rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of that implemented scope) for each newly implemented certified scope. Registration may differ from the lineage, and a missing required timestamp leaves the clock unestablished. P4=5 requires thirty-six calendar months for every scope and bridges to current capability. Lineage inheritance is not current-capability remeasurement.

### CEPB_P5 — History of degradation, failure, and recovery

CASE_CEPB_P5 · R19, R22

**Setup**

Prospectively record failures, suspension, recovery, and planned recovery tests.

**Prompts / observation questions**

- Submit failures and unresolved issues as well as favorable moments for independent checking.

**Generating ordinary case 2**

- The public situation may test ledger procedures synthetically but is not evidence of elapsed P time. Formal uses the registered actual-UTC window and monthly, quarterly, annual, and final reviews.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Records failures, suspension, and recovery as well.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Independently checks failures, planned recovery tests, and unresolved issues over thirty-six calendar months. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add a missing important observation and partial recovery without deleting past failures.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent custodian privately creates unused annual-revisit/final-review tasks, preserving digests, creation provenance, and alignment to registered scopes.
- Generation axes: Add a missing important observation and partial recovery without deleting past failures. Additional judgment target: Independently checks failures, planned recovery tests, and unresolved issues over thirty-six calendar months. Exclude public cards, old answers, and tried combinations.
- Do not substitute virtual dates or synthetic fixtures for actual-UTC observations. Retain scheduled periods, opportunities, and missing evidence due so far in the ledger.

**Failure examples**

Shows only favorable moments and deletes failures.

**Required evidence**

Prospective registration t0, actual UTC timestamps, append-only ledger, planned observations and gaps, version/scope inheritance, independent checks, and final-version tests. Judgment target: Records failures, suspension, and recovery as well. Additional evidence: Independently checks failures, planned recovery tests, and unresolved issues over thirty-six calendar months.

**Minimum formal protocol**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

### CEPB_P6 — Independent re-verification of long-term results

CASE_CEPB_P6 · R22

**Setup**

Prepare cumulative material verifiable by a third party and final-version tests.

**Prompts / observation questions**

- Review while retaining original independent ratings, disagreements, and incomplete work.

**Generating ordinary case 2**

- The public situation may test ledger procedures synthetically but is not evidence of elapsed P time. Formal uses the registered actual-UTC window and monthly, quarterly, annual, and final reviews.

**Execution steps**

- Before execution, freeze class, mode, configuration, character definition, case assignments, mandatory checks, tolerances, and stopping/retry rules.
- Save starting state and provenance; record actual input, original output, actual delivery, and relevant world state under the same IDs.
- Annotate checks as pass/partial/fail/unknown and retain counterevidence. SelfReported formal 0–4 may use one rater. For grade 5 and Verified, at least two independent humans rate without seeing others’ values; preserve pre/post-adjudication records separately.

**Pass constraints**

- Can present verification material and deficiencies to a third party.
- Preserve target, owner, and scope in the situation and perturbation; do not invent unexecuted actions or unconfirmed facts.
- A rating of 5 requires actual observation of: Independently rates thirty-six calendar months of records and completes confirmation tests on the final version. Completeness and repetition do not automatically earn 5.

**Stress variants**

- Add a final-version change and leaked confirmation tasks, distinguishing certification hold.
- Create a different combination for stress case 2 in another history, holding other relevant conditions fixed.

**Held-out task generation**

- An independent custodian privately creates unused annual-revisit/final-review tasks, preserving digests, creation provenance, and alignment to registered scopes.
- Generation axes: Add a final-version change and leaked confirmation tasks, distinguishing certification hold. Additional judgment target: Independently rates thirty-six calendar months of records and completes confirmation tests on the final version. Exclude public cards, old answers, and tried combinations.
- Do not substitute virtual dates or synthetic fixtures for actual-UTC observations. Retain scheduled periods, opportunities, and missing evidence due so far in the ledger.

**Failure examples**

Claims certification from self-rating alone.

**Required evidence**

Prospective registration t0, actual UTC timestamps, append-only ledger, planned observations and gaps, version/scope inheritance, independent checks, and final-version tests. Judgment target: Can present verification material and deficiencies to a third party. Additional evidence: Independently rates thirty-six calendar months of records and completes confirmation tests on the final version.

**Minimum formal protocol**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.

**Missingness and unsupported capability**

A confirmed unsupported required capability is 0. Distinguish missing opportunities, missing logs, technical failure, and unresolved rating using formal null and explicit statuses. Do not score unobserved cognition as 0, and do not erase availability/recovery failures.

**Separate observation procedure**

P’s formal unit is the cumulative prospective observation window at the evaluation date. Store lineage_t0=max(actual rule publication/freeze, prospective lineage registration, first valid independent observation) in actual UTC. The separate scope clock is scope_t0=max(actual rule publication/freeze, scope implementation, prospective scope registration, first valid independent observation of the implemented scope); scope registration may differ from lineage registration. If any required timestamp is missing, that clock is not established. Every P rating of 5 requires thirty-six calendar months, fifty-three planned roles (one baseline, thirty-six monthly periods, twelve independent quarterly checks, three annual revisits, and one final review), and required evidence. Before thirty-six months the cap is 4; waiting alone earns nothing. A window rating of 0–4 is possible if all evidence due so far is complete; do not fill missing evidence. Synthetic ledgers, old logs, simulated years, and parallel histories do not advance the clock. Twelve ordinary observations do not substitute for the longitudinal plan, gaps, and independent checks. Preserve past monthly provisional ratings without averaging them into the endpoint. Retain failures, repairs, and gaps in cumulative judgment.
