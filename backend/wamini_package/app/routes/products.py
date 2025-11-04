"""
products.py
------------
Contains routes for managing Product resources via REST API endpoints.
"""

from flask import Blueprint, jsonify, request
from ..models import db, Product

# Create Blueprint
products_bp = Blueprint('products', __name__, url_prefix='/api/products')

@products_bp.route('/', methods=['GET'])
def get_products():
    """Retrieve all published products."""
    products = Product.query.all()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "quantity": p.quantity,
        "price": p.price,
        "publish_date": p.publish_date.isoformat(),
        "user_id": p.user_id
    } for p in products]), 200
