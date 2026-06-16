# Program Team Setup

Diese Datei erklärt, wie das Sommercamp-Team Mika an Founder ausliefert.

## Empfohlener Weg: GitHub ZIP

Das ist der Hauptweg für Founder.

Public repo:

```text
https://github.com/Leopold-26/mika-sommercamp
```

Founder machen:

```text
GitHub öffnen -> Code -> Download ZIP -> entpacken -> Ordner in Codex öffnen -> Starte Mika
```

Keine Terminal-Befehle nötig.

## Was an Founder geschickt wird

Sendet:

1. GitHub-Link: `https://github.com/Leopold-26/mika-sommercamp`
2. Kurze Nachricht:

```text
Öffne den GitHub-Link, klicke auf Code -> Download ZIP, entpacke den Ordner, öffne den Ordner in Codex und schreibe im neuen Chat: Starte Mika.
```

Optional:

- [START_HERE.md](START_HERE.md)
- [INSTALL_FOR_FOUNDERS.md](INSTALL_FOR_FOUNDERS.md)
- `dist/mika-sommercamp-starter.zip`

## Warum nicht Plugin-first

Der Plugin-Weg funktioniert technisch, aber er ist für nicht-technische Founder zu fragil:

- Terminal nötig
- Codex CLI muss installiert sein
- zwei Befehle müssen exakt kopiert werden
- Codex muss neu gestartet werden
- Founder müssen verstehen, dass Plugin und Projektordner zwei verschiedene Dinge sind

Deshalb ist der Plugin-Weg nur noch Advanced.

## Nicht verschicken

Keine lokalen Links verschicken:

```text
codex://plugins/mika-sommercamp?marketplacePath=/Users/...
```

Diese Links funktionieren nur auf dem Laptop, auf dem sie erstellt wurden.

## Advanced: Plugin-Weg

Nur für technische Nutzer oder Team-Mitglieder:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex neu starten.

## Updates

Wenn Mika aktualisiert wurde:

1. Änderungen committen und auf `main` pushen.
2. Founder, die den ZIP-Weg nutzen, laden das Repo erneut als ZIP herunter.
3. Founder, die den Plugin-Weg nutzen, führen aus:

```bash
codex plugin marketplace upgrade gruenderszene-sommercamp
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex neu starten.
