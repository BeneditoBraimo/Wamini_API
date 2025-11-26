"""
__init__.py
-------------------------------------------------------------------------

Initializes and registers all route blueprints for Wamini backend API.
Compatible with Render Free deployment. Automatically creates tables on first request.
"""

import os
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from wamini_package.app.models import db

# Import blueprints from routes
from wamini_package.app.routes.routes import (
    user_bp, 
    product_bp,
    input_bp,
    transport_bp,
    negotiation_bp
)

def create_app():
    """
    Application factory that initializes Flask app and registers all route blueprints.
    
    Returns:
        app (Flask): Configured Flask application instance.
    """

    app = Flask(__name__)
    CORS(app)

    # Load environment variables from .env only in development
    if os.getenv("FLASK_ENV") == "development":
        from dotenv import load_dotenv
        env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
        load_dotenv(env_path)

    # Basic configurations
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # Use Render external DB URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    JWTManager(app)
    migrate = Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(input_bp)
    app.register_blueprint(transport_bp)
    app.register_blueprint(negotiation_bp)

    # Automatically create all tables on the first request (works in Render Free)
    @app.before_first_request
    def create_tables():
        db.create_all()
        print("All tables created successfully!")

    return app
