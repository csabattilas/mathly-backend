"""API documentation setup using Flask-Smorest."""

from flask_smorest import Api

def configure_api_docs(app):
    """Initialize Flask-Smorest for API documentation.
    
    This function initializes the Flask-Smorest API object.
    The configuration is loaded from ApiConfig in app/config/api.py.
    The actual registration of blueprints happens in app/__init__.py.
    
    Args:
        app: The Flask application instance
        
    Returns:
        Api: The initialized Flask-Smorest API object
    """
    # Initialize and return the Flask-Smorest API object
    return Api(app)
