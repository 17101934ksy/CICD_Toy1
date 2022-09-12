from project.models import User

def fetch_unique_email(email):
    """유저 이메일로 users 테이블의 데이터를 가져오는 함수

    Args:
        email (string): 유저 이메일(unique)

    Returns:
        _type_: None or data
    """
    user = User.query.filter_by(email=email).first()
    return user