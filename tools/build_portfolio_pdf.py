#!/usr/bin/env python3
"""Build a compact, image-led PDF portfolio from the website assets."""

from __future__ import annotations

import hashlib
import html
import os
from pathlib import Path

from PIL import Image, ImageOps
from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
TMP = ROOT / "tmp" / "pdfs" / "portfolio_images"
OUTPUT = ROOT / "output" / "pdf" / "Imants_Zvirgzdins_Visual_Portfolio.pdf"

PAGE_W, PAGE_H = landscape(A4)

INK = HexColor("#151A1C")
MUTED = HexColor("#596467")
PAPER = HexColor("#F5F7F5")
LINE = HexColor("#D7DEDC")
TEAL = HexColor("#167B78")
CORAL = HexColor("#D65E49")
GOLD = HexColor("#D8A83E")
DARK = HexColor("#090B0C")

PORTFOLIO_URL = "https://izvirgzdins-pixel.github.io/CV/"
EMAIL = "izvirgzdins@gmail.com"
PHONE = "+371 28 312 952"


def safe(text: str) -> str:
    return html.escape(text, quote=False)


def image_path(name: str) -> Path:
    path = ASSETS / name
    if not path.exists():
        raise FileNotFoundError(path)
    return path


def prepared_image(name: str, width_pt: float, height_pt: float, mode: str = "cover", bg: str = "#F5F7F5") -> Path:
    """Create a right-sized JPEG so the final PDF remains compact."""
    TMP.mkdir(parents=True, exist_ok=True)
    source = image_path(name)
    width_px = max(240, min(1800, int(width_pt * 2.1)))
    height_px = max(180, min(1800, int(height_pt * 2.1)))
    key = hashlib.sha1(f"{source}:{source.stat().st_mtime_ns}:{width_px}:{height_px}:{mode}:{bg}".encode()).hexdigest()[:14]
    output = TMP / f"{source.stem}-{key}.jpg"
    if output.exists():
        return output

    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened).convert("RGB")
        if mode == "contain":
            image.thumbnail((width_px, height_px), Image.Resampling.LANCZOS)
            canvas = Image.new("RGB", (width_px, height_px), bg)
            x = (width_px - image.width) // 2
            y = (height_px - image.height) // 2
            canvas.paste(image, (x, y))
            image = canvas
        else:
            image = ImageOps.fit(
                image,
                (width_px, height_px),
                method=Image.Resampling.LANCZOS,
                centering=(0.5, 0.5),
            )
        image.save(output, "JPEG", quality=80, optimize=True, progressive=True)
    return output


def draw_image(c: Canvas, name: str, x: float, y: float, w: float, h: float, mode: str = "cover", bg: str = "#F5F7F5") -> None:
    prepared = prepared_image(name, w, h, mode=mode, bg=bg)
    c.drawImage(ImageReader(str(prepared)), x, y, width=w, height=h, mask="auto")


def paragraph(c: Canvas, text: str, x: float, top: float, width: float, font_size: float = 10, leading: float | None = None,
              color=MUTED, font="Helvetica", space_after: float = 0) -> float:
    leading = leading or font_size * 1.35
    style = ParagraphStyle(
        "body",
        fontName=font,
        fontSize=font_size,
        leading=leading,
        textColor=color,
        alignment=TA_LEFT,
        spaceAfter=0,
        splitLongWords=True,
    )
    item = Paragraph(safe(text), style)
    _, h = item.wrap(width, PAGE_H)
    item.drawOn(c, x, top - h)
    return top - h - space_after


def bullets(c: Canvas, items: list[str], x: float, top: float, width: float, font_size: float = 9.2,
            leading: float = 12.4, gap: float = 4) -> float:
    y = top
    for item in items:
        y = paragraph(c, f"- {item}", x, y, width, font_size, leading, MUTED, space_after=gap)
    return y


def label(c: Canvas, text: str, x: float, y: float, color=TEAL) -> None:
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 7.4)
    c.drawString(x, y, text.upper())


def heading(c: Canvas, text: str, x: float, y: float, size: float = 25, color=INK) -> None:
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", size)
    c.drawString(x, y, text)


