"""
models.py

This module defines all SQLAlchemy ORM models for the Wamini API backend.

Models:
    - User: Represents platform users (farmers, buyers, transporters, etc.)
    - Product: Represents agricultural products listed by users.
    - Input: Represents agricultural inputs for sale (e.g., fertilizer, seeds).
    - Transport: Represents available transport services for logistics.
    - Negotiation: Represents ongoing or completed trade negotiations.
    - Message: Represents communication between users.

Each model includes:
    - SQLAlchemy column definitions
    - Relationship fields via foreign keys
    - A `to_dict()` method for easy JSON serialization
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


# Initialize SQLAlchemy intance (to be bound in app factory)
db = SQLAlchemy()


class User(db.Model):
    """
    Represents a registered user in the Wamini platform.

    Attributes:
        id (int): Primary key
        name (str): user's first name.
        phone (str): Phone number.
        password (str): Hashed password for authentication.
    """

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Cplumn(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        """Serialize User object into a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone': self.phone,
            'role': self.role,
            'join_date': self.join_date.isoformat()
        }
    

class Product(db.Model):
    """
    Represents a product listed by a user for sale.

    Attributes:
        id (int): Primary key.
        name (str): Product name.
        price (float): Product price.
        category (str): Product category (e.g., 'grains', 'vegetables').
        publish_date (datetime): Timestamp when the product was posted.
        user_id (int): Foreign key referencing the seller (User).
    """

    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
