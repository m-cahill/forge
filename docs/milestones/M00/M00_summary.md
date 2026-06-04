# 📌 Milestone Summary — M00: Anchor, Competition Intake, and Kaggle Submission Bible

**Project:** FORGE — Kaggle NVIDIA Nemotron Model Reasoning Challenge  
**Phase:** Initial intake (M00)  
**Milestone:** M00 — Anchor, competition intake, and Kaggle submission bible  
**Timeframe:** 2026-06-03 → 2026-06-04  
**Status:** Closed — awaiting merge  
**Branch:** `forge/M00-anchor-intake`  
**Baseline:** `9512c89` (Initial commit) → `f61e5cb` (M00 implementation tip pre-closeout)

---

## 1. Milestone Objective

Establish authoritative project truth, competition intake records, a FORGE-specific Kaggle operational reference, and an initial repository scaffold so later milestones (M01 control reproduction, local eval, solvers) can proceed without governance drift or mistaken submission assumptions.

Without M00, the project would lack a single Ultimate Truth ledger, documented LoRA `submission.zip` contract (vs CSV-style competitions), repo-first notebook policy, and explicit owner-action blockers for authenticated Kaggle facts.

---

## 2. Scope Definition

### In Scope

- `docs/FORGE_ANCHOR.md` verification (canonical at `docs/`)
- `docs/forge.md` Ultimate Truth initialization and M00 updates
- `docs/kaggle_submission_bible.md` and `docs/kaggle/*` runbook/evidence/debug docs
- Public Kaggle deadline recording; owner-action blockers for authenticated fields
- Repo scaffold (`configs/`, `data/`, `src/forge_nemotron/`, `tests/`, `artifacts/`, `submissions/`)
- `.cursorrules`, `.gitignore`, `README.md`, notebook/scripts READMEs
- `docs/milestones/M00/M00_plan.md`, `M00_toolcalls.md`
- `docs/milestones/M01/M01_plan.md` stub and M01 baseline recommendation
- Local verification: `compileall`, `forge_nemotron` import with `PYTHONPATH=src`

### Out of Scope

- Model training, LoRA creation, Kaggle submission, public score
- Solver implementation, package validator implementation, metric harness
- CI/GitHub Actions workflow configuration
- `pyproject.toml` / installable package wiring
- Reproduction of `tonghuikang/nemotron` (M01)
- Authenticated Kaggle Submit UI values (owner-action)

Scope did not change during execution.

---

## 3. Work Executed

| Area | Actions |
| ---- | ------- |
| Governance | Created/updated Ultimate Truth, authority rules, blocking questions, holdout register, promotion gates, risk register |
| Kaggle ops | FORGE submission bible; setup runbook; evidence template; notebook debug standard |
| Scaffold | Directory tree with `.gitkeep`; `src/forge_nemotron/__init__.py` (v0.0.0) |
| Milestones | M00 plan/toolcalls; M01 stub plan |
| Hygiene | README, `.gitignore` (reference docs, artifacts, `*.zip`), `.cursorrules` (hard gates + workflow) |

**Implementation commits (4):**

| SHA (short) | Message |
| ----------- | ------- |
| `6de7444` | `docs(forge): verify anchor and ultimate truth for M00` |
| `e1194d4` | `docs(kaggle): add FORGE submission bible and evidence runbooks` |
| `5270ac7` | `chore(scaffold): add FORGE project skeleton and M00 hygiene` |
| `f61e5cb` | `chore(scaffold): track data directory placeholders` |

Mechanical scaffold and documentation only; no competition logic implemented.

---

## 4. Validation & Evidence

| Check | Result | Notes |
| ----- | ------ | ----- |
| `python -m compileall src` | Pass | Closeout re-run |
| `PYTHONPATH=src` → `import forge_nemotron` | Pass | No `pyproject.toml`; import path documented |
| `pytest -q` | N/A | No tests configured; 0 tests collected |
| GitHub Actions / CI | N/A | No `.github/workflows` in repository |
| Scope guardrail review | Pass | No training/submission/score claims in committed docs |

Validation is **local-only**. CI truth signal does not exist yet; deferred to M01 or dedicated CI milestone.

---

## 5. CI / Automation Impact

- No workflows added or modified.
- `.cursorrules` defines milestone CI monitoring for future PRs.
- M00 did not claim green CI.

---

## 6. Issues & Exceptions

| Issue | Root cause | Status | Reference |
| ----- | ---------- | ------ | --------- |
| Daily submission limit unknown | Cursor cannot access authenticated Submit UI | Deferred — owner-action | BQ-001, `docs/kaggle/kaggle_setup_evidence.md` |
| Rules/team status unknown | Cursor cannot access authenticated account page | Deferred — owner-action | BQ-003, evidence doc |
| `FORGE_ANCHOR.md` header still says "repo root" in Status line | Pre-existing anchor metadata; canonical path resolved at `docs/` | Unchanged — no duplicate created | `docs/FORGE_ANCHOR.md` L5 |

