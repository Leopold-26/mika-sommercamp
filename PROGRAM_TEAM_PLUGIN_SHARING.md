# Mika Plugin Sharing

Diese Datei ist für das Gründerszene/Sommercamp-Team.

## Entscheidung

Mika wird als öffentliches GitHub-Marketplace-Repo verteilt.

```text
https://github.com/Leopold-26/mika-sommercamp
```

Das ist der richtige Weg, wenn eine Person den Link an eine andere Person weitergeben können soll.

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
2. den Founder-Setup-PDF `dist/mika-founder-one-pager.pdf`,
3. die Anleitung [INSTALL_FOR_FOUNDERS.md](INSTALL_FOR_FOUNDERS.md).

Founder müssen nicht verstehen, was ein Plugin, Marketplace oder Skill ist. Sie öffnen den GitHub-Link, kopieren zwei Befehle in Terminal, starten Codex neu und schreiben im eigenen Projektordner `Starte Mika.`

## Founder-Installation

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach:

1. Codex neu starten.
2. Projektordner öffnen.
3. Neuen Chat starten.
4. `Starte Mika.` schreiben.

## Weitergeben

Weil das Repo öffentlich ist, kann jede Person denselben GitHub-Link weitergeben.

Kein Workspace-Share-Button ist nötig.

## Updates

Wenn das Team Mika aktualisiert:

1. Änderungen committen und auf `main` pushen.
2. Foundern diese Befehle schicken:

   ```bash
   codex plugin marketplace upgrade gruenderszene-sommercamp
   codex plugin add mika-sommercamp@gruenderszene-sommercamp
   ```

3. Founder starten Codex neu und öffnen einen neuen Chat.

## Fallback

Falls die Codex CLI bei einem Founder nicht verfügbar ist:

1. Founder öffnet Codex und installiert die CLI/Command-Line-Tools aus den Einstellungen.
2. Wenn das nicht klappt, Founder lädt das GitHub-Repo als ZIP herunter.
3. Founder öffnet den entpackten Ordner in Codex.
4. Founder schreibt `Starte Mika.`
