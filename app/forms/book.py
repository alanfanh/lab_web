# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,SubmitField,DateTimeField,IntegerField,FloatField,DateField
from wtforms.validators import DataRequired, Optional, Length,NumberRange
from flask_wtf.file import FileField,FileRequired,FileAllowed


#图书馆
class BookForm(FlaskForm):
    booknumber = StringField('图书编号',validators = [Length(1,255)])
    bookname = StringField('书名',validators = [Length(1,255)])
    numbers = IntegerField('数量',validators = [NumberRange(1,65535)])
    prices = FloatField('价格')
    position = StringField('储位',validators = [Length(1,255)])
    status =  SelectField('状态',choices=[(1, '在库'), (2, '借出')],
        default = 1,coerce=int)
    username = StringField('借用人',validators = [Optional(),Length(1,64)])
    usermail = StringField('借用邮箱',validators = [Optional(),Length(1,64)])
    lendtime = DateField('借用时间',validators = [Optional()])
    backtime = DateField('归还时间',validators = [Optional()])
    submit = SubmitField(u'保存')