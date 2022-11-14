from marshmallow import Schema,fields


class EfesTahsilatSchema(Schema):

    id = fields.Int()
    siparisno = fields.String()
    tarih = fields.String()
    musteriadi = fields.String()
    musteri_id = fields.Int()
    tutar = fields.Float()
    masraf = fields.Float()
    aciklama = fields.String()
    kullaniciadi = fields.String()

class EfesTahsilatModel:
    id = None
    siparisno = ""
    tarih = ""
    musteriadi = ""
    musteri_id = None
    tutar = 0
    masraf = 0
    aciklama = ""
    kullaniciadi = ""