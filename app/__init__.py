from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from app.utils.db import db
from app.views.animal.AnimalsView import blp as AnimalsView
from app.views.animal.AnimalView import blp as AnimalView
from app.views.employee.EmployeesView import blp as EmployeesView
from app.views.employee.EmployeeView import blp as EmployeeView


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = Api(app)



    api.register_blueprint(AnimalsView)
    api.register_blueprint(AnimalView)
    api.register_blueprint(EmployeesView)
    api.register_blueprint(EmployeeView)
    return app

