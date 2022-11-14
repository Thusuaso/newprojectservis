from marshmallow import Schema,fields


class OdemelerSchema(Schema):
    id = fields.Int()
    tarih = fields.Date()
    musteriId = fields.Int()
    siparisNo = fields.String()
    siparisId = fields.Int()
    finansOdemeTurId = fields.Int()
    faturaKesimTurId = fields.Int()
    aciklama = fields.String()
    tutar = fields.Float()
    masraf = fields.Float()
    faturaNo = fields.String()
    kullaniciId = fields.Int()


class OdemelerModel:
    
    id = None
    tarih = None
    musteriId = None
    siparisNo = ""
    siparisId = None
    finansOdemeTurId = None
    faturaKesimTurId = None
    aciklama = ""
    tutar = 0
    masraf = 0
    faturaNo = ""
    kullaniciId = None

    