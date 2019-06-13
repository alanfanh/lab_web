# -*- coding: utf-8 -*-

from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, HiddenField, ValidationError,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, Regexp


#添加仓库的表单
class AddDepotForm(FlaskForm):
    depotname = StringField('仓库名称', validators=[DataRequired(), Length(1, 30)],render_kw = {"maxlength":"30"})
    template = SelectField('模板',validators=[DataRequired()],choices=[(1, '模板1'), (2, '模板2'),(3,'模板3')],
        default = 1,coerce=int)
    submit = SubmitField('保存')

