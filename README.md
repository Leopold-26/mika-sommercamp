# Mika Sommercamp

Mika ist der Codex-Assistent für das Gründerszene Sommercamp. Mika hilft Foundern beim Onboarding, prüft vorhandene Unterlagen, stellt Rückfragen, gibt Pushback, baut einen 10-Wochen-Plan und begleitet Website, App-MVP, QA, Launch und Retros.

## Einfachster Start

Du musst kein Plugin installieren und keine Terminal-Befehle ausführen.

1. Klicke oben rechts auf GitHub auf den grünen Button **Code**.
2. Klicke auf **Download ZIP**.
3. Entpacke die ZIP-Datei auf deinem Laptop.
4. Öffne den entpackten Ordner in Codex.
5. Starte in diesem Ordner einen neuen Chat.
6. Schreibe:

```text
Starte Mika.
```

Fertig. Mika liest dann die Projektanweisungen und Skills aus diesem Ordner.

## Warum das funktioniert

Der Ordner enthält alles, was Codex braucht:

- `AGENTS.md` mit Mikas Grundverhalten
- `.agents/skills/` mit den Mika-Skills
- `docs/sommercamp/` für Founder-Profil, Audit, Produktthese, Distribution und 10-Wochen-Plan
- `START_HERE.md` als einfache Anleitung

Codex erkennt Skills aus `.agents/skills`, wenn du genau diesen Ordner in Codex öffnest.

## Was du danach machst

Wenn Mika gestartet ist, gib ihr vorhandene Unterlagen direkt im Chat:

- Pitch Decks
- Notizen
- Screenshots
- Figma-Exports
- Prototyp-Links
- Landing-Page-Texte
- User Research
- bestehender Code

Mika prüft zuerst, was schon da ist. Danach fragt Mika nur nach dem, was wirklich fehlt.

## Was Mika dann macht

Mika führt dich durch diese Reihenfolge:

1. aktuellen Stand prüfen
2. Founder-Onboarding durchführen
3. Produktthese und Zielnutzer schärfen
4. Distribution und erste 100 Nutzer prüfen
5. 10-Wochen-Plan mit Launch in Woche 4 erstellen
6. Lücken mit dir besprechen
7. Sprint 1 starten
8. Website, Landing Page oder App-MVP bauen, wenn der Plan klar genug ist
9. QA, Launch, Retros und Updates begleiten

Mika soll nicht blind bauen. Wenn etwas unklar ist, fragt Mika nach und erklärt dir, welches Tool oder welcher Skill gerade hilft.

## GStack-Tiefe, aber für Sommercamp

Mika ist nicht nur eine leere Hülle mit ein paar Prompts. Die Skills sind als GStack-inspirierter Operating-Mode gebaut:

- Spezialistenrollen für Produkt, Distribution, Spec, Engineering, Design, Build, Code Review, Browser-QA, Launch, Release und Retro
- 95%-Verständnis-Regel vor Build, Review, QA oder Launch
- 0-10-Scorecards für Produkt, Distribution, Spec, Design, Engineering, Build, QA und Launch
- Stop/Proceed-Gates, damit Mika nicht blind baut
- konkrete Alternativen, wenn der aktuelle Weg zu breit oder riskant ist
- dauerhafte Arbeitsdokumente in `docs/sommercamp/`

Der Unterschied zu GStack ist der Fokus: Mika ist stärker auf nicht-technische Founder, Sommercamp-Zeitplan, Woche-4-Launch und Distribution-first Coaching angepasst.

## Für bestehende Projekte

Wenn du schon einen eigenen App-Ordner hast, nimm trotzdem zuerst den einfachen Weg:

1. Lade diesen Mika-Ordner herunter.
2. Öffne ihn in Codex.
3. Starte Mika.
4. Ziehe deine vorhandenen Unterlagen, Links oder Dateien in den Mika-Chat.

Mika kann dir danach helfen, bestehende Dateien zu prüfen oder den nächsten Build-Schritt sauber zu planen.

## Advanced: Plugin installieren

Nur wenn du Mika als wiederverwendbares Codex-Plugin installieren willst, nutze diesen Weg:

```bash
codex plugin marketplace add Leopold-26/mika-sommercamp --ref main
codex plugin add mika-sommercamp@gruenderszene-sommercamp
```

Danach Codex neu starten, einen Projektordner öffnen und `Starte Mika.` schreiben.

Dieser Plugin-Weg ist optional. Für Founder ist **Download ZIP** der empfohlene Weg.

## Team-Unterlagen

- [START_HERE.md](START_HERE.md) - einfache Founder-Anleitung
- [FOUNDER_PLUGIN_SETUP.md](FOUNDER_PLUGIN_SETUP.md) - Setup-Kurzfassung
- [TEAM_SETUP.md](TEAM_SETUP.md) - interne Team-Auslieferung
- `dist/mika-sommercamp-starter.zip` - fertiges Starter-Paket
- `dist/mika-sommercamp-plugin.zip` - Plugin-Paket für Advanced Setup
