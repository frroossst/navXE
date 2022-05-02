from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS
import secrets

db = SQLAlchemy()
DB_NAME = "graphs.db"

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(16)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://utftpzpmowwrbj:c8043af3092a13f20f7ea6e27e1df4bd4f19a7cac9ff97898174169e4b318ff9@ec2-3-217-113-25.compute-1.amazonaws.com:5432/d8618c3f7auie6"
    db.init_app(app)
    
    CORS(app,resources={r'/*' : {'origins' : '*'}})
    
    from .views import views

    app.register_blueprint(views,url_prefix="/")

    return app