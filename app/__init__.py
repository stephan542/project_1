from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "P@$$W0rd"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udpnroqnifkdui:30565a11c7ad9fdba7f63ec81fb3e91ed508231508a8734f8844b8fab2a6cbbf@ec2-107-21-126-193.compute-1.amazonaws.com:5432/d1afs04f48a935'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

UPLOAD_FOLDER = './app/static/images'

app.config.from_object(__name__)
from app import views