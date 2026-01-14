import os
import json
import random
from datetime import datetime
from flask import Flask, request, jsonify, send_file, render_template_string
from flask_cors import CORS
import subprocess
import tempfile
from weasyprint import HTML

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Database file
DB_FILE = 'names.json'

# Initialize database if not exists
if not os.path.exists(DB_FILE):
    with open(DB_FILE, 'w') as f:
        json.dump([], f)

# Health endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "leprechaun-name-generator",
        "timestamp": datetime.now().isoformat()
    }), 200

# Serve index.html
@app.route("/")
def index():
    return app.send_static_file('index.html')

# Name generation endpoint
@app.route("/api/generate-name", methods=["POST"])
def generate_name():
    try:
        data = request.get_json()
        first_name = data.get('first_name', '').strip()
        last_name = data.get('last_name', '').strip()
        method = data.get('method', 'traditional')
        
        if not first_name or not last_name:
            return jsonify({"success": False, "error": "First and last name required"}), 400
        
        # Irish first names
        irish_first = ["Aidan", "Brendan", "Cillian", "Darragh", "Eoin", "Finn", "Gearoid", "Liam", "Niall", "Oisin", "Padraig", "Ronan", "Sean", "Tadhg", "Cormac"]
        
        # Irish last names with prefixes
        irish_prefixes = ["Mc", "O'", "Mac", "Fitz"]
        irish_roots = ["Gleeson", "Murphy", "Kelly", "O'Brien", "Ryan", "Sullivan", "Walsh", "McCarthy", "O'Connor", "Doyle", "Kennedy", "Lynch", "Moore", "Reilly", "Brennan"]
        
        # Generate leprechaun name
        if method == "traditional":
            leprechaun_first = random.choice(irish_first)
            leprechaun_last = random.choice(irish_prefixes) + random.choice(irish_roots)
        elif method == "modern":
            leprechaun_first = random.choice(["Finn", "Riley", "Quinn", "Casey", "Dylan"])
            leprechaun_last = random.choice(["Green", "Gold", "Rainbow", "Clover", "Shamrock"])
        else:
            leprechaun_first = random.choice(irish_first)
            leprechaun_last = random.choice(irish_roots)
        
        leprechaun_name = f"{leprechaun_first} {leprechaun_last}"
        
        # Meanings
        meanings = [
            "Keeper of the rainbow's end",
            "Guardian of hidden treasures",
            "Weaver of golden dreams",
            "Master of four-leaf clovers",
            "Protector of ancient magic",
            "Craftsman of enchanted shoes",
            "Watcher of the emerald hills",
            "Keeper of the pot of gold"
        ]
        meaning = random.choice(meanings)
        
        # Save to database
        with open(DB_FILE, 'r') as f:
            names = json.load(f)
        
        entry = {
            "id": len(names) + 1,
            "real_name": f"{first_name} {last_name}",
            "leprechaun_name": leprechaun_name,
            "meaning": meaning,
            "method": method,
            "timestamp": datetime.now().isoformat()
        }
        names.append(entry)
        
        with open(DB_FILE, 'w') as f:
            json.dump(names, f, indent=2)
        
        return jsonify({
            "success": True,
            "leprechaun_name": leprechaun_name,
            "meaning": meaning,
            "method": method,
            "real_name": f"{first_name} {last_name}"
        })
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# PDF generation endpoint
@app.route("/api/generate-pdf", methods=["POST"])
def generate_pdf():
    try:
        data = request.get_json()
        leprechaun_name = data.get('leprechaun_name', 'Unknown Leprechaun')
        meaning = data.get('meaning', 'Guardian of hidden treasures')
        template = data.get('template', 'classic-emerald')
        
        # Load template
        template_file = f"pdf-templates/{template}-template.html"
        if not os.path.exists(template_file):
            template_file = "pdf-templates/classic-emerald-template.html"
        
        with open(template_file, 'r') as f:
            html_content = f.read()
        
        # Replace placeholders
        html_content = html_content.replace('{{leprechaun_name}}', leprechaun_name)
        html_content = html_content.replace('{{meaning}}', meaning)
        html_content = html_content.replace('{{date}}', datetime.now().strftime('%B %d, %Y'))
        
        # Generate PDF
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            pdf_path = tmp.name
        
        HTML(string=html_content).write_pdf(pdf_path)
        
        return send_file(
            pdf_path,
            as_attachment=True,
            download_name=f"leprechaun-certificate-{datetime.now().strftime('%Y%m%d')}.pdf",
            mimetype='application/pdf'
        )
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
