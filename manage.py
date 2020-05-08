#-*-coding:utf-8-*-
"""
app程序的路口文件
"""
import os
import sys,smtplib
from email.mime.text import MIMEText
from email.header import Header
from apscheduler.schedulers.background import BackgroundScheduler
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.views.auth import auth_bp
# from app.emails import send_mail
from app.views.book import book_bp
from app.views.depot import depot_bp
from app.views.user import user_bp
from app.views.main import main_bp
from app.views.record import record_bp
from app import db, create_app
from app.models import User, Role, T1, T2, T3, Book, Depot, Template, Record
# from threading import Thread
from sql_sendmail import get_to_list,get_books_list,MAIL
# from datetime import datetime

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)
app.register_blueprint(depot_bp)
app.register_blueprint(book_bp)
app.register_blueprint(record_bp)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    """
    shell
    """
    return dict(app=app, db=db, User=User, Role=Role, T1=T1, T2=T2, T3=T3, Book=Book, Depot=Depot, Template=Template)

manager.add_command("shell", Shell(make_shell_context))

# 发送催还邮件


def send_email(to_addr, msg):
    """
    封装smtplib库邮件发送邮件相关代码
    """
    server = smtplib.SMTP()
    server.connect(MAIL['host'])
    server.login(MAIL['user'], MAIL['passwd'])
    server.sendmail(MAIL['user'], to_addr, msg.as_string())
    server.close()

def send_lend_mail(sub="[系统邮件,勿回]物品归还提醒"):
    """
    执行邮件发送动作
    """
    to_list = get_to_list()
    book_to_list = get_books_list()
    if to_list != []:
        # 清除邮箱列表可能存在
        # if None in to_list:
        #     for i in to_list:
        #         if i is None:
        #             to_list.remove(i)
        for i in to_list:
            content1 = "%s,您借用的%s已到归还时间，请及时归还给实验室管理员。" % (
                i['username'], i['product_name'])
                
            print('88', type(content1))
            msg = MIMEText(content1, _subtype='plain', _charset='utf-8')
            msg['Subject'] = Header(sub, "utf-8")
            msg['From'] = MAIL['user']
            msg['To'] = i['usermail']
            # print('msg=',msg)
            send_email(to_addr=i['usermail'], msg=msg)
    # time.sleep(20)
    if book_to_list != []:
        for i in book_to_list:
            content = "%s,您借用的%s已到归还时间，请及时归还给实验室管理员。" % (
                i['username'], i['bookname'])
            msg = MIMEText(
                content, _subtype='plain', _charset='utf-8')
            msg['Subject'] = Header(sub, "utf-8")
            msg['From'] = MAIL['user']
            msg['To'] = i['usermail']
            send_email(to_addr=i['usermail'], msg=msg)

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_lend_mail, 'cron', day_of_week='mon-fri', hour=11, minute=22)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    scheduler.start()
    # send_lend_mail(sub='测试')
    try:
        manager.run()
    except (KeyboardInterrupt,SystemExit):
        scheduler.shutdown()
        print('Exit The Job!')
