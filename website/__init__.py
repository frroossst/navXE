from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
import secrets
import os

db = SQLAlchemy()
DB_NAME = "graphs.db"

def create_app():

    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = secrets.token_hex(16)
  
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")

    db.init_app(app)
    
    CORS(app,resources={r'/*' : {'origins' : '*'}})
    
    from .views import views

    app.register_blueprint(views,url_prefix="/")

    return app