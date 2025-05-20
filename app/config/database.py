"""Database configuration for the application."""

import os

class DatabaseConfig:
    """Database configuration settings."""
    
    @staticmethod
    def get_config():
        """Get the database configuration.
        
        Returns:
            dict: The database configuration settings
        """
        return {
            "SQLALCHEMY_DATABASE_URI": os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/dbname"),
            "SQLALCHEMY_TRACK_MODIFICATIONS": False
        }
