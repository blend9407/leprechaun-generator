#!/bin/bash
# Deployment script for Leprechaun Name Generator

echo "Deploying Leprechaun Name Generator..."

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export FLASK_APP=app_secure.py
export FLASK_ENV=production
export SECRET_KEY=$(openssl rand -hex 32)

# Run with gunicorn for production
if command -v gunicorn &> /dev/null; then
    echo "Starting with gunicorn..."
    gunicorn --bind 0.0.0.0:5000 --workers 4 app_secure:app
else
    echo "Starting with Flask development server..."
    python app_secure.py
fi
