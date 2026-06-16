from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "mika-team-explainer.pdf"
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
LIME = colors.HexColor("#D7FF00")
LIGHT = colors.HexColor("#F7F7F7")
LINE = colors.HexColor("#DDDDDD")


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
    font: str = "Helvetica",
    size: float = 9,
    leading: float = 11,
    color=INK,
) -> float:
    c.setFillColor(color)
    c.setFont(font, size)
    for line in wrap(c, text, font, size, width):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_gradient(c: canvas.Canvas, x: float, y: float, w: float, h: float) -> None:
    steps = 90
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
) -> None:
    c.setFont(font, size)
    c.setFillColor(color)
    cursor = x
    for char in text:
        c.drawString(cursor, y, char)
        cursor += c.stringWidth(char, font, size) + tracking


def draw_hero_word(c: canvas.Canvas, text: str, x: float, y: float, size: float, tracking: float) -> None:
    font = "Helvetica-BoldOblique"
    for offset in (7, 5, 3):
        draw_tracked_text(c, text, x + offset, y - offset, font, size, tracking, BLACK)
    draw_tracked_text(c, text, x, y, font, size, tracking, WHITE)


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
        150,
        PAGE_H - 119,
        304,
        44,
        124,
        PAGE_H - 130,
        "Ich führe Founder mit Fragen, Pushback und Skills.",
    )


def footer(c: canvas.Canvas, page: int) -> None:
    c.setFillColor(PURPLE_MID)
    c.rect(0, 0, PAGE_W, 36, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 9.5)
    c.drawString(M, 15, "Build fast. Launch early. Distribution first.")
    c.drawRightString(PAGE_W - M, 15, f"MIKA TEAM BRIEF · {page}")


def section_title(c: canvas.Canvas, title: str, x: float, y: float, w: float) -> None:
    c.setFillColor(BLACK)
    c.rect(x, y, w, 5, stroke=0, fill=1)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(x, y - 24, title.upper())


def bullet_list(c: canvas.Canvas, items: list[str], x: float, y: float, w: float, size: float = 8.8) -> float:
    for item in items:
        c.setFillColor(PURPLE)
        c.circle(x + 4, y + 4, 3, stroke=0, fill=1)
        y = draw_wrapped(c, item, x + 15, y, w - 15, "Helvetica-Bold", size, size + 2.2, INK)
        y -= 7
    return y


def card(c: canvas.Canvas, x: float, y: float, w: float, h: float, title: str, body: str) -> None:
    c.setFillColor(WHITE)
    c.setStrokeColor(BLACK)
    c.setLineWidth(1.3)
    c.rect(x, y - h, w, h, stroke=1, fill=1)
    c.setFillColor(PURPLE)
    c.rect(x, y - h, 8, h, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 8.8)
    c.drawString(x + 16, y - 19, title)
    draw_wrapped(c, body, x + 16, y - 33, w - 26, "Helvetica", 6.4, 7.8, MUTED)


