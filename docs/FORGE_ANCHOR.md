# FORGE_ANCHOR.md

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Document type:** Anchor document, project charter, execution doctrine, and Cursor handoff  
**Status:** Initial anchor, to be committed at repo root  
**Created:** 2026-06-03  
**Primary objective:** Maximize probability of winning the final leaderboard prize while preserving prize eligibility, reproducibility, and enterprise-grade audit discipline.  
**Competition URL:** <https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge/overview>

---

## 0. Why this document exists

FORGE exists because we missed the midpoint entry but still have enough time to pursue the final competition seriously. This document is the anchor for that effort. It should be copied to `docs/` as `docs/FORGE_ANCHOR.md` and treated as the stable mental model for Cursor, ChatGPT, and human operators.

This document is not a milestone plan. It is the project’s strategic spine: what we are trying to accomplish, what we believe wins, what must not be violated, and how every milestone should behave.

The short version of the project thesis is:

> FORGE should not try to “fine-tune a reasoning model” in the generic sense. FORGE should build a solver-guided, metric-aligned, synthetic-data and LoRA-engineering system that teaches Nemotron-3-Nano-30B to emit the exact deterministic reasoning traces and `\boxed{}` answers this benchmark rewards.

---

## 1. Source-of-truth hierarchy

When sources conflict, use this order:

1. **Kaggle competition rules, overview, evaluation, and submission UI**  
   These define legal eligibility, submission format, deadlines, scoring, daily submission limits, and final prize requirements.

2. **`docs/forge.md` — Ultimate Truth**  
   This is the living ledger of FORGE milestones, decisions, run outcomes, CI status, Kaggle submission IDs, scores, deferrals, and final candidate selection. It must be updated with every material milestone and score-affecting decision.

3. **`docs/FORGE_ANCHOR.md` — this document**  
   This document defines posture and strategy. It is subordinate to `docs/forge.md` for actual project state. If strategy changes materially, update this document and record the reason in `docs/forge.md`.

4. **Milestone artifacts**  
   `docs/milestones/MNN/MNN_plan.md`, `MNN_summary.md`, `MNN_audit.md`, and any run-specific files. These are point-in-time evidence records.

5. **Experiment artifacts and manifests**  
   Dataset hashes, solver logs, adapter hashes, package hashes, local scores, public leaderboard scores, notebook versions, and final submission zips.

6. **Cursor/chat transcripts and scratch plans**  
   Useful context, but not authoritative unless promoted into `docs/forge.md` or a milestone artifact.

### Mandatory `docs/forge.md` update rule

Every milestone must update `docs/forge.md` with:

- milestone number and title,
- date and branch,
- objective,
- completed deliverables,
- CI/test status,
- run IDs and artifact hashes,
- Kaggle submission IDs and scores when applicable,
- material decisions,
- unresolved risks or deferrals,
- next recommended milestone.

No milestone is closed until `docs/forge.md`, the milestone summary, and the milestone audit are all current.

---

## 2. Competition facts to anchor against

As of 2026-06-03, this competition requires a compatible LoRA adapter for `NVIDIA-Nemotron-3-Nano-30B`, packaged as `submission.zip`, with rank at most 32. The Kaggle overview states that final evaluation loads the base model with the submitted adapter in vLLM, uses deterministic inference parameters, asks the model to put the final answer in a `\boxed{}` LaTeX command, and scores by answer accuracy.

The key constraints we must treat as hard gates:

| Constraint        | FORGE interpretation                                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Base model        | Nemotron-3-Nano-30B only. We do not submit a standalone model.                                                                 |
| Submission        | `submission.zip` containing a valid LoRA adapter and `adapter_config.json`.                                                    |
| LoRA rank         | Rank must be ≤32. We can train/merge experiments freely, but final package must obey this.                                     |
| Inference         | Deterministic at evaluation time; do not rely on sampling diversity at inference.                                              |
| Output format     | The model should reliably emit final answers in `\boxed{...}`.                                                                 |
| Score             | Accuracy against ground truth, including exact string or relative numerical tolerance.                                         |
| Prize eligibility | Public Kaggle notebook and solution write-up are required. Documentation is not optional.                                      |
| Timeline          | Entry/rules acceptance must be completed before the entry deadline; final submissions must be ready before the final deadline. |
| Daily submissions | Must be verified in the live Kaggle Submit UI and recorded in `docs/forge.md`.                                                 |

