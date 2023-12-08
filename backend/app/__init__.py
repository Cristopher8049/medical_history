from flask import Flask
from config import Config
from flask_cors import CORS  
from extensions import db
from app.models.setup_models import create_tables
from app.routes.get_patient import get_bp
from app.routes.register import post_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)
    

    with app.app_context():
        create_tables()
        
    app.register_blueprint(get_bp)
    app.register_blueprint(post_bp)

    return app