No implementation defects or silent failures in M00 scope.

---

## 7. Deferred Work

| Item | Why deferred | Pre-existed | Status |
| ---- | ------------ | ----------- | ------ |
| BQ-001 daily submission limit | Authenticated UI only | Yes (M00 plan) | Open — owner |
| BQ-003 rules/team joined | Authenticated UI only | Yes | Open — owner |
| Exact `submission.zip` size/extra files | Submit UI not verified | Yes | Open — owner/M01 |
| Kaggle API submission support | Not verified | Yes | Open |
| `pyproject.toml` / pytest / CI | Out of M00 scope | N/A | Deferred to M01+ |
| Package validator, metric, solvers | M01+ | N/A | Not started |

---

## 8. Governance Outcomes

What is now provably true:

- **`docs/forge.md`** is Ultimate Truth with mandatory closeout rules.
- **`docs/FORGE_ANCHOR.md`** is the single canonical doctrine copy under `docs/`.
- FORGE competition artifact is **`submission.zip`** (LoRA, rank ≤ 32), not CSV.
- Notebook workflow is **repo-first** (commit → reupload); Kaggle-site edits are emergency-only.
- Four holdouts are registered; promotion gates and hard gates are in `.cursorrules`.
- Public deadlines recorded: entry **June 8, 2026**; final **June 15, 2026 11:59 PM UTC** (owner reconfirm recommended).
- M01 control baseline **recommended**: `tonghuikang/nemotron` — **not reproduced**.

---

## 9. Exit Criteria Evaluation

| Criterion | Result | Evidence |
| --------- | ------ | -------- |
| `docs/FORGE_ANCHOR.md` canonical | Met | `docs/FORGE_ANCHOR.md` committed |
| `docs/forge.md` current | Met | Closeout update |
| Kaggle bible + runbooks | Met | `docs/kaggle_submission_bible.md`, `docs/kaggle/*` |
| Public deadlines | Met | Competition Snapshot + evidence |
| Daily submission limit | Not Met (deferred) | Owner-action; no guess |
| Rules/team status | Not Met (deferred) | Owner-action; no guess |
| Repo scaffold | Met | Tree + `.gitkeep` |
| M00 plan/toolcalls | Met | `docs/milestones/M00/` |
| M00 summary/audit | Met | This file + `M00_audit.md` |
| M01 recommendation | Met | `docs/forge.md` § M01 Recommendation |
| No false competition claims | Met | Guardrail review |

M00 implementation scope is **complete**. Two intake fields remain **owner-action** per plan; they do not block merge of governance/scaffold work but must be resolved before submission budgeting.

---

## 10. Final Verdict

**Milestone objectives met for in-scope work. Safe to open PR for `forge/M00-anchor-intake`.**

Authenticated Kaggle facts (daily limit, rules/team) remain owner-action blockers and must be recorded before M01 Kaggle submission planning is considered complete.

---

## 11. Authorized Next Step

- **Authorized:** PR from `forge/M00-anchor-intake` → `main` (merge only with express permission).
- **Authorized:** M01 kickoff on branch `forge/M01-control-baseline` after merge or explicit authorization — inspect/wrap `tonghuikang/nemotron`; implement boxed-answer metric and package validation **before** any Kaggle submission.
- **Not authorized:** M01 implementation in this closeout; Kaggle upload; merge/push without permission.

---

## 12. Canonical References

| Reference | Location |
| --------- | -------- |
| Ultimate Truth | `docs/forge.md` |
| Doctrine | `docs/FORGE_ANCHOR.md` |
| Kaggle bible | `docs/kaggle_submission_bible.md` |
| M00 plan | `docs/milestones/M00/M00_plan.md` |
| M00 audit | `docs/milestones/M00/M00_audit.md` |
| M00 toolcalls | `docs/milestones/M00/M00_toolcalls.md` |
| M01 stub | `docs/milestones/M01/M01_plan.md` |
| Commits | `6de7444`, `e1194d4`, `5270ac7`, `f61e5cb` (+ closeout commit pending) |
| Baseline | `9512c89` |

---

## Kaggle Intake Facts (M00)

| Field | Value |
| ----- | ----- |
| Entry deadline | June 8, 2026 |
| Final deadline | June 15, 2026, 11:59 PM UTC |
| Daily submission limit | **OWNER ACTION** — not guessed |
| Rules/team status | **OWNER ACTION** — not guessed |

## Non-Claims (Explicit)

- No Kaggle submission
- No public score
- No reproduced baseline
- No package-valid adapter
- No model training
- No model inference

## Remaining Owner Actions

1. Confirm daily submission limit in authenticated Submit UI → update `docs/forge.md` and `docs/kaggle/kaggle_setup_evidence.md`
2. Confirm rules accepted / team joined → same
3. Reconfirm public deadlines on live Kaggle
4. Record exact zip constraints from Submit UI if shown
