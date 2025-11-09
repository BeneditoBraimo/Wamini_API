# Wamini Backend API - Project Overview
# Purpose

The Wamini backend API is a RESTful service built with Flask that powers an agricultural marketplace platform.
It enables users to register, publish products and inputs, offer transport services, and negotiate deals — all through secure, token-based communication.
  
The API is built using **Flask**, **Flask-SQLAlchemy**, **Flask-Migrate**, and **JWT authentication**.

---

## Features

- User registration and login with JWT authentication
- CRUD operations for:
  - Products
  - Inputs
  - Transport services
- Negotiation and messaging system
- Modular structure using Flask Blueprints
- PostgreSQL database backend

---

## Prerequisites

- Python 3.10+
- PostgreSQL
- Git
- pip (Python package manager)


---

## Setup Instructions

### 1. Clone the repository

      git clone <repository_url>
      cd Wamini_API/backend

### 2. Creating a virtual environment
      python -m venv venv

#### Activate it
##### Windows:
        venv\Scripts\activate
##### Linux/macOS:
        source venv/bin/activate

### 3. Install dependencies
        pip install -r requirements.txt

### 4. Set up environment variables
Create .env file in   "wamini_package/"  with the following structure:
      
      # Secret key for Flask sessions and JWT
      SECRET_KEY=your_secret_key_here

      # Database connection URL for SQLAlchemy
      SQLALCHEMY_DATABASE_URI=postgresql://<username>:<password>@<host>:<port>/<database_name>

      # JWT secret key
      JWT_SECRET_KEY=your_jwt_secret_here

      # Optional: Enable Flask debug mode
      FLASK_DEBUG=True


### 5. Set up Flask app environment variables (Windows CMD):
        set FLASK_APP=run
        set FLASK_ENV=development

#### Initialize the database
      flask db init
      flask db migrate -m "Initial migration"
      flask db upgrade

This will create the database tables as defined in models.py script.

### 6. Run the API
      flask run

The API will run at
          http://127.0.0.1:5000
      

### 7. Main Features and endpoints

| **Module**          | **Route Prefix**                     | **Key Endpoints**                               | **Description**                                                         |
| ------------------- | ------------------------------------ | ----------------------------------------------- | ----------------------------------------------------------------------- |
| **Users**     | `/api/v1/users`                      | `POST /register`, `POST /login`, `GET /profile` | Handles user registration, authentication (JWT), and profile retrieval. |
|  **Products**     | `/api/v1/products`                   | `POST /`, `GET /`, `DELETE /<id>`               | CRUD operations for agricultural product listings.                      |
|  **Inputs**       | `/api/v1/inputs`                     | `POST /`, `GET /`                               | CRUD operations for agricultural inputs (e.g., seeds, fertilizers).     |
| **Transports**   | `/api/v1/transports`                 | `POST /`, `GET /`                               | Adds and lists available transport services.                            |
| **Negotiations** | `/api/v1/negotiations`               | `POST /`, `GET /`                               | Starts and lists negotiation threads between users.                     |
| **Messages**     | `/api/v1/negotiations/<id>/messages` | `POST /`, `GET /`                               | Handles messaging within a negotiation thread.                          |



