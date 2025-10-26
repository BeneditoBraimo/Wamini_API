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