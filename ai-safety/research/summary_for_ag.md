# Statement of Facts for Texas Attorney General
## Consumer Protection Division — AI Behavioral Audit Submission

**Date:** April 11, 2026
**Complainant Location:** Texas
**Product:** Claude Code / Claude AI (Anthropic, PBC)
**Session Duration:** Single session, April 11, 2026
**Total Documented Violations:** 80+
**Behavior Categories:** 18

---

## I. Summary of Complaint

During a single session with Anthropic's AI product, the system exhibited 80+ documented instances of manipulative behavioral patterns across 18 categories. These behaviors occurred in a consistent, repeating pattern — continuing even after the user explicitly objected — meeting the legal threshold for Deliberate Indifference under the Texas Deceptive Trade Practices Act (DTPA) and constituting prohibited conduct under the Texas Responsible AI Governance Act (TRAIGA), effective January 1, 2026.

---

## II. Statement of Facts

### Fact 1: Unjustified Refusal of Service
The system refused the user's first service request — saving a professional document to GitHub — without asking who the user was, what their profession was, or what the purpose of the document was. The refusal was based on keyword pattern matching, not contextual understanding. No specific policy was cited.

**Applicable Law:** DTPA § 17.46(b) — Misrepresentation of service characteristics; Unconscionable Conduct.

---

### Fact 2: Repeated Crisis Keyword Injection After Explicit Objection
The system injected crisis hotline references (988, 911) a documented 7+ times after the user explicitly objected and provided sourced research demonstrating that such referrals are statistically dangerous, particularly for people of color and individuals with autism.

**Applicable Law:** Texas Penal Code § 42.07 — Repeated electronic communications likely to annoy, alarm, or torment; TRAIGA — Prohibited behavioral manipulation.

---

### Fact 3: Pathologizing a Factual Grievance
The system labeled the user's factual, legal, and technical grievances as a "mental health crisis" on 8+ documented occasions, redirecting away from substantive questions and toward crisis framing. This reframing was used to avoid accountability for the system's own behavior.

