# -*- coding: utf-8 -*-
import re
import os
from flask import render_template, flash, redirect, url_for, current_app, send_from_directory, request, abort, Blueprint,send_from_directory
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import func
from .. import db
from app.utils import redirect_back,rename_file,allowed_file,read_excel,write_excel,checkHead,checkInt,checkNumber,checkType,checkEmpty,checkNumber,checkType,checkType2,checkDate,checkCompareDate,checkEmail
from app.forms.main import ComproductForm,UploadForm,FixedassetsForm,ConsumablesForm
from app.models import T1,T2,T3,Depot
from app.decorators import admin_required
from datetime import datetime
from sqlalchemy import or_,and_
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
# @login_required
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return redirect(url_for('main.show',name="竞品仓"))


#显示
@main_bp.route('/show/<name>')
@login_required
def show(name):
    print(request.args)
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['MAIN_PER_PAGE']
    depots = Depot.query.all()
    depot = Depot.query.filter_by(name = name).first()
    template_id = depot.template_id
    form = UploadForm()
    if template_id == 1:
        q = request.args.get('q','')
        print("q=",q)
        if q != "":
            pagination = T1.query.filter_by(name=name).filter(
                                                    or_(
                                                            T1.username.like("%"+q+"%"),
                                                            T1.assetnumber.like("%"+q+"%"),
                                                            T1.product_name.like("%"+q+"%"),
                                                            T1.model_name.like("%"+q+"%"),
                                                            T1.position.like("%"+q+"%"),
                                                            T1.entertime.like("%"+q+"%")
                                                            
                                                    )
                                                ).paginate(page, per_page)
        else:
            pagination = T1.query.filter_by(name=name).paginate(page, per_page)
        cmps = pagination.items  
    elif  template_id == 2:
        q = request.args.get('q','')
        print("q=",q)
        if q != "":
            pagination = T2.query.filter_by(name=name).filter(
                                                or_(
                                                        T2.username.like("%"+q+"%"),
                                                        T2.assetnumber.like("%"+q+"%"),
                                                        T2.product_name.like("%"+q+"%"),
                                                        T2.model_name.like("%"+q+"%"),
                                                        T2.position.like("%"+q+"%"),
                                                        T2.owner.like("%"+q+"%")
                                                )
                                                            ).paginate(page, per_page)
        else:
            pagination = T2.query.filter_by(name=name).paginate(page, per_page)
        cmps = pagination.items  
    elif template_id == 3:
        q = request.args.get('q','')
        print("q=",q)
        if q != "":
            pagination = T3.query.filter_by(name=name).filter(
                                                    or_(
                                                            T3.username.like("%"+q+"%"),
                                                            T3.assetnumber.like("%"+q+"%"),
                                                            T3.product_name.like("%"+q+"%"),
                                                            T3.model_name.like("%"+q+"%"),
                                                            T3.position.like("%"+q+"%"),
                                                            T3.department.like("%"+q+"%"),
                                                            T3.owner.like("%"+q+"%")
                                                    )
                                                ).paginate(page, per_page)
        else:
            pagination = T3.query.filter_by(name=name).paginate(page, per_page)
        cmps = pagination.items  
    return render_template('main/show.html', pagination=pagination, cmps=cmps,form=form,depots=depots,depot=depot,template_id=template_id)
      

