# Local 5090 Probe — Blocked (M09)

**Milestone:** M09  
**Probe script:** `scripts/probe_local_5090.py` (exists from M08; not executed)

---

## Authorization

```text
M09_LOCAL_5090_PROBE_AUTHORIZED = no
Probe executed = no
CUDA/driver/VRAM remain TBD
```

---

## Rationale

Owner did not supply `M09_LOCAL_5090_PROBE_AUTHORIZED = yes`. Per M09 gates, the probe must not run without that exact authorization phrase.

---

## What would run if authorized (reference only)

```bash
python scripts/probe_local_5090.py --out docs/milestones/M09/evidence/local_5090_probe/local_5090_probe.json
```

The probe must not load models, train, or infer. M09 did not execute this command.

---

## Environment ledger (not hardware verification)

| Field | Value |
| ----- | ----- |
| Hardware ID | local_5090 |
| Listed hardware | RTX 5090 Blackwell (per `docs/forge.md` §14) |
| CUDA / driver / VRAM | **TBD** |

Listing hardware in the ledger is **not** CUDA/driver/VRAM verification.

---

## Non-claims

- No `nvidia-smi` or torch CUDA probe was executed in M09.
- No claim that local_5090 is training-ready.
