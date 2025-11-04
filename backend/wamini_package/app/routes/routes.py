"""
routes.py
-------------
This module defines the REST API routes for Wamini platform.

Features:
    - JWT-based athentication (for user signup/login)
    - CRDU operations for User, Products, Inputs, Transports, Negotiations
    - Modular structure using Flask Blueprints
"""

from flask import Blueprint, request, jsonify
from flask import (create_access_token, jwt_required, get_jwt_identity)


from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db, User, Product, Input, Transport, Negotiation

#---------------------------------------------------------------------------------
# Blueprints Declarations
#---------------------------------------------------------------------------------
user_bp = Blueprint("users", __name__, url_prefix="api/v1/users")
product_bp = Blueprint("products", __name__, url_prefix="api/v1/products")
input_bp = Blueprint("inputs", __name__, url_prefix="/api/v1/inputs")
transport_bp = Blueprint("transports", __name__, url_prefix="/api/v1/transports")
negotiation_bp = Blueprint("negotiations", __name__, url_prefix="/api/v1/negotiations")