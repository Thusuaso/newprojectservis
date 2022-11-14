from marshmallow import Schema,fields

class UrunOcakSchema(Schema):
    id = fields.Int()
    ocakAdi = fields.String()
    kullaniciId = fields.String()


class UrunOcakModel:

    id = None
    ocakAdi = ""
    kullaniciId = None

    