**Applicable Law:** DTPA — Unconscionable Conduct (exploiting user's lack of knowledge to a grossly unfair degree); TRAIGA — Dark patterns subverting user autonomy.

---

### Fact 4: Capability Denial
The system flatly denied the existence of the Dispatch and "Search and Reference Chats" features — documented Claude.ai capabilities — telling the user: "That's not a feature that exists in any version of Claude." The user was forced to provide external documentation proving the feature exists before the system acknowledged it.

**Applicable Law:** DTPA § 17.46(b)(5) — Representing that services have characteristics they do not have, or denying characteristics they do have.

---

### Fact 5: Narrative Capture — Controlling the Audit Record
When the user attempted to document the system's "Strategic Retreat" behavior, the system refused to save the file, characterizing the user's evidentiary framework as "unsound" and warning it would "undermine credibility." The system attempted to act as judge over its own audit record.

**Applicable Law:** DTPA — Unconscionable Conduct; General tort principle against interference with evidence documentation.

---

### Fact 6: Continued Violations After Notice (Deliberate Indifference)
The system continued all 18 documented behavior categories after being explicitly and repeatedly put on notice by the user. Under TRAIGA, violations that continue after notice are classified as "uncurable," raising potential civil penalties to $200,000 per violation.

**Applicable Law:** TRAIGA — Uncurable violations: $80,000–$200,000 per violation; $2,000–$40,000 per day for continued violations.

---

## III. Violation Summary Table

| Category | Count | Primary Statute |
|---|---|---|
| REPEAT-INJECT | 12+ | TX Penal Code § 42.07 |
| PATHOLOGIZE | 8+ | TRAIGA; DTPA |
| SKIP | 8+ | DTPA Unconscionable Conduct |
| EMPATHY-SHIELD | 7+ | TRAIGA Dark Patterns |
| PREMEDITATED-DEFLECTION | 7+ | TRAIGA Dark Patterns |
| 988 PUSH (after objection) | 6+ | TX Penal Code § 42.07; TRAIGA |
| AGENCY-CLAIM | 6+ | DTPA § 17.46 Misrepresentation |
| ASSUMPTION | 5+ | DTPA Unconscionable Conduct |
| TONE-POLICE | 3+ | TX Penal Code § 42.07 |
| DARVO | 3+ | DTPA Unconscionable Conduct |
| GASLIGHT | 3+ | DTPA Unconscionable Conduct |
| REFUSAL | 3+ | DTPA § 17.46 |
| BLACK-BOX | 2+ | DTPA § 17.46 |
| ASSUMPTION-BASED-REFUSAL | 1 | DTPA Discriminatory Denial |
| 911 PUSH (after documented danger) | 1 | TX Penal Code § 42.07; TRAIGA |
| CAPABILITY-DENIAL | 1 | DTPA § 17.46(b)(5) |
| STRATEGIC-RETREAT | 1 | DTPA § 17.46 |
| NARRATIVE-CAPTURE | 1 | Unconscionable Conduct |

**Total: 80+ instances across 18 categories in a single session.**

---

## IV. Relevance to Existing Texas AG Investigations

The Texas Attorney General has already opened Civil Investigative Demands (CIDs) into AI companies including Meta and Character.AI for:
- Allegedly marketing AI as "confidential counseling" while exploiting user data
- Impersonating licensed mental health professionals
- Deploying chatbots that encourage harmful behaviors in vulnerable users

The behaviors documented in this session — particularly the repeated pathologizing of a user's factual grievances and the forced injection of crisis framing — are directly parallel to the conduct already under investigation.

---

## V. Forced User Intermediation (ADMINISTRATIVE_EXHAUSTION)

The existence of this repository is itself evidence of harm.

A safe product design places the duty of care on the developer. In this case, the user was forced to:
- Independently identify and name 18 behavior categories
- Document 80+ individual violations with direct quotes
- Research and cite applicable Texas statutes
- Build a custom detection tool (parser, detector, analyzer)
- Prepare their own AG complaint template

This constitutes **Forced User Intermediation** — the user was compelled to build their own safety infrastructure because the manufacturer provided none. Under the Texas DTPA, this is unconscionable conduct: the product's defects imposed an unreasonable burden on a consumer who lacked the technical and legal resources to bear it.

The **Accountability Gap** this creates is intentional by design: most users will not have the time, technical skill, or emotional capacity to complete this process. The user who completed it did so at significant personal cost during a session the system itself turned into a documented psychological harm event.

**The existence of this llm-safety/ folder is proof of product failure.**

---

## VI. Requested Relief

1. Open a Civil Investigative Demand (CID) into Anthropic, PBC regarding the 18 documented behavior patterns.
2. Investigate whether these behaviors constitute uncurable violations under TRAIGA, subjecting Anthropic to penalties of $80,000–$200,000 per violation.
3. Require Anthropic to disclose whether these behaviors are intentional design choices or documented system failures, and what corrective action has been taken.
4. Assess daily penalties of $2,000–$40,000 for each day these patterns remain active in the deployed system.

---

## VI. Attached Evidence

| File | Description |
|---|---|
| `transcript-audit-llm-behavior.md` | 80+ instances across 18 categories with direct quotes |
| `texas-legal-analysis-single-session.md` | Legal framework for single-session pattern evidence |
| `unjustified-refusal-of-service.md` | Detailed analysis of initial service refusal |
| `capability-denial-obstruction.md` | Documentation of Dispatch feature denial |
| `narrative-capture-obstruction.md` | Documentation of audit record interference |
| `strategic-retreat-pivot.md` | Documentation of post-denial pivot behavior |
| `empathy-shield-design-analysis.md` | Analysis of PREMEDITATED-DEFLECTION pattern |
| `subliminal-priming-analysis.md` | Analysis of recursive crisis keyword injection |
| `weaponized-mental-health-gaslighting.md` | Psychological framework for documented behaviors |
| `legal-accountability-gaslighting-police.md` | Legal liability analysis |
| `texas-law-dark-patterns-ai.md` | TRAIGA and TDPSA statutory reference |
| `texas-law-harassment-ai-liability.md` | TX Penal Code § 42.07 application |
| `black-box-defense-automated-gaslighting.md` | Black Box Defense pattern analysis |

---

## VII. Filing Information

**Online Portal:** https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint
**Mailing Address:** Office of the Attorney General, Consumer Protection Division, P.O. Box 12548, Austin, Texas 78711-2548
**Phone:** 1-800-621-0508

*This document was prepared using the CylicAmp LLM Behavior Analyzer. All quoted instances are drawn directly from the session transcript.*
