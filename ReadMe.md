# lab-web

> lab-web is a Flask Web project.

## 介绍

基于Flask框架开发的web应用，资产管理平台。

### Developer

[FanHao](http://alanfanh.github)

## 环境

### 语言

```text
python3.6 64bit
```

### 依赖

> 可使用"pip install -r requirements.txt"一键安装所有依赖项。

> 具体依赖库请查看"requirements.txt"。

### 数据库

> MySQL或者MariaDB等关系型数据库

## 项目结构

> 持续更新中.....

```text
webapp
├── manage.py                      # 程序入口
├── app                            # 项目主代码文件夹
│   ├── __init__.py                  # app初始文件
│   ├── froms                        # 存放表单文件
│   │    ├── auth.py                    # 登陆、密码表单
│   │    ├── book.py                    # 图书管理表单
│   │    ├── depot.py                   # 仓库管理表单
│   │    ├── main.py                    # 主页3个仓库表单
│   │    └── user.py                    # 普通用户管理表单
│   ├── views                        # 存放视图函数
│   │    ├── auth.py                    # 登陆、密码视图函数
│   │    ├── book.py                    # 图书管理师视图函数
│   │    ├── depot.py                   # 仓库管理视图函数
│   │    ├── main.py                    # 主页仓库视图函数
│   │    └── user.py                    # 普通用户管理视图函数
│   ├── templates                    # 存放前端模版文件
│   │    ├── base.html                  # 基模板html
│   │    ├── auth                       # 认证模块的前端模版html
│   │    ├── book                       # 图书管理模块前端html
│   │    ├── depot                      # 仓库管理模块前端html
│   │    ├── main                       # 主页前端模版
│   │    │   ├── t1                       # 模版1(竞品)前端html
│   │    │   ├── t2                       # 模版2(固定资产)前端html
│   │    │   └── t3                       # 模版3(低值易损耗)前端html
│   │    ├── user                       # 普通用户管理前端模版
│   │    └── email                      # 忘记密码重置模版
│   ├── static                       # 静态文件目录
│   │    ├── js                         # js文件
│   │    │   ├── auth.js                  # 认证和普通用户模块前端js校验
│   │    │   ├── book.js                  # 图书管理模块前端js校验文件
│   │    │   ├── depot.js                 # 仓库管理和主页模块前端js校验文件
│   │    │   └── common.js                # 前端公共js校验文件
│   │    └── css                          # css文件目录 
│   ├── decorators.py                # 装饰器，权限控制、登陆状态和管理员权限
│   ├── model.py                     # 数据模型
│   ├── utils.py                     # 辅助函数
│   └── emails.py                    #
├── requirements.txt               # 项目依赖
├── Readme.md                      # 项目Guide
├── uwsgi_cnf.ini                  # uwsgi服务器的配置
├── config.py  		               # 配置文件
├── sql_sendmail.py	               # 邮件发送功能
├── fabfile.py                     # 自动化部署脚本
└── test                           # 单元测试文件夹
```

