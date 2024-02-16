from flask.views import MethodView
from flask_smorest import Blueprint, abort
from app.model.AnimalModel import AnimalModel
from app.schema.AnimalsSchemas import AnimalSchemas
from app.utils.db import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("animals", __name__, description="Animals viewvvvvvvvvvvvvvvvv")

@blp.route("/animals")
class AnimalsView(MethodView):
    @blp.response(200, AnimalSchemas(many=True))
    def get(self):
        items = AnimalModel.query.all()
        return items

    @blp.arguments(AnimalSchemas)
    @blp.response(201, AnimalSchemas)
    def post(self, item_data):
        print (item_data)
        item = AnimalModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")
        return item
    