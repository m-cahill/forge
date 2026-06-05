# M09 Next Decision — M10 Recommendation

**Date:** 2026-06-05  
**Branch:** `forge/M09-modal-tinker-setup-gate`  
**M09 training authorization:** `M09_TRAINING_AUTHORIZED = no`  
**M09 local probe:** `M09_LOCAL_5090_PROBE_AUTHORIZED = no`

---

## M09 outcomes

| Area | M09 result |
| ---- | ---------- |
| Modal account / credentials | **TBD** (no owner evidence) |
| Tinker account / credentials | **TBD** (no owner evidence) |
| Cloud GPU fallback | **TBD** |
| Cost acceptance | **TBD** / `cost_accepted: false` |
| Submit UI constraints | **OPEN** |
| Kaggle API submission | **TBD** |
| local_5090 probe | **not executed** |
| SQ-CORPUS-001 | **open** — prefer `train.csv` first |
| Readiness manifest | `public_control_repro_plan_modal_tinker_gate_v1` validates |
| Training | **NO-GO** |

---

## Primary recommendation: M10 — Continue Credential/Cost Closure

**Proposed title:** M10 — Continue Credential/Cost Closure

**Rationale:** M09 completed the setup gate documentation but received no owner status for Modal, Tinker, cloud GPU, or cost acceptance. The highest-leverage blocker for Gate C remains owner-supplied **status-only** evidence (never secrets). Until credentials and cost are recorded, `credentials_ready` and `cost_accepted` cannot advance and `compute_path` must remain `null`.

**M10 scope (draft — not started):**

1. Owner records Modal/Tinker/cloud GPU readiness (`ready` / `blocked` / TBD) with dates.
2. Owner records cost acceptance for paid paths with budget/limit notes.
3. Update readiness manifest blockers when evidenced.
4. Still: no training without explicit Gate C (`M10_TRAINING_AUTHORIZED = yes` or equivalent).

---

## Secondary M10 options

| Option | When to choose |
| ------ | -------------- |
| **M10 — Local 5090 Feasibility Probe** | Owner authorizes `M10_LOCAL_5090_PROBE_AUTHORIZED = yes` before spending on external compute |
| **M10 — Submission Package Constraint Preflight** | Submit UI evidence becomes deadline-critical (Jun 15 final) |
| **M10 — Corpus Segment Mapping Resolution** | Owner wants SQ-CORPUS-001 closed before any training authorization |
| **M10 — Controlled Public Baseline Training Attempt** | Only if owner supplies Gate C + credentials ready + cost accepted + compute path — **not recommended now** |

---

## Parallel owner-actions

1. Record Modal/Tinker/cloud GPU status (no secrets).
2. Record Modal/Tinker cost acceptance with budget ceiling.
3. Record Submit UI `submission.zip` constraints when available.
4. Optionally authorize local probe with exact phrase when CUDA/VRAM evidence is needed.
5. Provide Gate C training authorization only when ready for a controlled attempt.

---

## Explicit non-actions

This decision doc does **not** authorize:

- M10 implementation without owner kickoff,
- model training, inference, or Kaggle submission,
- local 5090 probe execution,
- merge to `main`.
