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

### 4. Install dependencies
        pip install -r requirements.txt


