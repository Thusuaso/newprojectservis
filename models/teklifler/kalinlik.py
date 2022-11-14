from marshmallow import Schema,fields


class KalinlikSchema(Schema):
    id = fields.Int()
    kalinlik = fields.String()
    sira = fields.Int()


class KalinlikModel:

    id = None
    kalinlik = ""
    sira = None

    