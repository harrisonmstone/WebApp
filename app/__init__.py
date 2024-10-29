from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

from .routes import bp

def create_app():
    # Create variable and load configuration from config.py
    app = Flask(__name__)
    app.config.from_object('config')

    # Initialize database
    # db.init_app(app)

    # Register flask project blueprint
    # from .views import main as main_blueprint
    app.register_blueprint(bp)

    return app