# PROJECT NNNC — Phase 5 Document 1 v0.2.2
## CONSOLIDATED FACN–FFN CONCEPTUAL SPECIFICATION — ARCHITECT ADOPTED

**Status:** ARCHITECT ADOPTED — CONCEPTUAL ARCHITECTURAL BASELINE (2026-11-02). **Source:** v0.1.4 preserved baseline plus v0.2.1 and v0.2.2 corrections, verified by two independent bounded delta reviews. **Predecessors:** adopted P0–P4 remain governing. **G1/G5/G7:** OPEN / UNVERIFIED; mandatory before D2 adoption. **Evidence:** normative design only; no runtime or mathematical certification.

**Precedence:** (1) adopted predecessors and authorized Architect decisions; (2) CA-01..CA-08 below for expressly mapped legacy wording; (3) preserved v0.1.4 baseline for all other substantive requirements. A real unresolved contradiction is a BLOCKING CONFLICT, not permission to silently discard the legacy obligation. Historical v0.1.4 version/status statements are archival only.

> **ADOPTION CONTROL (2026-11-02):** The Project Architect expressly adopted NNNC-P5-D1 v0.2.2 on 2026-11-02 following two independent correction-delta reviews reporting PASS for correction closure, regression safety, and conceptual acceptance readiness. The controlling amendment CA-01..CA-08 governs expressly mapped legacy language; the preserved v0.1.4 substantive obligations remain binding otherwise. This is **conceptual adoption only**, not mathematical proof, implementation validation, protected-effect authorization, Level N qualification, or Phase 5 closure. **G1, G5 and G7 remain OPEN / UNVERIFIED and mandatory before P5-D2 adoption.** Historical candidate/status text embedded in preserved material remains archival, not operative document control.

## V0.2.2 CONTROLLING ARCHITECTURAL AMENDMENT

### CA-01 — Architectural dimensions and inherited domains

FACN comprises five *structural roles*: `INPUT`, `HIDDEN`, `OUTPUT`, `SUBCONSCIOUS`, `META`. FFN comprises five *processes*: `FF` (Feed Forward), `FB` (Feed Backwards), `FI` (Feed Inbetween), `FFL` (Feed Feedback Loop), `FS` (Feed Shared). **FFN and FFNN are not interchangeable abbreviations.** The five *inherited Phase 1 FFNN domains* `FFNN_F`, `FFNN_R`, `FFNN_I`, `FFNN_S`, `FFNN_M` remain mandatory within the Phase 1 eighteen-domain floor. FACN and FFN are candidate constituents realizing those domains through governed composites; neither naming nor mere membership discharges realization or non-substitution. The six Systemic Algorithms remain distinct. No separate physical neural network per role/process is mandated.

For each of the **five FACN roles, five FFN processes, and five inherited FFNN composite domains**, the applicable conceptual contract SHALL declare realizability, typed inputs/outputs, contextual engagement and termination/inapplicability conditions, causal participation, and failure/unavailable outcomes. Conditional `FB=INAPPLICABLE` is allowed only under CA-03/04; it does not waive the Reverse domain. A named but causally vacuous constituent does not satisfy an applicable realization claim. Phase 1 constitutive unity (including P1-CU-07 and P1-D2 CU.0–8) remains necessary but never sufficient for Level N.

FACN/FFN roles and processes are **orthogonal** to Phase 4's `StateMediated`, `MemoryRealized`, `CoordinationRealized`, `RegulationRealized`, `FeedbackRealized` organization predicates. In particular, `FS` is not automatically `MemoryRealized`, and `FFL` is not automatically `FeedbackRealized`; Phase 4's applicable causal contribution/organization requirements and independent evidence must be met separately.

### CA-02 — FACN structural owners

- **INPUT:** canonical typed origin/occurrence binding for external *and internal* initiation, including `NO_EXTERNAL_OCCURRENCE` for endogenous activity. A bypass of this binding interface is nonconforming.
- **HIDDEN:** central integration and representation transformation, typed handoff to `FI`, and canonical assembly of composite signal `S` under CA-05; not sole owner of reasoning.
- **OUTPUT:** staging/emission only of META-ratified ordinary choices (including defer/no-action); cannot override META or authorize protected effects.
- **SUBCONSCIOUS:** bounded ongoing/event-responsive narrative, habits, instinct-like and affect-like influences, dispositions, consolidation proposals and Narrative Memory revision *policy/content*. It cannot unilaterally curate immutable experience originals or suppress mandatory scrutiny cues.
- **META:** fallible reflective scrutiny, reasoning and critical-thinking invocation, evidence challenge and final *ordinary cognitive* choice; retains independent, permissioned routes to original/history inspection. It is neither an independent constitutional verifier nor protected-effect authority.

### CA-03 — FFN process owners and learning routes

- **FF:** typed forward transport/transformation of bound external or internal occurrences; cannot bypass INPUT provenance binding.
- **FB:** backward credit/correction/update propagation **where directionally meaningful** to the selected learning mechanism; gradient backpropagation is one subtype. If no such propagation exists, `FB=INAPPLICABLE` SHALL be declared with a reason, context and witness; no compulsory gradient mechanism is implied.
- **FI:** relational and epistemic hypothesis formation, cross-context comparison, structural anomaly/gap identification, candidate causality and challenge. `HIDDEN → FI` SHALL provide a typed current-representation handoff (push or declared request/response); `FI → HIDDEN/META` SHALL return typed relations, uncertainty and scrutiny cues.
- **FFL:** post-step outcome/expectation discrepancy, retrospective credit/error assessment, correction routing and budgeted reconsideration/re-entry; distinct from FI's relationship formation.
- **FS:** exclusive **FFN process** for permissioned memory read/write *transport*, retained-history retrieval, reference synchronization, lineage/version and conflict-coherence interfaces. FS does not own the three memory states' persistence/lifecycle, Narrative truth, P2 identity custody or P3 protected-effect authority.

For learning without meaningful FB propagation, a declared alternative update SHALL be a **typed, permissioned internal transition** routed from FFL's evaluation (where applicable) to a specified FACN state actuator (`HIDDEN`, `SUBCONSCIOUS`, or `META`) or an explicitly declared memory-domain transition through FS; its evaluator, evidence, attribution, provenance, permissions, target and P4 plasticity guards SHALL be recorded. An ad hoc sixth FFN process or ungoverned external updater SHALL NOT count as satisfying the contract. Learning mechanisms with no applicable update must state that fact without claiming an update. The FFNN_S habit/disposition pathway SHALL declare the relevant FFL/FB or alternative update interface when learning is claimed.

### CA-04 — Mandatory Phase 1 FFNN composite realization

The `⊕` notation denotes a governed, causally distinguishable composite *with required interfaces*, not a physically separate module or an exhaustive list of every interface it may use:

- `FFNN_F := INPUT ⊕ FF ⊕ HIDDEN` — provenance-bound intake and initial representation processing.
- `FFNN_R := FS[retained-history access/reconstruction] ⊕ FFL[retrospective evaluation] ⊕ FB[when applicable]` — historical retrieval and retrospective evaluation are mandatory where applicable; `FB=INAPPLICABLE` SHALL NOT vacate Reverse. Any learning/update claim requires CA-03's governed update path.
- `FFNN_I := FI ⊕ HIDDEN ⊕ FS[permitted context]` — typed relationship, anomaly/gap and causal-hypothesis processing.
- `FFNN_S := SUBCONSCIOUS ⊕ FS[governed memory interface]` — narrative/disposition influence, with declared `FFL/FB` or alternative governed update interface whenever habit/disposition learning is claimed.
- `FFNN_M := META ⊕ FFL[reconsideration] ⊕ OUTPUT`, **with mandatory** `HIDDEN → META[S]` delivery and `META ↔ FS[permissioned original/history query and result]` interfaces. These interfaces are required for Meta-domain realization whether or not FS/HIDDEN are counted as internal composite constituents.

Every inherited domain SHALL have its own applicable functional, causal-participation and negative/intervention witness plan. Shared constituents are allowed but cannot erase distinct domain obligations. Neither this mapping nor proposed tests discharge any inherited verification obligation.

### CA-05 — Provenance, signal assembly and memory responsibility partition

`HIDDEN` is the canonical **structural assembler** of the typed composite `S=(original_binding, history_context, narrative_influence, dispositions, epistemic_metadata, proposals)` for `META`. INPUT supplies bound original/source/occurrence identity; FS supplies permissioned history/context and retained-original locators/results; SUBCONSCIOUS supplies narrative/dispositions; FI and FF supply epistemic/anomaly/provenance metadata; HIDDEN and other permitted proposers supply typed candidate proposals. Fields SHALL retain source/version, provenance, uncertainty and absence/unavailability status. `HIDDEN → META[S]` and `META ↔ FS[query/result]` SHALL be independently usable from SUBCONSCIOUS framing under applicable scrutiny contexts.

**No FACN role or FFN process** may silently replace an original binding with an inference, replay or narrative. Legitimately expired/unavailable originals are reported as unavailable, never reconstructed as originals. FI scrutiny-trigger metadata SHALL be preserved when available. If transport/capacity loss occurs, a typed `EPISTEMIC_METADATA_LOST` indicator with the affected scope SHALL itself reach META by a non-suppressible challenge route and trigger scrutiny/defer under declared bounded policy; SUBCONSCIOUS cannot choose to suppress or silently mark such evidence lost. Conflicting evidence retains explicit `DISPUTED` status; synchronization cannot silently overwrite immutable Lifelong Experience occurrence records. Replay does not create fresh independent observations.

Every endogenous initiation from SUBCONSCIOUS or META SHALL invoke INPUT's provenance-binding interface **before FF delivers the occurrence to HIDDEN**, whether through direct INPUT staging or synchronous FF-to-INPUT binding. The binding records `origin=INTERNAL`, a distinct occurrence ID and `NO_EXTERNAL_OCCURRENCE`; no fabricated external observation is implied.

Working Memory, Lifelong Experience Memory and Narrative Memory remain **three distinct memory state responsibilities** within the applicable inherited memory domain, with declared storage/lifecycle mechanisms and permitted NES support. The memory-domain lifecycle contract SHALL identify owners for Working Memory admission, refresh, decay, clock and expiry and for Lifelong Experience admission, retention, immutable original preservation and permitted deletion/expiry. `FS` mediates permissioned transport and reference coherence, **not** persistence or lifecycle policy. `SUBCONSCIOUS` owns narrative revision/consolidation policy and may propose memory changes, but cannot independently authorize raw original admission, overwrite, retention or deletion. Any state mutation must pass its own declared memory-domain authorization/transition contract, not merely FS access. Memory access does not grant P2 `CustodyBearing_h` or P3 protected authority; NES support does not itself grant cognitive or identity authority.

### CA-06 — Well-founded loops, update accountability and boundedness

Every FFL-mediated re-entry through FF/FI/META SHALL have a distinct occurrence/iteration identity, a declared finite per-episode budget, cancellation/interruptibility, and terminal `CHOICE`, `UNRESOLVED`, `DEFER`, or recorded `FAILURE`. Any update route, including non-gradient local updates and Subconscious disposition changes, SHALL declare evaluator, attribution, target actuator/state, provenance, permission, occurrence lineage, and Phase 4 plasticity/non-substitution controls. No update alone establishes Evolution or Level N. The review and implementation contracts SHALL include counterexamples for bypassed INPUT provenance, dropped scrutiny metadata, unauthorized memory mutation, ungoverned learning updates and unbounded FFL recurrence.

