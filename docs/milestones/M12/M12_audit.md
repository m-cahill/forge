# M12 Audit — Local CUDA PyTorch Environment Enablement

## 1. Header

| Field | Value |
| ----- | ----- |
| **Milestone** | M12 — Local CUDA PyTorch Environment Enablement |
| **Mode** | DELTA AUDIT |
| **Range** | M11 merge → M12 PR head `21c60e4` |
| **Branch** | `forge/M12-local-cuda-pytorch-enablement` |
| **PR** | [#13](https://github.com/m-cahill/forge/pull/13) |
| **current_sha** | `21c60e4` |
| **CI Status** | **Green** — [27043336258](https://github.com/m-cahill/forge/actions/runs/27043336258) (3.10, 3.11, 3.12) |
| **Audit Verdict** | **Pass** — CUDA environment evidenced; training gates preserved; no scope creep |

**Overall score: 4.6 / 5.0**

**Why not 5/5:** Main project env still CPU-only; no training feasibility run; external compute/credentials TBD; Submit UI OPEN; SQ-CORPUS-001 open; validate CLI not in CI; CUDA evidence is local-machine only.

**Why not lower:** All M12 deliverables complete; isolated env discipline; honest classification; manifest validates; 183 tests green; authorization boundaries respected; M13 recommendation evidence-based.

---

## 2. Executive Summary (Delta-Focused)

**Improvements**

- Isolated `.venv_cuda` path documented with live PyTorch selector command
- Reusable CUDA verification script with classification helpers (+9 tests)
- RTX 5090 + torch 2.11.0+cu128 evidenced as `cuda_ready_probe_only`
- Readiness manifest updates `compute_path: local_5090` with training still blocked
- Environment and Compute Ledger extended in `docs/forge.md`

**Risks**

- **GOV-007:** Submit UI OPEN — unchanged
- **GOV-012:** Modal/Tinker/cost TBD — external path still blocked
- **COMP-002:** Main env CPU-only — operators must use `.venv_cuda` explicitly
- **DATA-001:** SQ-CORPUS-001 open
- **COMP-003:** `cuda_ready_probe_only` could be misread as training-ready — mitigated by non-claims in evidence README/report

**Next action:** Merge PR #13 with owner permission; seed M13 feasibility dry run (not started).

---

## 3. Delta Map & Blast Radius

| Changed | Notes |
| ------- | ----- |
| `docs/milestones/M12/*` | Plan, setup plan, evidence, manifest, reports, summary, audit, run1 |
| `src/forge_nemotron/readiness/cuda_torch_verify.py` | New verification module |
| `scripts/verify_cuda_torch.py` | New CLI |
| `tests/unit/test_cuda_torch_verify.py` | +9 tests |
| `docs/forge.md`, `README.md`, `.gitignore`, `scripts/README.md` | Governance |

**Risk zones touched:** local compute classification. Not touched: training, inference, Kaggle submit, adapters, baseline vendoring, credentials.

---

## 4. M12 Acceptance Criteria

| Criterion | Status |
| --------- | ------ |
| Branch from green `main` | Met |
| Expanded `M12_plan.md`, `M12_toolcalls.md` | Met |
| `docs/forge.md` updated at closeout | Met |
| CUDA environment setup plan | Met |
| `verify_cuda_torch.py` | Met |
| `.venv_cuda` gitignored; not committed | Met |
| CUDA install evidenced | Met — success |
| Verification JSON + environment report | Met |
| Readiness manifest validates | Met |
| `M12_next_decision.md` | Met |
| Tests pass locally | Met — 183 |
| PR CI green | Met — 27043336258 |
| No training/inference/submission/adapters/credentials | Met |
| M13 stub seeded | Met (closeout) |

---

## 5. Guardrail Verification

| Guardrail | Verified |
| --------- | -------- |
| `M12_TRAINING_AUTHORIZED = no` | Yes — no training code executed |
| `M12_INFERENCE_AUTHORIZED = no` | Yes — no model load |
| `KAGGLE_SUBMISSION_AUTHORIZED = no` | Yes |
| Isolated environment | Yes — `.venv_cuda` gitignored |
| Evidence over success | N/A — install succeeded; failure path supported in script |
| Non-claims in docs | Yes |

---

## 6. Non-claims

`cuda_ready_probe_only` is not training readiness. No Kaggle submission, public/private score, training, inference, model loading, reproduced baseline, adapters, credentials, or committed environment files.
