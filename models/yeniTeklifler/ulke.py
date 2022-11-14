from marshmallow import Schema,fields


class UlkeSchema(Schema):
    id = fields.Int()
    ulkeAdi = fields.String()
    kod = fields.String()
    iconFlags = fields.String()
    pngFlags = fields.String()

class UlkeModel:
    id = None 
    ulkeAdi = ""
    kod = ""
    iconFlags = ""
    pngFlags = ""