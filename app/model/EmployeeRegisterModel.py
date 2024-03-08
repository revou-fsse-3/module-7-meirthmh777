# from app.models.base import Base
from app.utils.db import db
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Text
import bcrypt
from flask_login import UserMixin

class Registration(db.Model, UserMixin):
    __tablename__='employee_register_table'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100), nullable=False)
    password = mapped_column(Integer, nullable=False)
    def __repr__(self):
        return f'<User {self.name}>'

    # hashing password poetry add bcrypt
    def set_password(self, password):
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    # check password in system
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))


