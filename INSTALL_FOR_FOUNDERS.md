# Mika installieren

Diese Anleitung ist für Founder. Du brauchst nur Codex, Terminal und einen Projektordner.

## 1. Mika zu Codex hinzufügen

Öffne Terminal auf deinem Laptop und kopiere diese zwei Befehle nacheinander hinein:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex einmal neu starten.

Wenn Terminal sagt `codex: command not found`, ist die Codex CLI auf deinem Laptop noch nicht verfügbar. Öffne Codex, installiere die Command-Line-Tools/CLI aus den Codex-Einstellungen oder melde dich beim Sommercamp-Team.

## 2. Projektordner erstellen

Erstelle auf deinem Laptop einen neuen Ordner für dein Sommercamp-Projekt.

Beispiel:

```text
mein-sommercamp-projekt
```

Öffne genau diesen Ordner in Codex. Der Ordner darf leer sein.

## 3. Mika starten

Starte in Codex einen neuen Chat in diesem Projektordner und schreibe:

```text
Starte Mika.
```

Mika erstellt dann automatisch die Sommercamp-Dateien in deinem Ordner und beginnt mit dem Onboarding.

## 4. Unterlagen geben

Ziehe vorhandene Unterlagen direkt in den Mika-Chat oder lege sie später hier ab:

```text
docs/sommercamp/00_uploads/
```

Das können Pitch Decks, Notizen, Screenshots, Figma-Exports, Prototyp-Links, Landing-Page-Texte, User Research oder bestehender Code sein.

Mika prüft zuerst, was schon da ist, und fragt danach nur, was wirklich fehlt.

## Update später

Wenn das Sommercamp-Team sagt, dass Mika aktualisiert wurde, öffne Terminal und führe aus:

```bash
codex plugin marketplace upgrade gruenderszene-sommercamp
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex neu starten und einen neuen Chat öffnen.
