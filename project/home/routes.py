from flask import render_template, request, redirect, url_for, session, jsonify

from project import db, login_manager
from project.home import bp

@bp.route('/')
def index():
    return "hello flask"