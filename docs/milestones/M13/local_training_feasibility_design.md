# M13 — Local Training Feasibility Design

**Milestone:** M13  
**Status:** active  
**Branch:** `forge/M13-local-training-feasibility-dry-run`

---

## 1. Purpose and non-claims

M13 verifies that the isolated `.venv_cuda` environment can execute a **tiny toy CUDA training-like feasibility loop**: forward pass, loss, backward pass, and optimizer step on synthetic random tensors using a FORGE-owned toy MLP.

This is **not**:

- real model training,
- public baseline training,
- adapter / LoRA / QLoRA training,
- model inference,
- Nemotron or Hugging Face model loading,
- Kaggle submission readiness,
- full training readiness for the competition baseline.

Even a passing result (`cuda_training_feasibility_pass`) only supports planning a later **adapter feasibility** milestone.

---

## 2. Authorization state

```text
M13_LOCAL_TRAINING_FEASIBILITY_AUTHORIZED = yes
M13_FULL_BASELINE_TRAINING_AUTHORIZED = no
M13_INFERENCE_AUTHORIZED = no
KAGGLE_SUBMISSION_AUTHORIZED = no
```

---

## 3. Why this is not baseline training

| Aspect | M13 feasibility | Baseline / adapter training |
| ------ | --------------- | --------------------------- |
| Model | Tiny random-init MLP (~few thousand params) | Nemotron 30B + LoRA/QLoRA |
| Data | Random synthetic tensors | Competition / baseline corpus |
| Code | FORGE-owned script | Public baseline `train_sft.py` |
| Output | JSON telemetry only | Adapter weights, checkpoints |
| Authorization | Feasibility only | Gate C + readiness gates |

---

## 4. Toy workload description

- **Architecture:** 2-layer MLP — `Linear(64→128) → ReLU → Linear(128→32)`.
- **Input:** `torch.randn(32, 64)` synthetic batch.
- **Target:** `torch.randn(32, 32)` synthetic labels.
- **Loss:** MSE.
- **Optimizer:** SGD, lr=`1e-3`.
- **Precision:** fp32.
- **Steps:** 3 (default, configurable via `--steps`).
- **Seed:** 0 (default, configurable via `--seed`).
- **Device:** CUDA (`cuda:0`) in `.venv_cuda`.
- **Artifacts:** none — model state is not saved.

---

## 5. CUDA environment reference

From M12 evidence ([`cuda_torch_probe.json`](../M12/evidence/local_cuda_env/cuda_torch_probe.json)):

| Field | Value |
| ----- | ----- |
| Environment | `.venv_cuda` (gitignored) |
| Python | 3.11.9 |
| PyTorch | 2.11.0+cu128 |
| CUDA build | 12.8 |
| GPU | NVIDIA GeForce RTX 5090 |
| VRAM | 32607 MiB |
| Prior classification | `cuda_ready_probe_only` |

Main project venv remains CPU-only by design.

---

## 6. Metrics to collect

- Python and PyTorch versions, CUDA build, device name, VRAM total.
- CUDA memory allocated/reserved **before** loop.
- CUDA memory allocated/reserved **after** loop.
- **Peak** allocated/reserved during loop.
- Per-step loss and elapsed milliseconds.
- Success/failure, classification, exception traceback on failure.
- Command metadata and authorization flags.

---

## 7. Failure handling

| Outcome | Classification | Action |
| ------- | -------------- | ------ |
| Loop completes on CUDA | `cuda_training_feasibility_pass` | Record evidence; recommend M14 adapter feasibility dry run |
| CUDA visible but loop fails | `cuda_training_feasibility_failed` | Record traceback; recommend M14 CUDA troubleshooting |
| CUDA unavailable | `cuda_unavailable` | Do not claim pass; investigate environment |
| Not executed | `not_run` | No evidence claims |
| Authorization blocker | `blocked` | Stop; do not run |

Failures are recorded honestly in JSON and the human-readable report. No retry masking.

---

## 8. Next-decision criteria

| Result | Primary M14 recommendation |
| ------ | ---------------------------- |
| `cuda_training_feasibility_pass` | M14 — Local Adapter Feasibility Dry Run (still not full baseline training) |
| `cuda_training_feasibility_failed` | M14 — CUDA Troubleshooting |
| Blocked by Submit UI urgency | M14 — Submit UI Constraint Preflight |
| SQ-CORPUS-001 dominates | M14 — Corpus Segment Mapping Resolution |
| Gate C explicitly supplied | M14 — Controlled Public Baseline Training Attempt (only with full gates) |

See [`M13_next_decision.md`](M13_next_decision.md) after evidence is recorded.
