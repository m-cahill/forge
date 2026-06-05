# M09_plan.md — Modal/Tinker Setup Gate

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M09 |
| **Title** | Modal/Tinker Setup Gate |
| **Branch** | `forge/M09-modal-tinker-setup-gate` |
| **Status** | **merged** to `main` (`5a4300b`) via PR [#10](https://github.com/m-cahill/forge/pull/10) |
| **Precondition** | M08 merged to `main`; post-merge CI green; owner authorized M09 kickoff |
| **Primary goal** | Determine whether Modal/Tinker (or approved equivalent) is ready for a future controlled public baseline training attempt without storing secrets, training, inference, adapter files, or Kaggle submissions |

---

## 1. Objective

M09 closes the external training-path readiness gap.

M08 documented that:

- Modal/Tinker credentials are **TBD**
- Cost acceptance is **TBD**
- local_5090 CUDA/VRAM remains **TBD** (probe not run)
- Submit UI constraints remain **OPEN**
- Gate C training authorization is **not provided**
- Training remains **NO-GO**

M09 answers:

1. Is Modal account readiness known?
2. Is Tinker account readiness known?
3. Is cost acceptance recorded for paid external training?
4. Is Kaggle API submission status known?
5. Is the external training path selected, blocked, or deferred?
6. Should the project proceed toward controlled training, local 5090 probe, Submit UI preflight, or more schema/data work?
7. Can the reproduction readiness manifest move closer to `ready_for_training`, or does it remain blocked?

M09 is **not** a training milestone.

---

## 2. Current state

M00–M08 are merged to `main` (`ac7c5f2`).

| Blocker | Status |
| ------- | ------ |
| Submit UI `submission.zip` constraints | **OPEN** |
| Kaggle API submission | **TBD** |
| Modal credentials | **TBD** |
| Tinker credentials | **TBD** |
| Cloud GPU fallback | **TBD** |
| Cost acceptance | **TBD** |
| local_5090 CUDA/driver/VRAM | **TBD** |
| SQ-CORPUS-001 | **open** |
| Gate C training authorization | **not provided** |

M08 added `scripts/probe_local_5090.py` but did **not** execute it.

---

## 3. Source documents

Read before implementation:

- `docs/forge.md`, `docs/FORGE_ANCHOR.md`
- `docs/kaggle_submission_bible.md`, `docs/kaggle/kaggle_setup_evidence.md`
- `docs/milestones/M08/` — summary, audit, run1, readiness docs, `M08_next_decision.md`
- `src/forge_nemotron/baselines/reproduction_plan.py`
- `scripts/validate_reproduction_plan.py`, `scripts/probe_local_5090.py`

---

## 4. Authorization model

### Gate A — M09 kickoff

**Authorized** — branch, documentation, readiness manifests, credential/cost status recording (status only), validation, CI/PR/closeout.

### Gate B — Credential status recording

Allowed if owner provides **status only**, never secrets.

Examples: `Modal account: ready / blocked / TBD`

**Forbidden:** API keys, tokens, `.env`, credential files, screenshots containing secrets.

### Gate C — Cost acceptance recording

Allowed if owner provides cost status (yes/no/TBD, budget ceiling).

### Gate D — Local 5090 probe

Requires:

```text
M09_LOCAL_5090_PROBE_AUTHORIZED = yes
```

**M09 default:** `no` — create `local_5090_probe_blocked.md` only.

### Gate E — Training execution

Requires:

```text
M09_TRAINING_AUTHORIZED = yes
```

**M09 default:** `no` — no training, inference, `submission.zip`, or Kaggle submit.

---

## 5. Hard constraints

1. **No secrets committed** — Modal/Tinker/Kaggle/cloud credentials, `.env`, screenshots.
2. **No training** unless Gate E explicit.
3. **No inference**
4. **No Kaggle submission**
5. **No adapter artifacts** — `.safetensors`, `.bin`, `.pt`, `.pth`, adapter folders, `submission.zip`
6. **No public baseline vendoring** — no copied baseline code/data into FORGE

---

## 6. Scope

### In scope

- Modal/Tinker readiness evidence, external compute path decision, credential storage policy check
- Kaggle API / Submit UI status (preserve OPEN/TBD if no evidence)
- Local 5090 probe blocked doc (unless Gate D)
- SQ-CORPUS-001 status, readiness manifest, validator/tests, `M09_next_decision.md`
- `docs/forge.md`, README, toolcalls, CI

### Out of scope

- Training, inference, adapter generation, Kaggle submission, baseline reproduction
- Downloading/storing secrets, running Modal/Tinker jobs, real package creation

---

## 7. Deliverables

| # | Artifact | Path |
| - | -------- | ---- |
| 7.1 | Modal readiness evidence | `docs/milestones/M09/modal_readiness_evidence.md` |
| 7.2 | Tinker readiness evidence | `docs/milestones/M09/tinker_readiness_evidence.md` |
| 7.3 | External compute path decision | `docs/milestones/M09/external_compute_path_decision.md` |
| 7.4 | Credential storage policy check | `docs/milestones/M09/credential_storage_policy_check.md` |
| 7.5 | Kaggle API / Submit UI status | `docs/milestones/M09/kaggle_api_submit_status.md` |
| 7.6 | Local 5090 probe blocked OR probe evidence | `local_5090_probe_blocked.md` or `evidence/local_5090_probe/` |
| 7.7 | SQ-CORPUS-001 status | `docs/milestones/M09/sq_corpus_001_status.md` |
| 7.8 | Readiness manifest | `docs/milestones/M09/evidence/readiness/public_control_repro_plan.modal_tinker_gate.json` |
| 7.9 | Validator updates | `reproduction_plan.py`, `tests/unit/test_reproduction_plan.py` |
| 7.10 | Next decision | `docs/milestones/M09/M09_next_decision.md` |
| 7.11 | Governance | `docs/forge.md`, `README.md`, `M09_plan.md`, `M09_toolcalls.md` |

Default manifest when no owner evidence: `training_authorized: false`, `ready_for_training: false`, `credentials_ready: false`, `cost_accepted: false`, `compute_path: null`, Modal/Tinker **TBD**.

---

## 8. Implementation phases

### Phase A — Branch and plan setup

- Confirm clean `main`, branch `forge/M09-modal-tinker-setup-gate`
- Expand `M09_plan.md`, `M09_toolcalls.md`, mark M09 active in `docs/forge.md`, README

### Phase B — Readiness and credential docs

- Modal/Tinker evidence, external compute decision, credential policy, Kaggle status, probe blocked, SQ-CORPUS status, cost gate

### Phase C — Readiness manifest and validation

- M09 manifest; validator extensions; pytest + `validate_reproduction_plan.py`

### Phase D — Next decision and governance

- `M09_next_decision.md`; finalize `docs/forge.md`, README

Verification:

```bash
ruff check .
ruff format --check .
mypy src tests
pytest -q
python -m compileall src
python scripts/validate_reproduction_plan.py \
  docs/milestones/M09/evidence/readiness/public_control_repro_plan.modal_tinker_gate.json
```

---

## 9. Acceptance criteria

- [ ] Branch `forge/M09-modal-tinker-setup-gate` from green `main`
- [ ] `M09_plan.md` expanded; `M09_toolcalls.md` current
- [ ] `docs/forge.md` marks M09 active; README updated
- [ ] Modal/Tinker readiness docs exist; no secrets
- [ ] External compute path decision exists
- [ ] Credential storage policy check exists
- [ ] Kaggle API / Submit UI doc preserves OPEN/TBD
- [ ] Local 5090 probe blocked doc (probe not run)
- [ ] SQ-CORPUS-001 status doc exists
- [ ] M09 readiness manifest exists and validates
- [ ] Validator tests pass
- [ ] `M09_next_decision.md` exists; M10 not started
- [ ] No training, inference, submission, adapters, credentials committed
- [ ] CI green on PR

---

## 10. Risks and handling

| Risk | Handling |
| ---- | -------- |
| Credentials leak | Status only; never secrets |
| M09 drifts into training | Gate E required |
| Modal/Tinker overclaimed | Evidence or TBD only |
| Local probe accidental | Gate D phrase required |
| Cost ambiguous | Treat as not accepted |
| Gate C implied by readiness | Never — explicit training authorization required |

---

## 11. Closeout prompt for Cursor

```markdown
Close out milestone M09.

Tasks:
1. Ensure all documentation is updated as necessary.
2. Update `docs/forge.md` with completed M09 work, decisions, CI/local verification, readiness evidence, blockers, risks, next recommendation.
3. Create `docs/milestones/M09/M09_summary.md` using `docs/prompts/summaryprompt.md`.
4. Create `docs/milestones/M09/M09_audit.md` using `docs/prompts/unifiedmilestoneauditpromptV2.md`.
5. If GitHub Actions ran, create `docs/milestones/M09/M09_run1.md` per `docs/prompts/workflowprompt.md`.
6. Confirm acceptance criteria from this plan satisfied or explicitly deferred.
7. Confirm no credentials, adapters, zips, or probe JSON unless authorized and sanitized.
8. Confirm no local 5090 probe unless separately authorized.
9. Confirm no submission, training, inference, or reproduction claims without evidence.
10. Confirm readiness manifest reflects Modal/Tinker/compute/cost/submission/training state.
11. Confirm ruff, mypy, pytest, compileall, validate_reproduction_plan pass locally.
12. Prepare PR instructions for `forge/M09-modal-tinker-setup-gate` → `main`.
13. Seed `docs/milestones/M10/M10_plan.md` per `M09_next_decision.md`.
14. Do not merge, submit, train, infer, probe, or start M10 without explicit permission.
```

---

## 12. Final non-claims

Unless separately authorized and evidenced:

- no local 5090 probe executed
- no Kaggle submission or public/private score
- no model training or inference
- no reproduced public baseline
- no Kaggle-ready or real adapter package
- no copied/vendored public baseline code/data
- no committed credentials
