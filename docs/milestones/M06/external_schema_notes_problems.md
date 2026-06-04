# External Schema Notes — problems.jsonl

**Milestone:** M06  
**Authorization:** `M06_SCHEMA_INSPECTION_AUTHORIZED = yes`  
**Posture:** Derived notes only — no raw rows committed

---

## File record

| Field | Value |
| ----- | ----- |
| **file_name** | `problems.jsonl` |
| **external_source** | `C:\coding\nemotron-inspect\problems.jsonl` (outside FORGE working tree) |
| **baseline_commit** | `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85` |
| **file_size_bytes** | 941081 |
| **sha256** | `4b8bd8b62905fe156ffc9033f5677286e75a80e907841b0988a4b50cc4b8742e` |
| **row_count** | 9500 (full line count) |
| **inspection_date_utc** | 2026-06-04 |
| **inspector** | Cursor (M06 Gate B) |

---

## Schema

| top_level_key | value_type | sample_notes |
| ------------- | ---------- | ------------ |
| `id` | str | Problem identifier |
| `category` | str | Category label |
| `status` | str | Pipeline status (e.g. lifecycle state) |
| `submission` | str | Problem statement / submission text (short in sample0) |

---

## Semantics

| Question | Answer |
| -------- | ------ |
| Prompt field name(s) | `submission` (problem text presented to model) |
| Completion / trace field name(s) | **none** in this file |
| Answer field name(s) | **none** in this file (see `generation.jsonl` / `corpus.jsonl`) |
| Category field (if any) | `category` |
| `\boxed{}` present in samples? | **no** in first 50 `submission` values |
| Other format constraints | `status` tracks investigation/generation lifecycle |

---

## FORGE mapping

| Baseline field | FORGE `EvaluationExample` / synthetic field | Status |
| -------------- | ------------------------------------------- | ------ |
| `submission` | `prompt` | **mapped** |
| `id` | `example_id` | **mapped** |
| `category` | `category` | **mapped** |
| `status` | metadata only (not in EvaluationExample) | **partial** |

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
| SQ-PROB-001 | Enumerated values for `status` across full file | M07 optional |
| SQ-PROB-002 | Join semantics `problems.id` ↔ `corpus.problem_id` ↔ `generation.id` | M07 |

---

## Non-claims

- [x] Does **not** claim baseline reproduction or score parity.
- [x] Does **not** authorize training.
- [x] Raw problem rows are **not** committed to FORGE.
