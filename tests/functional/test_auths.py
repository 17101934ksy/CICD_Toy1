from project import create_app, db
from project.models import User

from flask_migrate import Migrate

import os
from sys import exit

def test_register(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET)
    THEN check that the response is valid id, password, email
    """
    response = test_client.get('/user-register')
    assert response.status_code == 200
    assert b'register' in response.data
