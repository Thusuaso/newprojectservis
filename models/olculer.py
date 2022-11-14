from marshmallow import Schema,fields


class OlculerSchema(Schema):
    id = fields.Int()
    en = fields.String()
    boy = fields.String()
    kenar = fields.String()
    kullaniciId = fields.Int()


class OlculerModel:

    id = None
    en = ""
    boy = ""
    kenar = ""
    kullaniciId = None

    