def rule(c: Canvas, x: float, y: float, w: float, color=LINE, thickness: float = 0.7) -> None:
    c.setStrokeColor(color)
    c.setLineWidth(thickness)
    c.line(x, y, x + w, y)


def page_header(c: Canvas, section: str, page_num: int, accent=TEAL) -> None:
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(38, PAGE_H - 27, "IMANTS ZVIRGZDINS")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7.5)
    c.drawRightString(PAGE_W - 38, PAGE_H - 27, f"{section.upper()}  /  {page_num:02d}")
    c.setFillColor(accent)
    c.rect(38, PAGE_H - 36, 58, 2.4, stroke=0, fill=1)


def page_footer(c: Canvas, page_num: int) -> None:
    rule(c, 38, 23, PAGE_W - 76)
    c.setFont("Helvetica", 7.2)
    c.setFillColor(MUTED)
    c.drawString(38, 11, "Mechanical Engineer  |  Industrial Designer")
    c.drawRightString(PAGE_W - 38, 11, f"{EMAIL}  |  {page_num:02d}")


def start_page(c: Canvas, section: str, page_num: int, bg=PAPER, accent=TEAL) -> None:
    c.setFillColor(bg)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    page_header(c, section, page_num, accent)


def finish_page(c: Canvas, page_num: int) -> None:
    page_footer(c, page_num)
    c.showPage()


def cover(c: Canvas) -> None:
    c.setFillColor(DARK)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    draw_image(c, "bbi-blimp-render-dark.jpg", 375, 0, PAGE_W - 375, PAGE_H, mode="cover", bg="#090B0C")
    c.setFillColor(DARK)
    c.rect(0, 0, 430, PAGE_H, stroke=0, fill=1)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 34)
    c.drawString(38, PAGE_H - 130, "IMANTS")
    c.drawString(38, PAGE_H - 169, "ZVIRGZDINS")
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, PAGE_H - 199, "MECHANICAL ENGINEER")
    c.drawString(40, PAGE_H - 217, "INDUSTRIAL DESIGNER")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(40, 112, "10+ YEARS EXPERIENCE")
    c.drawString(182, 112, "RIGA, LATVIA")
    c.setFont("Helvetica", 8.5)
    c.setFillColor(HexColor("#C7CFCD"))
    c.drawString(40, 88, EMAIL)
    c.drawString(40, 72, PHONE)
    c.drawString(40, 56, PORTFOLIO_URL)
    c.linkURL(f"mailto:{EMAIL}", (40, 84, 180, 97), relative=0)
    c.linkURL(PORTFOLIO_URL, (40, 52, 300, 66), relative=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7.2)
    c.drawRightString(PAGE_W - 30, 19, "MICROPHONE HANDLING-NOISE REDUCTION / BUBBLEBEE INDUSTRIES")
    c.showPage()