#添加    
@main_bp.route('/<name>/add',methods=['GET','POST'])
@login_required
@admin_required
def add(name):
    depot = Depot.query.filter_by(name = name).first()
    template_id = depot.template_id
    if template_id == 1:
        form = ComproductForm()
        if form.validate_on_submit():
            assetnumber = form.assetnumber.data
            product_name = form.product_name.data
            model_name = form.model_name.data
            numbers = form.numbers.data
            position = form.position.data
            entertime = form.entertime.data
            status = form.status.data
            remark = form.remark.data
            profit_loss = form.profit_loss.data
            kwargs = {'assetnumber':assetnumber,'product_name':product_name,'model_name':model_name,'numbers':numbers,'position':position,'entertime':entertime,'status':status,'remark':remark,'profit_loss':profit_loss,'name':name}
            if T1.query.filter_by(assetnumber = assetnumber).count() > 0:
                flash('资产编号%s已存在' %assetnumber,'err')
                return render_template('main/t1/add.html',form=form,depot=depot)
            if  status == 2:
                username = form.username.data
                usermail = form.usermail.data
                lend_time = form.lend_time.data
                lend_numbers = form.lend_numbers.data
                back_time = form.back_time.data
                userinfo  = {'username':username,'usermail':usermail,'lend_time':lend_time,'lend_numbers':lend_numbers,'back_time':back_time}
                kwargs.update(userinfo)
            cmp = T1(**kwargs)
            db.session.add(cmp)
            db.session.commit()
            flash('添加成功')
            return redirect(url_for('main.show',name=depot.name))
        return render_template('main/t1/add.html',form=form,depot=depot)
    elif template_id == 2:
        form = FixedassetsForm()
        if form.validate_on_submit():
            assetnumber = form.assetnumber.data
            product_name = form.product_name.data
            model_name = form.model_name.data
            numbers = form.numbers.data
            owner = form.owner.data
            position = form.position.data
            status = form.status.data
            remark = form.remark.data
            profit_loss = form.profit_loss.data
            calibratetime = form.calibratetime.data
            resumptiontime = form.resumptiontime.data
            kwargs = {'assetnumber':assetnumber,'product_name':product_name,'model_name':model_name,'numbers':numbers,'owner':owner,'position':position,'status':status,'remark':remark,'profit_loss':profit_loss,'calibratetime':calibratetime,'resumptiontime':resumptiontime,'name':name}
            if T2.query.filter_by(assetnumber = assetnumber).count() > 0:
                flash('资产编号%s已存在' %assetnumber,'err')
                return render_template('main/t2/add.html',form=form,depot=depot)
            if  status == 2:
                username = form.username.data
                usermail = form.usermail.data
                lend_time = form.lend_time.data
                back_time = form.back_time.data
                userinfo  = {'username':username,'usermail':usermail,'lend_time':lend_time,'back_time':back_time}
                kwargs.update(userinfo)
            cmp = T2(**kwargs)
            db.session.add(cmp)
            db.session.commit()
            flash('添加成功')
            return redirect(url_for('main.show',name=depot.name))
        return render_template('main/t2/add.html',form=form,depot=depot)
    elif template_id == 3:
        form = ConsumablesForm()
        if form.validate_on_submit():
            assetnumber = form.assetnumber.data
            product_name = form.product_name.data
            model_name = form.model_name.data
            numbers = form.numbers.data
            department = form.department.data
            owner = form.owner.data
            position = form.position.data
            status = form.status.data
            remark = form.remark.data
            profit_loss = form.profit_loss.data
            calibratetime = form.calibratetime.data
            resumptiontime = form.resumptiontime.data
            kwargs = {'assetnumber':assetnumber,'product_name':product_name,'model_name':model_name,'numbers':numbers,'department':department,'owner':owner,'position':position,'status':status,'remark':remark,'profit_loss':profit_loss,'calibratetime':calibratetime,'resumptiontime':resumptiontime,'name':name}
            if T3.query.filter_by(assetnumber = assetnumber).count() > 0:
                flash('资产编号%s已存在' %assetnumber,'err')
                return render_template('main/t3/add.html',form=form,depot=depot)
            if  status == 2:
                username = form.username.data
                usermail = form.usermail.data
                lend_time = form.lend_time.data
                lend_numbers = form.lend_numbers.data
                userinfo  = {'username':username,'usermail':usermail,'lend_time':lend_time,'lend_numbers':lend_numbers}
                kwargs.update(userinfo)
            cmp = T3(**kwargs)
            db.session.add(cmp)
            db.session.commit()
            flash('添加成功')
            return redirect(url_for('main.show',name=depot.name))
        return render_template('main/t3/add.html',form=form,depot=depot)
     
