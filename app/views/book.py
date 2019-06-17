# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, current_app, request, Blueprint,send_from_directory
from flask_login import login_required, current_user, fresh_login_required, logout_user
from app.forms.book import BookForm
from app.forms.main import UploadForm
from app.models import Book
from .. import db
from app.utils import redirect_back,rename_file,allowed_file,read_excel,write_excel,\
checkHead,checkInt,checkNumber,checkType,checkEmpty,checkNumber,checkType,checkType2,checkDate,checkCompareDate,checkEmail,checkLength
from app.decorators import admin_required
from sqlalchemy import or_
import os
from datetime import datetime
import re

book_bp = Blueprint('book', __name__)

#图书列表
@book_bp.route('/book/index')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['BOOK_PER_PAGE']
    q =  request.args.get('q','')
    if q:
        per_page = current_app.config['BOOK_PER_PAGE']
        pagination = Book.query.filter(
                                                or_(
                                                        Book.booknumber.like("%"+q+"%"),
                                                        Book.username.like("%"+q+"%"),
                                                        Book.bookname.like("%"+q+"%"),
                                                        Book.position.like("%"+q+"%")
                                                        
                                                )
                                            ).paginate(page, per_page)
        books = pagination.items
    else:
        pagination = Book.query.paginate(page, per_page)
    books = pagination.items
    form = UploadForm()
    return render_template('book/index.html', pagination=pagination, books=books,form=form)

#添加图书
@book_bp.route('/book/settings/add',methods=['GET','POST']) 
@login_required
@admin_required
def add():
    print("start")
    form = BookForm()
    print("check")
    if form.validate_on_submit():
        print("write")
        booknumber = form.booknumber.data
        bookname = form.bookname.data
        numbers = form.numbers.data
        prices = form.prices.data
        position = form.position.data
        status = form.status.data
        book = {"booknumber":booknumber,"bookname":bookname,"numbers":numbers,"prices":prices,"position":position,"status":status}
        if status == 2:
            username = form.username.data
            usermail = form.usermail.data
            lendtime = form.lendtime.data
            backtime = form.backtime.data
            userinfo  = {'username':username,'usermail':usermail,'lendtime':lendtime,'backtime':backtime}
            book.update(userinfo)
        if Book.query.filter_by(booknumber = booknumber).count() > 0:
            print("重复判断")
            flash('编号为%s的图书%s已存在' %(booknumber,bookname),'err')
            return render_template('book/settings/add.html',form=form)
        book = Book(**book)
        db.session.add(book)
        db.session.commit()
        flash('添加成功','success')
        print("添加成功")
        return redirect(url_for('book.index'))
    return render_template('book/settings/add.html',form=form)
    
 
#编辑图书
@book_bp.route('/book/settings/edit/<int:id>',methods=['GET','POST']) 
@login_required
@admin_required
def edit(id):
    form = BookForm()
    book = Book.query.get_or_404(id)
    if form.validate_on_submit():
        search_booknumber = Book.query.filter_by(booknumber = form.booknumber.data).first() 
        if Book.query.filter_by(booknumber = form.booknumber.data).count() > 0 and search_booknumber == form.booknumber.data:
            flash('编号为%s的图书%s已存在' %(form.booknumber.data,form.bookname.data),'err')
        else:
            book.booknumber = form.booknumber.data
            book.bookname = form.bookname.data
            book.numbers = form.numbers.data
            book.prices = form.prices.data
            book.position = form.position.data
            book.status = form.status.data
            if form.status.data == 1:
                book.username = None
                book.usermail =  None
                book.lendtime = datetime.now().strftime("%Y-%m-%d")
                book.backtime = datetime.now().strftime("%Y-%m-%d")
            elif form.status.data == 2:
                book.username = form.username.data
                book.usermail = form.usermail.data
                book.lendtime = form.lendtime.data
                book.backtime = form.backtime.data
            db.session.commit()
            flash('修改成功','success')
            return redirect(url_for('book.index'))
    form.booknumber.data = book.booknumber
    form.bookname.data = book.bookname 
    form.numbers.data = book.numbers
    form.prices.data = book.prices
    form.position.data = book.position
    form.username.data = book.username
    form.usermail.data = book.usermail
    form.lendtime.data = book.lendtime
    form.backtime.data = book.backtime
    # 数据库模型定义的string类型
    form.status.data = int(book.status)
    # print('book.status', book.status)
    return render_template('book/settings/edit.html',form=form)

#删除图书
@admin_required
@book_bp.route('/book/settings/del/<int:id>',methods=['GET','POST'])
@login_required
def delete(id):
    print(request.args)
    print(request.form)
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    flash('删除成功','success')
    # page = request.args.get('page',type=int)

    # return redirect(url_for('.index'))
    return redirect_back('book.index')

#全选删除
@book_bp.route('/book/settings/delall',methods=['GET','POST'])
@login_required
@admin_required
def delete_all():
    if request.method == 'POST':
        id = request.form.get('ids')
        print('id=', id)
        id = id.split(',')
        if 'on' in id:
            id.remove('on')
        if '' in id:
            id.remove('')
        print('id=', id)
        for i in id:
            book = Book.query.get_or_404(i)
            db.session.delete(book)
        db.session.commit()
        flash('删除成功','success')
        return redirect_back('book.index')