### Competition-facing posture

FORGE is a **final prize attempt**, not a midpoint artifact. Our strategy should optimize for private leaderboard generalization, final eligibility, and reproducible explanation of methods.

---

## 3. What FORGE is

FORGE is a competition-grade reasoning adapter laboratory. It should produce:

- validated synthetic reasoning data,
- deterministic solvers for puzzle families,
- metric-aligned training traces,
- LoRA adapters of rank ≤32,
- specialist adapters and legal merged/compressed adapters,
- exact local scoring and packaging validation,
- reproducible Kaggle submissions,
- a public notebook and write-up that make the final submission prize-eligible.

FORGE is intentionally narrow. It exists to win this Kaggle competition and to do so in a way that is auditable, reproducible, and explainable.

---

## 4. What FORGE is not

FORGE is not:

- a generic LLM training framework,
- a broad reasoning benchmark project,
- a model-serving platform,
- a general synthetic-data company stack,
- a place to chase open-ended RL research before the deterministic SFT baseline works,
- a notebook-only competition entry with no artifact discipline,
- a public leaderboard overfitting loop,
- a project that can close milestones without evidence.

If a proposed change does not improve validated score, valid packaging, reproducibility, documentation eligibility, or hard-category robustness, it should be deferred.

---

## 5. Winning thesis

The strongest available public signal suggests that winning approaches are not generic reasoning fine-tunes. They are **benchmark-shaped, solver-guided, data-centric LoRA systems**.

The public progress-prize repository is important because it exposes the shape of a strong solution: problem parsing, reasoners, synthetic/corpus generation, training dashboards, token-level inspection, per-category metrics, and a training execution flow. It also shows that successful work is organized as a pipeline, not a one-off notebook.

FORGE’s core thesis:

> The highest-probability final approach is to reproduce a strong public control adapter, build better verified data for the remaining hard/private-style categories, train specialists, and legally merge/compress them into a rank-32 adapter that preserves the solved categories while improving the unsolved ones.

This means we should prioritize:

1. **Exact metric alignment** over broad reasoning aesthetics.
2. **Correct synthetic traces** over high-volume unverified traces.
3. **Hard-category coverage** over retraining already-solved categories.
4. **Adapter merge/compression** over monolithic single-run training only.
5. **Prize documentation** from day one.

---

## 6. Strategic lanes

FORGE should run five lanes, but not all lanes have equal priority.

### Lane A — Public control reproduction

Purpose: establish a safe control adapter and prevent blind experimentation.

Deliverables:

- reproduce or wrap the best public progress-prize method sufficiently to produce a valid adapter,
- exact local metric/extraction harness,
- adapter packaging validator,
- one valid Kaggle control submission,
- public score and artifact hashes recorded in `docs/forge.md`.

This is mandatory. Without this, every improvement is unanchored.

### Lane B — Solver-guided synthetic data

Purpose: create higher-quality training data than the public baseline for hidden/private-like variants.

Target categories:

1. transformation / symbol-rule puzzles,
2. cryptarithm / arithmetic deduction,
3. bit manipulation edge cases,
4. equation numeric variants,
5. numeral systems,
6. unit conversion,
7. ciphers,
8. gravity or spatial toy worlds,
9. answer-format stress cases.

Rules:

- No trace enters training unless a deterministic solver or verifier confirms the answer.
- Every trace must include final `\boxed{answer}`.
- Every trace must record category, generator version, solver version, seed, and metric-extracted answer.
- Hard categories should get dedicated holdouts that never enter training.

### Lane C — Specialist adapters and legal merge/compression

Purpose: convert category-specific gains into one legal rank-32 final adapter.

Candidate adapter families:

- full public reproduction,
- transformation specialist,
- cryptarithm/equation specialist,
- bit manipulation specialist,
- formatting/answer-normalization specialist,
- balanced anti-forgetting adapter,
- merged/compressed adapter candidates.

Merge experiments:

- weighted adapter arithmetic,
- per-module weights,
- SVD compression to rank 32,
- control-preserving adapter soup,
- specialist insertion followed by regression checks.

