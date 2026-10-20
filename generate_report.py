from pathlib import Path
import json,csv,zipfile
r=Path(__file__).resolve().parent
res=json.loads((r/'execution_results.json').read_text())
rows=[
('VO-01','NNNC/NES separation','Build1 T-01; T-04','Scenario only; no ontological independence proof','OPEN','Phase 1 closure register / later integration'),
('VO-02','State/referent/identity distinctions','Build1 T-08','Conservative no-inference behavior; no identity proof','OPEN','Phase 2 Identity & Continuity'),
('VO-03','Process/constituent/entity distinction','Build1 T-01','Limited construction; no exhaustive independence countermodels','OPEN','Later entity integration'),
('VO-04','Pre-state authority','Build1 T-05; Build2 history tests; Build3 independent checker','Finite model, simplified P0 authorization','OPEN','Phase 0 O01/O06; governance implementation'),
('VO-05','Continuity/branch/restoration','Build1 T-07/T-08','No substantive identity or restoration verifier','OPEN','Phase 2 Identity & Continuity; P0-O08'),
('VO-06','Capability/evidence/claims separation','Build1 T-10/T-12','Limited qualification decision paths','OPEN','Qualification evaluation stage'),
('VO-07','External trust/custody vs membership','Build1 T-04','No complete independent semantic countermodels','OPEN','Boundary/integration stage'),
('VO-08','Profile floor and non-substitution','Build1 T-02/T-03/T-11','Necessary-condition checks, not realized FFNN/SA','OPEN','FFNN and SA realization phases'),
('VO-09','Internal causal integration','Build1 T-04','Unknown verdict; no interventions performed','OPEN','Causal integration domain'),
('VO-10','Cross-history protected conflicts','Build1 T-06; Build2 conflict tests; Build3 mutation','Central adjudication only; no distributed physical effects','OPEN','Phase 0 O03/O07; governance implementation'),
('VO-11','Build/scope/time evidence','Build1 T-12; evidence tests','Fixture evidence, not production custody','OPEN','Evidence/certification implementation'),
('VO-12','Cumulative transformations','Build1 T-09','Toy envelope, no evolving cognitive entity','OPEN','Development domain'),
('VO-13','Neutrality and endogenous regulation','No direct implementation','Untested interface','OPEN','Endogenous regulation domain'),
('VO-14','Level N certification and claims','Build1 T-01/T-02/T-03/T-10/T-11/T-12','Necessary conditions only, no Level N certification','OPEN','Qualification and certification evaluation')]
with (r/'VO_TRACEABILITY.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['VO','obligation','executed evidence','limitation','formal status','handoff']);w.writerows(rows)
acs=[('AC-01–16','OPEN','Legacy exact-source reconciliation required'),('AC-17–20','OPEN','Per-case oracle mapping not independently established'),('AC-21–22','PARTIAL ROUTING','VO-11; no full AC execution'),('AC-23–24','DEFERRED','VO-09 causal attribution'),('AC-25–29','OPEN','Governance/continuity; exact mapping remains open'),('AC-30–32','PARTIAL ROUTING','Build1 T-06/T-12; VO-10/11'),('AC-33–36','OPEN','Profile/claim exact mapping remains open'),('AC-37–39','PARTIAL ROUTING','Build1 T-02/T-11'),('AC-40–42','DEFERRED','Later realization and qualification')]
with (r/'AC_ROUTING.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['case range','mapping status','notes']);w.writerows(acs)
mut=res['checker_regeneration']['data']
assert len(mut)==4 and mut[0]['counterexample'] is None and all(m['counterexample'] is not None for m in mut[1:]),'Mutation gate failed'
report=f'''# NNNC Phase 1 — Build 4: Consolidated Regression and Traceability

**Baseline:** Architect-accepted P1-D1 v2.0 and P1-D2 v0.2.1.  
**Scope:** Reproduce Builds 1–3, independently regenerate Build 3 mutant counterexamples, reconcile test evidence with all 14 D2 verification obligations, and record open AC routing. No new NNNC mechanisms were developed.

## Execution

| Source suite | Tests executed | Result |
|---|---:|---|
'''
for s in res['suites']:report+=f"| Build {s['build']} | {s['tests']} | {'PASS' if s['passed'] else 'FAIL'} |\n"
report+=f"\n**Total:** {sum(s['tests'] for s in res['suites'])} passing tests; Build 3 checker re-executed and regenerated four variant outputs. These are the existing tests, not 32 independent mathematical properties.\n\n"
report+='| Checker variant | Attempts | Accepted | Witness |\n|---|---:|---:|---|\n'
for m in mut:report+=f"| {m['mutant']} | {m['counts']['attempts']} | {m['counts']['transitions']} | {'None within bound' if m['counterexample'] is None else ', '.join(m['counterexample']['issues'])} |\n"
report+='''
## Evidence and obligation reconciliation

The accompanying `VO_TRACEABILITY.csv` contains one entry per VO-01–VO-14 with executed evidence, limits, formal status and destination. **All 14 remain OPEN**: a passing scenario or bounded model exploration is not by itself a discharged general obligation. No Level N claim, cognitive realization, numerical-identity proof or physical protected-effect safety is established.

`AC_ROUTING.csv` retains the D2 §10 AC-01–42 grouping, distinguishes partial routing from execution, and does **not** invent missing case-by-case oracles. In particular, AC-01–16 and several other exact mappings remain OPEN. Build 5 must carry these forward, not silently mark them complete.

## Phase 0 obligation carry-forward

- **P0-O01** protected-write bypass elimination — OPEN; blocks real protected-effect safety claims.
- **P0-O02** durable journal and crash recovery — OPEN; blocks real protected-effect safety claims.
- **P0-O03** physical-effect idempotency and resource fencing — OPEN; blocks real protected-effect safety claims.
- **P0-O04** independent formal model — OPEN for Phase 0 implementation; Build 3 is an independent *simplified* checker, not its discharge.
- **P0-O05** canonical accounting integration — OPEN.
- **P0-O06** authenticated caller and delegation — OPEN.
- **P0-O07** multi-incident concurrency races — OPEN.
- **P0-O08** checkpoint restoration, branching and identity — OPEN; explicit Phase 2 handoff.

## Build 4 acceptance gate

1. Existing three test suites execute without failures — **PASS**.
2. Independent checker regenerates all three known mutant witnesses and no reference witness within bound — **PASS**.
3. All 14 VOs are individually mapped and honestly marked OPEN — **PASS**.
4. Legacy AC routing gaps and Phase 0 obligations remain visible — **PASS**.
5. No new mechanism or unplanned review expansion — **PASS**.

**Verdict: BUILD 4 ACCEPTED for its bounded integration/traceability objective.** This does not accept or certify the full NNNC architecture as implemented.

## Build 5 handoff and stopping rule

Proceed only to the planned **Build 5 final evaluation and Phase 1 closure report**. Evaluate artifacts against Phase 1's architectural and bounded reference-model gates, preserve the outstanding obligation register and destinations, and stop. Do not add more builds or expand the checker without an explicit new scope decision.

## Reproduction

Run `python run_build4.py` from this folder (Python standard library). Source files under `sources/` are copied verbatim from the archived Build 1–3 packages. `execution_results.json` contains the full test output and SHA-256 hashes for provenance. `generate_report.py` regenerates the report and CSV mappings.
'''
(r/'BUILD4_REPORT.md').write_text(report)
print('Report and mapping created')
