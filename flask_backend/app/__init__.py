from flask import Flask
from .config import Config
from .extensions import db, migrate
from .models import *
from flask_cors import CORS
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .routes.auth_routes import auth_bp
        from .routes.posts import posts_bp
        from .routes.user import user_bp
        app.register_blueprint(user_bp)
        app.register_blueprint(auth_bp, url_prefix='/api/auth')
        app.register_blueprint(posts_bp)

        db.create_all()

    return app