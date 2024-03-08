from flask import Blueprint, render_template, request
from app.connectors.connector import Session
from sqlalchemy import select
from app.model.AnimalModel import AnimalModel
from flask_login import current_user, login_required

animal_routes = Blueprint('animal_routes', __name__)

# method get animal by search

@animal_routes.route('/animals', methods=['GET'])
@login_required
def animal_home():
    response_data = dict()
    session = Session()
    try:
        animal_query = select(AnimalModel)
        if request.args.get('query') != None:
            search_query = request.args.get('query')
            animal_query = animal_query.where(AnimalModel.name.like(f'%{search_query}%'))
        animals = session.execute(animal_query)
        animals = animals.scalars()
        response_data['animals'] = animals
        # logout 
        response_data['name'] = current_user.name
    except Exception as e:
        print(e)
        return"error"
    return render_template("/animal_home.html", response_data=response_data)

# insert new animal
@animal_routes.route('/animals', methods=['POST'])
def animal_new_insert():
    new_animal = AnimalModel(
        name = request.form['name'],
        age = request.form['age'],
        gender = request.form['gender'],
        species = request.form['species'],
        special_requirements = request.form['special_requirements']
    )
    session = Session()
    session.begin()
    try:
        session.add(new_animal)
        session.commit()
    except Exception as e:
        # operation failed
        session.rollback()
        print(e)
        return{'message': 'insert new animal failed'}
    # operation success
    return{'message': 'insert new animal success'}

# delete certain animal by it's id
@animal_routes.route('/animals/<id>', methods=['DELETE'])
def delete_animal(id):
    session = Session()
    session.begin()
    try:
        animal_to_delete = session.query(AnimalModel).filter(AnimalModel.id==id).first()
        session.delete(animal_to_delete)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return{'message': 'delete animal failed'}
    return{'message': 'delete animal success'}

# update certain animal by it's id
@animal_routes.route('/animals/<id>', methods=['PUT'])
def update_animal(id):
    session = Session()
    session.begin()
    try:
        animal_to_update = session.query(AnimalModel).filter(AnimalModel.id==id).first()
        animal_to_update.name = request.form['name']
        animal_to_update.age = request.form['age']
        animal_to_update.gender = request.form['gender']
        animal_to_update.species = request.form['species']
        animal_to_update.special_requirements = request.form['special_requirements']
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return{'message': 'update animal failed'}
    return{'message': 'update animal success'}



