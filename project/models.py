from project import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(70), unique=True, nullable=False)
    password_hashed = Column(String(128), nullable=False)

    def __init__(self, email: str, password_plaintext: str):
        self.email = email
        self.password_hashed = self._generate_password_hash(password_plaintext)

    @staticmethod
    def _generate_password_hash(password_plaintext: str):
        return generate_password_hash(password_plaintext)