# Compute Readiness Evidence — M08

**Milestone:** M08  
**Probe authorization:** `M08_LOCAL_5090_PROBE_AUTHORIZED = no`  
**Does not authorize training or inference**

---

## local_5090

| Field | Value |
| ----- | ----- |
| `local_5090_probe_status` | `blocked_owner_authorization_required` |
| `local_5090 available` | **yes** (per prior environment ledger — `docs/forge.md` §14) |
| CUDA / driver / VRAM details | **TBD** — probe script exists but was **not** run in M08 |
| Probe script | `scripts/probe_local_5090.py` (create-only; run when Gate B authorized) |

### Probe table (not populated — probe not run)

| Field | Value |
| ----- | ----- |
| probe_date_utc | — |
| machine | local_5090 |
| GPU name | TBD |
| VRAM total | TBD |
| driver version | TBD |
| CUDA runtime | TBD |
| torch version | TBD |
| torch CUDA available | TBD |
| disk free | TBD |
| notes | M08: script available; owner must authorize probe before recording hardware evidence |

---

## Modal / Tinker / cloud (compute path)

| Path | Training-ready? | Evidence |
| ---- | --------------- | -------- |
| local_5090 | **TBD** (CUDA/VRAM) | Ledger lists hardware; no M08 probe |
| Modal/Tinker | **TBD** | No owner account evidence in M08 |
| cloud GPU fallback | **TBD** | No owner evidence in M08 |

**Selected `compute_path` for training:** **none** (`null` in readiness manifest until owner selects path with evidence)

---

## Decision

| Verdict | Rationale |
| ------- | --------- |
| **not ready for training** | Gate C not authorized; local CUDA stack not evidenced; external paths TBD |

---

## Non-claims

- No `nvidia-smi` or torch CUDA probe was executed in M08.
- Listing RTX 5090 in the environment ledger is **not** CUDA/driver/VRAM verification.
- No model load, inference, or training was performed.
