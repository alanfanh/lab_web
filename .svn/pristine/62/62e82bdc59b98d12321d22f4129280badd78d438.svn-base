#-*-coding:utf-8-*-
from flask import render_template
from .auth import auth_bp
from .main import main_bp
from .user import user_bp
from .book import book_bp
from .depot import depot_bp


@auth_bp.errorhandler(404)
@main_bp.errorhandler(404)
@user_bp.errorhandler(404)
@book_bp.errorhandler(404)
@depot_bp.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'),404


@auth_bp.errorhandler(403)
@main_bp.errorhandler(403)
@user_bp.errorhandler(403)

@book_bp.errorhandler(403)
@depot_bp.errorhandler(403)
def permission_denied(e):
    return  render_template('errors/403.html'),403

@auth_bp.errorhandler(401)
@main_bp.errorhandler(401)
@user_bp.errorhandler(401)
@book_bp.errorhandler(401)
@depot_bp.errorhandler(401)
def unauthorized(e):
    return 'You not authorized to visit this page', 401

@auth_bp.errorhandler(500)
@main_bp.errorhandler(500)
@user_bp.errorhandler(500)
@book_bp.errorhandler(500)
@depot_bp.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'),500
    