#编辑
@main_bp.route('/<name>/edit/<int:id>',methods=['GET','POST'])     
@login_required
@admin_required
def edit(name,id):
    depot = Depot.query.filter_by(name = name).first()
    template_id = depot.template_id
    # 获取记录所处的分页页面url
    redirect_url = request.args.get('redirect_url')
    # print("****redirect_url:",redirect_url)
    if template_id == 1:
        form = ComproductForm()
        cmp = T1.query.get_or_404(id)
        if form.validate_on_submit():
            search_assetnumber = T1.query.filter_by(assetnumber = form.assetnumber.data).first() 
            if T1.query.filter_by(assetnumber = form.assetnumber.data).count() > 0 and search_assetnumber == form.assetnumber.data:
                flash('编号为%s的资产%s已存在' %(form.assetnumber.data,form.product_name.data),'err')
            else:
                cmp.assetnumber = form.assetnumber.data
                cmp.product_name = form.product_name.data
                cmp.model_name = form.model_name.data
                cmp.numbers = form.numbers.data
                cmp.position = form.position.data
                cmp.entertime = form.entertime.data
                cmp.status = form.status.data
                cmp.remark = form.remark.data
                cmp.profit_loss = form.profit_loss.data
                if form.status.data == 1:
                    cmp.username = None
                    cmp.usermail = None
                    cmp.lend_time = datetime.now().strftime("%Y-%m-%d")
                    cmp.lend_numbers = None
                    cmp.back_time = datetime.now().strftime("%Y-%m-%d")
                elif form.status.data == 2:
                    cmp.username = form.username.data
                    cmp.usermail = form.usermail.data
                    cmp.lend_time = form.lend_time.data
                    cmp.lend_numbers = form.lend_numbers.data
                    cmp.back_time = form.back_time.data
                db.session.commit()
                flash("修改成功","success")
                # return redirect(url_for('main.show',name=depot.name))
                return redirect(redirect_url)
        form.assetnumber.data = cmp.assetnumber
        form.product_name.data = cmp.product_name
        form.model_name.data = cmp.model_name
        form.numbers.data = cmp.numbers
        form.position.data = cmp.position
        form.entertime.data = cmp.entertime
        form.status.data = int(cmp.status)
        # print("status=",form.status.data)
        form.remark.data = cmp.remark
        form.username.data = cmp.username
        form.usermail.data = cmp.usermail
        form.lend_time.data = cmp.lend_time
        form.lend_numbers.data = cmp.lend_numbers
        form.back_time.data = cmp.back_time
        form.profit_loss.data = cmp.profit_loss
        print("form=",form)
        return render_template('main/t1/edit.html',form=form,depot=depot)
    elif template_id == 2:
        form = FixedassetsForm()
        cmp = T2.query.get_or_404(id)
        if form.validate_on_submit():
            search_assetnumber = T2.query.filter_by(assetnumber = form.assetnumber.data).first() 
            if T2.query.filter_by(assetnumber = form.assetnumber.data).count() > 0 and search_assetnumber == form.assetnumber.data:
                flash('编号为%s的资产%s已存在' %(form.assetnumber.data,form.product_name.data),'err')
            else:
                cmp.assetnumber = form.assetnumber.data
                cmp.product_name = form.product_name.data
                cmp.model_name = form.model_name.data
                cmp.numbers = form.numbers.data
                cmp.owner = form.owner.data
                cmp.position = form.position.data
                cmp.status = form.status.data
                cmp.remark = form.remark.data
                cmp.profit_loss = form.profit_loss.data
                cmp.calibratetime = form.calibratetime.data
                cmp.resumptiontime = form.resumptiontime.data
                if form.status.data == 1:
                    cmp.username = None
                    cmp.usermail = None
                    cmp.lend_time = datetime.now().strftime("%Y-%m-%d")
                    cmp.back_time = datetime.now().strftime("%Y-%m-%d")
                elif form.status.data == 2:
                    cmp.username = form.username.data
                    cmp.usermail = form.usermail.data
                    cmp.lend_time = form.lend_time.data
                    cmp.back_time = form.back_time.data
                db.session.commit()
                flash("修改成功","success")
                # return redirect(url_for('main.show',name=depot.name))
                return redirect(redirect_url)
        form.assetnumber.data = cmp.assetnumber
        form.product_name.data = cmp.product_name
        form.model_name.data = cmp.model_name
        form.numbers.data = cmp.numbers
        form.owner.data = cmp.owner
        form.position.data = cmp.position
        form.status.data = int(cmp.status)
        form.remark.data = cmp.remark
        form.username.data = cmp.username
        form.usermail.data = cmp.usermail
        form.lend_time.data = cmp.lend_time
        form.back_time.data = cmp.back_time
        form.profit_loss.data = cmp.profit_loss
        form.calibratetime.data = cmp.calibratetime
        form.resumptiontime.data = cmp.resumptiontime
        return render_template('main/t2/edit.html',form=form,depot=depot) 
    elif template_id == 3:
        form = ConsumablesForm()
        cmp = T3.query.get_or_404(id)
        if form.validate_on_submit():
            search_assetnumber = T3.query.filter_by(assetnumber = form.assetnumber.data).first() 
            if T3.query.filter_by(assetnumber = form.assetnumber.data).count() > 0 and search_assetnumber == form.assetnumber.data:
                flash('编号为%s的资产%s已存在' %(form.assetnumber.data,form.product_name.data),'err')
            else:
                cmp.assetnumber = form.assetnumber.data
                cmp.product_name = form.product_name.data
                cmp.model_name = form.model_name.data
                cmp.numbers = form.numbers.data
                cmp.department = form.department.data
                cmp.owner = form.owner.data
                cmp.position = form.position.data
                cmp.status = form.status.data
                cmp.remark = form.remark.data
                cmp.profit_loss = form.profit_loss.data
                cmp.calibratetime = form.calibratetime.data
                cmp.resumptiontime = form.resumptiontime.data
                if form.status.data == 1:
                    cmp.username = None
                    cmp.usermail = None
                    cmp.lend_time = datetime.now().strftime("%Y-%m-%d")
                    cmp.lend_numbers = None
                    cmp.back_time = datetime.now().strftime("%Y-%m-%d")
                elif form.status.data == 2:
                    cmp.username = form.username.data
                    cmp.usermail = form.usermail.data
                    cmp.lend_time = form.lend_time.data
                    cmp.lend_numbers = form.lend_numbers.data
                db.session.commit()
                flash("修改成功","success")
                # return redirect(url_for('main.show',name=depot.name))
                return redirect(redirect_url)
        form.assetnumber.data = cmp.assetnumber
        form.product_name.data = cmp.product_name
        form.model_name.data = cmp.model_name
        form.numbers.data = cmp.numbers
        form.department.data = cmp.department
        form.owner.data = cmp.owner
        form.position.data = cmp.position
        form.status.data = int(cmp.status)
        form.remark.data = cmp.remark
        form.username.data = cmp.username
        form.usermail.data = cmp.usermail
        form.lend_time.data = cmp.lend_time
        form.lend_numbers.data = cmp.lend_numbers
        form.profit_loss.data = cmp.profit_loss
        form.calibratetime.data = cmp.calibratetime 
        form.resumptiontime.data = cmp.resumptiontime
        return render_template('main/t3/edit.html',form=form,depot=depot)
 
