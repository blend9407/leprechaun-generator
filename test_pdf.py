import os
import tempfile
from weasyprint import HTML
from datetime import datetime

# Check template
template_file = "pdf-templates/classic-emerald-template.html"
if os.path.exists(template_file):
    print(f"Template found: {template_file}")
    with open(template_file, 'r') as f:
        html = f.read()
    
    # Replace placeholders
    html = html.replace('{{leprechaun_name}}', 'Finn O\'Malley')
    html = html.replace('{{meaning}}', 'Guardian of hidden treasures')
    html = html.replace('{{date}}', datetime.now().strftime('%B %d, %Y'))
    
    # Generate PDF
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
        pdf_path = tmp.name
    
    try:
        HTML(string=html).write_pdf(pdf_path)
        size = os.path.getsize(pdf_path)
        print(f"PDF generated: {pdf_path} ({size} bytes)")
        if size > 1000:
            print("✓ PDF generation successful")
        else:
            print("⚠ PDF generated but size suspiciously small")
        os.unlink(pdf_path)
    except Exception as e:
        print(f"✗ PDF generation failed: {e}")
else:
    print(f"Template not found: {template_file}")
    # List available templates
    print("Available templates:")
    for f in os.listdir("pdf-templates"):
        print(f"  - {f}")
