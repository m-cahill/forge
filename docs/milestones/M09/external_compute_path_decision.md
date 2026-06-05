# External Compute Path Decision — M09

**Milestone:** M09  
**Updates:** M05 [`compute_path_decision.md`](../M05/compute_path_decision.md) with M08/M09 evidence  
**Does not authorize training**

---

## Summary

| Path | Status | Evidence |
| ---- | ------ | -------- |
| **local_5090** | **TBD** (ready-for-probe only) | Hardware listed in environment ledger; CUDA/driver/VRAM **TBD** — probe not authorized in M09 |
| **Modal/Tinker** | **TBD** | [`modal_readiness_evidence.md`](modal_readiness_evidence.md), [`tinker_readiness_evidence.md`](tinker_readiness_evidence.md) |
| **cloud GPU fallback** | **TBD** | No owner evidence in M09 |
| **Kaggle notebook** | evidence/submission only; not primary training | M01 probe; see [`docs/kaggle/kaggle_setup_evidence.md`](../../kaggle/kaggle_setup_evidence.md) |

**Selected `compute_path` for training:** **none** (`null` in manifest until owner selects path with evidence)

---

## Recommendation

**All primary training paths remain blocked for Gate C.**

| Priority | Next unblock action |
| -------- | ------------------- |
| 1 | Owner supplies Modal/Tinker/cloud credential status (no secrets) + cost acceptance |
| 2 | Optional: authorize local 5090 probe (`M09_LOCAL_5090_PROBE_AUTHORIZED = yes`) for CUDA/VRAM evidence |
| 3 | Owner records Submit UI `submission.zip` constraints (submission path; parallel) |

M05 matrix recommendation unchanged: **Modal/Tinker** is the most baseline-compatible future training path **when** credentials and cost are evidenced; **local_5090** remains preflight/feasibility; **Kaggle notebook** is not primary training.

---

## Per-path M09 notes

### local_5090

- Probe script: `scripts/probe_local_5090.py`
- M09: [`local_5090_probe_blocked.md`](local_5090_probe_blocked.md) — probe **not** executed
- Does not unblock Modal/Tinker credential closure

### Modal/Tinker

- Public baseline documents Modal upload and Tinker notebook paths
- Account and credential status: **TBD**
- Cost: **TBD** (`cost_accepted: false`)

### cloud GPU fallback

- **TBD** — consider only if local and Modal/Tinker paths remain blocked after owner review

### Kaggle notebook

- CPU probe complete (M01); not assumed for 30B SFT
- Submit UI zip constraints: **OPEN**

---

## Explicit non-authorization

This decision **does not** authorize training, inference, Kaggle submission, or baseline reproduction claims.
