# M11 Next Decision — M12 Recommendation

**Date:** 2026-06-06  
**Branch:** `forge/M11-credential-cost-closure`  
**Owner preference:** `prefer_local_cuda`  
**Evidence:** [owner_readiness_intake.md](owner_readiness_intake.md) · [external_compute_decision_matrix.md](external_compute_decision_matrix.md)

---

## M11 outcomes

| Area | M11 result |
| ---- | ---------- |
| Modal account/credentials | **TBD** |
| Tinker account/credentials | **TBD** |
| Cloud GPU | **TBD** |
| Cost acceptance | **TBD** |
| Kaggle API | **TBD** |
| Submit UI constraints | **OPEN** |
| Local 5090 probe status | **visible_no_torch_cuda** (M10; unchanged) |
| Gate D CUDA install | **not authorized** in M11 |
| Gate E training | **not authorized** in M11 |
| Readiness manifest | `public_control_repro_plan_credential_cost_gate_v1` validates |

---

## Primary recommendation: M12 — Local CUDA PyTorch Environment Enablement

**Proposed title:** M12 — Local CUDA PyTorch Environment Enablement

**Rationale:**

1. RTX 5090 is visible with ~32 GB VRAM and driver 591.86 (M10 probe).
2. Active PyTorch is `2.2.2+cpu`; `torch.cuda.is_available()` is **false**.
3. Owner preference is `prefer_local_cuda`.
4. Modal/Tinker/cost remain TBD — external path not ready.
5. Closing the local CUDA stack gap is the highest-leverage next step toward a actionable `local_5090` compute path.

**M12 scope (draft — not started):**

1. Owner authorizes Gate D: `M12_LOCAL_CUDA_SETUP_AUTHORIZED = yes`.
2. Install/verify CUDA-enabled PyTorch compatible with RTX 5090 / driver 591.86.
3. Re-run `probe_local_5090.py`; update probe classification if CUDA becomes available.
4. Update readiness manifest and compute ledger.
5. Still: no training without explicit Gate E authorization.

---

## Secondary M12 options

| Option | When to choose |
| ------ | -------------- |
| **M12 — Modal/Tinker Credential Setup Execution** | Owner supplies ready accounts + cost acceptance first |
| **M12 — Submit UI Constraint Preflight** | Submit UI evidence becomes deadline-critical (final Jun 15) |
| **M12 — Continue Credential/Cost Closure** | Owner still cannot supply Modal/Tinker/cost/API status |
| **M12 — Controlled Public Baseline Training Attempt** | Only if Gate E + all readiness gates satisfied — **not recommended now** |

---

## Parallel owner-actions

1. Record Modal/Tinker/cost status when available (no secrets).
2. Record Submit UI `submission.zip` constraints when authenticated evidence exists.
3. Provide Gate C / Gate E only when ready for controlled training.

---

## Explicit non-actions

This decision doc does **not** authorize:

- M12 implementation without owner kickoff,
- CUDA PyTorch install in M11,
- model training, inference, or Kaggle submission,
- merge to `main`,
- claiming training readiness from visible GPU alone.
