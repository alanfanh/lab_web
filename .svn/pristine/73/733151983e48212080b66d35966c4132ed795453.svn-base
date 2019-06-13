# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, current_app, request, Blueprint
from flask_login import login_required, current_user, fresh_login_required, logout_user
from app.forms.depot import AddDepotForm
from app.models import Depot,T1,T2,T3,Template
from .. import db
from app.utils import redirect_back
from app.decorators import admin_required


depot_bp = Blueprint('depot', __name__)

#仓库列表
@depot_bp.route('/depot/index')
@login_required
@admin_required
def index():
        page = request.args.get('page', 1, type=int)
        per_page = current_app.config['DEPOT_PER_PAGE']
        pagination = Depot.query.paginate(page, per_page)
        depots = pagination.items
        return render_template('depot/index.html', pagination=pagination, depots=depots)

#添加仓库
@depot_bp.route('/depot/settings/add',methods=['GET','POST']) 
@login_required
@admin_required
def add():
    form = AddDepotForm()
    print(request.form)
    if form.validate_on_submit():
        name = form.depotname.data
        template = form.template.data
        print("*****template=",template)
        name_search = Depot.query.filter_by(name=name).first()
        if name_search:
            flash('仓库已存在','err')
            return redirect_back()
        depot = Depot(name=name,template_id=template)
        db.session.add(depot)
        db.session.commit()
        flash('添加成功','success')
        return redirect(url_for('depot.index'))
    return render_template('depot/settings/add.html',form=form)
    
    
#删除仓库
@depot_bp.route('/depot/settings/del/<int:id>',methods=['GET','POST']) 
@login_required
@admin_required
def delete(id):
    depot=Depot.query.get_or_404(id)
    db.session.delete(depot)
    db.session.commit()
    flash('删除成功','success')
    return redirect_back()
    
