from marshmallow import Schema, fields

class AnimalSchemas(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    age = fields.Int()
    gender = fields.Str()
    species = fields.Str()
    special_requirements = fields.Str()



