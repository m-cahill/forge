# M02_plan.md — Exact Local Evaluation and Artifact Discipline

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M02 |
| **Title** | Exact Local Evaluation and Artifact Discipline |
| **Branch** | `forge/M02-local-eval` |
| **Status** | **active** — implementation complete; PR pending |
| **Precondition** | M01 merged to `main`; post-merge CI green; owner authorized kickoff 2026-06-04 |
| **Primary goal** | Make every future candidate locally scoreable, hashable, comparable, and auditable before spending Kaggle submissions |

---

## 1. Objective

M02 turns FORGE's M01 foundations into a deterministic local evaluation and artifact-governance layer.

By the end of M02, FORGE should be able to:

1. Score fixture predictions using the boxed-answer metric from M01.
2. Produce local evaluation reports with overall and per-category accuracy.
3. Write run manifests for evaluation runs.
4. Hash configs, datasets, predictions, packages, and reports.
5. Create and validate small fixture holdouts.
6. Run a tiny end-to-end smoke path (fixture examples → predictions → CLI → report → manifest → hashes).
7. Preserve explicit non-claims: no Kaggle submission, public score, training, inference, reproduced baseline, or Kaggle-ready adapter.

---

## 2. Locked decisions (owner 2026-06-04)

| Topic | Decision |
| ----- | -------- |
| Extra predictions | Warn by default; `--strict-extra-predictions` for nonzero exit |
| `metric_version` | `boxed_v1@forge_nemotron-0.1.0` (not hash of `boxed.py`) |
| Fixture holdout | Register `m02_fixture_holdout` as active-fixture; production holdouts remain planned |
| Evidence | Commit tiny files under `docs/milestones/M02/evidence/fixture_eval/` |
| PR strategy | One branch, one PR, five logical commits |
| Stretch | `--category-filter` if cheap; defer JSON Schema and Markdown reports |

---

## 3. Deliverables

| ID | Deliverable | Path |
| -- | ----------- | ---- |
| D1 | Evaluation records | `src/forge_nemotron/eval/records.py` |
| D2 | Local scorer + module CLI | `src/forge_nemotron/eval/scorer.py` |
| D3 | Eval CLI wrapper | `scripts/eval_predictions.py` |
| D4 | Artifact hashing | `src/forge_nemotron/artifacts/hashing.py` |
| D5 | Run manifest builder | `src/forge_nemotron/reports/run_manifest.py` |
| D6 | Fixture JSONL | `tests/fixtures/eval/` |
| D7 | Holdout manifest | `data/manifests/m02_fixture_holdouts.json` |
| D8 | Unit tests | `tests/unit/test_eval_scorer.py`, `test_artifact_hashing.py`, `test_run_manifest.py` |
| D9 | Committed evidence | `docs/milestones/M02/evidence/fixture_eval/` |
| D10 | Docs | `docs/forge.md`, `README.md`, `scripts/README.md` |

---

## 4. Hard constraints

- No Kaggle submission in M02.
- No model training or inference.
- No public baseline reproduction claim.
- Fixture packages/predictions labeled as fixtures only.
- Fixture holdout must not be used for training.

---

## 5. Implementation phases

### Phase A — Branch and milestone setup

- Commit authorized M01 Kaggle intake on `main` if present.
- Branch `forge/M02-local-eval` from clean `main`.
- Expand this plan; update `M02_toolcalls.md`, `docs/forge.md`, `README.md`.

### Phase B — Evaluation records and scorer

- `EvaluationExample`, `EvaluationPrediction`, `EvaluationResult`, `CategoryScore`
- `score_examples()` → `EvalReport`
- Unit tests in `test_eval_scorer.py`

### Phase C — Artifact hashing and manifest

- `sha256_file`, `sha256_json`, `write_json`, etc.
- `build_run_manifest()`
- Unit tests

### Phase D — CLI and fixtures

- `scripts/eval_predictions.py`
- Fixture JSONL + holdout manifest
- Smoke run

### Phase E — Documentation and evidence

- Update governance docs; commit tiny fixture evidence.

---

## 6. Acceptance criteria

- [ ] Branch `forge/M02-local-eval` from green `main`
- [ ] Expanded `M02_plan.md` and `M02_toolcalls.md`
- [ ] `docs/forge.md` marks M02 active
- [ ] Evaluation records and scorer exist
- [ ] CLI produces JSON, CSV, failures JSONL, manifest, `input_hashes.json`
- [ ] Per-category reporting and failure report
- [ ] Hashing utilities and manifest builder tested
- [ ] Fixture data and holdout manifest
- [ ] Tiny fixture eval smoke succeeds
- [ ] CI green on PR
- [ ] No Kaggle submit / score / training / inference claims

---

## 7. Non-claims

- No Kaggle submission, public/private score, training, inference, reproduced baseline, Kaggle-ready adapter, or holdout used for training.

---

*Full historical stub retained in git history; expanded 2026-06-04 per owner-authorized M02 kickoff.*
