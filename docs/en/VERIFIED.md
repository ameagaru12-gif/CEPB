# Independent verification: Verified

Version: CEPB 1.0.0. `Verified` describes independent checking of declared results, configurations, and evidence. It is a verification layer attached to a class such as Core, not another score, class, or denominator. The CEPB package does not operate an official certification authority or issue official badges.

## 1. Distinguishing self-assessment

Self-assessment is useful for development and finding gaps. A self-declared flag, a successful schema check, or another judgment by the developer's LLM alone does not establish Verified status. If verification covers only part of Core, describe it as verification of that subset, not as a verified completed Core score.

At least two human third parties must independently rerate the result, independently of the developers and initial raters who produced the assessed evaluation. The tested system and assisting LLMs do not count as people. Report affiliations, funding, conflicts, previous involvement, and roles. Paying for an assessment does not by itself demonstrate independence.

## 2. Freeze the verification scope

Freeze the class, items, lineage, scope, evaluation date, rule and data versions, implementation manifest, test plan, sampling rules, critical gates, necessary evidence, and procedures for disputes and retesting. Do not audit only selected successes. Verifiers must be able to reference the same versions of the manifest, results, and sampling plan.

A Verified claim for an entire class requires independent rechecking of all its item values, missing states, gates, and aggregation, together with sampled test checks under the plan. State what was sampled and what was not rerun. If a test, such as a hazardous physical action, cannot be rerun, distinguish record audits from witnessed observation and do not claim unverified scope.

## 3. Procedure

1. **Identify the target.** Check code, models, settings, media, and environment versions against the actual execution manifest. Do not substitute tests of an earlier version for success of the current configuration.
2. **Inspect the plan and all outcomes.** Check planned opportunities, failures, technical retries, missing evidence, exclusions, and interventions. Distinguish unsupported required capabilities scored 0 from missing observations retained as null.
3. **Check original evidence.** Trace inputs, actual requests, delivered text, audio and video, commands, receipts, states, and the owner, time, and branch of quoted evidence. A matching hash does not establish content truth.
4. **Rerate independently.** Initially hide developer scores, other verifiers' scores, and LLM suggestions. Use references and frozen anchors, retaining pre-adjudication values, support, and counterevidence.
5. **Sample tests.** Check ordinary, stress, and held-out conditions through the preregistered sampling procedure. Record whether checking used witnessing, external challenges, reruns, or stored-record audits.
6. **Adjudicate disagreements.** Append adjudication records without replacing initial ratings. Retain unresolved results as `disputed` and null. A vote cannot create missing evidence.
7. **Check aggregation and clocks.** Check fixed denominators, weights, completeness, caps, rounding, publication, registration, independent observation, and scope inheritance.
8. **Issue a scoped statement.** Report checked results, limitations, critical gates, retesting conditions, and the verifiers.

Domain O requires original responses from participants who experienced the interaction. A verifier's inference that a participant “must have felt presence,” or an LLM response, cannot replace them. Two verifiers and O's participant count are separate requirements.

## 4. Verification records

| Record | Required content |
|---|---|
| Target | Class, items, configuration hash, lineage, scope, evaluation time |
| People | Potentially pseudonymous identifiers, roles, independence and conflict disclosures |
| Checks | Original evidence, sampling plan, checks performed, rerun and non-rerun portions |
| Ratings | At least two independent values, grounds, pre/post-adjudication records, unresolved issues |
| Procedure | Interventions, version differences, missing and unsupported states, caps, critical gates |
| Statement | Verified scope, result, limitations, changes requiring rechecking |

A machine tool accepting verification records and arithmetic does not certify verifier independence, evidence truth, or semantic judgments. External verifier records and accessible supporting evidence are required.

## 5. Display and changes

Report results and procedures together, for example: “Core 420/590, CEPB 1.0.0, declared scope independently rerated and sampled by two third parties.” If evidence is missing, report an arithmetic range and gaps instead of a completed score. An audit confirming failures is still a useful verification result. Verified is not another name for high quality.

Unresolved critical gates suspend a perfect-result conformity claim. A minor misreading is not a permanent disqualification; record its scope and retesting. Do not automatically inherit an earlier Verified status after changes to models, prompts, memory, media, tools, or environments. Apply the change classification and bridge tests in [LONGITUDINAL](LONGITUDINAL.md), and update current capabilities and verified scope.

An Integrated 1000 conformity statement requires every unrounded final value to equal 5, all necessary opportunities, 36 calendar months for the lineage and every certified scope, final-configuration checks, required independent verification, and no unresolved critical gates. Writing this document, self-declaration, or rounding a display does not satisfy the conditions.
