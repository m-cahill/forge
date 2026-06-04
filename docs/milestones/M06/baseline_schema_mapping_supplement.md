# Baseline-to-FORGE Schema Mapping Supplement

**Milestone:** M06  
**Baseline commit:** `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85`  
**Source:** Gate B external schema inspection (derived notes only)

---

## Mapping table

| Baseline field | Meaning | FORGE type/field | Status |
| -------------- | ------- | ---------------- | ------ |
| `problems.submission` | Problem statement text | `EvaluationExample.prompt` | **mapped** |
| `train.csv` `prompt` | Tabular prompt | `EvaluationExample.prompt` | **mapped** |
| `corpus.segment` | Training segment (may include prompt+trace) | `prompt` / training trace fields | **partial** |
| `generation.latest_extracted` | Model extracted answer (latest run) | prediction completion (eval) | **partial** |
| `generation.runs[].extracted_answer` | Per-run extracted answer | prediction completion | **partial** |
| `corpus.answer` / `generation.answer` / `train.csv` `answer` | Ground truth | `EvaluationExample.expected` | **mapped** |
| `problems.category` / `corpus.category` | Category label | `EvaluationExample.category` | **mapped** (where present) |
| `train.csv` | No category column | `category` | **unknown** |
| `problems.id` / `corpus.problem_id` / `generation.id` | Identifiers | `example_id` | **partial** (transform TBD) |
| `\boxed{}` in corpus/problems/generation samples | Competition output format | `metric.boxed` extraction | **unknown** in inspected samples (0 hits in first 50–100 rows per file) |

---

## Cross-file join model (observed)

```text
problems.id  ←→  generation.id  (9500 rows each)
corpus.problem_id  ←→  problems.id  (17963 corpus rows)
train.csv  (69029 rows) — relationship to corpus TBD (SQ-CSV-001)
```

---

## Gaps for M07

1. **Segment structure** — how `corpus.segment` maps to SFT prompt/completion pairs.
2. **Boxed formatting** — whether baseline adds `\boxed{}` during training vs at inference only.
3. **Category on train.csv** — absent; may need join or default policy.
4. **Eval predictions** — generation file stores extracted answers, not full completions.

---

## Non-claims

- No byte-level compatibility or score parity claimed.
- No raw baseline data included in this document.
- Training not authorized (`M06_TRAINING_AUTHORIZED = no`).
