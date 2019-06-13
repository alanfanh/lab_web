#-*-coding:utf-8-*-
import unittest
from app.models import Role,User,T1,T2,T3,Book,Depot,Template
class BasicTestCase(unittest.TestCase):
    #用例执行前进行的操作
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		#用flask提供的测试客户端进行测试
		self.client = app.test_client()
        self.runner = app.test_cli_runner()
        #创建数据库
		db.create_all()
        #添加管理员账号
        admin_user = User(email='18392385468@163.com', name='系统管理员', username='admin')
        admin_user.set_password('admin')
        #添加普通用户
        normal_user = User(name='普通用户', username='normal')
        normal_user.set_password('12345')
        #添加模板
        tem1 = Template(id=1,name='模板1')
        tem2 = Template(id=1,name='模板2')
        tem3 = Template(id=1,name='模板3')
        #添加仓库
        t1 = Depot(id=1,name='竞品仓',template_id=1)
        t2 = Depot(id=1,name='固定资产仓',template_id=2)
        t3 = Depot(id=1,name='低值易损耗仓',template_id=3)
        #添加图书
        book = Book(booknumber=1,bookname='测试',numbers=1,prices=1.1,position='测试')
        db.session.add_all([admin_user,normal_user,tem1,tem2,tem3,t1,t2,t3,book])
        db.session.commit()
        
    #使用普通用户登录
    def login(self, name=None, password=None):
        if name is None and password is None:
            name = 'normal'
            password = '12345'
        return self.client.post(url_for('auth.login'), data=dict(
            name=name,
            password=password
        ), follow_redirects=True)
    
    #退出登录
    def logout(self):
        return self.client.get(url_for('auth.logout'), follow_redirects=True)
        
    #用例执行前进行的操作    
    def tearDown(self):
        db.drop_all()
        self.context.pop()
        
    