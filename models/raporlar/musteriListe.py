from marshmallow import Schema,fields


class MusteriListeSchema(Schema):
    id = fields.Int()
    musteriAdi = fields.String()
    bakiye = fields.Float()
    Yenipesinat = fields.Float()
    Eskipesinat =fields.Float()
    odeme = fields.Float()
    siparisBedel = fields.Float()

class MusteriListeModel:
    id = None
    musteriAdi = ""
    bakiye = 0
    Yenipesinat = 0
    Eskipesinat = 0
    odeme = 0
    siparisBedel = 0