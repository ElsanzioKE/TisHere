from flask import Flask
from .config import Config
from .extensions import db, migrate
from .models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(user_bp)
    # app.register_blueprint(post_bp)

    return app
