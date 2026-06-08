# Mika installieren

Diese Anleitung ist für Founder im Gründerszene Sommercamp. Du brauchst nur drei Dinge:

- Codex auf deinem Laptop
- Terminal
- einen Projektordner für deine App

Du musst keine Skill-Dateien herunterladen oder bearbeiten. Mika richtet die Projektstruktur später selbst ein.

## Schritt 1: GitHub-Link öffnen

Öffne dieses Repo:

```text
https://github.com/Leopold-26/mika-sommercamp
```

Der Link ist öffentlich und kann weitergegeben werden.

## Schritt 2: Terminal öffnen

Öffne die Terminal-App auf deinem Laptop.

Wichtig: Die folgenden Befehle gehören in Terminal, nicht in den Codex-Chat.

## Schritt 3: Mika installieren

Kopiere diese zwei Befehle nacheinander in Terminal und drücke nach jedem Befehl Enter:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Wenn beide Befehle durchgelaufen sind, starte Codex einmal neu.

## Schritt 4: Projektordner erstellen

Erstelle auf deinem Laptop einen neuen Ordner für dein Sommercamp-Projekt.

Beispiel:

```text
mein-sommercamp-projekt
```

Der Ordner darf leer sein.

## Schritt 5: Projektordner in Codex öffnen

Öffne genau diesen Ordner in Codex.

Das ist wichtig, weil Mika später Dateien in diesen Ordner schreibt, zum Beispiel Produktthese, Audit, Distribution-Plan und 10-Wochen-Plan.

## Schritt 6: Mika starten

Starte in Codex einen neuen Chat in deinem Projektordner und schreibe:

```text
Starte Mika.
```

Mika erstellt dann automatisch die Sommercamp-Struktur:

```text
docs/sommercamp/
docs/sommercamp/00_uploads/
docs/sommercamp/founder-profile.md
docs/sommercamp/current-state-audit.md
docs/sommercamp/product-thesis.md
docs/sommercamp/distribution-plan.md
docs/sommercamp/ten-week-plan.md
```

## Schritt 7: Unterlagen an Mika geben

Wenn du schon Materialien hast, ziehe sie direkt in den Mika-Chat oder schicke Links.

Das können sein:

- Pitch Deck
- Notizen
- Screenshots
- Figma-Export
- Prototyp-Link
- Landing-Page-Text
- User Research
- bestehender Code

Mika liest zuerst, was schon da ist. Danach fragt Mika nur nach dem, was wirklich fehlt.

## Was Mika danach macht

Mika führt dich durch diese Reihenfolge:

1. aktuellen Stand prüfen
2. offene Fragen stellen
3. Produktidee und Zielnutzer schärfen
4. Distribution und erste 100 Nutzer prüfen
5. 10-Wochen-Plan mit Launch in Woche 4 erstellen
6. Lücken im Plan mit dir besprechen
7. Sprint 1 starten
8. Website, Landing Page oder App-MVP bauen, wenn der Plan klar genug ist
9. QA, Launch, Retros und Updates begleiten

Mika soll nicht blind bauen. Wenn etwas unklar ist, fragt Mika nach und erklärt dir, welches Tool oder welcher Skill gerade hilft.

## Wenn etwas nicht klappt

Wenn Terminal sagt `codex: command not found`, ist die Codex CLI noch nicht verfügbar. Öffne Codex und installiere die Command-Line-Tools/CLI aus den Codex-Einstellungen. Wenn du die Option nicht findest, melde dich beim Sommercamp-Team.

Wenn Mika nach der Installation nicht sichtbar ist, starte Codex neu und öffne einen neuen Chat in deinem Projektordner.

Wenn du schon viele Unterlagen hast, musst du nicht alles neu erklären. Schicke Mika zuerst die Unterlagen oder Links und schreibe:

```text
Mika, prüfe meinen aktuellen Stand und führe mich danach durch das Onboarding.
```

## Mika später aktualisieren

Wenn das Sommercamp-Team sagt, dass Mika aktualisiert wurde, öffne Terminal und führe aus:

```bash
codex plugin marketplace upgrade gruenderszene-sommercamp
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex neu starten und einen neuen Chat öffnen.
