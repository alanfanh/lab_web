# -*-coding:utf-8-*-
import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Operations:
    CONFIRM = 'confirm'
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    USER_PER_PAGE = 20
    MAIN_PER_PAGE = 20
    DEPOT_PER_PAGE = 20
    BOOK_PER_PAGE = 20
    UPLOAD_PATH = os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = set(['xls', 'xlsx'])
    DOWNLOAD_PATH = os.path.join(basedir, 'downloads')
    MAIL_SERVER = 'smtp.tenda.com'
    MAIL_PORT = 25
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = (MAIL_USERNAME)
    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/test'
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/test'
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