def command_box(c: canvas.Canvas, x: float, y: float, w: float, h: float, lines: list[str]) -> None:
    c.setFillColor(BLACK)
    c.roundRect(x, y - h, w, h, 9, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Courier-Bold", 8.2)
    ty = y - 17
    for line in lines:
        c.drawString(x + 13, ty, line)
        ty -= 12


def step_card(c: canvas.Canvas, n: int, title: str, body: str, x: float, y: float, w: float, h: float) -> None:
    c.setFillColor(LIGHT)
    c.setStrokeColor(LINE)
    c.setLineWidth(1)
    c.roundRect(x, y - h, w, h, 8, stroke=1, fill=1)
    c.setFillColor(LIME)
    c.circle(x + 18, y - 22, 13, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(x + 18, y - 26, str(n))
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x + 40, y - 19, title)
    draw_wrapped(c, body, x + 40, y - 34, w - 50, "Helvetica", 7.7, 9.5, MUTED)


def page_one(c: canvas.Canvas) -> None:
    hero_h = 250
    draw_gradient(c, 0, PAGE_H - hero_h, PAGE_W, hero_h)
    draw_logo_text(c, "GRÜNDERSZENE", PAGE_W / 2 - 112, PAGE_H - 43, 25)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 10)
    c.drawRightString(PAGE_W - M, PAGE_H - 31, "TEAM")

    draw_mika_host(c, -26, PAGE_H - 220, 164)

    title_x = 150
    draw_hero_word(c, "MIKA", title_x, PAGE_H - 164, 42, 3.0)
    draw_hero_word(c, "TEAM BRIEF", title_x, PAGE_H - 202, 33, 1.5)

    draw_wrapped(
        c,
        "Interne Erklärung für Setup, Founder-Flow, Skills und Support.",
        title_x,
        PAGE_H - 229,
        300,
        "Helvetica-Bold",
        11,
        13,
        WHITE,
    )
    c.setFillColor(LIME)
    c.roundRect(PAGE_W - M - 92, PAGE_H - 190, 92, 32, 16, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(PAGE_W - M - 46, PAGE_H - 178, "INTERN")

    y = PAGE_H - hero_h - 30
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(M, y, "Was ist Mika?")
    y -= 26
    y = draw_wrapped(
        c,
        "Mika ist der Codex-Assistent für das Gründerszene Sommercamp. Mika macht aus einer Consumer-App-Idee einen geführten Arbeitsmodus: aktuellen Stand verstehen, gezielt nachfragen, Spec und Reviews nutzen, bauen, prüfen, launchen und lernen.",
        M,
        y,
        PAGE_W - 2 * M,
        "Helvetica-Bold",
        10.8,
        13.5,
        MUTED,
    )

    col_y = y - 24
    left_w = 250
    right_x = M + left_w + 26
    right_w = PAGE_W - M - right_x
    section_title(c, "Team-Promise", M, col_y, left_w)
    bullet_list(
        c,
        [
            "Mika ist Coach, Produkt-Sparring, Distribution-Partner und Coding-Agent in einem.",
            "Mika liest vorhandene Unterlagen zuerst, damit Founder nichts doppelt machen.",
            "Mika gibt Pushback, wenn Scope, Zielnutzer oder Distribution zu schwach sind.",
            "Mika baut nicht blind: erst ca. 95% Verständnis, dann kleinster launchbarer Schritt.",
        ],
        M,
        col_y - 43,
        left_w,
    )

    section_title(c, "Founder-Flow", right_x, col_y, right_w)
    steps = [
        ("GitHub öffnen", "Founder öffnet den öffentlichen Repo-Link. Dieser Link ist teilbar."),
        ("ZIP herunterladen", "Founder klickt auf Code und Download ZIP."),
        ("Entpacken", "Founder entpackt die ZIP-Datei auf dem Laptop."),
        ("Ordner öffnen", "Founder öffnet den ganzen entpackten Ordner in Codex."),
        ("Starten", "Founder schreibt: Starte Mika."),
    ]
    sy = col_y - 36
    for idx, (title, body) in enumerate(steps, start=1):
        step_card(c, idx, title, body, right_x, sy, right_w, 47)
        sy -= 56

    c.setFillColor(BLACK)
    c.rect(M, 62, PAGE_W - 2 * M, 72, stroke=0, fill=1)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(M + 16, 113, "Wichtig für das Team")
    draw_wrapped(
        c,
        "Mika baut nicht aus groben Ideen heraus. Wenn Kontext fehlt, erklärt Mika das passende Tool im Arsenal, fragt nach und baut erst, wenn Ziel, Nutzer, Flow, Scope und Risiko klar genug sind.",
        M + 16,
        95,
        PAGE_W - 2 * M - 32,
        "Helvetica-Bold",
        8.8,
        10.8,
        WHITE,
    )
    footer(c, 1)


SKILLS = [
    ("mika-start", "Startet oder resumed Mika und routet in den passenden nächsten Schritt."),
    ("mika-project-setup", "Erstellt Projektdateien, Upload-Ordner und dauerhaften Kontext im Founder-Ordner."),
    ("current-state-audit", "Liest Unterlagen, Links, Screenshots oder Code und verhindert doppelte Arbeit."),
    ("founder-onboarding", "Fragt Founder, Idee, Skill-Gaps, Zielnutzer, AI-Hilfe und Coaching-Stil ab."),
    ("spec-builder", "Macht aus vagen Feature-, Website- oder App-Wünschen eine klare Spezifikation."),
    ("product-wedge-review", "Schneidet breite Ideen auf den kleinsten launchbaren Consumer-Wedge herunter."),
    ("distribution-review", "Prüft erste 100 Nutzer, Kanal, Activation, Retention, Sharing und Story."),
    ("ten-week-plan", "Erstellt den 10-Wochen-Plan mit öffentlichem Launch in Woche 4."),
    ("engineering-plan-review", "Prüft Architektur, Datenfluss, Failure Modes, Tests, Datenschutz und technische Risiken."),
    ("design-review", "Prüft First Screen, CTA, UI-Zustände, Mobile, visuelle Richtung und AI-Slop-Risiko."),
    ("website-builder", "Fragt Produkt- und Designfragen und baut Website, Landing Page, Demo oder Web-App-MVP."),
    ("build-sprint", "Setzt den nächsten kleinen Build-Schritt um, prüft ihn und loggt die Änderung."),
    ("code-review", "Prüft Code auf Bugs, Regressionen, fehlende Tests, Privacy-Risiken und Vollständigkeit."),
    ("browser-qa", "Testet lokale oder deployte App-Flows im Browser und dokumentiert sichtbare Bugs."),
    ("launch-readiness", "Prüft UX, QA, Analytics, Datenschutz, Landing Page, Assets und Rollback."),
    ("ship-release", "Prüft Release-Schritte, Tests, QA-Status, Risiken, Rollback und Launch-Kommunikation."),
    ("growth-retro", "Führt wöchentliche Retros zu shipped work, Nutzern, Metriken und Entscheidung."),
    ("drift-check", "Holt Founder zurück auf den Wochenfokus, wenn sie überbauen oder ausweichen."),
    ("editorial-brief", "Erstellt Gründerszene-taugliche Updates aus Fortschritt, Learnings und Metriken."),
]


def page_two(c: canvas.Canvas) -> None:
    draw_gradient(c, 0, PAGE_H - 92, PAGE_W, 92)
    draw_logo_text(c, "GRÜNDERSZENE", M, PAGE_H - 44, 22)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 22)
    c.drawRightString(PAGE_W - M, PAGE_H - 48, "SKILL-LANDKARTE")

    y = PAGE_H - 122
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(M, y, "Welche Fähigkeiten sind im Mika-Ordner?")
    draw_wrapped(
        c,
        "Founder müssen diese Skill-Dateien nicht anfassen. Mika nutzt sie automatisch, sobald der heruntergeladene Ordner in Codex geöffnet ist.",
        M,
        y - 19,
        PAGE_W - 2 * M,
        "Helvetica-Bold",
        9.6,
        11.5,
        MUTED,
    )

    start_y = y - 52
    cols = 3
    gap_x = 10
    gap_y = 8
    card_w = (PAGE_W - 2 * M - gap_x * (cols - 1)) / cols
    card_h = 52
    for i, (name, body) in enumerate(SKILLS):
        col = i % cols
        row = i // cols
        x = M + col * (card_w + gap_x)
        cy = start_y - row * (card_h + gap_y)
        card(c, x, cy, card_w, card_h, name, body)

    footer(c, 2)


