# M13_plan.md — Local Training Feasibility Dry Run

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M13 |
| **Title** | Local Training Feasibility Dry Run |
| **Branch** | `forge/M13-local-training-feasibility-dry-run` |
| **Status** | active |
| **Precondition** | M12 merged to `main`, post-merge CI green, owner authorizes M13 kickoff |
| **Primary goal** | Verify local RTX 5090 CUDA environment can run a tiny controlled training-like workload without OOM, CUDA instability, environment breakage, or governance drift |

---

## Authorization distinction (critical)

| Category | Status |
| -------- | ------ |
| **Tiny toy CUDA training-like feasibility loop** | **Authorized** — synthetic tensors, FORGE-owned toy MLP, forward/backward/optimizer only |
| **Real model training / baseline training / adapter training** | **Not authorized** — no Nemotron, no baseline `train_sft.py`, no LoRA/QLoRA/PEFT, no checkpoints |

---

## 1. Objective

M13 is the first controlled CUDA training-feasibility milestone.

M12 proved CUDA PyTorch works in the isolated `.venv_cuda` environment:

```text
Environment: .venv_cuda
Python: 3.11.9
PyTorch: 2.11.0+cu128
CUDA build: 12.8
torch.cuda.is_available(): true
GPU: NVIDIA GeForce RTX 5090
VRAM: 32607 MiB
Tiny CUDA tensor smoke: passed
Classification: cuda_ready_probe_only
```

M13 should now answer:

1. Can `.venv_cuda` run a tiny forward/backward/update loop on CUDA?
2. Can FORGE record CUDA memory before/during/after the dry run?
3. Can a tiny training-like run be manifested, hashed, and audited?
4. Can the dry run complete without model artifacts, adapters, Kaggle uploads, or baseline claims?
5. Is the local 5090 viable for a later controlled adapter feasibility milestone?

M13 is **not** full baseline training, model inference, adapter creation, or a Kaggle submission milestone.

---

## 2. Authorization state

```text
M13_LOCAL_TRAINING_FEASIBILITY_AUTHORIZED = yes
M13_FULL_BASELINE_TRAINING_AUTHORIZED = no
M13_INFERENCE_AUTHORIZED = no
KAGGLE_SUBMISSION_AUTHORIZED = no
```

**Allowed:** `.venv_cuda`, tiny synthetic toy loop, CUDA telemetry, small JSON/Markdown evidence, readiness manifest and doc updates.

**Not allowed:** Nemotron/HF models, baseline checkpoints, `train_sft.py`, LoRA/QLoRA/PEFT, full SFT, inference, adapter files, checkpoints, `submission.zip`, Kaggle upload, score claims, baseline code/data copy, credentials.

---

## 3. Current state

M00–M12 merged to `main`. CUDA probe-only in `.venv_cuda`; main env CPU-only. No training, inference, adapters, or submission.

| Blocker | Status |
| ------- | ------ |
| Gate C full training authorization | not provided |
| Submit UI `submission.zip` constraints | OPEN |
| Kaggle API | TBD |
| Modal/Tinker/cloud credentials | TBD |
| Cost acceptance | TBD |
| SQ-CORPUS-001 | open |
| Baseline adapter candidate | none |

---

## 4. Required source context

- `docs/forge.md`, `docs/FORGE_ANCHOR.md`, `docs/competition_rules.md`
- `docs/milestones/M12/*` (summary, audit, CUDA evidence)
- `src/forge_nemotron/baselines/reproduction_plan.py`
- `scripts/verify_cuda_torch.py`

---

## 5. Hard constraints

1. **No real model training** — toy feasibility loop only.
2. **No inference** — no text generation.
3. **No model loading** — no Nemotron, HF weights, adapters.
4. **No adapter/package files** — no `.safetensors`, `.bin`, `.pt`, checkpoints, `submission.zip`.
5. **No Kaggle activity.**
6. **No secrets committed.**
7. **Evidence over success** — record failures honestly.

---

## 6. Deliverables

| ID | Artifact | Path |
| -- | -------- | ---- |
| 6.1 | Feasibility design doc | `docs/milestones/M13/local_training_feasibility_design.md` |
| 6.2 | Feasibility script | `scripts/run_cuda_training_feasibility.py` |
| 6.3 | Evidence | `docs/milestones/M13/evidence/local_training_feasibility/` |
| 6.4 | Human report | `docs/milestones/M13/local_training_feasibility_report.md` |
| 6.5 | Readiness manifest | `docs/milestones/M13/evidence/readiness/public_control_repro_plan.local_training_feasibility.json` |
| 6.6 | Validator updates | `reproduction_plan.py`, tests if needed |
| 6.7 | Doc updates | `docs/forge.md`, `README.md`, `scripts/README.md` |
| 6.8 | Next decision | `docs/milestones/M13/M13_next_decision.md` |

**Classification options:** `cuda_training_feasibility_pass`, `cuda_training_feasibility_failed`, `cuda_unavailable`, `not_run`, `blocked`.

Even `cuda_training_feasibility_pass` is **not** full training readiness.

---

## 7. Implementation phases

### Phase A — Branch and plan setup

- Branch from green `main`; expand plan; update `docs/forge.md`, README.

### Phase B — Feasibility script and design doc

- Design doc, `scripts/run_cuda_training_feasibility.py`, unit tests, `scripts/README.md`.

### Phase C — Run local CUDA dry run

```powershell
.venv_cuda\Scripts\python scripts\run_cuda_training_feasibility.py `
  --out docs\milestones\M13\evidence\local_training_feasibility\feasibility_run.json `
  --steps 3 `
  --device cuda
```

### Phase D — Readiness manifest and governance

- Manifest, validator, next decision, ledger updates.

---

## 8. Acceptance criteria

- [ ] Branch from green `main`
- [ ] Plan expanded; toolcalls active
- [ ] Design doc and script exist
- [ ] Dry run executed in `.venv_cuda` (or failure recorded)
- [ ] Evidence JSON + README + report exist
- [ ] Readiness manifest validates
- [ ] M13 next decision exists
- [ ] Tests and linters pass; CI green on PR
- [ ] No training/inference/submission/model artifacts/credentials

---

## 9. Final non-claims

No Kaggle submission, public/private score, real model training, model inference, model loading, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, or committed credentials.
