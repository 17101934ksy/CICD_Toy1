from flask import render_template, request, redirect, url_for, session, jsonify
from flask_login import logout_user, login_user

from project import db, login_manager
from project.auth import bp
from project.forms import RegisterForm
from project.fetchs import fetch_unique_email
from project.models import User

from werkzeug.security import check_password_hash

@bp.route('/')
def default_auth():
    try:
        if session['user_id'] is not None:

            return redirect(url_for('auth_bp.login'))
    except:
        return redirect(url_for('auth_bp.register'))


# @bp.route('/user-register', methods=['GET', 'POST'])
# def register():

#     register_form =  RegisterForm(request.form)

#     if 'register' in request.form and register_form.validate_on_submit():
#         user_id = request.form['userId']
#         user = fetch_unique_user(user_id)
#         print(request.form)

#         if user is None:
#             email = request.form['email']
#             email = fetch_unique_email(email)

#             if email is None:
#                 password = request.form['password']
#                 user_name = request.form['userName']
#                 phone = request.form['phone']
#                 address = request.form['address']

#                 # return redirect(url_for('auth_bp.login'))
#                 return "register complete"
#             return "email error"
#         return "user error"
#     return render_template('auth/register.html', form=register_form)


@bp.route('/register-user', methods=['GET', 'POST'])
def register():

    # register_form =  RegisterForm(request.form)

    if request.method == 'POST':
        data = request.get_json()

        email = fetch_unique_email(data['email'])

        if email is None:
            # return redirect(url_for('auth_bp.login'))
            user = User(email=data['email'], password_plaintext=data['password'], name=data['name'], phone=data['phone'], address=data['address'])
            db.session.add(user)
            db.session.commit()

            return "register complete"
        return "email exists"
    #return render_template('auth/register.html', form=register_form)
    return "register html"

# @bp.route('/user-login', methods=['GET', 'POST'])
# def login():

#     login_form = ''

#     if 'login' in request.form and login_form.validate_on_submit():
#         user = ''
#         session.clear()
#         session['user_id'] = user.userid
#         login_user(user)

#         return redirect(url_for('home_bp.index'))

#     return "login"

@bp.route('/login-user', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        data = request.get_json()
        
        user = fetch_unique_email(email=data['email'])

        if user is not None and check_password_hash(user.password_hashed, data['password']):

            session.clear()
            session['user_id'] = user.email
            # login_user(user)
            return "login complete"
        
        return "error"

    return "login"

@bp.route('/logout-user')
def logout():

    session.clear()
    try:
        if session['user_id'] is not None:
            return "session is valid logout error"
        else:
            return "logout error"
    except:
        return "logout complete"


@login_manager.unauthorized_handler
@bp.errorhandler(403)
def access_forbidden():
    return render_template('errors/page-403.html')


@bp.errorhandler(404)
def not_found_error():
    return render_template('errors/page-404.html')


@bp.errorhandler(500)
def internal_error():
    return render_template('errors/page-500.html')
