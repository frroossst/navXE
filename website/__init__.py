from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import secrets

db = SQLAlchemy()
DB_NAME = "graphs.db"

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views

    app.register_blueprint(views,url_prefix="/")

    return app