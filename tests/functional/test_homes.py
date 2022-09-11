from project import create_app, db
from project.config import config_dict

from flask_migrate import Migrate

from sys import exit
import os


def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    
    response = test_client.get('/home')
    assert response.status_code == 200
    assert b'hello flask' in response.data
    # assert b'Need an account?' in response.data
        # assert b'Existing user?' in response.data