"""
models.py
----------
This module defines the database schema for the Wamini API using SQLAlchemy ORM.
It includes the following main entities:

- User: Represents users of the platform.
- Product: Represents agricultural products published by users.
- Input: Represents agricultural inputs (e.g., fertilizers, seeds).
- Transport: Represents transport services offered by users.
- Negotiation: Represents communication or message exchanges between users.

Each model includes relationship mappings to maintain referential integrity.
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
        location (str): user's location.
        phone (str): Phone number.
        password (str): Hashed password for authentication.
    """

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Cplumn(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(20))
    password = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        """Serialize User object into a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'mobile_number': self.phone,
            'location': self.location,
            'password': self.password,
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