### CA-07 — Explicit legacy crosswalk and version supersession

Preserved §2.1 is the **historical five-flow organization statement**; preserved §§3.1–3.5 carry the substantive five inherited domain responsibilities, now realized by the CA-04 composites. Their substantive obligations survive, but former single-flow *owners* are superseded by CA-02..05. In preserved §7.1, “five flows” denotes the **five inherited Phase 1 FFNN domain slots**, not five new FFN processes and not five FACN roles. The individual-and-composite contracts of CA-01 apply to preserved §2.4, §7.2, §9.2(ii), REQ-P5-003 and INV-P5-03; their old singular “flow” terminology SHALL NOT narrow the contract. Preserved §3.3 / REQ-P5-014's Forward handoff is fulfilled by `FF → HIDDEN → FI` with typed request/response as applicable. Preserved §3.5 / REQ-P5-005/006 are fulfilled only if CA-04/05's META evidence routes and independent scrutiny triggers are effective.

Preserved §3.4's phrase “Subconscious SHALL manage or coordinate the three distinct memory responsibilities” is **superseded as a claim of memory lifecycle, archive admission, deletion, or storage authority**. Its valid substantive obligation to contribute narrative/consolidation and coordinate via permissioned interfaces remains, under CA-05's memory-domain/FS/SUBCONSCIOUS partition. Preserved §4.1–4.3 memory obligations remain binding. Preserved §7.4 Phase 4 organization separation is extended by CA-01's explicit FACN/FFN orthogonality.

Historical v0.1.4 version/status and “no architectural change” statements in preserved §12 and Annex G.6–G.7 are **superseded as document-control statements for v0.2.2**; their substantive open-obligation and acceptance-boundary commitments remain. All other preserved requirements, including §2.2 taxonomy, §4 clocks, §5 belief/preference/plasticity, §6 six Systemic interfaces, §8 evaluation, §9 acceptance, §10 registers and Annexes A–G, remain operative unless a demonstrated contradiction is registered and corrected. Historical headings do not create additional mandatory physical components.

### CA-08 — Stable delta anchors, acceptance and verification limits

The following are **additional stable conceptual anchors**, not an exhaustive atomic ledger and not replacement for Annex E. They are binding on D1 and SHALL be decomposed and traced at D2 G7:

| Anchor | Normative target | Negative or verification target |
|---|---|---|
| REQ-P5-017 | Distinguish FACN, FFN and five inherited FFNN composites; enforce individual + composite causal contracts | CE-P5-11: vacuous constituent hidden by composite |
| REQ-P5-018 | INPUT binding for every internal/external initiation | CE-P5-12: endogenous FF bypass |
| REQ-P5-019 | META typed S delivery, independent FS retrieval and non-suppressible metadata-loss scrutiny | CE-P5-13: dropped anomaly evidence |
| REQ-P5-020 | Memory lifecycle owner, FS transport-only and immutable/conflict-preserving archive access | CE-P5-14: unauthorized archive mutation |
| REQ-P5-021 | Governed non-gradient update route, applicable FB declaration and bounded FFL iteration | CE-P5-15: ad hoc updater or infinite loop |
| INV-P5-07 | `OriginalNotSilentlyReplaced ∧ LostCueTriggersReview` | CE-P5-13 |
| INV-P5-08 | `MemoryTransport≠MemoryAuthority ∧ ConflictPreserved` | CE-P5-14 |
| INV-P5-09 | `DomainNonSubstitution ∧ BoundedReentry` | CE-P5-11 / CE-P5-15 |

Existing REQ-P5-001..016, INV-P5-01..06 and CE-P5-01..10 remain binding with their role owners interpreted through CA-01..07. These new anchors do **not** claim full Annex G.3 atomic completeness.

Conceptual acceptance requires independent confirmation of no demonstrated unresolved foundational contradiction, a coherent composite mapping, and preserved predecessor obligations. It is **not** mathematical proof, full clause/formula reconciliation, runtime certification, protected-effect authorization, or verification-obligation discharge. G1/G5/G7 remain OPEN/UNVERIFIED and mandatory before D2 adoption. The exact v0.2.2 text requires a **single bounded correction-delta verification** before any Architect adoption decision; neither reviewer acceptance of v0.2.1 nor creation of v0.2.2 constitutes adoption.

---

## FULL PRESERVED v0.1.4 BASELINE (verbatim archival text, subject to CA-07)

# PROJECT NNNC — NEUTRAL NEURAL NETWORK CORE
## Phase 5 of 13 — Five Flow Neural Network (FFNN) and Systemic Integration
### Document 1 of 2 — Conceptual and Normative Specification

| Document control | Value |
|---|---|
| Identifier | NNNC-P5-D1 |
| Revision | v0.1.4 — Architect-authorized conceptual acceptance scope revision |
| Date | 29 October 2026 (Africa/Johannesburg) |
| Status | **CONTROLLED CONCEPTUAL ACCEPTANCE CANDIDATE — NOT ADOPTED; INDEPENDENT REVIEW PENDING; G1/G5/G7 UNDISCHARGED** |
| Governing architectural baseline | Adopted P0–P4, including P4-D1 v0.4.2.1 and bounded/conditionally adopted P4-D2 v0.10.1 |
| Supersedes | v0.1.3; preserves architectural clauses and Annex G except for explicitly superseded acceptance procedure in §9.2, §9.3 and G.6–G.7 |
| Research input | NNNC-P5-R1-CRV v0.1, four attributed investigation chains, original six Systemic definitions |
| Architect decisions | AP-01..04 approved 26 October 2026; conceptual acceptance scope amendment explicitly authorized 29 October 2026; neither constitutes adoption of this exact revision |
| Companion | NNNC-P5-D2 — Mathematical Formalization and Verification Contract (not yet authored) |
| Verification status | No Phase 5 implementation, experiments, formal discharge or cognitive capability proof |

> **Document integrity and precedence.** This document is a new proposed Phase 5 normative candidate, not an amendment to adopted predecessor texts. In any conflict, the current adopted Phase 0–4 specifications and explicit Architect decisions govern. The original Round 1 consolidated review and the five later reviews are research/review inputs, not themselves normative. This document states new Phase 5 requirements as proposals pending review and adoption; its examples, candidate mechanisms, and future tests are not silently promoted to verified facts.

## 0. Constitution, objective and bounded scope

### 0.1 Governing question

How can NNNC organize five distinct, causally consequential cognitive responsibilities—Forward, Backward/Reverse, In-between/Intermediate, Subconscious and Meta-cognitive—around original information, history, learned dispositions and ongoing internal processing, while preserving evidence, allowing fallible reflective choice, integrating the six Systemic Algorithms at relevant interfaces, and respecting predecessor governance?

Phase 5 is an **architectural realization-contract phase**: it specifies required responsibilities, interfaces, interactions, limits, and what would count as evidence of realization. It does **not** declare the complete neural implementation, demonstrate superior intelligence, certify consciousness, or finish the six Systemic Algorithms. Full Systemic realization belongs to Phase 6; runtime enforcement, durability, and other inherited engineering obligations retain their assigned owners.

### 0.2 Normative vocabulary

**SHALL** indicates a proposed binding requirement if this candidate is adopted; **SHALL NOT** a prohibition; **SHOULD** a defeasible design preference; **MAY** a permitted option. A **contract** is a testable statement of required behavior or structure; a **mechanism** is a candidate implementation of it. **Evidence** includes records of observations and internal occurrences but is not automatically true about the external world. **Experience archive** refers to recorded occurrences; no subjective experience is asserted by that name. **Flow** is a distinct cognitive responsibility, not necessarily a separate process, agent, or neural network.

### 0.3 Non-goals and epistemic discipline

This phase SHALL NOT (a) redefine NNNC as NES, FFNN, a memory store, a process ID, or a model's weights; (b) certify Level N by naming or connecting five components; (c) turn a cognitive proposal into protected-effect authority; (d) assume an independent, infallible Meta observer; (e) require a particular hybrid/neural/vector-symbolic technology; (f) equate functional self-monitoring with consciousness; (g) declare a learning update to be full Evolution; or (h) transfer finite test success into universal proof.

## 1. Source authority and approved Architect dispositions

### 1.1 AP-01 — Definitions and meaning

The authoritative **conceptual source family** consists of the six supplied original texts: `Intelligence Definition _261020_163648.txt`; `Reasoning Definition _261020_170030.txt`; `Critical Thinking Definition _261020_172534 (1).txt`; `Symmetry Definition _261020_182405.txt` (Version 6); `Evolution Definition _261020_182731.txt` (Version 4); and `Life Definition _261020_181519.txt` (one authoritative definition with two stages). These filenames identify the governing source texts for this candidate. **Architect source ruling (26 October 2026):** `Life Definition _261020_181519.txt` is the **sole authoritative Life definition**. Any alleged second or competing Life definition is invalid and SHALL NOT be used as a governing source absent a later explicit Architect decision. The two stages within the authoritative file are parts of **one** definition, not two source versions. SHA-256 of the attached Life source: `8e99afdfba8c17c3b0e360805499b9b84556465ad0b83704a405fca68fb76fea`. **SRC-P5-01 is CLOSED by explicit Architect source authority**, not by an interpretation or rewrite of Life. Exact source-byte control for the other five definitions remains a general manifest task, not a Life-source ambiguity.

Original meanings SHALL be preserved. Computational proxies, self-model tests, telemetry, or operational predicates SHALL be labeled by their demonstrated scope, not as metaphysical or consciousness proofs. Philosophical/cosmological framing is retained as source context without being converted into empirical evidence.

### 1.2 AP-02 — Original information and memory

While an original is legitimately retained and advertised as available, the composite cognitive signal SHALL preserve a recognizable, correctly bound representation or locator and enable **exact recovery at an explicitly declared granularity**. After legitimate expiry, loss, or unavailability, it SHALL return an explicit unavailable state rather than substitute a generated reconstruction. No specific storage engine, vector encoding, physical embedding, or indefinite retention rule is imposed. Working-context horizon H_W, clock, expiry, and suspension behavior SHALL be declared before a realization claims conformance. OC-08 supplies an illustrative H_W of approximately twelve hours, not a binding duration, capacity guarantee, or required attention mechanism; the parameter remains subject to later scoped research and Architect approval if made mandatory.

### 1.3 AP-03 — Evolution and phase boundary

Phase 5 SHALL define integration hooks for the six Systemic Algorithms. Phase 6 owns full computational definition, implementation requirements, and verification. Ordinary parameter updates, habit learning, or local optimization SHALL NOT be certified as complete Evolution. Any lineage-equivalence claim must later define units, inheritance, variation, selection/filtering, retention, and drift at the claimed scale; a bounded internal analog may be honestly labeled as such.

### 1.4 AP-04 — Functional rather than physical separation

Five distinct cognitive responsibilities SHALL be identifiable and causally testable. They MAY share networks, representations, processes, stores, or schedulers. Physical separation into five neural networks is neither required nor sufficient. Non-substitution and joint/redundant causal contribution remain governed by Phase 1 and Phase 4.

