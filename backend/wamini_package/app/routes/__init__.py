"""
__init__.py
-------------------------------------------------------------------------

initializes and registers all route blueprints for Wamini backend API.
"""
import os
from flask import Flask
from flask_cors import CORS

from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from ..models import db
# import blueprints from routes.py

from .routes import (
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
            app (Flask): configured Flask application instance.
    """

    # Load environment variables from backend/wamini_package/.env
    env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    load_dotenv(env_path)

    app = Flask(__name__)
    CORS(app)

    # Basic configurations
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    JWTManager(app)

    # Register Blueprints with URL prefixes already defined in routes.py
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(input_bp)
    app.register_blueprint(transport_bp)
    app.register_blueprint(negotiation_bp)

    return app