#-*-coding:utf-8-*-
from flask import Flask,url_for,request,redirect,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_dropzone import Dropzone
from flask_mail import Mail
from config import config
import sys
sys.path.append("..")
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
dropzone = Dropzone()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_views = 'admin.login'
login_manager.login_views = 'login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    dropzone.init_app(app)
    # from .main import admin
    # app.register_blueprint(admin,url_prefix='/admin')
    return app
