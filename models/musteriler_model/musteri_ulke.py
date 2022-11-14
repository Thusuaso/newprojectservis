from marshmallow import Schema,fields


class MusteriUlkeSchema(Schema):
    id = fields.Int()
    ulke_adi = fields.String()
    logo = fields.String()

class MusteriUlkeModel:
    id = None
    ulke_adi = ""
    logo = ""