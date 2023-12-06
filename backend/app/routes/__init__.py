from .get_patient import get_bp
from .register import post_bp

def init_app(app):
    app.register_blueprint(get_bp)
    app.register_blueprint(post_bp)
    