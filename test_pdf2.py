import os
import tempfile
from weasyprint import HTML
from datetime import datetime

template_file = "pdf-templates/classic-emerald-template.html"
print(f"Testing template: {template_file}")
print(f"Exists: {os.path.exists(template_file)}")

if os.path.exists(template_file):
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
        print(f"✓ PDF generated: {pdf_path} ({size} bytes)")
        
        # Clean up
        os.unlink(pdf_path)
        return True
    except Exception as e:
        print(f"✗ PDF generation failed: {e}")
        return False
else:
    print("Template not found")
    return False