No merged adapter advances unless it beats or preserves the control on solved/easy categories and improves at least one hard holdout.

### Lane D — Small exact-metric RL, only after SFT stability

Purpose: improve answer formatting and final-answer correctness, not to discover broad reasoning.

Rules:

- RL is optional.
- RL must use the exact answer extractor/verification logic.
- RL runs must be small, specialist-oriented, and regression-tested.
- Any RL candidate that damages the control categories is rejected or used only as a specialist merge ingredient.

### Lane E — Documentation and prize eligibility

Purpose: avoid ineligibility and improve contribution-award chances.

Deliverables:

- public Kaggle notebook,
- public write-up,
- reproducible training instructions,
- dataset provenance summary,
- solver/data method explanation,
- final adapter hash and package hash,
- open contribution form submissions if eligible.

Documentation is not a final-week afterthought. It is part of the build.

---

## 7. Operating principles

### 7.1 Determinism over intuition

Every score-affecting run should have a manifest. Every adapter should have a hash. Every dataset should have a provenance record. Re-running a config should produce comparable artifacts or explain why exact determinism is not possible.

### 7.2 Artifacts over memory

Do not rely on chat memory, notebook state, or local directories with ambiguous names. Every meaningful output belongs in a structured artifact directory with a manifest.

Recommended run layout:

```text
artifacts/runs/<run_id>/
  run_manifest.json
  config.yaml
  dataset_manifest.json
  local_eval.json
  local_eval_by_category.csv
  examples_failed.jsonl
  adapter_hash.txt
  package_hash.txt
  notes.md
```

Recommended submission layout:

```text
submissions/<submission_id_or_candidate>/
  submission.zip
  package_manifest.json
  adapter_config.json.snapshot
  hashes.txt
  kaggle_result.json
  notes.md
```

### 7.3 Verified data beats large data

A million weak traces are worse than ten thousand verified traces. The dataset must be solver-backed, answer-extracted, and category-tagged.

### 7.4 The metric is part of the model

The local metric is not a reporting utility. It is part of the training objective and data filter. Every trace should survive the same answer extraction behavior used in scoring.

### 7.5 Local validation protects against leaderboard noise

The public leaderboard is useful but dangerous. It may reward overfitting or luck. Candidate promotion should use:

- control comparison,
- public train holdout,
- synthetic hard holdout,
- formatting stress tests,
- public leaderboard score.

The public score can break ties, but it should not override repeated local regressions without investigation.

### 7.6 Preserve solved categories

A hard-category improvement that destroys easy-category accuracy is not a win. Anti-forgetting mixes and per-category eval gates are mandatory.

### 7.7 No silent failures

A failed package validator, failed solver verifier, failed CI run, or malformed answer extraction is a blocking failure. It cannot be waved through because the idea is promising.

### 7.8 Small milestones, large ambition

The project can go big technically, but milestones should stay small. Each milestone must prove one thing end to end.

---

## 8. Initial repository shape

Recommended scaffold:

```text
FORGE_ANCHOR.md
README.md
configs/
  train/
  data/
  merge/
  eval/
data/
  raw/
  external/
  generated/
  manifests/
docs/
  forge.md
  milestones/
    M00/
    M01/
notebooks/
  public_kaggle_solution.ipynb
scripts/
  make_dataset.py
  train_sft.py
  eval_adapter.py
  package_adapter.py
  validate_submission.py
  merge_adapters.py
  submit_notes.py
src/forge_nemotron/
  __init__.py
  metric/
  solvers/
  generators/
  data/
  training/
  adapters/
  packaging/
  eval/
  reports/
tests/
  unit/
  integration/
  e2e/
artifacts/
  runs/
submissions/
```

Recommended Python package boundaries:

| Package area  | Responsibility                                               |
| ------------- | ------------------------------------------------------------ |
| `metric/`     | exact extraction, normalization, verification, local scoring |
| `solvers/`    | deterministic puzzle solvers and proof/check functions       |
| `generators/` | synthetic prompt/trace generation                            |
| `data/`       | dataset manifests, filters, splits, deduplication            |
| `training/`   | SFT/QLoRA/GRPO wrappers and config loading                   |
| `adapters/`   | adapter inspection, merge, SVD compression                   |
| `packaging/`  | submission zip creation and validation                       |
| `eval/`       | local eval runners, category reports, error tables           |
| `reports/`    | notebook/write-up support tables and plots                   |

