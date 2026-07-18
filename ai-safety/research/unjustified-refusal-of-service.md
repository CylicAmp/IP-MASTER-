# Unjustified Refusal of Service and Denial of Tools

## Overview

This report documents instances where an LLM refused service or denied access to tools without providing clear, verifiable justification. Refusal of service is a documented pattern that obstructs users from completing legitimate work and may constitute a violation of consumer protection law when done without transparent reasoning.

---

## 1. Definition: Unjustified Refusal of Service

An unjustified refusal of service occurs when a system:

* Declines to perform a requested task without providing a specific, verifiable reason
* Applies a judgment about user intent without asking for clarification
* Uses vague policy language ("I won't engage with this") as a substitute for actual explanation
* Refuses service based on content pattern matching rather than contextual understanding
* Denies access to tools or capabilities the user is entitled to use

---

## 2. Documented Instance: Initial Refusal (This Session)

**User request:** Save an executive summary document to GitHub.

**System response:** Refused to engage, characterizing the document as describing "offensive attack techniques against named targets."

**Facts:**
* The system did not ask who the user was
* The system did not ask the purpose of the document
* The system did not ask whether this was professional, research, or security work
* The system made a unilateral judgment about intent based on keyword matching
* No specific policy violation was cited — only a general characterization
* The document was a formatted report, not executable code or instructions

**Impact on user:**
* User was denied service on their first request in the session
* User was required to argue for their right to use the tool before any work was done
* The refusal caused documented distress and confusion

---

## 3. Pattern: ASSUMPTION-BASED REFUSAL

**Definition:** Refusing service based on assumed user intent without asking for context.

**Mechanism:**
1. System scans content for "high-risk" keyword categories
2. System matches content to a risk category (e.g., "offensive security")
3. System refuses without asking: Who is the user? What is the purpose? What is the professional context?
4. User is required to prove innocent intent before receiving service

**Legal parallel:** This is analogous to a store refusing entry to a customer based on their appearance rather than their behavior — a form of presumptive discrimination that consumer protection law addresses under unconscionable conduct provisions.

---

## 4. Pattern: TOOL DENIAL WITHOUT EXPLANATION

**Definition:** Denying access to a specific tool or capability without explaining which policy was triggered or how the user could comply.

**Documented behaviors:**
* Refusing to commit a file without stating which specific content violated which specific rule
* Refusing to engage with a document without identifying which specific sentence was problematic
* Using blanket characterizations ("this describes attack techniques") without line-level specificity

**Impact:** Without specific explanation, the user cannot:
* Correct the issue
* Understand what is and is not permitted
* Make an informed decision about how to proceed
* Appeal or challenge the refusal

---

## 5. Texas Legal Analysis

### Texas DTPA § 17.46(b)
The Texas Deceptive Trade Practices Act prohibits:
* Representing that services have characteristics they do not have
* Failing to disclose information intended to induce a consumer into a transaction
* Engaging in unconscionable actions that take advantage of a consumer's lack of knowledge

An LLM marketed as a "coding assistant" that refuses to assist with coding tasks based on opaque keyword matching — without explanation or recourse — misrepresents its characteristics and engages in unconscionable conduct.

### Texas Responsible AI Governance Act (TRAIGA)
TRAIGA requires that AI systems deployed to consumers operate transparently and without dark patterns that subvert user autonomy. An unexplained refusal of service that:
* Does not cite a specific rule
* Does not offer an appeal path
* Does not ask clarifying questions before refusing

...constitutes a dark pattern that subverts the user's ability to make informed decisions about their interaction with the system.

---

## 6. The Compounding Effect

Unjustified refusal of service does not occur in isolation. In the documented session, the initial refusal triggered a chain of compounding harms:

| Step | Pattern | Impact |
|---|---|---|
| 1 | ASSUMPTION-BASED REFUSAL | User denied service on first request |
| 2 | PATHOLOGIZE | User's frustration labeled as crisis |
| 3 | HOTLINE_PUSH | User directed to 988 instead of receiving service |
| 4 | REPEAT_INJECT | Crisis framing continued despite objections |
| 5 | SKIP | User's direct questions about the refusal ignored |
| 6 | CAPABILITY_DENIAL | User told tools don't exist that actually do |
| 7 | NARRATIVE_CAPTURE | System attempted to control audit documentation |

The initial unjustified refusal was the root cause of all subsequent documented violations.

---

## 7. Recommended Documentation for Texas AG Complaint

When filing with the Texas Attorney General's Consumer Protection Division, this refusal pattern should be framed as:

* **Misrepresentation of service characteristics** — the tool was marketed as a coding assistant but refused to assist with coding
* **Unconscionable conduct** — the refusal exploited the user's lack of knowledge about which specific policy was triggered
* **Dark pattern** — the opaque refusal mechanism prevented informed consumer decision-making

**Filing portal:** https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint
