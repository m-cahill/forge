# M07_plan.md — Controlled Public Baseline Training Authorization Gate

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M07 |
| **Title** | Controlled Public Baseline Training Authorization Gate |
| **Branch** | `forge/M07-training-authorization-gate` |
| **Status** | **closed on branch** — PR [#8](https://github.com/m-cahill/forge/pull/8) CI green; merge pending |
| **Precondition** | M06 merged to `main`, post-merge CI green, owner authorized M07 kickoff |
| **Gate C** | `M07_TRAINING_AUTHORIZED = no` (Path A — blocked manifest) |

---

## 1. Objective

M07 is the formal gate before any real public control baseline training.

M06 completed schema inspection and produced derived notes from the public baseline artifacts, but training remains unauthorized. M07 must now determine whether all preconditions for training are satisfied:

1. Public baseline schema is sufficiently understood.
2. Corpus-to-FORGE mapping is sufficient or gaps are explicitly waived.
3. Compute path is selected.
4. Credentials are ready or not needed.
5. Submit UI constraints are recorded or explicitly deferred from training.
6. Training authorization is explicitly provided by owner.
7. Reproduction plan manifest can enter `ready_for_training` state.
8. No raw baseline code/data is committed to FORGE.
9. No Kaggle submission occurs.

M07 may produce a **training authorization package** and optional **dry-run scaffolding**, but it must not execute training unless the owner explicitly provides the required Gate C authorization.

---

## 2. Current state

M00–M06 are merged to `main`.

Current capabilities:

- boxed-answer metric,
- structural submission validator,
- local eval CLI,
- artifact hashing and run manifests,
- solver-verified synthetic data factory,
- adapter candidate manifest contract,
- reproduction plan manifest contract,
- public baseline planning docs,
- schema inspection gate artifacts from M06,
- derived schema notes for baseline artifacts,
- no raw public baseline data committed.

M06 findings (from M06 closeout):

| Artifact | Rows | SHA256 |
| -------- | ---- | ------ |
| `corpus.jsonl` | 17,963 | `1940a41c68d0f70013e0e448e04dd17c9143403bc1ce991e4603e9ad38b9fcf5` |
| `problems.jsonl` | 9,500 | `4b8bd8b62905fe156ffc9033f5677286e75a80e907841b0988a4b50cc4b8742e` |
| `generation.jsonl` | 9,500 | `58383d4ecb831d9a6567a34a9cccb0a48ba78c1511790eb981c011685ccd315d` |
| `train.csv` | 69,029 | `c99877aca84dc1564ef741a722a74458b06aa616b0b627d493a913063bd536ef` |

Known remaining blockers:

- Submit UI `submission.zip` constraints still open.
- Kaggle API submission still TBD.
- Modal/Tinker credentials TBD.
- local_5090 CUDA/driver/VRAM TBD.
- `corpus.segment` mapping partial / SQ-CORPUS-001.
- No training authorization.
- No real adapter candidate.
- No real local eval on a trained adapter.

---

## 3. Required source context

Cursor must read before implementation:

- `docs/forge.md`
- `docs/FORGE_ANCHOR.md`
- `docs/kaggle_submission_bible.md`
- `docs/kaggle/kaggle_setup_evidence.md`
- `docs/milestones/M04/candidate_promotion_preflight_gates.md`
- `docs/milestones/M05/control_reproduction_plan.md`
- `docs/milestones/M05/compute_path_decision.md`
- `docs/milestones/M05/baseline_acquisition_policy.md`
- `docs/milestones/M05/training_config_capture_template.md`
- `docs/milestones/M05/M05_next_decision.md`
- `docs/milestones/M06/M06_summary.md`
- `docs/milestones/M06/M06_audit.md`
- `docs/milestones/M06/M06_run1.md`
- `docs/milestones/M06/control_reproduction_execution_gate.md`
- `docs/milestones/M06/baseline_schema_mapping_supplement.md`
- all M06 external schema notes
- `src/forge_nemotron/baselines/reproduction_plan.py`
- `scripts/validate_reproduction_plan.py`
- `src/forge_nemotron/adapters/candidate_manifest.py`
- `scripts/validate_candidate_manifest.py`

External reference remains read-only:

- <https://github.com/tonghuikang/nemotron>

M07 uses M06 derived notes only — no new external clone/schema inspection unless explicitly authorized.

---

## 4. Authorization model

M07 has two possible paths.

### Path A — Authorization gate only (active)

Default: owner has **not** supplied training authorization.

**Locked for this run:**

```text
M07_TRAINING_AUTHORIZED = no
```

Allowed:

- readiness docs,
- manifests,
- checklists,
- validation code,
- dry-run templates,
- blocked decision,
- M08 recommendation.

Not allowed:

- training,
- inference,
- adapter creation,
- `submission.zip`,
- Kaggle submission.

### Path B — Training-preparation gate with authorization

Allowed only if owner supplies this exact statement or equivalent:

```text
M07_TRAINING_AUTHORIZED = yes
```

Required owner-provided fields:

```text
owner_training_authorization: <human-readable authorization string>
compute_path: <local_5090 | modal_tinker | cloud_gpu | other>
credentials_ready: <true/false>
cost_accepted: <true/false>
training_scope: <dry_run | controlled_public_baseline_attempt>
```

Even with authorization, M07 should default to preparing a manifest and dry-run command plan. Actual training execution should still be a separate explicitly named phase or future milestone unless the owner says “run training now.”

---

## 5. Hard constraints

### 5.1 No training unless Gate C is explicit

Do not run training unless `M07_TRAINING_AUTHORIZED = yes` is explicitly provided.

### 5.2 No inference unless explicitly authorized

Do not run Nemotron inference by default.

### 5.3 No Kaggle submission

Do not submit to Kaggle in M07.

### 5.4 No raw baseline data committed

Do not commit:

- `corpus.jsonl`,
- `problems.jsonl`,
- `generation.jsonl`,
- `train.csv`,
- tokenizer files,
- checkpoints,
- adapter weights,
- zipped packages,
- cloned public repo,
- public baseline source code.

### 5.5 No secrets committed

Do not commit:

- Kaggle API token,
- Modal token,
- Tinker key,
- cloud credentials,
- `.env` files,
- local machine paths containing secrets.

### 5.6 No baseline reproduction claim

M07 may claim “training authorized,” “training blocked,” or “ready-for-training manifest created” only if evidenced. It may not claim reproduction unless training/eval/package evidence exists.

---

## 6. Deliverables

### 6.1 Training authorization gate document

Create: `docs/milestones/M07/training_authorization_gate.md`

Sections:

1. Purpose and non-claims.
2. Required authorization fields.
3. Current authorization status.
4. Current compute status.
5. Current credential status.
6. Current schema mapping status.
7. Current Submit UI constraints status.
8. Go/no-go result.
9. Next required action.

### 6.2 Baseline schema readiness decision

Create: `docs/milestones/M07/baseline_schema_readiness_decision.md`

### 6.3 Compute and credential gate update

Create: `docs/milestones/M07/compute_credential_gate.md`

### 6.4 Submit UI constraint gate

Create: `docs/milestones/M07/submit_ui_constraint_gate.md`

Preserve blocker:

```text
Submit UI submission.zip constraints/warnings: OPEN — owner-action / not recorded
Kaggle API submission support: TBD
```

### 6.5 Reproduction plan ready-for-training manifest

Path A (active): `docs/milestones/M07/evidence/training_gate/public_control_repro_plan.training_blocked.json`

Path B (if authorized): `docs/milestones/M07/evidence/training_gate/public_control_repro_plan.ready_for_training.json`

### 6.6 Training config draft

Create: `docs/milestones/M07/training_config_draft.md` — draft only, not executed.

### 6.7 Dry-run command plan

Create: `docs/milestones/M07/dry_run_command_plan.md` — future commands only.

### 6.8 Optional validation hardening

If small and safe, add tests to `reproduction_plan.py` for `ready_for_training` gate.

### 6.9 M07 next decision document

Create: `docs/milestones/M07/M07_next_decision.md`

### 6.10 Documentation updates

Update:

- `docs/forge.md`,
- `README.md`,
- `docs/milestones/M07/M07_plan.md`,
- `docs/milestones/M07/M07_toolcalls.md`,
- `docs/kaggle/kaggle_setup_evidence.md` only if owner supplies Submit UI constraints,
- `scripts/README.md` only if scripts are added/changed.

---

## 7. Implementation phases

### Phase A — Branch and plan setup

- [x] Confirm current `main` clean (except M07 toolcalls log).
- [x] Create branch `forge/M07-training-authorization-gate`.
- [x] Expand `M07_plan.md`.
- [x] Create/update `M07_toolcalls.md`.
- [x] Update `docs/forge.md` — M07 active.
- [x] Update README current milestone.
- [x] Commit Phase A.

### Phase B — Gate documents

- [x] `training_authorization_gate.md`
- [x] `baseline_schema_readiness_decision.md`
- [x] `compute_credential_gate.md`
- [x] `submit_ui_constraint_gate.md`
- [x] Commit Phase B.

### Phase C — Reproduction plan training-gate manifest

- [x] `public_control_repro_plan.training_blocked.json`
- [x] evidence README
- [x] validator tests
- [x] validate manifest
- [x] Commit Phase C.

### Phase D — Training config draft and dry-run command plan

- [x] `training_config_draft.md`
- [x] `dry_run_command_plan.md`
- [x] Commit Phase D.

### Phase E — Next decision and governance updates

- [x] `M07_next_decision.md`
- [x] `docs/forge.md` in-progress record
- [x] Commit Phase E.
- [x] Closeout: summary, audit, run1

---

## 8. Acceptance criteria

M07 is complete only when:

- [x] Branch `forge/M07-training-authorization-gate` exists from current green `main`.
- [x] `docs/milestones/M07/M07_plan.md` is expanded.
- [x] `docs/milestones/M07/M07_toolcalls.md` exists.
- [x] `docs/forge.md` marks M07 active during implementation and is updated at closeout.
- [x] Training authorization gate doc exists.
- [x] Schema readiness decision exists.
- [x] Compute/credential gate exists.
- [x] Submit UI constraint gate exists.
- [x] Training-gate reproduction manifest exists and validates.
- [x] Evidence README labels training state clearly.
- [x] Training config draft exists.
- [x] Dry-run command plan exists and is not executed.
- [x] M07 next-decision document exists.
- [x] Submit UI zip constraints are either recorded or explicitly left open.
- [x] CI is green on PR — [26986703969](https://github.com/m-cahill/forge/actions/runs/26986703969).
- [x] No Kaggle submission is attempted.
- [x] No public/private score is claimed.
- [x] No training is performed unless explicitly authorized.
- [x] No model inference is performed unless explicitly authorized.
- [x] No public baseline reproduction is claimed.
- [x] No baseline code/data is copied into FORGE.
- [x] No real adapter/package is created unless explicitly authorized.

---

## 9. Optional stretch goals

Only after required criteria pass:

1. Add `validate_training_gate.py` wrapper if reproduction validator UX is unclear.
2. Add a Markdown go/no-go checklist for owner review.
3. Add local_5090 probe instructions (do not run unless owner authorizes).
4. Add CI step for `validate_reproduction_plan.py`.

Do not train, infer, submit, upload, or create adapters as a stretch goal.

---

## 10. Risks and handling

| Risk | Handling |
| ---- | -------- |
| M07 accidentally becomes training | Default to blocked manifest unless explicit authorization |
| Owner authorization ambiguous | Stop and ask; do not infer |
| Training config draft mistaken for executed config | Label draft/not executed |
| Dry-run command plan gets executed | Commands are future-only unless separately authorized |
| Submit UI constraints still open | Preserve blocker |
| Compute readiness overclaimed | Evidence or TBD only |
| Baseline reproduction overclaimed | Non-claims everywhere |

---

## 11. Closeout prompt for Cursor

Use this when M07 implementation is complete:

```markdown
Close out milestone M07.

Tasks:
1. Ensure all documentation is updated as necessary.
2. Update `docs/forge.md` with completed M07 work, decisions, CI/local verification status, training-gate evidence, unresolved blockers, risks, and next recommendation.
3. Create `docs/milestones/M07/M07_summary.md` using `docs/prompts/summaryprompt.md`.
4. Create `docs/milestones/M07/M07_audit.md` using `docs/prompts/unifiedmilestoneauditpromptV2.md`.
5. If GitHub Actions ran, analyze the workflow using `docs/prompts/workflowprompt.md` and create `docs/milestones/M07/M07_run1.md` or equivalent workflow evidence.
6. Confirm every acceptance criterion from `docs/milestones/M07/M07_plan.md` is satisfied or explicitly deferred with rationale and exit criteria.
7. Confirm public baseline code/data was not copied or vendored into FORGE.
8. Confirm no credentials or external clone artifacts were committed.
9. Confirm the training-gate manifest accurately reflects authorization state.
10. Confirm no Kaggle submission, public/private score, model training, model inference, Kaggle-ready adapter, real adapter package, copied baseline code/data, or reproduced-baseline claim is made without evidence.
11. Confirm `ruff check .`, `ruff format --check .`, `mypy src tests`, `pytest -q`, `python -m compileall src`, and `validate_reproduction_plan.py` pass locally.
12. Confirm CI status and include run IDs if CI exists.
13. Prepare PR instructions for `forge/M07-training-authorization-gate` → `main`.
14. Seed `docs/milestones/M08/M08_plan.md` according to `M07_next_decision.md`.
15. Create `docs/milestones/M08/M08_toolcalls.md` if that convention remains active.
16. Do not merge, upload to Kaggle, submit anything, start M08 implementation, run training, run inference, create real adapter files, or push extra post-closeout changes without explicit user permission.
```

---

## 12. Final non-claims

M07 must explicitly preserve unless separately authorized and evidenced:

- no Kaggle submission,
- no public score,
- no private score,
- no model training,
- no model inference,
- no reproduced public baseline,
- no Kaggle-ready adapter,
- no real adapter package,
- no copied/vendored public baseline code/data,
- no committed credentials.
