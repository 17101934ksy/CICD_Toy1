from project import create_app, db
from project.config import config_test_dict
from project.models import Music

from flask_migrate import Migrate

import json
from datetime import date


def test_music_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    
    response = test_client.get('/music')
    assert response.status_code == 200
    assert b'hello flask' in response.data

def test_register_music(test_client):
    """
    GIVEN register music
    WHEN the '/register-music' page is requested (GET, POST)
    THEN check that the response is valid music register
    """

    # test1
    response = test_client.get('/register-music')
    assert response.status_code == 200
    assert b'music register' in response.data

    # test2 노래 등록 성공  
    response = test_client.post(
        '/register-music',
        data=json.dumps({'name': 'After LIKE', 'artist': 'IVE', 'composer': 'admin', 'lyricist': 'admin', 'release': '2022, 9, 10'}),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    assert b'register complete' in response.data

    # test3 노래 등록 실패(music exists)
    response = test_client.post(
        '/register-music',
        data=json.dumps({'name': 'After LIKE', 'artist': 'IVE', 'composer': 'admin', 'lyricist': 'admin', 'release': '2022, 9, 10'}),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    assert b'music exists' in response.data

    music = Music.query.filter_by(name='After LIKE').first()
    db.session.delete(music)
    db.session.commit()

    # test4 노래 등록 실패(param error)
    response = test_client.post(
        '/register-music',
        data=json.dumps({'name': 'After LIKE', 'composer': 'admin', 'lyricist': 'admin', 'release': '2022, 9, 10'}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 500