def profile_page(c: Canvas, page_num: int) -> None:
    start_page(c, "Profile and experience", page_num)
    heading(c, "Product engineering with industrial-design range.", 38, PAGE_H - 78, 25)
    paragraph(
        c,
        "Mechanical engineer and industrial designer with 10+ years of experience developing physical products from early architecture through prototyping, validation, production documentation, and supplier handoff.",
        38,
        PAGE_H - 103,
        390,
        10.6,
        15,
        MUTED,
    )

    x_left = 38
    y = PAGE_H - 184
    label(c, "Core capabilities", x_left, y)
    y -= 25
    capabilities = [
        ("Mechanical product design", "Mechanisms, enclosures, electronics packaging, tolerance-aware details, and assembly definition."),
        ("CAD and documentation", "SolidWorks, controlled assemblies, production drawings, BOMs, manuals, and PDM workflows."),
        ("Manufacturing and DFM", "Injection moulding, CNC, sheet metal, extrusion, additive manufacturing, and supplier communication."),
        ("Validation", "FEA/CFD support, vibration and transmittance testing, ESP32 data logging, and assembly-process test jigs."),
    ]
    for title, body in capabilities:
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(x_left, y, title)
        y = paragraph(c, body, x_left, y - 8, 300, 8.8, 12, MUTED, space_after=10)
        rule(c, x_left, y + 4, 300)
        y -= 10

    x_timeline = 384
    label(c, "Professional experience", x_timeline, PAGE_H - 184)
    y = PAGE_H - 209
    roles = [
        ("2025.03 - 2026.07", "Senior Mechanical Engineer", "Bubblebee Industries", "Audio hardware, quick-release mechanisms, damping layouts, and ESP32 acceleration validation."),
        ("2023.10 - 2025.02", "Senior Mechanical Engineer", "Giraffe360", "LiDAR motor R&D, optical tooling, injection-moulded parts, CFD, jigs, and production support."),
        ("2023.06 - 2023.08", "Mechanical Designer", "Warp Agency", "Mechanical architecture and prototypes for a quiet 2 x 7 m kinetic robotic chandelier."),
        ("2022.09 - 2023.10", "Mechanical Engineer / Industrial Designer", "Riga Technical University", "Sealed sensors, industrial mechanisms, startup prototypes, calculations, and technical layouts."),
        ("2015.09 - 2022.09", "Lead Mechanical Engineer / Industrial Designer", "SAFtehnika JSC", "RF equipment and IoT products from concept through mass production, IP54/IP68, and ATEX support."),
        ("2013 - 2015.09", "Industrial Designer / Project Manager", "ET Sons", "Complex CNC-manufactured design objects and wearable product concepts."),
    ]
    for date, role, company, body in roles:
        c.setFillColor(TEAL)
        c.rect(x_timeline, y - 2, 5, 5, stroke=0, fill=1)
        c.setFillColor(MUTED)
        c.setFont("Helvetica-Bold", 7.2)
        c.drawString(x_timeline + 14, y, date)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 9.3)
        c.drawString(x_timeline + 128, y, role)
        c.setFont("Helvetica", 8.7)
        c.setFillColor(INK)
        c.drawString(x_timeline + 128, y - 13, company)
        y = paragraph(c, body, x_timeline + 128, y - 20, 285, 7.8, 10.2, MUTED, space_after=9)
        rule(c, x_timeline + 14, y + 4, 399, LINE, 0.5)
        y -= 10

    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, 47, stroke=0, fill=1)
    finish_page(c, page_num)


def project_intro(c: Canvas, page_num: int, company: str, title: str, date: str, accent=TEAL) -> None:
    start_page(c, company, page_num, accent=accent)
    label(c, f"{company}  /  {date}", 38, PAGE_H - 69, accent)
    heading(c, title, 38, PAGE_H - 101, 25)


def bubblebee_page(c: Canvas, page_num: int) -> None:
    project_intro(c, page_num, "Bubblebee Industries", "Microphone handling-noise reduction", "2025.03 - 2026.07", CORAL)
    draw_image(c, "bbi-vibration-analyzer-interface-enhanced.png", 38, 228, 468, 226, "cover", "#090B0C")
    draw_image(c, "bbi-blimp-render-dark.jpg", 38, 52, 229, 164, "cover", "#090B0C")
    draw_image(c, "bbi-quickrelease-render-dark.jpg", 277, 52, 229, 164, "cover", "#090B0C")
    x = 538
    y = 449
    paragraph(c, "Professional audio hardware focused on reducing transmitted handling noise while keeping microphone setup fast and production-ready.", x, y, 263, 10.5, 14.5, INK, space_after=17)
    label(c, "Engineering contribution", x, y - 65, CORAL)
    y = bullets(c, [
        "Designed mechanical quick-release concepts and blimp hardware.",
        "Developed damping layouts with strong emphasis on material choice and efficient assembly flow.",
        "Compared mechanical configurations through vibration and transmittance analysis.",
        "Built an ESP32-based acceleration test jig with custom data logging for validation.",
    ], x, y - 88, 263, 9.3, 12.5, 7)
    y -= 6
    rule(c, x, y, 263, CORAL, 1.2)
    label(c, "Process", x, y - 24, CORAL)
    paragraph(c, "Concept architecture  /  CAD  /  prototype build  /  vibration measurement  /  design iteration  /  production detail", x, y - 38, 263, 8.6, 12, MUTED)
    finish_page(c, page_num)


