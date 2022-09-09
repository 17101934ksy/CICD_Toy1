from project import create_app, db
from project.config import config_dict

from flask_migrate import Migrate

from sys import exit
import os


def flask_config():
    """플라스크 config 생성

    Returns:
        _object_: config 객체
    """
    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    get_config_mode = 'Debug' if DEBUG else 'Production'
    try:
        app_config = config_dict[get_config_mode.capitalize()]
    except KeyError:
        exit('Error: Invalid <config_mode>, Expected values [Debug, Production] ')

    return app_config


def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'hello flask' in response.data
    # assert b'Need an account?' in response.data
        # assert b'Existing user?' in response.data