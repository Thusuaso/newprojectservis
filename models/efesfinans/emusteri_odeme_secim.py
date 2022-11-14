from marshmallow import Schema,fields


class EfesMusteriOdemeSecimSchema(Schema):
    id = fields.Int()
    siparisno= fields.String()
    tutar = fields.Float()
    aciklama  = fields.String()
    masraf = fields.Float()

class EfesMusteriOdemeSecimModel:
    id = None
    siparisno = ""
    tutar = 0
    aciklama = ""
    masraf = 0
    