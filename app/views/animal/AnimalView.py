# from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from app.model.AnimalModel import AnimalModel
# from app.schema.AnimalsSchemas import AnimalSchemas
# from app.utils.db import db
# from sqlalchemy.exc import SQLAlchemyError

# blp = Blueprint("animal", __name__, description="Animal view")

# @blp.route("/animal/<string:animal_id>")
# class AnimalsView(MethodView):
#     @blp.response(200, AnimalSchemas)
#     def get(self, animal_id):
#         print(animal_id)
#         print("test")
#         item = AnimalModel.query.get_or_404(1)
#         return item

#     @blp.arguments(AnimalSchemas)
#     @blp.response(201, AnimalSchemas)
#     def put(self, item_data, animal_id):
#         print (item_data)
#         item = AnimalModel.query.get_or_404(animal_id)
#         item.update(**item_data)
#         db.session.add(item)
#         db.session.commit()
#         # self.dbSession.commit()
#         return item
    
#     def delete(self, animal_id):
#         item = AnimalModel.query.get_or_404(animal_id)
#         db.session.delete(item)
#         db.session.commit()
#         return{"message": "Item deleted."}
#         # self.dbSession.commit()
    