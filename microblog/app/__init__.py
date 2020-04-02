#
# Name: Ben Liu
# Filename: __init__.py
# Description: __init__.py file, makes the directory "app" into a module
# Citations: Miguel Grinberg Flask Mega-Tutorial - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
#

#imports
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#initializes important objects using the flask-integrated modules above
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
