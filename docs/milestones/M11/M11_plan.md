# M11_plan.md — Credential and Cost Closure Continuation

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M11 |
| **Title** | Credential and Cost Closure Continuation |
| **Branch** | `forge/M11-credential-cost-closure` |
| **Status** | **active** — implementation in progress |
| **Precondition** | M10 merged to `main`; post-merge CI green; owner authorized M11 kickoff |
| **Primary goal** | Convert credential, cost, external compute, Kaggle API, and Submit UI blockers from TBD/OPEN into evidence-backed statuses without recording secrets, training, inference, adapter artifacts, or Kaggle submissions |

---

## 1. Objective

M11 is a **readiness-decision milestone**.

M10 established local hardware visibility with CPU-only PyTorch (`visible_no_torch_cuda`). M11 closes owner-evidence gaps for Modal/Tinker/cloud credentials, cost acceptance, Kaggle API, and Submit UI constraints.

M11 is **not** a training milestone.

---

## 2. Authorization state (locked kickoff 2026-06-06)

| Gate | Value |
| ---- | ----- |
| M11 kickoff | **yes** |
| `M11_LOCAL_CUDA_SETUP_AUTHORIZED` | **no** |
| `M11_TRAINING_AUTHORIZED` | **no** |
| Kaggle submission | **not authorized** |

### Owner locked answers

| Item | Status |
| ---- | ------ |
| Modal account/credentials | **TBD** |
| Tinker account/credentials | **TBD** |
| Cloud GPU | **TBD** |
| Kaggle API | **TBD** |
| Cost acceptance | **TBD** |
| Submit UI constraints | **OPEN** |
| Local CUDA preference | **prefer_local_cuda** (preference only) |

---

## 3. Hard constraints

- No secrets committed or printed.
- No training, inference, adapters, `submission.zip`, or Kaggle submission.
- No CUDA PyTorch install or environment mutation unless Gate D explicitly authorized (it is **not**).
- No public baseline code/data vendoring.
- Cost acceptance not inferred from hardware ownership.

---

## 4. Deliverables

| # | Deliverable | Path |
| - | ----------- | ---- |
| 1 | Owner readiness intake | `owner_readiness_intake.md` |
| 2 | Modal/Tinker readiness update | `modal_tinker_readiness_update.md` |
| 3 | Cost acceptance update | `cost_acceptance_update.md` |
| 4 | Kaggle API / Submit UI update | `kaggle_submit_api_update.md` |
| 5 | Local CUDA path decision | `local_cuda_path_decision.md` |
| 6 | External compute decision matrix | `external_compute_decision_matrix.md` |
| 7 | Readiness manifest | `evidence/readiness/public_control_repro_plan.credential_cost_gate.json` |
| 8 | Validator/tests (if needed) | `reproduction_plan.py`, `test_reproduction_plan.py` |
| 9 | Next decision | `M11_next_decision.md` |
| 10 | Governance | `docs/forge.md`, `README.md` |

---

## 5. Implementation phases

### Phase A — Branch and plan setup

- Confirm clean `main`; create branch.
- Expand this plan; update `M11_toolcalls.md`, `docs/forge.md`, `README.md`.

### Phase B — Readiness docs

- Create deliverables 1–6.

### Phase C — Manifest and validation

- Create manifest; extend validator for `kaggle_api_status`, `submit_ui_constraints_status`.
- Run ruff, mypy, pytest, validate script.

### Phase D — Next decision and governance

- Create `M11_next_decision.md`; update `docs/forge.md`, `README.md`.

---

## 6. Acceptance criteria

- [ ] Branch `forge/M11-credential-cost-closure` from green `main`
- [ ] All M11 deliverables exist
- [ ] Manifest validates
- [ ] Validator tests pass
- [ ] Submit UI OPEN / Kaggle API TBD preserved (no guessing)
- [ ] No CUDA install, training, inference, submission, secrets
- [ ] CI green on PR
- [ ] Summary, audit, run evidence at closeout

---

## 7. Non-claims

M11 preserves: no Kaggle submission, no public/private score, no training, no inference, no CUDA PyTorch install, no reproduced baseline, no Kaggle-ready adapter, no copied baseline code/data, no committed credentials.
