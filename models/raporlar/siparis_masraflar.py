from marshmallow import Schema,fields


class SiparisMasrafSchema(Schema):
    id = fields.Int()
    tur = fields.String()
    aciklama = fields.String()
    tutar = fields.Float()
    ozel_iscilik = fields.Float()
    ilaclamatutar = fields.Int()
    ilaclamatur = fields.String()

class SiparisMasrafModel:
    id = None
    tur = ""
    aciklama = ""
    tutar = 0
    ozel_iscilik = 0
    ilaclamatutar = 0
    ilaclamatur = ""