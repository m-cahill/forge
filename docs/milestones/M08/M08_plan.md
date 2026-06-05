# M08_plan.md — Compute and Credential Readiness Closure

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M08 |
| **Title** | Compute and Credential Readiness Closure |
| **Branch** | `forge/M08-compute-credential-readiness` |
| **Status** | **closed on branch** — PR [#9](https://github.com/m-cahill/forge/pull/9); merge pending |
| **Precondition** | M07 merged to `main`; post-merge CI green; owner authorized M08 kickoff |
| **Primary goal** | Resolve or explicitly defer compute, credential, and Submit UI blockers that prevent Gate C training authorization |

---

## 1. Objective

M08 closes the readiness gap between “training authorization is blocked” and “training can be responsibly authorized.”

M07 established:

```text
M07_TRAINING_AUTHORIZED = no
training_authorized: false
ready_for_training: false
Training: NO-GO
Gate documentation: GO
```

M08 answers whether the project is ready for a future controlled public baseline training attempt by documenting:

1. local_5090 usability (probe script; run only when authorized),
2. Modal/Tinker credential status (owner evidence only),
3. cost acceptance,
4. Kaggle Submit UI `submission.zip` constraints,
5. Kaggle API submission support,
6. SQ-CORPUS-001 impact on training confidence,
7. whether reproduction plan can move toward `ready_for_training`.

M08 is a **readiness closure milestone**, not a training milestone.

---

## 2. Authorization model

| Gate | Phrase | M08 default |
| ---- | ------ | ----------- |
| A — Kickoff | Owner start | **authorized** |
| B — Local 5090 probe | `M08_LOCAL_5090_PROBE_AUTHORIZED = yes` | **no** — script only |
| C — Credential recording | Status only, never secrets | allowed |
| D — Training | `M08_TRAINING_AUTHORIZED = yes` | **no** |

---

## 3. Hard constraints

- No training, inference, Kaggle submission, adapter files, `submission.zip`, credentials in repo, or public baseline vendoring.
- Readiness must be evidence-backed or explicitly TBD/open.
- Do not run `probe_local_5090.py` without Gate B authorization.

---

## 4. Deliverables

| # | Artifact | Path |
| - | -------- | ---- |
| 7.1 | Compute readiness evidence | `docs/milestones/M08/compute_readiness_evidence.md` |
| 7.2 | Local 5090 probe script | `scripts/probe_local_5090.py` |
| 7.3 | Credential readiness evidence | `docs/milestones/M08/credential_readiness_evidence.md` |
| 7.4 | Cost acceptance gate | `docs/milestones/M08/cost_acceptance_gate.md` |
| 7.5 | Submit UI constraints evidence | `docs/milestones/M08/submit_ui_constraints_evidence.md` |
| 7.6 | SQ-CORPUS-001 resolution plan | `docs/milestones/M08/sq_corpus_001_resolution_plan.md` |
| 7.7 | Readiness matrix | `docs/milestones/M08/readiness_matrix.md` |
| 7.8 | Readiness manifest | `docs/milestones/M08/evidence/readiness/public_control_repro_plan.readiness.json` |
| 7.9 | Validator updates (if needed) | `reproduction_plan.py`, tests |
| 7.10 | Next decision | `docs/milestones/M08/M08_next_decision.md` |
| 7.11 | Governance | `docs/forge.md`, `README.md`, `scripts/README.md` |

---

## 5. Implementation phases

### Phase A — Branch and plan setup

- Confirm clean `main`, create branch, expand plan, toolcalls, `forge.md`, README.

### Phase B — Readiness docs

- Compute/credential/cost/submit/SQ-CORPUS/matrix evidence documents.

### Phase C — Probe script (no execution)

- `scripts/probe_local_5090.py` + CPU-safe tests; **do not run** without Gate B.

### Phase D — Readiness manifest and validation

- Manifest JSON + validator/tests; `validate_reproduction_plan.py` passes.

### Phase E — Next decision and governance

- `M08_next_decision.md`; update `forge.md` / README.

---

## 6. Acceptance criteria

- [x] Branch `forge/M08-compute-credential-readiness` from green `main`
- [x] All deliverables in §4 exist
- [x] Readiness manifest validates
- [x] Submit UI constraints OPEN or evidenced (not guessed) — **OPEN** preserved
- [x] No training/inference/submission/credentials/adapters
- [x] CI green on PR — [26988802789](https://github.com/m-cahill/forge/actions/runs/26988802789)
- [x] `M08_next_decision.md` recommends primary M09 path — Modal/Tinker setup gate

---

## 7. Locked owner inputs (M08 kickoff)

```text
Submit UI submission.zip constraints/warnings: OPEN
Kaggle API submission support: TBD
Modal / Tinker / Cloud GPU: TBD
Cost acceptance: TBD
credentials_ready: false
M08_LOCAL_5090_PROBE_AUTHORIZED = no
M08_TRAINING_AUTHORIZED = no
```

---

## 8. Non-claims

No Kaggle submission, public/private score, model training, inference, reproduced baseline, Kaggle-ready adapter, real adapter package, copied/vendored baseline code/data, or committed credentials unless separately authorized and evidenced.

---

*Authority: [`docs/milestones/M07/M07_next_decision.md`](../M07/M07_next_decision.md)*
