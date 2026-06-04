# External Schema Notes — generation.jsonl

**Milestone:** M06  
**Authorization:** `M06_SCHEMA_INSPECTION_AUTHORIZED = yes`  
**Posture:** Derived notes only — no raw rows committed

---

## File record

| Field | Value |
| ----- | ----- |
| **file_name** | `generation.jsonl` |
| **external_source** | `C:\coding\nemotron-inspect\generation.jsonl` (outside FORGE working tree) |
| **baseline_commit** | `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85` |
| **file_size_bytes** | 4774648 |
| **sha256** | `58383d4ecb831d9a6567a34a9cccb0a48ba78c1511790eb981c011685ccd315d` |
| **row_count** | 9500 (full line count) |
| **inspection_date_utc** | 2026-06-04 |
| **inspector** | Cursor (M06 Gate B) |

---

## Schema

| top_level_key | value_type | sample_notes |
| ------------- | ---------- | ------------ |
| `id` | str | Problem id (aligns with `problems.jsonl`) |
| `answer` | str | Reference answer |
| `any_correct` | bool | Aggregate correctness flag |
| `latest_correct` | bool | Latest run correctness |
| `latest_extracted` | str | Extracted answer from latest run |
| `latest_avg_logprob` | float | Latest run metric |
| `latest_min_logprob` | float | Latest run metric |
| `latest_num_gen_tokens` | int | Latest run token count |
| `latest_run` | str | Latest run identifier |
| `num_runs` | int | Count of generation runs |
| `runs` | list[object] | Per-run records (see nested keys below) |

**Nested `runs[]` object keys (sample run[0]):**

| key | value_type |
| --- | ---------- |
| `run` | str |
| `correct` | bool |
| `extracted_answer` | str |
| `avg_logprob` | float |
| `min_logprob` | float |
| `num_gen_tokens` | int |
| `num_prompt_tokens` | int |

---

## Semantics

| Question | Answer |
| -------- | ------ |
| Prompt field name(s) | **not in file** — join to `problems.submission` |
| Completion / trace field name(s) | **not in file** — run metadata only |
| Answer field name(s) | `answer`; model output via `latest_extracted` / `extracted_answer` |
| Category field (if any) | **none** at top level |
| `\boxed{}` present in samples? | **no** in first 50 rows (full-row scan) |
| Other format constraints | Multiple runs per problem; logprob fields for filtering |

---

## FORGE mapping

| Baseline field | FORGE `EvaluationExample` / synthetic field | Status |
| -------------- | ------------------------------------------- | ------ |
| `answer` | `expected` | **mapped** |
| `latest_extracted` | prediction completion (eval input) | **partial** |
| `id` | `example_id` | **mapped** |
| `runs[].extracted_answer` | per-run prediction for eval harness | **partial** |
| `latest_correct` / `correct` | local metric alignment check | **partial** |

---

## License and redistribution

| Item | Notes |
| ---- | ----- |
| LICENSE observed | **no** at repo root |
| Redistribution of rows into FORGE repo | **not allowed** in M06 |
| Copying policy for FORGE | `no_code_copy` |

---

## Open questions

| ID | Question | Owner |
| -- | -------- | ----- |
| SQ-GEN-001 | Whether full model completions are stored elsewhere (not in JSONL top-level) | M07 |
| SQ-GEN-002 | Extraction logic parity with FORGE `metric.boxed` | M07 eval gate |

---

## Non-claims

- [x] Does **not** claim baseline reproduction.
- [x] Does **not** authorize training.
- [x] Raw generation rows are **not** committed to FORGE.
