"""CORS configuration for the application."""

import os
from flask import Flask
from flask_cors import CORS

def configure_cors(app: Flask):
    """Configure CORS for the application.
    
    CORS is only enabled in development mode.
    In production, CORS is disabled for security.
    
    Args:
        app: The Flask application instance
    """
    env = os.getenv("FLASK_ENV", "development")
    if env == "development":
        CORS(app, resources={
            r"/*": {
                "origins": ["http://localhost:4200"],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"]
            }
        })
        app.logger.info("CORS enabled for development")
    else:
        app.logger.info("CORS disabled (production mode)")
