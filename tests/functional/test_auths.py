from project import create_app, db
from project.models import User
from project.forms import RegisterForm
from flask import request
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.wrappers import Request, Response
import json

from flask_migrate import Migrate

def test_register(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET, POST)
    THEN check that the response is valid email, password, name, phone, address
    """

    # test1
    response = test_client.get(
        '/user-register'
    )
    assert response.status_code == 200
    assert b'register html' in response.data

    # test2
    response = test_client.post(
        '/user-register', 
        data = json.dumps({'email': 'admin@admin.com', 'password': '12341234', 'name': 'admin', 'phone': '010-1111-1111', 'address': 'seoul'}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200 
    assert b'email exists' in response.data

    # test3
    response = test_client.post(
        '/user-register', 
        data = json.dumps({'email': 'admin2@admin.com', 'password': '12341234', 'name': 'admin', 'phone': '010-1111-1111', 'address': 'seoul'}),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200 
    assert b'register complete' in response.data
    user = User.query.filter_by(email='admin2@admin.com').first()
    db.session.delete(user)
    db.session.commit()


def test_login(test_client):
    """
    GIVEN user login
    WHEN the '/user-login' page is requested (POST)
    THEN check that the response is valid email, password
    """

    # test1
    response = test_client.get(
        '/user-login'
    )
    assert response.status_code == 200
    assert b'login' in response.data

    # test2 로그인 성공
    response = test_client.post(
        '/user-login',
        data=json.dumps({'email': 'admin@admin.com', 'password': '12341234'}),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    assert b'login complete' in response.data

    # test3 로그인 실패(email none)
    response = test_client.post(
        '/user-login',
        data = json.dumps({'email': 'test@test.com', 'password': '12341234'}),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    assert b'error' in response.data
    
    # test3 로그인 실패(password error)
    response = test_client.post(
        '/user-login',
        data=json.dumps({'email': 'admin@admin.com', 'password':'1234123'}),
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    assert b'error' in response.data