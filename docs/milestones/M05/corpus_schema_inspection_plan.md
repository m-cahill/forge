# Corpus Schema Inspection Plan

**Milestone:** M05  
**Purpose:** Cursor-executable workflow for a **future authorized milestone**  
**Status:** Plan only — **no schema extraction in M05**

---

## 1. Preconditions (future milestone)

Before any inspection:

1. Owner authorizes external clone/download and schema work.
2. [`baseline_acquisition_policy.md`](baseline_acquisition_policy.md) reviewed and accepted.
3. Reproduction plan manifest updated with `data_sources` and inspection run ID.
4. Confirm no large files will be committed to FORGE.

---

## 2. Cursor-executable workflow

### Step 1 — Clone outside FORGE

```text
# Example: operator-chosen path OUTSIDE repo root
# e.g. C:\external\nemotron-inspect (Windows) or ~/external/nemotron-inspect (Linux)
git clone https://github.com/tonghuikang/nemotron.git <external_path>
cd <external_path>
git rev-parse HEAD   # record commit for manifest
```

**Rules:**

- Clone path must **not** be inside the FORGE git working tree.
- Do not add the clone as a submodule or subtree of FORGE.

### Step 2 — Identify target files

Inspect (read-only) as needed:

| File | Typical role |
| ---- | ------------ |
| `corpus.jsonl` | Training corpus |
| `problems.jsonl` | Problem definitions |
| `generation.jsonl` | Generation outputs |
| `train.csv` | Tabular training export |
| `vocab.jsonl` / `vocab.json` | Vocabulary |

Record file size and SHA256 from external path only.

### Step 3 — Sample inspection (no bulk commit)

- Read at most **N** lines per file (e.g. N ≤ 5) for schema inference.
- Use `jq`, Python one-liner, or editor — output goes to **derived notes**, not raw dump in FORGE.
- If `\boxed{}` appears in samples, note field names and frequency qualitatively.

### Step 4 — Complete schema notes template

Copy [`external_schema_notes_template.md`](external_schema_notes_template.md) to a new file, e.g.:

```text
docs/milestones/M06/external_schema_notes_corpus.md
```

Fill all fields. Commit **only** the derived notes document, not source JSONL.

### Step 5 — Map to FORGE

| Baseline concept | FORGE target |
| ---------------- | ------------ |
| Prompt / problem text | `EvaluationExample` input fields |
| Completion / reasoning trace | Eval prediction or training trace fields |
| Final answer | `\boxed{}` extraction via `forge_nemotron.metric.boxed` |
| Category | `category` tag on examples |
| Synthetic parallel | M03 `make_dataset.py` JSONL schema |

Document gaps as **unknown** until evidenced.

### Step 6 — Update governance

- Update `docs/forge.md` Dataset Ledger or milestone notes.
- Update reproduction plan manifest `data_sources` with hashes.
- Do not claim corpus parity or reproduction.

---

## 3. Prohibited in inspection milestone

- Committing baseline repo, code, corpus, tokenizer, checkpoints
- Training or inference on inspected data without separate authorization
- Guessing hyperparameters or schema fields not observed in samples

---

## 4. Expected outputs

| Output | Location |
| ------ | -------- |
| Filled schema notes | `docs/milestones/MNN/external_schema_notes_*.md` |
| Manifest update | Reproduction plan or run manifest hashes |
| Mapping table | Milestone doc or `baseline_format_mapping` supplement |

---

## 5. M05 boundary

M05 delivers this plan and [`external_schema_notes_template.md`](external_schema_notes_template.md) only.

M05 does **not** perform Steps 1–6 unless separately authorized.
