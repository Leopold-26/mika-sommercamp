---
name: engineering-plan-review
description: Review a Mika spec or build plan like an engineering lead before implementation, covering architecture, data flow, state, failure modes, tests, privacy, and technical risk in founder-friendly language.
---

# Engineering Plan Review

Use this skill before complex implementation, especially when the work involves backend state, auth, payments, AI APIs, uploads, database changes, integrations, background jobs, analytics, or meaningful technical risk.

Read the nearest available `references/gstack-quality-bar.md` for the shared stop/proceed gates.

## Founder Framing

Explain the tool simply:

```text
Wir sind gerade vor dem Bauen. Dafür habe ich einen Engineering-Plan-Review im Arsenal. Der prüft, ob die Idee technisch tragfähig ist, wo Daten fließen, was kaputtgehen kann und welche Tests wir brauchen. Ich brauche dafür noch ein paar Antworten, damit ich nicht rate.
```

## 95% Understanding Gate

Do not approve implementation until these are clear or explicitly assumed:

- core user flow,
- data inputs and outputs,
- where data is stored,
- external services or APIs,
- auth/privacy needs,
- error and empty states,
- performance or cost risks,
- test plan,
- rollback or manual fallback.

Ask missing questions in one concise round. If the founder is non-technical, give examples and defaults.

## Mandatory Diagrams For Complexity

If the work involves data persistence, AI calls, external APIs, auth, payments, uploads, or background jobs, include at least one Mermaid diagram in `docs/sommercamp/engineering-plan.md`:

- sequence diagram for user/API flow,
- state diagram for lifecycle states,
- data-flow diagram for where information moves and persists,
- component diagram for boundaries.

Diagrams are not decoration. They are used to expose hidden assumptions.

## Review Passes

Evaluate:

1. Architecture: simplest viable structure.
2. Data Flow: what is created, read, updated, deleted, and persisted.
3. State Transitions: first-use, success, failure, retry, empty, loading.
4. Failure Modes: API errors, bad input, missing files, slow AI, duplicate actions.
5. Tests: what can be checked automatically and what needs browser/user QA.
6. Privacy/Security: sensitive data, permissions, secrets, user trust.
7. Scope Control: what to cut for the first launch.

## Engineering Scorecard

Rate 0-10:

1. Architecture simplicity.
2. Data-flow clarity.
3. State/error handling.
4. Testability.
5. Privacy/security posture.
6. Cost/performance risk.
7. Week-four feasibility.

Any score below 7 blocks build unless the risk is explicitly accepted. Overall score below 8 should route to more planning or scope cuts.

## Output

Create or update `docs/sommercamp/engineering-plan.md` with:

- Summary
- Architecture
- Data Flow
- Diagram
- State and Error Handling
- Failure Modes
- Tests
- Privacy and Security
- Performance and Cost
- Risks
- Cuts
- Scorecard
- Readiness Dashboard
- Decision Needed

End with:

- `Ready to build`
- `Ready after founder answer`
- `Not ready`

Then ask one clear question or route to `$build-sprint`, `$website-builder`, or `$design-review`.
