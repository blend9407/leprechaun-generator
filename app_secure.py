"""
Leprechaun Name Generator - Secure Flask Application
Enhanced version with configuration management, caching, and template pre-loading
"""

import os
import json
import random
import re
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_talisman import Talisman
from weasyprint import HTML
from werkzeug.middleware.proxy_fix import ProxyFix

# Import configuration and utility modules
import config
import cache
import template_loader

# Initialize Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure random secret key

# Security middleware
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

# Initialize Talisman for security headers
Talisman(
    app,
    content_security_policy=config.SECURITY_HEADERS['Content-Security-Policy'],
    content_security_policy_nonce_in=['script-src'],
    force_https=False,  # Set to True in production
    session_cookie_secure=False,  # Set to True in production
    session_cookie_http_only=True,
    frame_options='DENY',
    referrer_policy='strict-origin-when-cross-origin'
)

# Initialize rate limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=config.RATE_LIMIT_DEFAULT,
    storage_uri="memory://",
    strategy="fixed-window",
    enabled=not config.DEBUG  # Disable in debug mode for development
)

# Initialize database cache and template loader
name_cache = cache.init_cache(config.DB_FILE, config.DB_AUTO_SAVE_INTERVAL)
template_loader_instance = template_loader.init_template_loader(config.PDF_TEMPLATE_DIR)

# Configure PDF generation

# Helper functions
def validate_input(text):
    """Validate user input against regex pattern"""
    if not text or not isinstance(text, str):
        return False
    return bool(config.NAME_REGEX.match(text))

def sanitize_input(text):
    """Sanitize input by stripping and limiting length"""
    if not text:
        return ''
    text = text.strip()
    if len(text) > 50:
        text = text[:50]
    return text

def generate_leprechaun_name(first_name, last_name):
    """Generate a leprechaun name with Irish flair"""
    # Use configuration values
    first_names = config.FIRST_NAMES
    last_names = config.LAST_NAMES

    if not first_name or not last_name:
        # Generate random name
        generated_first = random.choice(first_names)
        generated_last = random.choice(last_names)
        return f"{generated_first} {generated_last}"

    # Create Irish-sounding combination
    irish_prefixes = ['Mc', "O'", 'Fitz']
    irish_suffixes = ['-een', '-y', ' the Lucky', ' of the Emerald Isle']

    # 30% chance to add Irish prefix
    if random.random() < 0.3:
        last_name = random.choice(irish_prefixes) + last_name

    # 20% chance to add Irish suffix
    if random.random() < 0.2:
        last_name = last_name + random.choice(irish_suffixes)

    return f"{first_name} {last_name}"

def save_to_database(name_data):
    """Save generated name to database using cache"""
    try:
        index = name_cache.add(name_data)
        return True, f"Name saved successfully (ID: {index})"
    except Exception as e:
        return False, f"Error saving to database: {str(e)}"

def generate_pdf(name, template_name='classic-emerald'):
    """Generate PDF certificate using pre-loaded templates"""
    try:
        # Validate template name
        if template_name not in config.ALLOWED_TEMPLATES:
            template_name = 'classic-emerald'

        # Get pre-loaded template
        template_content = template_loader_instance.get_template(template_name)
        if not template_content:
            return None, f"Template '{template_name}' not found"

        # Replace placeholders
        html_content = template_content.replace('{{name}}', name)
        html_content = html_content.replace('{{date}}', datetime.now().strftime('%B %d, %Y'))

        # Generate PDF
        pdf = HTML(string=html_content).write_pdf()
        return pdf, None

    except Exception as e:
        return None, f"PDF generation error: {str(e)}"

# Routes
@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
@limiter.limit(config.RATE_LIMIT_NAME_GENERATION)
def generate_name():
    """Generate a leprechaun name"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        # Get and validate inputs
        first_name = data.get('firstName', '')
        last_name = data.get('lastName', '')

        # Sanitize inputs
        first_name = sanitize_input(first_name)
        last_name = sanitize_input(last_name)

        # Validate if provided
        if first_name and not validate_input(first_name):
            return jsonify({'error': 'Invalid first name format'}), 400
        if last_name and not validate_input(last_name):
            return jsonify({'error': 'Invalid last name format'}), 400

        # Generate name
        leprechaun_name = generate_leprechaun_name(first_name, last_name)

        # Prepare data for saving
        name_data = {
            'firstName': first_name if first_name else 'Random',
            'lastName': last_name if last_name else 'Random',
            'leprechaunName': leprechaun_name,
            'timestamp': datetime.now().isoformat(),
            'ip': request.remote_addr
        }

        # Save to database
        success, message = save_to_database(name_data)
        if not success:
            app.logger.warning(f"Failed to save name: {message}")

        return jsonify({
            'leprechaunName': leprechaun_name,
            'saveStatus': 'success' if success else 'warning',
            'saveMessage': message
        })

    except Exception as e:
        app.logger.error(f"Error in generate_name: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/download-pdf', methods=['POST'])
@limiter.limit(config.RATE_LIMIT_PDF_GENERATION)
def download_pdf():
    """Generate and download PDF certificate"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        name = data.get('name', '')
        template = data.get('template', 'classic-emerald')

        # Validate inputs
        if not name or not isinstance(name, str):
            return jsonify({'error': 'Name is required'}), 400

        name = sanitize_input(name)
        if not validate_input(name):
            return jsonify({'error': 'Invalid name format'}), 400

        # Validate template
        if template not in config.ALLOWED_TEMPLATES:
            template = 'classic-emerald'

        # Generate PDF
        pdf_data, error = generate_pdf(name, template)
        if error:
            return jsonify({'error': error}), 500

        # Create response
        response = make_response(pdf_data)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename="leprechaun-certificate-{datetime.now().strftime("%Y%m%d")}.pdf"'

        # Log download
        app.logger.info(f"PDF generated for name: {name}, template: {template}")

        return response

    except Exception as e:
        app.logger.error(f"Error in download_pdf: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/stats')
def stats():
    """Get application statistics"""
    try:
        total_names = name_cache.get_count()

        return jsonify({
            'totalNamesGenerated': total_names,
            'appName': config.APP_NAME,
            'appVersion': config.APP_VERSION,
            'templatesAvailable': config.ALLOWED_TEMPLATES,
            'rateLimits': {
                'nameGeneration': config.RATE_LIMIT_NAME_GENERATION,
                'pdfGeneration': config.RATE_LIMIT_PDF_GENERATION
            }
        })

    except Exception as e:
        app.logger.error(f"Error in stats: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'cache': 'enabled' if config.CACHE_ENABLED else 'disabled',
        'templatesLoaded': len(template_loader_instance.get_all_templates())
    })

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(429)
def ratelimit_handler(error):
    return jsonify({
        'error': 'Rate limit exceeded',
        'message': 'Please wait before making more requests'
    }), 429

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"Internal server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500

# Application startup
if __name__ == '__main__':
    print(f"Starting {config.APP_NAME} v{config.APP_VERSION}")
    print(f"Database cache initialized with {name_cache.get_count()} names")
    print(f"Loaded {len(template_loader_instance.get_all_templates())} PDF templates")
    print(f"Rate limiting: {config.RATE_LIMIT_NAME_GENERATION} for name generation")
    print(f"Security headers: {len(config.SECURITY_HEADERS)} configured")

    # Configure logging
    import logging
    logging.basicConfig(
        filename=config.LOG_FILE if not config.DEBUG else None,
        level=getattr(logging, config.LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Run application
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=config.DEBUG,
        threaded=True
    )
