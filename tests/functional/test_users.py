from project import create_app, db
from project.config import config_dict

from flask_migrate import Migrate

from sys import exit
import os

def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """


    DEBUG = (os.getenv('DEBUG', 'False') == 'True')

    get_config_mode = 'Debug' if DEBUG else 'Production'

    try:
        app_config = config_dict[get_config_mode.capitalize()]

    except KeyError:
        exit('Error: Invalid <config_mode>, Expected values [Debug, Production] ')

    flask_app = create_app(app_config)
    Migrate(flask_app, db)

    # if not DEBUG:
    #     Minify(app=flask_app, html=True, js=False, cssless=False)

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        # assert b'Flask User Management Example!' in response.data
        # assert b'Need an account?' in response.data
        # assert b'Existing user?' in response.data