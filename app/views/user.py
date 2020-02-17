# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, current_app, request, Blueprint
from flask_login import login_required, current_user, fresh_login_required, logout_user
from app.forms.user import AddAccountForm
from app.models import User,Permission
from .. import db
from app.utils import redirect_back
from app.decorators import admin_required,permission_required
from sqlalchemy import or_

user_bp = Blueprint('user', __name__)

#普通用户列表
@user_bp.route('/user/index')
@login_required
@admin_required
def index():
        q = request.args.get('q','')
        print("q=",q)
        page = request.args.get('page', 1, type=int)
        per_page = current_app.config['USER_PER_PAGE']
        if q:
            pagination = User.query.filter(
                                                    or_(
                                                        User.username.like("%"+q+"%"),
                                                        User.name.like("%"+q+"%")
                                                    )
           
           ).paginate(page, per_page)
        else:
            pagination = User.query.paginate(page, per_page)
        users = pagination.items  
        for user in users:
            if user.username == "admin":
                users.remove(user)
        return render_template('user/index.html', pagination=pagination, users=users)

#添加普通用户
@user_bp.route('/user/settings/add',methods=['GET','POST']) 
@login_required
@admin_required
def add_account():
    form = AddAccountForm()
    print(request.form)
    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        password= form.password.data
        if  User.query.filter_by(name= name).first():
            flash('名称已存在','err')
            return render_template('user/settings/add.html',form=form)
        if User.query.filter_by(username= username).first():
            flash('用户已存在','err')
            return render_template('user/settings/add.html',form=form)
        user = User(name=name,username=username)
        #设置密码
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('添加成功','success')
        return redirect(url_for('user.index'))
    return render_template('user/settings/add.html',form=form)
    
#编辑普通用户
@user_bp.route('/user/settings/edit/<int:id>',methods=['GET','POST']) 
@login_required
@admin_required
def edit_account(id):
    form = AddAccountForm()
    print('form.data=',form.data)
    user = User.query.filter_by(id = id).first_or_404()
    if form.validate_on_submit():
        search_username = User.query.filter_by(username=form.username.data).first()
        search_name = User.query.filter_by(name=form.name.data).first()
        if search_name and search_name == form.username.data:
            flash('用户已存在','err')
        elif search_name and search_name == form.name.data:
            flash('名称已存在','err')
        else:
            user.name = form.name.data
            user.username = form.username.data
            user.password_hash = user.set_password(form.password.data)
            print('***pass***',form.password.data)
            print('***hash pass***',user.password_hash)
            db.session.add(user)
            db.session.commit()
            flash('修改成功','success')
            return redirect(url_for('user.index'))
    form.name.data = user.name
    form.username.data = user.username
    return render_template('user/settings/edit.html',form=form)
    
#删除普通用户
@user_bp.route('/user/settings/del/<int:id>',methods=['GET','POST']) 
@login_required
@admin_required
def del_account(id):
    user=User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('删除成功','success')
    return redirect_back()