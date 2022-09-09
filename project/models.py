from project import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, String, Integer
from project.utils import generate_integer

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    password_hashed = Column(String(128), nullable=False)
    email = Column(String(70), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    phone = Column(String(15), nullable=False)
    address = Column(String(70), nullable=False)
    

    def __init__(self, email: str, password_plaintext: str, phone: str):
        self.email = email
        self.password_hashed = self._generate_password_hash(password_plaintext)
        self.phone = self._generate_integer(phone)

    @staticmethod
    def _generate_password_hash(password_plaintext: str):
        return generate_password_hash(password_plaintext)

    @staticmethod
    def _generate_integer(phone: str):
        return generate_integer(phone)
        