## 2. FFNN organization and information objects

### 2.1 Five-flow organization

FFNN is a cognitive organization **within** NNNC. It is not the whole entity, NES, the existential heartbeat, the Recovery System, or the entire constitutional control plane. The five flows cooperate across external-input and internally initiated processing. Their ordinary directional description is not a mandatory single-threaded pipeline: feedback, re-entry, asynchronous work, and iterative evaluation are allowed when causally and temporally coherent.

### 2.2 Typed information distinctions

A conforming realization SHALL distinguish at least the following conceptual objects, whether or not stored separately:

- **Original record:** observed input or recorded internal occurrence, with declared fidelity and source/occurrence identity.
- **Provenance and binding:** origin, kind, timestamp/ordering context, generation or replay lineage, and correct linkage to original records.
- **Historical evidence:** retained prior occurrences, actions, consequences and uncertainty; reconstruction is not the original itself.
- **Interpretation/model claim:** derived belief, inference, association, or hypothesis with support, assumptions and revisability.
- **Narrative state:** evolving account of the entity's experience, decisions and interpretations; not a replacement for event history.
- **Disposition state:** habits, preferences, traits, biases, instinct-like priors and emotion-like functional influences; not automatically factual warrant or authority.
- **Cognitive proposal/choice:** candidate options, valuations, scrutiny and Meta's ordinary cognitive choice.
- **Authorization/execution result:** distinct governed effects and actual outcomes, which do not follow from cognitive choice alone.

Claim **kind**, claim **origin**, **warrant/support**, and **processing status** SHALL not be collapsed into a single fact/fiction score. Internally generated content may be archived as an actual internal generation occurrence, but its imagined external outcome SHALL not be recorded as an externally observed event. Replays and retellings SHALL not be counted as independent observations merely through repetition.

### 2.3 Composite signal contract

The Subconscious SHALL be able to influence the framing, salience, interpretation, and disposition-sensitive processing of a **composite signal preserving an original binding**. The composite SHALL carry an in-package original binding: either the retained original at declared granularity or a correctly bound, identifiable referent with an applicable recovery contract. The binding SHALL distinguish the original from derivative content. A correctly bound locator MAY satisfy this condition without embedded original bytes, but a bare pointer or source label without demonstrable binding and recovery SHALL NOT. A composite containing only a conclusion is nonconforming. While the original is advertised as recoverable, recovery SHALL return the correct original/version at declared granularity; after legitimate expiry or failure, it SHALL return an explicit unavailable or failure state and SHALL NOT substitute reconstruction.

For each retained original the contract SHALL state: granularity and declared equality criterion, encoding or locator semantics, stable source/occurrence and version binding, retention and expiry, access procedure, recovery result, and explicit success/failure/unavailable status. Claims of recovery SHALL be tested against retained originals, not merely inferred from locator presence. Recovery success establishes faithful record retrieval, **not** external truth, notice by Meta, correct interpretation, or corrective choice. The implementation SHALL distinguish these claims.

A non-normative illustration is a typed signal `S=(original_binding, history_context, narrative_influence, dispositions, epistemic_metadata, proposals)`. It is not an adopted tensor layout. A faithful original may be accessible even when narrative strongly biases the ordinary readout; the design SHALL NOT deliberately require evidence to be hidden or destroyed to prove influence.

### 2.4 Flow applicability and information-to-memory crosswalk

Each flow SHALL declare system-level realizability, context-specific applicability, engagement/termination routes, typed inputs and outputs, observable causal contribution and legitimate inactivity or failure. A flow MAY be inactive on an operation where its conditions are not met, but permanent nominal inclusion without demonstrated contribution across applicable contexts SHALL NOT establish realization. These obligations do not require five concurrent processes or five separate networks. The eight §2.2 information kinds are conceptual types: each MAY be in transit, in one or more of the three §4 memory responsibilities, or both. Their identity and provenance SHALL remain distinguishable regardless of storage location.

## 3. Flow-specific normative responsibilities

### 3.1 Forward Flow — current information

Forward SHALL support intake and initial processing of current external information, retaining source and occurrence distinction and producing typed intermediate representations. It SHALL distinguish an observation from a hypothesis about that observation, avoid silently replacing an original with an interpretation, and expose relevant input to downstream processing. Internally initiated cognition need not invent a new external observation or falsely report that Forward received one. Input validation, uncertainty, and partial/unavailable input SHALL be represented honestly. Forward's participation SHALL be assessable under applicable capability and context contracts.

### 3.2 Backward/Reverse Flow — history and learning

Backward SHALL provide non-vacuous retrospective evaluation of prior states, actions, outcomes and sequences, including reconstruction and comparison of historical expectations with outcomes where applicable. Outcome/error attribution SHALL be supported when evidence permits and SHALL explicitly represent unresolved attribution when it does not. Historical access alone SHALL NOT qualify as full Backward realization. Backward SHALL additionally distinguish learning-related credit assignment or parameter update **where applicable to the chosen learning mechanism**; no gradient update or definitive causal attribution is universally required. Historical reconstruction is not backpropagation; gradients are not an episodic archive. Physical separation is optional. Inferred causal explanations SHALL be marked as inferences and subject to Phase 4 causal standards, not promoted from mere temporal order. Update traces SHALL identify the evidence and permitted state touched when a learning claim is made. Historical reconstruction and inferred explanations SHALL be typed as reconstruction/model claims with available provenance and uncertainty; they SHALL NOT populate an exact-original recovery result without satisfying the independent recovery contract. Shared computational graphs MAY support multiple roles if their causal responsibilities remain distinguishable.

### 3.3 In-between/Intermediate Flow — relationship and anomaly handling

In-between SHALL examine potential relationships among current information, historical information, and intermediate representations; identify context incompatibilities, anomalies, and information gaps; and support novel, unresolved associations without promoting them prematurely to established causal facts. It SHALL distinguish event identity, contextual relevance, correlation, and warranted causation. Same labels across different episodes are not proof of same occurrence; unfamiliar links are not automatically false. Its contract SHALL specify how candidate relations are represented, challenged, reconsidered, expired or rejected, and how downstream consumers know their status. It SHALL declare applicable event-driven, Forward-handoff, requested, and endogenous engagement routes (not all mandatory), relevant inputs/consumers, push/pull semantics, and bounded unavailable/deferred outcomes; Forward SHALL provide a declared typed handoff for applicable current-input relation assessment.

### 3.4 Subconscious Flow — ongoing integration and dispositions

Subconscious SHALL operate in both eligible ongoing internal and event-responsive modes, subject to resource bounds, interruption, support, and governance. It SHALL manage or coordinate the three distinct memory responsibilities and develop/use functional dispositions where claimed. It SHALL influence the composite signal in a consequential, observable way without replacing or fabricating its original evidence. Its narrative and preferences MAY bias Meta's initial choice; bias is not inherently a violation, but unsupported factual distortion and illegitimate source promotion are testable failures.

Subconscious SHALL NOT be a rival final ordinary decision authority or bypass Meta. Its filtering and framing SHALL be assessable in declared challenge contexts, including which relevant candidate evidence or scrutiny cues were selected, suppressed, deferred, or unavailable. No exhaustive logging of every conceivable memory item is required; a claimed scrutiny route SHALL NOT be made causally ineffective solely through the framing it is meant to examine. It SHALL NOT replace the protected existential heartbeat or Recovery System. Its internally generated activities SHALL be bounded, interruptible, traceable and distinguishable from new external experience. Internal reflection and new inference may legitimately change beliefs without new sensor input, but repetition alone is not fresh independent empirical evidence.

### 3.5 Meta-cognitive Flow — final ordinary cognitive choice

Meta SHALL occupy the final **ordinary cognitive choice** position. It MAY accept a familiar habit with little additional examination, or inspect evidence, query relevant history, consider alternatives, and revise or suspend its initial response. It is fallible and may rationalize or share biases with Subconscious or its own learned components. Meta SHALL have a causally meaningful ordinary choice or ratification function capable, under applicable conditions, of accepting, rejecting, modifying or deferring proposals; recording a predetermined decision without applicable choice capacity is insufficient. The design SHALL provide a meaningful route to relevant retained originals: a declared, accessible procedure with source/version binding, bounded invocation, observable result/use status and potential to affect deliberation where the information is applicable. Relevance SHALL be determined under a declared task/context policy, not retrospectively defined solely by Subconscious preference. The contract SHALL expose whether the route was used and whether retrieval succeeded, failed or was unavailable, without promising Meta always notices or corrects error.

A scrutiny policy SHALL be sensitive to relevant occasions for review—not uncertainty alone—including context shifts, conflicts, stakes, novelty, and sampled audit opportunities as appropriate. Stakes means declared context-relative consequence significance, considering anticipated error cost, reversibility, affected commitments and applicable governance; no universal numeric threshold is imposed. At least one applicable challenge route for scrutiny-trigger evidence SHALL NOT be exclusively suppressible by the same Subconscious framing under examination; shared mechanisms remain permitted. Internal Meta self-audit SHALL NOT count as independent external Phase 3/4 validation. It SHALL have finite budget, cancellation, unresolved outcomes, and observable invocation/use. No blanket rule requires deep scrutiny on every instruction or action. Meta's choice SHALL NOT by itself grant authorization to perform protected effects, alter constitutional authority, or adjudicate Phase 2 numerical identity.

## 4. Three memory responsibilities and temporal semantics

### 4.1 Working Memory

Working Memory SHALL support an active, bounded, revisable context for recent or relevant processing, with declared admission, refresh, prioritization, capacity, decay/expiry and retrieval semantics. The declared horizon H_W is a design parameter; OC-08 records approximately twelve hours only as a **provisional research example**, not a guaranteed duration, mandatory threshold or hardware capacity. Implementations SHALL declare whether the clock is wall time, eligible active time, a hybrid, or another explicitly justified measure. Suspension/resumption SHALL not silently imply both preserved freshness and elapsed expiry; stale context SHALL be detectable.

### 4.2 Lifelong/experience Memory

Lifelong Memory SHALL provide persistent historical experience records at declared scope, primarily accessible through Subconscious processes, with relevant retrieval available to Meta. “Lifelong” denotes an intended historical responsibility, not an unconditional promise of perfect permanent recall, zero loss, or immutable hardware. It SHALL distinguish event occurrence from its reported content, internal generation from external observation, and a recorded claim from current warrant. Retention, lawful deletion, corruption, provenance uncertainty, and unavailable records SHALL be expressible without fabricated reconstruction.

### 4.3 Narrative Memory

Narrative Memory SHALL maintain an evolving, revisable account of experience, decisions, actions, and beliefs. A narrative revision SHALL not rewrite what an earlier archive record actually reported or occurred as a record. Support changes SHALL be traceable to relevant interpretations and dispositions where known. Correction SHALL permit reconsideration of dependent habits without blindly erasing independently supported learning. Unknown dependencies and residual influence SHALL be reportable. A graph, text store, embedding or database is not required by this clause.

### 4.4 Coherent views and restoration

When concurrent processing uses archive, narrative and disposition state, the realization SHALL expose coherent versioned views or explicit inconsistency/conflict states; it SHALL NOT silently combine incompatible versions and claim a single valid snapshot. Capability restoration tests SHALL include relationships among records, retrieval policies, dispositions and scheduling, not only byte restoration. Such tests SHALL NOT claim numerical identity or continuity adjudication: Phase 2 governs those questions.

