from app.utils.db import db
from app.model.base import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Text

class AnimalModel(db.Model):
    __tablename__ = "animal_table"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(100), nullable=False)
    age = mapped_column(Integer, nullable=False)
    gender = mapped_column(String(100), nullable=False)
    species = mapped_column(String(100), nullable=False)
    special_requirements = mapped_column(Text, nullable=False)
    def __repr__(self):
        return f'<Animal {self.name}>'
    
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

        
