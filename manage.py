#-*-coding:utf-8-*-
from app import db,create_app
from app.models import User,Role,T1,T2,T3,Book,Depot,Template
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
import os
from threading import Thread
from sql_sendmail import send_lend_mail,get_to_list
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
from app.views.auth import auth_bp 
from app.views.main import main_bp
from app.views.user import user_bp
from app.views.depot import depot_bp
from app.views.book import book_bp
from app.emails import send_mail
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)
app.register_blueprint(depot_bp)
app.register_blueprint(book_bp)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role,T1=T1,T2=T2,T3=T3,Book=Book,Depot=Depot,Template=Template)
manager.add_command("shell",Shell(make_shell_context))
if __name__ == '__main__':
    t1 = Thread(target=manager.run)
    # t2 = Thread(target=send_lend_mail,args=("test","test"))
    # print("get_to_list()=",get_to_list())
    threadlist = []
    threadlist.append(t1)
    # threadlist.append(t2)
    for i in threadlist:
        i.start()