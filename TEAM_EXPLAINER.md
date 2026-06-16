# Mika Sommercamp: Team-Erklärung

## Wofür Mika da ist

Mika ist der Codex-Assistent für das Gründerszene Sommercamp. Mika hilft Foundern, aus einer Consumer-App-Idee einen klaren Arbeitsmodus zu machen: erst aktuellen Stand verstehen, dann Onboarding, Produktthese, Distribution, Spec, Design-/Engineering-Review, 10-Wochen-Plan, Website/App-MVP, Code-Review, Browser-QA, Release, Retros und Editorial Updates.

Mika ist bewusst nicht nur Coding-Assistent. Mika soll coachen, nachfragen, Pushback geben, Founder auf Distribution und Launch fokussieren und dann mit Codex bauen. Zentrale Regel: Mika soll vor dem Bauen ungefähr 95% Verständnis erreichen. Wenn Kontext fehlt, erklärt Mika das passende Werkzeug und fragt nach, statt zu raten.

## Founder-Flow

1. Founder öffnet das öffentliche GitHub-Repo.
2. Founder klickt auf **Code** und **Download ZIP**.
3. Founder entpackt die ZIP-Datei.
4. Founder öffnet den entpackten Ordner in Codex.
5. Founder schreibt `Starte Mika.`
6. Mika nutzt die repo-lokalen Anweisungen und Skills aus `.agents/skills`.
7. Mika prüft vorhandene Unterlagen, Links, Screenshots, Figma-Exports oder Code.
8. Mika führt das Onboarding durch und fragt nur nach fehlendem Kontext.
9. Mika erstellt Produktthese, Distribution-Plan, Risiken, Spec, Engineering-Plan, Design-Review, Website-Brief und 10-Wochen-Plan.
10. Mika bespricht den Plan, fragt nach Lücken und startet dann Sprint 1.

## Skills im Mika-Ordner

- `mika-start`: Startet oder resumed Mika und routet in den passenden nächsten Skill.
- `mika-project-setup`: Erstellt AGENTS.md, Starter-Dateien und `docs/sommercamp/*`, wenn der Projektordner leer ist.
- `current-state-audit`: Liest vorhandene Unterlagen, fasst den aktuellen Stand zusammen und verhindert doppelte Arbeit.
- `founder-onboarding`: Interviewt den Founder zu Person, Idee, Skill-Gaps, Zielnutzer, Distribution und Coaching-Stil.
- `spec-builder`: Macht aus vagen Feature-, Website- oder App-Wünschen eine klare Spezifikation.
- `product-wedge-review`: Schneidet breite Ideen auf den kleinsten launchbaren Consumer-Wedge herunter.
- `distribution-review`: Prüft erste 100 Nutzer, Kanäle, Activation, Retention, Shareability und Gründerszene-Story.
- `ten-week-plan`: Baut oder aktualisiert den 10-Wochen-Plan mit Launch in Woche 4.
- `engineering-plan-review`: Prüft Architektur, Datenfluss, Failure Modes, Tests, Datenschutz und technische Risiken.
- `design-review`: Prüft First Screen, CTA, UI-Zustände, Mobile, visuelle Richtung und AI-Slop-Risiko.
- `website-builder`: Fragt Produkt- und Designfragen und baut Landing Page, Website, Demo oder Web-App-MVP.
- `build-sprint`: Setzt den nächsten kleinen Build-Schritt um, prüft ihn und loggt die Änderung.
- `code-review`: Prüft Code auf Bugs, Regressionen, fehlende Tests, Privacy-Risiken und unvollständige Umsetzung.
- `browser-qa`: Testet lokale oder deployte App-Flows im Browser und dokumentiert sichtbare Bugs.
- `launch-readiness`: Prüft UX, QA, Analytics, Datenschutz, Landing Page, Distribution Assets und Rollback.
- `ship-release`: Prüft letzte Release-Schritte, Tests, QA-Status, Risiken, Rollback und Launch-Kommunikation.
- `growth-retro`: Führt wöchentliche Retros zu shipped work, Nutzern, Metriken, Blockern und nächster Entscheidung.
- `drift-check`: Bringt Founder zurück auf den Wochenfokus, wenn sie überbauen, abdriften oder Distribution vermeiden.
- `editorial-brief`: Erstellt interne oder öffentliche Gründerszene-Updates aus Fortschritt, Learnings und Metriken.

## Auslieferung

Für Founder soll es so einfach wie möglich sein:

1. GitHub-Link per Mail, Slack oder Notion schicken: `https://github.com/Leopold-26/mika-sommercamp`
2. Founder-PDF oder `INSTALL_FOR_FOUNDERS.md` mitschicken.
3. Founder lädt das Repo als ZIP herunter und entpackt es.
4. Founder öffnet den entpackten Ordner in Codex und schreibt `Starte Mika.`
5. Vorhandene Unterlagen können direkt in den Chat gezogen werden.

Der Plugin-Weg bleibt nur für technische Nutzer oder Team-Mitglieder relevant.

## Team-Hinweise

- Der Link bleibt gleich, solange das GitHub-Repo öffentlich bleibt.
- Nach Skill- oder Icon-Änderungen Plugin-Version mit Cachebuster aktualisieren, committen und auf `main` pushen.
- Nicht versprechen, dass Mika beliebig große Apps komplett ohne Entscheidungen baut.
- Das Versprechen ist: Mika baut den kleinsten launchbaren nächsten Schritt und führt Founder mit Fragen, Pushback und klaren Defaults.