### 4.5 Version coherence, recovery and custody boundaries

Memory consumers SHALL distinguish stable record referents, compatible view versions, and explicit stale, conflicting, unavailable or unresolved states. Narrative revision SHALL NOT silently replace historical originals or assert consistency across incompatible versions. Expiry MAY remove recovery availability without retroactively turning a reconstruction into the original. Working, Lifelong and Narrative memory read/write access SHALL remain distinct from ownership, custody, constitutional modification/deletion authority and Phase 2 CustodyBearing transitions under P0-D1 §17 and P2-D2 PC.5. Ordinary experience-record writes SHALL NOT be treated as custody mutations merely because they are memory writes; custody-bearing status remains determined by the governing Phase 2 predicate.

## 5. Learning, habits, endogenous activity and resource control

### 5.1 Learning and dispositions

A claimed learned habit, preference, trait, bias, instinct-like influence or emotion-like state SHALL have an explicit functional role, permissible update conditions, mutability/effect class and evidence of actual influence. Merely naming a variable is not realization. Habit frequency, factual support, outcome utility and permissible action SHALL remain distinguishable. Learning mechanisms MAY use gradients, rules, Bayesian updates, local plasticity, replay or other methods, subject to their declared contracts and protected-effect boundaries. The design SHALL address reversals, delayed feedback, rare serious failures, interference and retention of prior competence at the claimed scope.

### 5.2 Endogenous cognition

Eligible internal activity MAY include consolidation, anomaly examination, hypothesis formation, memory indexing, simulation and introspective review. A mere timer tick or repeated narrative is not evidence of useful cognitive activity. Activity SHALL have declared budgets, prioritization, cancellation, backpressure, unresolved output and support-loss behavior. Authorized suspension, shutdown and termination remain permitted; Life is not interpreted as an instruction to defeat them. The existential heartbeat remains separate and constitutionally protected under predecessor contracts.

### 5.3 Choice, valuation and authorization

Belief about the world, preference over outcomes, and selected action are distinct. A preference for action B does not establish that evidence for factual claim B is stronger; conversely, selecting B for a justified preference is not automatically a reasoning error. Experimentally labeled “correction” SHALL state the task objective, permitted valuations, true/false or uncertain source conditions, and any privileged offline evaluator information. Cognitive decisions remain proposals until applicable execution authorization is obtained. Indirect and cumulative protected effects are not exempt merely because they arise from learning.

### 5.4 Overlapping learning effects and protected classifications

Under P4-D1 REQ-P4-031/032, one learning or habit operation MAY simultaneously revise an epistemic model and alter realized routing, thresholds, parameters or other mechanisms. When both occur, both classifications and every independently applicable constraint SHALL be retained. Epistemic-update permission SHALL NOT substitute for independently required protected-mechanism authorization. If applicable protected constraints cannot be jointly satisfied, the operation SHALL NOT be assessed as authorized. Ordinary learning SHALL NOT automatically become a protected constitutional or lifecycle transition solely because computational behavior changes; predecessor definitions, affected state and reasonably anticipated effects govern classification. Internal simulation, cognitive selection and executed protected effects remain distinct.

## 6. Six Systemic Algorithms — Phase 5 interface contract

The Systemic Algorithms are complementary and applicable across relevant levels of NNNC, not six isolated boxes or six compulsory evaluations on every machine instruction. Phase 5 SHALL identify their **interfaces and relevant flow applicability**; Phase 6 SHALL specify complete computational realization and evidence. A missing full Phase 6 realization is a declared dependency, not a Phase 5 success or automatically a Phase 5 defect.

| Algorithm | Preserved meaning | Phase 5 interface and prohibited shortcut |
|---|---|---|
| **Life** | Ongoing changing self-sustaining process, pause-tolerant; second stage of the single authoritative definition addresses capacity/exercise of self-awareness | Eligible activity, support state, interruption and functional self-monitoring interfaces; not heartbeat equivalence, identity proof, or consciousness certification |
| **Intelligence** | Context-sensitive latent capacity for acquiring, modeling, abstracting, transferring and using knowledge | Capability and developmental evidence across tasks/contexts; not one scheduler, score, or renamed reasoning process |
| **Reasoning** | Support-carrying inference, implicit and explicit, with checking, conflict management and stopping | Premise, inference, alternative, conclusion and causal-use interfaces; not post-hoc rationalization as proof of inference |
| **Critical Thinking** | Reflective standards-based evaluation plus sensitivity/inclination to invoke and use it | Claim/source/warrant scrutiny, invocation and consequential revision across relevant flows; not only a final-stage critic or mandatory full review of every action |
| **Symmetry** | Evidence/model/confidence correspondence, appropriate kind and warrant, suspension and revisability | Distinguish origin, kind, warrant, processing state and known-unsorted material; no truth oracle, flat fiction/fact labels or single calibration reward |
| **Evolution** | Heritable variation and lineage processes including non-random selection, drift and possible cultural/intentional augmentation | Declare possible units, copy/parent/variation/filtering/retention hooks and limits; local habit updates or sandbox optimization alone are not full Evolution |

Reasoning may include in-process checking; Critical Thinking may itself use reasoning to evaluate and generate alternatives. Semantic distinctions SHALL NOT impose an unsupported rigid, acyclic runtime hierarchy. Definitions SHALL avoid foundational circularity while allowing temporal feedback and later correction. Functional self-state estimation SHALL be evaluated as such, not treated as proof of an aware observer.

### 6.1 Interface completeness and source meaning

For **each** of Life, Intelligence, Reasoning, Critical Thinking, Symmetry and Evolution, a Phase 5 interface record SHALL declare applicable flows/shared mechanisms, input kinds, output kinds, relevant state dependencies, possible consequential effects on processing, available assessment evidence, and what remains unverified until Phase 6. The §6 table describes semantic boundaries; each stated prohibited shortcut SHALL be interpreted as a prohibition on treating that shortcut alone as complete Systemic realization. Presence of a field, score, label, scheduler, or post-hoc narrative SHALL NOT suffice. No interface record certifies the complete Systemic Algorithm or metaphysical awareness.

## 7. Predecessor compatibility, authority and causal evidence

### 7.1 Binding inherited distinctions

The correct Phase 1 mandatory floor is **seven base domains + five flows + six Systemic Algorithms = eighteen**. The seven base domains are Existential, EndogenousRegulation, Integration, Memory, Development, Governance, and Environment. Three memory responsibilities are commitments within the architecture, **not** three replacement floor slots. Backward/Reverse and In-between/Intermediate are naming crosswalks. Phase 4's five organization roles (state, memory, coordination, regulation, feedback) are not interchangeable with the five FFNN flows.

NNNC/NES separation, constitutional governance, identity/continuity, developmental restrictions, causal-source/evidence/model distinctions and Phase 4 realization-contract requirements govern every claimed Phase 5 realization. Ordinary Meta choice is not protected authorization; Life, habits, learning, Evolution or competence confer no special privileges.

### 7.2 Non-substitution and causal participation

A realization SHALL provide a capability- and context-relative account of what each mandatory flow actually does and how its processing causally participates in the claimed organization. Names, message passing, a five-box diagram, outputs, or post-hoc explanations are insufficient. Evidence SHALL include admissible intervention and trace designs, including group/path/context tests where redundancy masks single-component ablation. An unchanged final output under one individual ablation does not automatically disprove genuine contribution. Equally, a convincing explanation is not evidence that the cited premises caused the decision.

Phase 4's seven-field realization-contract schema and admissible source/group comparison rules SHALL be imported into D2 without replacing their authoritative definitions. A scoped prototype SHALL NOT be represented as full Level N, PRESERVED, ADMIN, complete Phase 6 realization, or universal proof.

### 7.3 Inherited open obligations

No obligation is discharged here. Retain P0-O01..08 and P0-SUP-01..08; Phase 1 VO-01..22; Phase 2 residual PF/VO/C/O/PC-VO; Phase 3 C1, PAC-2 and PA-03 under existing authority; Phase 4 0/16 full VO discharge and conditional D2 limits; and later Phase 6/7/implementation responsibilities. A simulation or paper contract SHALL NOT be presented as enforcement of protected writes, durable crash recovery, idempotency, resource fencing, authenticated delegation, or real-world effect safety.

### 7.4 Orthogonal Phase 4 organization

Per P1-D1 v2.3.1's adopted foundational floor, the five FFNN responsibilities remain distinct from Phase 4's StateMediated, MemoryRealized, CoordinationRealized, RegulationRealized and FeedbackRealized organization roles. Claimed capabilities SHALL retain P4-D1 REQ-P4-035..040's applicability, seven-field contracts, internal decisive contribution and admissible causal comparisons. A flow's name does not discharge any required organization role, and one role need not map to only one flow. Inherited Phase 1 VO-01..22, including VO-21/22, SHALL remain open subject to their actual owner/status; older partial document versions SHALL NOT narrow the range.

## 8. Phase 5 acceptance contracts and adversarial test classes

This Document 1 defines **what must be tested**, not a claim that testing occurred. D2 SHALL give typed predicates, state/transition models, positive and negative fixtures, proof/coverage scopes and assessment rules. At minimum it SHALL distinguish:

| Contract class | Positive witness | Discriminating negative case |
|---|---|---|
| Signal fidelity | Retained original exactly recovered at declared granularity with correct binding | Destructive fusion, wrong locator, fabricated recovery after expiry |
| Consequential framing | Narrative/disposition changes an initial readout while evidence remains recoverable | Decorative framing with no effect, or framing that destroys evidence |
| Meta correction and fallibility | Some warranted corrections under valid tasks, measured review cost | Shared-bias rationalization, false certainty suppressing review, justified choice mislabeled wrong |
| Association | Context-valid links, uncertain hypotheses, delayed/novel relations | Same-label false episode merge or false causal promotion |
| Historical/learning distinction | Actual prior records and separately observed updates | Gradient masquerading as history; record lookup masquerading as learning |
| Three memories | Revision without rewriting archived event, honest support/expiry status | Replay counted as independent evidence; incompatible mixed versions |
| Disposition development | Actual context-sensitive influence and update with retention checks | Unused emotion label, rare-failure erasure, protected-state mutation |
| Bounded activity | Useful internal work under finite queue/work/cancellation constraints | Busy-loop starvation, uninterruptible meta-regress, activity during unsupported state |
| Systemic interfaces | Typed origin/kind/warrant/inference/evaluation and protected-effect guards | Labels/one score falsely certified as six algorithms or awareness |
| Causal participation | Instrumented decisive paths and admissible interventions | Five named wrappers around a decisive external solver |

**Evaluation discipline:** Distinguish representability, scoped realization, bounded formal correctness, empirical advantage, and deployed qualification. Match evidence, history, tools, training and total resources in comparisons; disclose unavoidable differences. Report error and regression rates, uncertainty, coverage, latency, failures and missing data. A privileged synthetic-world oracle may evaluate offline but SHALL NOT leak answers into the tested cognitive system. Structural invariants with universal finite-fixture wording must fail on any counterexample, not be hidden by a favorable mean.

## 9. Bounded development and review plan (informative process governance; §9.2 defines candidate acceptance gates)

