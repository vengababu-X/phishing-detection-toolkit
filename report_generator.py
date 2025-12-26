from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_report(url, result):
    filename = f"reports/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    c.drawString(50, 800, "PhishGuard Pro – Security Report")
    c.drawString(50, 760, f"URL: {url}")
    c.drawString(50, 730, f"Result: {result}")
    c.drawString(50, 700, f"Generated: {datetime.now()}")
    c.save()
    return filename
