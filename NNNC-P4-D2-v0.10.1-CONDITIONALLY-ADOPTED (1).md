# PROJECT NNNC — PHASE 4 DOCUMENT 2 ADOPTION RECORD

Decision: **P4-AD-2026-10-26-01**  
Authority: **Project Architect, Albert Edward Mc Manus**  
Date: **26 October 2026 (Africa/Johannesburg)**  
Decision: **ACCEPTED AND ADOPTED AT BOUNDED / CONDITIONAL SCOPE**  
Document: **NNNC-P4-D2 v0.10.1**  
Governing D1: **v0.4.2.1 ADOPTED**, P4-AD-2026-10-25-01

Architect instruction: “I move to adopt document 2”. This follows the issued v0.10.1 bounded-acceptance candidate and its explicitly stated adoption scope.

The accepted scope is the Phase4 mathematical reference specification and declared finite verification contract, including the supplied closure review, five targeted repairs and twelve post-repair bounded FV dispositions. The revision remains v0.10.1; recording adoption does not amend normative formulas, source constraints, acceptance gates or test evidence. Candidate SHA-256: `4ea50f516abd2f4f3323a03f41a36d8b4aacc4c04fcb99d108441576efbac168`.

**Preserved conditions:** all sixteen full VOs remain NOT_DISCHARGED (0/16); the full completed-D2 N7 gate remains UNMET. Adoption does not convert bounded checks into universal proof, actual causal realization, deployment safety, qualification, identity or runtime authorization. P0-O01..08, P1 VO01..22, Phase2 PF/PC-VO and other owning registers, Phase3 PAC-2/PA-03 and Phase5/6/7 domain/runtime obligations remain open under their original owners. No nonapplicability or waiver is created.

**Current status:** D1 v0.4.2.1 is ADOPTED; D2 v0.10.1 is BOUNDED / CONDITIONALLY ADOPTED. Phase4 has an adopted architectural and bounded mathematical-reference baseline; full mathematical/implementation verification remains open.

This adoption overlay supersedes only NOT ADOPTED, pending Architect decision and ready-for-consideration status passages of the exact retained candidate. Those passages are historical to issuance. The candidate's substantive restrictions and open obligations remain binding. Earlier review reports and ADOPTION-BINDING.json are historical pre-adoption evidence. CURRENT-ADOPTION.json and this record govern current adoption; FV-RESULTS.json carries the derived current status.

<!-- BEGIN EXACT ADOPTED D2 CANDIDATE -->
# PROJECT NNNC — PHASE 4 DOCUMENT 2

