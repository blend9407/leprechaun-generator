
# watermark.py - Simple PDF watermarking
from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
import base64

def add_watermark_to_pdf(pdf_data, watermark_text="FREE VERSION"):
    """Add a simple watermark to PDF data"""
    # For now, we'll just add a watermark text to the HTML
    # In production, use proper PDF watermarking library
    return pdf_data

# Alternative: Create watermarked HTML
def create_watermarked_html(html_content, watermark_text="FREE VERSION"):
    """Add watermark CSS to HTML"""
    watermark_css = f"""
    <style>
    .watermark {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) rotate(-45deg);
        font-size: 60px;
        color: rgba(0, 0, 0, 0.1);
        z-index: 1000;
        pointer-events: none;
        white-space: nowrap;
        font-weight: bold;
    }}
    </style>
    <div class="watermark">{watermark_text}</div>
    """
    # Insert watermark before closing body tag
    if '</body>' in html_content:
        return html_content.replace('</body>', watermark_css + '
</body>')
    else:
        return html_content + watermark_css
