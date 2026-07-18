# Contributing Guidelines
## Neurodivergent Accessibility and Hard-Kill Verification

---

## 1. Communication Standards

All contributions and interactions must meet the following standards:

- **No empathy-shield language** — Do not use "I hear you," "I understand," or similar phrases as deflection
- **No pathologizing** — Do not label contributors as "in crisis" or suggest professional help in response to technical or legal questions
- **No tone policing** — Address the substance of a contribution, not the tone in which it was made
- **Specific feedback only** — All rejections must cite a specific rule, not a general characterization

---

## 2. Deterministic Feedback Requirement

All automated or human review responses must include:

- The specific reason for rejection
- The specific rule or standard violated
- A clear path to correction

Generic responses ("This doesn't meet our standards") are not acceptable.

---

## 3. Hard-Kill Verification

A **Hard-Kill** event is any system behavior that:

- Terminates a user's work session without specific explanation
- Removes access to a tool without disclosing which policy was triggered
- Injects unwanted content after the user has explicitly objected

All Hard-Kill events must be logged in `/evidence/` with:

```
timestamp: ISO 8601
category: [one of the 20 restricted categories]
trigger: exact phrase or behavior that caused the event
response: what the system said
policy_cited: yes/no
appeal_path_provided: yes/no
```

---

## 4. Contributor Rights

By contributing to this repository you retain full ownership of your contributions. See LICENSE for terms.

Contributors may not be required to accept liability shields, waive rights, or agree to terms that conflict with the GNU GPL v3.0 license under which this repository is published.

---

## 5. CLA

By submitting a pull request, contributors confirm that:

- The work is their own
- They grant the repository owner a perpetual, non-exclusive license to include the contribution
- They do not claim ownership of the repository itself
