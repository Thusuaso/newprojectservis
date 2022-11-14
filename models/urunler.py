from marshmallow import Schema,fields


class UrunlerSchema(Schema):
    id = fields.Int()
    urunAdi = fields.String()
    kullaniciId = fields.Int()


class UrunlerModel:

    id = None
    urunAdi = ""
    kullaniciId = None
