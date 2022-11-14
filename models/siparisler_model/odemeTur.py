from marshmallow import Schema,fields

class OdemeTurSchema(Schema):
    id = fields.Int()
    odemeTurAdi = fields.String()

class OdemeTurModel:
    id = None
    odemeTurAdi = ""