def page_three(c: canvas.Canvas) -> None:
    draw_gradient(c, 0, PAGE_H - 92, PAGE_W, 92)
    draw_logo_text(c, "GRÜNDERSZENE", M, PAGE_H - 44, 22)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 22)
    c.drawRightString(PAGE_W - M, PAGE_H - 48, "AUSLIEFERUNG")

    y = PAGE_H - 124
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(M, y, "So gebt ihr Mika an Founder weiter")
    draw_wrapped(
        c,
        "Wichtig: Nicht den alten lokalen codex://... Link verschicken. Nur der öffentliche GitHub-Link ist auf anderen Laptops teilbar.",
        M,
        y - 20,
        PAGE_W - 2 * M,
        "Helvetica-Bold",
        9,
        11,
        MUTED,
    )

    steps = [
        ("GitHub-Link schicken", "Per Mail, Slack oder Notion: github.com/Leopold-26/mika-sommercamp."),
        ("PDF mitschicken", "Founder-PDF erklärt den Ablauf ohne Codex-Fachwörter: Link öffnen, ZIP laden, Ordner öffnen."),
        ("Founder öffnet Codex", "Founder entpackt die ZIP und öffnet den ganzen Ordner in Codex."),
        ("Founder startet Mika", "Im neuen Chat schreibt der Founder: Starte Mika."),
        ("Unterlagen einsammeln", "Founder können Materialien direkt in den Chat ziehen; Mika auditiert sie vor weiteren Fragen."),
    ]
    sy = y - 56
    for idx, (title, body) in enumerate(steps, start=1):
        step_card(c, idx, title, body, M, sy, PAGE_W - 2 * M, 43)
        sy -= 50

    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(M, sy - 8, "Founder-Kurzfassung")
    command_box(
        c,
        M,
        sy - 20,
        PAGE_W - 2 * M,
        56,
        [
            "GitHub öffnen -> Code -> Download ZIP -> entpacken",
            "Ordner in Codex öffnen -> neuen Chat starten -> Starte Mika",
        ],
    )
    c.linkURL(REPO_URL, (M, sy - 89, PAGE_W - M, sy - 18), relative=0)

    col_top = sy - 96
    left_w = 250
    right_x = M + left_w + 26
    right_w = PAGE_W - M - right_x

    section_title(c, "Updates", M, col_top, left_w)
    bullet_list(
        c,
        [
            "Der GitHub-Link bleibt gleich, solange das Repo öffentlich bleibt.",
            "Nach Skill-, Icon- oder Textänderungen committen und auf main pushen.",
            "Founder laden danach bei Bedarf die ZIP erneut herunter.",
        ],
        M,
        col_top - 42,
        left_w,
        8.4,
    )

    section_title(c, "Support", right_x, col_top, right_w)
    bullet_list(
        c,
        [
            "Wenn Mika zu früh bauen will: Onboarding-Status, Produktthese und Distribution-Plan prüfen.",
            "Wenn Mika Unterlagen übersieht: Dateien in docs/sommercamp/00_uploads/ legen oder Links im Chat nachreichen.",
            "Wenn Skills nicht sichtbar sind: prüfen, ob der ganze entpackte Ordner in Codex geöffnet wurde.",
        ],
        right_x,
        col_top - 42,
        right_w,
        8.4,
    )

    c.setFillColor(BLACK)
    c.rect(M, 72, PAGE_W - 2 * M, 70, stroke=0, fill=1)
    c.setFillColor(LIME)
    c.roundRect(M + 16, 100, 92, 26, 13, stroke=0, fill=1)
    c.setFillColor(BLACK)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(M + 62, 109, "MERKSATZ")
    draw_wrapped(
        c,
        "Mika soll Founder nicht nur bedienen, sondern führen: erst 95% verstehen, dann widersprechen, dann planen, dann den kleinsten sinnvollen nächsten Schritt bauen.",
        M + 122,
        115,
        PAGE_W - 2 * M - 140,
        "Helvetica-Bold",
        9.6,
        12,
        WHITE,
    )
    footer(c, 3)


def render() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=A4)
    c.setTitle("Mika Sommercamp Team-Erklärung")
    c.setAuthor("Gründerszene Sommercamp")

    page_one(c)
    c.showPage()
    page_two(c)
    c.showPage()
    page_three(c)
    c.save()
    print(OUT)


if __name__ == "__main__":
    render()
