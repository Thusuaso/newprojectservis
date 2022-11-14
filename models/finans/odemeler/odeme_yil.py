from marshmallow import Schema,fields



class OdemeYilSchema(Schema):
    id = fields.Int()
    yil = fields.Int()

class OdemeYilModel:

    id = None
    yil = 0