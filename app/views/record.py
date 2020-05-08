# -*- coding: utf-8 -*-
import os
from datetime import datetime
from flask import render_template, Blueprint, request, current_app, send_from_directory
from flask_login import login_required
from app.utils import write_excel
from app.models import Record
from sqlalchemy import or_
from .. import db


record_bp = Blueprint('record', __name__)


# 删除记录主页
@record_bp.route('/record/index')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['BOOK_PER_PAGE']
    q = request.args.get('q', '')
    if q:
        pagination = Record.query.filter(or_(Record.assetnumber.like("%"+q+"%"), Record.brand.like(
            "%"+q+"%"), Record.product.like("%"+q+"%"), Record.depotname.like("%"+q+"%"))).paginate(page, per_page)
        records = pagination.items
    else:
        pagination = Record.query.paginate(page, per_page)
    records = pagination.items
    return render_template('record/index.html', pagination=pagination, records=records)


# 导出记录数据
@record_bp.route('/record/explore', methods=['GET'])
@login_required
def explore():
    if not os.path.exists(current_app.config['DOWNLOAD_PATH']):
        os.mkdir(current_app.config['DOWNLOAD_PATH'])
    filename = "删除记录_%s.xls" %(datetime.now().strftime("%Y-%m-%d_%H%M%S"))
    path = os.path.join(current_app.config['DOWNLOAD_PATH'],filename)
    records = Record.query.all()
    head = ['记录编号','品牌','产品名','原所属仓库','删除时间']
    data = []
    data.append(head)
    status_dict = {'1':'在库','2':'借出'}
    content = [[record.assetnumber, record.brand, record.product,
                record.depotname, record.delete_time.strftime("%Y-%m-%d")] for record in records]
    data.extend(content)
    write_excel(data,path)
    return send_from_directory(current_app.config['DOWNLOAD_PATH'],filename,as_attachment=True)
