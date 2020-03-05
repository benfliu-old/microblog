#
# Name: Ben Liu
# Filename: config.py
# Description: Config file providing security for the website with a secret passcode
# Citations: Miguel Grinberg Flask Mega-Tutorial - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
#

#imports
import os
basedir = os.path.abspath(os.path.dirname(__file__))

#creates Config class for security
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False