from flask import Blueprint, render_template, request
from app.connectors.connector import Session
from sqlalchemy import select
from app.model.EmployeeModel import EmployeeModel
from flask_login import current_user, login_required

employee_routes = Blueprint('employee_routes', __name__)

# method get employee by search
@employee_routes.route('/employees', methods=['GET'])
@login_required
def employee_home():
    response_data = dict()
    session = Session()
    try:
        employee_query = select(EmployeeModel)
        if request.args.get('query') != None:
            search_query = request.args.get('query')
            employee_query = employee_query.where(EmployeeModel.name.like(f'%{search_query}%'))
        employees = session.execute(employee_query)
        employees = employees.scalars()
        response_data['employees'] = employees
        # logout 
        response_data['name'] = current_user.name
    except Exception as e:
        print(e)
        return"error"
    return render_template("/employee_home.html", response_data=response_data)

# insert new employee
@employee_routes.route('/employees', methods=['POST'])
def employee_new_insert():
    new_employee = EmployeeModel(
        name = request.form['name'],
        role = request.form['role'],
        schedule = request.form['schedule'],
    )
    session = Session()
    session.begin()
    try:
        session.add(new_employee)
        session.commit()
    except Exception as e:
        # operation failed
        session.rollback()
        print(e)
        return{'message': 'insert new employee failed'}
    # operation success
    return{'message': 'insert new employee success'}

# delete certain employee by it's id
@employee_routes.route('/employees/<id>', methods=['DELETE'])
def delete_employee(id):
    session = Session()
    session.begin()
    try:
        employee_to_delete = session.query(EmployeeModel).filter(EmployeeModel.id==id).first()
        session.delete(employee_to_delete)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return{'message': 'delete employee failed'}
    return{'message': 'delete employee success'}

# update certain employee by it's id
@employee_routes.route('/employees/<id>', methods=['PUT'])
def update_employee(id):
    session = Session()
    session.begin()
    try:
        employee_to_update = session.query(EmployeeModel).filter(EmployeeModel.id==id).first()
        employee_to_update.name = request.form['name']
        employee_to_update.role = request.form['role']
        employee_to_update.schedule = request.form['schedule']
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
        return{'message': 'update employee failed'}
    return{'message': 'update employee success'}


