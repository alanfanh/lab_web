# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp,Optional
from app.models import User



class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[Length(5,32),Regexp('^[a-zA-Z0-9_]*$',
                                                          message='The username should contain only _,a-z, A-Z and 0-9.')])
    password = PasswordField('密码', validators=[Length(5,32),Regexp('^[a-zA-Z0-9_]*$',
                                                          message='The username should contain only _,a-z, A-Z and 0-9.')])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登录')


#管理员账户修改密码表单
class ChangePasswordForm(FlaskForm):
    name = StringField(u'备注')
    username = StringField(u'用户名')
    email = StringField('Email',validators=[Length(1,64),Email()])
    changepwd = BooleanField(u'更改密码',default=False)
 
    oldpassword = PasswordField(u'旧密码',validators=[Optional(),Length(5,32)])
    password = PasswordField(u'新密码',validators=[Optional(),Length(5,32),Regexp('^[a-zA-Z0-9_]*$',
                                                      message='The username should contain only _,a-z, A-Z and 0-9.')])
    password2 = PasswordField(u'确认密码',validators=[Optional(),EqualTo('password',message='Passwords must match')])
        
    submit = SubmitField('保存')

#管理员账户忘记密码表单
class ForgetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[Length(1, 254), Email()])
    submit = SubmitField('确定')

#管理员账户重置密码表单
class ResetPasswordForm(FlaskForm):
    email = StringField('Email', validators=[Length(1, 254), Email()])
    password = PasswordField('密码', validators=[ Length(5, 32), EqualTo('password2'),Regexp('^[a-zA-Z0-9_]*$',
                                                          message='The username should contain only _,a-z, A-Z and 0-9.')])
    password2 = PasswordField('确认密码')
    submit = SubmitField('保存')