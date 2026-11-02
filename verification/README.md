# Verification and experimental test kits

**[Phase-by-phase evidence index](EVIDENCE-INDEX.md)** — what has actually been archived, reported, or remains missing.


The scripts under [legacy-test-kit](legacy-test-kit/) are historical, bounded Python experiments, **not** a production NNNC implementation or proof of real-world protected-effect safety.

## Files

- `step9.py` — earlier governance model.
- `model.py` — Step 10 effect protocol atop Step 9; explicitly logical-only, without durable I/O or concurrency guarantees.
- `test_step10.py` — Step 10 tests.
- `explore.py` — bounded state-space exploration using `model.py` and `step9.py`.
- `run_build4.py` — historical Phase 1 Build 4 runner; references `sources/nnnc_phase1_build1..3` **not present in the repository snapshot**, so this command is not reproducible from this checkout alone.
- `generate_report.py` — report generation from `execution_results.json`; review paths before running because the files have been reorganized.

Historical evidence is in [reports](reports/), [results](results/), and [traceability](traceability/). Existing report and result content is preserved verbatim; it is not a fresh test run.

### Caution

Relocation preserves the scripts together so their sibling imports remain coherent, but scripts with hard-coded working-directory or report paths may need future adaptation. No execution or end-to-end reproducibility claim is made by this organization change.

Phase 0 obligations P0-O01 through P0-O08 remain tracked; O01–O03 block claims of safe real protected effects.
