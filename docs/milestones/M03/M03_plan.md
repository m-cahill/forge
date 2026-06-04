# M03_plan.md — Solver and Synthetic Trace Factory

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M03 |
| **Title** | Solver and Synthetic Trace Factory |
| **Branch** | `forge/M03-solver-factory` |
| **Status** | **closed** (PR [#4](https://github.com/m-cahill/forge/pull/4) CI green; not merged) |
| **Precondition** | M02 merged to `main`; post-merge CI green; owner authorized M03 kickoff |
| **Primary goal** | First small, deterministic, solver-verified synthetic trace factory |

---

## 1. Objective

M03 builds a minimal verified synthetic trace pipeline:

```text
solver → generator → verifier → JSONL dataset → dataset manifest + hashes → local eval smoke → evidence
```

Success metric: every generated example is deterministic, verified, manifest-recorded, hashable, and locally evaluable — not dataset size.

**Non-claims:** no Kaggle submission, public/private score, model training, model inference, reproduced baseline, Kaggle-ready adapter.

---

## 2. Locked decisions (M03 kickoff)

| Topic | Decision |
| ----- | -------- |
| Property tests | Defer Hypothesis; use seeded loop/table tests only |
| Evidence | Commit full tiny dataset (~50 examples) under `docs/milestones/M03/evidence/synthetic_smoke/` |
| Boxing | `SolverResult.answer` unboxed; writer appends `Final answer: \boxed{...}` |
| String transforms | **Three only:** reverse, rotate L/R, simple substitution mapping |
| Arithmetic safety | No `eval`, `exec`, or `ast.literal_eval`; structured problem dicts only |
| Categories | `arithmetic_numeric`, `string_symbol_transform`, `formatting_stress` |
| Default smoke counts | 20 + 20 + 10 = **50** examples |

---

## 3. Current foundation (M02)

- Local eval: `forge_nemotron.eval`, `scripts/eval_predictions.py`
- Hashing: `forge_nemotron.artifacts.hashing`
- Run manifests: `forge_nemotron.reports.run_manifest`
- Boxed metric: `forge_nemotron.metric.boxed`
- `m02_fixture_holdout` — evaluation-only; do not train on fixture or M03 smoke

---

## 4. Hard constraints

1. No Kaggle submission  
2. No training or inference  
3. No public baseline reproduction claim  
4. Verified examples only (`verified=True` required)  
5. Holdout discipline — M03 smoke labeled; not production holdout activation  
6. Every written completion ends with final `\boxed{...}`  

---

## 5. Scope

### In scope

- `src/forge_nemotron/solvers/` — base, arithmetic, string_transform  
- `src/forge_nemotron/generators/` — arithmetic, string_transform, formatting_stress  
- `src/forge_nemotron/data/` — synthetic writer, dataset manifest  
- `scripts/make_dataset.py`  
- Unit tests (determinism, rejection paths, solver correctness)  
- Local eval self-check → **synthetic factory self-check accuracy** (expect 100%)  
- Committed evidence + governance updates  

### Out of scope

- Large-scale generation, training, Kaggle upload, baseline reproduction  
- Hypothesis dependency  
- Extra string transforms (case, multi-cipher) unless stretch after green CI  

---

## 6. Deliverables

| ID | Deliverable | Path |
| -- | ----------- | ---- |
| 7.1 | Solver interfaces | `solvers/base.py` |
| 7.2 | Arithmetic solver/generator | `solvers/arithmetic.py`, `generators/arithmetic.py` |
| 7.3 | String transform (3 types) | `solvers/string_transform.py`, `generators/string_transform.py` |
| 7.4 | Formatting stress generator | `generators/formatting_stress.py` |
| 7.5 | Synthetic writer | `data/synthetic.py` |
| 7.6 | Dataset manifest | `data/manifest.py` |
| 7.7 | CLI | `scripts/make_dataset.py` |
| 7.8 | Eval integration | eval JSONL from generated examples |
| 7.9 | Evidence | `docs/milestones/M03/evidence/synthetic_smoke/` |
| 7.10 | Tests | `tests/unit/test_solver_*.py`, etc. |

---

## 7. Implementation phases

| Phase | Focus | Expected commit |
| ----- | ----- | ----------------- |
| A | Branch, plan, forge.md, README | `docs(milestones): expand M03 solver factory plan` |
| B | Solver/generator foundations | `feat(solvers): add solver and generator foundations` |
| C | Arithmetic + string families | `feat(solvers): add verified arithmetic and string transforms` |
| D | Formatting stress + synthetic writer | `feat(data): add verified synthetic trace writer` |
| E | Manifest + `make_dataset.py` | `feat(data): add synthetic dataset manifest and CLI` |
| F | Evidence + eval smoke | `docs(data): record M03 synthetic smoke evidence` |

---

## 8. Acceptance criteria

- [x] Branch `forge/M03-solver-factory` from green `main`
- [x] Solver base protocol; arithmetic + string (3 transforms) + formatting stress
- [x] Writer rejects unverified, missing boxed, duplicate IDs
- [x] Dataset manifest with SHA256 and category counts
- [x] `make_dataset.py` deterministic for fixed seed
- [x] Local eval smoke 100% synthetic factory self-check
- [x] Evidence committed with non-claim README
- [x] Dataset Ledger + Run Ledger updated in `docs/forge.md`
- [x] Tests + CI green; no training/submission/score claims

---

## 9. Closeout

Use closeout prompt in anchor/plan when implementation complete. Do not merge without express permission.
