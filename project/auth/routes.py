from flask import render_template, request, redirect, url_for, session, jsonify

from project import db, login_manager
from project.auth import bp

@bp.route('/user-register')
def register():

    
    return "register"