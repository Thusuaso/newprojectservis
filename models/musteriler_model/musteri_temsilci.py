from marshmallow import Schema,fields


class MusteriTemsilciSchema(Schema):

    id = fields.Int()
    kullanici_adi = fields.String()


class MusteriTemsilciModel:
    id = None
    kullanici_adi = ""