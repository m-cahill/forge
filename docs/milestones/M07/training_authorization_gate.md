# Training Authorization Gate

**Milestone:** M07  
**Branch:** `forge/M07-training-authorization-gate`  
**Date:** 2026-06-05  
**Path:** A — authorization gate only (blocked)

---

## 1. Purpose and non-claims

This document records whether FORGE is authorized to begin a controlled public baseline training attempt.

**M07 does not claim:**

- model training occurred,
- model inference occurred,
- baseline reproduction,
- Kaggle submission or public/private score,
- Kaggle-ready adapter or real adapter package,
- copied/vendored public baseline code or data.

M07 may claim only that training authorization was evaluated and recorded in manifests/docs.

---

## 2. Required authorization fields (Gate C)

Training requires owner-supplied authorization equivalent to:

```text
M07_TRAINING_AUTHORIZED = yes
owner_training_authorization: <human-readable authorization string>
compute_path: <local_5090 | modal_tinker | cloud_gpu | other>
credentials_ready: <true/false>
cost_accepted: <true/false>
training_scope: <dry_run | controlled_public_baseline_attempt>
```

Reproduction plan manifest must reflect `training_authorized: true`, `owner_training_authorization`, `compute_path`, `schema_inspection_status: complete` (or waiver), and `credentials_ready: true` (or waiver) for `status: ready_for_training`.

---

## 3. Current authorization status

| Field | Value |
| ----- | ----- |
| M07 kickoff | **authorized** (implementation of training gate) |
| `M07_TRAINING_AUTHORIZED` | **no** |
| `training_authorized` (manifest) | **false** |
| `owner_training_authorization` | **not provided** |
| `cost_accepted` | **TBD** |
| `training_scope` | **not assigned** |

**Result:** Training is **blocked** for M07.

---

## 4. Current compute status

| Item | Status |
| ---- | ------ |
| `local_5090` | **available** (per environment ledger) |
| CUDA / driver / VRAM | **TBD** — not evidenced in M07 |
| `compute_path` (training) | **not selected** for authorized training |
| Modal | **TBD** |
| Tinker | **TBD** |
| Cloud GPU fallback | **TBD** |
| Cost acceptance | **TBD** |

M05 recommendation preserved: local_5090 for preflight; Modal/Tinker (or equivalent) for baseline-compatible full training **after** Gate C.

---

## 5. Current credential status

| Item | Status |
| ---- | ------ |
| `credentials_ready` | **false** / TBD |
| Modal account | **TBD** |
| Tinker account | **TBD** |
| Kaggle API (submission) | **TBD** |
| Secrets in repo | **none** — policy enforced |

Do not request or record secrets in FORGE docs.

---

## 6. Current schema mapping status

| Area | Status | Reference |
| ---- | ------ | --------- |
| Schema inspection (Gate B) | **complete** | M06 derived notes + schema-gate manifest |
| `corpus.jsonl` | understood (derived notes) | M06 |
| `problems.jsonl` | understood | M06 |
| `generation.jsonl` | understood | M06 |
| `train.csv` | understood | M06 |
| `corpus.segment` mapping | **partial** | SQ-CORPUS-001 — open |
| `\boxed{}` in baseline samples | **not observed** in inspected rows | M06 — unknown for full corpus |

Schema completeness supports **documentation** of readiness; it does **not** substitute for Gate C training authorization.

---

## 7. Current Submit UI constraints status

```text
Submit UI submission.zip constraints/warnings: OPEN — owner-action / not recorded
Kaggle API submission support: TBD
```

Does **not** block M07 training-authorization documentation. **Does** block confident Kaggle submission planning.

See [`submit_ui_constraint_gate.md`](submit_ui_constraint_gate.md).

---

## 8. Go / no-go result

| Gate | Result |
| ---- | ------ |
| Training authorization (Gate C) | **NO-GO** — `M07_TRAINING_AUTHORIZED = no` |
| Ready-for-training manifest | **NO** — blocked manifest path |
| Controlled baseline training attempt | **NO-GO** in M07 |
| M07 gate documentation | **GO** — proceed with blocked record |

---

## 9. Next required action

1. **Owner:** Provide Gate C authorization fields when ready to authorize training (separate from M07 kickoff).
2. **Owner:** Record Submit UI `submission.zip` constraints when available.
3. **Owner:** Confirm compute path, credentials, cost acceptance, and local_5090 CUDA/VRAM when available.
4. **Cursor:** Follow `M07_next_decision.md` for recommended M08 path after M07 closeout.

---

## Evidence

- Training-gate manifest: [`evidence/training_gate/public_control_repro_plan.training_blocked.json`](evidence/training_gate/public_control_repro_plan.training_blocked.json)
- Schema readiness: [`baseline_schema_readiness_decision.md`](baseline_schema_readiness_decision.md)
