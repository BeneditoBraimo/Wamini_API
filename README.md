# Wamini Backend API

This is the backend API for **Wamini**, a platform for agricultural products, inputs, transports, and negotiations.  
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
        set FLASK_APP=wamini_package.run
        set FLASK_ENV=development




