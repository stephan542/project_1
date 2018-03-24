from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "P@$$W0rd"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://stephan542:Project_1@localhost/UserProfiles"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

UPLOAD_FOLDER = './app/static/images'

app.config.from_object(__name__)
from app import views