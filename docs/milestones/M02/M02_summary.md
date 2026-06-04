# 📌 Milestone Summary — M02: Exact Local Evaluation and Artifact Discipline

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Evaluation and artifact governance (pre–Lane A reproduction)  
**Milestone:** M02 — Exact Local Evaluation and Artifact Discipline  
**Timeframe:** 2026-06-04  
**Status:** Closed — PR [#3](https://github.com/m-cahill/forge/pull/3) **merged** to `main` (`e78dc97`)  
**Branch:** `forge/M02-local-eval` (merged)  
**PR head (pre-merge):** `cfd39707116a218d2b44920c28479fec701be12b`  
**Squash merge on `main`:** `e78dc975c278c73edffb4b920cf72a067c781420`  
**Post-merge CI:** [26973864069](https://github.com/m-cahill/forge/actions/runs/26973864069) green  
**Baseline:** M01 merged `d59d97b`; M01 Kaggle intake on `main` `ce9dc7f`

---

## 1. Milestone Objective

Make every future adapter candidate locally scoreable, hashable, comparable, and auditable **before** spending Kaggle submissions.

Without M02, FORGE could not record per-category local scores, input hashes, or run manifests alongside package validation — blocking safe candidate promotion per `docs/forge.md` §11.

---

## 2. Scope Definition

### In Scope

- `src/forge_nemotron/eval/` — records, `score_examples()`, module CLI
- `src/forge_nemotron/artifacts/hashing.py` — SHA256 file/text/JSON
- `src/forge_nemotron/reports/run_manifest.py` — local eval manifests
- `scripts/eval_predictions.py` — wrapper CLI (`--strict-extra-predictions`, `--category-filter`)
- Fixture JSONL under `tests/fixtures/eval/`
- `data/manifests/m02_fixture_holdouts.json`
- Committed fixture evidence `docs/milestones/M02/evidence/fixture_eval/`
- Unit tests (+15): `test_eval_scorer`, `test_artifact_hashing`, `test_run_manifest`
- `docs/forge.md`, README, `scripts/README.md`, M02 plan/toolcalls/run1/summary/audit

### Out of Scope

- Kaggle submission, public/private score
- Model training, inference, adapter generation
- Reproduction of `tonghuikang/nemotron`
- Production holdout activation (public_train, synthetic_balanced, hard_category, formatting_edge remain planned)
- JSON Schema for manifests, Markdown report output (deferred stretch)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Eval engine | `EvaluationExample` / `Prediction` / `Result` / `CategoryScore`; deterministic scorer |
| Artifacts | Canonical JSON hashing; `write_json` |
| Manifests | `build_run_manifest()` with `metric_version=boxed_v1@forge_nemotron-0.1.0` |
| CLI | JSON + CSV + failures JSONL + `input_hashes.json` + manifest |
| Fixtures | 8 examples, 3 prediction sets; holdout manifest + register row |
| Evidence | Mixed-pred smoke **6/8 = 0.75** committed as fixture-only |
| Governance | M02 active → closeout; Run Ledger entry; M03 stub |

**Commits on branch (implementation):** `c825f88`, `59d0f51`, `32f4043`, `a0a5580`, `61fe3ad`, `c8dc65b` (+ `ce9dc7f` M01 intake in PR base from `main`)

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `ruff check .` | Pass | Local + CI |
| `ruff format --check .` | Pass | Local + CI |
| `mypy src tests` | Pass | Local + CI |
| `pytest -q` | Pass | **106** tests (local + CI) |
| `compileall src` | Pass | Local |
| GitHub Actions PR #3 | **Green** | [26973038855](https://github.com/m-cahill/forge/actions/runs/26973038855) |
| Fixture eval smoke | Pass | **0.75** on `predictions_mixed.jsonl` — **not** a Kaggle/public score |
| Kaggle submission / training / reproduction | **Not claimed** | Explicit non-claims preserved |

---

## 5. CI / Automation Impact

- No workflow file changes; existing M01 CI certifies M02 delta.
- Test count increased 91 → 106 without gate weakening.
- Post-merge CI on `main` after PR #3 merge: **green** — [26973864069](https://github.com/m-cahill/forge/actions/runs/26973864069) on `e78dc97`.

---

## 6. Issues & Exceptions

| Issue | Root cause | Status | Reference |
| ----- | ---------- | ------ | --------- |
| Submit UI zip constraints | Owner not recorded | Open | `docs/forge.md` §M01 |
| Fixture 0.75 vs leaderboard | By design — mixed fixture preds | Documented | Evidence README + audit |
| `git` metadata in manifest | Optional; `unknown` + warning if absent | Documented | `run_manifest.py` |

No HIGH implementation defects blocking M02 closeout.

---

## 7. Deferred Work

| Item | Why deferred | Status |
| ---- | ------------ | ------ |
| JSON Schema for eval/manifest | Stretch | M02+ |
| Markdown eval report | Stretch | M02+ |
| Production holdouts | No real sources/hashes yet | Planned |
| Public baseline training | After M02 merge | M03+ / Lane A |
| Kaggle API submit | Not evidenced | Open |

---

## 8. Governance Outcomes

What is now provably true:

- **Local eval CLI** scores JSONL examples/predictions with M01 boxed metric.
- **Per-category** CSV and failure JSONL are produced deterministically.
- **Hashes** and **run manifests** record inputs and `metric_version`.
- **`m02_fixture_holdout`** is active-fixture, evaluation-only, never for training.
- **Fixture evidence 0.75** is labeled local-only; must not be cited as public/private score.

---

## 9. Fixture Score Disclaimer (required)

The committed smoke result **6/8 = 0.75** (`predictions_mixed.jsonl`) is:

- hand-authored fixture data only,
- local evaluation only,
- **not** leaderboard evidence,
- **not** a Kaggle or public score,
- **not** produced by model inference.

Future candidate comparisons must use recorded local eval artifacts with hashes, not this number alone.

---

## 10. Exit State

| Criterion | Met |
| --------- | --- |
| M02 deliverables implemented | Yes |
| PR CI green | Yes — run 26973038855 |
| Summary + audit + run1 | Yes |
| Non-claims preserved | Yes |
| Merged to `main` | Yes — `e78dc97` |

**Next recommendation:** Authorize M03 solver factory planning on a new branch; owner records Submit UI zip constraints; defer Kaggle submit until package validation + local eval on real candidates.
