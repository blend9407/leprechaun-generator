"""
Configuration module for Leprechaun Name Generator
Centralizes all configuration values for maintainability
"""

import os
import re

# Application settings
APP_NAME = "Leprechaun Name Generator"
APP_VERSION = "1.0.0"
DEBUG = False  # Set to True for development

# Database settings
DB_FILE = 'names.json'
DB_AUTO_SAVE_INTERVAL = 300  # Auto-save cache every 5 minutes (seconds)

# Rate limiting settings
RATE_LIMIT_DEFAULT = ["100 per hour", "20 per minute"]
RATE_LIMIT_NAME_GENERATION = "10 per minute"
RATE_LIMIT_PDF_GENERATION = "5 per minute"

# Security settings
SECURITY_HEADERS = {
    'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline' https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:;",
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block',
    'Referrer-Policy': 'strict-origin-when-cross-origin'
}

# Input validation
NAME_REGEX = re.compile(r'^[a-zA-Z\s\-\']{1,50}$')

# PDF generation settings
PDF_TEMPLATE_DIR = 'pdf-templates'
ALLOWED_TEMPLATES = ['classic-emerald', 'pot-of-gold', 'rainbow-magic']
PDF_TEMPLATE_FILES = {
    'classic-emerald': 'classic-emerald-template.html',
    'pot-of-gold': 'pot-of-gold-template.html',
    'rainbow-magic': 'rainbow-magic-template.html'
}

# Name generation settings
FIRST_NAMES = [
    'Finnegan', 'Seamus', 'Patrick', 'Liam', 'Connor', 'Aiden', 'Rory', 'Declan',
    'Kieran', 'Brendan', 'Colin', 'Darragh', 'Eamon', 'Fergus', 'Grady', 'Hugh',
    'Ian', 'Jarlath', 'Killian', 'Lorcan', 'Mickey', 'Niall', 'Oisin', 'Padraig',
    'Quinn', 'Rafferty', 'Shane', 'Tadhg', 'Ultan', 'Vaughn'
]

LAST_NAMES = [
    "O'Malley", "Fitzgerald", "O'Brien", "Murphy", "Kelly", "Sullivan",
    "Walsh", "McCarthy", "O'Connor", "Doyle", "Kennedy", "Ryan", "Gallagher",
    "Doherty", "McLoughlin", "O'Donnell", "Murray", "Quinn", "Moore",
    "McGrath", "Burke", "Smith", "White", "Flynn", "Campbell", "Johnston",
    "Brown", "Wilson", "Taylor", "Davis"
]

# Logging settings
LOG_FILE = 'flask_secure.log'
LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Cache settings
CACHE_ENABLED = True
CACHE_MAX_SIZE = 1000  # Maximum cached responses
CACHE_TTL = 300  # Cache time-to-live in seconds