def giraffe_page(c: Canvas, page_num: int) -> None:
    project_intro(c, page_num, "Giraffe360", "LiDAR motor and optical tooling", "2023.10 - 2025.02", TEAL)
    draw_image(c, "giraffe360-lidar-optics-white.jpg", 38, 278, 235, 176, "contain", "#FFFFFF")
    draw_image(c, "giraffe360-moldflow-pressure-side-brackets.png", 281, 278, 235, 176, "contain", "#FFFFFF")
    draw_image(c, "giraffe360-cad-optical-tooling-enhanced.jpg", 38, 52, 322, 214, "contain", "#E8ECEB")
    draw_image(c, "giraffe360-camera-assembly-screenshot.png", 369, 52, 147, 214, "contain", "#FFFFFF")
    x = 548
    y = 450
    paragraph(c, "Mechanical R&D and production support for a LiDAR-integrated camera platform, connecting rotating hardware, optical alignment, electronics packaging, and assembly process design.", x, y, 253, 10.2, 14.2, INK, space_after=16)
    label(c, "Selected responsibilities", x, y - 68)
    bullets(c, [
        "LiDAR-integrated brushless motor development and injection-moulded part design.",
        "Optical component gluing robot, adjustment frames, and PCB test jigs.",
        "Moldflow pressure and deflection analysis for the RJC side-bracket tooling.",
        "Assembly issue investigation and supplier communication for process reliability.",
    ], x, y - 91, 253, 9.1, 12.3, 7)
    finish_page(c, page_num)


def warp_page(c: Canvas, page_num: int) -> None:
    project_intro(c, page_num, "Warp Agency / Gravity Team Lustra", "2 x 7 m kinetic robotic chandelier", "2023.06 - 2023.08", CORAL)
    draw_image(c, "warp-lustra-installed-overview.jpg", 38, 52, 489, 402, "cover", "#101214")
    draw_image(c, "warp-lustra-installed-open.jpg", 538, 262, 125, 192, "cover", "#101214")
    draw_image(c, "warp-lustra-carriage-detail.jpg", 674, 262, 127, 192, "cover", "#101214")
    x = 538
    y = 240
    paragraph(c, "Mechanical architecture and workshop validation for a large-format chandelier designed to move quietly, reliably, and repeatedly above an occupied interior.", x, y, 263, 9.8, 13.5, INK, space_after=14)
    bullets(c, [
        "Rail, pulley, actuator, support, and ceiling-interface design.",
        "Low-noise motion and robust repeated operation.",
        "Workshop prototypes before full ceiling installation.",
        "SolidWorks assemblies, part models, and installation-ready details.",
    ], x, y - 68, 263, 8.7, 11.6, 5)
    finish_page(c, page_num)


def spectrum_page(c: Canvas, page_num: int) -> None:
    project_intro(c, page_num, "SAFtehnika JSC / LMT", "Spectrum Compact and drone integration", "2015.09 - 2022.09", TEAL)
    draw_image(c, "img-017.png", 38, 255, 495, 199, "contain", "#FFFFFF")
    draw_image(c, "img-014.png", 38, 52, 235, 191, "contain", "#FFFFFF")
    draw_image(c, "img-018.png", 285, 52, 248, 191, "contain", "#FFFFFF")

    x = 561
    label(c, "Lead mechanical engineering", x, 450)
    y = paragraph(c, "Portable RF measurement hardware developed for field installers and regulatory institutions, from product architecture through production release.", x, 431, 240, 9.6, 13.1, INK, space_after=12)

    label(c, "Spectrum Compact", x, y, TEAL)
    y = bullets(c, [
        "Owned mechanical architecture, industrial design, and manufacturable product detail.",
        "Combined CNC, sheet metal, silicone moulding, PCB packaging, and IP54 requirements.",
        "Prepared production drawings, assembly documentation, BOMs, and supplier-ready files.",
    ], x, y - 18, 240, 8.6, 11.5, 5)

    rule(c, x, y + 2, 240, TEAL, 1)
    label(c, "Drone modification with LMT", x, y - 21, TEAL)
    bullets(c, [
        "Developed a lightweight modular attachment for RF tower monitoring and audit workflows.",
        "Integrated vibration damping, exchangeable RF polarization components, and infrared-camera support.",
    ], x, y - 39, 240, 8.6, 11.5, 5)
    finish_page(c, page_num)