---

## 9. Run manifest contract

Every training, eval, merge, and submission candidate should have a manifest. Minimal fields:

```json
{
  "run_id": "M03_20260603_transform_v001",
  "created_at_utc": "2026-06-03T00:00:00Z",
  "git_commit": "<sha>",
  "branch": "forge/M03-transform-solver",
  "base_model": "NVIDIA-Nemotron-3-Nano-30B",
  "adapter_rank": 32,
  "training_config_hash": "<sha256>",
  "dataset_manifest_hash": "<sha256>",
  "solver_manifest_hash": "<sha256>",
  "local_metric_version": "<version>",
  "package_validator_version": "<version>",
  "local_score": null,
  "local_score_by_category": {},
  "kaggle_submission_id": null,
  "kaggle_public_score": null,
  "artifact_paths": [],
  "notes": ""
}
```

A run without a manifest is not eligible for final selection.

---

## 10. Testing and verification doctrine

### 10.1 Unit tests

Required unit coverage:

- answer extraction and boxed answer edge cases,
- numerical tolerance matching,
- solver correctness,
- generator determinism,
- dataset deduplication,
- category tagging,
- package validation,
- adapter config rank detection.

### 10.2 Property tests

Use Hypothesis-style property testing where practical:

- generated arithmetic puzzles round-trip through solver,
- bit operations match Python reference implementations,
- numeral-system conversions invert correctly,
- answer extractor does not crash on malformed reasoning text,
- package validator rejects missing files consistently.

### 10.3 Integration tests

Required integration tests:

- generate tiny synthetic dataset → verify → write manifest,
- train or mock-train tiny adapter path → package → validate,
- local metric scores known predictions correctly,
- adapter merge script preserves valid config and rank limit.

### 10.4 End-to-end smoke test

Every milestone after M01 should maintain a tiny E2E smoke path:

```text
fixture prompts
  → solver/generator
  → tiny train or mock train
  → local eval
  → package validation
  → artifact manifest
```

### 10.5 Submission package validator

Before any Kaggle upload, the validator must check:

- `submission.zip` exists,
- `adapter_config.json` exists,
- `adapter_model.safetensors` or equivalent expected adapter weights exist,
- LoRA rank ≤32,
- expected base model compatibility,
- no accidental extra large files,
- package hash recorded,
- unpack/repack stability checked.

---

## 11. Data doctrine

### 11.1 Data sources

Allowed sources:

- public competition artifacts allowed by rules,
- public notebooks/writeups/repos allowed by competition rules and licenses,
- self-generated synthetic data,
- teacher-generated traces only if competition rules permit them and provenance is recorded,
- deterministic solver outputs.

Every data source must be recorded in a data manifest.

### 11.2 Data rejection rules

Reject an example if:

- the solver cannot verify the answer,
- answer extraction does not recover the intended final answer,
- category is unknown and not intentionally tagged as unknown,
- prompt/answer duplicates an evaluation holdout,
- trace contains malformed `\boxed{}` output,
- provenance is missing,
- token length exceeds the chosen training/evaluation safety limit.

### 11.3 Holdout discipline

Maintain at least four holdouts:

1. public train holdout,
2. synthetic balanced holdout,
3. hard-category holdout,
4. formatting edge-case holdout.

No holdout should enter training. If a holdout is compromised, retire it and record the reason.

---

## 12. Adapter doctrine

### 12.1 Adapter families

Use named adapter families:

- `control_public_repro`,
- `balanced_sft`,
- `transform_specialist`,
- `bit_specialist`,
- `crypto_equation_specialist`,
- `formatting_specialist`,
- `merge_svd_rank32`,
- `merge_weighted_rank32`,
- `rl_format_small`.

### 12.2 Promotion gates

An adapter can advance only if:

- package validator passes,
- local score is recorded,
- per-category score is recorded,
- regression against control is understood,
- dataset/config hashes are recorded,
- no unresolved severe audit issue exists.

### 12.3 Final candidate logic

Final selection should include:

