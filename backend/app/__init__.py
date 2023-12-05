from flask import Flask
from config import Config
from app.routes import init_app
from app.models.setup_models import db
from app.models.setup_models import create_tables

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_app(app)

    db.init_app(app)
    with app.app_context():
        create_tables()

    return app