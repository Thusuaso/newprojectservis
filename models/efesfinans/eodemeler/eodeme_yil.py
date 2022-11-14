from marshmallow import Schema,fields



class EfesOdemeYilSchema(Schema):
    id = fields.Int()
    yil = fields.Int()

class EfesOdemeYilModel:

    id = None
    yil = 0