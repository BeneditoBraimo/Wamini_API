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
        surname (str): user's surname.
        email (str): Unique email address (used for login).
        phone (str): Phone number.
        password (str): Hashed password for authentication.
        role (str): Defines the user's role (e.g., 'farmer', 'buyer', 'transporter').
        join_date (datetime): Date the user joined (default = current time).
    """

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), default='farmer')
    join_date = db.Column(db.DateTime, default=datetime.now(datetime.timetz))

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