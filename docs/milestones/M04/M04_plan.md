# M04_plan.md — Public Control Adapter Reproduction Preflight

## Milestone

| Field | Value |
| ----- | ----- |
| **Milestone** | M04 |
| **Title** | Public Control Adapter Reproduction Preflight |
| **Branch** | `forge/M04-control-preflight` |
| **Status** | **closed** — PR [#5](https://github.com/m-cahill/forge/pull/5); CI green; merge pending permission |
| **Precondition** | M03 merged to `main`, post-merge CI green, owner authorized M04 kickoff |
| **Primary goal** | Prepare FORGE to reproduce or wrap the public control baseline safely, without training or submitting yet |

---

## 1. Objective

M04 creates the preflight layer needed before any real public control adapter reproduction attempt.

- M01: metric and package validation
- M02: local evaluation and artifact manifests
- M03: deterministic solver-verified synthetic traces

M04 maps the public baseline workflow into FORGE local contracts and defines what a real control-candidate run must produce before any Kaggle submission.

**By end of M04:**

1. Documented public control reproduction preflight dossier
2. Baseline artifact and data-format mapping (`tonghuikang/nemotron` → FORGE)
3. Adapter candidate manifest contracts
4. Candidate promotion preflight gates
5. Mock/dry-run control candidate package manifest
6. Package validator integration where practical (`validate_candidate_manifest.py`)
7. M04 next-decision document for M05
8. Green CI and full milestone documentation

**M04 is not a training milestone.**

---

## 2. Current state

M00–M03 merged to `main`. FORGE has installable package, CI (Python 3.10–3.12), boxed metric, structural LoRA validator, baseline intake, local eval CLI, hashing, run manifests, synthetic trace factory, ledgers, fixture/synthetic smoke evidence.

**Non-claims (preserve):** no Kaggle submission, no public/private score, no training, no inference, no reproduced baseline, no Kaggle-ready adapter.

**Open intake:** Submit UI `submission.zip` constraints — **OPEN** (owner-action); Kaggle API path TBD.

---

## 3. Hard constraints

| Rule | M04 posture |
| ---- | ----------- |
| No training | No SFT, QLoRA, inference, Modal/Tinker, GPU jobs |
| No Kaggle submission | No upload |
| No score claim | No public/private score |
| No reproduction claim | Map/plan only |
| No code copy | Clean-room / external-reference only |
| Evidence over assumptions | Document in M04 artifacts; mark unknown |

---

## 4. Deliverables and acceptance

| ID | Deliverable | Path | Acceptance |
| -- | ----------- | ---- | ------------ |
| 4.1 | Public control preflight dossier | `public_control_preflight.md` | Exists; no reproduction claim; open questions explicit |
| 4.2 | Baseline format mapping | `baseline_format_mapping.md` | Each row mapped/unknown/deferred |
| 4.3 | Candidate manifest contract | `src/forge_nemotron/adapters/candidate_manifest.py` | Validator + tests (rank, status rules) |
| 4.4 | Promotion preflight gates | `candidate_promotion_preflight_gates.md` | Every gate has required evidence |
| 4.5 | Mock preflight evidence | `evidence/control_preflight/` | Validates; non-claims loud |
| 4.6 | Validation CLI | `scripts/validate_candidate_manifest.py` | Passes on mock manifest |
| 4.7 | Submit UI constraints | kaggle docs / forge.md | Recorded or explicitly OPEN |
| 4.8 | M04 next decision | `M04_next_decision.md` | Recommends M05; does not start M05 |
| 4.9 | Governance updates | `docs/forge.md`, `README.md`, toolcalls | M04 active/complete per phase |

**Status enum (full):** `preflight`, `packaged`, `local_eval_complete`, `submitted`, `rejected`

---

## 5. Implementation phases

### Phase A — Branch and plan setup

- Confirm clean `main`; branch `forge/M04-control-preflight`
- Expand this plan; toolcalls; mark M04 active in `docs/forge.md` and README
- Commit: `docs(milestones): expand M04 control preflight plan`

### Phase B — Public baseline preflight docs

- `public_control_preflight.md`, `baseline_format_mapping.md`
- M01 intake + fresh read-only GitHub inspection (no clone/copy)
- Commit: `docs(baseline): map public control reproduction preflight`

### Phase C — Candidate manifest contract

- `src/forge_nemotron/adapters/`, `tests/unit/test_candidate_manifest.py`
- Commit: `feat(adapters): add candidate manifest contract`

### Phase D — Mock evidence and script

- `evidence/control_preflight/`, `scripts/validate_candidate_manifest.py`
- Commit: `docs(adapters): add control candidate preflight evidence`

### Phase E — Gates and next decision

- `candidate_promotion_preflight_gates.md`, `M04_next_decision.md`
- Update `docs/forge.md`
- Commit: `docs(governance): define control candidate promotion gates`

---

## 6. Acceptance criteria (closeout)

- [x] Branch `forge/M04-control-preflight` from green `main`
- [x] All deliverables 4.1–4.9
- [x] Mock manifest validates
- [x] Submit UI constraints OPEN or recorded (not guessed) — **OPEN**
- [x] CI green on PR — [26977971068](https://github.com/m-cahill/forge/actions/runs/26977971068)
- [x] All non-claims preserved
- [x] No public baseline code copied into FORGE

---

## 7. Stretch goals (deferred)

JSON Schema, manifest diff helper, checklist template, dependency matrix beyond preflight docs — only after required criteria; `to_json`/`from_json` roundtrip allowed if trivial.

---

## 8. Closeout

Use closeout prompt in milestone kickoff (summary, audit, run1, M05 stub seed) — **only with owner permission**; do not merge or start M05 without authorization.
