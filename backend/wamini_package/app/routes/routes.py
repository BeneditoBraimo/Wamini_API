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

#-------------------------------------------------------------------------------------
# USER ROUTES
#-------------------------------------------------------------------------------------

@user_bp.route("/register", methods=["POST"])
def register_user():
    "register a new user"
    data = request.get_json()
    if User.filter_by(mobile_number=data.get("mobile_number").first()):
        return jsonify({"error": "Mobile number already registered"}), 409
    
    hashed_pw = generate_password_hash(data.get("password"))

    user = User(
        name = data.get("name"),
        localization = data.get("localization"),
        password = hashed_pw,
        mobile_number=data.get("mobile_number"),
        photo=data.get("photo")
    )

    db.session.add(user)
    db.session.commit()
    return jsonify({"message":"User successfully registered.", "user_id": user.id}), 201