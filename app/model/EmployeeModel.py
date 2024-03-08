from app.utils.db import db
from app.model.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Text

class EmployeeModel(db.Model):
    __tablename__ = "employee_table"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(100), nullable=False)
    role = mapped_column(String(100), nullable=False)
    schedule = mapped_column(String(100), nullable=False)

    def __init__(self, name:str, role:str, schedule:str ):
        self.name = name
        self.role = role
        self.schedule = schedule

    def update(self, name:str, role:str, schedule:str ):
        print(name, role, schedule)
        self.name = name
        self.role = role
        self.schedule = schedule

        
