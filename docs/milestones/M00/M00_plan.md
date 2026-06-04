# M00_plan.md — Anchor, Competition Intake, and Kaggle Submission Bible

## Milestone

**Milestone:** M00  
**Title:** Anchor, competition intake, and Kaggle submission bible  
**Branch:** `forge/M00-anchor-intake`  
**Primary owner:** Cursor  
**Status:** closed — awaiting merge (2026-06-04)  
**Target posture:** Local verification documented; CI deferred to M01+.

---

## 1. Objective

Establish FORGE authoritative project truth, competition intake records, initial repo scaffold, and a FORGE-specific Kaggle submission reference.

**M00 is governance/documentation/scaffold only.** No training, Kaggle submission, solver implementation, or score claims.

`docs/forge.md` is Ultimate Truth and must stay current through closeout.

---

## 2. Locked decisions (M00)

| Topic | Decision |
| ----- | -------- |
| Anchor location | **`docs/FORGE_ANCHOR.md`** canonical; no repo-root duplicate |
| Public deadlines | Entry **June 8, 2026**; final **June 15, 2026 11:59 PM UTC** (owner reconfirm) |
| Daily limit / rules | **Owner-action**; no guessing |
| PANTANAL bible | Style reference only; FORGE uses `submission.zip`, not CSV |
| M01 baseline | Recommend [tonghuikang/nemotron](https://github.com/tonghuikang/nemotron); not reproduced yet |
| Branch | All M00 work on `forge/M00-anchor-intake` |

---

## 3. Deliverables

### 5.1 `docs/FORGE_ANCHOR.md`

- Verify exists at `docs/FORGE_ANCHOR.md`.
- Verify `docs/forge.md` authority hierarchy matches.
- Do not duplicate or move anchor unless verification fails.

### 5.2 `docs/forge.md`

- Preserve structure; fill public dates; owner-action blockers for authenticated fields.
- Update M00 exit checklist and M01 recommendation.

### 5.3 `docs/kaggle_submission_bible.md`

- FORGE-specific; `submission.zip`; LoRA rank ≤ 32; notebook repo-first policy; debug standard; prohibited claims.

### 5.4 `docs/kaggle/`

- `kaggle_setup_runbook.md`
- `kaggle_setup_evidence.md`
- `notebook_debug_standard.md`

### 5.5 Repo scaffold

Per `docs/FORGE_ANCHOR.md` §8: `configs/`, `data/`, `src/forge_nemotron/`, `tests/`, `artifacts/runs/`, `submissions/`, etc.

### 5.6 Hygiene

- `README.md`, `.gitignore`, `notebooks/README.md`, `scripts/README.md`
- `src/forge_nemotron/__init__.py`

### 5.7 M01 handoff

- `docs/milestones/M01/M01_plan.md` stub
- M01 recommendation in `docs/forge.md`

---

## 4. Implementation phases

| Phase | Work |
| ----- | ---- |
| A | Branch + verify anchor + `docs/forge.md` |
| B | Kaggle bible + `docs/kaggle/*` |
| C | Live intake (public dates + owner-action blockers) |
| D | Scaffold |
| E | `M00_plan.md`, `M00_toolcalls.md` |

---

## 5. Acceptance criteria

- [x] `docs/FORGE_ANCHOR.md` in canonical location
- [x] `docs/forge.md` current
- [x] `docs/kaggle_submission_bible.md` FORGE-specific (no CSV submission rules)
- [x] `docs/kaggle/` runbook, evidence, debug standard exist
- [x] Public entry/final deadlines recorded
- [ ] Daily submission limit recorded (**owner-action**)
- [ ] Rules/team status verified (**owner-action**)
- [x] Repo scaffold exists
- [x] `M00_plan.md`, `M00_toolcalls.md` exist
- [x] `M00_summary.md`, `M00_audit.md` (closeout)
- [x] M01 recommendation recorded
- [x] No false Kaggle submission/score claims

---

## 6. Closeout (after permission)

1. Update `docs/forge.md`
2. `M00_summary.md`, `M00_audit.md`
3. Seed M01 if not done
4. PR/merge only with express permission

See `docs/FORGE_ANCHOR.md` §21 closeout template.
