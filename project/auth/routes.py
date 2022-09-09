from flask import render_template, request, redirect, url_for, session, jsonify
from flask_login import login_user

from project import db, login_manager
from project.auth import bp
from project.forms import RegisterForm
from project.fetchs import fetch_unique_user

@bp.route('/user-register', methods=['GET', 'POST'])
def register():

    register_form =  RegisterForm(request.form)

    if 'register' in request.form and register_form.validate_on_submit():

        
        user = fetch_unique_user()
        return redirect(url_for('auth_bp.login'))

    return "register"

@bp.route('/user-login', methods=['GET', 'POST'])
def login():

    login_form = ''

    if 'login' in request.form and login_form.validate_on_submit():
        user = ''
        session.clear()
        session['user_id'] = user.userid
        login_user(user)

        return redirect(url_for('home_bp.index'))

    return redirect(url_for('home_bp.index'))