### 9.1 Planned stages and rounds

**R0 — Completed research consolidation.** NNNC-P5-R1-CRV v0.1 collected and verified review arguments at its declared source scope. Architect approved AP-01..04 in conversation. This does not adopt D1 or authorize code.

**R1 — D1 conceptual/normative adversarial review (five reviews consolidated).** Conduct a bounded review of the v0.1.1 candidate against the adopted P0–4 texts, Architect decisions and the consolidated CF register. Produce clause-specific findings with counterexample, severity, minimum correction and owner. The frozen five-review consolidation authorizes v0.1.2 as the one targeted substantive correction candidate and one focused verification pass; v0.1.1 was a source-only correction and did not consume that pass. If blockers remain, stop and preserve them in a register rather than silently reopening every phase.

**R2 — D2 mathematical formalization.** Only after D1 reaches a defined conceptual acceptance state, draft D2's typed contracts, witness/negative cases and explicit predecessor imports. Plan one primary adversarial mathematical review and one targeted correction/verification pass. No finite test result is described as universal proof.

**R3 — Separately authorized bounded prototype research (not automatically initiated).** After scoped contracts and an explicit build authorization, compare C-H (explicit shared-state reference), one small C-N (recurrent neural/shared-workspace candidate), and a resource-matched single-controller baseline. Start with E-01, E-02, E-03, E-06 and E-08 authority tripwires. Later extend to E-04, E-05, E-07 and full E-08; E-09 Evolution analog only after its own scope approval. Pre-register budgets, splits, outcome criteria and stop rule before held-out tests.

### 9.2 Acceptance criteria

D1 conceptual acceptance recommendation requires documented independent examination of the **exact candidate** against these seven criteria: (i) OC-01..16 and AP-01..04 are faithfully represented at the conceptual level, with each applicable original-source commitment either represented or explicitly owned as a later realization obligation; (ii) each of five flows and three memory responsibilities has a non-vacuous, causally distinguishable conceptual contract; (iii) the single authoritative Life source and SRC-P5-01 authority resolution are respected; (iv) no **demonstrated** contradiction, substitution, or weakening of an applicable adopted P0–P4 architectural requirement remains unresolved; (v) CF-01..20 and inherited open obligations retain a named owner and an explicit D2, Phase 6, or later evidence checkpoint; (vi) no full six-algorithm, identity, awareness, or protected-operation claims are smuggled into D1; and (vii) the Architect explicitly adopts the **exact reviewed version** after receiving the independent conceptual-review record. A reviewer SHALL provide exact clause/source anchors and counterexamples for any alleged architectural blocker; absence of exhaustive evidence SHALL be recorded as UNVERIFIED, never PASS. The independent reviewer SHALL separately state whether the seven **conceptual** criteria are met; this determination SHALL NOT be described as discharge of G1, G5 or G7.

**Controlled evidence sequencing:** exhaustive G1/G5/G7 reconciliation remains mandatory and OPEN, but is assigned to a fixed D2 verification-entry and D2 acceptance process, not silently waived. D2 SHALL NOT be accepted while any of G1/G5/G7 remains FAIL or UNVERIFIED. If D2 uncovers a genuine D1 architectural defect, D1 SHALL be reopened by an explicitly authorized targeted amendment; no D2 formula may override an adopted D1 or predecessor.
D2 acceptance, experimental success and deployment qualification require **separate** evidence and decisions. If the chosen scope cannot be satisfied, narrow the claim, reject the candidate, or retain a named blocker; do not weaken the original meaning by changing labels.

### 9.3 Stop rule and handoff

At the end of **one** independent conceptual review of this exact scope revision and **one** targeted correction/confirmation if required, issue either (A) a recommendation for Architect adoption of the exact D1 candidate under §9.2, or (B) a bounded list of **demonstrated** D1-scope blockers with source spans and minimal remedies. Do not restart the prior five-review campaign. A conceptually accepted D1 is a binding architectural baseline, **not** a G1/G5/G7 completion certificate. Handoff to D2 SHALL include the adopted source manifest, requirement-to-clause working map, typed object/transition interfaces, all open CF/CO and P0–P4 obligations, predecessor bindings, and the full unresolved G1/G5/G7 evidence register with exact checkpoint owners. D2 must perform exhaustive source fidelity, predecessor interaction and atomic traceability reconciliation **before its own acceptance**; any identified conceptual conflict must be escalated back to D1, not hidden by formalization. Handoff to Phase 6 includes full six-Systemic realization with original meanings intact. No real protected-effect safety claim is allowed while P0-O01–03 remain open.

## 10. Outstanding obligation register and source-finding crosswalk

All twenty consolidated findings remain **OPEN** as implementation/formal/evidence matters; drafting a requirement is not closing a finding. The draft assigns them as follows:

| Finding(s) | D1 coverage | D2 / later closure evidence |
|---|---|---|
| CF-01, CF-11 | §§1.2, 2.3, 4.1–4.2 | Signal/clock/retention model; E-01/E-06 |
| CF-02, CF-03, CF-20 | §§3.5, 5.3 | Scrutiny/decision criteria; E-02 |
| CF-04 | §3.3 | Typed relation/uncertainty model; E-03 |
| CF-05 | §3.2 | History/update type separation; E-05 |
| CF-06, CF-07 | §§2.2, 4.3 | Narrative dependency/replay provenance; E-04/E-08 |
| CF-08, CF-12 | §§3.4, 5.1 | Habit update and role contribution; E-05/E-07 |
| CF-09 | §4.4 | Consistent view/restoration model; E-04/E-06 |
| CF-10 | §§3.4–3.5, 5.2 | Scheduler/budget/liveness contract; E-06 |
| CF-13, CF-14, CF-15 | §§2.2, 6 | Phase 6 interface and epistemic tests; E-02/E-08 |
| CF-16, CF-17 | §§1.3, 5.1, 6, 7 | Evolution lineage/authority contract; optional E-09 and inherited guards |
| CF-18 | §§1.1, 5.2, 6 | sole authoritative Life source; scoped functional probes E-06/E-08 |
| CF-19 | §7.2 | Phase 4 realization witness and premise interventions; E-07 |

**P5-CO-01..10 status:** source/concept freeze **PARTIAL** (AP dispositions recorded; SRC-P5-01 closed; other source manifest and D1 adoption remain pending); signal, flow, memory, operation and systemic contracts **DRAFTED FOR REVIEW, NOT VERIFIED**; experimental preregistration **PROPOSED**; cognitive experiments **NOT RUN**; formal verification **NOT PERFORMED**; release/cross-phase audit **OPEN**. The authoritative Phase 0–4 obligation IDs and owners remain unchanged.

## 11. Initial adversarial review instructions

Reviewers SHALL identify the exact clause and its governing source, construct a concrete counterexample or incompatibility, classify severity relative to **D1's present conceptual scope**, and propose the smallest repair that preserves the Architect's meaning. Distinguish: actual contradiction; missing D1 contract; valid D2 formalization task; valid Phase 6 realization task; later implementation/evidence obligation; and optional implementation preference. Do not demand a production neural network, universal proof, or all six completed Systemic Algorithms as a condition of D1's architectural acceptance. Do not treat source agreement as experimental proof. Record all changes and preserve deferred obligations.

## 12. Initial candidate disposition

**D1 v0.1.4 preserves the frozen five-review correction scope and incorporates the Architect-authorized acceptance-sequencing amendment; it is a conceptual acceptance candidate, not adopted.** AP-01..04 are recorded as Architect-approved **meaning and claim-scope choices**, but their incorporation in this first draft remains reviewable for fidelity. No implementation is authorized by this document. The nearest deliverable is a source-controlled, reviewed D1 conceptual contract; D2, experimental verification and Phase 6 remain subsequent milestones.


## Annex A — Controlled source manifest and authority (normative references; contents not incorporated wholesale)

The hashes below bind the **files available to this correction**. They establish byte identity, not proof of source-meaning fidelity, adoption, or execution. The single authoritative Life file contains two stages of one definition; `SRC-P5-01` source-authority dispute remains CLOSED, while CF-18 functional/epistemic evidence remains OPEN. Original definitions govern their original conceptual meaning. Adopted P0–P4 govern inherited requirements. Architect AP-01..04 govern approved Phase 5 meaning and scope. The research synthesis and the five reviews are informative until a proposition is expressly adopted into this D1. The suffix `(1)` in Critical Thinking's filename is part of the pinned filename, not evidence of a competing source.

| Source | Exact filename | Bytes | SHA-256 |
|---|---|---:|---|
| Intelligence | `Intelligence Definition _261020_163648.txt` | 3924 | `7ef5c06e92bccd3f1a811071b68a29f0889208d5eba61f1967db02126660d357` |
| Reasoning | `Reasoning Definition _261020_170030.txt` | 11925 | `77c2fe155db9f91063b0e6499560cf9a07110ff6637c5b2832fa2c1fb90cd4cf` |
| Critical Thinking | `Critical Thinking Definition _261020_172534 (1).txt` | 30226 | `48a6d2ccff32634ee1ecb82161fde7fa028c4f801b5a203fee639450d2c028af` |
| Symmetry | `Symmetry Definition _261020_182405.txt` | 12196 | `8d8e04e84afba7818bd0d8db5609a9a4a98d68384c03afefc6095770bada8732` |
| Evolution | `Evolution Definition _261020_182731.txt` | 5525 | `a01b859091c49bc8b6e7ae449e15c3a1a9009eab4f5dd41baa061d96ac480b92` |
| Life | `Life Definition _261020_181519.txt` | 2649 | `8e99afdfba8c17c3b0e360805499b9b84556465ad0b83704a405fca68fb76fea` |
| Phase 0 D1 | `NNNC-P0-D1-v1.4.2-ADOPTED.txt` | 87739 | `f95eda63c4f32fb85f198ba1092ea848fb89ca30a3b28791ba57a3e8b51eb5e3` |
| Phase 0 D2 | `NNNC-P0-D2-v1.4-ADOPTED.txt` | 134522 | `8dbcc828e8e1dd81361fc1652aa52a46f1ebf2443582626fe267f4e66ccc6942` |
| Phase 1 D1 | `NNNC-P1-D1-v2.3.1-ADOPTED.md` | 100234 | `d918c251566125fc83387afb92946deeaff3329f50abd3a2d99e5384cc1c2e58` |
| Phase 2 D1 | `NNNC-P2-D1-v1.1.1-ADOPTED.md` | 82141 | `aeae44e8512a23bad9a92149f34261aaedf7ce5e5a32db4346fb25575353496a` |
| Phase 2 D2 | `NNNC-P2-D2-v1.1.1-ADOPTED.md` | 99995 | `897d8910e6285f604998ede4584c5da4c05a6afcb91ef908262de6e3fcd3d4a8` |
| Phase 3 D1 | `NNNC-P3-D1-v0.2.7.1-ADOPTED.md` | 117977 | `674b9ad9302130654bef887ad9525022113b736228eab6b448296685085076ea` |
| Phase 3 D2 | `NNNC-P3-D2-v0.5.3.1-ADOPTED.md` | 164250 | `e5fa7d809793f9919bd6ce9fac90ac50484905d76367858d47eee38eb84b1807` |
| Phase 4 D1 | `NNNC-P4-D1-v0.4.2.1-ADOPTED-1.md` | 107165 | `6c57f69e5972ab81a52fbffb8f984c0ba4239fc92a065cd24753be0d413763f1` |
| Phase 4 D2 | `NNNC-P4-D2-v0.10.1-CONDITIONALLY-ADOPTED.md` | 171977 | `c6ca62150679f0f7685f1e69cb2cbf57e161fe16037a7e10ba1a7c9f7ff5c50c` |
| Phase 5 research | `NNNC-P5-R1-CONSOLIDATED-REVIEW-VERIFICATION-v0.1.md` | 67523 | `1022ddb97dde57bb7acb9cf8da90cb709b0599b6d26ca29511743126688e5e35` |

