# M04 Audit — Public Control Adapter Reproduction Preflight

## 1. Header

| Field | Value |
| ----- | ----- |
| **Milestone** | M04 — Public Control Adapter Reproduction Preflight |
| **Mode** | DELTA AUDIT |
| **Range** | M03 merge `fe2a7dd` → M04 PR head `26861ff` |
| **Branch** | `forge/M04-control-preflight` |
| **PR** | [#5](https://github.com/m-cahill/forge/pull/5) |
| **current_sha** | `26861ffbbb526ad313bdd299e26c1de1b7d5d7e8` |
| **CI Status** | **Green** — [26977971068](https://github.com/m-cahill/forge/actions/runs/26977971068) (3.10, 3.11, 3.12) |
| **Audit Verdict** | **Pass** — preflight contracts delivered; no baseline copy; mock manifest clearly labeled |

**Overall score: 4.6 / 5.0**

**Why not 5/5:** Submit UI zip constraints still OPEN; candidate manifest CLI not in CI; corpus schema byte-level mapping still unknown; no real control candidate (expected for M04).

**Why not lower:** Complete dossier/mapping, status-aware validator with tests, green CI, explicit non-claims, clean-room posture preserved.

---

## 2. Executive Summary (Delta-Focused)

**Improvements**

- Documented public baseline workflow and FORGE mapping with unknowns explicit
- Adapter candidate manifest contract with five statuses and hash promotion rules
- Mock preflight evidence + CLI; 11 tests for rank/status/submitted/rejected paths
- Promotion gates and M05 recommendation without starting M05

**Risks**

- **GOV-006:** Mock manifest could be mistaken for real adapter — mitigated by README, `non_claims`, forge disclaimer
- **GOV-007:** Submit UI constraints OPEN — documented blocker; not guessed

**Next action:** Merge PR #5 with owner permission; authorize M05 planning only.

---

## 3. Delta Map & Blast Radius

| Changed | Notes |
| ------- | ----- |
| `adapters/candidate_manifest.py` | New governance contract |
| `docs/milestones/M04/*` | Preflight docs + small JSON evidence |
| `scripts/validate_candidate_manifest.py` | New CLI |
| Tests +11 | Manifest validation |

**Risk zones touched:** candidate promotion, baseline intake references. Not touched: training, Kaggle submit, real adapters, baseline repo vendoring.

---

## 4. M04 Acceptance Criteria

| Criterion | Status |
| --------- | ------ |
| Branch from green `main` | Met |
| Deliverables 4.1–4.9 | Met |
| Mock manifest validates | Met |
| Submit UI OPEN (not guessed) | Met |
| PR CI green | Met — 26977971068 |
| No training/submission/score/reproduction claims | Met |
| No baseline code copied | Met |

---

## 5. Validator Rules Verified (tests)

| Rule | Test coverage |
| ---- | ------------- |
| `adapter_rank` > 32 rejected | `test_rank_over_32_rejected` |
| `preflight` allows null hashes | `test_preflight_valid_without_hashes` |
| `submitted` requires package hash + `kaggle_submission_id` | `test_submitted_*` |
| `rejected` requires notes or `rejection_reason` | `test_rejected_*` |

---

## 6. Closeout Authorization

M04 may be marked **closed** in governance docs. **Merge** of PR #5 requires separate express owner permission. **M05 implementation** requires separate authorization.
