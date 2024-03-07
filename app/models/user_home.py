from app.models.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Text
class User(Base):
    __tablename__='user'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(100), nullable=False)
    email = mapped_column(String(100), nullable=False)
    occupation =mapped_column(Text, nullable=False)
    def __repr__(self):
        return f'<User {self.name}>'
