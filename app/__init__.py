from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "P@$$W0rd"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kbozojlxmjyrcq:ffe9f82b655bc67113811e363ae89b89b52cf83d7a77fa0b1adc813fbb1162e4@ec2-107-20-151-189.compute-1.amazonaws.com:5432/d7o1o5i55rofj7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

UPLOAD_FOLDER = './app/static/images'

app.config.from_object(__name__)
from app import views