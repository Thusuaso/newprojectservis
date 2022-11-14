from marshmallow import Schema,fields

class FaturaKesimTurSchema(Schema):
    id = fields.Int()
    faturaKesimTurAdi = fields.String()

class FaturaKesimTurModel:
    id = None
    faturaKesimTurAdi = ""