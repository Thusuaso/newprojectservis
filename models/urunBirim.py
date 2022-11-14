from marshmallow import Schema,fields


class UrunBirimSchema(Schema):
    id = fields.Int()
    birimAdi = fields.String()

class UrunBirimModel:
    id = None
    birimAdi = ""