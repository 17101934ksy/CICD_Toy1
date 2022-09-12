from flask import render_template, request, redirect, url_for, session, jsonify
from jinja2 import TemplateNotFound, TemplateAssertionError

from project import db, login_manager
from project.music import bp
from project.fetchs import fetch_unique_music
from project.models import Music

from datetime import date

@bp.route('/<template>')
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'

        segment = get_segment(request)
        return render_template("music/" + template, segment=segment)

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


@bp.route('/music')
def index():
    return "hello flask"

@bp.route('/register-music', methods=['GET', 'POST'])
def register_music():
    
    if request.method == 'POST':
        data = request.get_json()
        
        year, month, day = map(int, data['release'].split(','))
        release = date(year, month, day)

        music = fetch_unique_music(data['name'], data['artist'], release)

        if music is None:
            try:
                music = Music(name=data['name'], artist=data['artist'], composer=data['composer'], lyricist=data['lyricist'], release=release)
                db.session.add(music)
                db.session.commit()
                return "register complete"
            except:
                return "register error"
        return "music exists"

    return "music register"
    
    