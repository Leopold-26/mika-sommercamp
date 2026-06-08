# Mika Delivery Plan

## Ziel

Founder sollen Mika mit möglichst wenig Setup nutzen können, und der Link soll weiterleitbar sein.

Der alte lokale `codex://...marketplacePath=/Users/...` Link ist dafür falsch, weil er nur auf dem Ersteller-Laptop funktioniert.

## Hauptweg

```text
GitHub-Link öffnen -> zwei Codex-Befehle ausführen -> Codex neu starten -> Projektordner öffnen -> Starte Mika
```

GitHub-Link:

```text
https://github.com/Leopold-26/mika-sommercamp
```

Founder-Befehle:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

## Warum GitHub

Ein öffentliches GitHub-Repo kann jede Person weitergeben. Es hängt nicht an deinem lokalen Mac, nicht an einem Workspace-Share-Button und nicht an individuellen Freigaben.

## Was das Plugin enthält

Das Plugin enthält alles, was wiederverwendbar ist:

- Mika-Skills
- Onboarding-Logik
- Current-State-Audit
- Produkt- und Distribution-Reviews
- Spec-, Design-, Engineering- und Code-Reviews
- Website- und Web-App-MVP-Building
- Browser-QA
- Launch- und Release-Checks
- Drift-Check
- Retros
- Editorial-Briefing
- Templates für die Projektdateien

Das Plugin enthält nicht die individuellen Founder-Unterlagen. Diese entstehen im jeweiligen Projektordner des Founders.

## Founder-Kurzversion

```text
1. Öffne https://github.com/Leopold-26/mika-sommercamp
2. Kopiere die zwei Installationsbefehle aus INSTALL_FOR_FOUNDERS.md in Terminal.
3. Starte Codex neu.
4. Erstelle oder öffne deinen Projektordner.
5. Schreibe: Starte Mika.
6. Ziehe vorhandene Unterlagen in den Mika-Chat.
```

## Updates

Wenn Mika aktualisiert wurde:

```bash
codex plugin marketplace upgrade gruenderszene-sommercamp
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex neu starten und einen neuen Chat öffnen.
