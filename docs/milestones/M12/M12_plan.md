# M12_plan.md — Local CUDA PyTorch Environment Enablement

## Milestone

**Milestone:** M12  
**Title:** Local CUDA PyTorch Environment Enablement  
**Branch:** `forge/M12-local-cuda-pytorch-enablement`  
**Status:** implemented on branch — Phases A–D complete; closeout pending  
**Precondition:** M11 merged to `main`, post-merge CI green, owner authorizes M12 kickoff with local CUDA setup permission.  
**Primary goal:** Create and verify an isolated local CUDA-enabled PyTorch environment for the RTX 5090 host, without training, inference, model loading, adapter creation, or Kaggle submission.

---

## 1. Objective

M12 converts the local 5090 from "hardware visible, PyTorch CPU-only" to an evidence-backed CUDA PyTorch readiness state, if possible.

M10 proved:

```text
GPU: NVIDIA GeForce RTX 5090
VRAM: 32607 MiB
Driver: 591.86
PyTorch: 2.2.2+cpu
torch.cuda.is_available(): false
Classification: visible_no_torch_cuda
```

M11 preserved the owner preference:

```text
prefer_local_cuda
```

M12 should answer:

1. Can we create an isolated local Python environment with CUDA-enabled PyTorch?
2. Does PyTorch detect the RTX 5090?
3. What PyTorch, CUDA runtime, driver, Python, and GPU details are recorded?
4. Is a tiny CUDA tensor smoke possible without loading models?
5. Can the local environment be classified as `cuda_ready_probe_only`?
6. What remains before a training feasibility dry run?
7. Should M13 be a local training feasibility dry run, package preflight, or another blocker closure milestone?

M12 is **environment enablement only**. It is not model training.

---

## 2. Authorization state

Owner authorization for M12:

```text
M12_LOCAL_CUDA_SETUP_AUTHORIZED = yes
M12_TRAINING_AUTHORIZED = no
M12_INFERENCE_AUTHORIZED = no
KAGGLE_SUBMISSION_AUTHORIZED = no
```

Allowed:

* Create an isolated local CUDA Python environment (`.venv_cuda`).
* Install CUDA-enabled PyTorch in that isolated environment.
* Run `nvidia-smi`.
* Run PyTorch CUDA availability checks.
* Run tiny tensor allocation / arithmetic smoke tests only.
* Record sanitized evidence.
* Update manifests and docs.

Not allowed:

* Training.
* Inference.
* Loading Nemotron or any model weights.
* Downloading or creating adapter files.
* Creating `submission.zip`.
* Kaggle upload/submission.
* Storing credentials.
* Copying public baseline code/data.

---

## 3. Current state

M00–M11 are merged to `main`.

Current blockers:

| Blocker                        | Status                            |
| ------------------------------ | --------------------------------- |
| CUDA-enabled PyTorch           | unavailable in active environment |
| local 5090 hardware            | visible                           |
| Modal/Tinker/cloud credentials | TBD                               |
| Cost acceptance                | TBD                               |
| Submit UI constraints          | OPEN                              |
| Kaggle API                     | TBD                               |
| SQ-CORPUS-001                  | open                              |
| Gate C training authorization  | not provided                      |

M12 focuses only on the CUDA-enabled PyTorch blocker.

---

## 4. Required source context

* `docs/forge.md`
* `docs/FORGE_ANCHOR.md`
* `docs/competition_rules.md`
* `docs/kaggle_submission_bible.md`
* `docs/kaggle/kaggle_setup_evidence.md`
* `docs/milestones/M10/M10_summary.md`
* `docs/milestones/M10/local_5090_probe_report.md`
* `docs/milestones/M10/M10_next_decision.md`
* `docs/milestones/M11/M11_summary.md`
* `docs/milestones/M11/M11_audit.md`
* `docs/milestones/M11/M11_next_decision.md`
* `docs/milestones/M11/local_cuda_path_decision.md`
* `scripts/probe_local_5090.py`
* `src/forge_nemotron/readiness/gpu_probe.py`
* `src/forge_nemotron/baselines/reproduction_plan.py`
* `scripts/validate_reproduction_plan.py`

Use the current official PyTorch install selector during implementation. Do not rely on stale remembered commands.

---

## 5. Hard constraints

### 5.1 Use an isolated environment

Do not mutate the main project environment destructively.

