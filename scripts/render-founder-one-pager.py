from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "mika-founder-one-pager.pdf"
AVATAR = ROOT / "plugins" / "mika-sommercamp" / "assets" / "mika-avatar-sticker.png"
REPO_URL = "https://github.com/Leopold-26/mika-sommercamp"

PAGE_W, PAGE_H = A4
M = 38

PURPLE = colors.HexColor("#7A00FF")
PURPLE_DARK = colors.HexColor("#240046")
PURPLE_MID = colors.HexColor("#5F00D9")
BLACK = colors.HexColor("#050505")
WHITE = colors.white
INK = colors.HexColor("#111111")
MUTED = colors.HexColor("#555555")
LINE = colors.HexColor("#E6E6E6")
LIME = colors.HexColor("#D7FF00")
LIGHT = colors.HexColor("#F7F7F7")


def wrap(c: canvas.Canvas, text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        candidate = " ".join([*current, word])
        if c.stringWidth(candidate, font, size) <= width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def draw_wrapped(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    font: str,
    size: float,
    leading: float,
    color=INK,
) -> float:
    c.setFillColor(color)
    c.setFont(font, size)
    for line in wrap(c, text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_gradient(c: canvas.Canvas, x: float, y: float, w: float, h: float) -> None:
    steps = 80
    for i in range(steps):
        t = i / (steps - 1)
        r = PURPLE_DARK.red * (1 - t) + PURPLE.red * t
        g = PURPLE_DARK.green * (1 - t) + PURPLE.green * t
        b = PURPLE_DARK.blue * (1 - t) + PURPLE.blue * t
        c.setFillColor(colors.Color(r, g, b))
        c.rect(x + (w / steps) * i, y, w / steps + 1, h, stroke=0, fill=1)

    c.setStrokeColor(colors.Color(1, 1, 1, alpha=0.14))
    c.setLineWidth(0.6)
    grid = 32
    gx = x
    while gx <= x + w:
        c.line(gx, y, gx, y + h)
        gx += grid
    gy = y
    while gy <= y + h:
        c.line(x, gy, x + w, gy)
        gy += grid


def draw_logo_text(c: canvas.Canvas, text: str, x: float, y: float, size: float) -> None:
    c.setFont("Helvetica-BoldOblique", size)
    c.setFillColor(BLACK)
    c.drawString(x + 3, y - 3, text)
    c.setFillColor(WHITE)
    c.drawString(x, y, text)


def draw_tracked_text(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    font: str,
    size: float,
    tracking: float,
    color,
) -> float:
    c.setFont(font, size)
    c.setFillColor(color)
    cursor = x
    for char in text:
        c.drawString(cursor, y, char)
        cursor += c.stringWidth(char, font, size) + tracking
    return cursor - x


def draw_hero_word(c: canvas.Canvas, text: str, x: float, y: float, size: float, tracking: float) -> None:
    font = "Helvetica-BoldOblique"
    # Layered offsets keep the Gründerszene-style chunky 3D shadow while
    # tracked front letters prevent tight glyphs like M/I from merging.
    for offset in (8, 6, 4, 2):
        draw_tracked_text(c, text, x + offset, y - offset, font, size, tracking, BLACK)
    draw_tracked_text(c, text, x, y, font, size, tracking, WHITE)


def draw_pill(c: canvas.Canvas, text: str, x: float, y: float, w: float, h: float) -> None:
    c.setFillColor(WHITE)
    c.roundRect(x, y, w, h, h / 2, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(x + w / 2, y + h / 2 - 3, text)


def draw_footer(c: canvas.Canvas, page_label: str) -> None:
    c.setFillColor(PURPLE_MID)
    c.rect(0, 0, PAGE_W, 42, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(M, 17, "Build fast. Launch early. Distribution first.")
    c.drawRightString(PAGE_W - M, 17, page_label)


def draw_command_box(c: canvas.Canvas, lines: list[str], x: float, y: float, w: float, h: float) -> None:
    c.setFillColor(BLACK)
    c.roundRect(x, y - h, w, h, 10, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Courier-Bold", 8.8)
    ty = y - 18
    for line in lines:
        c.drawString(x + 14, ty, line)
        ty -= 13


def draw_detail_step(c: canvas.Canvas, n: int, title: str, body: str, x: float, y: float, w: float) -> float:
    c.setFillColor(LIME)
    c.circle(x + 13, y - 12, 11, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x + 13, y - 16, str(n))
    c.setFont("Helvetica-Bold", 11)
    c.drawString(x + 32, y - 10, title)
    return draw_wrapped(c, body, x + 32, y - 25, w - 32, "Helvetica", 8.7, 10.6, MUTED) - 8


def draw_speech_bubble(
    c: canvas.Canvas,
    x: float,
    y: float,
    w: float,
    h: float,
    tail_x: float,
    tail_y: float,
    body: str,
) -> None:
    c.setFillColor(colors.Color(0, 0, 0, alpha=0.22))
    tail_shadow = c.beginPath()
    tail_shadow.moveTo(x + 22 + 4, y + 12 - 4)
    tail_shadow.lineTo(tail_x + 4, tail_y - 4)
    tail_shadow.lineTo(x + 42 + 4, y + 9 - 4)
    tail_shadow.close()
    c.drawPath(tail_shadow, stroke=0, fill=1)
    c.roundRect(x + 4, y - 4, w, h, 15, stroke=0, fill=1)

    c.setFillColor(WHITE)
    c.setStrokeColor(BLACK)
    c.setLineWidth(1.4)
    tail = c.beginPath()
    tail.moveTo(x + 22, y + 12)
    tail.lineTo(tail_x, tail_y)
    tail.lineTo(x + 42, y + 9)
    tail.close()
    c.drawPath(tail, stroke=1, fill=1)
    c.roundRect(x, y, w, h, 15, stroke=1, fill=1)

    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(x + 15, y + h - 18, "Hey, ich bin Mika.")
    draw_wrapped(c, body, x + 15, y + h - 32, w - 30, "Helvetica-Bold", 8.1, 9.7, MUTED)


def draw_mika_host(c: canvas.Canvas, avatar_x: float, avatar_y: float, avatar_size: float) -> None:
    if AVATAR.exists():
        c.drawImage(ImageReader(str(AVATAR)), avatar_x, avatar_y, width=avatar_size, height=avatar_size, mask="auto")
    draw_speech_bubble(
        c,
        145,
        PAGE_H - 119,
        290,
        44,
        124,
        PAGE_H - 130,
        "Ich führe dich vom Setup bis zum ersten Launch.",
    )


def draw_step(
    c: canvas.Canvas,
    n: int,
    title: str,
    body: str,
    x: float,
    y: float,
    w: float,
    h: float,
) -> None:
    c.setFillColor(WHITE)
    c.setStrokeColor(BLACK)
    c.setLineWidth(1.6)
    c.rect(x, y - h, w, h, stroke=1, fill=1)
    c.setFillColor(PURPLE)
    c.rect(x, y - h, 9, h, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(x + 17, y - 27, str(n))
    c.setFont("Helvetica-Bold", 9.8)
    c.drawString(x + 17, y - 45, title.upper())
    draw_wrapped(c, body, x + 17, y - 57, w - 28, "Helvetica-Bold", 8.4, 10.0, MUTED)


def draw_section_title(c: canvas.Canvas, title: str, x: float, y: float, w: float) -> None:
    c.setFillColor(BLACK)
    c.rect(x, y - 4, w, 5, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(x, y - 25, title.upper())


def draw_bullets(c: canvas.Canvas, items: list[str], x: float, y: float, width: float) -> float:
    for item in items:
        c.setFillColor(PURPLE)
        c.circle(x + 4, y + 4, 3, stroke=0, fill=1)
        y = draw_wrapped(c, item, x + 15, y, width - 15, "Helvetica-Bold", 9.2, 11.2, INK)
        y -= 7
    return y


def render() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=A4)
    c.setTitle("Mika Sommercamp Founder Setup")

    c.setFillColor(WHITE)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # Header / hero
    hero_h = 245
    draw_gradient(c, 0, PAGE_H - hero_h, PAGE_W, hero_h)
    draw_pill(c, "Setup", M, PAGE_H - 38, 56, 22)
    draw_logo_text(c, "GRÜNDERSZENE", PAGE_W / 2 - 110, PAGE_H - 42, 25)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 10)
    c.drawRightString(PAGE_W - M, PAGE_H - 31, "SOMMERCAMP")

    draw_mika_host(c, -26, PAGE_H - 218, 160)

    title_x = 150
    draw_hero_word(c, "MIKA", title_x, PAGE_H - 164, 46, 3.5)
    draw_hero_word(c, "STARTEN", title_x, PAGE_H - 207, 46, 1.8)

    draw_wrapped(
        c,
        "Dein Codex-Assistent für Onboarding, Website/App-MVP, Distribution, Build-Sprints und Launch.",
        title_x,
        PAGE_H - 230,
        328,
        "Helvetica-Bold",
        10.5,
        12.5,
        WHITE,
    )
    c.setFillColor(LIME)
    pill_w = 118
    pill_x = PAGE_W - M - pill_w
    pill_y = PAGE_H - 198
    c.roundRect(pill_x, pill_y, pill_w, 34, 17, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 10.5)
    c.drawCentredString(pill_x + pill_w / 2, pill_y + 12, "GITHUB-LINK")
    c.linkURL(REPO_URL, (pill_x, pill_y, pill_x + pill_w, pill_y + 34), relative=0)

    # Intro
    y = PAGE_H - hero_h - 26
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 19)
    c.drawString(M, y, "Du brauchst: GitHub-Link, Terminal, Codex.")
    y -= 25
    draw_wrapped(
        c,
        "Mika wird einmal über GitHub installiert. Danach öffnest du deinen eigenen Projektordner in Codex, "
        "schreibst Starte Mika und lässt dich durch Onboarding, Plan, Build und Launch führen.",
        M,
        y,
        PAGE_W - 2 * M,
        "Helvetica-Bold",
        10.5,
        13,
        MUTED,
    )

    # Steps
    y = PAGE_H - hero_h - 82
    gap = 10
    step_w = (PAGE_W - 2 * M - gap) / 2
    step_h = 72
    steps = [
        ("GitHub öffnen", "Öffne github.com/Leopold-26/mika-sommercamp. Der Link ist öffentlich und teilbar."),
        ("Zwei Befehle ausführen", "Kopiere die Installationsbefehle aus INSTALL_FOR_FOUNDERS.md in Terminal."),
        ("Codex neu starten", "Danach Codex einmal schließen und wieder öffnen, damit Mika sichtbar wird."),
        ("Projektchat starten", "Öffne deinen Projektordner in Codex und schreibe: Starte Mika."),
    ]
    for i, (title, body) in enumerate(steps, start=1):
        col = (i - 1) % 2
        row = (i - 1) // 2
        draw_step(c, i, title, body, M + col * (step_w + gap), y - row * (step_h + gap), step_w, step_h)

    # Two columns
    col_top = y - 2 * (step_h + gap) - 20
    left_w = 270
    right_x = M + left_w + 22
    right_w = PAGE_W - M - right_x

    draw_section_title(c, "Mika bringt mit", M, col_top, left_w)
    left_y = col_top - 42
    left_y = draw_bullets(
        c,
        [
            "Alle Mika-Skills kommen aus dem GitHub-Plugin. Du musst keine Skill-Dateien anfassen.",
            "Mika erstellt die Projektdateien in deinem Ordner: Profil, Audit, Produktthese, Spec, Website-Brief, Distribution und 10-Wochen-Plan.",
            "Mika fragt nach, gibt Pushback, erklärt passende Tools und baut erst, wenn Ziel, Nutzer, Scope und Risiko klar genug sind.",
        ],
        M,
        left_y,
        left_w,
    )

    c.setFillColor(PURPLE)
    c.rect(M, left_y - 88, left_w, 72, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(M + 14, left_y - 38, "Erster Prompt")
    c.setFillColor(BLACK)
    c.roundRect(M + 14, left_y - 69, left_w - 28, 25, 12, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Courier-Bold", 12)
    c.drawString(M + 26, left_y - 61, "Starte Mika.")

    draw_section_title(c, "Deine Unterlagen", right_x, col_top, right_w)
    right_y = col_top - 42
    right_y = draw_bullets(
        c,
        [
            "Ziehe Pitch Decks, Notizen, Screenshots, Figma-Exports, Prototyp-Links oder bestehenden Code direkt in den Mika-Chat.",
            "Mika analysiert alles zuerst und schreibt eine strukturierte Zusammenfassung in current-state-audit.md.",
            "Wenn du Dateien dauerhaft speichern willst, lege sie später in docs/sommercamp/00_uploads/ ab.",
        ],
        right_x,
        right_y,
        right_w,
    )

    c.setFillColor(BLACK)
    c.rect(right_x, right_y - 96, right_w, 78, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(right_x + 14, right_y - 34, "Danach führt Mika:")
    draw_wrapped(
        c,
        "Onboarding abschließen, 10-Wochen-Plan bauen, Lücken abfragen, Sprint 1 starten, dann Woche für Woche weiter.",
        right_x + 14,
        right_y - 52,
        right_w - 28,
        "Helvetica-Bold",
        10.5,
        13,
        WHITE,
    )

    draw_footer(c, "GRÜNDERSZENE SOMMERCAMP · 1")

    c.showPage()
    c.setFillColor(WHITE)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    draw_gradient(c, 0, PAGE_H - 92, PAGE_W, 92)
    draw_logo_text(c, "GRÜNDERSZENE", M, PAGE_H - 44, 22)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 21)
    c.drawRightString(PAGE_W - M, PAGE_H - 48, "SETUP")

    y = PAGE_H - 124
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(M, y, "Ganz konkret: so startest du Mika")
    y -= 23
    y = draw_wrapped(
        c,
        "Bitte die Befehle in Terminal kopieren, nicht in den Codex-Chat. Danach arbeitest du wieder nur in Codex.",
        M,
        y,
        PAGE_W - 2 * M,
        "Helvetica-Bold",
        10,
        12.4,
        MUTED,
    )

    full_w = PAGE_W - 2 * M
    col_y = y - 22

    c.setFillColor(LIGHT)
    c.setStrokeColor(LINE)
    c.setLineWidth(1)
    c.roundRect(M, col_y - 86, full_w, 86, 10, stroke=1, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(M + 16, col_y - 23, "1. GitHub-Link öffnen")
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(PURPLE)
    c.drawString(M + 16, col_y - 44, "github.com/Leopold-26/mika-sommercamp")
    c.linkURL(REPO_URL, (M + 16, col_y - 50, M + full_w - 16, col_y - 34), relative=0)
    draw_wrapped(
        c,
        "Im Repo findest du die Founder-Anleitung INSTALL_FOR_FOUNDERS.md. Du musst nichts herunterladen, um Mika als Plugin zu installieren.",
        M + 16,
        col_y - 65,
        full_w - 32,
        "Helvetica",
        8.5,
        10.2,
        MUTED,
    )

    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(M, col_y - 112, "2. Terminal öffnen und diese zwei Befehle nacheinander ausführen")
    draw_command_box(
        c,
        [
            "codex plugin marketplace add Leopold-26/mika-sommercamp --ref main",
            "codex plugin add mika-sommercamp@gruenderszene-sommercamp",
        ],
        M,
        col_y - 128,
        full_w,
        50,
    )
    draw_wrapped(
        c,
        "Danach Codex einmal neu starten. Das ist wichtig, damit das Plugin und alle Mika-Skills geladen werden.",
        M,
        col_y - 190,
        full_w,
        "Helvetica-Bold",
        8.7,
        10.5,
        MUTED,
    )

    y2 = col_y - 225
    y2 = draw_detail_step(c, 3, "Projektordner erstellen", "Erstelle einen neuen Ordner für dein Sommercamp-Projekt. Der Ordner darf komplett leer sein.", M, y2, PAGE_W - 2 * M)
    y2 = draw_detail_step(c, 4, "Ordner in Codex öffnen", "Öffne genau diesen Ordner in Codex und starte dort einen neuen Chat. So kann Mika Dateien in den richtigen Projektordner schreiben.", M, y2, PAGE_W - 2 * M)
    y2 = draw_detail_step(c, 5, "Ersten Prompt senden", "Schreibe im Projektchat nur: Starte Mika. Danach richtet Mika docs/sommercamp/ ein und beginnt mit dem Onboarding.", M, y2, PAGE_W - 2 * M)
    y2 = draw_detail_step(c, 6, "Unterlagen geben", "Ziehe vorhandene Materialien in den Chat oder schicke Links. Mika prüft sie zuerst, damit du nichts doppelt erklären musst.", M, y2, PAGE_W - 2 * M)

    section_y = y2 - 12
    draw_section_title(c, "Wenn etwas nicht klappt", M, section_y, 238)
    draw_bullets(
        c,
        [
            "Terminal sagt codex: command not found: Codex CLI in den Codex-Einstellungen installieren oder beim Team melden.",
            "Mika ist nach dem Install nicht sichtbar: Codex neu starten und einen neuen Chat im Projektordner öffnen.",
        ],
        M,
        section_y - 42,
        PAGE_W - 2 * M,
    )

    c.setFillColor(BLACK)
    c.rect(M, 76, PAGE_W - 2 * M, 82, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(M + 16, 133, "Was Mika danach macht")
    draw_wrapped(
        c,
        "Mika erstellt die Projektdateien, auditiert deinen aktuellen Stand, stellt Onboarding-Fragen, baut einen 10-Wochen-Plan mit Launch in Woche 4 und fragt dich nach Lücken. Danach führt Mika dich Schritt für Schritt durch Sprint 1, Website/App-MVP, QA, Launch und Retros.",
        M + 16,
        114,
        PAGE_W - 2 * M - 32,
        "Helvetica-Bold",
        8.6,
        10.4,
        WHITE,
    )

    draw_footer(c, "GRÜNDERSZENE SOMMERCAMP · 2")

    c.save()
    print(OUT)


if __name__ == "__main__":
    render()
