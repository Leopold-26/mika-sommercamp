---
name: design-review
description: Review or shape the founder's website, landing page, onboarding flow, app screens, visual direction, interaction states, and mobile UX before or after build work.
---

# Design Review

Use this skill when UI quality matters: landing pages, websites, onboarding, consumer app screens, product demos, empty/loading/error states, mobile layout, visual identity, or design references.

Read the nearest available `references/gstack-quality-bar.md` for score interpretation.

## Founder Framing

```text
Wir sind gerade an der Nutzeroberfläche. Dafür habe ich einen Design-Review im Arsenal. Der hilft, bevor wir bauen oder nachdem wir gebaut haben: Was sieht der Nutzer zuerst, was soll er fühlen, welche Zustände fehlen, und wo wirkt es generisch?
```

## 95% Understanding Gate

Before giving final design direction or building, understand:

- first screen goal,
- primary CTA,
- target user emotion,
- design references,
- what should feel premium, fast, playful, editorial, utility, or social,
- mobile needs,
- loading/empty/error/success states,
- what should not be copied or imitated.

Ask 3 to 7 design questions if unclear. Offer defaults for non-designers.

## Review Passes

Rate each 0-10 and explain what a 10 would mean:

1. First-screen clarity.
2. Information hierarchy.
3. CTA and conversion path.
4. Interaction states.
5. Mobile/responsive behavior.
6. Trust and credibility.
7. Visual distinctiveness.
8. AI-slop risk: generic gradients, vague copy, fake testimonials, template feel.

## Design Red Flags

Push back if:

- the first screen says a vague value prop but not the actual user outcome,
- CTA is generic or not tied to the product loop,
- the page could belong to any AI startup,
- mobile layout is untested,
- there are no loading, empty, error, or success states,
- visual references are copied rather than translated,
- screenshots/mockups show atmosphere but not the actual product.

## 10-Star Design Target

For each major weakness, define the 10-star version:

- what the user sees first,
- what they understand in 5 seconds,
- what they want to click,
- what trust or emotion the design creates,
- what feels specific to this product rather than template-like.

If the overall design score is below 8, do not route directly to build unless the founder accepts a rough prototype.

## Output

Create or update `docs/sommercamp/design-review.md` with:

- Current rating
- Scorecard with "what makes it an 8/10"
- Strongest design choice
- Weakest design risk
- Required fixes
- Optional upgrades
- 10-star design target
- Mobile/state checklist
- Founder decisions needed
- Decision state: `Ready`, `Ready after fixes`, `Needs design cut`, or `Not ready`
- Recommended next skill

If the design is ready to build, route to `$website-builder` or `$build-sprint`. If already built, route to `$browser-qa` or `$launch-readiness`.
