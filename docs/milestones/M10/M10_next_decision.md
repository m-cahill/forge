# M10 Next Decision — M11 Recommendation

**Date:** 2026-06-05  
**Branch:** `forge/M10-local-5090-feasibility-probe`  
**Probe classification:** `visible_no_torch_cuda`  
**Evidence:** [`local_5090_probe_report.md`](local_5090_probe_report.md) · [`evidence/local_5090_probe/local_5090_probe.json`](evidence/local_5090_probe/local_5090_probe.json)

---

## M10 outcomes

| Area | M10 result |
| ---- | ---------- |
| `nvidia-smi` | **available** |
| GPU | **NVIDIA GeForce RTX 5090** |
| VRAM total | **32607 MiB** (~32 GB) |
| Driver | **591.86** |
| PyTorch | **2.2.2+cpu** installed |
| `torch.cuda.is_available()` | **false** |
| Probe classification | **`visible_no_torch_cuda`** |
| Training | **NO-GO** (`M10_TRAINING_AUTHORIZED = no`) |
| Submit UI constraints | **OPEN** |
| Modal/Tinker/cost | **TBD** |
| SQ-CORPUS-001 | **open** |
| Readiness manifest | `public_control_repro_plan_local_5090_probe_v1` validates |

**Supersedes:** M08/M09 `local_5090` CUDA/VRAM **TBD** in `docs/forge.md` for this host.

---

## Primary recommendation: M11 — Credential and Cost Closure Continuation

**Proposed title:** M11 — Credential and Cost Closure Continuation

**Rationale (probe-result-driven):** The RTX 5090 is visible with adequate VRAM and a current driver, but **PyTorch CUDA is not available** in the active environment (`2.2.2+cpu`). Per M10 decision logic, local path is not jointly GPU+CUDA-ready; external compute credential/cost closure remains the default primary track while Modal/Tinker status is TBD.

**M11 scope (draft — not started):**

1. Owner records Modal/Tinker/cloud GPU readiness and cost acceptance (status only, no secrets).
2. Update readiness manifest blockers when evidenced.
3. Still: no training without explicit Gate C authorization.

---

## Secondary M11 options

| Option | When to choose |
| ------ | -------------- |
| **M11 — Local CUDA Stack Fix + Training Feasibility Dry Run** | Owner prefers local path; authorize CUDA-enabled PyTorch install/verify, then tiny no-training or authorized feasibility smoke — **hardware already present** |
| **M11 — Submission Package Constraint Preflight** | Submit UI evidence becomes deadline-critical (final Jun 15) |
| **M11 — Corpus Segment Mapping Resolution** | Owner wants SQ-CORPUS-001 closed before training authorization |
| **M11 — Controlled Public Baseline Training Attempt** | Only if owner supplies Gate C + credentials + cost + compute path — **not recommended now** |

---

## Parallel owner-actions

1. Record Modal/Tinker/cost status (no secrets).
2. Record Submit UI `submission.zip` constraints when available.
3. If pursuing local path: install/verify CUDA-enabled PyTorch and re-run probe before training feasibility.
4. Provide Gate C only when ready for a controlled training attempt.

---

## Explicit non-actions

This decision doc does **not** authorize:

- M11 implementation without owner kickoff,
- model training, inference, or Kaggle submission,
- merge to `main`,
- claiming training readiness from visible GPU alone.
