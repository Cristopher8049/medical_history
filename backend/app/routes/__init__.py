# app/routes/__init__.py
from .home_routes import main_bp

def init_app(app):
    app.register_blueprint(main_bp)