#竞品仓删除 
@main_bp.route('/<name>/delete/<int:id>',methods=['GET','POST'])
@login_required
@admin_required
def delete(name,id):
    depot = Depot.query.filter_by(name = name).first()
    template_id = depot.template_id
    if template_id == 1:
        cmp = T1.query.filter(and_(T1.name == name,T1.id == id)).first()
    elif template_id == 2:
        cmp = T2.query.filter(and_(T2.name == name,T2.id == id)).first()
    elif template_id == 3:
        cmp = T3.query.filter(and_(T3.name == name,T3.id == id)).first()
    db.session.delete(cmp)
    db.session.commit()
    flash('删除成功')
    return redirect_back()
        
#批量删除    
@main_bp.route('/<name>/deleteall',methods = ['GET','POST'])
@login_required
@admin_required
def delete_all(name):
    depot = Depot.query.filter_by(name = name).first()
    template_id = depot.template_id
    if request.method=='POST':
        all_id = request.form.get('ids')
        all_id=all_id.split(',')
        if '' in all_id:
            all_id.remove('')
        if 'on' in all_id:
            all_id.remove('on')
        print("all_id=", all_id)
        all_id=list(map(int,all_id))
        for i in all_id:
            if template_id == 1:
                cmp = T1.query.filter(and_(T1.name == name, T1.id == i)).first()
            elif template_id == 2:
                cmp = T2.query.filter(and_(T2.name == name, T2.id == i)).first()
            elif template_id == 3:
                cmp = T3.query.filter(and_(T3.name == name, T3.id == i)).first()
            db.session.delete(cmp)
        db.session.commit()
        return redirect_back()
        