#上传
#读取excel文件中的内容并存入到mysql数据库
@book_bp.route('/book/upload',methods=['GET','POST'])       
@login_required
@admin_required
def upload():
    # print("request.files=",request.files)
    status_dict = {"在库":"1","借出":"2"}
    if request.method == 'POST' and 'file' in request.files:
        f = request.files.get('file')
        # print("f=",f)
        filename = rename_file(f.filename)
        # print("filename=",filename)
        if allowed_file(f.filename):
            # print("*******start upload*********")
            if not os.path.exists(current_app.config['UPLOAD_PATH']):
                os.mkdir(current_app.config['UPLOAD_PATH'])
            path = os.path.join(current_app.config['UPLOAD_PATH'], filename)
            f.save(path)
        else:
            # print("*******error *********")
            flash('失败:上传文件格式错误,请上传文件后缀为.xls和.xlsx的文件','err')
            return redirect(url_for('book.index'))
        datas = read_excel(path)
        # print("*******datas=",datas)
        #判断表格格式是否正确
        head =  ['图书编号','书名','数量','价格','储位','状态','借用人','借用邮箱','借用时间','预计归还时间']
        if not checkHead(head,datas[0]):
            flash("失败:上传文件表头信息错误,正确的表头信息为%s" %datas[0],'err')
            return  redirect(url_for('book.index'))
        #检查内容是否符合格式
        datas.remove(datas[0])
        for data in datas:
            if checkEmpty(data['图书编号']) or not checkType(data['图书编号']) or not checkLength(data['图书编号'],1,255):
                flash("失败:图书编号不能为空，且只能输入数字、字母和下划线,范围:1-255,图书编号=%s" %data['图书编号'],'err')
                return redirect(url_for('book.index'))
            if checkEmpty(data['书名']) or not checkType2(data['书名']) or not checkLength(data['书名'],1,255):
                flash("失败:书名不能为空，且只能输入数字、字母、中文和下划线,范围:1-255,书名=%s" %data['书名'],'err')
                return redirect(url_for('book.index'))
            if checkEmpty(data['价格']) or not checkNumber(data['价格']):
                flash("失败:价格不能为空，且只能输入整数或小数,价格=%s" %data['价格'],'err')
                return redirect(url_for('book.index'))
            if checkEmpty(data['储位']) or not checkType2(data['储位']) or not checkLength(data['储位'],1,255):
                flash("失败:储位不能为空，且只能输入数字、字母、中文和下划线,范围:1-255,储位=%s" %data['储位'],'err')
                return redirect(url_for('book.index'))
            # kwargs = {'booknumber':data['图书编号'],'bookname':data['书名'], 'numbers':data['数量'],'prices':data['价格'],'position':data['储位'],'status':status_dict[data['状态']]}
            kwargs = {'bookname':data['书名'], 'numbers':data['数量'],'prices':data['价格'],'position':data['储位'],'status':status_dict[data['状态']]}
            if status_dict[data['状态']] == '1':
                if not checkEmpty(data['借用人']):
                    flash('失败:在库时借用人必须为空,借用人=%s' %data['借用人'],'err')
                    return redirect(url_for('book.index'))
                if not checkEmpty(data['借用邮箱']):
                    flash('失败:在库时借用邮箱必须为空,借用邮箱=%s' %data['借用邮箱'],'err')
                    return redirect(url_for('book.index'))
            elif status_dict[data['状态']] == '2':
                if checkEmpty(data['借用人']):
                    flash('失败:借用人不能为空,借用人=%s' %data['借用人'],'err')
                    return redirect(url_for('book.index'))
                if checkEmpty(data['借用时间']) or not checkDate(data['借用时间']):
                    flash("失败:借用时间格式为年-月-日或年/月/日,借用时间=%s" %data['借用时间'],'err')
                    return redirect(url_for('book.index'))
                if checkEmpty(data['预计归还时间']) or not checkDate(data['预计归还时间']):
                    flash("失败:预计归还时间格式为年-月-日或年/月/日,预计归还时间=%s" %data['预计归还时间'],'err')
                    return redirect(url_for('book.index'))
                if checkCompareDate(data['借用时间'],data['预计归还时间']):
                    flash('失败:预计归还时间不能小于借用时间,借用时间=%s,预计归还时间=%s' %(data['借用时间'],data['预计归还时间']),'err')
                    return redirect(url_for('book.index'))
                userinfo = {'username':data['借用人'],'usermail':data['借用邮箱'],'lend_time':data['借用时间'],'back_time':data['预计归还时间']}
                kwargs.update(userinfo)
            if Book.query.filter_by(booknumber = data['图书编号']).count() > 0:
                flash('失败:编号为%s的图书%s已存在' %(data['图书编号'],data['书名']),'err')
                return redirect(url_for('book.index'))
            db.session.add(**kwargs)
        db.session.commit()
        flash('上传成功','success')
        return redirect(url_for('book.index'))
        
           
#下载
@book_bp.route('/book/explore',methods=['GET'])       
@login_required
def explore():
    if not os.path.exists(current_app.config['DOWNLOAD_PATH']):
        os.mkdir(current_app.config['DOWNLOAD_PATH'])
    filename = "图书_%s.xls" %(datetime.now().strftime("%Y-%m-%d_%H%M%S"))
    path = os.path.join(current_app.config['DOWNLOAD_PATH'],filename)
    books = Book.query.all()
    print("books=",books)
    head = ['图书编号','书名','数量','价格','储位','状态','借用人','借用邮箱','借用时间','预计归还时间']
    data = []
    data.append(head)
    print("data=",data)
    status_dict = {'1':'在库','2':'借出'}
    content = [[book.booknumber,book.bookname,book.numbers,book.prices,book.position,status_dict[book.status],book.username,book.usermail,book.lendtime.strftime("%Y-%m-%d"),book.backtime.strftime("%Y-%m-%d")] for book in books]
    data.extend(content)
    print(data)  
    write_excel(data,path)
    return send_from_directory(current_app.config['DOWNLOAD_PATH'],filename,as_attachment=True)

        
        

        
        
        
            




