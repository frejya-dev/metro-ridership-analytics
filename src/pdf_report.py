from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


METRO_BLUE = "#0054A6"
METRO_PURPLE = "#7257D8"
TEXT_GRAY = "#666666"


def format_number(value):
    return f"{value:,.0f}"


def generate_pdf_report(summary, chart_path, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    c.setFillColor(colors.HexColor(METRO_BLUE))
    c.rect(0, height - 0.45 * inch, width, 0.45 * inch, fill=True, stroke=False)

    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(0.75 * inch, height - 1.15 * inch, "LA Metro Ridership Report")

    c.setFont("Helvetica", 11)
    c.setFillColor(colors.HexColor(TEXT_GRAY))
    c.drawString(0.75 * inch, height - 1.45 * inch, "Systemwide Monthly Boardings | Apr 2025 - Mar 2026")

    y = height - 2.05 * inch

    c.setFillColor(colors.HexColor(METRO_PURPLE))
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.75 * inch, y, "Key Metrics")

    y -= 0.35 * inch
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 10)

    metrics = [
        ("Total Ridership", format_number(summary["total"])),
        ("Average Monthly Ridership", format_number(summary["average"])),
        ("Highest Month", f"{summary['highest_month']} ({format_number(summary['highest_value'])})"),
        ("Lowest Month", f"{summary['lowest_month']} ({format_number(summary['lowest_value'])})"),
        ("Latest Month", f"{summary['latest_month']} ({format_number(summary['latest_value'])})"),
        ("Month-over-Month Change", f"{summary['mom_change']:+.1f}%"),
    ]

    for label, value in metrics:
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0.75 * inch, y, label)
        c.setFont("Helvetica", 10)
        c.drawString(3.1 * inch, y, value)
        y -= 0.25 * inch

    y -= 0.15 * inch

    c.setFillColor(colors.HexColor(METRO_PURPLE))
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.75 * inch, y, "Ridership Trend")

    y -= 3.25 * inch
    c.drawImage(chart_path, 0.75 * inch, y, width=7.0 * inch, preserveAspectRatio=True, mask="auto")

    y -= 0.45 * inch

    c.setFillColor(colors.HexColor(METRO_PURPLE))
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.75 * inch, y, "Key Observations")

    y -= 0.32 * inch
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 10)

    observations = [
        "Ridership remained relatively stable across the reporting period.",
        f"{summary['highest_month']} recorded the highest monthly ridership.",
        f"{summary['latest_month']} ended the period with {summary['mom_change']:+.1f}% month-over-month change.",
    ]

    for observation in observations:
        c.drawString(0.9 * inch, y, f"- {observation}")
        y -= 0.24 * inch

    c.setFillColor(colors.HexColor(TEXT_GRAY))
    c.setFont("Helvetica", 8)
    c.drawString(0.75 * inch, 0.5 * inch, "Generated automatically with Python, pandas, matplotlib, and ReportLab.")

    c.save()