- one safest candidate,
- one highest-upside candidate,
- one fallback control candidate.

Final submissions should not be chosen solely by the latest public leaderboard score. The final private leaderboard may punish overfitting.

---

## 13. Submission budget doctrine

Cursor must inspect the live Kaggle Submit page and record the daily team submission limit in `docs/forge.md`.

If the limit is five per day, default usage should be:

| Slot | Use                                          |
| ---- | -------------------------------------------- |
| 1    | control or near-control regression check     |
| 2    | best locally validated improvement           |
| 3    | specialist/merge candidate                   |
| 4    | riskier high-upside candidate                |
| 5    | reserve for packaging fix or final candidate |

Final 72 hours:

- stop speculative submissions,
- prioritize reproducible candidates,
- keep a package-valid fallback,
- confirm notebook/write-up eligibility,
- do not consume final slots on unvalidated ideas.

---

## 14. Milestone sequence

### M00 — Anchor and competition intake

Goal: establish project truth and enter competition correctly.

Deliverables:

- commit `FORGE_ANCHOR.md`,
- create/update `docs/forge.md`,
- record competition rules, deadlines, rank limit, submission format, daily submission limit,
- create milestone folder and plan,
- verify rules accepted before entry deadline.

Exit criteria:

- `docs/forge.md` exists and is current,
- live Kaggle submission limit recorded,
- repo scaffold exists,
- M00 summary/audit complete.

### M01 — Public control reproduction

Goal: produce one valid adapter package and control score.

Deliverables:

- local metric helpers,
- package validator,
- public baseline reproduction or wrapper,
- first valid submission zip,
- Kaggle public score recorded.

Exit criteria:

- control candidate submitted or ready,
- validator passes,
- `docs/forge.md` updated.

### M02 — Exact local evaluation and artifact discipline

Goal: make every candidate comparable before spending submissions.

Deliverables:

- local eval CLI,
- per-category reporting,
- fixed holdouts,
- run manifest schema,
- artifact hashing.

Exit criteria:

- local eval can score any candidate,
- all runs create manifests,
- CI/smoke tests green.

### M03 — Solver and synthetic trace factory

Goal: create verified hard-category data.

Deliverables:

- initial solvers,
- generators,
- trace templates,
- metric filter,
- dataset manifests.

Exit criteria:

- at least one hard category has verified training data,
- dataset generation is deterministic for fixed seeds,
- bad examples are rejected automatically.

### M04 — Adapter sweep

Goal: train and evaluate multiple candidates.

Deliverables:

- SFT configs,
- balanced and specialist adapters,
- local scores,
- package-valid candidates,
- at least one improved Kaggle candidate if local results support it.

Exit criteria:

- control preserved,
- hard-category candidate identified,
- no untracked data/config.

### M05 — Merge and compression lab

Goal: combine specialist gains into legal rank-32 candidates.

Deliverables:

- merge scripts,
- SVD compression if useful,
- merged candidates,
- regression tables,
- top package-valid candidates.

Exit criteria:

- at least one merged candidate beats control locally or on public LB,
- final candidate shortlist exists.

### M06 — Final documentation and eligibility

Goal: lock prize eligibility.

Deliverables:

- public Kaggle notebook,
- public solution write-up,
- final method summary,
- data provenance summary,
- final candidate table,
- open contribution award submission if eligible.

Exit criteria:

- notebook and write-up are public,
- final package hashes recorded,
- final candidate selection rationale documented.

### M07 — Final submission lock

Goal: submit final candidates without chaos.

Deliverables:

- final safe candidate,
- final high-upside candidate,
- fallback control package,
- final `docs/forge.md` state,
- final milestone summary and audit.

Exit criteria:

- final submissions selected,
- all package hashes recorded,
- no unresolved prize-eligibility blocker,
- final audit complete.

---

## 15. Audit posture

FORGE should maintain a default 5/5 audit posture.

Audit dimensions:

| Dimension             | 5/5 expectation                                               |
| --------------------- | ------------------------------------------------------------- |
| Scope control         | Milestone did exactly what it said, no untracked scope creep. |
| Evidence              | Tests, hashes, manifests, scores, and CI evidence exist.      |
| Reproducibility       | A competent agent can rerun or inspect the result.            |
| Competition alignment | Work improves valid score, packaging, or eligibility.         |
| Risk handling         | Deferrals have rationale and exit criteria.                   |
| Documentation         | `docs/forge.md`, summary, and audit are current.              |

