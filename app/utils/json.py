"""JSON utilities for the application."""

def model_to_dict(model):
    """Convert a SQLAlchemy model instance to a dictionary.
    
    Args:
        model: A SQLAlchemy model instance
        
    Returns:
        dict: A dictionary representation of the model
    """
    if hasattr(model, '__table__'):
        return {c.name: getattr(model, c.name) for c in model.__table__.columns}
    return model.__dict__

def init_json_encoder(app):
    """Initialize JSON handling for the Flask app.
    
    This is a placeholder function to maintain API compatibility.
    The actual serialization is handled in the route handlers.
    
    Args:
        app: The Flask application instance
    """
    # No longer needed as we're handling serialization in the routes
    pass
