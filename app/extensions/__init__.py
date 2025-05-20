"""Extensions package for Flask application.

This package contains all Flask extensions used in the application.
Each extension is initialized in its own module for better organization.
"""

from .database import db, init_db
from .firebase import init_firebase

__all__ = ['db', 'init_db', 'init_firebase']
