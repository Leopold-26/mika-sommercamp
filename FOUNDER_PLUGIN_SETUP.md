# Mika Setup für Founder

Das ist die Kurzfassung. Die ausführlichere Anleitung steht in [INSTALL_FOR_FOUNDERS.md](INSTALL_FOR_FOUNDERS.md).

## 1. GitHub-Link öffnen

```text
https://github.com/Leopold-26/mika-sommercamp
```

## 2. Terminal öffnen

Die Befehle gehören in Terminal, nicht in den Codex-Chat.

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex neu starten.

## 3. Eigenen Projektordner öffnen

Erstelle einen Ordner für dein Sommercamp-Projekt und öffne genau diesen Ordner in Codex. Der Ordner darf leer sein.

## 4. Mika starten

Starte im Projektordner einen neuen Codex-Chat und schreibe:

```text
Starte Mika.
```

Mika legt danach automatisch `docs/sommercamp/` an und führt dich durch Onboarding, aktuellen Stand, Produktthese, Distribution, 10-Wochen-Plan und den ersten Build-Sprint.

## 5. Unterlagen geben

Ziehe vorhandene Unterlagen direkt in den Mika-Chat oder schicke Links:

- Pitch Decks
- Notizen
- Screenshots
- Figma-Exports
- Prototyp-Links
- Landing-Page-Texte
- User Research
- bestehender Code

Mika analysiert zuerst, was schon da ist, und fragt danach nur nach fehlenden Informationen.

## Wenn etwas nicht klappt

Wenn Terminal sagt `codex: command not found`, installiere die Codex CLI aus den Codex-Einstellungen oder melde dich beim Sommercamp-Team.

Wenn Mika nach der Installation nicht auftaucht, starte Codex neu und öffne einen neuen Chat im Projektordner.