def aranet_integra_page(c: Canvas, page_num: int) -> None:
    project_intro(c, page_num, "SAFtehnika JSC / Aranet", "IoT sensors and 5G radio equipment", "2015.09 - 2022.09", GOLD)
    draw_image(c, "img-023.png", 38, 292, 319, 162, "contain", "#FFFFFF")
    draw_image(c, "img-024.png", 369, 292, 147, 162, "contain", "#FFFFFF")
    draw_image(c, "integra-e2-render-angle.png", 38, 52, 478, 226, "contain", "#FFFFFF")

    x = 548
    label(c, "Aranet", x, 450, GOLD)
    y = paragraph(c, "Industrial design and mechanical engineering for LoRa sensor products used in farming, horticulture, offices, and education.", x, 431, 253, 9.4, 12.8, INK, space_after=8)
    y = bullets(c, [
        "Injection-moulded parts, IP68 solutions, drawings, BOMs, and quality control.",
        "Aranet4 exceeded 100,000 produced units and was Latvia's Most Innovative Product of 2019.",
    ], x, y, 253, 8.5, 11.2, 4)

    rule(c, x, y - 2, 253, GOLD, 1)
    label(c, "Integra-E2", x, y - 25, GOLD)
    y = paragraph(c, "Lead mechanical engineering for point-to-point 5G radio equipment with a simple, robust enclosure philosophy.", x, y - 42, 253, 9.4, 12.8, INK, space_after=8)
    bullets(c, [
        "Aluminium-extrusion base and CNC-machined heat-sink cover.",
        "IP68 design, ATEX certification support, assembly definition, and BOM documentation.",
    ], x, y, 253, 8.5, 11.2, 4)
    finish_page(c, page_num)


def rtu_upcatalyst_page(c: Canvas, page_num: int) -> None:
    project_intro(c, page_num, "Riga Technical University / UpCatalyst", "Industrial sensors and process mechanisms", "2022.09 - 2023.10", TEAL)
    c.setFillColor(white)
    c.rect(38, 52, 370, 402, stroke=0, fill=1)
    c.rect(420, 52, 381, 402, stroke=0, fill=1)
    draw_image(c, "rtu-scaffolding-sensor-ipin.jpg", 38, 224, 370, 230, "cover", "#FFFFFF")
    draw_image(c, "upcatalyst-scraper-container-clean.jpg", 420, 224, 381, 230, "cover", "#FFFFFF")
    label(c, "Scaffolding pressure sensor", 54, 200)
    y = paragraph(c, "Load-cell based sensor with sealed mechanical architecture and wireless operation.", 54, 183, 330, 9.5, 12.5, INK, space_after=7)
    bullets(c, [
        "PU overmoulding, LoRa antenna, wireless charging, and IP68 protection.",
        "Sheet-metal covers, PCB layout, battery assembly, and FEA support.",
    ], 54, y, 330, 8.4, 11.1, 4)

    label(c, "Carbon scraper mechanism", 436, 200, CORAL)
    y = paragraph(c, "Mechanical scraper concept, layout, calculations, and documentation for an industrial carbon-processing mechanism.", 436, 183, 341, 9.5, 12.5, INK, space_after=7)
    bullets(c, [
        "Scraper architecture and industrial process layout.",
        "Mechanical load calculations, FEA stress analysis, and production drawings.",
    ], 436, y, 341, 8.4, 11.1, 4)
    finish_page(c, page_num)


