from marshmallow import Schema,fields


class MusteriOdemeSecimSchema(Schema):
    id = fields.Int()
    siparisno= fields.String()
    tutar = fields.Float()
    aciklama = fields.String()
    masraf = fields.Float()
    faturatur = fields.String()
    sira = fields.Int()
    kur = fields.Float()

class MusteriOdemeSecimModel:
    id = None
    siparisno = ""
    tutar = 0
    aciklama = ""
    masraf = 0 
    faturatur = ""
    sira = 0
    kur = 0