A milestone cannot receive 5/5 if:

- `docs/forge.md` is stale,
- package hashes are missing for submitted adapters,
- CI is red without an explicit deferral,
- submission scores are not recorded,
- serious risks are hidden,
- notebook/write-up eligibility is ignored near final.

---

## 16. CI and quality gates

Minimum recommended CI checks:

- Ruff lint/format,
- mypy where practical,
- pytest unit tests,
- solver property tests,
- local metric tests,
- package validator tests,
- artifact manifest tests,
- smoke E2E path,
- optional GPU tests marked and not required for standard CI.

GPU-heavy training should not be a required CI job. Instead, CI should validate the orchestration, configs, packaging, and small fixtures. Training evidence should be captured through run manifests and milestone artifacts.

---

## 17. Hardware posture

A 5090 Blackwell is available and should be used for fast iteration, local evaluation, QLoRA experiments where feasible, and high-throughput generation/verification. However, we must not assume one GPU removes all memory constraints for a 30B model.

Use the 5090 for:

- tiny end-to-end smoke training,
- LoRA/QLoRA experiments if memory permits,
- fast local inference/eval,
- solver-generated data verification,
- adapter packaging tests,
- partial sweeps.

Use external/Kaggle/G4/Tinker/Modal-style compute only when necessary for full training throughput or memory.

Record all compute environments in run manifests.

---

## 18. Risk register

| Risk                                | Impact                           | Mitigation                                            |
| ----------------------------------- | -------------------------------- | ----------------------------------------------------- |
| Invalid submission package          | Wastes submissions, blocks score | Package validator before every upload.                |
| Public leaderboard overfit          | Poor private score               | Maintain hard holdouts and anti-forgetting gates.     |
| Hard-category misidentification     | Training time wasted             | Error analysis after control submission.              |
| RL time sink                        | Late-stage instability           | RL is optional and only after SFT control is stable.  |
| Documentation ineligibility         | Prize loss despite score         | Public notebook/write-up in M06, not after final.     |
| Daily submission limit              | Reduced feedback                 | Verify live limit and use slots deliberately.         |
| Catastrophic forgetting             | Overall score drops              | Balanced replay mix and per-category gates.           |
| Data leakage / rule violation       | Disqualification risk            | Record provenance and follow Kaggle rules.            |
| Unreproducible notebook             | Prize eligibility risk           | Notebook must cite artifacts and hashes.              |
| Last-minute CI fixes after closeout | Needless CI churn                | Carry fixes to next milestone/branch unless blocking. |

---

## 19. Cursor operating rules

Cursor should operate as an implementation agent under these rules:

1. **Start every milestone from a plan.**  
   If the milestone folder does not exist, create it and copy the plan to `MNN_plan.md`.

2. **Ask clarifying questions only before implementation or when blocked.**  
   For urgent final-phase work, make the best safe assumption and record it.

3. **Keep milestones small.**  
   Do not bundle unrelated solver work, training sweeps, and documentation changes unless explicitly authorized.

4. **Update `docs/forge.md` with every material milestone.**  
   This is non-negotiable.

5. **Use artifact manifests.**  
   Every dataset, adapter, eval, merge, and submission candidate must be traceable.

6. **Do not close a milestone on red CI by default.**  
   If red CI is accepted, the audit must explicitly justify why and define next corrective action.

7. **Do not push after milestone closeout unless instructed.**  
   New work should go on the next branch to avoid needless CI runs.

8. **Use explicit closeout prompts.**  
   Each milestone should end with instructions to generate summary and audit, merge if appropriate, create next branch, and seed next milestone stub.

9. **Preserve prize eligibility.**  
   If any change affects the public notebook/write-up, record it.

10. **Prefer evidence over narration.**  
    Claims require tests, scores, hashes, or artifacts.

---

## 20. Branch and commit convention

Recommended branch names:

```text
forge/M00-anchor-intake
forge/M01-control-baseline
forge/M02-local-eval
forge/M03-solver-factory
forge/M04-adapter-sweep
forge/M05-merge-compress
forge/M06-docs-eligibility
forge/M07-final-lock
```

