# Phase 0 — Ontological Boundary: evidence

Existing code: [legacy test kit](../legacy-test-kit/) (`step9.py`, `model.py`, `test_step10.py`, `explore.py`). Historical reports: [Step 11 audit](../reports/PHASE0_STEP11_AUDIT.md) and [closure/handoff](../reports/PHASE0_CLOSURE_AND_HANDOFF.md).

**Reported historical results:** 15 Step 10 targeted tests passed; depth-5 explorer visited 550 states with zero invariant violations in that bounded search. **Not freshly rerun here.** Model explicitly excludes durable I/O and concurrent/physical-effect guarantees. P0-O01..O08 remain tracked, especially deployment blockers O01–O03.
