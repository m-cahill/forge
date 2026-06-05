# M08 Next Decision — M09 Recommendation

**Date:** 2026-06-05  
**Branch:** `forge/M08-compute-credential-readiness`  
**M08 training authorization:** `M08_TRAINING_AUTHORIZED = no`  
**M08 local probe:** `M08_LOCAL_5090_PROBE_AUTHORIZED = no`

---

## M08 outcomes

| Area | M08 result |
| ---- | ---------- |
| Readiness docs + matrix | **complete** |
| Readiness manifest | `public_control_repro_plan_readiness.json` validates |
| Probe script | Created; **not executed** |
| Submit UI constraints | **OPEN** (no owner evidence) |
| Credentials / cost | **TBD** / `credentials_ready: false` |
| SQ-CORPUS-001 | **open** — interim: prefer `train.csv` first |
| Training | **NO-GO** |

---

## Primary recommendation: M09 — Modal/Tinker Setup Gate

**Proposed title:** M09 — Modal/Tinker Setup Gate (or credential + cost closure)

**Rationale:** M08 documented blockers without owner evidence. The highest-leverage path to Gate C is owner-supplied credential and cost status (no secrets in repo), plus optional authorized local_5090 probe. Submit UI constraints remain urgent for submission but do not unblock training documentation alone.

**M09 scope (draft — not started):**

1. Owner records Modal/Tinker/Kaggle API readiness (TBD → ready/blocked).
2. Owner records cost acceptance for paid paths.
3. Update readiness manifest fields when evidenced.
4. Optional: `M09_LOCAL_5090_PROBE_AUTHORIZED = yes` + probe artifact.
5. Still: no training without `M09_TRAINING_AUTHORIZED = yes` (or equivalent Gate C phrase).

---

## Secondary M09 options

| Option | When to choose |
| ------ | -------------- |
| **M09 — Controlled Public Baseline Training Attempt** | Owner supplies Gate C + `credentials_ready` + `cost_accepted` + compute path + schema/corpus policy |
| **M09 — Local 5090 Feasibility Probe** | Owner wants CUDA/VRAM evidence before credential spend |
| **M09 — Submit Package Constraint Preflight** | Submit UI evidence becomes deadline-critical |
| **M09 — Corpus Segment Mapping Resolution** | Owner wants SQ-CORPUS-001 closed before any training authorization |

---

## Parallel owner-actions

1. Record Submit UI `submission.zip` constraints when available.
2. State Modal/Tinker account readiness and cost acceptance (no secrets).
3. Optionally authorize local probe: `M08_LOCAL_5090_PROBE_AUTHORIZED = yes` (or M09 equivalent).
4. Provide Gate C when ready: training authorization phrase + compute path.

---

## Explicit non-actions

This decision doc does **not** authorize:

- M09 implementation without owner kickoff,
- model training, inference, or Kaggle submission,
- merge to `main`.
