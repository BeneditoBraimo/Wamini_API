"""
__init__.py
-------------------------------------------------------------------------

initializes and registers all route blueprints for Wamini backend API.
"""

from flask import Flask
from flask_cors import CORS

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

    app = Flask(__name__)
    CORS(app)

    # Resister Blueprints with URL prefixes already defined in routes.py
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(input_bp)
    app.register_blueprint(transport_bp)
    app.register_blueprint(negotiation_bp)

    return app