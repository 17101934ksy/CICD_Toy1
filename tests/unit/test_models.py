from project.models import User

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password_hashed fileds are defined correctly
    """
    user = User('gosunsangtrip@gmail.com', 'FlaskPassword123')
    assert user.email == 'gosunsangtrip@gmail.com'
    assert user.password_hashed != 'FlaskPassword123'