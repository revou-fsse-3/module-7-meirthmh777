from flask import Blueprint, render_template, request, redirect
from app.connectors.connector import engine
from sqlalchemy import select
from app.model.EmployeeRegisterModel import Registration
from sqlalchemy.orm import sessionmaker
from flask_login import login_user, logout_user


employee_register_routes = Blueprint('employee_register_routes', __name__)

# get the employee
@employee_register_routes.route('/register', methods=['GET'])
def employee_register():
    return render_template("/employee_register.html")

@employee_register_routes.route('/register', methods=['POST'])
def employee_do_register():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    
    new_employee_register = Registration(name=name, email=email)
    new_employee_register.set_password(password)

    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    session.begin()
    try:
        session.add(new_employee_register)
        session.commit()
    except Exception as e:
        # operation failed
        session.rollback()
        print(e)
        return{'message': 'new employee failed do register'}
    # operation success
    return{'message': 'new employee success do register'}

@employee_register_routes.route('/login', methods=['GET'])
def employee_login():
    return render_template("/employee_login.html")

# check email if already exists
@employee_register_routes.route('/login', methods=['POST'])
def employee_do_login():
    # search employee
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()

    try:
        employee_try_login =  session.query(Registration).filter(Registration.email==request.form['email']).first()
        # check email is exists in db
        if employee_try_login == None:
            return{"message" : "email not found"}
        # check password
        if not employee_try_login.check_password(request.form['password']):
            return{"message" : "wrong password"}
        # if login ok
        login_user(employee_try_login, remember=False)
        return redirect('/animals')
    except Exception as e:
        session.rollback()
        print(e)
        return{'message': 'employee failed do login'}
    
# logout
@employee_register_routes.route('/logout', methods=['GET'])
def employee_do_logput():
    logout_user()
    return redirect('/login')