from marshmallow import Schema,fields


class MaliyetAySchema(Schema):
    id = fields.Int()
    ay = fields.Int()
    ay_str = fields.String()

class MaliyetAyModel:
    id = None
    ay = 0
    ay_str = ""