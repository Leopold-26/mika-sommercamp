# Mika Delivery Plan

## Ziel

Founder sollen Mika ohne Terminal, ohne Plugin-Verständnis und ohne lokale `codex://`-Links starten können.

## Hauptweg

```text
GitHub-Link öffnen -> Code -> Download ZIP -> entpacken -> Ordner in Codex öffnen -> Starte Mika
```

GitHub-Link:

```text
https://github.com/Leopold-26/mika-sommercamp
```

## Warum dieser Weg

Der heruntergeladene Ordner enthält bereits alles, was Codex braucht:

- `AGENTS.md`
- `.agents/skills/`
- `docs/sommercamp/`
- `START_HERE.md`

Codex erkennt repo-lokale Skills aus `.agents/skills`, wenn der Founder den ganzen Ordner in Codex öffnet. Deshalb muss der Founder Mika nicht als Plugin installieren.

## Founder-Kurzversion

```text
1. Öffne https://github.com/Leopold-26/mika-sommercamp
2. Klicke auf Code.
3. Klicke auf Download ZIP.
4. Entpacke die ZIP.
5. Öffne den entpackten Ordner in Codex.
6. Schreibe: Starte Mika.
7. Ziehe vorhandene Unterlagen in den Mika-Chat.
```

## Advanced-Weg

Das Plugin bleibt im Repo, aber es ist nicht der Hauptweg für Founder.

Plugin-Befehle nur für technische Nutzer:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex neu starten.

## Nicht mehr verwenden

Keine lokalen Links verschicken wie:

```text
codex://plugins/mika-sommercamp?marketplacePath=/Users/...
```

Diese Links funktionieren nur auf dem ursprünglichen Laptop.
