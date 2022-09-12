from project.models import User
from project import create_app, db
from project.config import config_test_dict

from flask_migrate import Migrate

from sys import exit
import os, pytest

def flask_config():
    """플라스크 config 생성

    Returns:
        _object_: config 객체
    """
    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    get_config_mode = 'Debug' if DEBUG else 'Production'
    try:
        app_config = config_test_dict[get_config_mode.capitalize()]
    except KeyError:
        exit('Error: Invalid <config_mode>, Expected values [Debug, Production] ')

    return app_config


@pytest.fixture(scope='module')
def new_user():
    user = User('admin@admin.com', '12341234', 'admin', '010-1111-1111', 'seoul')
    return user

@pytest.fixture(scope='module')
def test_client():

    flask_app = create_app(flask_config())

    with flask_app.test_client() as testing_client:
        yield testing_client

