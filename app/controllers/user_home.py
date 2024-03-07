from flask import Blueprint, render_template, request
from app.connectors.connector import Session
from sqlalchemy import select
from app.models.user_home import User


user_routes = Blueprint('user_routes', __name__)

# method get user by search
@user_routes.route('/user', methods=['GET'])
def user_home():
    response_data = dict()
    session = Session()
    try:
        user_query = select(User)
        if request.args.get('query') != None:
            search_query = request.args.get('query')
            user_query = user_query.where(User.name.like(f'%{search_query}%'))
        users = session.execute(user_query)
        users = users.scalars()
        response_data['users'] = users
    except Exception as e:
        print(e)
        return"error"
    return render_template("/user_home.html", response_data=response_data)

# insert new user
@user_routes.route('/user', methods=['POST'])
def user_new_insert():
    new_user = User(
        name = request.form['name'],
        email = request.form['email'],
        occupation = request.form['occupation']
    )
    session = Session()
    session.begin()
    try:
        session.add(new_user)
        session.commit()
    except Exception as e:
        # operation failed
        session.rollback()
        print(e)
        return{'message': 'insert new user failed'}
    # operation success
    return{'message': 'insert new user success'}

# delete certain user by it's id
@user_routes.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    session = Session()
    session.begin()
    try:
        user_to_delete = session.query(User).filter(User.id==id).first()
        session.delete(user_to_delete)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return{'message': 'delete user failed'}
    return{'message': 'delete user success'}

# update certain user by it's id
@user_routes.route('/user/<id>', methods=['PUT'])
def update_user(id):
    session = Session()
    session.begin()
    try:
        user_to_update = session.query(User).filter(User.id==id).first()
        user_to_update.name = request.form['name']
        user_to_update.email = request.form['email']
        user_to_update.occupation = request.form['occupation']
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return{'message': 'update user failed'}
    return{'message': 'update user success'}

