# backend/wamini_package/init_db.py

import os
from wamini_package.app import create_app
from wamini_package.app.models import db

# Cria a instância do Flask
app = create_app()

# Inicializa todas as tabelas definidas nos models
with app.app_context():
    db.create_all()
    print("All tables have been created successfully!")
