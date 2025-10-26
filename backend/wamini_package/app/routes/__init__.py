from flask import Flask
from flask_cors import CORS
from .routes.main_routes import main

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Register Blueprints
    app.register_blueprint(main)
    
    return app