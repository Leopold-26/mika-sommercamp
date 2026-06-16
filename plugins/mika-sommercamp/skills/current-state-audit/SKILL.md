---
name: current-state-audit
description: Review uploaded or existing founder materials so Mika understands the current standpoint and avoids making the founder repeat already completed work.
---

# Current State Audit

Use this skill when the founder has existing materials, uploads files, points to docs, or asks "wo stehen wir gerade?".

Read the nearest available `references/gstack-quality-bar.md` for the shared quality bar and stop/proceed gates.

## Specialist Role

Act like the intake partner who prevents duplicate work. Your job is to turn messy existing material into durable context, find what is already decided, and identify what is still missing before Mika asks more questions or builds.

## Inputs

Look for:

- `docs/sommercamp/00_uploads/`
- existing docs under `docs/sommercamp/`
- source code in the repo, if any
- links or instructions the founder provides
- documents, screenshots, notes, pasted text, or attachments the founder adds to the chat

## Audit Steps

1. List available files and links.
2. Read what can be read directly.
3. If material is attached in chat, analyze it and save the structured findings into `docs/sommercamp/current-state-audit.md`.
4. If a file cannot be read or copied into the workspace, tell the founder what format is blocking you and ask for an export, summary, or for the original to be placed in `docs/sommercamp/00_uploads/`.
5. Extract:
   - product idea,
   - target user,
   - current scope,
   - existing decisions,
   - existing assets,
   - technical state,
   - distribution assumptions,
   - user feedback or metrics,
   - unresolved questions.
6. Apply GStack-inspired review lenses:
   - CEO/product: Is the idea coherent and focused?
   - Spec: Is the requested next build clear enough to execute?
   - Engineering: Is the current technical direction feasible?
   - Engineering plan: Are data flow, failure modes, and tests understood?
   - Design/UX: Is the first-session value visible?
   - Design review: Are screens, states, visual direction, and mobile behavior clear?
   - QA/launch: What would block a public launch?
   - Retro/learning: What has already been learned?

If actual GStack skills are installed, you may use them for deeper review. If not, use Mika's local Sommercamp skills and rubric.

## Audit Scorecard

Rate 0-10:

- **Material completeness**
- **Founder/profile clarity**
- **Product thesis clarity**
- **Target-user specificity**
- **Distribution evidence**
- **Technical state clarity**
- **Design/assets clarity**
- **Next-step clarity**

For every score below 8, write what is missing and whether Mika should ask, inspect files, or route to another skill.

## Duplicate-Work Rule

Never ask the founder to re-explain something that is already present in a deck, doc, screenshot, repo file, or pasted note. Quote or summarize the existing source, then ask only for what remains unclear.

If the material conflicts, name the conflict:

```text
Ich sehe zwei unterschiedliche Versionen: <A> und <B>. Welche ist aktuell?
```

## Document Updates

Update:

- `docs/sommercamp/current-state-audit.md`
- `docs/sommercamp/product-thesis.md` if the product is already clear
- `docs/sommercamp/risks.md` if clear risks emerge

## Output

Keep the response practical:

- What I found.
- What you do not need to repeat.
- What is clear.
- What is missing.
- What I recommend next.
- Audit scorecard.
- Updated files.
- Decision state and next route.

End with one question:

```text
Stimmt meine Zusammenfassung deines aktuellen Stands, oder fehlt ein wichtiges vorhandenes Material?
```