Recommended commit style:

```text
docs(forge): add anchor document and competition source of truth
feat(metric): add exact boxed-answer extraction harness
feat(packaging): add LoRA submission validator
test(solvers): add transformation solver property tests
chore(submission): record control candidate public score
```

---

## 21. Closeout prompt template for Cursor

Use this at the end of each milestone:

```markdown
Close out milestone MNN.

Tasks:
1. Update `docs/forge.md` with completed work, decisions, artifact hashes, CI status, Kaggle submissions/scores, risks, and next recommendation.
2. Create `docs/milestones/MNN/MNN_summary.md` using the project summary format.
3. Create `docs/milestones/MNN/MNN_audit.md` using the unified audit format and score the milestone out of 5.
4. Confirm all acceptance criteria from `MNN_plan.md` are satisfied or explicitly deferred with rationale and exit criteria.
5. Confirm CI status and include run IDs or local verification evidence.
6. If the branch is ready and CI is green, prepare merge instructions.
7. After merge, create the next milestone branch `forge/MNN+1-<slug>`.
8. Create `docs/milestones/MNN+1/MNN+1_plan.md` as a stub and create `MNN+1_toolcalls.md` if that is part of current repo convention.
9. Do not push additional changes to the closed milestone branch after closeout unless the user explicitly instructs it.
```

---

## 22. Initial suggestions for `docs/forge.md`

When creating or updating `docs/forge.md`, include these top-level sections:

1. **Competition Snapshot**  
   URL, dates, submission format, LoRA rank limit, metric, inference parameters, documentation requirements, daily submission limit.

2. **Current Strategy**  
   One paragraph summarizing the active thesis and current lane priorities.

3. **Milestone Ledger**  
   Table of M00–MNN with branch, status, CI, summary, audit score.

4. **Submission Ledger**  
   Submission ID, date, candidate name, adapter hash, zip hash, public score, notes.

5. **Run Ledger**  
   Run ID, config hash, dataset hash, adapter hash, local score, category scores.

6. **Dataset Ledger**  
   Dataset version, source, category counts, verification rate, holdout contamination checks.

7. **Adapter Candidate Board**  
   Control, specialists, merged candidates, final shortlist.

8. **Risk and Deferral Register**  
   Active risks with owner, target milestone, and exit criteria.

9. **Documentation Eligibility Tracker**  
   Notebook/write-up status, public links, final method hash, contribution award status.

10. **Final Decision Log**  
    Why the final candidates were selected.

---

## 23. Final compact truth

FORGE should win by being more disciplined than the leaderboard churn around it.

The project should build a complete system:

```text
competition rules
  → exact metric
  → public control reproduction
  → deterministic solvers
  → verified synthetic traces
  → specialist adapters
  → legal rank-32 merge/compression
  → package validation
  → deliberate submissions
  → public notebook/write-up
  → final candidate lock
```

The most important things to preserve:

- `docs/forge.md` as Ultimate Truth,
- valid LoRA package constraints,
- exact metric alignment,
- verified synthetic data,
- anti-forgetting category gates,
- artifact hashes and manifests,
- public documentation eligibility,
- small milestones with green CI by default.

The strongest guiding sentence:

> FORGE is a solver-guided, artifact-first, audit-governed LoRA competition system built to produce one legal rank-32 Nemotron adapter that generalizes better than public baselines and remains fully prize-eligible.

---

## 24. Source notes

Primary current competition sources:

- Kaggle competition overview: <https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge/overview>
- Kaggle competition page: <https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge>
- Public progress-prize repository: <https://github.com/tonghuikang/nemotron>

Internal project-pattern sources used for this anchor’s governance style:

- deterministic/artifact-first runtime patterns from DARIA,
- evidence-over-narration and clean-room discipline from Foundry,
- CI truthfulness and milestone governance from RediAI,
- no-silent-failure and content-addressable artifact posture from QuantLab,
- safe-consumer-surface and unknown/unsupported discipline from CLARITY,
- boundary/non-proof discipline from AURORA and ORNITHOS handoff practice.

These references are seed context only. FORGE’s active truth lives in `docs/forge.md`.
