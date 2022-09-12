from flask import render_template, request, redirect, url_for, session, jsonify
from jinja2 import TemplateNotFound, TemplateAssertionError

from project import db, login_manager
from project.home import bp


@bp.route('/<template>')
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'

        segment = get_segment(request)
        return render_template("home/" + template, segment=segment)

    except TemplateAssertionError:
        return render_template('errors/page-403.html'), 403
    except TemplateNotFound:
        return render_template('errors/page-404.html'), 404
    except:
        return render_template('errors/page-500.html'), 500

def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment
    except:
        return None




@bp.route('/home')
def index():
    return "hello flask"