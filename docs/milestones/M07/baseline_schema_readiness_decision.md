# Baseline Schema Readiness Decision

**Milestone:** M07  
**Baseline commit (M06 inspection):** `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85`  
**Source:** M06 derived schema notes only — no new external inspection in M07

---

## Decision table

| Area | Status | Notes |
| ---- | ------ | ----- |
| `corpus.jsonl` schema | **ready** | Keys, row count (17,963), SHA256 recorded; derived notes at `docs/milestones/M06/external_schema_notes_corpus.md` |
| `problems.jsonl` schema | **ready** | 9,500 rows; join to `generation.id` observed |
| `generation.jsonl` schema | **ready** | 9,500 rows; `runs[]`, `latest_extracted` documented |
| `train.csv` schema | **ready** | 69,029 rows; `prompt`/`answer` columns; category absent |
| `corpus.segment` mapping | **partial** | SQ-CORPUS-001 — SFT prompt/completion structure not fully resolved |
| `\boxed{}` visibility | **not observed** | 0 hits in first 50–100 rows per file (M06); competition still requires `\boxed{}` at eval |

---

## SQ-CORPUS-001

**ID:** SQ-CORPUS-001  
**Status:** **open**  
**Topic:** `corpus.segment` structure and mapping to FORGE training trace fields  

**Evidence:**

- M06 mapping supplement marks `corpus.segment` as **partial**.
- Segment may embed prompt+trace; exact SFT field split not proven in FORGE.

**M07 decision:** Remains **open**. Does not block M07 training-authorization **documentation** on Path A. May block confident training **execution** until resolved or explicitly waived by owner with rationale.

**Exit criteria:** Documented mapping policy or owner waiver recorded in reproduction plan with `schema_inspection_waiver` if training proceeds before full resolution.

---

## Readiness vs authorization

| Question | M07 answer |
| -------- | ---------- |
| Is external schema inspection complete? | **Yes** (M06 Gate B) |
| Is FORGE mapping sufficient for training without gaps? | **No** — partial segment mapping + boxed visibility unknown in corpus |
| Does schema alone authorize training? | **No** — Gate C required |

---

## Non-claims

- No raw baseline rows in this document.
- No score parity or reproduction claim.
- No assertion that `\boxed{}` is absent from full corpus — only **not observed** in M06 sample window.
