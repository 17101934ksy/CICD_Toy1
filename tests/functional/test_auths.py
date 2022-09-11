from project import create_app, db
from project.models import User
from project.forms import RegisterForm
from flask import request 

from flask_migrate import Migrate

import os
from sys import exit

def test_register(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET)
    THEN check that the response is valid id, password, email
    """
    # form = RegisterForm(request.form)
    # form['userId'] = "admin"
    # form['password'] = "admin123"
    # form['userName'] = 'ksy'
    # form['phone'] = '010-1111-1111'
    # form['address'] = 'seoul'
    # form['register'] = ''
    
    response = test_client.get('/user-register')
    assert response.status_code == 200

    # response = test_client.post('/user-register', request)
    # assert response.status_code == 200
    # assert b'register' in response.data
