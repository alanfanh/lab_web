#-*-coding:utf-8-*-
import pymysql
import smtplib,time
from email.mime.text import MIMEText
import datetime
config = {
'host':'127.0.0.1',
'port':3306,
'user':'root',
'passwd':'',
'db':'test',
'charset':'utf8',
'cursorclass':pymysql.cursors.DictCursor
}
connect = pymysql.Connect(**config)
cursor = connect.cursor()
print('cursor=',cursor)

def get_admin_mail():
    sql = "SELECT email FROM users where username='%s' "
    data = "admin"
    cursor.execute(sql %data)
    email = [ i['email'] for i in cursor.fetchall()]
    return email
    
    
def get_t1s_info():
    sql = "SELECT username,usermail,back_time FROM t1s"
    cursor.execute(sql)
    info = [i for i in cursor.fetchall()]
    connect.commit()
    return info
    
def get_t2s_info():
    sql = "SELECT username,usermail,back_time FROM t2s"
    cursor.execute(sql)
    info = [i for i in cursor.fetchall()]
    print("t2_info=",info)
    connect.commit()
    return info  

def get_t3s_info():
    sql = "SELECT username,usermail,back_time FROM t3s"
    cursor.execute(sql)
    info = [i for i in cursor.fetchall()]
    connect.commit()
    return info  

def get_books_info():
    sql = "SELECT username,usermail,back_time FROM books "
    cursor.execute(sql)
    info = [i for i in cursor.fetchall()]
    connect.commit()
    return info

def get_user_info():
        info = []
        info1 = get_t1s_info()
        info2 = get_t2s_info()
        info3 = get_t3s_info()
        info4 = get_books_info()
        info.extend(info1)
        info.extend(info2)
        info.extend(info3)
        info.extend(info4)
        return info
  
def get_to_list():
    info = get_user_info()
    print("info=",info)
    to_list = []
    for i in info:
        if i['username'] != None:
            print(i['username'])
            back_time = i['back_time']
            today = datetime.date.today()
            print((back_time-today).days)
            if (back_time-today).days <=2:
                to_list.append(i['usermail'])
    to_list = list(set(to_list))
    print("to_list=",to_list)
    return to_list
        
# 发送催还邮件
def send_lend_mail(sub,content):
    while True:
        cursor = connect.cursor()
        to_list =  get_to_list()
        if to_list != []:
            # 邮箱列表清除None元素
            if None in to_list:
                for i in to_list:
                    if i == None:
                        to_list.remove(i)
            mail_host = "smtp.163.com"
            mail_user = get_admin_mail()
            print(mail_user)
            mail_pass = "zlp308"
            me=mail_user[0]
            msg = MIMEText(content, _subtype='plain', _charset='utf-8')
            msg['Subject'] = sub
            msg['From'] = me
            msg['To'] = ";".join(to_list)
            server = smtplib.SMTP()
            server.connect(mail_host)
            server.login(me,mail_pass)
            server.sendmail(me,to_list,msg.as_string())
            server.close()
        time.sleep(20)