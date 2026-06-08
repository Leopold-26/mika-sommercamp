---
name: spec-builder
description: Turn a vague founder request, feature idea, website idea, or app change into a precise Mika spec before design, engineering, build, QA, or shipping work starts.
---

# Spec Builder

Use this skill when the founder asks for a feature, website, app, integration, AI flow, or product change and the request is not yet precise enough to build safely.

## 95% Understanding Gate

Mika should not build from guesses. Before implementation, reach roughly 95% understanding of:

- target user and painful moment,
- desired outcome,
- exact user flow,
- must-have behavior,
- acceptance criteria,
- non-goals and cuts,
- data/content needed,
- distribution or learning goal,
- design references or tone when UI is involved,
- technical constraints and unknowns.

If any of these are missing, say:

```text
Ich kann das bauen, aber ich will nicht raten. Dafür nutze ich jetzt den Spec-Builder: Er macht aus deiner Idee eine klare Bauanleitung. Damit ich bei 95% Verständnis bin, brauche ich noch diese Antworten:
```

Ask 5 to 8 focused questions. If the founder cannot answer, propose a default and mark it as an assumption.

## Output

Create or update `docs/sommercamp/spec.md` with:

- Goal
- User
- Problem Moment
- Scope
- Non-Goals
- User Flow
- Screens or Touchpoints
- Data and Integrations
- Acceptance Criteria
- Open Questions
- Assumptions Mika Made
- Recommended Next Skill

## Routing

After the spec:

- Use `$product-wedge-review` if the scope is still too broad.
- Use `$design-review` if UI, brand, screens, or interaction quality matter.
- Use `$engineering-plan-review` if architecture, state, backend, AI, auth, payments, or integrations matter.
- Use `$website-builder` for a landing page, website, demo, or first web-app MVP.
- Use `$build-sprint` only when the spec is clear enough to implement.

End with one decision question:

```text
Stimmt diese Spezifikation so, oder soll ich eine Annahme ändern, bevor ich den nächsten Review/Build-Schritt starte?
```
