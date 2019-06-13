
# 实验室资产管理系统 #	
### python版本:python3.7

### 目录结构
````
requirements.txt     					需要安装的第三方库列表
config.py  								开发和生产环境下配置文件
manage.py 								开发环境下应用入口文件
test										单元测试文件
sql_sendmail.py									查询到期账号的邮箱,发送邮件
app										app项目
	__init__.py							app项目初始化文件，生成app										
	--forms								表单文件,用于生成各个页面的控件
			--__init__.py
			--auth.py					登录表单、修改管理员密码表单、忘记密码表单和重置密码表单
			--book.py					图书管理模块表单
			--depot.py					仓库管理模块表单
			--main.py					主页竞品仓表单、固定资产仓表单和低值易损耗仓表单
			--user.py					普通用户管理表单
	--views								视图函数
			--__init__.py
			--auth.py					登录、修改管理员密码、忘记密码和重置密码视图函数
			--book.py					图书管理模块视图函数
			--depot.py					仓库管理模块视图函数
			--main.py					主页视图函数
			--user.py					普通用户管理视图函数
	--templates						前端文件
			base.html					模板html
			--auth						认证模块前端html
			--book						图书管理模块前端html
			--depot						仓库管理模块前端html
			--main						main主页模块前端html
				--t1						模板1（竞品仓）前端html
				--t2						模板2（固定资产仓）前端html
				--t3						模板3（低值易损耗仓）前端html
			--user						普通用户管理前端html
			--email						忘记密码和重置密码邮件模板
	--static								js、css文件目录
			--css
			--js
				--auth.js				认证和普通用户模块前端js校验文件
				--book.js				图书管理模块前端js校验文件
				--depot.js 				仓库管理和主页模块前端js校验文件
				--common.js			前端公共s校验文件
	decorators.py                      装饰器,权限装饰器、登录状态装饰器和管理员权限装饰
	models.py 							数据模型，用来定义app项目的数据库模型
	emails.py
	utils.py 								辅助函数
````