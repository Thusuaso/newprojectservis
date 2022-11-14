from marshmallow import Schema,fields


class UrunSchema(Schema):
    id = fields.Int()
    urunAdi = fields.String()
    sira = fields.Int()

class UrunModel:
    id = None 
    urunAdi = ""
    sira = 0