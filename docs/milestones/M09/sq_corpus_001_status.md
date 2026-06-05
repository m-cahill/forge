# SQ-CORPUS-001 Status — M09

**ID:** SQ-CORPUS-001  
**Topic:** `corpus.segment` structure and mapping to FORGE SFT fields  
**Milestone:** M09

---

## Status

```text
SQ-CORPUS-001 remains open.
Interim training path should prefer train.csv first.
```

No new owner evidence or schema inspection was performed in M09.

---

## Carry-forward (M06/M07/M08)

| Item | State |
| ---- | ----- |
| `corpus.segment` mapping | **partial** |
| `\boxed{}` in inspected samples | not observed in M06 sample window |
| Schema inspection gate | **complete** (M06) |
| Training blocked by SQ-CORPUS alone? | **maybe** for corpus-first SFT; not for `train.csv`-first interim |

See [`docs/milestones/M08/sq_corpus_001_resolution_plan.md`](../M08/sq_corpus_001_resolution_plan.md).

---

## Decision options (unchanged)

| Option | M09 stance |
| ------ | ---------- |
| 1. Keep open; prefer `train.csv` first | **default** |
| 2. Waive with owner rationale | not applied |
| 3. Resolve via deeper schema inspection | deferred |
| 4. Build conversion pipeline later | future milestone |

---

## Manifest

Blocker: `sq_corpus_001_open` in [`evidence/readiness/public_control_repro_plan.modal_tinker_gate.json`](evidence/readiness/public_control_repro_plan.modal_tinker_gate.json).

---

## Non-claims

- No raw baseline data committed in M09.
- Open status does not imply `train.csv` is fully mapped for all competition categories.
