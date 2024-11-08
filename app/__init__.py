from flask import Flask
from .auth import auth_bp, login_manager
from .routes import bp
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

def create_app():
    # Create variable and load configuration from config.py
    app = Flask(__name__)
    app.config.from_object('config')

    app.secret_key = "supersecretkey"

    login_manager.init_app(app)
    # Initialize database
    # db.init_app(app)

    # Register flask project blueprint
    # from .views import main as main_blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(bp)

    return app


# from datetime import timedelta

# app.config['SESSION_PERMANENT'] = True
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)