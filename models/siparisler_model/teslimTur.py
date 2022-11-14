from marshmallow import Schema,fields


class TeslimTurSchema(Schema):
    id = fields.Int()
    teslimTurAdi = fields.String()

class TeslimTurModel:
    id = None
    teslimTurAdi = fields.String()