Preferred local environment name:

```text
.venv_cuda
```

The environment directory must not be committed.

Ensure `.gitignore` covers:

```text
.venv_cuda/
.venv-cuda/
cuda_env/
```

### 5.2 No training

Do not run any training loop, optimizer, SFT, QLoRA, LoRA, or fine-tuning step.

### 5.3 No inference

Do not load models or generate predictions.

### 5.4 No model or adapter files

Do not download, create, or commit model weights, adapter files, checkpoints, or `submission.zip`.

### 5.5 No credentials

Do not store, print, request, or commit secrets.

### 5.6 No Kaggle activity

Do not upload, submit, or edit Kaggle notebooks.

### 5.7 Evidence over success

If CUDA PyTorch installation fails, record the failure honestly and classify the environment accordingly.

---

## 6. Deliverables

### 6.1 CUDA environment setup plan

`docs/milestones/M12/cuda_environment_setup_plan.md`

### 6.2 Local CUDA environment evidence

`docs/milestones/M12/evidence/local_cuda_env/README.md`  
`docs/milestones/M12/evidence/local_cuda_env/cuda_torch_probe.json`

### 6.3 CUDA PyTorch verification script

`scripts/verify_cuda_torch.py`

### 6.4 Environment classification report

`docs/milestones/M12/local_cuda_environment_report.md`

### 6.5 Reproduction readiness manifest update

`docs/milestones/M12/evidence/readiness/public_control_repro_plan.local_cuda_env.json`

### 6.6 Validator updates if needed

`src/forge_nemotron/baselines/reproduction_plan.py`  
`tests/unit/test_reproduction_plan.py`

### 6.7 Documentation updates

`docs/forge.md`, `README.md`, `scripts/README.md`, `.gitignore`

### 6.8 M12 next decision document

`docs/milestones/M12/M12_next_decision.md`

---

## 7. Implementation phases

### Phase A — Branch and plan setup

* Confirm current `main`, clean working tree, M11 merged, CI green.
* Branch `forge/M12-local-cuda-pytorch-enablement`.
* Expand plan, toolcalls, forge.md, README, `.gitignore`.

### Phase B — Environment setup plan and verification script

* `cuda_environment_setup_plan.md`
* `scripts/verify_cuda_torch.py` + tests
* `scripts/README.md`

### Phase C — Isolated CUDA environment installation and probe

* Create `.venv_cuda`, install via official PyTorch selector.
* Run verification script with `--tiny-smoke`.
* Record evidence; do not commit `.venv_cuda`.

### Phase D — Readiness manifest and governance

* `public_control_repro_plan.local_cuda_env.json`
* Validator updates if needed
* `M12_next_decision.md`

---

## 8. Acceptance criteria

* [ ] Branch `forge/M12-local-cuda-pytorch-enablement` from green `main`
* [ ] Expanded `M12_plan.md`, `M12_toolcalls.md`
* [ ] `docs/forge.md` marks M12 active / updated at closeout
* [ ] CUDA environment setup plan exists
* [ ] `scripts/verify_cuda_torch.py` exists
* [ ] Isolated environment gitignored; not committed
* [ ] CUDA PyTorch install attempt evidenced
* [ ] Verification JSON and environment report exist
* [ ] Readiness manifest validates
* [ ] `M12_next_decision.md` exists
* [ ] Tests pass locally; CI green on PR
* [ ] No training, inference, submission, adapters, credentials, or model artifacts

---

## 9. Classification options

| Classification           | Meaning                                                                      |
| ------------------------ | ---------------------------------------------------------------------------- |
| `not_visible`            | GPU not visible via driver tools                                             |
| `visible_no_torch_cuda`  | GPU visible, PyTorch CUDA unavailable                                        |
| `cuda_ready_probe_only`  | PyTorch CUDA available; tiny smoke passes or basic CUDA visibility confirmed |
| `cuda_smoke_failed`      | PyTorch CUDA available but tiny smoke failed                                 |
| `blocked_install_failed` | CUDA PyTorch install failed                                                  |
| `unknown`                | insufficient evidence                                                        |

`cuda_ready_probe_only` is **not** training readiness.

---

## 10. Final non-claims

* no Kaggle submission, public/private score
* no model training or inference
* no reproduced public baseline
* no Kaggle-ready adapter or real adapter package
* no copied/vendored public baseline code/data
* no committed credentials