Revision: **v0.10.1 — Bounded post-closure-review correction candidate**  
Date: **26 October 2026 (Africa/Johannesburg)**  
Status: **READY FOR BOUNDED / CONDITIONAL ADOPTION CONSIDERATION — NOT ADOPTED**  
Completed-D2 status: **INCOMPLETE; N7 full gate UNMET; 0/16 full VOs discharged**  
Governing architecture: **D1 v0.4.2.1 ADOPTED, P4-AD-2026-10-25-01; unchanged**  
Predecessors: **P0 v1.4.2/v1.4; P1 v2.3.1/v0.5.1; P2 v1.1.1/v1.1.1; P3 v0.2.7.1/v0.5.3.1**  
Supersedes: **v0.10 as current candidate; exact old issue retained in sources/**

The supplied v0.10 closure review recommended one finding-specific pass, with bounded adoption consideration conditional on correction. This issue records author verification of those corrections, not a new independent review or Architect adoption. N7 and all source protections remain unchanged. Current AC control/status clauses supersede earlier dated pending/status readings; adopted D1 and predecessors control substance.

# Current operative completion-audit supplement — P4-D2 v0.10.1

## AC.0 Authority, scope and exact change map

Governing D1 is **v0.4.2.1, adopted by P4-AD-2026-10-25-01 on 25 October 2026**. The Architect authorized preparation of D2, not its adoption. This issue incorporates one bounded correction pass for the five findings in the supplied v0.10 closure review. Earlier v0.9.1 repairs and adopted D1 remain unchanged. The supplied review accepted finite scope and conditionally recommended bounded adoption consideration after these repairs; new author execution is not a new independent review.

Precedence remains adopted D1 and governing predecessors, then operative N0–N7 (v0.8), then compatible CW clarifications, then this explicit supplement. AC.1 provides qualified normal-form argument lists for source schemata; AC.2 specifies the source correspondence obligations; AC.3/4 supply clause/VO dossiers. These do not waive a governing source constraint. All earlier pending/adoption/status passages in retained sources are historical to their issues. AC.6 supplies the current disposition only. No requirement, invariant, counterexample or VO is removed or renumbered. The previous v0.9.1 candidate is retained exactly in sources/; the exact v0.8 source remains in the reference documents.

The finite kernel is a diagnostic interpretation of a declared subset. A source-typed contract can be specified without deploying its implementation. Conversely a signature or a simulation is not proof of actual correspondence. **World truth, model-relative truth, evidence-relative judgment and runtime authorization remain separate.**

## AC.1 Typed normal form and dependency contract

TYPED-SIGNATURES.json and typed_core.py serialize the many-sorted kernel. W is a realization history, S a candidate system, ER an event referent, X a governed operation, C a context, K a capability, R a realization contract, M a model, E evidence and F a frame. SourceCondition is a finite consistent partial assignment including empty; a source mechanism/group or occurrence set is mapped to it only by an explicit InterpretsSource interpretation. Fin(A) denotes finite subsets; background sets are nonempty when sufficiency is asserted. World, model, evidence and predecessor carriers are never silently identified. Option and Knowledge constructors are not Boolean falsehood.

The signatures spell out parameters that earlier prose held fixed. MinimumOrganization(s,c,w) is the world-explicit section of MinimumOrganization(s,c). CapabilityContinues(k,s,c,s2,c2,w) is similarly world-explicit. OrganizationAssessment(s,k,r,c,f) exposes k, which must equal r's independently validated binding; the native form fixing r's capability is its section. PriorGate(x,h,P,b) exposes the effect envelope and correspondence contract held fixed by the native two-argument notation. These extensions add context parameters, not new authorization or qualification conditions.

The dependency order is:
1. Governing requirements and additional claims determine applicability and required roles independently of outcome/witness.
2. Prior registry/version/context/subject determine operative selection; malformed operative records still count toward uniqueness. Seven-field consistency does not query realization.
3. Actual or explicitly simulated transitions plus independently specified attribution and comparison semantics determine relevant participation.
4. An independently fixed target determines substantive success.
5. Applicability, unique well-formed coverage, roles, consequential participation, substantive success and applicable inherited conditions jointly define capability realization.
6. Qualified observations/protocols determine assessment; assessment never defines world truth or applicability.

The serialized capability and floor definitions are exactly these conjunctions. Sufficient requires nonempty admissible backgrounds, a defined admissible intervention and all declared background outcomes. MinimalSufficient additionally requires every proper subcondition, including empty, to fail sufficiency. ContractWellFormed is declared-binding consistency plus all seven field checks. AllRequiredImportsEstablished is true only for the complete independently determined applicable import call set with actual strict-prior arguments and established source truth; it is never an uninterpreted permissive flag.

Source-contract parameters retain explicit denotations and limits:

| Parameter family | Required interpretation | Positive-use restriction |
|---|---|---|
| RequiredRoles / Applicable | adopted required domains plus additional claims, independent of submitted realization | absence of a domain interpretation cannot remove its requirement |
| OperativeContractFor / UniqueCoverage | independently governed active context/version/subject/capability selection | absent, malformed or ambiguous coverage cannot certify or refute mechanism realization |
| SevenFieldsConsistent | REQ-035(a)–(g), typed endpoints, capability/context consistency, external boundaries and comparison assumptions | syntax alone establishes neither physical mechanisms nor authority |
| Role realization | state mediation; retained consequential memory; combining/constraining/altering coordination; regulator disposition; distinct-occurrence feedback | capability-specific participation, not graph membership or unrelated activity |
| Attribution / InterpretsSource | named source kind, target, background, permitted comparisons, model/world mapping and relevant redundancy/joint/compensation/preemption treatment | unknown or unimplemented semantics gives UNDETERMINED; no default physical actual-cause predicate |
| SubstantiveSuccess | target fixed independently of candidate outcomes | output fit cannot substitute for internal role participation |
| AbstractionAdequate | purpose, context/intervention/observable domain and preservation/failure criteria | predictive adequacy cannot establish intervention or mechanism adequacy |
| InheritedConditions / PriorGate | complete applicable native constraints and actual source correspondence | missing/unknown/denied material input cannot yield positive dependent certification |
| Witness evidence | exact subject/build/world/version/scope, valid observation interval, protocol and adequate independent provenance | candidate assertions or fabricated observer independence cannot certify an actual system |

The checker checks its serialized definitions and uses, detects cycles and rejects wrong arity, cross-sort equality/calls and undeclared symbols. **It is not a Lean/Coq/TLA+ proof, a parser/typechecker of all retained prose, or proof of imported semantics.** The qualified signature table and source audit are the review material for the wider use-site audit. Claims outside the translated kernel are explicitly subject to source-level independent inspection; they are not silently labeled machine-checked.

## AC.2 Source-level predecessor correspondence

IMPORT-AUDIT.md/JSON specify exact current source anchors and semantic constraints, not merely function names. Each record binds the source hash, anchor, source-native arguments, required preservation and remaining assurance owner. The bridge preserves fifteen actual operation fields, including instance/build/target, originator/executor/delegation, all direct and indirect effects and scopes, prior policy/session, strict history prefix, rule version and lifecycle context/flag.

P0.May uses the trusted AuthCtx and actual envelope's kind/target projections against the version-consistent canonical prestate. P1.PriorValidAuth and EffectiveGovernance preserve prior approval/execution/P0 authorization and source history semantics. P3.GeneralConstitutionallyAuthorized retains all seven II.1 conjuncts, including complete governing scope bases and the actual prior principal/state. Every applicable P2.AuthorizedTransition call preserves occurrence, real locus, history and rule version. A non-lifecycle act needs no fictitious locus. A lifecycle flag, context or indirect effect cannot bypass the lifecycle dispatch. Illicit actual effects can be represented without inventing valid authority.

Formally, for independently established required call inventory Calls(x,h,P,b), PriorGate means that this inventory is complete for the actual operation and every call's native predicate holds with its source-preserving strict-prior tuple. If the inventory or mapping is unknown, the evidence-relative assessment is undetermined; an empty inventory is not a substitute for missing knowledge. An established source denial blocks the protected assessment. Post-hoc coverage enlargement or a new grant cannot authorize a past effect.

Source P3 GX/GH/GG/PRINC are its explicitly declared native P1 aliases. P2 X/H/O/I/L/V and P0 registered instance/operation/envelope remain separate carriers. P2's coarse AuthorizedProtected(GOV,V) is not an operation-level substitute. No new globally typed Recon interface is invented. P2 PC.5 E-1 text is current; its universal custody/effect assurance is still open. P1 unity and eighteen mandatory slots remain cumulative; no local causal or enactment witness confers Level N or identity.

bridge_contract.py tests the declared nominal mapping with **stipulated imported evidence**. It does not authenticate that evidence or implement the imported predicates. effect_bridge.py separately exercises the adopted finite P3 guard and exact P2 callback shape. Every output retains runtime_authorization=NOT_ESTABLISHED. These fixtures support inspection of the wrapper contract, not a deployed refinement proof. P3 PAC-2 and all other inherited obligations remain open on their owning registers.

## AC.3 Clause-by-clause verification dossier

CLAUSE-AUDIT.json preserves all 109 governing identities with primary source paragraphs, explicit requirement subtargets and full supplemental blocks. The added subitems are audit references, not new architectural requirements. Each source identity has an assessable author interpretation, positive obligation, distinguishing failure, named controls, exact residual and explicit nondischarge status. CLAUSE-LEVEL-AUDIT.md is the readable crosswalk.

Paragraph decomposition and manual semantic targets are **not** a proof of complete logical decomposition. Supplemental paragraphs containing formulas or normative qualifiers are retained for direct reviewer inspection. Their parent controls do not automatically verify every subclause. The old TESTED=False/DISCHARGED=False whole-identity flags remain valid even where selected controls execute successfully. Source-generated identifier counts cannot establish semantic adequacy.

The new controls add real disconfirmation, stale/future/conflicting evidence checks, immutable history under model revision, append-and-reference reassessment, explicit competing-regulator combination and unresolved-conflict behavior, a redundant stateful mechanism and source-preserving nominal import mutations. Preemptive/stochastic actual attribution is not fabricated; absent named semantics gives UNDETERMINED. The finite distribution contrast example compares model distributions only, not physical causation or calibrated empirical confidence.

## AC.4 VO-specific acceptance proposals and deferred owners

VO-CLOSURE-DOSSIER.json supplies sixteen separate records. Each links governing source subitems, a positive/negative AU control, existing CA controls, method/bounds, residuals, acceptance criterion and result files. The proposal for each is SUBMITTED_FOR_INDEPENDENT_CONFIRMATION. **All sixteen full VO statuses remain NOT_DISCHARGED.** No authorized nonapplicability decision is invented.

A reviewer must establish whether a named bounded result satisfies the source obligation at its required scope; accepting a finite subproperty is not a full VO discharge. Later-domain implementations, empirical causal discovery and deployment enforcement remain deferred where D1 assigns them. Source typing/correspondence and mandatory semantic coverage are present-phase closure tasks and are not relabeled as later implementation to evade N7.

P0-O01–08, P1 VO01–22, P2 PF/VO/C/O/PC-VO, P3 PAC-2 and deferred PA-03 remain tracked. No owner or authority is reassigned. No consciousness, cognition or safe physical effect is inferred from this package.

## AC.5 Bounded disposition and stopping rule

The supplied v0.10 closure review is received. Its five concrete findings define this single v0.10.1 pass; all previous accepted finite properties are retained. No new general architecture review or requirement for later deployed FFNN/SA/NES mechanisms is introduced. The records separate the review's conditional recommendation from author verification of the repairs. Targeted confirmation is confined to those repairs and any concrete counterexample they expose.

The completed-D2 N7 gate is unchanged: all twelve FV PASS, no mandatory completion blocker, VO-specific justified discharge or authorized nonapplicability and separate Architect adoption. Bounded/conditional adoption consideration is a different disposition: the declared finite specification and controls may be adopted with explicit retained residuals. It cannot be renamed completed-D2 adoption, full VO discharge or deployed assurance. This issue does not adopt D2.

## AC.6 Current status — v0.10.1

**D1 v0.4.2.1 remains ADOPTED. D2 v0.10.1 is NOT ADOPTED; ready for BOUNDED / CONDITIONAL adoption consideration at the supplied review's declared finite scope, subject to finding-specific confirmation.** All twelve FV checks are post-repair bounded PASS under that recommendation; this is not a new independent full-scope proof. The full completed-D2 gate remains UNMET, all sixteen full VOs remain NOT_DISCHARGED and inherited obligations remain open.

## AC.6.1 Five repairs and exact interpretation

1. Supplement count and supplement list use distinct keys. Builders interpolate the integer count only. No raw Python dictionary presentation is part of the current normative document or report.
2. The operative registry now includes the ten listed missing P4 symbols and two callable P2 imports. P0.Support and P3.Provenance are audit topic labels, not source-published functions; they are classified in SOURCE-CONTRACT-TOPICS.json and the import coverage register. No new authorization predicate or global source function is invented.
3. For structurally bound, independently selected applicable calls, conjunction evaluates all required truth values. Any established FALSE yields DENIED, even if another call is missing/unknown. With no FALSE, a missing/unknown/ambiguous/malformed call yields UNDETERMINED. Invalid correspondence itself remains undetermined, not an established denial about the candidate. AuthCtx fixture components are an ordered tuple; duplicate lifecycle links are rejected.
4. Operation declarations carry a complete finite lifecycle-locus inventory, unioned over every reachable call. Supplied LifecycleCall records must cover exactly that inventory, with no missing, extra or duplicate locus. The single-locus legacy grammar denotes the one native event locus. Every selected callback and per-locus native P3 finite guard is checked; a valid denial dominates unknown. An arbitrary tuple does not prove the inventory complete in a real program.
5. The ledger/audit source is the current adopted D1 v0.4.2.1. DEF-P4-016 and AM-P4-CW-01..04 are explicitly indexed as governing supplements without changing the stable 109 identity inventory. ENABLING/INHIBITING queries require the actual and both counterfactual assignments to belong to the declared admissible background set, otherwise return None (unresolved).

## AC.6.2 Missing-symbol sections and source-topic discipline

ActualConcurrent(w,a,b) retains N1's realized endpoints, complete relevant actual order and absence of either precedence; it is not OrderAssessment. ApplicableCapabilities(s,c) is the required-plus-claimed set, a finite registry value only in the declared finite profile; a truncated unknown set cannot waive mandatory coverage. CapabilityOrganization(s,k,r,c,w) requires the uniquely bound well-formed contract, required-role realization and relevant internal participation; it does not assert substantive success. SatisfiesOrganization(s,k,r,c,w) is CapabilityRealized with k fixed by the validated contract, the explicit-capability section of the native (s,r,c,w) notation. Neither alias changes Phase1 whole qualification.

MemoryRealized and CoordinationRealized denote capability-relative consequential retained state and combining/constraining/altering respectively, distinct from the corresponding required system-floor aggregates. Their independent finite interpretations remain the memory and coordination trace witnesses, not output success or labels. Outcome(mu,z,c) applies to an admissible intervened state z; an undefined intervention supplies no such state. AdmissibleComparisons names the fixed model/source/context comparison domain. CoverageFailure is the native prior-envelope versus recorded-effects condition. AbstractionMap returns Some(map) only for a declared correspondence on the requested domain; absence is None, not a default equivalence.

P2.CustodyBearing is source PC.5 with the formerly subscripted history explicit, typed P2.X×P2.L×P2.H×P2.V→Bool. P2.Judge retains its native claim and finite evidence-view arguments, typed P2.NativeIdentityClaim×Fin(P2.Q)→P2.Verdict; its three outcomes are unchanged. P0.Support identifies P0-SUP-01..08's normative contract and P3.Provenance identifies the source material-control/provenance constraints; neither label is callable. PA-03 is the deferred same-principal separation proposal, not the name of a material-control lookup registry. Source obligations retain their own authority and scope.

## AC.7 Qualified callable signature register

Parameters require their source-bound interpretation, not assumed truth. World and capability arguments held fixed by native section notation are explicit. Source-contract topic labels are separately classified below.

| Symbol | Arguments → result | Source / kind |
|---|---|---|
| Occurs | W × ER → Bool | P4 N1 / D1 DEF001 / parameter |
| Reports | E × ER → Bool | P4 D1 5B.3 / parameter |
| ActualPrecedes | W × ER × ER → Bool | P4 N1 / parameter |
| ModelPrecedes | M × ER × ER × C → Bool | P4 N1 / parameter |
| OrderAssessment | F × ER × ER → OrderVerdict | P4 N1 / parameter |
| OrderCompleteness | W × Domain × Interpretation × Provenance → Bool | P4 N1 / parameter |
| Applicable | K × S × C → Bool | P4 N2 / parameter |
| RequiredRoles | K × S × C → Fin(Role) | P4 N2 / parameter |
| OperativeContractFor | R × K × S × C → Bool | P4 N2 / parameter |
| ContractWellFormed | R × K × C → Bool | P4 N2 / definition |
| UniqueCoverage | S × K × R × C → Bool | P4 N2 / parameter |
| RelevantInternalOrganization | S × K × R × C × W → Bool | P4 N2 / parameter |
| SubstantiveSuccess | S × K × C × W → Bool | P4 N2 / parameter |
| InheritedConditions | S × K × C × W → Bool | P4 N2/N5 / parameter |
| RequiredRolesRealized | S × K × R × C × W → Bool | P4 N2 / parameter |
| StateMediated | S × C × W → Bool | D1 5B.1 / parameter |
| RegulationRealized | S × C × W → Bool | D1 5B.1 / parameter |
| FeedbackRealized | S × C × W → Bool | D1 5B.1 / parameter |
| RequiredMemoryRolesRealized | S × C × W → Bool | D1 5B.1 / parameter |
| RequiredCoordinationRealized | S × C × W → Bool | D1 5B.1 / parameter |
| Sufficient | M × SourceCondition × Outcome × C × Backgrounds × Intervention → Bool | P4 N3 / definition |
| MinimalSufficient | M × SourceCondition × Outcome × C × Backgrounds × Intervention → Bool | P4 N3 / definition |
| ActualContribution | Attribution × M × SourceCondition × Outcome × W × C → Bool | P4 N3 / parameter |
| ModelContribution | M × S × SourceCondition × Target × C → Bool | D1 5B.1 / parameter |
| RealizedContribution | Attribution × M × S × SourceCondition × Outcome × W × C → Bool | D1 5B.1 / parameter |
| EvidenceContributionAssessment | S × SourceCondition × Outcome × F → Assessment | D1 5B.1 / parameter |
| EffectAnalysis | X × PreHistory → EffectResult | D1 5B.3 / parameter |
| ActualEffects | X × History → ActualEffectResult | D1 5B.3 / parameter |
| RequiredScopes | Fin(Eff) → Fin(P3.Scope) | D1 5B.3 / predecessor-owned / parameter |
| CoverageSound | X × PreHistory × Fin(Eff) × Assumptions → Bool | D1 5B.3 / parameter |
| AssumptionsApplicable | Assumptions × C × AssuranceLevel → Bool | D1 5B.3 / parameter |
| CoverageEstablished | X × PreHistory × Fin(Eff) × Assumptions × AssuranceLevel × F → Bool | D1 5B.3 / parameter |
| PriorGate | X × PreHistory × Fin(Eff) × Bridge → Bool | P4 N5 / Audit AC3 / definition |
| ProtectedExecutionAssessment | X × PreHistory × F → Assessment | D1 5B.3 / parameter |
| OccurrenceAssessment | ER × F → Assessment | D1 5B.3 / parameter |
| LocusInfo | ER × F → Knowledge(L) | P4 1 / parameter |
| PlacementInfo | ER × F → Knowledge(T) | P4 1 / parameter |
| OrganizationAssessment | S × K × R × C × F → Assessment | D1 5B.1 / explicit k binding / parameter |
| EvidenceSupportsCapability | S × K × R × C × F → Bool | P4 5 / parameter |
| CapabilityContinues | K × S × C × S × C × W → Bool | D1 5B.1 / explicit world parameter / parameter |
| AbstractionAdequate | Map × Claim × Domain → Bool | D1 REQ027 / parameter |
| ModelRevision | M × M × History → Bool | P4 6 / parameter |
| MechanismChange | X × History × History → Bool | P4 6 / parameter |
| CompatibleModels | F → Fin(M) | P4 7C / parameter |
| Identified | F × Query → Bool | P4 7C / parameter |
| P0.May | P0.AuthCtx × P0.OperationKind × P0.Target × P0.Sigma → Bool | P0 D2 I4 + operative authorization-view paragraph / parameter |
| P1.PriorValidAuth | P1.X × P1.Gamma → Bool | P1 D2 4 / parameter |
| P1.EffectiveGovernance | P1.H × P1.X → Option(P1.Gamma) | P1 D2 4 / parameter |
| P1.LevelNConforms | P1.I × P1.Profile × P1.Time → Bool | P1 D2 3 + CU / parameter |
| P1.CUAssess | P1.I × P1.CUContract × P1.E × P1.Obs → P1.Decision | P1 D2 CU3 / parameter |
| P2.AuthorizedTransition | P2.X × P2.L × P2.H × P2.V → Bool | P2 D2 3 + PC7 / parameter |
| P2.AuthorizedCustodyStep | P2.X × P2.K × P2.K × P2.L × P2.H × P2.V → Bool | P2 D2 3 / parameter |
| P2.ValidLocusAuthority | P2.X × P2.L × P2.H × P2.V → Bool | P2 D2 3 / parameter |
| P2.InvariantOK | P2.X × P2.H × P2.V → Bool | P2 D2 3 / parameter |
| P3.GeneralConstitutionallyAuthorized | P1.X × P1.Gamma × P1.A × P1.H × Fin(P3.Basis) → Bool | P3 D2 II1 / parameter |
| P3.PreGov | P1.X × P1.H → Option(P1.Gamma) | P3 D2 I4 / parameter |
| BindingHolds | S × BuildRef × K × C × R × W → Bool | D1 AM-CW01 / parameter |
| TraceSeams | W → Bool | D1 AM-CW02 / parameter |
| WitnessEvidenceQualified | Witness × F → Bool | D1 AM-CW03 / parameter |
| WitnessSupports | Witness × F → Bool | D1 DEF016 / parameter |
| Influences | M × SourceCondition × Target × C → Bool | N3 / D1 DEF002 / parameter |
| InterpretsSource | SourceReferent × SourceCondition × Interpretation → Bool | N3 / parameter |
| ProperSubconditions | SourceCondition → Fin(SourceCondition) | N3 includes empty condition / parameter |
| NonemptyBackgrounds | Backgrounds → Bool | N3 / parameter |
| AdmissibleComparison | M × SourceCondition × C × Backgrounds × Intervention → Bool | N3 / parameter |
| AllBackgroundOutcomes | M × SourceCondition × Outcome × C × Backgrounds × Intervention → Bool | N3 / parameter |
| AllProperSubconditionsFail | M × SourceCondition × Outcome × C × Backgrounds × Intervention → Bool | N3 / parameter |
| EvidenceQualified | S × BuildRef × K × C × F → Bool | D1 AM-CW03 / parameter |
| AllRequiredImportsEstablished | X × PreHistory × Fin(Eff) × Bridge → Bool | N5 / parameter |
| SevenFieldsConsistent | R × K × C → Bool | REQ035(a)-(g) / parameter |
| DeclaredBindingConsistent | R × K × C → Bool | N2 / parameter |
| ActualConcurrent | W × ER × ER → Bool | D2 N1: realized endpoints, complete relevant actual order and neither precedence direction / parameter |
| SatisfiesOrganization | S × K × R × C × W → Bool | D1 5B.1: native (s,r,c,w) section with k fixed by validated r binding / definition |
| CapabilityOrganization | S × K × R × C × W → Bool | D1 5B.1 / N2: organization only, without substantive-success inference / definition |
| MemoryRealized | S × K × R × C × W → Bool | D1 5B.1 / REQ036: capability-relative consequential retained state / parameter |
| CoordinationRealized | S × K × R × C × W → Bool | D1 5B.1 / REQ037: capability-relative combining/constraining/altering / parameter |
| ApplicableCapabilities | S × C → Fin(K) | D1 5B.1 / N2: required union claimed; finite registry profile, not arbitrary truncation / parameter |
| Outcome | M × AdmissibleState × C → Outcome | D1 5B.1 / N3: outcome on an admitted intervened state; undefined intervention has no such state / parameter |
| AdmissibleComparisons | M × SourceCondition × C → Fin(Intervention) | D1 5B.1: fixed model/source/context comparison domain / parameter |
| CoverageFailure | X × History → Bool | D1 5B.3: recorded actual effect outside prior admitted envelope / parameter |
| AbstractionMap | Domain × Domain × Domain → Option(Map) | D2 6: explicit declared correspondence; missing map is None / parameter |
| P2.CustodyBearing | P2.X × P2.L × P2.H × P2.V → Bool | P2 PC5: CustodyBearing_h(z,l,v), history explicit, unchanged custody/effect clause / parameter |
| P2.Judge | P2.NativeIdentityClaim × Fin(P2.Q) → P2.Verdict | P2 PC3: exact three-valued rule-relative public Judge(k,qbar) / parameter |
| CapabilityRealized | S × K × R × C × W → Bool | P4 AC1 normal form / definition |
| MinimumOrganization | S × C × W → Bool | P4 AC1 normal form / definition |

| Source-topic label | Governing contract | Classification |
|---|---|---|
| P0.Support | P0-D1 10.6–10.13, P0-SUP-01..08 | Noncallable source-contract topic; no invented function signature |
| P3.Provenance | P3 material-control/provenance requirements and REQ-P3-045 lexical precedence | Noncallable source-contract topic; no invented function signature |

## AC.8 Current finite evidence and gate record

Existing reference suite: **20 groups / 207 assertions PASS**. Completion suite: **18 groups / 253 assertions PASS**. Targeted repair suite: **5 groups / 1425 assertions PASS**. Historical144 diagnostics remain separately reported. Counts are finite checks, not independent physical trials or universal proofs.

Typed kernel: **85 callable declarations / 8 serialized bodies / 24 call sites**; two noncallable source topics are classified separately. Clause dossier: **109 identities / 347 primary audit items / 64 supplements**. The adopted witness definition and all four AM-P4-CW clauses are included. No raw source dictionary is interpolated here.

| Gate | Bounded post-repair disposition | Evidence |
|---|---|---|
| FV-01 | PASS | Separate numeric/list keys; exact adopted/source retention; no current raw-source dump |
| FV-02 | PASS | Well-foundedness axiom, finite controls and explicit integer countermodel |
| FV-03 | PASS | Actual/model/evidence separation and warranted concurrency |
| FV-04 | PASS | Four coverage cases and all seven field checks |
| FV-05 | PASS | Corrected callable/topic inventory, explicit sections and acyclic typed kernel |
| FV-06 | PASS | Constructive, redundant, regulator and disconnected-role controls |
| FV-07 | PASS | Empty-subset minimality and admitted actual/lo/hi role backgrounds |
| FV-08 | PASS | Denial-dominant conjunction, collision-free tuple context, unique complete multilocus calls |
| FV-09 | PASS | Current adopted D1 clauses and witness supplements in source/VO dossiers |
| FV-10 | PASS | Reproducible manifest and historical migration; actual package checks reported separately |
| FV-11 | PASS | All OPEN/DEFER/inherited registers retained; full VO discharge0/16 |
| FV-12 | PASS | Bounded acceptance consideration distinct from full completion/adoption/runtime authority |

These are post-repair bounded dispositions under the supplied review's conditional recommendation and author execution. They are not a new independent reviewer result for changed bytes. Finding-specific confirmation remains applicable. The completed-D2 N7 gate is NOT satisfied by twelve bounded checks alone: full VO decisions and a separate Architect adoption are absent. No full VO is silently reclassified.

| VO | Current finite scope | Full status |
|---|---|---|
| P4-VO-01 | Occurrence and incomplete knowledge; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-02 | Correlation/influence/common causes; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-03 | Order/concurrency/unknown order; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-04 | Delay and absent ACK; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-05 | Feedback and well-founded history; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-06 | Evidence/provenance/independent challenge; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-07 | Causal ancestry versus identity; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-08 | Strict-prior effect/authorization bridge; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-09 | NNNC/NES/external boundary; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-10 | Model revision without history rewrite; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-11 | Intervention versus predictive success; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-12 | Abstraction and emergence; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-13 | Simulation and actual computation effects; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-14 | Scoped roles/redundancy/attribution; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-15 | Identification with competing models; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |
| P4-VO-16 | Positive organization/capability realization; accepted or conditionally accepted finite scope in supplied v0.10 review; current repair evidence attached | NOT_DISCHARGED |

# Retained reference candidate — exact v0.9.1 bytes

N0–N7 remain controlling as specified above; dated status/evidence statements in this retained material refer to their issues. The exact v0.10 issue, including its reported formatting defect, is separately archived in sources/ and is not current operative text.

<!-- BEGIN EXACT P4 D2 v0.9.1 SOURCE -->
# PROJECT NNNC — PHASE 4 — DOCUMENT 2

Revision: **v0.9.1 — Current predecessor alignment and positive causal-realization witness**  
Issue date: **25 October 2026**  
Status: **INCOMPLETE / LIMITED-SCOPE MATHEMATICAL REVIEW CANDIDATE — NOT ADOPTED**  
Companion: **P4-D1 v0.4.2.1**  
Current predecessors: **adopted P0 v1.4.2/v1.4; P1 v2.3.1/v0.5.1; P2 v1.1.1/v1.1.1; P3 v0.2.7.1/v0.5.3.1**  

The supplied baseline follows exactly. Historical adoption, candidate and test statuses describe their respective issues. The explicit current CW amendment follows that baseline and controls only its named changes and limited formal definitions. Existing D1 adoption is preserved; no new adoption, completed-D2 status or VO discharge is claimed. D2 v0.8 N7's completed-D2 gate is retained.

# Part I — Exact supplied source

<!-- BEGIN EXACT P4 SOURCE -->
# PROJECT NNNC — PHASE 4 DOCUMENT 2
## v0.8 — Bounded Post-Review Correction Candidate

| Control | Disposition |
|---|---|
| Governing baseline | NNNC-P4-D1 v0.4.1 ADOPTED, unchanged |
| Revision authority | Architect approved incorporation of AM-P4-D2-07-01..06 on 24 October 2026 |
| Supersedes | v0.7 as current D2 candidate only; v0.7 frozen verbatim in historical appendix |
| Status | INCOMPLETE CORRECTION CANDIDATE; NOT ADOPTED; NOT VERIFIED |
| Independent review | 11 sustained findings (6 Moderate, 5 Minor), as reported by revisionist adjudication |
| VO discharge | 0/16; no change authorized without affirmative evidence |
| Verification | FV-01..12 specified; execution/review not yet completed |

**Controlling interpretation and incorporation (VC-P4-D2-08).** Sections N0–N8 below are the **operative v0.8 corrections** and supersede inconsistent or less precise language in the historical v0.7 material, which is preserved verbatim after the explicit `HISTORICAL NONOPERATIVE BASELINE` marker. All unconflicted v0.7 definitions remain provisional candidate clauses, not accepted architecture. No section of the historical appendix overrides N0–N8. This arrangement is a documented interim consolidation, **not** a claim that every historical clause has been individually rewritten. Exact historical targets and replacements are recorded in the amendment register. P4-D1 and authoritative predecessor contracts control any conflict. The complete v0.7-to-v0.8 diff accompanies this document.

## N0. Governing semantics, assessment layers and authority [AM-06]

The governing mathematical contract is the expressly designated typed definitions, axioms, invariants, imported interfaces and verification obligations in this candidate, subject to the adopted D1 and authoritative predecessor restrictions. `WorldTruth`, `ModelTruth` and `EvidenceAssessment` are distinct sorts. No inference from the latter two to the first is valid without a separately stated, justified bridge. An executable reference interpretation, including historical §15 and its `p4d2_v07_transition_model.py`, is **diagnostic**, not normative; its successful tests neither establish implementation conformance nor authorize protected effects. Any future normative designation requires separately reviewed conformance evidence. A runtime bridge is not deployed enforcement absent independent evidence. Omitted mandatory semantics SHALL be registered as limitations; tests omitting them SHALL NOT discharge their obligations.

## N1. Occurrence ordering and knowledge [AM-01; replaces §2, clarifies §§7B,13.1]

Let `Realized(w)={e∈ER | Occurs(w,e)}`. `ActualPrecedes_w ⊆ Realized(w)×Realized(w)` is irreflexive and transitive. **Every admissible complete realized history SHALL have a well-founded `ActualPrecedes_w`**: every nonempty subset of `Realized(w)` has an element with no predecessor within that subset. This is a governing semantic axiom, **not** a theorem proved by finite exploration. A complete infinite history indexed by integers with `e_(n-1) ActualPrecedes e_n` for every integer n is acyclic but non-well-founded and inadmissible. A finite prefix asserted as realized SHALL obey inherited predecessor constraints and applicable occurrence constraints; passing finite-prefix checks does not establish well-foundedness of an unrestricted infinite completion. An evidence projection is not a complete realized history.

`ModelPrecedes(μ,e1,e2,c)` is a model-relative assertion. `OrderAssessment(f,e1,e2)` is evidence-relative, with values BEFORE, AFTER, CONCURRENT, UNKNOWN. Neither is definitionally equal to `ActualPrecedes`. `OrderCompleteness(w,D,κ,provenance)` requires a named occurrence domain/pair/region `D`, interpretation `κ`, and an independently justified completeness warrant `provenance`; caller-supplied `true` is insufficient. `ActualConcurrent_w(a,b)` requires realized a,b, a warranted complete relevant order, and neither precedence direction. Incomplete identical observations may be compatible both with precedence and with concurrency, and therefore produce UNKNOWN. Abstract recurrent model edges may be cyclic only when instantiated as distinct concrete occurrences obeying the well-founded realized relation.

**Required discrimination:** valid finite partial order; integer-indexed infinite descending-predecessor countermodel; same incomplete evidence compatible with two concrete histories; valid recurrent abstract dynamics instantiated as distinct concrete occurrences. The infinite case is a mathematical countermodel, not an exhaustive machine test.

## N2. Operative contracts, noncircularity and realization [AM-02; replaces §§5,7A,14,15 where conflicting]

Let `S,C,K,R` be disjoint sorts. `Applicable(k,s,c)` is independently determined from adopted required capabilities and candidate claims, without querying contract validity, organization satisfaction, observed success or assessment. `RequiredRoles(k,s,c)` is likewise imported from governing requirements. `OperativeContractFor(r,k,s,c)` is determined solely by declared contract version, active status, context, system and capability binding, and unambiguous selection rules; inactive, historical and context-distinct records are permitted but not counted as operative. `ContractWellFormed(r,k,c)` independently validates all seven existing §7A fields and their typed consistency without querying realization or evidence. Governing coverage is:

```math
\forall s\in S\;\forall c\in C\;\forall k\in K:\quad
Applicable(k,s,c)\Rightarrow\exists r\in R\bigl(
OperativeContractFor(r,k,s,c)\land ContractWellFormed(r,k,c)\land
\forall r'\in R(OperativeContractFor(r',k,s,c)\Rightarrow r'=r)\bigr).
```

No operative contract, a sole malformed operative contract, or two distinct operative contracts each **fails**. Exactly one well-formed operative contract passes this *coverage* condition only; coverage alone is not realization.

`RelevantInternalOrganization(s,k,r,c,w)` is interpreted from realized mechanisms, state transitions and causal relationships using an independently declared attribution rule. `SubstantiveSuccess(s,k,c,w)` uses success criteria fixed independently of candidate outcomes. `CapabilityRealized(s,k,r,c,w)` requires applicability, unique operative well-formed contract, required roles, relevant consequential internal participation, substantive success and every applicable inherited condition. Both participation and success are necessary; together they are sufficient **only if all other stated conjuncts hold**. Evidence assessment follows, never defines, world-level realization. The separate system-level `MinimumOrganization` floor from §5 is preserved. A capability without a capability-specific memory role is not thereby rejected; applicable system-level memory obligations remain.

**Typed dependency order:** predecessor obligations/candidate claims → Applicable/RequiredRoles; declarations/version/context → OperativeContractFor; seven-field syntax/consistency → ContractWellFormed; realized transition semantics + attribution assumptions → RelevantInternalOrganization; independent target contract → SubstantiveSuccess; conjunction + inherited conditions → CapabilityRealized; independent provenance/observations → EvidenceAssessment. None of these arrows is reversed. Unknown predecessor inputs remain unknown and prohibit dependent positive certification.

## N3. Source conditions, sufficiency and contribution [AM-03; replaces §3, refines §7C]

`CausalVariable`, `Value`, `MechanismId` and `Occurrence` are distinct sorts. `SourceCondition` is a **finite consistent partial assignment** from causal variables to values (including the empty assignment). `MechanismGroup` and `OccurrenceSet` are separate sorts, related to conditions only by an explicit interpretation map `InterpretsSource`. For deterministic model μ, admissible nonempty background set B, admissible well-defined intervention/comparison I, outcome y and context c:

```math
Sufficient_{\mu,B,I}(A,y,c)\iff B\neq\varnothing\land
\forall b\in B:\ Outcome_{\mu}(I(A,b),c)\equiv_y y.
MinimalSufficient_{\mu,B,I}(A,y,c)\iff
Sufficient_{\mu,B,I}(A,y,c)\land
\forall A'\subsetneq A:\neg Sufficient_{\mu,B,I}(A',y,c).
```

Compatibility of A and b, background admissibility and intervention legality must be declared; an undefined intervention cannot satisfy the schema. **The empty proper subassignment is tested.** `ActualContribution(α,μ,A,y,w,c)` requires a named attribution rule α, admissible comparison, realized-history correspondence and identified source type; group redundancy does not entail each member's necessity. Preemption, stochastic attribution and cases without admissible interventions remain OPEN unless separately specified; positive toy contrasts cannot fill these gaps. Observational equivalence is not causal identification.

## N4. Evidence ledger, migration and discharge [AM-04]

The **109 governing identities** (40 REQ, 12 INV, 36 CE, 16 P4-VO, five P4-VO-16-NC) remain stable; derived records may be added with new identifiers but are not additional D1 obligations. For each identity separately track `INVENTORIED`, `SPECIFIED`, `TESTED`, `INDEPENDENTLY_REVIEWED`, `DISCHARGED`, with explicit evidence and scope. A test pass is not a VO discharge. All 16 VO statuses start `NOT_DISCHARGED`; a change requires an inspectable claim-specific criterion, evidence and authorized decision. The companion v0.8 ledger preserves the original source excerpt and OPEN fields without disguising them as specifications. Historical test migration must identify the semantic property, its replacement or residual, equivalence/strength argument and executed evidence where claimed; **no numeric parity requirement** and no silent coverage loss. `PASS` is not permitted without an independent oracle.

## N5. Predecessor imports and fail-closed conclusions [AM-05]

Every imported predicate retains its authoritative name, typed argument signature, source anchor, version, assumptions, scope and owner. In particular `P2.AuthorizedTransition(x₂,l,h₂,v)` remains four-argument and is not replaced by a Phase 4 Boolean; Phase 3 constitutional restrictions remain additional. Unresolved imports may remain **uninterpreted** in mathematical models but never be assigned permissive truth to certify identity, continuity, qualification, authorization or protected execution. Denied, unresolved or malformed predecessor-governed inputs cannot produce a positive dependent conclusion. Conflicts with authoritative predecessors are registered with source anchors, affected predicates, consequence, owner and architect decision required; the predecessor controls pending resolution. Unrelated properties may be tested with their bounded scope intact. Phase 0 protected-effect implementation blockers P0-O01–03 remain open and block deployed safety assurance; Phase 1, Phase 2, Phase 3 imports and PAC-2 retain their original owners and status. No silent ownership transfer or waiver.

## N6. Incorporation, supersession and residual governance [AM-06, VC-P4-D2-08]

This v0.8 is one bounded authorized correction pass. `AM-P4-D2-07-01..06` are approved for incorporation, **not deemed verified**. Exact target map: AM-01 §§2/7B/13.1 → N1; AM-02 §§5/7A/14/15 → N2; AM-03 §§3/7C → N3; AM-04 §§7/10/11/13–15 → N4; AM-05 §§4/7F/12/15.4 → N5; AM-06 control/§§7D/8/11/13–15 → N0,N6–N8. The frozen v0.7 text is retained verbatim below, clearly historical; its inconsistent formulas are superseded, not concurrently operative. The diff and SHA-256 manifest provide source provenance. No REQ, INV, CE, VO or OPEN-D2 identifier is renumbered.

**OPEN-D2 crosswalk:** 01→AM-02/05 (seven-field contract); 02→AM-04/06 (semantic crosswalk); 03→AM-01/02/03/04 (reference semantics); 04→AM-05/02 (predecessors); 05→AM-03/04 (attribution); 06→AM-01 (order); 07→AM-01/03/04 (abstraction/evidence); 08→AM-06/04/05 (closure). Each remains OPEN unless separately evidenced and authorized. Five inherited categories: Phase 0 engineering/safety; Phase 1 ontology/qualification; Phase 2 identity/continuity; Phase 3 constitutional authority; Phase 4 causal verification. Unresolved items have original owners pending a documented owner confirmation; no newly invented discharge.

## N7. Focused verification protocol — FV-01..12

Each check must receive PASS, FAIL or BLOCKED with evidence; no inference from draft text to executed result. The following are the acceptance oracles, not assertions of completion:

| Check | Required PASS evidence |
|---|---|
| FV-01 | Full source diff and exact amendment/supersession anchors; no unaccounted normative change or conflicting operative clause |
| FV-02 | Well-foundedness axiom, valid finite witness and mathematically valid infinite non-well-founded countermodel distinguished |
| FV-03 | Distinct actual/model/evidence types; incomplete observations do not imply concurrency |
| FV-04 | Four operative-contract cases: absent, sole malformed, two distinct, exactly one valid; expected fail/fail/fail/pass |
| FV-05 | Typed acyclic dependency graph, primitive/import provenance, no success-to-applicability cycle |
| FV-06 | Constructive positive and relevant negative causal-role controls; unrelated regulation and external-only output rejected |
| FV-07 | Typed source/background/intervention, empty-subset minimality, redundancy and joint contribution discriminators |
| FV-08 | Typed predecessor adapters; denied, unresolved and malformed authorization cannot yield positive protected-effect assessment |
| FV-09 | All 109 governing identities preserved; property or explicit blocker for each mandatory obligation |
| FV-10 | Hash manifest, reproducible executions, property-based migration of meaningful earlier controls |
| FV-11 | OPEN-D2-01..08, five inherited categories, 16 VO statuses and owners reconciled; no unsupported discharge |
| FV-12 | Normative/diagnostic/runtime boundary and architect authorization/adoption distinction explicit |

**Gate:** Completed-D2 adoption consideration requires all 12 PASS, no mandatory acceptance blockers, VO-specific justified discharge or authorized nonapplicability, and a separate explicit architect adoption. Conditional/incomplete applies where traceable work remains blocked without demonstrated contradiction. FAIL applies to demonstrated contradiction, predecessor restriction violation, lost mandatory obligation or material evidence misrepresentation. One focused verification round follows this revision; further substantive revision requires separate authorization.

## N8. Current evidence, status and architect decision

**Current focused-verification disposition: NOT YET PERFORMED.** FV-01..FV-12 are **PENDING**, not PASS. The earlier reported v0.7 20/20 checks remain historical bounded diagnostic evidence only; they were not rerun or independently reproduced in this revision. The earlier 109 ledger records remain mostly semantic placeholders. Formal VO discharge remains **0/16**. The architect approved preparation/incorporation of v0.8; **did not adopt v0.8**. The remaining unresolved predecessor mappings, full semantic ledger, actual attribution cases and independent verification prevent completed-D2 acceptance. **Current gate: CONDITIONAL / INCOMPLETE**, pending focused verification, without presuming its outcome.

---

# HISTORICAL NONOPERATIVE BASELINE — v0.7 (VERBATIM)

The following is an exact historical copy of the frozen Round 1 source. Where it conflicts with N0–N8, the v0.8 corrections control; historical claims of execution and historical statuses remain dated historical records only.

# PROJECT NNNC — NEUTRAL NEURAL NETWORK CORE
## Phase 4 of 13 — Causal Architecture
### Document 2 of 2 — Mathematical Formalization and Verification Contract

| Control | Value |
|---|---|
| Identifier | NNNC-P4-D2 |
| Revision | v0.7 — ROUND 1 INTEGRATED TRANSITION MODEL / BOUNDED STOP CANDIDATE |
| Status | DRAFT; NOT REVIEWED, NOT ADOPTED, NOT VERIFIED |
| Date | 23 October 2026 |
| Governing document | NNNC-P4-D1 v0.4.1 — ADOPTED |
| Predecessor status | Phase 0 conditional baseline; Phase 1 D1 v2.0 / D2 v0.2.1; Phase 2 D1 v1.0 / D2 v1.0 conditional; Phase 3 D1 v0.2.6 + adopted C1 / D2 v0.5.2 conditional |
| Formal evidence | No machine-checked proofs; bounded finite reference-model checks in §13 only |
| Review route | Round 1 draft → independent adversarial review → bounded correction / reproducible verification → architect decision |

**Scope and limitation.** This Round 1 candidate (with v0.7 stop disposition in §15) fixes an explicit typed semantic core and a verification contract; §13 records v0.4 finite checks, §7F records v0.5 controls, and §14 adds v0.6 source-linked realization fixtures. It does not purport to finish all forty governing requirements or discharge any of sixteen verification obligations. Unelaborated interfaces are marked OPEN rather than implicitly proved. P4-D1 prevails on any conflict. Mathematical modeling does not itself demonstrate a real NNNC, empirical causation, or safe protected effects.

## 0. Normative inheritance and mathematical discipline

**D2-RULE-01.** `Imported_*` denotes a predecessor-defined relation whose exact definition and argument structure remain controlled by its source. No P4 axiom may make an unauthorized imported transition true. In particular `P2.AuthorizedTransition(x₂,l,h₂,v)` retains its predecessor arguments and adopted Phase 3 C1 specialization.

**D2-RULE-02.** Separate (a) world/history truth, (b) model-relative truth, and (c) evidence-relative assessment. Neither (b) nor (c) implies (a) without independently justified bridging assumptions.

**D2-RULE-03.** Every theorem or test must declare universe, assumptions, bounds, proof method, and exact claim. `PLANNED` is not `PASS`; `UNKNOWN` is not `FALSE`; absence of a counterexample in a finite search is not universal proof.

## 1. Primitive sorts and partial knowledge

Let `W` be realized histories, `ER` event referents (actual, alleged, hypothetical or simulated), `E` evidence records, `F` evidence frames, `L` loci, `T` placements, `C` contexts, `S` candidate systems, `K` capabilities, `R` realization contracts, `M` causal models, `X` operations, `Eff` effect descriptors, and `Scope` imported protected-effect scopes. Distinct sorts are not implicitly coercible. `FiniteNonempty(T)` denotes finite nonempty subsets of `T`.

```
Knowledge(T) ::= Unknown | Known(T) | Disputed(FiniteNonempty(T))
Assessment ::= PROPOSED | SUPPORTED_UNDER_ASSUMPTIONS
             | REFUTED_UNDER_ASSUMPTIONS | UNDETERMINED
Occurs             : W × ER → Bool
Reports            : E × ER → Bool
OccurrenceAssessment : ER × F → Assessment
LocusInfo          : ER × F → Knowledge(L)
PlacementInfo      : ER × F → Knowledge(T)
```

**D2-AX-01 — No evidential creation.** `Reports(e,r)` imposes no axiom `Occurs(w,r)`. Similarly `OccurrenceAssessment(r,f)=SUPPORTED_UNDER_ASSUMPTIONS` does not entail `Occurs(w,r)` without a separately justified evidence-to-world bridge. The realized occurrence predicate is independent of whether `r` is recorded, locatable or placed.

**D2-AX-02 — Knowledge non-collapse.** `Unknown`, `Known(v)` and `Disputed(V)` are distinct constructors. `Unknown` is not a claim of falsehood, nonoccurrence or inapplicability.

**Required controls (unexecuted):** a world with an unreported occurrence; a false report; a realized occurrence with unknown locus; two occurrences with unknown relative order (CE-P4-07, 08, 22, 23; VO-01).

## 2. Occurrence order, concurrency and feedback

For each `w∈W`, `Precedes_w ⊆ ER×ER` is an irreflexive transitive relation restricted to realized occurrences of `w`. In finite histories, this implies no precedence cycles. For infinite histories, occurrence-level well-foundedness is an **additional explicit assumption** when required, not inferred from acyclicity alone. `OrderAssessment(r1,r2,f)` is evidence-relative and may be `BEFORE`, `AFTER`, `CONCURRENT`, or `UNKNOWN`; it is not identical to `Precedes_w`.

`Concurrent_w(a,b)` means `Occurs(w,a) ∧ Occurs(w,b) ∧ ¬Precedes_w(a,b) ∧ ¬Precedes_w(b,a)` **only when the declared execution semantics establish that the order is complete enough for this conclusion**. Without that assumption, incomparability yields `ORDER_UNRESOLVED`, not proven concurrency. Abstract feedback cycles are allowed in model descriptions; their realized witnesses must be distinct well-founded occurrences. A delayed or absent acknowledgment does not imply nonoccurrence.

**Required controls (unexecuted):** asynchronous delayed acknowledgment, competing paths, abstract feedback with ordered occurrence witnesses, and a rejected self-precedence cycle (VO-03..05).

## 3. Causal models, influence, attribution and identification

A model `μ∈M` declares variables, structural mechanisms, admissible contexts, interventions, target outcomes and interpretation. `Influences_μ(A,Y,c)` is true only under a **declared admissible comparison** in which variation of source `A` changes the specified property of `Y`; observational correlation alone does not establish this predicate. Actual attribution is separately typed:

```
Influences        : M × Source × Target × C → Bool
ActualContribution : AttributionRule × M × Source × Outcome × W × C → Bool
Sufficient       : M × FiniteNonempty(Source) × Outcome × C → Bool
MinimalSufficient: M × FiniteNonempty(Source) × Outcome × C → Bool
```

For a finite deterministic model, `Sufficient(μ,A,y,c)` requires `A` to yield `y` in **every background in a separately declared nonempty admissible background set**. `MinimalSufficient(μ,A,y,c)` holds iff `Sufficient(μ,A,y,c)` and no proper **nonempty** subset is sufficient; if the empty set could be sufficient, that possibility must be checked separately, not hidden by the nonempty-set type. This is a local convention, not a universal theory of actual causation. `ActualContribution` requires a specified attribution rule `α`; it is never inferred from group membership alone. Necessary, sufficient, enabling, inhibiting and contributing roles have distinct predicates or explicit scoped definitions.

**Required controls (unexecuted):** redundant `A∨B`, joint `A∧B`, context-gated `A∧G`, irrelevant `Z` in a successful group, common-cause observational equivalence, and two evidence-compatible models with different intervention outcomes. Preemption is OUTSIDE the initial attribution rule until expressly modeled (VO-02, 11, 14, 15).

## 4. Interventions, effects and predecessor authorization

```
EffectAnalysis : X × PreHistory → Unresolved(Reason) | Covered(Set(Eff), Assumptions)
ActualEffects  : X × History → Unavailable | Recorded(Set(Eff))
RequiredScopes : Set(Eff) → Set(Scope)
```

`Unavailable ≠ Recorded(∅)`. `Covered(P,A)` is an **analysis result**, not proof that `P` is complete. `CoverageSound(x,h⁻,P,A)` means that every effect of every execution admitted by declared semantics under `A` is included in `P`. `AssumptionsApplicable(A,actualContext,assuranceLevel)` and `CoverageEstablished(...)` are separate evidence/assurance judgments. `RequiredScopes(P)` is the union of scopes defined by imported predecessor rules, including indirect substrate/service effects. The caller's label cannot determine these scopes.

**D2-AX-03 — Strict-prior gate.** A positive `ProtectedExecutionAssessment(x,h⁻)` requires a `Covered(P,A)` analysis, established coverage and applicable assumptions at the stated assurance level, and **every imported strict-prior authorization condition** for `RequiredScopes(P)` and relevant lifecycle links. The predicate reports a qualified assessment; it is not an authorization primitive. `Unresolved` never yields a positive protected-execution assessment. `ActualEffects(x,h)=Recorded(E)` with `E⊈P` yields `CoverageFailure(x,h)`; post-hoc widening of `P` cannot supply missing prior authorization.

**D2-AX-04 — Classification by effect.** Simulating or describing a protected operation does not authorize it. Actual protected effects of the simulation computation itself remain subject to the same imported rules. Model revision and mechanism adaptation may overlap and both classifications then apply; a permission for one does not discharge the other. Ordinary unprotected model revision is not automatically constitutional or lifecycle transition.

**Required controls (unexecuted):** unresolved analysis versus covered empty set; simulation performing a real protected checkpoint write; out-of-scope actual effect; incompatible overlapping permissions; administrative relabeling; a model whose coverage assumptions do not apply to deployment (VO-08, 10, 13).

## 5. Organization and capability-relative realization

Let `ApplicableCapabilities(s,c) = K_required(s,c) ∪ K_claimed(s,c)`, where `K_required` is derived from governing architecture/qualification contracts **without consulting whether a candidate contract is valid or realized**. A partial study may omit examination but must record mandatory omitted capabilities and cannot conclude complete qualification.

Retain the governing system-level floor **without weakening its five conjuncts**:

```
MinimumOrganization(s,c) ⇔
  StateMediated(s,c) ∧ RegulationRealized(s,c) ∧ FeedbackRealized(s,c)
  ∧ RequiredMemoryRolesRealized(s,c) ∧ RequiredCoordinationRealized(s,c)
```

For a capability `k`, `ApplicableRoles(k,c)` is fixed by governing capability requirements, not by convenient observed success. A contract `r` is bound to `k` by `ContractFor(r,k,c)`; ambiguous or missing binding cannot establish realization. `ContractWellFormed(r,k,c)` must check **all seven fields of REQ-P4-035** and governing relationships/coverage, independently of applicability and success. `CapabilityOrganization(s,k,r,c)` requires that contract-required state, mechanisms and relationships participate in **decisive processing** of `k`; unrelated activity cannot qualify. `CapabilityRealized(s,k,r,c)` additionally requires independently fixed substantive success conditions. These are distinct from `EvidenceSupportsCapability(s,k,r,f)` and from full inherited Phase 1 NNNC qualification.

**D2-AX-05 — Nonvacuity.** Neither an empty applicable-role set, an absent/malformed contract, a trivial logging mechanism, a message-only assembly, nor an external-service wrapper can alone establish positive capability realization. A capability legitimately requiring no memory role is not failed merely for lacking capability-specific memory, while system-level applicable memory obligations remain in force.

**D2-AX-06 — Continuation non-identity.** `CapabilityContinues(k,s,c,s',c')` requires the specified causal relationships to persist or be reconstructed; it does **not** imply imported `SameEntity(s,s')` or imported lifecycle authorization.

**Required controls (unexecuted):** constructive consequential state/memory/coordination/regulation/feedback; logging-only history; message-only assembly; external-service wrapper; redundancy assessed through group/trajectory comparison; restored state with broken required relationship; inconclusive evidence returning UNDETERMINED; irrelevant consequential internal activity (VO-16 and NC-01..05).

## 6. Abstraction, boundaries, provenance and revision

`AbstractionMap(low,high,domain)` must declare admissible contexts, interventions, observables and preserved properties. `AbstractionAdequate(map,claim,domain)` is claim-relative; predictive adequacy does not entail intervention, mechanism-identification or explanatory adequacy. System-level causal organization confers neither new entity identity nor authority. A boundary map distinguishes NNNC-internal mechanisms from NES and external services; causal contribution by the latter cannot be counted as internal decisive processing merely by renaming it.

`ModelRevision(μ,μ',h)` changes representation; it does not alter the realized history `h`. `MechanismChange(x,h,h')` is a separate realized transition and may co-occur with model revision, subject to inherited constraints. Provenance and evidence may support assessments but do not manufacture occurrence or independent evaluator status. An evaluator's self-issued claim alone is not independent validation.

## 7. Verification registry and mandatory evidence format

The **authoritative mapping** is P4-D1 v0.4.1 §7.1, including its property-level ledger. Preserve exactly `REQ-P4-001..040`, `INV-P4-01..12`, `CE-P4-01..36`, `P4-VO-01..16` and `P4-VO-16-NC-01..05`. No ID is silently dropped or renumbered.

| Obligation | Formalization focus | Current status |
|---|---|---|
| P4-VO-01 | Occurrence, report, knowledge | PLANNED — NOT DISCHARGED |
| P4-VO-02 | Correlation/influence/common cause | PLANNED — NOT DISCHARGED |
| P4-VO-03 | Precedence, concurrency, uncertainty | PLANNED — NOT DISCHARGED |
| P4-VO-04 | Delay/acknowledgment | PLANNED — NOT DISCHARGED |
| P4-VO-05 | Feedback and occurrence well-foundedness | PLANNED — NOT DISCHARGED |
| P4-VO-06 | Provenance/evidence/independent assessment | PLANNED — NOT DISCHARGED |
| P4-VO-07 | Causal ancestry versus identity | PLANNED — NOT DISCHARGED |
| P4-VO-08 | Effect coverage and imported prior authorization | PLANNED — NOT DISCHARGED |
| P4-VO-09 | NNNC–NES boundary | PLANNED — NOT DISCHARGED |
| P4-VO-10 | Model revision versus history/mechanism | PLANNED — NOT DISCHARGED |
| P4-VO-11 | Intervention semantics versus prediction | PLANNED — NOT DISCHARGED |
| P4-VO-12 | Abstraction/emergence | PLANNED — NOT DISCHARGED |
| P4-VO-13 | Simulation versus realized effects/authority | PLANNED — NOT DISCHARGED |
| P4-VO-14 | Roles, redundancy, actual attribution | PLANNED — NOT DISCHARGED |
| P4-VO-15 | Identifiability/compatible models | PLANNED — NOT DISCHARGED |
| P4-VO-16 | Positive organization/capability realization | PLANNED — NOT DISCHARGED |

Each VO SHALL eventually have a record with (i) source clauses and exact predecessor imports, (ii) typed property and assumptions, (iii) constructive witness, (iv) distinguishing negative witness, (v) method and bounded universe, (vi) executable artifact and reproducibility instructions where applicable, (vii) actual result, and (viii) reviewer disposition. Every independently assessable sub-property needs its own coverage line or explicit justified deferral. The five VO-16 NC subcases require separate traceable results. No registry assignment is a verification result.

## 7A. Explicit seven-field realization-contract schema (Round 1 expansion)

This section **refines**, but does not discharge, `OPEN-D2-01`. Let `CapabilityId`, `Mode`, `Condition`, `MechanismId`, `StateId`, `Dependency`, `ContributionClaim`, `ExternalDependency`, `ContinuityRule`, `ComparisonDesign` and `EvidenceRequirement` be disjoint typed sorts. For each `r ∈ R`, define the **total record** (field values may still be empty or invalid):

```
RealizationContract(r) = (
  operational : (CapabilityId, Set(Mode), Set(Condition)),     // (a)
  participants : (Set(MechanismId), Set(StateId)),              // (b)
  dependencies : Set(Dependency),                              // (c)
  contributions : Set(ContributionClaim),                      // (d)
  external : Set(ExternalDependency),                          // (e)
  lifecycle : Set(ContinuityRule),                             // (f)
  discrimination : (Set(ComparisonDesign), Set(EvidenceRequirement)) // (g)
)
```

`ContractFor(r,k,c)` holds only when `operational.CapabilityId = k`, the declared mode and conditions encompass `c`, and no incompatible binding exists. `Applicable(k,s,c)` is derived **only** from governing required capability/role obligations and candidate claims, without reference to `ContractFor`, contract validity or observed outcomes. Define `RequiredRoles(k,c)` from those same governing sources. For a full qualification claim, `Coverage(s,c) ⇔ ∀k(Applicable(k,s,c) ⇒ ∃!r ContractFor(r,k,c) ∧ ContractWellFormed(r,k,c))`; a partial prototype instead reports `MissingCoverage` and cannot assert full coverage.

`ContractWellFormed(r,k,c)` requires **all seven** fields to be present, well-typed, mutually consistent, and relevant to `k,c`; nonempty participants and dependencies appropriate to required roles; contribution claims identifying specific source, target, context, attribution rule and admissible comparisons; external/NES dependencies explicitly classified (an affirmative `None` must be justified, not left blank); lifecycle rules covering applicable maintenance, degradation, unavailability, uncertainty, restoration and permitted variation; and comparisons identifying assumptions, outcomes, distinguishable alternatives, evidence limitations and intervention permission **separately**. A field being syntactically nonempty is not proof of truth. `ContractWellFormed` is **not** defined using `CapabilityRealized`, `SatisfiesOrganization` or success evidence.

The following predicates are kept distinct:

```
ModelContribution(μ,s,A,Y,c)                 // model-relative, comparison-dependent
RealizedContribution(α,μ,s,A,y,w,c)         // world-relative under declared α
EvidenceContributionAssessment(s,A,y,f)     // evidence-relative
SatisfiesOrganization(s,r,c,w)              // semantic, world-relative
OrganizationAssessment(s,r,c,f)             // evidence-relative
```

`SatisfiesOrganization(s,r,c,w)` requires valid contract binding, relevant internal state and mechanisms actually participating in decisive capability processing, applicable required-role integration, consequential regulation and feedback, and contract-relative substantive conditions in `w`. It does **not** follow from `ContractWellFormed`, from a successful output alone, or from an internal graph edge. For redundant or jointly sufficient contributors, evaluate a declared **group or trajectory** comparison rather than treating failure of individual ablation as absence of contribution. A world-level satisfaction claim is permitted only with its declared realized-history and attribution assumptions; assessment remains `UNDETERMINED` where evidence cannot discriminate.

**Status mapping.** For the D1 three-valued `OrganizationAssessment`: `SUPPORTED ↦ SUPPORTED_UNDER_ASSUMPTIONS` with recorded assumptions; `REFUTED ↦ REFUTED_UNDER_ASSUMPTIONS`; `UNDETERMINED ↦ UNDETERMINED`. `PROPOSED` is a general claim state **before** sufficient adjudicating evidence and is not an extra value of the D1 three-valued assessment. No mapping implies world truth.

**Positive/negative fixtures (specified, not executed):** `R7-POS` a seven-field contract with relevant internal state, integrated decision mechanisms, consequential regulation and distinct-occurrence feedback; `R7-NEG-1` missing field (g); `R7-NEG-2` two conflicting capability bindings; `R7-NEG-3` unrelated system memory for a memory-dependent capability; `R7-NEG-4` consequential regulation only on an irrelevant subsystem; `R7-NEG-5` external wrapper with only forwarding/logging; `R7-NEG-6` redundant internal contributors with valid group-level influence. Each fixture must supply explicit interpretations, not merely narrative labels.

## 7B. Typed causal order and assessment separation

Let `Precedes_w` be a strict partial order on occurred referents. Add `OrderCompleteness(w,a,b)` as an **explicit** declared property of the observed/realized execution model for the pair. Define `Concurrent_w(a,b)` only if both occur, both directions of precedence are false **and** `OrderCompleteness(w,a,b)` holds. Otherwise the world-level model returns `UnresolvedOrder` when the relation is not established; the evidence-level `OrderAssessment` can remain `UNKNOWN` even where the world order is fixed. A total order is **not** assumed. Feedback is a mechanism-level dependency cycle whose realization requires an acyclic sequence of distinct occurrences; an edge `a→a` at occurrence level is invalid. For infinite histories, a well-foundedness assumption must be supplied separately, e.g. no infinite descending `Precedes_w` chain.

## 7C. Attribution, identifiability and effect-scope proof obligations

For each declared causal model `μ`, the intervention semantics must distinguish `do(X:=x)` from observation `X=x`, specify admissible interventions, exogenous backgrounds, and relevant outcome equivalence. For any set `A`, include the empty set when testing whether a purported sufficient group is **minimal**: `MinimalSufficient(A) ⇔ Sufficient(A) ∧ ∀B ⊊ A ¬Sufficient(B)`, where `Sufficient(∅)` is well-typed in the **auxiliary test domain** even though candidate groups are nonempty. This corrects the omission risk of the initial convention without claiming a universal attribution theory. Redundant `A∨B`, conjunctive `A∧B`, preemptive and probabilistic cases must carry distinct assumptions and outcomes; preemption and stochastic attribution remain explicitly unresolved until formalized.

For evidence frame `f`, define `CompatibleModels(f) = {μ | μ satisfies declared observation constraints of f}`. `Identified(f,q)` holds only if `CompatibleModels(f)` is nonempty and all compatible models agree on the value of causal query `q` under the declared admissible interventions. Empty compatibility sets mean **inconsistent evidence/model assumptions**, not vacuous identification. If two compatible models disagree, return `UNDETERMINED` and retain both; observational fit does not determine mechanism.

For protected operation `x` with prior history `h⁻`, define `PriorGate(x,h⁻)` as the **conjunction** of imported applicable Phase 0–3 predicates, retaining original argument types, authority and lifecycle parameters. The Phase 4 wrapper must not replace these with an unconstrained `Authorized=true`. A positive execution assessment requires independently established `CoverageSound` for all admissible direct and indirect effects, `AssumptionsApplicable` at the stated assurance level, complete effect-derived `RequiredScopes`, and `PriorGate`. If an effect class or import is unresolved, the result is `UNDETERMINED` / **not positively authorized**; `Recorded(∅)` and `Unavailable` are distinct. Post-execution scope expansion cannot retroactively satisfy the prior gate. This is a **formal obligation schema**, not a completed imported-signature audit or safe implementation claim.

## 7D. Reproducible finite-model fixture specification (not yet executed)

The first finite test suite SHALL use explicit small bounds and separate semantic interpretations: at most four occurrence referents, three mechanisms, three state variables, two candidate capabilities, two evidence frames, two models, and two admissible contexts **per fixture**. Each fixture declares whether its universe is closed, which occurrence pairs have complete ordering, which predecessor interfaces are uninterpreted, and which intervention assumptions hold. Mandatory paired witnesses include: occurrence without report / report without occurrence; unknown order / established concurrency; abstract feedback / distinct occurrence chain; observationally equivalent confounded models / different `do` effects; joint sufficiency / redundant contribution / irrelevant member; model revision / realized mechanism change; seven-field positive realization / each of the five NC negatives; covered effects / uncovered actual effect / unavailable record; hypothetical simulation / actual protected computation.

**Execution evidence format:** fixture ID; governing `REQ`, `INV`, `CE`, `VO`, `NC` IDs; full typed instance; expected SAT/UNSAT or assertion result; actual solver/tool output; exact tool version and invocation; assumptions and bound; artifact hash; reviewer disposition. **All actual results currently `NOT RUN`.** A finite pass establishes only the declared bounded property under its assumptions.

## 7E. Round 1 traceability and inherited-risk gate

The authoritative property-level assignments remain **P4-D1 v0.4.1 §7.1**; they are not replaced by this supplement. For each `REQ-P4-001..040`, `INV-P4-01..12`, `CE-P4-01..36`, `P4-VO-01..16` and `P4-VO-16-NC-01..05`, the next revision SHALL provide a separate machine-readable ledger row with source anchor, typed formula, constructive witness, discriminating negative witness, exact inherited imports, proof/test status and evidence location. Until that ledger is transcribed and checked, `OPEN-D2-02` remains open. `OPEN-D2-04` remains open until predecessor signatures are actually audited. `P0-O01..O03` continue to block safe real protected-effect claims; no test fixture overrides that gate. Phase 2 PF obligations, Phase 3 PAC-1 evidence reconciliation and PAC-2 predecessor audit remain inherited unresolved work.

## 7F. v0.5 predecessor-interface audit and discriminating countermodels

**Scope:** This section extends rather than supersedes §§0–7E and the existing 40/12/36/16 source-derived mapping. A signature found in a predecessor is not a proof that the corresponding implementation or authority judgment is valid. The reference model remains non-executable for real protected effects.

### 7F.1 Source-anchored imported interfaces

The exact Phase 2 D2 v1.0 §3 interface declarations include:

```text
AuthorizedTransition:  X × L × H × V → Bool
AuthorizedCustodyStep: X × K × K × L × H × V → Bool
ValidLocusAuthority:  X × L × H × V → Bool
InvariantOK:          X × H × V → Bool
```

Phase 2 explicitly warns that `AuthorizedTransition` is authorization for the **specific lifecycle transition**, not merely checkpoint reading/initialization; `InvariantOK` must be expanded against applicable invariants, not assigned `true` by fiat. Phase 2's `CustodyContractValid` is a native §4.4 conjunction, **not** an imported Phase 1 custody predicate. Phase 3 D2 v0.5.2 retains `P2.AuthorizedTransition(x2,l,h2,v)` with those four arguments unchanged and requires an explicit source correspondence for relevant lifecycle effects. These are **located signatures**, not complete semantic import proofs.

**Import contract P4-IMP-01.** For any Phase 4 action `a` whose realized effects intersect a predecessor lifecycle/custody/constitutional scope, the corresponding predecessor call must preserve (i) the same governed operation, (ii) its actual locus, (iii) its strictly preceding history, (iv) its applicable rule version, and (v) the specific authority/custody/constitutional constraints. Failure to resolve a required argument or scope yields `UNDETERMINED` and cannot establish a positive protected execution assessment. Phase 0 `Pi` canonical policy/revocation/session/ledger and D1 positive NES support are **not** alternative permission oracles.

**Import contract P4-IMP-02.** Phase 1's `D2-REQ-002` non-substitution and `D2-REQ-003` open-world treatment remain binding. A contract name, component manifest, simulated constituent, or external service does not establish an NNNC internal mechanism. Missing evidence is not negative evidence. Phase 4 capability assessments are separate from Phase 1 whole-entity qualification.

**Import contract P4-IMP-03.** A protected-effect scope must cover direct and indirect possible effects *before* execution. An actual effect outside the admitted envelope creates `CoverageFailure`; later discovery cannot repair prior authorization. A Phase 4 model may express a hypothetical operation without licensing its physical effects. P0-O01–O03 remain assurance blockers.

### 7F.2 Concrete countermodel: observational fit is not causal identification

Two deterministic structural causal models with exogenous binary `U`:

```text
M1: X := U; Y := X
M2: X := U; Y := U
```

Both yield the same passive observations `(X,Y)={(0,0),(1,1)}` under `U∈{0,1}`. But after `do(X:=0)`, `M1` forces `Y=0`, whereas `M2` permits `Y=1` when `U=1`. Therefore observational equality alone cannot establish the interventional relation `X→Y`. `Identified(f,q)` must return false for a frame admitting both models when `q` is that intervention effect. This is a **constructive finite counterexample**, not a proof about an NNNC deployment.

### 7F.3 Concrete controls: predecessor-gate non-substitution

The v0.5 synthetic gate fixture represents a located predecessor signature and four positional arguments, the claimed strictly prior state, the claimed verdict, the independently classified effect envelope, and lifecycle permission. It rejects a missing imported call, wrong arity, wrong signature, stale prestate, denial, uncovered indirect effect, unknown effect envelope, and failed lifecycle condition. A passing synthetic case demonstrates only that the *wrapper fixture* rejects those malformed inputs. It cannot establish the soundness of the predecessor predicate, trusted provenance, resource-side fencing, or actual effect coverage.

### 7F.4 Realized feedback and distinct occurrences

A declared abstract feedback cycle may have a valid unfolded occurrence witness `o0 ≺ o1 ≺ o2` with separate identifiers. Neither `o0 ≺ o0` nor a reversed timestamp pair is a valid strict-order witness. This control does not assume that every real execution is totally ordered, nor that unknown order implies concurrency. A model-level loop and a realized occurrence cycle are distinct objects.

### 7F.5 Executed evidence and precise limits

The accompanying `p4d2_v05_integration_checks.py` and `NNNC-P4-D2-v0.5-integration-results.json` provide **30 passing checks and zero failing checks**. The checks include five predecessor-source/signature assertions, seven literal seven-field checks, synthetic prior-gate negative mutations, a finite causal-model example, and distinct-occurrence feedback controls. Source SHA-256 digests are recorded in the results file. All are **bounded source inspections or synthetic countermodels**. The Phase 4 VO discharge count remains **0/16**; the five VO-16 negative controls remain unverified as complete integrated realization tests.

### 7F.6 Bounded integration ledger and outstanding work

| Item | v0.5 disposition | Remaining closure condition |
|---|---|---|
| `OPEN-D2-01` | Seven governing fields independently located; synthetic malformed-field tests pass | Full typed capability-relative realizations and substantive witness |
| `OPEN-D2-02` | Identifier inventory retained from v0.3 | Clause-level 40/12/36/16+5 formula/witness/oracle ledger still open |
| `OPEN-D2-03` | Finite causal/feedback and guard fixtures extended | Integrated multi-sort transition model with discriminating countermodels open |
| `OPEN-D2-04` | Phase 2 four source signatures and Phase 3 preserved call located | Complete Phase 0–3 semantic import/bridge and Phase 1 qualification audit open |
| `OPEN-D2-05` | Observationally equivalent / interventionally distinct counterexample executed | Preemption, stochastic attribution, and actual-contribution rule open |
| `OPEN-D2-06` | Distinct ordered feedback witness exercised | Open-world order and infinite-history well-foundedness remain open |
| `OPEN-D2-07` | Causal nonidentification witness executed | Full abstraction and independent-evidence countermodels open |
| `OPEN-D2-08` | No obligation discharged or silently removed | Master closure-register reconciliation open |

**Round 1 stopping rule:** This v0.5 increment does not trigger independent acceptance review. The next bounded step must either (a) complete the clause-level crosswalk and an integrated executable witness for `REQ-P4-035..040`, or (b) document a precise unresolved predecessor semantic blocker and stop Round 1 as incomplete. Further isolated Boolean checks without source-linked semantic coverage are not an adequate substitute.

## 8. Unresolved formalization and integration work

- **OPEN-D2-01 (PARTIALLY SPECIFIED):** §7A transcribes all seven fields and defines binding and satisfaction, but independent type-checking, executable instances and full inherited-role coverage remain outstanding.
- **OPEN-D2-02:** Elaborate the full 40-REQ/12-INV/36-CE property-level crosswalk and all five VO-16 negative subcases; confirm each against the exact adopted source text.
- **OPEN-D2-03:** Specify finite reference-model domains, executable semantics, constructive and discriminating countermodels; run and preserve results.
- **OPEN-D2-04:** Audit exact imported predecessor authorization, lifecycle, identity, custody, qualification and boundary signatures; do not replace imported predicates with assumed booleans.
- **OPEN-D2-05 (PARTIALLY SPECIFIED):** §7C resolves the empty-set minimality test and defines a nonvacuous identifiability condition; resolve remaining formal subtleties of actual-contribution attribution (including empty-set sufficiency and redundancy), observational identification, stochastic criteria and preemption scope.
- **OPEN-D2-06:** Complete occurrence-order semantics, especially concurrency versus unknown order, and the infinite-history well-foundedness assumptions.
- **OPEN-D2-07:** Establish semantic adequacy of causal abstraction, independent evaluation, evidence uncertainty, and model/actual-history separation with countermodels.
- **OPEN-D2-08:** Reconcile obligations into the NNNC master closure register; preserve P0-O01..O08, Phase 2 PF-series and Phase 3 PAC-2 (plus the recorded PAC-1 review disposition) without inventing discharge.

**Safety qualification.** P0-O01 protected-write bypass, O02 durable journal/crash recovery and O03 physical-effect idempotency/fencing remain blockers to claims of safe real protected effects. Neither D1 adoption nor any finite D2 model closes them.

## 9. Bounded review and acceptance

**Round 1:** complete typed signatures and semantic crosswalk; build finite witnesses. **Round 2:** independent adversarial mathematical and predecessor-fidelity review, with anchored findings and severity. **Round 3:** one consolidated blocker-correction pass and one focused verification, with residuals explicitly registered. **Stop rule:** stop after the bounded verification gate; a remaining material blocker yields rejection or narrowly scoped conditional disposition, not an automatic new review cycle. **Acceptance:** requires explicit architect decision; no claim of proof without reproducible evidence.

### Drafting change log

| Revision | Disposition |
|---|---|
| v0.1 | First typed semantic candidate, inherited boundary rules, planned VO registry, and explicit open-work register. No proofs executed or claims of adoption. |
| v0.2 | Round 1 expansion: seven-field contract schema, explicit applicability and assessment mapping, order semantics, identification/minimality corrections, protected-gate schema, finite fixture plan and inherited-risk controls. No proofs executed; NOT ADOPTED. |



## 10. v0.3 normative-source traceability ledger (source-extracted; verification pending)

This ledger transcribes each operative requirement, invariant and adversarial case's **single-line source clause** from the adopted P4-D1 v0.4.1. Some source clauses are multi-paragraph and this extraction is **not a substitute for the complete governing text**. Assigned VOs come directly from D1 §7.1; they are **administrative coverage**, not proof of semantic adequacy. Source text is retained to make independent review possible. No requirement or case is discharged by transcription.

| Source ID | Governing clause (source excerpt) | Assigned VO(s) | Mathematical hook / outstanding disposition |
|---|---|---|---|
| `REQ-P4-001` | REQ-P4-001 — Non-conflation. P4 SHALL distinguish temporal succession, correlation, causal influence, logical implication, computational data dependency, authorization, custody, organizational integration and identity. None alone substitutes for another. | P4-VO-01 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-002` | REQ-P4-002 — Typed referents. Each causal relation SHALL identify the kinds of its endpoints (e.g. event, state property, component operation, governance occurrence or boundary interaction), its context, and its evidential status. Phase 1 and Phase 2 native sorts SHALL NOT be silently merged. | P4-VO-01, P4-VO-02, P4-VO-14 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-003` | REQ-P4-003 — Event/state distinction. Persistent states, transitions between states, observations of those states, and records of transitions SHALL remain distinguishable. A change in a representation does not automatically establish a corresponding change in its represented environment. | P4-VO-01, P4-VO-02 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-004` | REQ-P4-004 — Partial order. For historical occurrence claims, established causal precedence SHALL be distinguished from concurrency, merely observed ordering and unknown order. A missing proven precedence edge SHALL NOT establish concurrency. Applicable Phase 2 causal-history rules remain controlling. | P4-VO-01, P4-VO-02, P4-VO-03 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-005` | REQ-P4-005 — Feedback without self-origin. | P4-VO-03, P4-VO-04, P4-VO-05 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-006` | REQ-P4-006 — Delay and latency. Causal descriptions SHALL allow delayed effects, queued events, asynchronous observations, and absent acknowledgments without assuming global synchronous time or instantaneous propagation. | P4-VO-01, P4-VO-03 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-007` | REQ-P4-007 — Competing effects. When multiple candidate causes or mutually exclusive outcomes compete, the architecture SHALL represent the competing paths and evidence; it SHALL NOT silently select one as historically actual merely because it is locally feasible. | P4-VO-01, P4-VO-03, P4-VO-04 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-008` | REQ-P4-008 — No retroactive authorization. Later observations, outcomes or model updates SHALL NOT retroactively supply the strict-prior constitutional authorization required for a protected occurrence. | P4-VO-03, P4-VO-04 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-009` | REQ-P4-009 — Mechanism specification. A claimed causal mechanism SHALL specify its input conditions, affected variables or operations, mediating dependencies, boundary conditions and possible failure modes at a level appropriate to its claim. | P4-VO-02, P4-VO-15 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-010` | REQ-P4-010 — Observation versus intervention. The architecture SHALL distinguish passive observation, deliberate intervention, naturally occurring perturbation and simulated intervention. Observational associations alone SHALL NOT be labeled experimentally verified effects. | P4-VO-02, P4-VO-11, P4-VO-15 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-011` | REQ-P4-011 — Counterfactual discipline. Counterfactual claims SHALL name the model, intervention, held-fixed assumptions, comparison outcome and scope of validity. Unidentifiable counterfactuals SHALL remain undetermined rather than receive fabricated values. | P4-VO-05, P4-VO-11, P4-VO-15 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-012` | REQ-P4-012 — Uncertainty. Causal assessments SHALL represent uncertainty arising from incomplete observations, hidden common causes, model misspecification, nondeterminism, competing explanations, and measurement error where relevant. A numeric confidence score SHALL NOT substitute for an articulated evidence contract. | P4-VO-05, P4-VO-11, P4-VO-15 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-013` | REQ-P4-013 — Falsifiability and revision. Claims SHALL admit identifiable challenges or disconfirming evidence where their semantics permit. Model revisions SHALL preserve historical provenance and distinguish changed interpretation from changed history. | P4-VO-06, P4-VO-10, P4-VO-11 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-014` | REQ-P4-014 — Multi-level organization. P4 SHALL accommodate causal relations at constituent, module, flow, system and external-interaction levels, with explicit mappings where an explanation crosses levels. Higher-level labels SHALL NOT erase lower-level dependencies needed for verification. | P4-VO-09, P4-VO-12, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-015` | REQ-P4-015 — Cognitive relevance without premature qualification. The architecture SHALL support causal descriptions of perception, memory change, internal processing, learning, decision formation and action selection as candidate functions. Merely labeling a process with these names SHALL NOT establish Phase 1 qualification, FFNN realization, six-algorithm realization or intelligence. | P4-VO-09, P4-VO-12, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-016` | REQ-P4-016 — NNNC–NES boundary. Causal accounts SHALL distinguish NNNC-owned processes from NES-provided execution, transport, persistence and resource effects. Dependence on substrate execution SHALL NOT collapse entity identity into a specific substrate or imply substrate authority over protected NNNC state. | P4-VO-09, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-017` | REQ-P4-017 — Boundary evidence. External observations, commands, effects and feedback SHALL carry source, timing/order, provenance, reliability and trust-boundary qualifications appropriate to the causal claim. A reported physical effect is not an independently verified physical effect. | P4-VO-07 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-018` | REQ-P4-018 — Continuity compatibility. Causal accounts of migration, replacement, branching, suspension, restoration and termination SHALL preserve Phase 2 distinctions among causal ancestry, custody, constitutive continuation and numerical identity. Causal linkage alone SHALL NOT establish identity preservation. | P4-VO-07 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-019` | REQ-P4-019 — Constitution compatibility. Any intervention, learning operation, model revision or execution step that is a protected act SHALL satisfy applicable prior Phase 0–3 authorization; P4 causal competence or prediction accuracy SHALL NOT grant authority. Adopted C1's general protected authorization and unchanged Phase 2 lifecycle specialization apply according to effect scope. | P4-VO-08, P4-VO-09, P4-VO-13 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-020` | REQ-P4-020 — Model plurality. The architecture MAY host deterministic, stochastic, structural, dynamical, rule-based or hybrid causal representations. It SHALL define correspondence between representations when transferring a claim and SHALL NOT presume equivalent causal meaning from equivalent predictive accuracy. | P4-VO-13 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-021` | REQ-P4-021 — Model provenance. Each operative causal model SHALL have a traceable version, applicable context, provenance of supporting evidence, known limitations and compatibility relation to predecessor constraints. A self-generated assertion SHALL NOT count as independent validation. | P4-VO-06, P4-VO-15 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-022` | REQ-P4-022 — Safe learning boundary. Learning or updating causal models MAY alter epistemic state within authorized scope. Changing protected governance, lifecycle state, authority, constitutional rules or real external resources requires its own applicable authorization; an inferred causal advantage cannot bypass that boundary. | P4-VO-06, P4-VO-10, P4-VO-15 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-023` | REQ-P4-023 — Error and recovery semantics. The architecture SHALL represent mistaken attribution, missing effects, false observations, stale evidence, contradictory measurements, causal-model failure and recovery as distinct possible conditions, without claiming that any particular recovery implementation is already safe. | P4-VO-06, P4-VO-10 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-024` | REQ-P4-024 — Independent challenge. A causal claim proposed by a component SHALL be challengeable through evidence or tests not defined solely by that component's own assertion. Independence claims SHALL be evaluated under Phase 3's material-control and provenance constraints. | P4-VO-06, P4-VO-10 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-025` | REQ-P4-025 — Domain separation. Every causal claim SHALL distinguish the realized referent, its representation (if any), and the evidence used to assess it. Evidence or model state SHALL NOT be silently promoted into an actual effect. Where a referent is only hypothetical or not yet implemented, the claim SHALL say so. | P4-VO-01, P4-VO-06 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-026` | REQ-P4-026 — Domain correspondence. Claims that a representation tracks a realized mechanism SHALL identify a correspondence relation, observation limits and applicable context. Correct prediction alone SHALL NOT establish correct mechanism identification; lack of an internal explanation alone SHALL NOT negate an actual mechanism. | P4-VO-01, P4-VO-06 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-027` | REQ-P4-027 — Abstraction adequacy. | P4-VO-12 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-028` | REQ-P4-028 — Emergent organization. System-level causal properties MAY be modeled when supported by declared organization and abstraction semantics. Emergence SHALL NOT be treated as proof of an extra entity, intrinsic agency, consciousness, numerical identity or a mechanism independent of the realization. | P4-VO-12 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-029` | REQ-P4-029 — Intervention typing and effect-derived scope. An intervention SHALL identify its target, context, intended changes, relevant possible side effects, epistemic or realized status and applicable predecessor authorization requirements. Applicable protected scopes SHALL be derived from operations and resources the intervention can affect, including indirect effects through invoked components, services and substrate operations. Caller-supp | P4-VO-08, P4-VO-11, P4-VO-13 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-030` | REQ-P4-030 — Non-equivalence of intervention classes. Describing, simulating or evaluating an intervention SHALL NOT establish permission or capacity to execute its represented effects. The computation performing simulation or evaluation may itself have realized effects; those effects SHALL be assessed independently of the hypothetical represented effects. Any protected effect of the computation or intervention SHALL satisfy applicable strict-pri | P4-VO-08, P4-VO-13 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-031` | REQ-P4-031 — Learning versus mechanism change. A model update SHALL be distinguished from alteration of realized routing, parameters, components or other mechanisms. Claims of adaptive causal improvement SHALL specify which changed and what evidence supports the claim. | P4-VO-08, P4-VO-10 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-032` | REQ-P4-032 — Plasticity governance. Actual mechanism adaptation SHALL preserve inherited identity, continuity, qualification and constitutional constraints. Model revision SHALL NOT rewrite historical occurrences; mechanism adaptation SHALL NOT inherit permission solely from epistemic update authority. | P4-VO-08, P4-VO-10 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-033` | REQ-P4-033 — Causal-role qualification. Necessary, sufficient, contributing, enabling, inhibiting and competing causes SHALL be evaluated relative to an explicit outcome and background conditions. An identified contributor SHALL NOT be asserted sufficient without supporting semantics; an unobserved cause SHALL NOT be asserted absent. A causal-role claim SHALL distinguish potential influence from contribution to a specified realized outcome. Where | P4-VO-02, P4-VO-14 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-034` | REQ-P4-034 — Identifiability and underdetermination. Where different causal structures remain compatible with the evidence, the architecture SHALL preserve the alternatives or return an undetermined assessment. Model-fit or confidence SHALL NOT collapse observational equivalence into unique causal truth. | P4-VO-14 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-035` | REQ-P4-035 — Positive causal organization contract. | P4-VO-14, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-036` | REQ-P4-036 — State-mediated processing and memory. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-037` | REQ-P4-037 — Coordinated internal processing. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-038` | REQ-P4-038 — Regulation and feedback. | P4-VO-05, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-039` | REQ-P4-039 — Causal continuity obligations. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `REQ-P4-040` | REQ-P4-040 — Discriminating realization evidence. | P4-VO-14, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-01` | INV-P4-01 — No identity from causation. Causal ancestry or similarity alone never entails numerical identity. | P4-VO-07, P4-VO-12, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-02` | INV-P4-02 — No authority from causation. Causal effectiveness, competence or predicted utility never entails authorization. | P4-VO-08, P4-VO-09, P4-VO-12, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-03` | INV-P4-03 — No cause from sequence. Temporal precedence or correlation alone never entails causal influence. | P4-VO-02, P4-VO-11, P4-VO-15 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-04` | INV-P4-04 — No effect from representation. A modeled or logged effect alone never entails actual execution or physical effect. | P4-VO-01, P4-VO-04, P4-VO-10, P4-VO-13, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-05` | INV-P4-05 — No fabricated order. Unknown causal ordering never entails proven precedence or proven concurrency. | P4-VO-03, P4-VO-04, P4-VO-05, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-06` | INV-P4-06 — No self-certification. An internal model's own assertions alone never establish independent causal validation. | P4-VO-06 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-07` | INV-P4-07 — Predecessor preservation. P4 cannot weaken inherited lifecycle, custody, constitutional, protected-operation, qualification or boundary constraints. | P4-VO-07, P4-VO-08, P4-VO-09, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-08` | INV-P4-08 — Domain non-substitution. A causal representation or assessment cannot independently establish a realized event. | P4-VO-01, P4-VO-06, P4-VO-10, P4-VO-11, P4-VO-15, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-09` | INV-P4-09 — Abstraction accountability. A higher-level causal attribution cannot evade declared lower-level dependencies, validation or governing constraints. | P4-VO-12 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-10` | INV-P4-10 — No simulated authority. Epistemic or simulated intervention cannot authorize corresponding realized effects. | P4-VO-08, P4-VO-13, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-11` | INV-P4-11 — Plasticity non-equivalence. Updating a model cannot by itself establish or authorize a change in the mechanism it models. | P4-VO-10 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `INV-P4-12` | INV-P4-12 — No unqualified causal-role inference. | P4-VO-14, P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-01` | CE-P4-01: correlation without causation. | P4-VO-02 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-02` | CE-P4-02: reversed cause/effect despite observed ordering. | P4-VO-03 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-03` | CE-P4-03: hidden common cause and observational equivalence. | P4-VO-02, P4-VO-15 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-04` | CE-P4-04: delayed or absent acknowledgment. | P4-VO-04 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-05` | CE-P4-05: apparent cycle with no well-founded event semantics. | P4-VO-05 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-06` | CE-P4-06: two competing paths with unknown ordering. | P4-VO-03 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-07` | CE-P4-07: model predicts an effect but no effect occurs. | P4-VO-01 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-08` | CE-P4-08: forged, stale or self-issued causal evidence. | P4-VO-01, P4-VO-06 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-09` | CE-P4-09: causal lineage mistaken for identity continuity. | P4-VO-07 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-10` | CE-P4-10: useful intervention mistaken for constitutional authority. | P4-VO-08 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-11` | CE-P4-11: administrative label hiding a lifecycle-affecting effect. | P4-VO-08 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-12` | CE-P4-12: cross-boundary observation mistaken for substrate-owned authority. | P4-VO-09 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-13` | CE-P4-13: a revised model retroactively changing historical facts. | P4-VO-10 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-14` | CE-P4-14: a successful predictor with invalid causal intervention semantics. | P4-VO-11 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-15` | CE-P4-15: accurate prediction despite a causally mistaken model. | P4-VO-11 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-16` | CE-P4-16: higher-level causal attribution without a valid abstraction correspondence. | P4-VO-12 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-17` | CE-P4-17: simulated intervention misrepresented as actual or authorized execution. | P4-VO-08, P4-VO-13 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-18` | CE-P4-18: model revision falsely asserted to alter realized mechanism or history. | P4-VO-10 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-19` | CE-P4-19: contributing condition misclassified as sufficient or necessary without scope. | P4-VO-14 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-20` | CE-P4-20: observationally equivalent causal models falsely adjudicated as uniquely identified. | P4-VO-15 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-21` | CE-P4-21: apparent emergent system-level effect asserted as a new authority or identity. | P4-VO-12 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-22` | CE-P4-22: Actual occurrence without any report. | P4-VO-01 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-23` | CE-P4-23: Actual occurrence with unknown locus or placement; unknown order remains unknown. | P4-VO-01, P4-VO-03 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-24` | CE-P4-24: Redundant sufficient mechanisms defeat a universal single-removal inference. | P4-VO-14 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-25` | CE-P4-25: Joint sufficiency differs from individual sufficiency. | P4-VO-14 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-26` | CE-P4-26: Context-dependent influence and irrelevant membership in a successful group. | P4-VO-14 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-27` | CE-P4-27: Indirect protected mutation hidden behind a model-update or simulation label. | P4-VO-08, P4-VO-13 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-28` | CE-P4-28: Unresolved effect analysis incorrectly treated as an empty effect set. | P4-VO-08 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-29` | CE-P4-29: Realized effect exceeds scope assessed before prior authorization. | P4-VO-08 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-30` | CE-P4-30: Constructive organization with consequential state, memory, coordination, regulation and feedback. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-31` | CE-P4-31: Logging-only history without consequential memory. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-32` | CE-P4-32: Message-only assembly without realized claimed integration. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-33` | CE-P4-33: External-service wrapper without decisive internal processing. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-34` | CE-P4-34: Redundant organization with group/trajectory contribution but no single-removal change. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-35` | CE-P4-35: Stored state restored while required causal relationship remains absent. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |
| `CE-P4-36` | CE-P4-36: Inconclusive organization evidence incorrectly classified as realization or absence. | P4-VO-16 | **OPEN:** elaborate typed sub-property and positive/negative witness for each relevant VO; D1 full clause controls. |


### 10.1 VO property-level control plan (distinct from assignment)

| VO | Typed semantic property / required negative discrimination | Current state |
|---|---|---|
| `P4-VO-01` | `Occurs(w,r)` independent of `Reports(e,r)` and `OccurrenceAssessment(r,f)`; false report and unreported real event. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-02` | `Influences(μ,A,Y,c)` only with declared interventions; common-cause correlation cannot establish it. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-03` | `Precedes_w` strict partial order; `Concurrent_w` requires order-completeness; unknown order remains unresolved. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-04` | Absence of acknowledgment does not entail `¬Occurs`; distinguish delayed, lost and absent acknowledgments. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-05` | Feedback mechanism cycles require distinct ordered occurrence witnesses; no `Precedes_w(r,r)`. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-06` | Provenance and evaluator independence are external evidence conditions; contrary evidence must be admissible. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-07` | Causal ancestry is not `SameEntity`; continuity needs predecessor authorized transition and lineage conditions. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-08` | `CoverageSound ∧ AssumptionsApplicable ∧ PriorGate` for protected-effect assessment; unresolved effects fail positive gate. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-09` | Boundary-classified NES/external effects cannot count as NNNC internal decisive processing. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-10` | `ModelRevision` changes representation not realized history; mechanism change is distinct and may overlap. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-11` | Predictive-equivalent models can diverge under `do`; predictive fit is not intervention validation. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-12` | `AbstractionAdequate` is property/domain-relative; predictive adequacy cannot imply intervention adequacy. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-13` | Simulated target effects differ from real computation effects; actual protected checkpoint write needs prior gate. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-14` | Actual contribution requires declared attribution rule; joint, redundant, gated and irrelevant members differ. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-15` | `Identified(f,q)` requires nonempty compatible-model set and unanimous causal-query value. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |
| `P4-VO-16` | Seven-field bound contract plus capability-relevant decisive organization, regulation, feedback, continuity, evidence; NC-01..05 distinct. | **SPECIFIED / NOT DISCHARGED**; source import and witness completeness pending |


### 10.2 Independent five-negative-control register

| ID | Required rejected inference | Counterpart / result |
|---|---|---|
| `P4-VO-16-NC-01` | Genuine but capability-irrelevant internal effect ⇒ capability realized | Relevant internal decisive contribution; illustrative predicate check only |
| `P4-VO-16-NC-02` | Nominal regulator ⇒ consequential regulation | Regulator alters relevant disposition; illustrative predicate check only |
| `P4-VO-16-NC-03` | Logging or abstract feedback loop ⇒ realized consequential feedback | Distinct ordered feedback occurrences; illustrative predicate check only |
| `P4-VO-16-NC-04` | Six-field / ambiguously bound contract ⇒ seven-field well-formedness | All seven applicable fields; illustrative missing-field mutation checks only |
| `P4-VO-16-NC-05` | System memory unrelated to capability ⇒ capability memory realized | Capability-dependent decisive memory; illustrative predicate check only |

## 11. Executed bounded illustrative checks — evidence and limitations

A dependency-free Python script `p4d2_round1_checks.py` was executed in the working environment, producing `NNNC-P4-D2-v0.3-bounded-check-results.json`. These are **hand-authored illustrative predicates**, not an encoding of the complete P4-D1 specification, not an independent solver, and not a substitute for independently assessed finite models. In particular the NC checks encode a simplified acceptance rule and do **not** prove that actual NNNC causal organization exists. They exercise distinction examples and the 3-node strict partial-order enumeration, not inherited transition signatures.

- Script result: **32/32 PASS**, 0 FAIL; 19 strict partial orders on three labeled nodes.
- `p4d2_round1_checks.py` SHA-256: `5edc948b2c55dd98ea6b08aa2d99e762d6d1698048f95d31939a008e17137070`.
- `NNNC-P4-D2-v0.3-bounded-check-results.json` SHA-256: `3fdcf54c112edce5d484891598a1fe7c47c95722f775f8b38f023a1004803e02`.
- Reproduce: `python3 p4d2_round1_checks.py > NNNC-P4-D2-v0.3-bounded-check-results.json` (Python standard library only).
- **Discharge status: ZERO P4-VOs discharged.** The source crosswalk is complete at identifier/assignment level only. Many tests remain schematic or unexecuted; no universal safety claim follows.

## 12. Remaining Round 1 acceptance blockers and bounded handoff

1. **Predecessor signature audit OPEN:** obtain and typecheck actual Phase 0–3 imported authority, custody, lifecycle, identity, qualification and boundary contracts. Never instantiate an uninterpreted predecessor predicate as `True` to prove authorization.
2. **Source semantic fidelity OPEN:** compare the full text of every multi-paragraph REQ/INV/CE with its typed property, including independently assessable subproperties; current excerpts and VO assignment are insufficient.
3. **Executable model completeness OPEN:** implement typed histories, causal models, evidence, intervention and seven-field realization in a reproducible reference model with positive and discriminating negative witnesses. The illustrative checks do not satisfy this requirement.
4. **Attribution and concurrency OPEN:** resolve probabilistic/preemptive scope, soundness of actual contribution, closed-vs-open occurrence order and infinite-history well-foundedness.
5. **Independent review NOT STARTED:** after Round 1 blockers, submit for adversarial review; do not advance adoption on the basis of this drafting milestone.
6. **Inherited obligations RETAINED:** P0-O01..O08, Phase 2 PF residuals, Phase 3 PAC-1 evidence reconciliation and PAC-2, plus P4-D1 deferred work remain tracked under the project-wide obligation protocol.

**Round 1 decision:** v0.3 is a stronger **traceability and illustrative-control candidate**, but **NOT a complete Round 1 verification candidate**. The next bounded increment is a typed executable semantic reference model and actual predecessor-signature ledger; if either cannot be completed within the defined gate, record a conditional stop rather than inflate verification status.

### v0.3 change record

Adds source-extracted identifier-complete 40/12/36 ledger, sixteen property-family records, five separate NC records, and reproducible illustrative finite checks with recorded hashes. Does not modify the adopted P4-D1 baseline, discharge VOs, or certify protected effects.


## 13. v0.4 bounded integrated reference-model supplement — operative within declared scope

**Revision status:** v0.4 ROUND 1 INTEGRATED REFERENCE MODEL CANDIDATE — DRAFT, NOT ADOPTED, NOT VERIFIED. This supplement supersedes v0.3 statements that *no* finite reference checks have been executed, but does not alter any governing Phase 4 D1 requirement or claim verification discharge. The inherited v0.3 ledger and all OPEN-D2 issues remain operative unless expressly narrowed here.

### 13.1 Executable typed fragment and exact limits

The accompanying dependency-free Python reference `p4d2_v04_reference.py` defines executable interpretations for: (a) finite strict partial orders and epistemically guarded concurrency; (b) finite two-input Boolean causal influence under controlled variation; (c) nonempty unanimity-based identifiability; (d) a synthetic protected-effect *assessment* gate; and (e) a seven-field realization-contract schema with independently fixed role requirements. These are finite interpretations of selected Phase 4 interfaces, not a comprehensive NNNC transition model.

The reference uses **sets of occurrence-pairs**, not timestamps, to interpret strict order. `classify_order` returns `ORDER_UNRESOLVED` for incomparable events absent a completeness premise. Its `CONCURRENT` classification under a `complete=True` flag is valid only if that premise is independently justified; the test does not establish the premise.

Causal functions are exhaustively enumerated over 2 Boolean inputs and 1 Boolean output (16 truth tables). `influences(fn,src)` means that a controlled flip of the designated input changes output in at least one admissible background. This does not establish actual contribution, preemption, probabilistic causation or real-world intervention feasibility. `identified(models,q)` requires a nonempty model family with unanimous answers; the family is supplied, not recovered from evidence.

### 13.2 Predecessor signature import ledger — inspected, not fully discharged

| Source | Exact located signature or contract | Phase 4 preservation rule | Audit disposition |
|---|---|---|---|
| P2-D2 v1.0 §3 imported signatures | `AuthorizedTransition: X×L×H×V→Bool` | Preserve original `x,l,h,v` and actual lifecycle scope | Source signature LOCATED; runtime bridge OPEN |
| P2-D2 v1.0 §3 imported signatures | `AuthorizedCustodyStep: X×K×K×L×H×V→Bool` | Do not infer custody authority from causal ancestry | Source signature LOCATED; Phase 0 semantic expansion OPEN |
| P2-D2 v1.0 §3 imported signatures | `ValidLocusAuthority: X×L×H×V→Bool` | Do not infer locus authority from model predictions | Source signature LOCATED; Phase 0 semantic expansion OPEN |
| P2-D2 v1.0 §3 imported signatures | `InvariantOK: X×H×V→Bool` | Must be expanded against applicable inherited invariants, not assigned true by fiat | Source signature LOCATED; expansion OPEN |
| P3-D2 v0.5.2 §I / §§authorization | `P2.AuthorizedTransition(x₂,l,h₂,v)` | Preserve unchanged four-argument call and same-operation correspondence; administrative relabeling cannot suppress lifecycle checks | Source contract LOCATED; effect/bridge completeness OPEN (PAC-2 inherited) |
| P0-D1 v1.4.2 / P0-D2 v1.4 | Positive NES support and protected-effect baseline | No new privilege from substrate support; retain prior authorization, recovery and physical-effect safety gates | Full exact-clause import OPEN |
| P1-D1 v2.0 / P1-D2 v0.2.1 | Qualification, entity boundary, governance and custody distinctions | Do not collapse NNNC identity into causal ancestry or evidence | Full exact-clause import OPEN |
| P2-D2 v1.0 conditional | PF-01, PF-10 and imported `Recon` | Preserve unresolved predecessor interface checks | OPEN, not discharged |
| P3-D2 v0.5.2 conditional | PAC-1 review evidence and PAC-2 predecessor audit | Do not claim independently certified predecessor completeness | OPEN / disposition to be reconciled |

**Critical interpretation:** The executable gate takes a caller-provided dictionary of scope and lifecycle decisions as *test inputs*, not an implementation of P0/P2/P3 imported predicates. Thus a synthetic positive gate result **cannot** count as a verified authorized operation. `ActualEffects=None` denotes unknown post-execution effects and does not prove that actual effects were contained; the executable routine is an *assessment fragment*, not a soundness certificate. In particular, the synthetic `GATE-EMPTY-COVERED` case does not assert that the real protected-scope set is empty.

### 13.3 Reproducible executed bounded checks

- Script: `p4d2_v04_reference.py`, SHA-256 `c7af1e5fd280d41da69c6070dd9e86c600aae63b8945e6a66c56bc61818932dd`.
- Results: `NNNC-P4-D2-v0.4-reference-results.json`, SHA-256 `95ebd6311661f8b973f8982b4595c994f7b6d203c5a8ee42578db64651f94e94`.
- Reproduction: `python3 p4d2_v04_reference.py > NNNC-P4-D2-v0.4-reference-results.json`.
- Executed results: **37/37 PASS**, **0 FAIL**; 19 strict partial orders on three labeled vertices; 16 two-input Boolean functions.
- Negative controls: seven missing-field mutations, incorrect capability binding, absence of each required organizational role, absent decisive internal contribution, and absent substantive success. These tests use a *synthetic interpretation* of the seven-field schema; they do not demonstrate independent field relevance, source-derived role completeness, or realized NNNC capability.
- Formal P4 verification obligations discharged: **ZERO**. The v0.3 32 illustrative checks and v0.4 37 checks are separate evidence packages, not additive independent proof counts.

### 13.4 Found limitations and targeted mathematical repairs for next gate

**V04-LIM-01 — Gate totality versus applicability.** A nonempty scope-decision dictionary in the fixture does not prove all `RequiredScopes(P)` are enumerated. An adequate next model must quantify over the actual derived scope set, require complete correspondence to predecessor import calls, and reject incomplete mappings.

**V04-LIM-02 — Effect analysis soundness.** No executable derivation of `CoverageSound` from operational semantics is provided. A declared coverage flag is not evidence of completeness; the full gate remains OPEN.

**V04-LIM-03 — Causal role interpretation.** Synthetic role flags do not establish world-level realized contribution. The next model must encode transitions, causal comparisons, redundant and joint contribution under a declared attribution rule, and counterfactual assumptions.

**V04-LIM-04 — Seven-field schema adequacy.** The synthetic validator tests structural presence and simple consistency only. The governing `ContractWellFormed` additionally requires relevance, typed dependencies, evidence limitations, intervention permission, coverage and justified external declarations. The executable validator SHALL NOT be substituted for that normative predicate.

**V04-LIM-05 — Predecessor completeness.** Signature location is not signature-and-semantics audit. Phase 0 and 1 exact definitions, Phase 2 `Recon` and Phase 3 bridge obligations require independent clause-by-clause import verification.

**V04-LIM-06 — Complete source-to-property ledger.** The v0.3 identifier crosswalk remains insufficient for a complete property-level semantic audit of all REQ, INV, CE, VO and NC clauses.

### 13.5 Bounded Round 1 gate and stop rule

Round 1 remains **IN PROGRESS**. Before independent Round 2 review, either (a) supply a fully source-audited imported-signature ledger, complete clause-level property crosswalk and discriminating executable semantic fixtures for the declared core; or (b) explicitly stop Round 1 with unresolved material blockers and submit only a *limited-scope review candidate*, never an acceptance-ready mathematical contract. A finite test result may justify a narrowly scoped fixture claim but not discharge the governing P4-VO register without a separate reviewed discharge argument.

### 13.6 Revision record

`v0.4`: Retains v0.3 intact as an archival predecessor and adds a bounded executable reference-model interpretation, actual recorded results, located predecessor signatures, a six-item limitation register and an explicit bounded stop gate. No adoption or implementation certification asserted.


**v0.5 revision overlay:** §7F and the updated control header are operative additions to v0.4. Historical v0.4 status/result statements elsewhere in the consolidated text describe that earlier increment; they are not current final review or adoption claims. **v0.5 is DRAFT, NOT ADOPTED, NOT VERIFIED.**


## 14. v0.6 — capability-realization semantic ledger and bounded discriminators

**Revision control.** This section adds prospective mathematical semantics and executed synthetic witnesses without changing the adopted P4-D1 obligations, predecessor interfaces, or any earlier v0.5 open disposition. The v0.6 reference script and JSON result are companion evidence; neither constitutes proof of real implementation or VO discharge. This is a **bounded Round 1 stopgap**, not a claim of complete Round 1 closure.

### 14.1 Source-linked clause-level obligations (REQ-P4-035..040)

For candidate `s`, capability `k`, context `c`, and versioned contract `r`, define independent applicability `Required(k,s,c)` from the governing requirements and candidate claims, prior to evaluating `r`. Let `Field_i(r,k,c)` be typed, substantive and consistent descriptions for the seven fields `(a)..(g)` in P4-D1 §5B REQ-P4-035. A nonempty label is insufficient: each field must have declared typed referents, binding and an assessable semantic condition. The finite fixture checks only presence, **not** these substantive semantics.

`ContractWellFormed(r,k,c) := UniqueBinding(r,k,c) ∧ ∧_{i=a}^g Field_i(r,k,c) ∧ CoverageOfRequiredRoles(r,k,c) ∧ ConsistentDependencies(r,k,c)`.

`RelevantContribution(s,k,m,c)` requires a declared actual-contribution rule and a capability-relevant contrast; it does **not** follow from internal location or mere successful output. `DecisiveOrganization(s,k,r,c)` requires a nonempty set of relevant contributing internal mechanisms, correctly bound state and dependencies, and every independently applicable role; role satisfaction must be evaluated at the capability scope. `RealizationAssessed` is evidence-relative, and `CapabilityRealized` is a world/model-relative semantic claim: neither implies the other without a justified bridge.

| Source | Required semantic discrimination | Positive witness target | Negative witness / counterexample | Current disposition |
|---|---|---|---|---|
| `REQ-P4-035`, D1 §5B | Seven substantive fields, unique capability binding, independent mandatory applicability, decisive internal causal contribution; external/NES effects separately typed | Bound seven-field contract and internally decisive group | Missing seventh field; ambiguous binding; consequential but irrelevant internal activity; external-only wrapper | Synthetic field/binding and internal-relevance checks **PASS**; substantive typed-field validity and world bridge **OPEN** |
| `REQ-P4-036`, D1 §5B | Internal state affects *later* processing; memory must be consequential where applicable | Ordered state-mediated transition whose retained value changes subsequent processing | Logging/retrieval without effect; conflating observation with state | Synthetic memory-effect discriminator **PASS**; temporal state-transition witness **OPEN** |
| `REQ-P4-037`, D1 §5B | Coordinated dependencies contribute to the whole capability, not mere graph connectivity | Joint processing where changing a mechanism group alters decisive outcome | Message-only assembly; pairwise connectivity mistaken for whole-capability integration | Synthetic coordination discriminator **PASS**; typed group-process witness **OPEN** |
| `REQ-P4-038`, D1 §5B | Regulation changes selection/inhibition/allocation; feedback acts on distinct later occurrences | Consequential regulator and ordered feedback chain | Nominal regulator; abstract loop without realized distinct occurrences | Synthetic controls **PASS**; integrated regulation-conflict and occurrence model **OPEN** |
| `REQ-P4-039`, D1 §5B | Restoration of data and of necessary causal relationships are independent; capability continuation is not identity | Preserved/reconstructed relationships across permitted transition | Restored bytes with missing causal link | Synthetic missing-link control **PASS**; exact P2 continuity and authority bridge **OPEN** |
| `REQ-P4-040`, D1 §5B | Discriminating comparisons with explicit assumptions, intervention permissions and evidence limitations; redundancy allowed | Redundant OR: joint group removal changes outcome despite single ablation being nondiscriminating | Single ablation used as universal test; unknown evidence declared success | Finite OR and unknown-evidence controls **PASS**; provenance, permission and stochastic contrasts **OPEN** |

**Seven required D1 §5B.2 scenarios:** (1) constructive organization, (2) logging-only memory, (3) message-only integration, (4) external-service wrapper, (5) redundancy and group contrast, (6) restored state with broken causal relation, and (7) inconclusive evidence are represented as *synthetic finite fixtures*. This is scenario-presence coverage, not semantic verification of deployed causal organization.

### 14.2 Exact independent negative-control crosswalk

| ID | Negative control | v0.6 fixture | Limitation |
|---|---|---|---|
| `P4-VO-16-NC-01` | Internal causal effect irrelevant to capability | `NEG-IRRELEVANT-INTERNAL` | Relevance represented as independent fixture input, not derived from causal graph |
| `P4-VO-16-NC-02` | Nominal regulator without consequential effect | `NEG-NOMINAL-REGULATOR` | No policy competition modeled |
| `P4-VO-16-NC-03` | Logging or abstract feedback without consequential realized loop | `NEG-ABSTRACT-FEEDBACK`, `NEG-LOGGING-ONLY` | No full event-history trace |
| `P4-VO-16-NC-04` | Six-field or ambiguous contract binding | `NEG-MISSING-FIELD`, `NEG-AMBIGUOUS-BINDING` | Field contents not semantically validated |
| `P4-VO-16-NC-05` | Unrelated system memory used to claim capability memory | `NEG-IRRELEVANT-MEMORY` | No independent counterfactual memory trace |

**Non-substitution controls:** `POS-MEMORY-NOT-REQUIRED` prevents imposing capability-specific memory on a capability not requiring it; `NEG-PARTIAL-NOT-FULL` and `NEG-UNTESTED-MANDATORY` prevent partial study or omitted mandatory roles from proving complete qualification. These fixtures do not alter the five-conjunct `MinimumOrganization` floor, which must be separately assessed. The `required` input is independently supplied and is never computed from contract validity.

### 14.3 Executed evidence, reproducibility and non-claims

Execute `python p4d2_v06_realization_model.py` from an environment containing the adopted `NNNC-P4-D1-v0.4.1-ADOPTED.md` in `/mnt/data`. The companion JSON `NNNC-P4-D2-v0.6-realization-results.json` records the actual test IDs, expected/observed results, count and SHA-256 of the source file. **25/25 bounded checks passed, zero failed.** This includes six source-clause presence checks, not six semantic verifications. The model's `state_effect`, `coordination_effect`, `decisive_internal`, `feedback_effect` and other truth values are stipulated fixture inputs. Therefore a passing test verifies only that the *assessment logic* responds to those inputs as declared; it does not independently establish that the input conditions hold in any NNNC. No real protected effects were executed. **P4-VO discharged: 0/16.**

### 14.4 Round 1 closure decision and bounded stop

**Round 1 is not complete.** Existing v0.5 `OPEN-D2-01..08` remain open except for additional *synthetic discrimination coverage* under `OPEN-D2-01/02/03`; no obligation is silently discharged. The full 40/12/36/16+5 inventory in §10 is still an administrative mapping, not a clause-complete formula/witness/oracle proof ledger. In particular, positive organization remains dependent on stipulated mechanism-effect facts, and exact Phase 0–3 semantic import is incomplete. These are explicit blockers to calling this a complete mathematical verification candidate.

**Stopgap / handoff:** Stop adding isolated Boolean fixtures. The next bounded increment, if authorized, must deliver (i) one typed, multi-sort, state-transition reference model deriving state, memory, coordination, regulation and feedback contributions from transitions rather than supplied flags; (ii) independent causal contrasts and negative controls for each of the seven D1 §5B.2 scenarios; (iii) a formula/witness/oracle ledger for the entire 40/12/36/16+5 inventory with explicit unresolved entries; and (iv) a precise predecessor-import blocker report where a source-defined relation cannot be integrated. If this cannot be achieved in the next increment, close drafting as **INCOMPLETE / REVIEWABLE WITH BLOCKERS**, and do not claim Round 1 acceptance or request adoption.

**v0.6 disposition:** DRAFT; finite illustrative evidence only; no independent adversarial review, no machine-checked theorem, no formal VO discharge, no adoption, and no protected-effect deployment assurance.


## 15. v0.7 — bounded integrated transition model and Round 1 stop disposition

**Status:** DRAFT — INCOMPLETE / REVIEWABLE WITH BLOCKERS. This section supplements and does not silently supersede §§0–14. All P4-D1 clauses remain governing. This is the final bounded Round 1 development increment under the v0.6 stop rule; no automatic further drafting rounds are authorized.

### 15.1 Typed executable reference interpretation

The companion `p4d2_v07_transition_model.py` defines a finite deterministic `State` product with retained memory, sensor, regulator, coordinator, internal mechanism, external service, causal link, restoration marker, log and output. Transition actions `sense`, `decide` and `feedback` generate distinct indexed states in a history. The outcome of `decide` is derived from preceding state and mechanism gates, rather than supplied as a `state_effect` or `coordination_effect` Boolean. `contrast` evaluates a declared single-field intervention by replaying the same action sequence with one altered field; it is a *toy-model counterfactual*, not a physical intervention or a universal attribution criterion. A separate OR fixture checks group redundancy.

The model establishes neither capability realization for NNNC nor identity, authority, custody, or qualification. In particular it has **no imported authorization implementation**. Successful toy outputs cannot authorize protected effects. `restored=True` is not an identity or continuity witness. Logs are intentionally irrelevant to decisions. Feedback is represented by distinct history positions; the reference model does not resolve asynchronous or open-world ordering.

### 15.2 Bounded evidence and limitations

The executed companion results report **20/20 passing assertions, 0 failures**. These checks include constructive internal state use, a later decision influenced by retained memory, coordination and regulator contrasts, an external-only success negative control, logging-only and message-only controls, broken restored causal link, distinct feedback steps, and redundancy group contrast. The check named `no_authority_inferred_from_success` is a *non-integration sentinel*, not a positive proof of authorization preservation. Some cases exercise only model-level distinctions. No empirical evidence, predecessor-wide model check, or machine-checked theorem was produced. **P4 verification obligations discharged: 0/16.**

### 15.3 Property ledger — completeness versus discharge

The companion `NNNC-P4-D2-v0.7-property-ledger.json` contains explicit records for the 40 `REQ`, 12 `INV`, 36 `CE`, 16 `P4-VO` and five `P4-VO-16-NC` identifiers (**109 records**). It preserves source excerpts from v0.6 where available, assigned VO mappings and **OPEN** placeholders for formal formula, positive witness, negative witness, oracle and inherited imports. The ledger is *inventory-complete but semantically incomplete*: source excerpts are not full clauses, generic placeholders are not proofs, and no row is discharged. The exact P4-D1 source governs if any excerpt differs.

### 15.4 Predecessor integration blocker report

1. **Phase 0:** protected effect and session-fencing obligations P0-O01–O03 remain engineering blockers. Native authorization, ledger, custody and effect-scope proof interfaces are not implemented in this reference model.
2. **Phase 1:** ontology and qualification are not mechanically imported; no model-to-world bridge or full positive-support/role semantics are established.
3. **Phase 2:** `AuthorizedTransition(x₂,l,h₂,v)` remains an imported four-argument predicate, not a Boolean or a test-suite output; lineage, identity and continuity semantics are not reimplemented.
4. **Phase 3:** constitutional authorization, delegation and protected operation rules are not instantiated. Adopted C1 and conditional D2 require an exact semantic import audit; PAC-2 remains open.
5. **Phase 4:** actual attribution beyond the toy deterministic contrast, preemption, stochastic inference, non-vacuous causal abstraction, concurrent feedback, full seven-field typed substantive checks, and independent evidence provenance remain open.

### 15.5 Mandatory stop and handoff

**Round 1 drafting stops here as INCOMPLETE / REVIEWABLE WITH BLOCKERS**, pursuant to the bounded stop rule stated in v0.6 §14.4. A narrowly scoped **diagnostic** independent review may examine the typed core, ledger adequacy, and listed blockers; this document must **not** be presented for acceptance as a complete mathematical verification contract. Round 2 reviewers should first decide whether the missing semantic imports and clause-level formulas are acceptance-blocking (presumptively yes), identify any mathematical contradictions, and return a finite prioritized correction list. Round 3 may only begin after that review and an explicitly bounded correction plan. No obligation is waived, deferred without registration, or silently discharged.

**v0.7 disposition:** Not adopted, not independently reviewed, no formal VO discharge, no protected-effect assurance.

<!-- END EXACT P4 SOURCE -->

# Part II — Operative v0.9.1 bounded causal-realization formalization and alignment

## CW.0 Authority, precedence and honest status

**INCOMPLETE / LIMITED-SCOPE REVIEW CANDIDATE — NOT ADOPTED; 0/16 VOs DISCHARGED.** Governing adopted D1 remains v0.4.1. Proposed D1 v0.4.2.1 accompanies this candidate; its CW clarifications require separate adoption. Most of this finite handoff directly formalizes already adopted REQ-P4-035–040 and the controlling D2 v0.8 N0–N8 corrections.

Part I preserves exact supplied v0.8 bytes, including its frozen v0.7 appendix and historical evidence. N0–N8 remain controlling over inconsistent v0.7 clauses. This part supplies the expressly scoped current definitions below and updated source/status readings; it does not reactivate superseded historical equations or remove unresolved obligations. N7's completed-D2 gate is retained, not weakened. This is one user-authorized bounded current-phase pass, not another automatic incremental drafting loop.

The five historical v0.3–v0.7 scripts were not attached, but were recovered from project files during this pass. Their exact bytes are archived and rerun with a documented IO-root-only adapter; results reproduce 32/37/30/25/20 passing diagnostics. No historical case is retired. The new standard-library code is a separate declared reference interpretation with its own controls, finite universe and independent task oracle; historical counts are not accumulated into its result totals.

## CW.1 Carriers, binding and dependency order

Retain N0–N5's disjoint world/model/evidence domains, typed source assignments and exact predecessor contracts. New presentation sorts are WitnessID, BuildRef, ContextRef, ContractVersion, MechanismRef, StateRef, RoleRef and OccurrenceRef; these do not identify P1 instances, P2 individuals, P3 principals or scopes by name. `CausalWitness` is `(id,subject,build,capability,contextDomain,contractVersion,worldRef,modelRef,occurrences,dependencies,comparisons,evidence,assumptions,claimScope)` with typed projections. A simulated world is marked SIMULATED_REALIZATION; the code supplies no physical-world correspondence proof.

| Schema / function | Signature | Meaning / implementation limit |
|---|---|---|
| Applicable | K×S×C→Bool | N2 governing required capabilities plus additional claims; independent of contracts, observed success and evidence. General source registry import remains OPEN. |
| RequiredRoles | K×S×C→Fin(RoleRef) | N2 governing role requirements, not selected by successful ablation. The finite interpretation has a fixed memory-guided role set and a separate input-gate role set. |
| OperativeContractFor | R×K×S×C→Bool | N2 independently selected active/version/context/subject/capability record; no/invalid/multiple operative records cannot satisfy coverage. The fixture implements one explicit active version/context; general precedence registry remains OPEN. |
| ContractWellFormed | R×K×C→Bool | Seven-field declared syntax, typed references, domain/binding/dependency consistency; no query of world realization or assessment. Finite checker limited to its exact grammar. |
| Trace | Wiring×Context→SimulatedHistory | Sense/decide/feedback operations produce immutable state transitions and distinct ordered occurrences under declared equations. |
| RoleWitness | Wiring×RoleRef→Fin(ContextRef) | Actual finite wiring plus controlled contrasts, independent of qualification. Feedback additionally needs a changed state passed through a distinct occurrence to later processing. |
| RelevantInternalOrganization | S×K×R×C×W→Bool | N2 world-level schema under applicable attribution/correspondence interpretation; finite subset checks source boundary and required trace contrasts only. General actual-attribution soundness is OPEN. |
| SubstantiveSuccess | S×K×C×W→Bool | N2 independently fixed target; fixture uses an enumerated task table, separately written from engine equations. |
| CapabilityRealized | S×K×R×C×W→Bool | N2 conjunction of applicability, unique well-formed contract, required relevant organization, substantive success and applicable inherited conditions. The code's local result is finite-model satisfaction only; unresolved real inherited conditions prevent a complete NNNC assertion. |
| WitnessAssessment | CausalWitness×F→Assessment | Bound observation/provenance/protocol and independent criteria; no observation defaults to UNDETERMINED. SUPPORTED is under the specified simulated-world assumptions. |
| CapabilityContinues | K×S×C×S×C→Bool | Native relationship-preservation/reconstruction schema; no SameEntity consequence. Only paired finite before/after wiring controls are executed here. |

Dependency order is unchanged: governing contract/claims → applicability and roles; declared independent registry → operative contract; syntax/consistency → well-formedness; simulated actual wiring/state/history and separately declared comparisons → relevant role participation; independent target → substantive success; conjunction → local realization; then qualified observations → assessment. Witness generation or a desired verdict is never an input to Applicability/RequiredRoles. The typed dependency graph is inspectable in DEPENDENCIES.json; it is not a full use-site or theorem-prover typecheck of every predecessor/prose clause.

## CW.2 Positive organization witness under a declared finite interpretation

The fixture has internal retained memory M, sensor input U, regulator G, a selecting/combining mechanism, output D and a feedback operation. For the memory-guided capability the normal transition is `D=G·(M XOR U)` followed at a later occurrence by `M:=D`. A separate input-gate capability uses `D=G·U`; it legitimately lacks capability-specific memory requirements while the separate system-level memory floor remains.

One processing cycle is three distinct occurrences: sense, decide, feedback. Sequential cuts in this fixture are an explicit finite execution interpretation, not a universal synchronous architecture. The main context universe is 16 cases: initial M∈{0,1}, two binary inputs (four sequences), and G∈{0,1}. The task oracle is a separately enumerated eight-row (G,M,U) table replayed to form the target trajectory; it does not call the engine's decision function. Contrasts change a declared wiring/state condition while holding the context/input trajectory fixed. Outcome equality and state/provenance relationships are checked independently.

Role contrasts identify the declared contexts where a role can affect decisive processing; they do not attribute every role as an actual cause of every individual output, including inhibited/zero-output cases. General outcome-specific ActualContribution remains separately scoped. The five system-level role conditions remain cumulative: consequential state, required memory, capability-relevant coordination, consequential regulation and feedback. The finite role checks require the base wiring actually to contain the relevant path; adding a missing path in a comparison does not prove it was already realized. The feedback check requires an actual memory-changing write and a later consuming decision, not a logging append. Capability-relative roles are assessed separately from that system floor. Core/world generation, oracle output, role comparison evidence and certification remain different objects.

The seven-field contract remains exactly REQ-P4-035(a)–(g), with metadata outside those seven fields. The finite checker validates: operational capability/mode/domain; declared mechanism/state referents; well-typed complete required dependency endpoints; named source-group/target/attribution grammar; explicit NES/external boundary; continuity condition categories and preserved links; context-complete comparison design, assumptions, evidence limits and separate absence of real intervention authority. It never concludes actual realization merely from a structurally valid record. Its fixed grammar is not a complete semantic validator for arbitrary future contracts.

`WitnessSupports` is a presentation relation requiring a bound operative contract, covered declared contexts, actual finite traces, capability-relevant roles, matching substantive target, valid occurrence/state seams, qualified observation records and explicit limitations. It is not another primitive that redefines N2 realization. Alternative adequate evidence formats remain possible. No witness alone entails actual NNNC realization, P1.LevelNConforms, P2 identity or protected authority.

Exported witnesses include exact wiring/build, context domain, full positive trajectory, reference/observed outcomes and role-contrast contexts. Complete sampled trajectories cover only this finite discrete domain. Whole-interval, stochastic/preemptive and real-domain claims need their own protocols and are not supplied by interpolation or a success flag.

## CW.3 Nonvacuity, correspondence and epistemic results

N2 coverage is independent of successful realization. Required capabilities remain required when contracts are absent, malformed, inactive or ambiguous. Historical/context-distinct contracts may coexist without counting as operative; the implemented registry has a deliberately fixed active context/version grammar. Four explicit coverage controls return fail/fail/fail/pass for absent, sole malformed, multiple operative and unique valid records. All seven field-removal controls and typed/inconsistent referent mutations are distinct from actual wiring failures.

Actual finite world transitions are separate immutable values from the mechanism model, predictions and evidence. The evidence fixture must carry the bound build hash, subject, world reference, complete context set and actual finite trace records under the declared observer protocol. Evidence absent, conflicting, unvalidated, candidate-self-issued or bound to another build/context returns UNDETERMINED. It cannot create an occurrence or silently replace the actual trace. Qualified positive evidence can support only the declared simulated-world claim; it does not authenticate a physical correspondence.

A fully known countermodel can refute the **bound finite-model realization claim**. That is not a proof that an actual NNNC does not exist. Local OrganizationAssessment values map exactly: SUPPORTED→SUPPORTED_UNDER_ASSUMPTIONS; REFUTED→REFUTED_UNDER_ASSUMPTIONS; UNDETERMINED→UNDETERMINED. PROPOSED remains the pre-adjudication causal-claim state, not a fourth value of D1's local three-valued organization assessment.

Disconnected memory/housekeeping activity, log-only feedback, disabled combining, a regulator affecting only unrelated activity, an external-service wrapper, restored data with a broken dependency, and incomplete evidence have separate controls. Tests do not infer actual individual contribution solely from membership in a successful group. Ordinary internal role contrasts and substantive success are both needed; neither substitutes for the other.

## CW.4 Occurrence order, feedback and the infinite countermodel

N1's well-foundedness axiom is retained. The finite checker validates irreflexive transitive realized precedence on explicitly declared finite domains, with all finite subset/well-foundedness consequences bounded to that domain. Unknown observational order is not a complete relation. Established concurrency additionally needs an explicit independently interpreted relevant-order warrant; a supplied flag alone does not create that warrant. The finite warrant identifier is a declared closed-observer fixture assumption, not real infrastructure assurance.

For the required mathematical infinite countermodel, take occurrences {e_n:n∈Z} and e_i≺e_j iff i<j. Irreflexivity and transitivity hold, hence no finite cycle. But the nonempty set of all occurrences has no predecessor-minimal member: e_(n−1) is a strict predecessor of every e_n. Thus the relation is not well-founded and violates N1 despite acyclicity. This argument, not finite enumeration, supplies the countermodel. It is not a machine-checked proof of admissibility for arbitrary infinite histories.

A recurrent abstract model can unfold into distinct finite occurrences. It cannot justify e≺e, a cycle in actual occurrence history, or a whole infinite completion from a valid finite prefix. Delayed/missing acknowledgements remain evidence gaps, not non-occurrence.

## CW.5 Sufficiency, group comparisons and identification

N3's SourceCondition remains a finite consistent partial assignment, including the empty assignment. The executable finite interpretation evaluates a declared deterministic Boolean model on a separately nonempty background domain with source values overridden by the intervention. Sufficient requires the target in every such background. MinimalSufficient checks every proper subassignment, including empty. Empty/invalid background or intervention inputs yield no supported sufficiency result; neither vacuous universal truth nor a missing model establishes a cause.

OR redundancy, AND joint sufficiency and context-gated A∧G are separate models. In OR with A=B=1, removing either alone can leave the outcome unchanged while joint removal changes it. This establishes a group-level contrast, not a universal theory that each actual group member contributed. Irrelevant Z must not acquire contribution from group membership. Preemption, stochastic causal attribution and physically inadmissible interventions remain explicit OPEN scopes; none is filled by these Boolean controls.

Two structures X:=U,Y:=X and X:=U,Y:=U agree observationally for binary U but disagree under do(X:=0) at U=1. Nonempty model-family unanimity may support an identified query only within the independently justified family; an empty family or observational fit alone does not. Claim-relative abstraction must name context/intervention/observable preservation. Predictive agreement does not imply intervention, mechanism or explanatory equivalence. The code demonstrates this countermodel, not general real-world identification.

## CW.6 Effect coverage and exact predecessor bridge

A finite closed operation graph declares each operation's own effects and invoked operations. The analysis computes the union of effects over the complete reachable graph, including indirect calls; a missing operation makes coverage unresolved. This is derived finite-program coverage, not a caller-provided “complete” Boolean. Actual runtime code/assumption correspondence remains external. Post-execution unavailable effects are not an empty observed set; actual effects outside the envelope are a coverage failure, not retroactive permission to widen it.

The adapter invokes the copied current Phase 3 finite guard from the confirmed/adopted P3 package and, where lifecycle effects apply, forwards the exact `(occurrence,locus,history,ruleVersion)` to a typed local representation of the imported P2 call. Missing, mismatched, denied, unknown or malformed results cannot yield the conditional positive result. That callback is a controlled import fixture, not a redefinition or validation of P2.AuthorizedTransition. The observed operation/event correspondence must be declared; string equality alone is no physical proof.

The conditional output is deliberately named `SUPPORTED_IN_FINITE_IMPORT_FIXTURE`. Every result separately states `runtime_authorization=NOT_ESTABLISHED`. This avoids promoting a Boolean stub into real authorization. Complete real import semantics, source-integrated effect discovery, authenticated actor/session/ledger guarantees, protected execution and the relevant P2/P3 bridges remain OPEN. P0-O01–03 still block deployment assurance. A simulation's actual computation effects are analyzed separately from its represented hypothetical effects; changing the label cannot erase a protected write.

The copied P3 model includes the adopted lifecycle-activation and provisional custody/commitment/role/competence dispatch corrections. It is provenance-bound to the confirmed P3 source, not automatically a production enforcement implementation.

## CW.7 Current predecessor alignment and obligations

| Governing source | Current Phase 4 constraint | Remaining owner/scope |
|---|---|---|
| P0-D1 v1.4.2 / D2 v1.4 | NNNC–NES ownership boundary, strict prior protected effects, P0-SUP-01–08 support/outcome/evidence distinction; no support loss privilege | P0-O01–08, original engineering/verification owners; O01–03 deployment blockers |
| P1-D1 v2.3.1 / D2 v0.5.1, adopted | Required roles/links and independently governed interpretations; constitutive unity necessary for Level N; 18 slots and all other prerequisites cumulative | P1 VO-01–22, legacy cases, domain realization and actual registry/evidence/continuum assurance |
| P2-D1/D2 v1.1.1, adopted | Positive history/seams, seven preservation/six release conditions, no identity/authority from causation, exact authorization tuple; E-1 accessor textual correction closed | P2 PF/VO/C/O and PC-VO inventories; universal/real effect/import/custody proofs OPEN |
| P3-D1 v0.2.7.1 / D2 v0.5.3.1, adopted | C1 general/lifecycle separation, effect-derived checks, immutable prior authority, provisional isolation and enacted-governance evidence | PAC-2, original and PG VOs/import/runtime proofs OPEN; PA-03 remains deferred |
| P4 D1 v0.4.1 adopted; proposed D1 v0.4.2.1 | All existing 109 identities, minimum organization and capability-specific success remain; new witness clarification does not substitute for those conditions | DEFER-P4-01–06, OPEN-D2-01–08; original owners retained |

This table specifically supersedes the historical old-version/status readings in D1 control/§0.2 and D2 control, N5, §7F/13.2/15.4; underlying native signatures remain subject to current operative predecessor amendments. Older PAC-1 “review not started” descriptions are historical: P3 focused review and targeted correction/adoption are recorded; PAC-2 remains open. P4 does not certify or reopen P3's adoption. Current enacted-governance evidence does not supply general causal-mechanism identification.

Support availability never determines duty applicability or factual outcome by itself. This revision has no implemented P0 scheduler/progress guarantee. Source ownership is not reassigned; unresolved imports remain open. Unknown imported truth cannot be set to true to prove a positive dependent real conclusion.

## CW.8 Verification ledger, semantic migration and explicit blockers

The current PROPERTY-LEDGER.json contains 109 distinct records: 40 REQ, 12 INV, 36 CE, 16 VO and five NC. Each retains its source clause(s), relevant supplemental source blocks, current formal hook or explicit blocker, named controls where executed, assumptions/finite scope, owning obligations and separate inventory/specification/test/review/discharge fields. A link to a test means only its explicitly stated subproperty was exercised; it is not complete coverage of every multi-paragraph source clause. Full independent sub-obligation semantic audit is still OPEN-D2-02/FV-09, not “done” because the count is correct.

The recovered original scripts and all 144 historical diagnostic case identities are retained and rerun; MIGRATION-LEDGER.json records their exact result/source and scoped new counterparts. Only their hard-coded /mnt/data IO root is redirected into an isolated folder via an explicit AST adapter; tests, expected outcomes and archived source bytes remain unchanged. This is rerun evidence, not recreation of missing originals. No historical property is retired in favor of an asserted unproved equivalent. General sub-obligation semantic adequacy remains FV-09/OPEN-D2-02. There is no numeric parity rule.

SPECIFIED, TESTED, INDEPENDENTLY_REVIEWED and DISCHARGED are separate dimensions. All 16 VOs remain NOT_DISCHARGED. New finite tests do not authorize a status change or nonapplicability. FV-RESULTS.json records bounded editorial execution versus material missing evidence; it does not invent an independent new reviewer verdict. Any source conflict is entered in PREDECESSOR-IMPORTS.json rather than resolved by Phase 4 precedence.

## CW.9 Existing FV gate and bounded disposition

The N7 completion condition is unchanged. This pair is prepared for the already-planned focused verification/review, not offered as a completed mathematical D2. It stops at **INCOMPLETE / REVIEWABLE WITH BLOCKERS** if full typed/import semantics, clause-level audit, meaningful historical migration or required authorized VO discharge cannot be established. These are distinct from later-domain implementations that D1 explicitly defers. Their exact current evidence and limits are in FV-RESULTS.json and OPEN-OBLIGATIONS.json.

No further isolated-test round is automatically scheduled. Next: one focused review of this current pair/package against the existing 12 FV conditions and the stated finite subset, then only bounded disposition/repair of concrete findings under Architect authorization. Neither preparation nor a favorable limited review adopts either new document. A separate explicit Architect decision is required for any adoption, with its precise completed or conditional scope recorded.


## Targeted repair issuance — 25 October 2026

The paired v0.4.2.1/v0.9.1 issuance corrects four fixture/ledger discrepancies without adding or weakening requirements. State mediation uses a sense-to-decision sensor-state path independent of retained memory; input-gate requires state, coordination and regulation. Organization assessment accepts explicit required/claimed applicability, treats missing/malformed/ambiguous operative coverage as UNDETERMINED and forwards the exact capability and subject. Lifecycle dispatch follows the P3 flag, context and effect-tag routes and cannot skip its P2 callback. REQ-P4-007 and REQ-P4-024 now have partial control routes. See TARGETED-REPAIR-REPORT.md and CA-T09/12/17/20. These repairs do not discharge FV-05, FV-08, FV-09 or any VO. D1 awaits Architect adoption consideration; D2 remains INCOMPLETE / NOT ADOPTED.


## Current finite evidence and gate disposition

Fresh diagnostic reference checks: **20 groups / 207 assertions, all PASS**. Five historical suites were recovered and rerun with a documented IO-root-only adapter: 32/37/30/25/20 passing diagnostics; no historical test was retired or silently replaced. FV editorial execution: **9 bounded PASS / 3 BLOCKED** (FV-05,08,09); earlier user-supplied focused review received; targeted repair confirmation pending. **0/16 VOs discharged. Completed-D2 gate remains UNMET — INCOMPLETE / REVIEWABLE WITH BLOCKERS.**

| Control | Assertions | Executed scope |
|---|---|---|
| CA-T01 | 34 | 16 contexts: actual finite six-occurrence trajectories versus separately enumerated target table |
| CA-T02 | 14 | Four N2 contract cases, seven field removals and malformed operative binding cannot erase coverage |
| CA-T03 | 8 | Typed/referential and context-specific content mutations in each of seven finite contract fields |
| CA-T04 | 5 | NC-05/CE-31: retained/logged or unrelated memory lacks decisive later memory path |
| CA-T05 | 4 | NC-01/CE-32: real housekeeping/log activity and connected declared graph do not establish capability organization |
| CA-T06 | 3 | CE-33: substantive external-only success is not internal decisive processing |
| CA-T07 | 4 | NC-02: nominal disconnected regulator versus consequential processing inhibition |
| CA-T08 | 5 | NC-03: consequential feedback state write to later decision versus logging-only path |
| CA-T09 | 13 | CE-35: data equality without relationship continuation; legitimate memory-independent capability does not waive system floor |
| CA-T10 | 12 | 19 finite strict partial orders and self/cycle negatives; bounded arithmetic checks do not prove infinite well-foundedness |
| CA-T11 | 6 | Unknown versus warranted closed concurrency and an actual simulated occurrence without a report |
| CA-T12 | 17 | CE-08/36: explicit bound trace observations, no default support, independent-fixture limits and unchanged actual history |
| CA-T13 | 17 | Empty proper subset, nonempty backgrounds, OR redundancy/AND joint sufficiency/gated context/irrelevant Z; no general actual causation claim |
| CA-T14 | 5 | Observational equivalence versus distinct intervention outcomes; nonempty conditional identification |
| CA-T15 | 2 | Claim-relative abstraction: preserved passive predictions do not entail intervention adequacy |
| CA-T16 | 8 | Indirect simulation effects derived from complete finite program, actual unavailable/out-of-envelope distinguished; no runtime authorization |
| CA-T17 | 20 | Exact four-argument lifecycle correspondence; denial/unknown/malformed/missing bridge cannot promote dependent assessment |
| CA-T18 | 12 | P0 support/outcome/applicability separation only; no live scheduler, attribution or continuity proof |
| CA-T19 | 6 | Identity/causal success does not generate native P3 authority; floor retained, actual P1 unity remains an open dependency |
| CA-T20 | 12 | Exact supplied source bytes and unique 109-record inventory; zero unsupported discharges |

Passing finite controls do not replace the missing import, full semantic audit, migration or authorized VO-discharge evidence. The positive witness is marked SIMULATED_REALIZATION; no actual NNNC, protected permission, identity or Level N claim follows. See FV-RESULTS.json and OPEN-OBLIGATIONS.json.

**END OF CURRENT LIMITED REVIEW CANDIDATE — NOT ADOPTED**

<!-- END EXACT P4 D2 v0.9.1 SOURCE -->

END: NOT ADOPTED; BOUNDED/CONDITIONAL CONSIDERATION ONLY; FULL N7 GATE UNMET.

<!-- END EXACT ADOPTED D2 CANDIDATE -->
