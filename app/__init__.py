from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from app.utils.db import db
# from app.views.animal.AnimalsView import blp as AnimalsView
# from app.views.animal.AnimalView import blp as AnimalView
# from app.views.employee.EmployeesView import blp as EmployeesView
# from app.views.employee.EmployeeView import blp as EmployeeView

# ----------
from app.model.AnimalModel import AnimalModel
from app.model.EmployeeModel import EmployeeModel
from app.controllers.animal_controller import animal_routes
from app.controllers.employee_controller import employee_routes
from sqlalchemy import select, text
from sqlalchemy.orm import sessionmaker
from app.connectors.connector import engine, connection
from app.controllers.employee_register_controller import employee_register_routes
from dotenv import load_dotenv
from flask_login import LoginManager
import os
from app.model.EmployeeRegisterModel import Registration

load_dotenv()

app = Flask(__name__)



app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
db.init_app(app)
with app.app_context():
    db.create_all()
api = Api(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# api.register_blueprint(AnimalsView)
# api.register_blueprint(AnimalView)
# api.register_blueprint(EmployeesView)
# api.register_blueprint(EmployeeView)

    # -----------
app.register_blueprint(animal_routes)
app.register_blueprint(employee_routes)
app.register_blueprint(employee_register_routes)

# user loader to search employee data to database
# is there any cookie data in each request?
login_manager = LoginManager()
login_manager.init_app(app)

# employee loader, check in database
@login_manager.user_loader
def load_employee(employee_id):
    connection = engine.connect()
    Session = sessionmaker(connection)
    session = Session()
    return session.query(Registration).get(int(employee_id))

@app.route('/')
def hello_universe():
    # SQL Way
    # Session = sessionmaker(connection)
    # with Session() as session:
    #     session.execute(text("INSERT INTO animal_table (name, age, gender, species, special_requirements) VALUES ('alex', 10, 'male', 'mammals', 'medication')"))
    #     session.execute(text("INSERT INTO animal_table (name, age, gender, species, special_requirements) VALUES ('gloria', 7, 'female', 'mammals', 'nothing')"))
    #     session.execute(text("INSERT INTO employee_table (name, role, schedule) VALUES ('gloria', 'nurse', 'morning')"))
    #     session.commit()


    animal_query = select(AnimalModel)
    # employee_query = select(AnimalModel)
    Session = sessionmaker(connection)
    with Session() as s:
        result_animal = s.execute(animal_query)
        # result_emlpoyee = s.execute(employee_query)
        for row in result_animal.scalars():
            print(f'ID: {row.id}, Name: {row.name}')
        # for row in result_emlpoyee.scalars():
        #     print(f'ID: {row.id}, Name: {row.name}')

    return "hello universe"

