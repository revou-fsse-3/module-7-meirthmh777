from app.utils.db import db

class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    role = db.Column(db.String)
    schedule = db.Column(db.String)

    def __init__(self, name:str, role:str, schedule:str ):
        self.name = name
        self.role = role
        self.schedule = schedule

    def update(self, name:str, role:str, schedule:str ):
        print(name, role, schedule)
        self.name = name
        self.role = role
        self.schedule = schedule

        
