# from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from app.model.EmployeeModel import EmployeeModel
# from app.schema.EmployeesSchemas import EmployeeSchemas
# from app.utils.db import db
# from sqlalchemy.exc import SQLAlchemyError

# blp = Blueprint("employees", __name__, description="employees view")

# @blp.route("/employees")
# class AnimalsView(MethodView):
#     @blp.response(200, EmployeeSchemas(many=True))
#     def get(self):
#         items = EmployeeModel.query.all()
#         return items

#     @blp.arguments(EmployeeSchemas)
#     @blp.response(201, EmployeeSchemas)
#     def post(self, item_data):
#         print (item_data)
#         item = EmployeeModel(**item_data)
#         try:
#             db.session.add(item)
#             db.session.commit()
#         except SQLAlchemyError:
#             abort(500, message="An error occurred while inserting the item.")
#         return item
    