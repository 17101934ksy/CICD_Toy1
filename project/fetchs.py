from project.models import User, Music
from sqlalchemy import and_

def fetch_unique_email(email):
    """유저 이메일로 users 테이블의 데이터를 가져오는 함수

    Args:
        email (string): 유저 이메일(unique)

    Returns:
        _type_: None or data
    """
    user = User.query.filter_by(email=email).first()
    return user

def fetch_unique_music(name, artist, release):
    music = Music.query.filter(and_(Music.name==name, Music.artist==artist, Music.release==release)).first()

    return music

