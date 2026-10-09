# Adapters and observation evidence

[日本語](../ja/ADAPTER_GUIDE.md) | [CLI](CLI.md)

CEPB does not require an internal API from any particular model or framework. Manual chat, local models, hosted services, games, voice apps, and robots can save equivalent kinds of evidence. `cepb.py` does not invoke a generator; it validates and aggregates saved ratings.

## Adapter responsibilities

1. Receive frozen cases, character definition, histories, and budgets.
2. Create isolated histories from declared baseline states and operate the system in the planned order and repetitions.
3. Save **actual transmitted input and actually delivered output**. A planned prompt or internal draft is not a delivered response.
4. Record matching timestamps, turn/request IDs, owners, branches, and interventions.
5. Save commands, receipts, and independent before/after state when actions occur.
6. Have humans annotate the oracles and enter item-bundle ratings into the campaign JSON.

## Example event ledger

This is a recommended interchange format, not a CLI input that receives automatic semantic grading.

```json
{"event_id":"event_001","campaign_id":"demo","history_id":"history_01","case_id":"c2_ordinary_01","repeat_index":1,"turn_id":"turn_01","request_id":"request_01","timestamp_utc":"2026-10-10T01:00:00Z","clock_kind":"real","source_kind":"delivered_output","artifact_ref":"raw/turn_01.txt","sha256":"actual_digest_from_saved_bytes"}
```

`timestamp_utc` is real UTC calendar time. Store simulation time separately. Prefer `artifact_ref` relative to the campaign file. Derived summaries, anonymization, and synchronization transforms require new IDs, original references, and processing history. A hash checks content changes; it does not alone prove truthful execution or existence at a claimed time.

## World and media evidence

Distinguish speech synthesis requests, completed audio, actual playback start/end, interruption, and recognized input. Separate a selected avatar state from actual display. Tag worlds as virtual, digital, or physical and separate observations from generated narrative. Retain post-stop actions, delayed deliveries, and duplicate receipts.

## Histories and repetitions

Different seeds from one checkpoint are repetitions, not automatically independent life histories. Construct at least two evaluation histories with different eligible experience content. Do not feed sibling-branch results into each other, and isolate interventions. Experience retrieval, agreement pressure, new facts, and world changes are different comparisons.

Do not insert evaluator-only answers, anchors, or held-out challenges into the character's regular generation prompt to elicit benchmark performances. If an LLM assists annotation, separately retain its model, prompt, output, and disagreement with humans.

## Sharing evidence

Personal information need not be published. Follow participant permissions and separate audit originals from public excerpts and aggregates. Record access rights and retention periods. CEPB's MIT license does not grant permission to redistribute other people's dialogue or avatars.
