# Compute Readiness Checklist — M06

**Milestone:** M06  
**Purpose:** Record compute posture before any training authorization  
**Does not authorize training**

---

## local_5090 readiness

| Check | Status | Evidence |
| ----- | ------ | -------- |
| Hardware available | **yes** (listed) | `docs/forge.md` Environment ledger |
| CUDA version | **TBD** | Owner probe not supplied in M06 |
| Driver version | **TBD** | Owner probe not supplied |
| VRAM | **TBD** | RTX 5090 assumed; not probed in M06 |
| torch CUDA | **TBD** | Not probed in M06 |
| Disk space | **TBD** | Not probed in M06 |
| Expected memory risk (30B SFT) | **high** | M05 compute matrix — full SFT may not fit locally |

**Notes:** M05 locked **local_5090** for preflight/dry-run only. No M06 probe script run (stretch goal deferred).

---

## Modal/Tinker readiness

| Check | Status | Evidence |
| ----- | ------ | -------- |
| Account | **TBD** | Owner |
| API key | **TBD** | Never commit |
| Cost acceptance | **TBD** | Owner |
| Baseline compatibility | **partial** | Public repo documents Modal/Tinker paths |
| Artifact capture plan | **planned** | Run manifests + `training_config_capture_template.md` |

---

## Kaggle readiness

| Check | Status | Evidence |
| ----- | ------ | -------- |
| Submit UI constraints | **OPEN** | Not recorded |
| GPU availability | **unknown** | M01 probe: CPU-only, no base model paths |
| Notebook evidence | **yes** (probe only) | `docs/kaggle/kaggle_setup_evidence.md` |

---

## Decision

| Verdict | Rationale |
| ------- | --------- |
| **not ready for training** | Gate C not authorized; credentials TBD; local CUDA stack not evidenced |

M06 does **not** claim compute readiness for baseline training.
