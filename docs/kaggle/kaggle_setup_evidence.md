# Kaggle Setup Evidence — FORGE

**Authority:** Subordinate to [`docs/forge.md`](../forge.md).  
**Last updated:** 2026-06-04 (M04: Submit UI zip constraints remain OPEN)

Record every Kaggle verification attempt. Do not claim scores, submission success, or package validity without a row here (or linked milestone evidence).

## Competition intake (M00+)

| Field | Value | Source | Recorded At | Verified By |
| ----- | ----- | ------ | ----------- | ----------- |
| Competition URL | <https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge> | Public | 2026-06-03 | Cursor |
| Entry / team merger deadline | **June 8, 2026** | Owner — live Kaggle competition page (logged in) | 2026-06-04 | Owner |
| Final submission deadline | **June 15, 2026, 11:59 PM UTC** | Owner — live Kaggle competition page (logged in) | 2026-06-04 | Owner |
| Daily submission limit | **5 per day** (`0 / 5 used` at probe) | Authenticated Submit UI + M01 debug probe | 2026-06-04 | Owner |
| Rules accepted / team joined | **Yes** | Authenticated competition page / Rules or Submit UI | 2026-06-04 | Owner |
| Submit UI accessible | **Yes** | Authenticated Submit UI | 2026-06-04 | Owner |
| Team name | not recorded | Submit UI / team page | 2026-06-04 | Owner |
| Additional Submit UI notes | **OPEN — not recorded** | Submit UI (warnings, zip constraints) | — | Owner-action (M04 preserved) |
| Base model | NVIDIA-Nemotron-3-Nano-30B | Overview | 2026-06-03 | Cursor |
| Submission artifact | `submission.zip` (LoRA + `adapter_config.json`) | Overview | 2026-06-03 | Cursor |
| LoRA rank limit | ≤ 32 | Overview | 2026-06-03 | Cursor |
| Kaggle API submission supported | **TBD** | Submit UI / docs | — | Pending |

### Rules / team verification (2026-06-04)

| Field | Value |
| ----- | ----- |
| Rules accepted / team joined | **Yes** |
| Verified via | Authenticated Kaggle competition page / Rules or Submit UI |
| Submit UI accessible | **Yes** |
| Team name | not recorded |
| Additional notes | not recorded |

**Non-claims:** This confirms competition eligibility intake only. It does **not** prove submission readiness, package validity, a scored submission, or a public score.

### Deadline reconfirmation (owner 2026-06-04)

| Field | Value |
| ----- | ----- |
| Entry / team merger deadline | **June 8, 2026** |
| Final submission deadline | **June 15, 2026, 11:59 PM UTC** |
| Verified from | Live Kaggle competition page while logged in |
| Verified at | 2026-06-04 |
| Verified by | Owner |
| Prior public-page record | 2026-06-03 (Cursor) — dates unchanged after owner reconfirm |

## Notebook / debug attempts

**M01 debug probe scope:** `forge_m01_kaggle_debug_probe.ipynb` is an **environment probe only**. It is **not** expected to write `/kaggle/working/submission.zip`. Missing `submission.zip` after a successful probe run is **not** a failure — submission artifacts belong to a future submission notebook (not created unless explicitly authorized).

| Date UTC | Notebook | Git commit | Mode | Accelerator | Internet | Inputs observed | Outputs / hashes | Submission attempted | Submission ID | Score | Notes |
| -------- | -------- | ---------- | ---- | ----------- | -------- | --------------- | ---------------- | -------------------- | ------------- | ----- | ----- |
| 2026-06-04 | `forge_m01_kaggle_debug_probe.ipynb` | main post-M01 merge | Interactive | **None** (CPU only) | TBD | `/kaggle/input/competitions`; base model paths **not** attached | `probe_test.txt` 83 B; SHA256 `a8f624087fe0520a0c0c97f914e54f4e7b6478f750b85d5f9d8e971c6e360a8c`; **no** `submission.zip` (expected) | **no** | — | — | Env probe only — **not** expected to create `submission.zip`. Py 3.12.13; Linux 6.6.122+; CWD `/kaggle/working`; ~19.5 GB free; torch 2.10.0+cpu; CUDA false; nvidia-smi N/A. **No** scored submission, **no** public score, **no** package validity, **no** inference, **no** submission readiness. |

### M01 probe detail (2026-06-04)

| Observation | Value |
| ----------- | ----- |
| Run mode | Interactive |
| Is Kaggle | true |
| Daily submissions | `0 / 5 used` → limit **5/day** |
| Python | 3.12.13 |
| Platform | Linux-6.6.122+-x86_64-with-glibc2.35 |
| CWD | `/kaggle/working` |
| `/kaggle/input` | contains `competitions` |
| `/kaggle/working` free | ~19.5 GB |
| GPU | none; `nvidia-smi` not found |
| PyTorch | 2.10.0+cpu |
| CUDA available | false |
| Paths checked (not visible) | `/kaggle/input/nemotron-3-nano-30b-a3b-bf16`, `/kaggle/input/nvidia-nemotron-3-nano-30b-a3b-bf16` |
| Debug file | `/kaggle/working/tmp/forge_debug/probe_test.txt` |
| `submission.zip` at `/kaggle/working/` | **Not created** — expected for probe; not a failure |

## Owner-action checklist

- [x] Reconfirm entry / team merger deadline (**June 8, 2026**) on live Kaggle — owner 2026-06-04
- [x] Reconfirm final submission deadline (**June 15, 2026, 11:59 PM UTC**) on live Kaggle — owner 2026-06-04
- [x] Record daily submission limit from Submit UI — **5 per day** (2026-06-04)
- [x] Record rules accepted / team status — **yes**; Submit UI accessible (2026-06-04)
- [ ] Note any extra `submission.zip` constraints from UI
