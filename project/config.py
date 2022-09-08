import os

class Config(object):
    """Setup Config class

    Args:
        object (class): class
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('SECRET_KEY', 'b5a03A2G264207rZrXn5dOe2zRqvOvng8Fc4QgbKPFY')

    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        os.getenv('DB_ENGINE', 'mysql'),
        os.getenv('DB_USERNAME', 'root'),
        os.getenv('DB_PASS', '1234'),
        os.getenv('DB_HOST', 'localhost'),
        os.getenv('DB_PORT', 3306),
        os.getenv('DB_NAME', 'toy1')
    )

    SQLALCHEMY_TRACK_MODIATIONS = False
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static')

class ProductionConfig(Config):
    """Setup config to product

    Args:
        Config (class): parent class
    """
    DEBUG = False
    
    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

class DebugConfig(Config):
    """Setup config to debug

    Args:
        Config (class): parent class
    """
    DEBUG = True

config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}