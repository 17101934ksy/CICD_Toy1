from project.models import User

def fetch_unique_user(user_id):
    """유저 아이디로 users 테이블의 데이터를 가져오는 함수

    Args:
        user_id (string): 유저 아이디(pk)

    Returns:
        _type_ : None or data
    """
    user = User.query.filter_by(id=user_id).first()

    return user

def fetch_unique_email(email):
    """유저 이메일로 users 테이블의 데이터를 가져오는 함수

    Args:
        email (string): 유저 이메일(unique)

    Returns:
        _type_: None or data
    """
    user = User.query.filter_by(email=email).first()
    return user