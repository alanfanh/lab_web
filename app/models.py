#-*-coding:utf-8-*-
from flask_login import LoginManager,login_user,logout_user,UserMixin,login_required,AnonymousUserMixin
from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
#角色表
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')
    @staticmethod
    def insert_roles():
        roles = {
            'User':(Permission.QUERY,True),
            'Administrator':(0xff,False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

#权限表
class Permission:
    ADD = 0x01
    EDIT = 0x02
    DEL = 0x04
    QUERY = 0x08
    ADMINISTRATOR = 0x80

#用户表
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,nullable=False,index=True)
    username = db.Column(db.String(64),unique=True,nullable=False,index=True)
    password_hash= db.Column(db.String(256),nullable=False)
    email = db.Column(db.String(64),nullable=True,index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __init__(self,name,username):
        # super(User,self).__init__(**kwargs)
        self.name = name
        self.username =username
        if self.role is None:
            if self.username == "admin":
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)
    def get_id(self):
        return self.id
    def __repr__(self):
        return '<User %r>' %self.name
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def can(self,permission):
        return self.role is not None and (self.role.permissions & permission) == permission
    def is_administrator(self):
        return self.can(Permission.ADMINISTRATOR)


class AnonymousUser(AnonymousUserMixin):
    def can(self,permission):
        return False
    def is_administrator(self):
        return False
login_manager.anonymous_user = AnonymousUser
      

# t1_depot = db.Table('t1_depot',
                                            # db.Column('t1_id',db.Integer,db.ForeignKey('t1s.sign'),primary_key=True),
                                            # db.Column('depot_id',db.Integer,db.ForeignKey('depots.id'),primary_key=True)
# ) 
       
# 竞品     
class T1(db.Model):
    __tablename__ = 't1s'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),index=True)
    assetnumber = db.Column(db.String(255),unique=True,index=True)
    product_name = db.Column(db.String(255),index=True)
    model_name = db.Column(db.String(255),index=True)
    numbers = db.Column(db.Integer)
    position = db.Column(db.String(255),index=True)
    entertime = db.Column(db.Date,default=datetime.now,nullable=False)
    status = db.Column(db.String(255))
    username = db.Column(db.String(64),index=True,nullable=True)
    usermail = db.Column(db.String(64),nullable=True)
    lend_time = db.Column(db.Date,default=datetime.now,nullable=True)
    lend_numbers = db.Column(db.Integer,nullable=True)
    back_time = db.Column(db.Date,default=datetime.now,nullable=True)
    remark = db.Column(db.String(64))
    profit_loss = db.Column(db.String(64))
    # depots = db.relationship('Depot',secondary= 't1_depot',backref = db.backref('t1s'))
    # sign = db.Column(db.Integer,default=1,index=True)
    def __init__(self,**kwargs):
        super(T1,self).__init__(**kwargs)
        
     
        
#固定资产   
class T2 (db.Model):
    __tablename__ = 't2s'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),index=True)
    assetnumber = db.Column(db.String(255),unique=True,index=True)
    product_name = db.Column(db.String(255),index=True)
    model_name = db.Column(db.String(255),index=True)
    numbers = db.Column(db.Integer)
    owner = db.Column(db.String(255))
    position = db.Column(db.String(255),index=True)
    status = db.Column(db.String(255))
    calibratetime = db.Column(db.Date,default=datetime.now,nullable=False)
    resumptiontime = db.Column(db.Date,default=datetime.now,nullable=False)
    username = db.Column(db.String(64),index=True,nullable=True)
    usermail = db.Column(db.String(64),nullable=True)
    lend_time = db.Column(db.Date,default=datetime.now,nullable=True)
    back_time = db.Column(db.Date,default=datetime.now,nullable=True)
    remark = db.Column(db.String(64))
    profit_loss = db.Column(db.String(64))
    # sign = db.Column(db.Integer,default=2)
    # depots = db.relationship('Depot',secondary= 't2_depot',backref = db.backref('t2s'))
    def __init__(self,**kwargs):
        super(T2,self).__init__(**kwargs)

# fixedasset_depot = db.Table('fixedasset_depot',
                                           # db.Column('fixedasset_id',db.Integer,db.ForeignKey('fixedassets.id'),primary_key=True),
                                           # db.Column('depot_id',db.Integer,db.ForeignKey('depots.id'),primary_key=True)

# )        
        
#低值易耗品
class T3(db.Model):
    __tablename__ = 't3s'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),index=True)
    assetnumber = db.Column(db.String(255),unique=True,index=True)
    product_name = db.Column(db.String(255),index=True)
    model_name = db.Column(db.String(255),index=True)
    numbers = db.Column(db.Integer)
    department = db.Column(db.String(255))
    owner = db.Column(db.String(255))
    position = db.Column(db.String(255),index=True)
    status = db.Column(db.String(255))
    calibratetime = db.Column(db.Date,default=datetime.now,nullable=False)
    resumptiontime = db.Column(db.Date,default=datetime.now,nullable=False)
    username = db.Column(db.String(64),index=True,nullable=True)
    usermail = db.Column(db.String(64),nullable=True)
    lend_numbers = db.Column(db.Integer,nullable=True)
    lend_time = db.Column(db.Date,default=datetime.now,nullable=True)
    back_time = db.Column(db.Date,default=datetime.now,nullable=True)
    remark = db.Column(db.String(64))
    profit_loss = db.Column(db.String(64))
    # sign = db.Column(db.Integer,default=3)
    def __init__(self,**kwargs):
        super(T3,self).__init__(**kwargs)
     
    
#仓库表
class Depot(db.Model):
    __tablename__ = 'depots'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),unique=True)
    template_id = db.Column(db.Integer,db.ForeignKey('templates.id'))
    def __init__(self,**kwargs):
          super(Depot,self).__init__(**kwargs)
    
    
#模板表
class Template(db.Model):
    __tablename__ = 'templates'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),unique=True)
    depots = db.relationship('Depot',backref="templates",lazy="dynamic")
    def __init__(self,**kwargs):
          super(Template,self).__init__(**kwargs)
    
#图书馆
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    booknumber = db.Column(db.String(255))
    bookname = db.Column(db.String(255))
    numbers = db.Column(db.Integer)
    prices = db.Column(db.Float)
    position = db.Column(db.String(255))
    status = db.Column(db.String(255))
    username = db.Column(db.String(64),nullable=True)
    usermail = db.Column(db.String(64),nullable=True)
    lendtime = db.Column(db.Date,nullable=True)
    backtime = db.Column(db.Date,nullable=True)
    def __init__(self,**kwargs):
          super(Book,self).__init__(**kwargs)
          

# 删除记录表
class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    assetnumber = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    product = db.Column(db.String(255))
    depotname = db.Column(db.String(128))
    delete_time = db.Column(db.Date, default=datetime.now, nullable=True)

    def __init__(self, **kwargs):
        super(Record, self).__init__(**kwargs)