def breadth_page(c: Canvas, page_num: int) -> None:
    project_intro(c, page_num, "Selected breadth", "Industrial design and production detail", "2013 - 2023", CORAL)
    boxes = [
        (38, 269, 179, 185, "fire-alarm-smoke-detector-render.png", "Fire alarm system", "EN-54 product-family design for smoke, sound, light, and control devices."),
        (229, 269, 179, 185, "img-029.png", "Chemical gas sensor", "Compact IP68 concept with a simplified airtight, screw-free assembly."),
        (420, 269, 179, 185, "img-044.png", "Latvian Architecture Award", "50+ part Rubik's-cube pineapple produced with 5-axis CNC milling."),
        (611, 269, 190, 185, "img-040.png", "Production drawings", "Supplier-ready part, assembly, exploded-view, and quality-control documentation."),
    ]
    for x, y, w, h, image, title, body in boxes:
        draw_image(c, image, x, y, w, h, "contain", "#FFFFFF")
        c.setFillColor(white)
        c.rect(x, 52, w, 205, stroke=0, fill=1)
        label(c, title, x + 13, 232, CORAL)
        paragraph(c, body, x + 13, 214, w - 26, 8.8, 12, INK)

    finish_page(c, page_num)


def credentials_page(c: Canvas, page_num: int) -> None:
    start_page(c, "Certifications and training", page_num, accent=GOLD)
    heading(c, "Certifications and training", 38, PAGE_H - 78, 27)
    paragraph(c, "SolidWorks certification and specialist training supporting mechanical design, simulation, plastics, and production-ready product development.", 38, PAGE_H - 106, 650, 10.2, 14, MUTED)

    draw_image(c, "cert-solidworks-professional-mechanical-design.jpg", 38, 287, 366, 185, "contain", "#FFFFFF")
    draw_image(c, "cert-solidworks-associate-mechanical-design.jpg", 420, 287, 381, 185, "contain", "#FFFFFF")

    label(c, "Dassault Systemes SOLIDWORKS", 38, 269, GOLD)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(38, 251, "SOLIDWORKS Professional - Mechanical Design")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.2)
    c.drawString(38, 237, "Academic exam at Riga Technical University  /  2023.03.14")

    label(c, "Dassault Systemes SOLIDWORKS", 420, 269, GOLD)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(420, 251, "SOLIDWORKS Associate - Mechanical Design")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8.2)
    c.drawString(420, 237, "Academic exam at Riga Technical University  /  2023.03.10")

    rule(c, 38, 220, 763)
    draw_image(c, "cert-plm-solidworks-simulation.jpg", 38, 49, 118, 158, "contain", "#FFFFFF")
    label(c, "PLM Group Latvija SIA", 174, 191, GOLD)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(174, 170, "SolidWorks Simulation Training")
    paragraph(c, "Specialist training in simulation workflows for mechanical product development.", 174, 150, 218, 8.8, 12, MUTED)
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(174, 89, "2016.03.17-18")

    draw_image(c, "cert-plm-solidworks-plastics.jpg", 420, 49, 118, 158, "contain", "#FFFFFF")
    label(c, "PLM Group Latvija SIA", 556, 191, GOLD)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(556, 170, "SOLIDWORKS Plastics Training")
    paragraph(c, "Specialist training in plastics design and injection-moulding analysis workflows.", 556, 150, 225, 8.8, 12, MUTED)
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 8.2)
    c.drawString(556, 89, "2016.11.10-11")
    finish_page(c, page_num)


def build() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    canvas = Canvas(str(OUTPUT), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    canvas.setTitle("Imants Zvirgzdins - Visual Portfolio")
    canvas.setAuthor("Imants Zvirgzdins")
    canvas.setSubject("Mechanical engineering and industrial design portfolio")
    canvas.setCreator("Imants Zvirgzdins portfolio generator")

    cover(canvas)
    profile_page(canvas, 2)
    bubblebee_page(canvas, 3)
    giraffe_page(canvas, 4)
    warp_page(canvas, 5)
    spectrum_page(canvas, 6)
    aranet_integra_page(canvas, 7)
    rtu_upcatalyst_page(canvas, 8)
    breadth_page(canvas, 9)
    credentials_page(canvas, 10)
    canvas.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
