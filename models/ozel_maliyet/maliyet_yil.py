from marshmallow import Schema,fields


class MaliyetYilSchema(Schema):
    id = fields.Int()
    yil = fields.Int()

class MaliyetYilModel:
    id = None
    yil = 0