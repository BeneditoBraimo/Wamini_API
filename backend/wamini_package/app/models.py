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
    Represents a registered user in the Wamini system.

    Attributes:
        id (int): Primary key identifier.
        name (str): Full name of the user.
        localization (str): User's geographic location.
        password (str): Hashed password for authentication.
        mobile_number (str): Unique mobile contact of the user.
        photo (str): Optional path or URL to user's profile photo.
    Relationships:
        products (list[Product]): Products published by this user.
        inputs (list[Input]): Agricultural inputs published by this user.
        transports (list[Transport]): Transport services published by this user.
        negotiations (list[Negotiation]): Negotiations initiated by this user.
    """
    
    

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