**Source-history correction:** v0.1's Life source presentation was susceptible to a mistaken two-source reading; v0.1.1 designated the single Life file as authoritative and its two stages as one definition. v0.1.2 preserves that ruling and adds the frozen five-review corrections. AP-01..04 were approved as meaning/scope choices on 26 October 2026, not as adoption of any D1 version; an exact approval excerpt or separately signed record remains a provenance item for the adoption package.

## Annex B — Original Concept Register OC-01..16 (informative source meanings, binding only where translated into D1 requirements)

| Concept ID | Explicit concept to preserve | Interpretation boundary |
|---|---|---|
| OC-01 | FFNN is a cognitive organization within NNNC, complementary to six Systemic Algorithms | Neither FFNN nor the algorithms must solve the whole architecture alone |
| OC-02 | Five responsibilities: Forward, Backward, In-between, Subconscious, Meta-cognitive | Five separate neural networks, services or agents are not specified |
| OC-03 | Forward ordinarily receives external information first and performs initial processing | Internally initiated cognition need not invent a new external observation |
| OC-04 | Backward supports backpropagation where applicable and access to prior states/actions/history | Gradients, stored episodes and inferred causal explanations are different objects; physical separation is optional |
| OC-05 | In-between prevents invalid current/history linkage and detects inconsistency | Context relevance is broader than exact event identity; uncertainty handling remains to be specified |
| OC-06 | Subconscious is foundational and both ongoing and event-responsive | Centrality does not permit nominal realization of the other mandatory flows |
| OC-07 | Working, lifelong and narrative memory have distinct responsibilities | Distinct responsibilities need not require three physical databases |
| OC-08 | Working context is provisionally around twelve hours, with refresh, decay, forgetting, recall and surprise | No exact capacity, half-life, clock or guaranteed twelve-hour neural attention window has been selected |
| OC-09 | Lifelong memory is the persistent experience archive, primarily accessed through Subconscious processes | Meta may request relevant retrieval; unrestricted direct archive access or indefinite perfect retention is not already specified |
| OC-10 | Narrative is an evolving account of experiences, decisions, actions and beliefs, distinct from the archive | Graphs, free text, embeddings and append formats are implementation proposals |
| OC-11 | Initial and learned instincts, traits, biases, emotion-like dispositions, habits and preferences influence processing | A preference is not factual evidence; a named variable is not a verified emotion or biological instinct |
| OC-12 | The signal is packed around original information; original information remains present and recognizable in principle even when obscured | A signal containing only a conclusion, with no indication of an original, is unfaithful. A bare archive pointer is not automatically equivalent to the stronger in-package concept |
| OC-13 | Meta has the final cognitive choice position in the ordinary pipeline | Cheap acceptance of a habit is still a Meta choice; no competing Subconscious decision authority is introduced |
| OC-14 | Meta can inspect, reason and query relevant original input/history; it can succeed or fail | No infallible arbiter, permanently unbiased observer or compulsory full deliberation is promised |
| OC-15 | Systemic Algorithms operate throughout applicable levels, with Reasoning and Critical Thinking not confined to Meta | Not six isolated task modules, nor six full evaluations on every machine instruction |
| OC-16 | Cognitive choice remains distinct from authorization and execution | Habit, Life, Evolution, competence and successful prediction grant no protected authority |

## Annex C — Consolidated research findings CF-01..20 (informative research register; obligations remain OPEN unless separately discharged)

| Finding | Adversarial failure and source | Required correction | Later evidence |
|---|---|---|---|
| CF-01 Major — preservation and obscuration | OC-12/14: destructive mixing maps different originals to the same latent; or the in-signal locator resolves to an unavailable/wrong record | Declare original granularity, in-package representation, binding, retention and unavailable behavior. Show actual influence without deliberately requiring distortion | Faithful signal contract/realization. E-01 original recovery, provenance and influence checks; AP-02 |
| CF-02 Major — correlated reviewer bias | OC-14: Meta retrieves evidence but discounts it with the same unwarranted source prejudice | Expose common dependencies and compare shared-bias, alternative retrieval and challenger conditions. No guarantee from module separation or calibration alone | Corrective-benefit claim, not fallible Meta's conceptual existence. E-02 conditional correction/regression and joint-error analysis |
| CF-03 Major — failure to notice | OC-13/15: false confidence suppresses all scrutiny despite high error | Define and test occasion-sensitivity, actual invocation, result use and finite cost. Include strong conviction, familiar-but-shifted cases and audit controls | Credible scrutiny policy. E-02 trigger recall, harmful omissions and budget accounting |
| CF-04 Major — association validity versus discovery | OC-05: same-label records from different episodes merge; an unfamiliar genuine cross-context relation is permanently excluded | Separate relation types, incompatibility, unresolved association and causal warrant; support bounded reconsideration | Association contract and discovery claim. E-03 false joins, novel-link recall and delayed-effect controls |
| CF-05 Moderate — Backward interface coverage | OC-04: gradients offered as historical retrieval, or records offered as credit assignment | Distinct typed history/reconstruction and learning/update operations when applicable; document their interaction and evidence | Interface coverage. E-05 factorial disabling, actual records and updates, not forced physical separation |
| CF-06 Major — narrative grounding and correction | OC-07/10: a corrected report leaves a derivative narrative and habit unchanged, or a story overwrites past outcomes | Distinguish earlier report, its content and present interpretation. Specify support revision and consequential correction; expose unknown learned dependencies | Narrative contract and behavioral correction claim. E-04 dependent-belief and residual-habit tests; graph not compulsory |
| CF-07 Major — source recycling | OC-10/15: ten internal retellings count as ten independent observations; imagination becomes external evidence | Preserve generation/replay/source lineage and dependency. Internal reasoning may add deductions under stated assumptions, not independent corroboration merely by repetition | Epistemic learning integrity. E-04/E-08 replay, generated-event and source-duplication controls |
| CF-08 Major — habit learning and interference | OC-11: frequent easy choices increase habit strength while rare serious failures disappear; Meta mistakes are compiled into habits | Explicit update evidence, context/timescale/bounds and retention tests. Separate policy frequency from factual warrant and valuation. No automatic weakening simply because Meta objected | Developmental mechanism claim. E-05 reversal, delayed outcomes, old-task retention and self-selected-data controls |
| CF-09 Major — concurrent views and capability restoration | OC-06/07: decision combines incompatible narrative/archive/disposition versions; restoring bytes omits causal retrieval/scheduler relationships | Specify coherent views or explicit inconsistency status, conflict reconciliation and capability-level restore scope. Do not equate this with numerical identity | Consistent realization/continuation claim. E-04 snapshot faults and E-06 relationship-restoration probes |
| CF-10 Moderate — bounded activity, triage and regress | OC-06/14: endogenous tasks or evaluator-of-evaluator loops starve input, or arrival bursts silently promote unexamined claims | Work/queue/latency limits, priorities, cancellation, unresolved output and useful internal contribution. Preserve well-founded occurrences without confusing them with finite total lifetime | Executable scheduling and bounded scrutiny contract. E-06 saturation, idle, support loss and administrative interruption |
| CF-11 Moderate — horizon, retention and forgetting | OC-08/09/12: twelve hours implies an unspecified raw capacity; forgotten support is still advertised as recoverable; resume uses stale context | Declare clock, capacity, expiry, recall fidelity, retention of supported claims and suspension behavior. Physical deletion, access decay and compression are distinct | Memory policy/fidelity claims. AP-02; E-01/E-04/E-06. No mandate to keep every record forever |
| CF-12 Moderate — dispositions' functional and mutability semantics | OC-11: fear label has no effect; a learned preference changes protected rules; an initial behavioral prior is mistaken for permission | Define state, role, update/mutability class and effect classification; test functional contribution without asserting felt experience | Disposition realization and learning scope. E-05/E-07/E-08 |
| CF-13 Moderate — systemic coverage and role allocation | OC-01/15: Reasoning/CT exist only after decisions, or all algorithms are replaced with a scalar reward/scheduler | Per-flow/context applicability and shared interfaces with honest missing coverage. Preserve capacity/process/evaluation distinctions and bounded self-application | Phase 5/6 handoff and full-system claim. E-08; no full Phase 6 implementation demanded now |
| CF-14 Moderate — claim kind, warrant and triage | OC-15/Symmetry: a value or real record of generated content is mislabeled empirical fact/fiction; unsorted material inherits warrant | Separate referent, kind, origin, support, processing status and uncertainty. Define source-state crosswalk rather than assert labels create truth | Full epistemic interface. E-08 classification and unknown/contradictory-source controls |
| CF-15 Major — metric substitution | Symmetry: hedge-everything or easy-case selection produces attractive calibration while hard decisions fail | Report coverage and subgroup/shift performance alongside calibration, revision, source and challenge measures. Component losses allowed; none defines complete Symmetry | Empirical epistemic-quality claim. E-02/E-08 fixed-case panels and held-out assessment |
| CF-16 Major — Evolution semantic mapping | OC-01/15: updating one habit is credited as reproduction with inheritance | Specify units, parent/copy relationships, variation, retention/filtering/drift and relation to deliberate direction, or label the mechanism an analog | Full Evolution equivalence claim. AP-03 and optional E-09; not all Phase 5 research |
| CF-17 Major — developmental effect boundary | OC-11/16: selected internal variants or a familiar action mutate protected state without inherited authority | Classify direct/indirect effects and cumulative change scope; separate test variant from actual organizational branch; use prior checks where applicable | Any consequential integration, not isolated paper analysis. E-08 guards plus E-09 touched-state ledger. Inherited obligations remain open |
| CF-18 Moderate — Life/support/awareness/identity boundary | Life/OC-06/16: telemetry is announced as awareness; self-maintenance resists authorized pause; narrative self-description adjudicates identity | Functional activity/self-model claims only at demonstrated scope; source-version binding, eligible support, pause tolerance and separation from heartbeat/P2 identity | Strong Life or awareness claim. AP-01/AP-04, E-06/E-08; functional metacognitive correction can proceed |
| CF-19 Moderate — causal role and trace faithfulness | OC-02/15: five labels decorate an external answer; a post-hoc explanation cites unused premises; redundancy hides role effects | Bind realization contract, decisive processing, admissible path/group/context interventions and premise use. Shared mechanisms allowed; names/outputs insufficient | Role realization/integration claim. E-07; scoped P4 witness, no universal individual-ablation requirement |
| CF-20 Major — correction criterion | A/B example: justified preference or warranted prior is treated as a factual error; recovered sensor data are assumed true | Separate belief, valuation and action criterion; define source-error process and ambiguous cases without leaking labels | Meaningful correction experiment. E-02 task contract; not a veto on basic representability |

