from marshmallow import Schema,fields


class TedarikciFaturaSchema(Schema):
    id = fields.Int()
    link = fields.String()
    evrak_adi = fields.String()

class TedarikciFaturaModel:
    id = None
    link = ""
    evrak_adi = ""