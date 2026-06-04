# Baseline Acquisition Policy

**Milestone:** M05  
**Applies to:** Future milestones inspecting or reproducing `tonghuikang/nemotron`  
**Status:** Active policy — M05 performs no acquisition

---

## 1. Principles

1. **Clean-room FORGE:** FORGE source tree contains FORGE implementations only.
2. **External reference:** Public baseline is cited by URL, file names, and commands — not vendored.
3. **Evidence over copy:** Record hashes, schema notes, and provenance — not large blobs in git.
4. **License posture:** No root LICENSE observed; default is **no code copy** until governance updates.

---

## 2. Allowed actions (future, with owner authorization)

| Action | Allowed | Where |
| ------ | ------- | ----- |
| Clone public repo for read-only analysis | Yes | **Outside** FORGE working tree |
| Read file listings, README, script names | Yes | External clone or GitHub API |
| Inspect small samples of JSONL/CSV | Yes | External only; derived notes in FORGE docs |
| Record SHA256, row counts, field names | Yes | `external_schema_notes_template.md` |
| Hash corpora for manifest | Yes | Hash in docs/manifests — not the file in repo |

---

## 3. Prohibited actions

| Action | Prohibited |
| ------ | ---------- |
| Commit clone, baseline Python code, or submodules into FORGE | Yes |
| Commit `corpus.jsonl`, `tokenizer.json`, checkpoints, adapters, zips | Yes |
| Paste baseline implementation into FORGE modules | Yes |
| Train on holdout or competition-private data without provenance | Yes |
| Assume license permits copying without recorded evidence | Yes |

---

## 4. Small samples

If a tiny schema sample is needed for validation:

| Preferred | Avoid |
| --------- | ----- |
| Hand-authored schema sketch | Raw corpus rows in repo |
| Redacted tiny sample (non-committed) | Full `corpus.jsonl` commit |
| Derived field list and types | Tokenizer binary in repo |
| Mapping table to FORGE types | Checkpoints or adapter weights |

---

## 5. Recording external paths

- Record external clone paths in **local operator notes** or milestone toolcalls — not as committed secrets.
- Reproduction plan manifest may reference `baseline_repo` URL and optional `baseline_commit`.
- Do not commit `.env`, API keys, or Modal/Tinker credentials.

---

## 6. M05 scope

M05 defines this policy only. M05 does **not**:

- Clone the baseline repo
- Download corpora into FORGE
- Extract schema from live files
- Authorize training

Owner must authorize acquisition and inspection in a future milestone before Cursor executes external clone/download workflows.
