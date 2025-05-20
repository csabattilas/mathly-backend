from flask import Flask
from dotenv import load_dotenv
import os
from flask_migrate import Migrate
from flask_smorest import Api
from .extensions import db, init_db, init_firebase
from .swagger import configure_api_docs
from .config import configure_cors
from .utils.terminal import COLORS, print_startup_banner, print_routes
from .utils.json import init_json_encoder

migrate = Migrate()

def create_app():
    load_dotenv()

    # Print colorful startup message
    print_startup_banner()

    app = Flask(__name__)
    
    # Register custom JSON encoder to handle SQLAlchemy models
    init_json_encoder(app)
    
    # Load database configuration
    from .config import DatabaseConfig
    app.config.update(DatabaseConfig.get_config())

    # Initialize extensions
    init_db(app)
    migrate.init_app(app, db) 
    init_firebase()

    # Configure CORS - only in development mode
    configure_cors(app)
    
    # Load API configuration and initialize Flask-Smorest
    from .config import ApiConfig
    app.config.update(ApiConfig.get_config())
    
    from .swagger import configure_api_docs
    api = configure_api_docs(app)
    
    # Register routes with Flask-Smorest
    try:
        from .routes.protected import protected_bp
        api.register_blueprint(protected_bp)
    except ImportError as e:
        print(f"{COLORS['RED']}Warning: Could not import protected routes: {e}{COLORS['END']}")
    
    try:
        from .routes.public import public_bp
        api.register_blueprint(public_bp)
    except ImportError as e:
        print(f"{COLORS['RED']}Warning: Could not import public routes: {e}{COLORS['END']}")

    # Print all registered routes
    print_routes(app)
  
    return app
