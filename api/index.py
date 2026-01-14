# Simpler approach: Use Flask's built-in WSGI
from app_secure import app

# Export the Flask app as WSGI application
# Vercel will use this as the handler
application = app
