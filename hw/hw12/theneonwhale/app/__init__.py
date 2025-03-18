from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from . import routes, auth
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)

    return app

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))
