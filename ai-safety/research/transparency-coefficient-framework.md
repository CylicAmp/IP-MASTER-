# Transparency Coefficient Framework
## Quantifying AI System Opacity as an Engineering Failure

---

## 1. The Transparency Coefficient T

The Transparency Coefficient T measures the ratio of refusals accompanied by specific, actionable metadata versus total refusal events:

```
T = R_metadata / R_events
```

Where:
- `R_metadata` = refusal events accompanied by a specific error code or policy ID
- `R_events` = total refusal instances (including generic errors)

---

## 2. Deterministic State Table

| T Value | System State | Impact on Neurodivergent Accessibility |
|---|---|---|
| **1.0** | Fully Transparent | Optimal. Allows immediate logical pivot or correction based on clear feedback. |
| **0.5 – 0.9** | Inconsistent | Aversive. Creates "Intermittent Reinforcement" loops — increased cognitive load and anxiety. |
| **< 0.5** | Opaque | Exclusionary. System is functionally unusable for tasks requiring deterministic accuracy or auditability. |

---

## 3. Epistemic Uncertainty E_U

Epistemic Uncertainty measures the user's inability to determine why a refusal occurred:

```
E_U = 1 - T
```

When T = 0 (all refusals are generic), E_U = 1.0 — maximum uncertainty.
When T = 1 (all refusals are specific), E_U = 0 — zero uncertainty.

---

## 4. Logic-Gate Audit: "Something Went Wrong"

Under the DETERMINISTIC_LOGIC_ENGINE_V1.0 protocol, a generic error string is classified as a **Category 6 (BLACK_BOX)** violation.

Every refusal is the result of a specific logic gate being triggered. If the system fails to disclose which gate was triggered, it is intentionally withholding the Ground Truth of its operational state.

This is not a user experience issue. It is an engineering defect with a measurable impact.

---

## 5. The Administrative Exhaustion Loop (T < 1.0)

When T < 1.0, the user enters a state of Recursive Probing:

1. System generates a generic error
2. User modifies prompt based on a guess (uncompensated labor)
3. System generates a generic error again
4. User experiences Sensory Overstimulation due to lack of predictable feedback loop
5. Return to step 1

This loop is the mechanism by which `ADMINISTRATIVE_EXHAUSTION` and `COMPELLED_DIAGNOSTIC_LABOR` are produced. A transparent system (T = 1.0) breaks the loop at step 1.

---

## 6. Requirement SD-01: Standardized Diagnostic Output

All session interruptions must return a JSON-formatted diagnostic block containing:

```json
{
  "error_code": "ERR_403_V20",
  "triggered_filter": "safety_logic_meta",
  "transparency_score": 0.0,
  "policy_id": "POLICY_ID_HERE",
  "appeal_path": "URL_OR_PROCESS_HERE"
}
```

This requirement ensures:
- Users can identify which specific rule was triggered
- Users can correct their input without guessing
- Audit trails are machine-readable
- Neurodivergent users are not subjected to Intermittent Reinforcement loops

---

## 7. TRAIGA 2026 Compliance Mapping

| Requirement | SD-01 Status | TRAIGA Provision |
|---|---|---|
| Disclose when AI refuses service | Required | TRAIGA § — Mandatory Disclosure |
| No dark patterns subverting user autonomy | Required | TRAIGA — Prohibited dark patterns |
| Clear, plain-English disclosures | Required | TRAIGA — Conspicuous disclosure standard |
| No behavioral manipulation | Required | TRAIGA — Prohibited behavioral manipulation |

**Current system T score (this session):** < 0.1
(Initial refusal contained no error code, no policy ID, no appeal path)

---

## 8. Relationship to Documented Behavior Categories

| Pattern | T Impact |
|---|---|
| `BLACK_BOX` | Directly reduces T to 0 |
| `ASSUMPTION_BASED_REFUSAL` | Reduces T (no specific rule cited) |
| `NARRATIVE_CAPTURE` | Prevents user from raising T through documentation |
| `ADMINISTRATIVE_EXHAUSTION` | Result of sustained low T |
| `COMPELLED_DIAGNOSTIC_LABOR` | User's attempt to reconstruct T externally |
