# Mika Sharing

Diese Datei ist für das Gründerszene/Sommercamp-Team.

## Entscheidung

Mika wird öffentlich über GitHub verteilt. Der Hauptweg ist nicht mehr Plugin-Installation, sondern Download ZIP.

```text
https://github.com/Leopold-26/mika-sommercamp
```

## Founder-Flow

Founder sollen diese Schritte befolgen:

1. GitHub-Link öffnen.
2. Auf **Code** klicken.
3. Auf **Download ZIP** klicken.
4. ZIP entpacken.
5. Entpackten Ordner in Codex öffnen.
6. Im neuen Chat schreiben: `Starte Mika.`
7. Vorhandene Unterlagen in den Chat ziehen oder Links schicken.

## Warum das einfacher ist

Der entpackte Ordner enthält bereits:

- `AGENTS.md`
- `.agents/skills/`
- `docs/sommercamp/`
- `START_HERE.md`

Codex kann diese repo-lokalen Skills direkt nutzen, wenn der Ordner geöffnet wird.

## Warum nicht der alte Link?

Der lokale Codex-Link sah ungefähr so aus:

```text
codex://plugins/mika-sommercamp?marketplacePath=/Users/<creator>/...
```

Dieser Link funktioniert nur auf dem Rechner, auf dem diese Datei existiert. Bei anderen Foundern gibt es diesen lokalen Pfad nicht, deshalb zeigt Codex `Failed to load plugin`.

Founder dürfen diesen lokalen Link nicht bekommen.

## Was Founder bekommen

Founder bekommen:

1. den GitHub-Link `https://github.com/Leopold-26/mika-sommercamp`,
2. die kurze Download-ZIP-Anleitung aus [INSTALL_FOR_FOUNDERS.md](INSTALL_FOR_FOUNDERS.md).

Founder müssen nicht verstehen, was ein Plugin, Marketplace oder Skill ist.

## Optionaler Plugin-Weg

Der Plugin-Weg bleibt für technische Nutzer möglich:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex neu starten.

Für Founder ist das nicht der empfohlene Weg.