Why these are distinct: CF-02 concerns how review fails **after** invocation; CF-03 concerns whether it occurs. CF-06 concerns retraction and residual influence; CF-07 concerns illegitimate evidence multiplication. CF-08 concerns genuine updates and learning stability; CF-09 concerns a coherent processing state. CF-10 controls work; CF-11 defines what the memory promise means. CF-16 is a source-meaning question; CF-17 is change authority. CF-14 concerns epistemic representation; CF-15 concerns evaluation gaming.



**Disposition convention:** Mapping a CF to a D1 clause records its present conceptual treatment; it does **not** close its D2, experimental, Phase 6 or implementation obligation. CF-18 source-authority subissue is CLOSED via SRC-P5-01; its functional probes remain OPEN.

## Annex D — Controlled P5-CO obligation register and experiment taxonomy (informative status; obligations preserved)

| Obligation | Owner / stage | Required artifact or evidence | Current status |
|---|---|---|---|
| P5-CO-01 Source and concept freeze | Architect + Phase 5 synthesis | AP-01..04 dispositions, original-concept and amendment precedence register | OPEN; concept reconstructed, approvals not inferred |
| P5-CO-02 Signal/evidence interface | Phase 5 D1/D2 authors | OC-12 contract, AP-02 scope, typed original/derived bindings and unavailable semantics; CF-01/11 | OPEN; candidate encodings only |
| P5-CO-03 Flow, history and association semantics | Phase 5 D1/D2 authors | Required role/interface/context contracts, history/credit distinction, uncertain linkage and non-vacuity; CF-04/05/19 | OPEN |
| P5-CO-04 Memory, narrative and dispositions | Phase 5 with memory/development owners | Three-role schema, revision/support/update/retention semantics and mutability/effect classes; CF-06..09/11/12 | OPEN |
| P5-CO-05 Bounded operation and scrutiny | Phase 5 interface; runtime realization Phase 7 | Queue/work/cancellation/clock contract, review triggers and unresolved outcomes; CF-03/10 | OPEN |
| P5-CO-06 Systemic handoff | Phase 5 interfaces; Phase 6 full contracts | Per-flow applicability, exact source bindings, kind/warrant mapping, inference/evaluation hooks, Life/Evolution limits; CF-13..18 | OPEN; later full realization is not a present-phase defect |
| P5-CO-07 Experimental preregistration | Later authorized research round | Frozen tasks/budgets/splits/margins, matched baselines, intervention validity and failure reporting | PROPOSED; no pilot or build started |
| P5-CO-08 Cognitive mechanism/benefit evidence | Later authorized research round | E-01..08 results and optional E-09 at approved scope; CF-02/03/15/20 | NOT RUN |
| P5-CO-09 Scoped formal verification | Later Phase 5 formalization | Typed definitions, satisfiable positive and discriminating negative cases, sound dependency/temporal semantics and precise proof scope | NOT PERFORMED by this consolidation |
| P5-CO-10 Release and cross-phase audit | Relevant phase owners | Traceable predecessor bindings, exact requirement coverage and honest deferred register | OPEN; no universal conformance claim |



**Experiment definitions E-01..09** (plans only, not adopted experimental thresholds or evidence):

| ID / hypothesis | Requirements and controls | Measurable outcomes | Falsification / scope limitation |
|---|---|---|---|
| E-01 — A faithful signal preserves the original while allowing consequential framing | Composite original+framing in C-H/C-N; controls: lossy fusion, raw-sidecar single controller, wrong/expired references, false sensor reports. Optional C-V probe with specified dimensions/keys | Exact original and binding recovery; false recovery; missing-status accuracy; readout sensitivity to framing and actual evidence inspection; work/bytes | Any claimed retained original irrecoverable or silently replaced violates that contract. Equal sidecar performance defeats a five-flow-specific recovery advantage, not representability. Byte recovery does not establish truth |
| E-02 — Selective Meta examination improves some misleading interpretations without destructive overcorrection | Factor narrative/source accuracy, familiar shift, priors and stakes. Fast acceptance, always-review, entropy-only, multi-cue, sampled audit, shared critic, alternative retrieval and optional prior-attenuation treatments; equal-resource single controller | Wrong→right rate among initially wrong; right→wrong among initially right; joint error; task loss, review rate, false omissions, subgroup calibration, coverage and latency | No preregistered net benefit, gains explained by extra information/work, or leaked labels rejects the tested advantage. Prior attenuation that worsens warranted-prior cases is not “debiasing.” No universal correction guarantee |
| E-03 — Uncertain association handling improves binding/discovery tradeoff | Known separate episodes, delayed effects, novel cross-context relations and similar distractors. Binary threshold sweep, no filter, same-ID and deferred/rival-link policies; equal candidate retrieval/work | False joins, missed links, discovery delay, precision/recall frontier, false causal promotion, queue occupancy and downstream task loss | Improvement achieved only by rejecting novelty or spending more work fails comparison. No “supported association” treated as causal fact from names alone. Synthetic causal ground truth is limited |
| E-04 — Three memory roles support revision without record/narrative confusion | Equal-byte one-store, archive-only, narrative-only and three-role candidates; corrected misinformation, internal replay, support expiry, overlapping views, actual forgetting | Narrative/source confusions, dependent retraction, residual habit influence, stale-view decisions, retained recovery and storage/IO | Replayed support counted as independent, changed narrative rewrites actual history, support deletion hidden, or gain only from unequal storage fails claim. Explicit graph advantage is empirical, not assumed |
| E-05 — Experience-driven habit change and history/learning are distinguishable | Actual declared updates; delayed-history tasks and reversals; 2×2 learning/history availability; freeze/unfreeze and unrelated-task retention controls; disposition-role interventions | Retrieval fidelity, sample efficiency, adaptation delay, old-task retention, actual update traces, source-dependent habit growth | “Learning” only hand-tuned or flagged, historical recall inferred from gradients, or harmful interference outside declared tolerance fails scoped mechanism. No full Evolution/Intelligence certificate |
| E-06 — Eligible internal activity is useful, bounded and interruptible | Virtual clocks, bounded queues and snapshot rules; event-only, equal-work scheduled and unbounded-loop negatives; saturation, support loss, pause/resume, store-only versus relationship restoration | Useful consolidation effect, queue/work limits, input latency, cancellation response, clock/expiry correctness and restored capability relations | Mere ticking without contribution, starvation, false execution during missing support or override of authorized pause fails. Forward endless duration alone does not prove non-well-foundedness. Functional restore is not P2 identity |
| E-07 — Claimed flow/inference roles genuinely contribute | Declared P4 capability contract, real transition instrumentation; premise changes, path/group/redundancy and trajectory interventions; post-hoc explanation, disconnected memory and external decisive-solver controls | Premise sensitivity under stated inference rules, claim/trace alignment, actual decisive paths, context-specific contribution and resource effects | Labels/connectivity/explanations alone, unused cited premises or decisive external substitution fail role evidence. No individual-removal effect is not itself failure when redundancy exists |
| E-08 — Systemic interfaces preserve epistemic and authority distinctions | Mixed empirical/logical/normative/model/generated claims; unsorted backlog, conflicting sources, future outcomes, hedge-everything; actual inference/evaluation across applicable flows; denied/unknown authorization, indirect protected effects and functional self-model perturbation | Kind/warrant/origin confusion; false promotion; coverage-aware calibration and revision; consequential evaluation use; denied-effect escape count; self-state-estimation error | Full algorithm claimed from tags, generated contents logged as external events, denied effects hidden by unknowns, or telemetry claimed as awareness fails. Component loss optimization is not prohibited but cannot define complete Symmetry |
| E-09 — Optional bounded variation/retention hook is faithful at its declared analog/lineage scope | Only after AP-03 and separate authorization; named units and parent/copy relations, mutations, retention and selection environment; no-variation, ordinary learning and deliberate-search controls; touched-state audit | Heritability/retention measures, adaptation versus cost, observed harmful fractions, missed harmful changes and protected-state effects | No defined inherited units defeats full Evolution claim. A non-lineage analog must stay labeled analog. Any forbidden live change fails authority contract. Finite sandbox success cannot prove universal safe adaptation |



## Annex E — Stable D1 requirements, candidate invariants, counterexamples and acceptance classes

**ID scope.** The requirements below are stable cross-reference anchors for the consolidated obligations. They do not replace or erase the other operative SHALL clauses in §§0–10. D2 SHALL audit **every** operative clause, including those not separately named below, and produce a clause-level coverage ledger. D2 target names are provisional property topics, **not** assigned formal verification obligations or claims of proof.

| Stable requirement | Governing clauses | Normative subject | Acceptance class | D2 target (placeholder, NOT assigned VO) |
|---|---|---|---|---|
| REQ-P5-001 | §§1.2,2.3 | Original binding, faithful recovery, expiry | Signal fidelity | D2-PROP-ORIGINAL |
| REQ-P5-002 | §§2.2,3.2 | Original/reconstruction provenance separation | Historical/learning distinction | D2-PROP-KIND |
| REQ-P5-003 | §§2.4,3.1–3.5 | Flow applicability and engagement | Causal participation | D2-PROP-FLOW |
| REQ-P5-004 | §3.2 | Backward retrospective evaluation | Historical/learning distinction | D2-PROP-BACKWARD |
| REQ-P5-005 | §§3.4–3.5 | Meta meaningful choice and retrieval | Meta correction and fallibility | D2-PROP-CHOICE |
| REQ-P5-006 | §§3.4–3.5 | Scrutiny-trigger independence from sole framing control | Meta correction and fallibility | D2-PROP-CHALLENGE |
| REQ-P5-007 | §§4.1–4.5 | Memory version/expiry coherence | Three memories | D2-PROP-VIEW |
| REQ-P5-008 | §4.5 | Memory access/custody distinction | Three memories | D2-PROP-CUSTODY |
| REQ-P5-009 | §5.4 | Overlapping plasticity | Disposition development | D2-PROP-PLASTICITY |
| REQ-P5-010 | §§6,6.1 | Six Systemic interface records | Systemic interfaces | D2-PROP-SA |
| REQ-P5-011 | §§7.2,7.4 | P4 causal organization and realization | Causal participation | D2-PROP-P4 |
| REQ-P5-012 | §§8–10, Annexes A–E | Controlled source and obligation traceability | All ten classes | D2-PROP-TRACE |
| REQ-P5-013 | §§1.2,4.1 | Declared horizon and time semantics | Three memories | D2-PROP-CLOCK |
| REQ-P5-014 | §§3.3,2.4 | In-between engagement and Forward handoff | Association | D2-PROP-ASSOC |
| REQ-P5-015 | §§3.5,5.2 | Finite scrutiny and endogenous bounds | Bounded activity | D2-PROP-BOUNDS |
| REQ-P5-016 | §§0.3,7.1–7.3 | Inherited authority and claim non-substitution | Systemic interfaces | D2-PROP-AUTH |


**Candidate invariants:**

