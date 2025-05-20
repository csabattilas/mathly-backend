"""Database extension setup."""

from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy instance
db = SQLAlchemy()

def init_db(app):
    """Initialize the SQLAlchemy database with the Flask app.
    
    Args:
        app: Flask application instance
    """
    db.init_app(app)
