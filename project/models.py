from project import db
from werkzeug.security import generate_password_hash
from sqlalchemy import Column, String, Integer, DATE, ForeignKey
from project.utils import generate_integer
from datetime import datetime, date

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(70), unique=True, nullable=False)
    password_hashed = Column(String(128), nullable=False)
    name = Column(String(255), nullable=False)
    phone = Column(String(15), nullable=False)
    address = Column(String(70), nullable=False)
    
    def __init__(self, email: str, password_plaintext: str, name: str, phone: str, address: str):
        self.email = email
        self.password_hashed = self._generate_password_hash(password_plaintext)
        self.name = name
        self.phone = self._generate_integer(phone)
        self.address = address

    @staticmethod
    def _generate_password_hash(password_plaintext: str):
        return generate_password_hash(password_plaintext)

    @staticmethod
    def _generate_integer(phone: str):
        return generate_integer(phone)
        
    def __repr__(self):
        return f'{self.email}'

class Music(db.Model):
    __tablename__ = 'musics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    artist = Column(String(30), nullable=False)
    composer = Column(String(15), nullable=False)
    lyricist = Column(String(15), nullable=False)
    release = Column(DATE, nullable=False)

    def __init__(self, name: str, artist: str, composer: str, lyricist: str, release: date):
        self.name = name
        self.artist = artist
        self.composer = composer
        self.lyricist = lyricist
        self.release = release
    
    def __repr__(self):
        return f'{self.name}'

# class MusicViewer(db.Model):
#     __tablename__ = 'musicviewers'

#     id = Column(Integer, ForeignKey('musics.id'), primary_key=True, nullable=False)
#     viewer = Column(Integer, nullable=False)
#     heart = Column(Integer, nullable=False)

#     music = db.relationship('musics', backref='musicviewers')

#     def __init__(self):
#         self.viewer = 0
#         self.heart = 0
    
#     def __repr__(self):
#         return f'{self.viewer}'