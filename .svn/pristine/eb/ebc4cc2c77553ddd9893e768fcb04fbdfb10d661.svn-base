# -*- coding: utf-8 -*-
"""
    :author: 张丽萍
"""
from flask import url_for

from app.models import User
from .config import Operations
from app.utils import generate_token
from tests.base import BaseTestCase


class AuthTestCase(BaseTestCase):
    #管理员用户登录
    def test_login_admin_user(self):
        response = self.login(name='admin', password='admin')
        data = response.get_data(as_text=True)
        self.assertIn('登录成功!', data)
    #普通用户登录
    def test_login_normal_user(self):
        response = self.login()
        data = response.get_data(as_text=True)
        self.assertIn('登录成功!', data)
        
    #不存在的用户登录
    def test_login_notuser(self):
        response = self.login(name='12345', password='12345')
        data = response.get_data(as_text=True)
        self.assertIn('用户不存在!', data)
        
    #错误密码登录
    def test_login_errpwd(self):
        response = self.login(name='normal', password='normal')
        data = response.get_data(as_text=True)
        self.assertIn('密码错误!', data)
    
    #退出登录
    def test_logout_user(self):
        self.login()
        response = self.logout()
        data = response.get_data(as_text=True)
        self.assertIn('Logout success.', data)
    
    #忘记密码发送链接
    def test_reset_password(self):
        #不存在的邮箱
        response = self.client.post(url_for('auth.forget_password'), data=dict(
            email='18392385469@163.com',
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('不存在的邮箱.', data)
        self.assertNotIn('密码重置邮件已发送,请打开邮箱查看.', data)
        #正确邮箱
        response = self.client.post(url_for('auth.forget_password'), data=dict(
            email='18392385468@163.com',
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('密码重置邮件已发送,请打开邮箱查看.', data)
        user = User.query.filter_by(email='18392385468@163.com').first()
        self.assertTrue(user.validate_password('admin'))
        #正确的token
        token = generate_token(user=user, operation=Operations.RESET_PASSWORD)
        response = self.client.post(url_for('auth.reset_password', token=token), data=dict(
            email='18392385468@163.com',
            password='new-password',
            password2='new-password'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('密码重置成功.', data)
        self.assertTrue(user.validate_password('new-password'))
        self.assertFalse(user.validate_password('admin'))
        # bad token
        response = self.client.post(url_for('auth.reset_password', token='bad token'), data=dict(
            email='18392385468@163.com',
            password='new-password',
            password2='new-password'
        ), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('链接无效或超时.', data)
        self.assertNotIn('密码重置成功.', data)
    