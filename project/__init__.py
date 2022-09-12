from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from importlib import import_module
from sqlalchemy import MetaData

naming_convention = {
    'ix': "ix_%(column_0_label)s",
    'uq': "uq_%(table_name)s_%(column_0_name)s",
    'ck': "ck_%(table_name)s_%(column_0_name)s",
    'fk': "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    'pk': "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
login_manager = LoginManager()

def register_extensions(app):
    """Register db, login_manager 

    Args:
        app (object): flask object
    """
    db.init_app(app)
    login_manager.init_app(app)

def register_blueprints(app):
    """Register blueprint

    Args:
        app (object): flask object
    """
    for module_name in ('auth','music'):
        module = import_module('project.{}.routes'.format(module_name))
        app.register_blueprint(module.bp)

def configure_database(app):
    """Database config setting

    Args:
        app (object): flask object
    """
    @app.before_request
    def initialize_database():
        db.create_all()
    
    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(config):
    """Create Flask app

    Args:
        config (object): config variables objects

    Returns:
        Flask app
    """
    app = Flask(__name__)

    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)

    return app