from flask import render_template, request, redirect, url_for, session, jsonify

from project import db, login_manager
from project.auth import bp

@bp.route('/')
def auth():
    return "hello flask"