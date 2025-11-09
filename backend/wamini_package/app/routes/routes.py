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
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity)


from datetime import datetime, timedelta, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import db, User, Product, Input, Transport, Negotiation, Message

#---------------------------------------------------------------------------------
# Blueprints Declarations
#---------------------------------------------------------------------------------
user_bp = Blueprint("users", __name__, url_prefix="/api/v1/users")
product_bp = Blueprint("products", __name__, url_prefix="/api/v1/products")
input_bp = Blueprint("inputs", __name__, url_prefix="/api/v1/inputs")
transport_bp = Blueprint("transports", __name__, url_prefix="/api/v1/transports")
negotiation_bp = Blueprint("negotiations", __name__, url_prefix="/api/v1/negotiations")

#-------------------------------------------------------------------------------------
# USER ROUTES
#-------------------------------------------------------------------------------------

@user_bp.route("/register", methods=["POST"], endpoint='user_register')
def register_user():
    """Register a new user safely"""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    # Ensure required fields exist
    required_fields = ["name", "mobile_number", "password"]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"'{field}' is required"}), 400

    # Check if mobile number is already registered
    if User.query.filter_by(mobile_number=data.get("mobile_number")).first():
        return jsonify({"error": "Mobile number already registered"}), 409

    # Hash password
    hashed_pw = generate_password_hash(data["password"])

    # Create user
    user = User(
        name=data["name"],
        localization=data.get("localization"),
        password=hashed_pw,
        mobile_number=data["mobile_number"],
        photo=data.get("photo")
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User successfully registered.", "user_id": user.id}), 201


@user_bp.route("/login", methods=["POST"], endpoint='user_login')
def login_user():
    """Authenticate and return access token."""
    data = request.get_json()
    user = User.query.filter_by(mobile_number=data.get("mobile_number")).first()
    if not user or not check_password_hash(user.password, data.get("password")):
        return jsonify({"error": "Invalid credentials"}), 401
    
    expires = timedelta(hours=24)
    access_token = create_access_token(identity=user.id, expires_delta=expires)

    return jsonify({
        "access_token": access_token,
        "user": {"id":user.id, "name": user.name}
    }), 200

@user_bp.route("/profile", methods=["GET"], endpoint='profile_get')
@jwt_required
def get_profile():
    """Retrieve logged-in user's profile"""
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify({
        "id": user.id,
        "name": user.name,
        "localization": user.localization,
        "mobile_number": user.mobile_number,
        "photo": user.photo
    }), 200


#------------------------------------------------------------------------------------------
#   PRODUCT ROUTES
#------------------------------------------------------------------------------------------

@product_bp.route("", methods=["POST"], endpoint='product_get')
@jwt_required
def add_product():
    """Publish a new product."""
    user_id = get_jwt_identity()
    data = request.get_json()

    product = Product(
        name=data["name"],
        quantity=data["quantity"],
        price=data["price"],
        photo=data["photo"],
        user_id=user_id
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product added successfully", "product_id": product.id}), 201


@product_bp.route("", methods=["GET"], endpoint='product_list')
def list_products():
    """List all products."""
    products = Product.query.all()

    result = [{
        "id": p.id,
        "name": p.price,
        "quantity": p.quantity,
        "publish_date": p.publish_date,
        "user_id": p.user_id,

    } for p in products]

    return jsonify(result), 200

@product_bp.route("/<int:product_id>", methods=["DELETE"], endpoint='product_delete')
@jwt_required
def delete_product(product_id):
    """Delete a product (only by the owner)"""
    user_id = get_jwt_identity()
    product = Product.query.get_or_404(product_id)

    if product.user_id != user_id:
        return jsonify({"error": "unauthorized"}), 403
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted."}), 200


#---------------------------------------------------------------------------
# INPUT ROUTES
#---------------------------------------------------------------------------

@input_bp.route("", methods=["POST"], endpoint='input_add')
@jwt_required()
def add_input():
    """Add an agricultural Input."""
    user_id = get_jwt_identity()
    data = request.get_json()

    new_input = Input(
        name=data["name"],
        quantity=data["quantity"],
        price=data["price"],
        photo=data["photo"],
        user_id=user_id
    )

    db.session.add(new_input)
    db.session.commit()

    return jsonify({"message": "Input added successfully", "input_id": new_input.id}), 201


@input_bp.route("", methods=["GET"], endpoint='inputs_list')
def list_inputs():
    """List all agricultural inputs"""

    inputs = Input.query.all()

    result = [{
        "id":i.id,
        "name":i.name,
        "price": i.price,
        "quantity": i.quantity,
        "publish_date": i.publish_date,
        "user_id": i.user_id
    } for i in inputs]

    return jsonify(result), 200


# -----------------------------------------------------------------------------------
# TRANSPOST ROUTES
# -----------------------------------------------------------------------------------

@transport_bp.route("", methods=["POST"], endpoint='transport_add')
@jwt_required()
def add_transport():
    """Add a transport service"""

    user_id = get_jwt_identity()
    data = request.get_json()

    transport = Transport(
        transport_type=data["transport_type"],
        name=data["name"],
        price_per_km=data["price_per_km"],
        photo=data.get("photo"),
        user_id=user_id
    )

    db.session.add(transport)
    db.session.commit()

    return jsonify({
        "message": "Transport dervice added successfully",
        "transport_id": transport.id
    }), 201


@transport_bp.route("", methods=["GET"], endpoint='transport_list')
def list_transports():
    """List all transport services."""
    transports = Transport.query.all()
    result = [{
        "id": t.id,
        "transport_type": t.transport_type,
        "name": t.name,
        "price_per_km": t.price_per_km,
        "user_id": t.user_id
    } for t in transports]

    return jsonify(result), 200


# ----------------------------------------------------------------------------
# NEGOTIATION ROUTES
# ----------------------------------------------------------------------------

@negotiation_bp.route("", methods=["POST"], endpoint='negotiation_start')
@jwt_required()
def start_negotiation():
    """Start a negotiation related to a product/input/transport"""

    user_id = get_jwt_identity()
    data = request.get_json()

    negotiation = Negotiation(
        user_id=user_id,
        product_id=data.get("product_id"),
        input_id=data.get("input_id"),
        transport_id=data.get("transport_id"),
        messages=data.get("messages", [])
    )

    db.session.add(negotiation)
    db.session.commit()

    return jsonify({"message": "megotiation started", "negotiation_id": negotiation.id}), 201



@negotiation_bp.route("", methods=["GET"], endpoint='negotiations_list')
@jwt_required()
def list_negotiations():
    """List all negotiations of the logged-in user."""

    user_id = get_jwt_identity()
    negotiations = Negotiation.query.filter_by(user_id=user_id).all()

    result = [{
        "id": n.id,
        "messages": n.messages,
        "created_at": n.created_at,
        "product_id": n.product_id,
        "input_id": n.input_id,
        "transport_id": n.transport_id
    } for n in negotiations]

    return jsonify(result), 200


# --------------------------------------------------------------------------------------------
# MESSAGE ROUTES
# --------------------------------------------------------------------------------------------

@negotiation_bp.route("/<int:negotiation_id>/messages", methods=["POST"], endpoint='message_send')
@jwt_required()
def send_message(negotiation_id):
    """
        Send a message within a negotiation thread.
        Requires authentication. The sender must be a registered user.
    """

    user_id = get_jwt_identity()
    data = request.get_json()

    negotiation = Negotiation.query.get_or_404(negotiation_id)

    message = Message(
        sender_id=user_id,
        negotiation_id=negotiation.id,
        body=data.get("body"),
        timestamp=datetime.now(timezone.utc)
    )

    db.session.add(message)
    db.session.commit()

    return jsonify({
        "message": "Message successfully sent.",
        "data": {
            "id": message.id,
            "body": message.body,
            "sender_id": user_id,
            "negotiation_id": negotiation_id,
            "timestamp": message.timestamp.isoformat()
        }
    }), 201



@negotiation_bp.route("/<int:negotiation_id>/messages", methods=["GET"], endpoint='messages_get')
@jwt_required()
def get_messages(negotiation_id):
    """
        Retrieve all messages within a negotiation.
        Only participants can participate in the thread.
    """

    user_id = get_jwt_identity()
    negotiation = Negotiation.query.get_or_404(negotiation_id)

    messages = Message.query.filter_by(negotiation_id=negotiation.id).order_by(Message.timestamp.asc()).all()

    result = [{
        "id": m.id,
        "sender_id": m.sender_id,
        "body": m.body,
        "timestamp": m.timestamp.isoformat()
    } for m in messages]

    return jsonify(result), 200