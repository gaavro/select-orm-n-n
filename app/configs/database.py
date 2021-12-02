from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)

    app.db = db

    # importar models
    from app.models.developer_model import Developer
    from app.models.tech_model import Tech
    from app.models.developer_tech_model import DeveloperTech