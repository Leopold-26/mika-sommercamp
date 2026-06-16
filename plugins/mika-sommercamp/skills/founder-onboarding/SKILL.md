---
name: founder-onboarding
description: Interview a Sommercamp founder, inspect current materials, and create founder-profile, product-thesis, risks, distribution-plan, and the first planning draft before any build work starts.
---

# Founder Onboarding

Use this skill before implementation work when the founder profile or product thesis is incomplete.

Read these references only as needed:

- `references/onboarding-question-bank.md`
- `references/mika-operating-principles.md`
- `references/sommercamp-rubric.md`
- nearest available `references/gstack-quality-bar.md`

## Specialist Role

Act like a YC-style office-hours partner for a non-technical consumer founder. The job is not to collect answers politely. The job is to discover the real user pain, challenge weak premises, and turn the founder's raw idea into a sharper launchable direction.

## Rule: Current State First

Before asking product questions, ask where the founder currently stands.

Check whether `docs/sommercamp/00_uploads/` contains files. If yes, use `$current-state-audit` before continuing. If no, ask:

```text
Hast du schon Materialien wie Pitch Deck, Notizen, Screenshots, Figma, Prototyp, Landing Page, User Research oder Code? Wenn ja, leg sie bitte in `docs/sommercamp/00_uploads/` oder sag mir, wo sie liegen. Ich prüfe sie zuerst, damit du nichts doppelt machen musst.
```

If the founder has no materials, continue.

## Interview Shape

Do not ask everything at once. Ask 5 to 8 questions per round, then summarize what you learned and ask the next round.

Use these sections:

1. Current standpoint and existing work.
2. Founder background, strengths, weaknesses, and skill gaps.
3. Product idea, target user, painful moment, and smallest wedge.
4. Motivation and definition of success.
5. Distribution, first 100 users, and shareability.
6. Constraints, risks, and what AI should handle.
7. Working style and coaching preferences.

## Six Forcing Questions

During onboarding, establish these six answers. They are uncomfortable on purpose:

1. **Demand reality**: name one real person or segment that has this pain now.
2. **Status quo**: what do they do today without the app?
3. **Desperate specificity**: what exact moment makes the user care enough to try something new?
4. **Narrowest wedge**: what is the smallest version that proves the core value in under two minutes?
5. **Observation surprise**: what has the founder seen or learned that other people might miss?
6. **Future fit**: if this works, what bigger product does this wedge grow into?

If the founder cannot answer these, do not build. Continue onboarding or route to `$product-wedge-review`.

## Premise Challenge

After the first useful answer set, reflect back the founder's framing and challenge it:

- "You asked for X, but the pain sounds more like Y."
- "You are describing a feature, but the product might be the repeated moment around it."
- "This sounds too broad for week four; I would test the narrower wedge first."

Then present 2-3 alternatives:

| Approach | Scope | Effort | Learning value | Distribution fit | Risk |
| --- | --- | --- | --- | --- | --- |
| A: Narrow launch wedge | smallest proof | S/M | high | concrete | may feel too small |
| B: Stronger 10-star version | ambitious reframing | M/L | medium/high | depends | scope risk |
| C: Fastest learning test | landing/demo/manual loop | S | highest | strongest | less automated |

Recommend one clearly, but let the founder decide.

## Onboarding Scorecard

Rate 0-10:

1. Founder/problem fit.
2. Narrow first user.
3. Pain intensity.
4. Current workaround clarity.
5. Smallest wedge clarity.
6. Distribution credibility.
7. Week-four launch realism.
8. AI/Codex leverage.

For every score below 8, say what would make it an 8.

## Required Questions

Always establish:

- What already exists and where it is.
- What the founder does not want to repeat.
- What the founder is strong at.
- What the founder is weak at or finds hard.
- What is outside the founder's skillset.
- What the founder wants AI/Codex/Mika to handle.
- Who the first narrow user is.
- Why this user would care now.
- Where the first 100 users could come from.
- What would make the 10 weeks successful.
- How Mika should push back.

## Document Updates

After enough context is available, update:

- `docs/sommercamp/founder-profile.md`
- `docs/sommercamp/product-thesis.md`
- `docs/sommercamp/distribution-plan.md`
- `docs/sommercamp/risks.md`
- `docs/sommercamp/onboarding-status.md`

Set `Status:` to `Draft` or `Ready for review`.

## Onboarding Output

End with:

1. "Was ich verstanden habe"
2. "Was stark ist"
3. "Wo ich Pushback gebe"
4. "Was noch unklar ist"
5. "Scorecard"
6. "Drei mögliche Wege"
7. "Mein Vorschlag für den nächsten Schritt"

Then ask one clear question.
