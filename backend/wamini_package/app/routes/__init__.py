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