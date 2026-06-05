# External Compute Decision Matrix — M11

**Milestone:** M11  
**Owner preference:** `prefer_local_cuda`  
**Primary M12 recommendation:** Local CUDA PyTorch Environment Enablement (see [M11_next_decision.md](M11_next_decision.md))

---

## Matrix

| Path | Current evidence | Status | Next action |
| ---- | ---------------- | ------ | ----------- |
| local_5090 | RTX 5090 visible; ~32 GB VRAM; driver 591.86; PyTorch 2.2.2+cpu; `visible_no_torch_cuda` | **blocked for CUDA training** | M12 — Local CUDA PyTorch Environment Enablement (owner preference) |
| Modal/Tinker | No owner credential evidence; M09/M11 TBD | **TBD** | Owner status needed; cost acceptance TBD |
| Cloud GPU | No owner credential/cost evidence | **TBD** | Owner status needed |
| Kaggle notebook | CPU-only prior probe (M01) | **not primary training** | Submission/evidence path only |

---

## Aggregate readiness

| Field | Value |
| ----- | ----- |
| `credentials_ready` | **false** |
| `cost_accepted` | **false** |
| `compute_path` | **null** |
| `ready_for_training` | **false** |
| `training_authorized` | **false** |

---

## Rationale for primary M12 path

Local hardware is present and probed, but the active Python stack lacks CUDA-enabled PyTorch. Owner preference aligns with closing that gap before external paid compute. Modal/Tinker and cloud paths remain TBD until owner supplies status and cost acceptance.

---

## Non-claims

- No compute path is authorized for training in M11.
- Matrix does not claim external account functionality.
