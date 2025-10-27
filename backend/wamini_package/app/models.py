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
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    localization = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)
    mobile_number = db.Column(db.String(20), unique=True, nullable=False)
    photo = db.Column(db.String(255))

    # Relationships
    products = db.relationship('Product', backref='user', lazy=True)
    inputs = db.relationship('Input', backref='user', lazy=True)
    transports = db.relationship('Transport', backref='user', lazy=True)
    negotiations = db.relationship('Negotiation', backref='user', lazy=True)

    def __repr__(self):
        return f"<User id={self.id} name={self.name!r}>"


    

class Product(db.Model):
    """
    Represents a product published by a user for sale.

    Attributes:
        id (int): Primary key identifier.
        name (str): Product name.
        quantity (int): Quantity available.
        price (float): Unit price.
        publish_date (datetime): Date and time of product publication.
        photo (str): Optional product image (path or URL).
        user_id (int): Foreign key linking to the publishing user.
    """

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)
    photo = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Product id={self.id} name={self.name!r} price={self.price}>"


class Input(db.Model):
    """
    Represents an agricultural input published by a user.

    Attributes:
        id (int): Primary key identifier.
        name (str): Input name (e.g., seeds, fertilizer).
        quantity (int): Available quantity.
        price (float): Unit price.
        publish_date (datetime): Date and time of publication.
        photo (str): Optional input image (path or URL).
        user_id (int): Foreign key linking to the publishing user.
    """

    __tablename__ = 'inputs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)
    photo = db.Column(db.String(255))



class Transport(db.Model):
    """
    Represents a transport service offered by a user.

    Attributes:
        id (int): Primary key identifier.
        type (str): Vehicle type (e.g., Moto Bike, Mini Truck, Truck).
        name (str): Vehicle or service name.
        price_per_km (float): Price charged per kilometer.
        publish_date (datetime): Date and time of publication.
        photo (str): Optional vehicle image (path or URL).
        user_id (int): Foreign key linking to the publishing user.
    """

    __tablename__ = 'transports'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    price_per_km = db.Column(db.Float, nullable=False)
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)
    photo = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Transport id={self.id} type={self.type!r} rate={self.price_per_km}/km>"

