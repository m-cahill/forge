# M10_plan.md — Local 5090 Feasibility Probe

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M10 |
| **Title** | Local 5090 Feasibility Probe |
| **Branch** | `forge/M10-local-5090-feasibility-probe` |
| **Status** | **complete** — PR [#11](https://github.com/m-cahill/forge/pull/11) CI green; merge pending |
| **Precondition** | M09 merged to `main`; post-merge CI green; owner authorized M10 kickoff |
| **Primary goal** | Run a safe no-training local hardware/environment probe and record whether local compute is viable for future preflight, tiny feasibility, or controlled training milestones |

---

## 1. Objective

M10 closes the local hardware uncertainty that has remained open since M08.

The project currently has:

- a safe local probe script,
- `local_5090` listed as available,
- no actual CUDA/driver/VRAM evidence,
- no model training, inference, adapters, or Kaggle submissions.

M10 answers:

1. Is the RTX 5090 visible to the system?
2. Is `nvidia-smi` available?
3. What driver and CUDA versions are visible?
4. Is PyTorch installed?
5. Does PyTorch see CUDA?
6. What GPU name and VRAM are reported?
7. Is there sufficient disk/RAM information to plan future training?
8. What should M11 pursue?

M10 is a **hardware/environment feasibility probe**, not a training milestone.

**Supersedes:** M09-seeded stub “Credential and Cost Closure.” Prior M08/M09 compute docs remain historical; M10 probe evidence supersedes `local_5090` TBD fields in `docs/forge.md`.

---

## 2. Authorization state

| Field | Value |
| ----- | ----- |
| `M10_LOCAL_5090_PROBE_AUTHORIZED` | **yes** |
| `M10_TRAINING_AUTHORIZED` | **no** |
| `M10_INFERENCE_AUTHORIZED` | **no** |
| `KAGGLE_SUBMISSION_AUTHORIZED` | **no** |

**Allowed:** run `scripts/probe_local_5090.py`, `nvidia-smi` via probe, import torch if available, record facts, write sanitized JSON, update docs/manifests.

**Not allowed:** training, inference, Nemotron/30B load, adapters, `submission.zip`, Kaggle upload, credentials, baseline code/data copy.

---

## 3. Hard constraints

- No training, inference, model weights, adapter files, or Kaggle activity.
- Probe inspects environment/hardware only.
- Visible CUDA ≠ training readiness; classify at most `cuda_ready_probe_only` or `feasibility_candidate`.

---

## 4. Deliverables

### 4.1 Local 5090 probe evidence

```bash
python scripts/probe_local_5090.py --out docs/milestones/M10/evidence/local_5090_probe/local_5090_probe.json
```

Create `docs/milestones/M10/evidence/local_5090_probe/README.md` and sanitized `local_5090_probe.json`.

### 4.2 Human-readable report

`docs/milestones/M10/local_5090_probe_report.md` — authorization, command, hardware/CUDA/torch/disk summary, readiness classification, limitations, recommendation.

Readiness classifications: `not_visible`, `visible_no_torch_cuda`, `cuda_ready_probe_only`, `feasibility_candidate`, `blocked`.

### 4.3 Compute readiness ledger

Update `docs/forge.md` Environment and Compute Ledger with probe status, GPU, CUDA/driver, torch CUDA, VRAM, probe date, evidence path. Cross-reference M08/M09 docs; do not edit closed milestone files unless factual correction required.

### 4.4 Reproduction readiness manifest

`docs/milestones/M10/evidence/readiness/public_control_repro_plan.local_5090_probe.json` — extends prior state; `training_authorized: false`, `ready_for_training: false`.

### 4.5 Validator updates if needed

`src/forge_nemotron/baselines/reproduction_plan.py`, `tests/unit/test_reproduction_plan.py` — validate `local_5090_probe_status`, `compute_path = local_5090`.

### 4.6 M10 next decision

`docs/milestones/M10/M10_next_decision.md` — probe-result-driven M11 recommendation.

### 4.7 Rules evidence

`docs/competition_rules.md` committed; rule-derived facts referenced in `docs/forge.md`, `docs/kaggle/kaggle_setup_evidence.md`, `docs/kaggle_submission_bible.md`. Submit UI zip constraints remain **OPEN** unless owner supplies evidence.

---

## 5. Implementation phases

| Phase | Scope | Expected commit |
| ----- | ----- | ----------------- |
| **A** | Branch, plan, toolcalls, forge/README, competition rules | `docs(milestones): expand M10 local 5090 feasibility probe` |
| **B** | Run probe, evidence README, probe report | `docs(readiness): record local 5090 probe evidence` |
| **C** | Readiness manifest, validator/tests | `feat(baselines): add local 5090 readiness manifest` |
| **D** | Governance, M10_next_decision, forge closeout prep | `docs(governance): record M10 local compute decision` |

---

## 6. Acceptance criteria

- [x] Branch from green `main`
- [x] M10 plan expanded; toolcalls active
- [x] Probe run with owner authorization
- [x] Probe JSON + README + report exist
- [x] Readiness manifest validates
- [x] M10_next_decision exists
- [x] Tests/CI green on PR — [27027762042](https://github.com/m-cahill/forge/actions/runs/27027762042)
- [x] No training, inference, submission, adapters, credentials, baseline copy
- [x] No overclaiming training readiness
- [ ] Merge to `main` — **pending owner permission**

---

## 7. Final non-claims

No Kaggle submission, public/private score, model training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, copied baseline code/data, or committed credentials unless separately authorized and evidenced.
