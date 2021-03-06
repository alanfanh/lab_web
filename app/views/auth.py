# -*- coding: utf-8 -*-

from flask_login import login_user, logout_user, login_required, current_user, login_fresh, confirm_login,fresh_login_required
from flask import Flask,render_template,request,flash,Blueprint,redirect,url_for
from app.forms.auth import LoginForm,ChangePasswordForm,ForgetPasswordForm,ResetPasswordForm
from app.models import User
from .. import db
from app.utils import redirect_back,generate_token,validate_token
from app.emails import send_reset_password_email,send_mail
from config import Operations
from ..decorators import admin_required,unlogin_required

auth_bp = Blueprint('auth', __name__)

 
#登录用户 
@auth_bp.route('/login', methods=['GET', 'POST'])
@unlogin_required
def login():
    # if current_user.is_authenticated:
        # return redirect(url_for('main.index'))
    form=LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember_me.data
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if username == user.username and user.validate_password(password):
                login_user(user,remember)
                flash(u'登录成功!')
                return redirect(url_for('main.index'))
            elif not user.validate_password(password):
                flash(u'密码错误!')
        else:
            flash(u'用户不存在!')
    return render_template('auth/login.html', form=form)
      
#重新认证
@auth_bp.route('/re-authenticate', methods=['GET', 'POST'])
@login_required
def re_authenticate():
    if login_fresh():
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit() and current_user.validate_password(form.password.data):
        confirm_login()
        return redirect_back()
    return render_template('auth/login.html', form=form)

#退出登录
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout success.', 'info')
    return redirect(url_for('auth.login'))

#管理员账户修改密码
@auth_bp.route('/change-password/<int:id>',methods=['GET','POST'])
@fresh_login_required
@admin_required
def change_password(id):
    form = ChangePasswordForm()
    user = User.query.filter_by(id = id).first_or_404()
    print("form=",form)
    if form.validate_on_submit() and  request.method == "POST":
        #若勾选更改密码，则修改密码后退出到登录界面
        if form.changepwd.data == True:
            if current_user.validate_password(form.oldpassword.data):
                current_user.set_password(form.password.data)
                user.email = form.email.data
                db.session.commit()
                return redirect(url_for('auth.logout'))
            else:
                flash(u"旧密码错误!")
        else:
            #不勾选更改密码,当前输入邮箱与从数据库查询的密码不一致时，修改邮箱
            if user.email != form.email.data:
                user.email = form.email.data
                db.session.commit()
            return redirect(url_for('main.index'))
    form.name.data = user.name
    form.username.data = user.username
    form.email.data= user.email
    return render_template('auth/change_password.html',form=form)
   

#忘记密码
@auth_bp.route('/forget-password', methods=['GET', 'POST'])
@unlogin_required
def forget_password():
    # if current_user.is_authenticated:
        # return redirect(url_for('main.index'))

    form = ForgetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower(),role_id = 1).first()
        print("user=",user)
        if user:
            print("******start**********")
            token = generate_token(user=user, operation=Operations.RESET_PASSWORD)
            send_reset_password_email(user=user, token=token)
            flash('密码重置邮件已发送,请打开邮箱查看.', 'info')
            return redirect(url_for('.login'))
        flash('不存在的邮箱.', 'warning')
        return redirect(url_for('.forget_password'))
    return render_template('auth/forget_password.html', form=form)

#忘记密码重置密码
@auth_bp.route('/reset-password/<token>', methods=['GET', 'POST'])
@unlogin_required
def reset_password(token):
    # if current_user.is_authenticated:
        # return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower(),role_id = 1).first()
        if user is None:
            flash('用户不存在.','warning')
            return redirect(url_for('auth.login'))
        if validate_token(user=user, token=token, operation=Operations.RESET_PASSWORD,
                          new_password=form.password.data):
            flash('密码重置成功.', 'success')
            return redirect(url_for('.login'))
        else:
            flash('链接无效或超时.', 'danger')
            return redirect(url_for('.forget_password'))
    return render_template('auth/reset_password.html', form=form)
