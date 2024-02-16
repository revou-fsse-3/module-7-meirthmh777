from marshmallow import Schema, fields

class EmployeeSchemas(Schema):
    # id = fields.Int()
    id = fields.Int(dump_only=True)
    name = fields.Str()
    role = fields.Str()
    schedule = fields.Str()



