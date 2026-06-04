# External Schema Notes — corpus.jsonl

**Milestone:** M06  
**Authorization:** `M06_SCHEMA_INSPECTION_AUTHORIZED = yes`  
**Posture:** Derived notes only — no raw rows committed

---

## File record

| Field | Value |
| ----- | ----- |
| **file_name** | `corpus.jsonl` |
| **external_source** | `C:\coding\nemotron-inspect\corpus.jsonl` (outside FORGE working tree) |
| **baseline_commit** | `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85` |
| **file_size_bytes** | 42589263 |
| **sha256** | `1940a41c68d0f70013e0e448e04dd17c9143403bc1ce991e4603e9ad38b9fcf5` |
| **row_count** | 17963 (full line count) |
| **inspection_date_utc** | 2026-06-04 |
| **inspector** | Cursor (M06 Gate B) |

---

## Schema

| top_level_key | value_type | sample_notes |
| ------------- | ---------- | ------------ |
| `problem_id` | str | Join key to problems/generation `id` |
| `segment` | str | Training segment text (length varies; sample0 was 15 chars) |
| `category` | str | Category label |
| `masked_token_count` | int | Token accounting |
| `unmasked_token_count` | int | Token accounting |
| `token_count` | int | Token accounting |
| `answer` | str | Ground-truth answer string |
| `included` | bool | Inclusion flag for corpus row |

---

## Semantics

| Question | Answer |
| -------- | ------ |
| Prompt field name(s) | `segment` (training text segment; not named `prompt`) |
| Completion / trace field name(s) | Encoded inside `segment` (structure not fully parsed in M06 sample) |
| Answer field name(s) | `answer` |
| Category field (if any) | `category` |
| `\boxed{}` present in samples? | **no** in first 50 rows (segment and full-row scan) |
| Other format constraints | Token count fields suggest tokenizer-aware segmentation |

---

## FORGE mapping

| Baseline field | FORGE `EvaluationExample` / synthetic field | Status |
| -------------- | ------------------------------------------- | ------ |
| `segment` | `prompt` (partial — may embed prompt+trace) | **partial** |
| `answer` | `expected` | **mapped** |
| `category` | `category` | **mapped** |
| `problem_id` | `example_id` (with prefix/transform) | **partial** |
| `included` | dataset filter / manifest flag | **partial** |

---

## License and redistribution

| Item | Notes |
| ---- | ----- |
| LICENSE observed | **no** at repo root (M01/M04/M06) |
| Redistribution of rows into FORGE repo | **not allowed** in M06 — derived notes only |
| Copying policy for FORGE | `no_code_copy` |

---

## Open questions

| ID | Question | Owner |
| -- | -------- | ----- |
| SQ-CORPUS-001 | Exact structure inside `segment` (prompt vs completion boundaries) | M07 training gate |
| SQ-CORPUS-002 | Whether training applies `\boxed{}` wrapper post-hoc vs in corpus | M07 |
| SQ-CORPUS-003 | Mapping `included=false` rows to FORGE dataset policy | Owner |

---

## Non-claims

- [x] This fill does **not** claim baseline reproduction.
- [x] This does **not** authorize training.
- [x] Raw corpus rows are **not** committed to FORGE.
