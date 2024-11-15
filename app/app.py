from flask import Flask
from .models import db, User
from .routes import bp
from config import Config
from flask_login import LoginManager

def create_app():
    # Create variable and load configuration from config.py
    app = Flask(__name__)
    app.config.from_object(Config)

    #Initialize database
    db.init_app(app)

    #Initialize Login Manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    #User loader callback for Flask-login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register flask project blueprint
    app.register_blueprint(bp)

    # Create tables in the database (only if they don't exist)
    with app.app_context():
        db.create_all()

    return app

