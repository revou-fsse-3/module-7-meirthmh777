# from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from app.model.EmployeeModel import EmployeeModel
# from app.schema.EmployeesSchemas import EmployeeSchemas
# from app.utils.db import db
# from sqlalchemy.exc import SQLAlchemyError

# blp = Blueprint("employee", __name__, description="Employee view")

# @blp.route("/employee/<string:employee_id>")
# class AnimalsView(MethodView):
#     @blp.response(200, EmployeeSchemas)
#     def get(self, employee_id):
#         print(employee_id)
#         print("test")
#         item = EmployeeModel.query.get_or_404(employee_id)
#         return item
 
#     @blp.arguments(EmployeeSchemas)
#     @blp.response(201, EmployeeSchemas)
#     def put(self, item_data, employee_id):
#         print (item_data)
#         item = EmployeeModel.query.get_or_404(employee_id)
#         item.update(**item_data)
#         db.session.add(item)
#         db.session.commit()
#         # self.dbSession.commit()
#         return item
    
#     def delete(self, employee_id):
#         item = EmployeeModel.query.get_or_404(employee_id)
#         db.session.delete(item)
#         db.session.commit()
#         return{"message": "Item deleted."}
#         # self.dbSession.commit()
    