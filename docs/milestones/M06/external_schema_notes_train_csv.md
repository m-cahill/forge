# External Schema Notes — train.csv

**Milestone:** M06  
**Authorization:** `M06_SCHEMA_INSPECTION_AUTHORIZED = yes`  
**Posture:** Derived notes only — no raw rows committed

---

## File record

| Field | Value |
| ----- | ----- |
| **file_name** | `train.csv` |
| **external_source** | `C:\coding\nemotron-inspect\train.csv` (outside FORGE working tree) |
| **baseline_commit** | `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85` |
| **file_size_bytes** | 3138334 |
| **sha256** | `c99877aca84dc1564ef741a722a74458b06aa616b0b627d493a913063bd536ef` |
| **row_count** | 69029 (data rows; excludes header) |
| **inspection_date_utc** | 2026-06-04 |
| **inspector** | Cursor (M06 Gate B) |

---

## Schema

| column | value_type (sample) | sample_notes |
| ------ | ------------------- | ------------ |
| `id` | int/str | Row identifier |
| `prompt` | str | Input prompt text |
| `answer` | int/str | Target answer (numeric or string in samples) |

---

## Semantics

| Question | Answer |
| -------- | ------ |
| Prompt field name(s) | `prompt` |
| Completion / trace field name(s) | **none** |
| Answer field name(s) | `answer` |
| Category field (if any) | **none** |
| `\boxed{}` present in samples? | **no** in first 100 `prompt`/`answer` cells |
| Other format constraints | Tabular export; row count differs from `corpus.jsonl` (69029 vs 17963) |

---

## FORGE mapping

| Baseline field | FORGE `EvaluationExample` / synthetic field | Status |
| -------------- | ------------------------------------------- | ------ |
| `prompt` | `prompt` | **mapped** |
| `answer` | `expected` | **mapped** |
| `id` | `example_id` | **mapped** |
| category | `category` | **unknown** — column absent |

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
| SQ-CSV-001 | Relationship between `train.csv` and `corpus.jsonl` (different row counts) | M07 |
| SQ-CSV-002 | Whether CSV is export of competition train vs internal SFT set | Owner |

---

## Non-claims

- [x] Does **not** claim baseline reproduction.
- [x] Does **not** authorize training.
- [x] Raw CSV rows are **not** committed to FORGE.