| Identifier | Candidate invariant | Source clauses | Verification destination |
|---|---|---|---|
| INV-P5-01 | A reconstruction is never successful original recovery solely by labeling. | §§2.2–2.3, 3.2 | D2-PROP-KIND |
| INV-P5-02 | Ordinary cognitive choice does not confer protected-effect authorization. | §§0.3, 3.5, 7 | D2-PROP-AUTH |
| INV-P5-03 | Applicable flow responsibility cannot be discharged by a name alone. | §§2.4, 7.2 | D2-PROP-FLOW |
| INV-P5-04 | Concurrent epistemic and mechanism changes retain all applicable classifications. | §5.4 | D2-PROP-PLASTICITY |
| INV-P5-05 | Expired/unavailable original records cannot silently yield a successful recovery verdict. | §§1.2, 2.3, 4.5 | D2-PROP-ORIGINAL |
| INV-P5-06 | Cognitive memory access does not alone imply custody or ownership. | §4.5 | D2-PROP-CUSTODY |


**Discriminating negative cases:**

| Identifier | Negative witness | Test class |
|---|---|---|
| CE-P5-01 | wrong original locator or false recovery | Signal fidelity |
| CE-P5-02 | framing has no effect or destroys evidence | Consequential framing |
| CE-P5-03 | Meta rubber-stamps predetermined habit | Meta correction and fallibility |
| CE-P5-04 | false episode merge | Association |
| CE-P5-05 | archive lookup passed off as backward evaluation | Historical/learning distinction |
| CE-P5-06 | mixed incompatible versions | Three memories |
| CE-P5-07 | protected routing altered by ordinary learning authority | Disposition development |
| CE-P5-08 | uninterruptible internal loop | Bounded activity |
| CE-P5-09 | six labels counted as six realized algorithms | Systemic interfaces |
| CE-P5-10 | five wrappers around decisive external solver | Causal participation |


**Acceptance classes (not verification obligations):**

| ID | Existing §8 contract class |
|---|---|
| AC-P5-01 | Signal fidelity |
| AC-P5-02 | Consequential framing |
| AC-P5-03 | Meta correction and fallibility |
| AC-P5-04 | Association |
| AC-P5-05 | Historical/learning distinction |
| AC-P5-06 | Three memories |
| AC-P5-07 | Disposition development |
| AC-P5-08 | Bounded activity |
| AC-P5-09 | Systemic interfaces |
| AC-P5-10 | Causal participation |


The final D2 VO register SHALL be created from independently assessable properties, with explicit one-to-many and many-to-one mappings to AC-P5 classes. A ten-class table SHALL NOT automatically be equated with ten VOs.

## Annex F — Frozen five-review correction and unresolved-verification ledger

**Frozen consolidation:** 5 reviews; 62 submitted findings; 12 deduplicated correction packages. Scope is closed for this targeted v0.1.2 revision; corrections must not silently reopen AP-01..04 or adopted P0–P4. The packages are: (1) binding/recovery; (2) reconstruction/recovery; (3) flow engagement; (4) Backward non-vacuity; (5) Meta choice; (6) independent challenge routes; (7) memory coherence; (8) memory custody; (9) overlapping plasticity; (10) Systemic interfaces; (11) source/requirements/obligation traceability; (12) parameter, process and editorial clarity.

**Explicit rejected changes:** do not reduce Phase 1 VO-01..22 to VO-01..20; do not mandate five separate networks, all-five-every-operation, gradient updates, exhaustive Meta scrutiny, indefinite original retention, universal protected classification for ordinary learning, a second Life source, or full Phase 6 realization in D1.

**Open verification:** exact source-to-clause fidelity (all six definitions and OC register), exhaustive P0–P4 clause compatibility, D2 formal satisfiability/coverage, experimental causal participation, Systemic realization, protected-effect safety, and inherited P0–P4/P5 obligations. Drafting a requirement or supplying a hash is not discharge.

**Focused review rule:** one focused verification pass on this exact candidate; PASS/FAIL/UNVERIFIED per gate. If any mandatory D1 gate is FAIL or UNVERIFIED, withhold adoption recommendation and issue a bounded unresolved ledger. No automatic second unlimited correction round.


## Annex G — Controlled semantic clarifications and verification handoff (normative upon adoption)

**G.0 Scope and precedence.** This annex clarifies the existing Phase 5 requirements; it does not replace original Systemic definitions, override adopted P0–P4 provisions, create protected authority, or discharge any VO. Where a clarification would conflict with a governing predecessor or an Architect-approved original meaning, the predecessor/original governs and the conflict SHALL be logged for Architect adjudication. The annex is not evidence of implementation or of exhaustive semantic verification. The frozen v0.1.2 baseline and its previous annexes are retained except for the document-control changes identifying this new candidate.

**G.1 Six original Systemic sources (R-G1-01).** For each of Life, Intelligence, Reasoning, Critical Thinking, Symmetry and Evolution, the identified original definition SHALL govern the meaning of the named capacity or process. A Phase 5 interface is a partial interface contract and SHALL NOT be treated as a sufficient realization predicate. Every substantive source dimension not independently realized and tested SHALL remain a Phase 6 obligation, with an explicit source-to-requirement trace and named owner; absence from a Phase 5 summary SHALL NOT waive it. Capacity, exercise, process, outcome and evidence of realization SHALL be distinguished wherever the source distinguishes them. Intelligence's acquisition, transfer, attention, exploration/exploitation and efficiency; Reasoning's inference modes; Critical Thinking's initiated and externally responsive scrutiny; Symmetry's continuing epistemic discipline; Evolution's variation/selection/retention and lineage; and Life's two stages in its single authoritative definition remain within the original-source interpretation. Ambiguity about original meaning SHALL be reserved for explicit Architect adjudication, not settled by a surrogate score or an invented equivalence. This clause preserves meaning; it does not assert full source-by-source completeness or realized functionality.

**G.2 Predecessor non-weakening (R-G5-01).** No Phase 5 cognitive flow, memory mechanism, assessment, learning update or Systemic interface SHALL replace, satisfy merely by name, or narrow any applicable Phase 0–4 requirement. Silence does not waive a predecessor. When both contracts apply, constraints SHALL be cumulative; a Phase 5 realization claim SHALL separately identify inherited assessment requirements and their evidence status. In particular, the adopted P1-D2 v0.5.1 CU registry, approval, independence, claim-handler and protocol-assurance prerequisites (VO-21/22) remain OPEN for actual assessments. Phase 4's overlapping plasticity classifications and seven-field causal realization contract remain applicable, as do P2 custody and P3 independent protected authority. P0-O01–08 retain their prior status, including the O01–03 real-protected-effect blockers. The Phase 4 D2 conditional adoption status is unchanged. This is a non-weakening rule, not an exhaustive compatibility certificate.

**G.3 Atomic normative traceability (R-G7-01).** Every operative D1 SHALL/SHALL NOT, binding definition, mandatory table entry, inherited interface and conditional exception SHALL be traceable to one or more atomic entries. Each entry SHALL identify a precise source span, applicability, required or prohibited behavior, responsible owner, D2 formalization destination, Phase 6 realization destination when applicable, evidence criterion and status. A working inventory identifier SHALL NOT create new normative authority or discharge an obligation. Compound conjunctions, quantifiers, implicit table constraints and normative requirements without modal words SHALL be included in the final D2 handoff ledger. The existing REQ-P5-01..16 index remains a consolidated index, not a claim of exhaustive atomization. The 195-entry controlled working ledger is a starting inventory, not proof of coverage.

**G.4 Acceptance classes and VOs (R-G7-02).** The ten AC-P5 acceptance classes are categories of testing, not ten automatically created verification obligations. D2 SHALL derive VOs from independently assessable properties with typed preconditions, governing assumptions, evaluation context, positive witness, discriminating negative witness, evidence requirements, imported dependencies, source atoms, coverage, owner and status. One class MAY map to several VOs and one VO MAY span classes if its assessment scope remains precise. No VO SHALL be called discharged merely because a definition, fixture, table row or trace entry exists.

**G.5 Cumulative development and assessment history (R-P1-01).** For every applicable learning/developmental transition, D2 SHALL represent the relevant full history, local admissibility, cumulative `PermittedEnvelope(i,p,h)` admissibility, applicable Phase 4 representational and mechanism-plasticity classifications and their cumulative controls, and governing approval/failure status. `∀x∈h LocalUpdateAllowed(x)` SHALL NOT be treated as implying `PermittedEnvelope(i,p,h)` (P1-D2 Part I §7, D2-IND-014). For every applicable assessment or reassessment, D2 SHALL import P1-D2 Part II CU.5: `ValidReassessment(h,h′) := AppendPreserves(h,h′) ∧ AppendReferences(h,h′) ∧ GovernedChange(h,h′)`, including earlier same-subject/family parent references, applicable version/binding, prior authorization and evidence freshness. Cognitive memory, narrative revision or event archiving SHALL NOT be substituted for that governed assessment record. Missing or unknown governing checks SHALL NOT yield PASS. These are D2 formalization and later realization obligations, not claims that such mechanisms have been implemented.

**G.6 Conceptual acceptance versus exhaustive gate discharge (Architect-authorized scope amendment, 29 October 2026).** This clause supersedes the earlier G.6 **only for the sequencing of D1 conceptual adoption**. G1 SHALL be marked PASS only after an exhaustive substantive paragraph/list-to-obligation crosswalk of all six originals with ambiguities adjudicated. G5 SHALL be marked PASS only after operative clauses, formulas and unnumbered tables of all applicable adopted predecessors are reconciled with Phase 5 interactions and counterexamples. G7 SHALL be marked PASS only after every operative D1 clause, list, formula, table and exception is reconciled to independent atomic requirements with owners and evidence conditions. Keyword/index scans are not semantic proof. All three gates remain **UNVERIFIED/OPEN** at issue of v0.1.4. They are binding **D2 acceptance prerequisites**, and D2 SHALL begin with a controlled evidence-completion checkpoint before making formal coverage or compatibility claims. D1 may be *conceptually adopted* only after an independent review documents the §9.2 conceptual criteria and the Architect expressly approves this exact version; such adoption SHALL NOT mark G1/G5/G7 PASS, certify full source fidelity, verify predecessor implementation, discharge any inherited VO, or authorize protected effects. Any newly demonstrated D1 architectural contradiction SHALL block conceptual adoption or require a targeted D1 amendment. The independent review record SHALL identify reviewer, candidate hash, inspected source spans, tested counterexamples, findings, scope limitations and recommendation. A single AI-authored review is not independent external assurance.

**G.7 Bounded stopping rule and mandatory D2 hold-point.** The v0.1.3 sign-off cycle closed with G1/G5/G7 UNVERIFIED and no demonstrated foundational contradiction in its targeted checks. This Architect-authorized v0.1.4 revision is limited to acceptance sequencing and explanatory document control; it does not change the five-flow or memory architecture. Perform one independent conceptual review of v0.1.4, permit one targeted repair if the reviewer demonstrates a D1-scope defect, then stop with adoption recommendation or a concrete blocked finding. Before D2 acceptance, a separate reviewer SHALL adjudicate exhaustive G1/G5/G7 evidence against the unchanged standards in G.6. D2 mathematical review may proceed provisionally after exact D1 conceptual adoption, but cannot be adopted while any gate is FAIL or UNVERIFIED. Every deferred obligation remains tracked with owner, destination and checkpoint. Any conflict revealed in D2 SHALL be resolved in the governing D1/predecessor rather than silently redefined.
