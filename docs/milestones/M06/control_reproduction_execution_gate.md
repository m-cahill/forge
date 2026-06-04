# Control Reproduction Execution Gate

**Milestone:** M06  
**Branch:** `forge/M06-control-repro-execution-gate`  
**Status:** Active implementation  
**Baseline:** https://github.com/tonghuikang/nemotron @ `82bd1880aa8a8986ad572ccd17ae35b2b5c7da85`

---

## 1. Purpose and non-claims

M06 is an **execution gate** between M05 planning and any future training attempt. It records whether external schema inspection, compute/credential readiness, and manifest gates support a controlled reproduction path.

**M06 does NOT claim:**

- Baseline reproduced or score parity
- Model training or inference
- Kaggle submission or public/private score
- Kaggle-ready adapter or real adapter package
- License clearance to copy baseline code into FORGE

**M06 MAY claim:**

- Schema inspection completed with derived notes (Gate B)
- Reproduction plan manifest at schema-gate state
- Compute/credential checklists recorded (evidence or TBD)
- Go/no-go recommendation for M07

---

## 2. Gate A / B / C model

| Gate | Phrase | M06 status |
| ---- | ------ | ---------- |
| **A — Kickoff** | Owner authorized M06 implementation | **Authorized** |
| **B — Schema inspection** | `M06_SCHEMA_INSPECTION_AUTHORIZED = yes` | **Authorized** — derived notes committed |
| **C — Training** | `M06_TRAINING_AUTHORIZED = yes` | **NOT authorized** |

**Critical:** M06 kickoff and Gate B do **not** imply Gate C. Training requires separate owner authorization and manifest fields (`training_authorized: true`, `owner_training_authorization`, `credentials_ready`, compute path).

---

## 3. Current readiness

| Area | Status | Evidence |
| ---- | ------ | -------- |
| M05 merged / CI | Green on `main` | `34169d0`, post-merge [26983281413](https://github.com/m-cahill/forge/actions/runs/26983281413) |
| Reproduction plan contract | Extended for schema gate | `reproduction_plan.py` |
| Schema inspection | **Complete** | `external_schema_notes_*.md` |
| Mapping supplement | **Complete** | `baseline_schema_mapping_supplement.md` |
| Schema-gate manifest | **Validates** | `public_control_repro_plan.schema_gate.json` |
| Real control candidate | **None** | Adapter board unchanged |

---

## 4. External schema inspection status

- **Status:** `complete`
- **Method:** Read-only clone at `C:\coding\nemotron-inspect` (outside FORGE tree)
- **Files inspected:** `corpus.jsonl`, `problems.jsonl`, `generation.jsonl`, `train.csv`
- **Committed:** Derived notes only (field names, types, counts, hashes)
- **Not committed:** Raw JSONL/CSV rows, tokenizer, code, checkpoints

---

## 5. Compute readiness status

See [`compute_readiness_checklist.md`](compute_readiness_checklist.md).

**Summary:** `local_5090` listed as available; CUDA/driver/VRAM probe **TBD**. Modal/Tinker **TBD**. Kaggle notebook CPU-only at M01 probe. **No compute path authorized for training in M06.**

---

## 6. Credential readiness status

See [`credential_readiness_checklist.md`](credential_readiness_checklist.md).

**Summary:** All credential rows **TBD**; no secrets in repo.

---

## 7. Training authorization status

| Field | Value |
| ----- | ----- |
| `M06_TRAINING_AUTHORIZED` | **no** |
| `training_authorized` (manifest) | `false` |
| `owner_training_authorization` | absent |
| `status` | `preflight` (not `ready_for_training`) |

---

## 8. Submit UI constraints status

| Item | Status |
| ---- | ------ |
| Submit UI `submission.zip` constraints/warnings | **OPEN** — owner-action / not recorded |
| Kaggle API submission support | **TBD** |

Does not block M06 schema inspection.

---

## 9. Go/no-go recommendation for M07

**Recommend:** M07 — **Controlled Public Baseline Training Authorization Gate**

**Rationale:** Schema inspection complete; core fields map to FORGE eval types with known partials (`corpus.segment`, boxed format in samples). Training remains blocked until owner supplies Gate C, credentials, compute path, and training config capture.

See [`M06_next_decision.md`](M06_next_decision.md).
