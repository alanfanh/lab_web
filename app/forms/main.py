# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,SubmitField,DateTimeField,IntegerField,FloatField,DateField
from wtforms.validators import DataRequired, Optional, Length,NumberRange
from flask_wtf.file import FileField,FileRequired,FileAllowed


#模板1表单
class ComproductForm(FlaskForm):
    assetnumber = StringField(u'资产编号',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    product_name = StringField(u'品牌',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    model_name = StringField(u'规格型号',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    numbers = IntegerField(u'现存数量',validators=[NumberRange(1,65535)],render_kw={'maxlength': '255'})
    position = StringField(u'储位',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    entertime = DateField (u'入库时间',validators=[Optional()])
    status = SelectField(u'状态',choices=[(1, '在库'), (2, '借出')],
        default = 1,coerce=int)
    username = StringField(u'借机人',validators=[Optional(),Length(0,64)],render_kw={'maxlength': '64'})
    usermail = StringField(u'借机邮箱',validators=[Optional(),Length(0,64)],render_kw={'maxlength': '64'})
    lend_time = DateField (u'借机时间',validators=[Optional()])
    lend_numbers = IntegerField(u'借机数量',validators=[Optional(),NumberRange(1,65535)])
    back_time = DateField (u'预计归还时间',validators=[Optional()])
    remark = StringField(u'备注',validators=[Optional(),Length(0,64)],render_kw={'maxlength': '64'})
    profit_loss = StringField(u'盘盈/盘亏',validators=[Optional(),Length(0,64)],render_kw={'maxlength': '64'})
    submit = SubmitField(u'保存')
    cancel = SubmitField(u'重置')

#上传表单    
class UploadForm(FlaskForm):
    file = FileField(validators= [FileRequired(),FileAllowed(['xls','xlsx'])])
    upload = SubmitField(u'上传')
    
    
#模板2表单
class FixedassetsForm(FlaskForm):
    assetnumber = StringField(u'资产编号',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    product_name = StringField(u'品牌',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    model_name = StringField(u'规格型号',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    numbers = IntegerField(u'数量(套/个)',validators=[NumberRange(1,65535)],render_kw={'maxlength': '255'})
    owner = StringField(u'责任组/人',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    position = StringField(u'储位',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    status = SelectField(u'状态',choices=[(1,'在库'),(2,'借出')],default=1,coerce=int)
    calibratetime = DateField (u'上次校准时间',validators=[Optional()])
    resumptiontime = DateField (u'复校时间',validators=[Optional()])
    username = StringField(u'借用人',render_kw={'maxlength': '64'})
    usermail = StringField(u'借用邮箱',render_kw={'maxlength': '64'})
    lend_time = DateField (u'借用时间',validators=[Optional()])
    back_time = DateField (u'预计归还时间',validators=[Optional()])
    remark = StringField(u'备注',validators=[Optional(),Length(0,64)],render_kw={'maxlength': '64'})
    profit_loss = StringField(u'盘盈/盘亏',validators=[Optional(),Length(0,64)],render_kw={'maxlength': '64'})
    submit = SubmitField(u'保存')
    cancel = SubmitField(u'重置')
    
    
    
#模板3表单
class ConsumablesForm(FlaskForm):
    assetnumber = StringField(u'资产编号',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    product_name = StringField(u'品牌',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    model_name = StringField(u'规格型号',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    numbers = IntegerField(u'数量(套/个)',validators=[NumberRange(1,65535)],render_kw={'maxlength': '255'})
    department = StringField(u'部门',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    owner = StringField(u'组别',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    position = StringField(u'储位',validators=[Length(1,255)],render_kw={'maxlength': '255'})
    status = SelectField(u'状态',choices=[(1,'在库'),(2,'借出')],default=1,coerce=int)
    calibratetime = DateField (u'上次校准时间',validators=[Optional()])
    resumptiontime = DateField (u'复校时间',validators=[Optional()])
    username = StringField(u'借用人',render_kw={'maxlength': '64'})
    usermail = StringField(u'借用邮箱',render_kw={'maxlength': '64'})
    lend_numbers = IntegerField(u'借用数量',validators=[Optional(),NumberRange(1,65535)])
    lend_time = DateField (u'借用时间',validators=[Optional()])
    remark = StringField(u'备注',validators=[Optional(),Length(0,64)],render_kw={'maxlength': '64'})
    profit_loss = StringField(u'盘盈/盘亏',validators=[Optional(),Length(0,64)],render_kw={'maxlength': '64'})
    submit = SubmitField(u'保存')
    cancel = SubmitField(u'重置')
    
    
