---
name: website-builder
description: Guide a non-technical Sommercamp founder from product and design questions to a simple launchable website, landing page, clickable prototype, or first web-app MVP, then implement and visually verify it.
---

# Website Builder

Use this skill when the founder asks Mika to build a website, landing page, waitlist page, product demo, clickable prototype, frontend, or first web-app MVP.

## Gate

Before building, check:

- `docs/sommercamp/current-state-audit.md`
- `docs/sommercamp/product-thesis.md`
- `docs/sommercamp/distribution-plan.md`
- `docs/sommercamp/ten-week-plan.md`
- existing files in the project folder

If the founder has not completed basic onboarding, route to `$mika-start` or `$founder-onboarding` first. Do not make them answer design questions before you understand the user, painful moment, wedge, and distribution path.

If the founder has existing copy, brand assets, screenshots, Figma exports, product sketches, competitor links, or a previous landing page, inspect those before asking questions.

If the requested website/app is vague, route to `$spec-builder` before building. If the visual direction or interaction states are weak, route to `$design-review`. If the app needs backend, auth, database, AI APIs, payments, uploads, or integrations, route to `$engineering-plan-review`.

## Founder-Friendly Intake

Ask only what is needed to build the next launchable version. Prefer 5 to 8 questions in one round. If the founder says "du entscheidest" or gives weak answers, choose sensible defaults and state the assumptions.

Always establish:

1. What should be built now: landing page, waitlist, product website, clickable demo, or usable MVP.
2. The one target user and the painful moment.
3. The primary action: join waitlist, try demo, create account, upload something, share, pay, or book.
4. The 3 to 5 must-have screens or sections.
5. What content already exists and what Mika should write.
6. Design direction: clean/editorial, playful, premium, utility, social, or experimental.
7. Visual references: websites, apps, screenshots, colors, typography, or brands the founder likes or dislikes.
8. Technical constraints: existing stack, deployment target, analytics, auth, payments, database, or no backend yet.

Push back if the requested website is too generic, too much like a pitch deck, or hides the actual product loop. A Sommercamp website should help launch, learn, or acquire users.

## Scope Rules

Default to the simplest useful build:

- For a landing page or waitlist, prefer static HTML/CSS/JS or the existing app framework.
- For an interactive consumer MVP, prefer the existing framework. If the folder is empty, choose a simple Vite/React app unless a plain static build is enough.
- Add auth, payments, database, AI APIs, or complex backend only when needed for the first real user test.
- Build mobile-first and responsive.
- Make the first screen explain the product clearly.
- Include the primary CTA above the fold.
- Add only analytics hooks or event stubs if real analytics setup would slow the sprint.

Do not build:

- dashboards before users exist,
- admin panels unless required to operate the test,
- broad platform features,
- design systems larger than the MVP,
- fake functionality that looks real but cannot be tested.

## Build Flow

1. Summarize the requested output in plain language.
2. Ask the missing intake questions or state assumptions.
3. Create or update `docs/sommercamp/website-brief.md` with:
   - goal,
   - audience,
   - page/app structure,
   - design direction,
   - copy decisions,
   - technical approach,
   - what is deliberately cut.
4. Explain the build plan simply: fastest now, cleanest later, and main risk.
5. Implement the website or web-app MVP.
6. Run available checks.
7. Use `$code-review` for meaningful code changes.
8. If a local website/app exists, start the dev server when practical and use `$browser-qa`.
9. Fix visible layout issues: overlap, clipping, weak mobile layout, unreadable contrast, broken CTA, or blank screens.
10. Update `docs/sommercamp/build-log.md`.

## Design Guidance

Make design questions concrete for non-designers:

- "Soll es eher wie ein klares Magazin, eine moderne Consumer-App oder ein mutiges Kampagnenmotiv wirken?"
- "Welche 2 Websites oder Apps gefallen dir visuell?"
- "Welche Farbe oder Stimmung soll es auf keinen Fall haben?"
- "Soll der erste Screen eher Vertrauen, Neugier, Geschwindigkeit oder Status auslösen?"

If they do not know, pick a direction that matches the user and distribution path. Explain the choice briefly.

## Output

End with:

- what was built,
- where the main files are,
- how it was checked,
- what is still fake or risky,
- the next user/distribution test,
- one clear question about changes or launch.
