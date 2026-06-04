# Kaggle Setup Runbook — FORGE

**Authority:** Subordinate to Kaggle rules/UI and [`docs/forge.md`](../forge.md).  
**Companion:** [`docs/kaggle_submission_bible.md`](../kaggle_submission_bible.md)

## Purpose

Step-by-step verification of competition intake before M01 submissions. M00 records evidence; it does not submit.

## Prerequisites

- Kaggle account with competition access
- Team membership confirmed (if applicable)
- Local repo on branch `forge/M00-anchor-intake` or later

## Runbook steps

### 1. Open competition

1. Go to <https://www.kaggle.com/competitions/nvidia-nemotron-model-reasoning-challenge>
2. Confirm overview: base model, LoRA adapter, `submission.zip`, rank ≤ 32, `\boxed{}` answers.
3. Record URL and date in [`kaggle_setup_evidence.md`](kaggle_setup_evidence.md).

### 2. Rules and team status (authenticated)

1. Open **Rules** tab.
2. Confirm rules accepted / team joined.
3. Record status in evidence table and update `docs/forge.md` Competition Snapshot → Rules accepted.

**If not accepted:** complete acceptance before entry deadline (**June 8, 2026**).

### 3. Deadlines (public + confirm on site)

| Deadline | Public value (M00) | Verify on Kaggle |
| -------- | ------------------ | ---------------- |
| Entry | June 8, 2026 | Rules/Overview |
| Final | June 15, 2026, 11:59 PM UTC | Overview |

Update `docs/forge.md` if live UI differs.

### 4. Daily submission limit (authenticated)

1. Open **Submit** or **Submissions** UI while logged in.
2. Record exact daily team submission limit.
3. Update `docs/forge.md` and bible section 2.

**Do not guess** if UI is unavailable to Cursor.

### 5. Submission package expectations

From overview (confirm on Submit UI):

- Artifact: `submission.zip`
- Contents: LoRA adapter + `adapter_config.json` (+ expected weight files)
- Rank ≤ 32; compatible with Nemotron-3-Nano-30B

Note any size limits or extra required files in evidence.

### 6. Prize eligibility

Confirm requirements for:

- Public Kaggle notebook
- Public solution write-up

Record links/requirements in evidence; track in `docs/forge.md` Documentation Eligibility Tracker.

### 7. Notebook workflow (FORGE policy)

1. Edit notebook in repo under `notebooks/`.
2. Commit via git.
3. Reupload/resync to Kaggle.
4. Log attempt in [`kaggle_setup_evidence.md`](kaggle_setup_evidence.md).

### 8. Post-verification

1. Update `docs/forge.md` blocking questions BQ-001–BQ-003.
2. Close or defer M00 exit criteria checkboxes.
3. Do **not** claim submission readiness or score without evidence.

## Owner-action blockers (M00)

| Item | Action |
| ---- | ------ |
| Daily submission limit | Authenticated Submit UI |
| Rules/team status | Authenticated competition page |
| Exact zip size/extra files | Submit UI + rules if specified |

Cursor records blockers when authenticated access is unavailable.