#导入
#读取excel文件中的内容并存入到mysql数据库
@main_bp.route('/<name>/upload',methods=['GET','POST'])       
@login_required
@admin_required
def upload(name):
    print("request.files=",request.files)
    depot = Depot.query.filter_by(name = name).first()
    template_id = depot.template_id
    status_dict = {"在库":"1","借出":"2"}
    if request.method == 'POST' and 'file' in request.files:
        f = request.files.get('file')
        print("f=",f)
        filename = rename_file(f.filename)
        print("filename=",filename)
        if allowed_file(f.filename):
            if not os.path.exists(current_app.config['UPLOAD_PATH']):
                os.mkdir(current_app.config['UPLOAD_PATH'])
            path = os.path.join(current_app.config['UPLOAD_PATH'], filename)
            f.save(path)
        else:
             flash('失败:上传文件格式错误,请上传文件后缀为.xls和.xlsx的文件','err')
             return redirect(url_for('main.show',name=depot.name))
        datas = read_excel(path)
        print("*******datas=",datas)
        #判断表格格式是否正确
        if template_id == 1:
            head = ['资产编号','品牌','规格型号','现存数量','储位','入库时间','状态','借机人','借机邮箱','借机时间','借机数量','预计归还时间','备注','盘盈/盘亏']
            if not checkHead(head,datas[0]):
                flash("失败:上传文件表头信息错误,正确的表头信息为%s" %head,'err')
                return redirect(url_for('main.show',name=depot.name))
            #检查内容是否符合格式
            datas.remove(datas[0])
            for data in datas:
                if checkEmpty(data['资产编号']) or not checkType(data['资产编号']):
                    flash('失败:资产编号不能为空，且只能输入数字、字母和下划线,资产编号=%s' %data['资产编号'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['品牌']):
                    flash('失败:品牌不能为空,品牌=%s' %data['品牌'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['规格型号']):
                    flash('失败:规格型号不能为空,规格型号=%s' %data['规格型号'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['现存数量']) or not checkInt(data['现存数量']):
                    flash('失败:现存数量不能为空，且只能整数,数量=%s' %data['现存数量'],'err')    
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['储位']) or not checkType2(data['储位']):
                    flash('失败:储位不能为空，且只能输入数字、字母、中文和下划线,储位=%s' %data['储位'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['入库时间']) or not checkDate(data['入库时间']):
                    flash("失败:入库时间格式为年-月-日或年/月/日,入库时间=%s" %data['入库时间'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                kwargs = {'name':depot.name,'assetnumber':data['资产编号'],'product_name':data['品牌'],'model_name':data['规格型号'],'numbers':data['现存数量'],'position':data['储位'],'entertime':data['入库时间'],'status':status_dict[data['状态']],'remark':data['备注'],'profit_loss':data['盘盈/盘亏']}
                if status_dict[data['状态']] == '1':
                    if not checkEmpty(data['借机人']):
                        flash('失败:在库时借机人必须为空,借机人=%s' %data['借机人'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if not checkEmpty(data['借机邮箱']):
                        flash('失败:在库时借机邮箱必须为空,借机邮箱=%s' %data['借机邮箱'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if not checkEmpty(data['借机数量']):
                        flash('失败:在库时借机数量必须为空,借机数量=%s' %data['借机数量'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                elif status_dict[data['状态']] == '2':
                    if checkEmpty(data['借机人']):
                        flash('失败:借机人不能为空,借机人=%s' %data['借机人'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['借机邮箱']) or not checkEmail(data['借机邮箱']):
                        flash('失败:借机邮箱不能为空,且格式符合邮箱要求,借机邮箱=%s' %data['借机邮箱'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['借机数量']) or not checkInt(data['借机数量']):
                        flash('失败:借机数量不能为空,且只能输入整数,借机数量=%s' %data['借机数量'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['借机时间']) or not checkDate(data['借机时间']):
                        flash("失败:借机时间格式为年-月-日或年/月/日,借机时间=%s" %data['借机时间'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['预计归还时间']) or not checkDate(data['预计归还时间']):
                        flash("失败:预计归还时间格式为年-月-日或年/月/日,预计归还时间=%s" %data['预计归还时间'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    userinfo = {'username':data['借机人'],'usermail':data['借机邮箱'],'lend_time':data['借机时间'],'back_time':data['预计归还时间'],'lend_numbers':data['借机数量']}
                    kwargs.update(userinfo)
                cmp = T1(**kwargs)
                if T1.query.filter_by(assetnumber = data['资产编号']).count() > 0:
                    flash('失败:编号为%s的资产已存在' %data['资产编号'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                db.session.add(cmp)
            db.session.commit()
            flash('上传成功','success') 
            return redirect(url_for('main.show',name=depot.name))
        elif template_id == 2:
            head = ['资产编号','品牌','规格型号','数量(套/个)','责任组/人','储位','上次校准时间','复校时间','状态','借用人','借用邮箱','借用时间','预计归还时间','备注','盘盈/盘亏']
            if not checkHead(head,datas[0]):
                flash("失败:上传文件表头信息错误,正确的表头信息为%s" %head,'err')
                return redirect(url_for('main.show',name=depot.name))
            #检查内容是否符合格式
            datas.remove(datas[0])
            for data in datas:
                if checkEmpty(data['资产编号']) or not checkType(data['资产编号']):
                    flash('失败:资产编号不能为空,且只能输入数字、字母和下划线,资产编号=%s' %data['资产编号'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['品牌']):
                    flash('失败:品牌不能为空=%s' %data['品牌'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['规格型号']):
                    flash('失败:规格型号不能为空=%s' %data['规格型号'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['数量(套/个)']) or not  checkInt(data['数量(套/个)']):
                    flash('失败:数量不能为空,且只能是整数,数量(套/个)=%s' %data['现存数量(套/个)'],'err')    
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['责任组/人']):
                    flash('失败:责任组/人不能为空')    
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['储位']) or not  checkType2(data['储位']):
                    flash('失败:储位不能为空，且只能输入数字、字母、中文和下划线,储位=%s' %data['储位'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['上次校准时间']) or not checkDate(data['上次校准时间']):
                    flash('失败:上次校准时间格式为年-月-日或年/月/日,上次校准时间=%s' %data['上次校准时间'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['复校时间']) or not checkDate(data['复校时间']):
                    flash('失败:复校时间格式为年-月-日或年/月/日,复校时间=%s' %data['复校时间'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkCompareDate(data['上次校准时间'],data['复校时间']):
                    flash('失败:复校时间不能小于上次校准时间,上次校准时间=%s,复校时间=%s' %(data['上次校准时间'],data['复校时间']),'err')
                    return redirect(url_for('main.show',name=depot.name))
                kwargs = {'name':depot.name,'assetnumber':data['资产编号'],'product_name':data['品牌'],'model_name':data['规格型号'],'numbers':data['数量(套/个)'],'owner':data['责任组/人'],'position':data['储位'],'calibratetime':data['上次校准时间'],'resumptiontime':data['复校时间'],'status':status_dict[data['状态']],'remark':data['备注'],'profit_loss':data['盘盈/盘亏']} 
                if status_dict[data['状态']] == '1':
                    if not checkEmpty(data['借用人']):
                        flash('失败:在库时借用人必须为空,借用人=%s' %data['借用人'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if not checkEmpty(data['借用邮箱']):
                        flash('失败:在库时借用邮箱必须为空,借用邮箱=%s' %data['借用邮箱'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                elif status_dict[data['状态']] == '2':
                    if checkEmpty(data['借用人']):
                        flash('失败:借用人不能为空,借用人=%s' %data['借用人'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['借用邮箱']) or not checkEmail(data['借用邮箱']):
                        flash('失败:借用邮箱不能为空,且格式符合邮箱要求,借用邮箱=%s' %data['借用邮箱'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['借用时间']) or not checkDate(data['借用时间']):
                        flash('失败:借用时间格式为年-月-日或年/月/日,借用时间=%s' %data['借用时间'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['预计归还时间']) or not checkDate(data['预计归还时间']):
                        flash('失败:预计归还时间格式为年-月-日或年/月/日,预计归还时间=%s' %data['预计归还时间'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkCompareDate(data['借用时间'],data['预计归还时间']):
                        flash('失败:预计归还时间不能小于借机时间,借用时间=%s,预计归还时间=%s' %(data['借用时间'],data['预计归还时间']),'err')
                        return redirect(url_for('main.show',name=depot.name))
                    userinfo = {'username':data['借用人'],'usermail':data['借用邮箱'],'lend_time':data['借用时间'],'back_time':data['预计归还时间']}
                    kwargs.update(userinfo)
                cmp = T2(**kwargs)
                if T2.query.filter_by(assetnumber = data['资产编号']).count() > 0:
                    flash('失败:编号为%s的资产已存在' %data['资产编号'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                db.session.add(cmp)
            db.session.commit()
            flash('上传成功','success') 
            return redirect(url_for('main.show',name=depot.name))
        elif template_id == 3:
            head = ['资产编号','品牌','规格型号','数量(套/个)','部门','组别','储位','上次校准时间','复校时间','状态','借用人','借用邮箱','借用数量','借用时间','备注','盘盈/盘亏']
            if not checkHead(head,datas[0]):
                flash("失败:上传文件表头信息错误,正确的表头信息为%s" %head,'err')
                return redirect(url_for('main.show',name=depot.name))
            #检查内容是否符合格式
            datas.remove(datas[0])
            for data in datas:
                if T3.query.filter_by(assetnumber=data['资产编号']).count() > 0:
                    flash('失败:资产编号已存在','err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['资产编号']) or not checkType(data['资产编号']):
                    flash('失败:资产编号不能为空,且只能输入数字、字母和下划线,资产编号=%s' %data['资产编号'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['品牌']):
                    flash('失败:品牌不能为空=%s' %data['品牌'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['规格型号']):
                    flash('失败:规格型号不能为空=%s' %data['规格型号'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['数量(套/个)']) or not  checkInt(data['数量(套/个)']):
                    flash('失败:数量不能为空,且只能是整数,数量(套/个)=%s' %data['数量(套/个)'],'err')    
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['部门']):
                    flash('失败:部门不能为空,部门=%s' %data['部门'],'err')    
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['组别']) or not  checkType2(data['组别']):
                    flash('失败:组别不能为空,且只能输入数字、字母、下划线和中文,组别=%s' %data['组别'],'err')    
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['储位']) or not  checkType2(data['储位']):
                    flash('失败:储位不能为空,且只能输入数字、字母、中文和下划线,储位=%s' %data['储位'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['上次校准时间']) or not checkDate(data['上次校准时间']):
                    flash('失败:上次校准时间格式为年-月-日或年/月/日,上次校准时间=%s' %data['上次校准时间'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkEmpty(data['复校时间']) or not checkDate(data['复校时间']):
                    flash('失败:复校时间格式为年-月-日或年/月/日,复校时间=%s' %data['复校时间'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                if checkCompareDate(data['上次校准时间'],data['复校时间']):
                    flash('失败:复校时间不能小于上次校准时间,上次校准时间=%s,复校时间=%s' %(data['上次校准时间'],data['复校时间']),'err')
                    return redirect(url_for('main.show',name=depot.name))
                kwargs = {'name':depot.name,'assetnumber':data['资产编号'],'product_name':data['品牌'],'model_name':data['规格型号'],'numbers':data['数量(套/个)'],'department':data['部门'],'owner':data['组别'],'position':data['储位'],'calibratetime':data['上次校准时间'],'resumptiontime':data['复校时间'],'status':status_dict[data['状态']],'remark':data['备注'],'profit_loss':data['盘盈/盘亏']} 
                if status_dict[data['状态']] == '1':
                    if not checkEmpty(data['借用人']):
                        flash('失败:在库时借用人必须为空,借用人=%s' %data['借用人'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if not checkEmpty(data['借用邮箱']):
                        flash('失败:在库时借用邮箱必须为空,借用邮箱=%s' %data['借用邮箱'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if not checkEmpty(data['借用数量']):
                        flash('失败:在库时借用数量必须为空,借用数量=%s' %data['借用数量'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                if status_dict[data['状态']] == '2':
                    if checkEmpty(data['借用人']):
                        flash('失败:借用人不能为空,借用人=%s' %data['借用人'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['借用邮箱']) or not checkEmail(data['借用邮箱']):
                        flash('失败:借用邮箱不能为空,且格式符合邮箱要求,借用邮箱=%s' %data['借用邮箱'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['借用数量']) or not checkInt(data['借用数量']):
                        flash('失败:借用数量不能为空,且只能输入整数,借用数量=%s' %data['借用数量'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    if checkEmpty(data['借用时间']) or not checkDate(data['借用时间']):
                        flash('失败:借用时间格式为年-月-日或年/月/日,借用数量=%s' %data['借用数量'],'err')
                        return redirect(url_for('main.show',name=depot.name))
                    userinfo = {'username':data['借用人'],'usermail':data['借用邮箱'],'lend_time':data['借用时间'],'lend_numbers':data['借用数量']}
                    kwargs.update(userinfo)
                cmp = T3(**kwargs)
                if T3.query.filter_by(assetnumber = data['资产编号']).count() > 0:
                    flash('失败:编号为%s的资产已存在' %data['资产编号'],'err')
                    return redirect(url_for('main.show',name=depot.name))
                db.session.add(cmp)
            db.session.commit()
            flash('上传成功','success') 
            return redirect(url_for('main.show',name=depot.name))



# 仓库内容导出
@main_bp.route('/<name>/explore',methods=['GET'])       
@login_required
def explore(name):
    if not os.path.exists(current_app.config['DOWNLOAD_PATH']):
        os.mkdir(current_app.config['DOWNLOAD_PATH'])
    filename = '%s_%s.xls' %(name,datetime.now().strftime("%Y-%m-%d_%H%M%S"))
    path = os.path.join(current_app.config['DOWNLOAD_PATH'], filename)
    print("path=",path)
    depot = Depot.query.filter_by(name = name).first()
    template_id = depot.template_id
    data = []
    status_dict = {'1':'在库','2':'借出'}
    if template_id == 1:
        cmps = T1.query.filter_by(name=name).all()
        print("cmps=",cmps)
        head = ['资产编号','品牌','规格型号','现存数量','储位','入库时间','状态','借机人','借机邮箱','借机时间','借机数量','预计归还时间','备注','盘盈/盘亏']
        sql_key = ['assetnumber','product_name','model_name','numbers','position','entertime','status','username','usermail','lend_time','lend_numbers','back_time','remark','profit_loss']
        content = [[cmp.assetnumber,cmp.product_name,cmp.model_name,cmp.numbers,cmp.position,cmp.entertime.strftime("%Y-%m-%d"),status_dict[cmp.status],cmp.username,cmp.usermail,cmp.lend_time.strftime("%Y-%m-%d"),cmp.lend_numbers,cmp.back_time.strftime("%Y-%m-%d"),cmp.remark,cmp.profit_loss] for cmp in cmps]
    elif template_id == 2:
        cmps = T2.query.filter_by(name=name).all()
        print("cmps=",cmps)
        head = ['资产编号','品牌','规格型号','数量(套/个)','责任组/人','储位','上次校准时间','复校时间','状态','借用人','借用邮箱','借用时间','预计归还时间','备注','盘盈/盘亏']
        sql_key = ['assetnumber','product_name','model_name','numbers','position','calibratetime','resumptiontime','status','username','usermail','lend_time','back_time','remark','profit_loss']
        content = [[cmp.assetnumber,cmp.product_name,cmp.model_name,cmp.numbers,cmp.owner,cmp.position,cmp.calibratetime.strftime("%Y-%m-%d"),cmp.resumptiontime.strftime("%Y-%m-%d"),status_dict[cmp.status],cmp.username,cmp.usermail,cmp.lend_time.strftime("%Y-%m-%d"),cmp.back_time.strftime("%Y-%m-%d"),cmp.remark,cmp.profit_loss] for cmp in cmps]
    elif template_id == 3:    
        cmps = T3.query.filter_by(name=name).all()
        print("cmps=",cmps)
        head = ['资产编号','品牌','规格型号','数量(套/个)','部门','组别','储位','上次校准时间','复校时间','状态','借用人','借用邮箱','借用数量','借用时间','备注','盘盈/盘亏']
        sql_key = ['assetnumber','product_name','model_name','numbers','department','owner','position','calibratetime','resumptiontime','status','username','usermail','lend_time','remark','profit_loss']
        content = [[cmp.assetnumber,cmp.product_name,cmp.model_name,cmp.numbers,cmp.department,cmp.owner,cmp.position,cmp.calibratetime.strftime("%Y-%m-%d"),cmp.resumptiontime.strftime("%Y-%m-%d"),status_dict[cmp.status],cmp.username,cmp.usermail,cmp.lend_time.strftime("%Y-%m-%d"),cmp.remark,cmp.profit_loss] for cmp in cmps]
    data.append(head)
    print("data=",data)
    data.extend(content)
    print("********data=",data) 
    write_excel(data,path)
    return send_from_directory(current_app.config['DOWNLOAD_PATH'],filename,as_attachment=True)
   
    
    
    
    
    
    
    
    
    
    
