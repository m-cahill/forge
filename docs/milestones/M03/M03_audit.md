# M03 Audit — Solver and Synthetic Trace Factory

## 1. Header

| Field | Value |
| ----- | ----- |
| **Milestone** | M03 — Solver and Synthetic Trace Factory |
| **Mode** | DELTA AUDIT |
| **Range** | M02 merge `e78dc97` → M03 PR head `1c7dde2` |
| **Branch** | `forge/M03-solver-factory` |
| **PR** | [#4](https://github.com/m-cahill/forge/pull/4) |
| **current_sha** | `1c7dde268faa55a42ebba0d9f202531e99509334` |
| **CI Status** | **Green** — [26975703019](https://github.com/m-cahill/forge/actions/runs/26975703019) (3.10, 3.11, 3.12) |
| **Audit Verdict** | **Pass** — M03 factory pipeline delivered; synthetic self-check clearly not competition evidence |

**Overall score: 4.7 / 5.0**

**Why not 5/5:** Dataset/eval CLI not in CI; only three string transforms; no contamination check vs holdout IDs; Submit UI zip constraints still open. No HIGH issues.

**Why not lower:** Deterministic solvers, writer rejection gates, 127 tests, green CI, explicit non-claims, full smoke evidence with hashes.

---

## 2. Executive Summary (Delta-Focused)

**Improvements**

- First verified synthetic trace factory on structured problems (no eval/exec)
- Writer owns `\boxed{}` consistency; solvers return unboxed answers
- Dataset manifest + `make_dataset.py` integrate with M02 eval layer
- 50-example committed smoke with 100% factory self-check

**Risks**

- **GOV-005:** Factory 1.0 could be misread as model score — mitigated by README, summary §9, Run Ledger notes
- Synthetic smoke not registered as production holdout (correct — not for training unless reclassified)

**Next action:** Merge PR #4 with permission; authorize M04 preflight planning.

---

## 3. Delta Map & Blast Radius

| Changed | Notes |
| ------- | ----- |
| `solvers/`, `generators/`, `data/` | New factory surface |
| `scripts/make_dataset.py` | New CLI |
| `eval/records.py` | `synthetic_smoke` split |
| `docs/milestones/M03/evidence/` | Small JSONL evidence |
| Tests +21 | Solver, writer, determinism |

**Risk zones touched:** data provenance, trace format. Not touched: training, Kaggle submit, real adapters.

---

## 4. M03 Acceptance Criteria

| Criterion | Status |
| --------- | ------ |
| Branch from green `main` | Met |
| Solver base + arithmetic + string (3) + formatting stress | Met |
| Writer rejects unverified / missing boxed / duplicates | Met (tests) |
| Dataset manifest + SHA256 | Met |
| `make_dataset.py` deterministic | Met (seed 123 tests + smoke) |
| Local eval 100% factory self-check | Met |
| Evidence + non-claims README | Met |
| Dataset + Run Ledger | Met |
| PR CI green | Met — 26975703019 |
| No training/submission/score claims | Met |

---

## 5. Closeout Authorization

M03 may be marked **closed** in governance docs. **Merge** of PR #4 requires separate express owner permission.
