# SQ-CORPUS-001 Resolution Plan — M08

**ID:** SQ-CORPUS-001  
**Status:** **open** (not resolved or waived in M08)  
**Topic:** `corpus.segment` structure and mapping to FORGE training trace fields

---

## 1. Current issue

External baseline `corpus.jsonl` includes a `segment` field whose full structure and mapping to FORGE SFT fields (prompt/completion, trace boundaries, `\boxed{}` placement) is **partially** documented in M06 and carried as **open** in M07.

---

## 2. Evidence from M06/M07

| Source | Finding |
| ------ | ------- |
| M06 mapping supplement | `corpus.segment` marked **partial** |
| M06 schema notes | 17,963 rows; SHA256 recorded; derived notes only in repo |
| M07 baseline schema decision | SQ-CORPUS-001 **open**; `\boxed{}` not observed in M06 sample window |
| M07 training gate | Schema inspection **complete**; mapping gap does not block Path A documentation |

---

## 3. Impact on training

| Impact | Assessment |
| ------ | ------------ |
| Gate C documentation | Does not block M07/M08 readiness **documentation** |
| Confident training config | **May block** — unclear SFT field split from `corpus.segment` |
| Submission | **No** direct block |
| Readiness manifest | Listed blocker: `sq_corpus_001_open` |

---

## 4. Options

| Option | Description | M08 stance |
| ------ | ----------- | ---------- |
| A | Resolve by deeper schema inspection (authorized external read; no raw data in repo) | Deferred — not executed in M08 |
| B | Waive with owner rationale + `schema_inspection_waiver` in manifest | Not applied — no owner waiver |
| C | Avoid corpus; use `train.csv` first for initial SFT | **Recommended interim** — lower mapping risk |
| D | Build FORGE-compatible conversion pipeline later | Future milestone |

---

## 5. Recommendation

**Primary:** Option **C** for first controlled training attempt — prioritize `train.csv` (documented `prompt`/`answer` columns) while SQ-CORPUS-001 remains open.

**Parallel:** Option **A** if owner wants corpus-based reproduction fidelity before training.

**Do not** treat partial mapping as resolved without evidence or explicit waiver.

---

## Exit criteria

- Documented mapping policy in reproduction plan **or**
- Owner waiver with rationale recorded **or**
- Demonstrated conversion artifact with hashes (no raw baseline rows in FORGE repo)

---

## Non-claims

- No new external schema inspection in M08.
- No raw baseline data committed.
