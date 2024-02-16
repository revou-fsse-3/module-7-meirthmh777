from app.utils.db import db

class AnimalModel(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    species = db.Column(db.String)
    special_requirements = db.Column(db.String)

    
    def __init__(self, name:str, age:int, gender:str, species:str, special_requirements:str ):
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species
        self.special_requirements = special_requirements

    def update(self, name:str, age:int, gender:str, species:str, special_requirements:str  ):
        print(name, age, gender, species, special_requirements)
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species
        self.special_requirements = special_requirements

        
