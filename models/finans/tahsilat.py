from marshmallow import Schema,fields


class TahsilatSchema(Schema):

    id = fields.Int()
    siparisno = fields.String()
    tarih = fields.String()
    musteriadi = fields.String()
    musteri_id = fields.Int()
    tutar = fields.Float()
    masraf = fields.Float()
    aciklama = fields.String()
    kur = fields.Float()
    kullaniciadi = fields.String()

class TahsilatModel:
    id = None
    siparisno = ""
    tarih = ""
    musteriadi = ""
    musteri_id = None
    tutar = 0
    masraf = 0
    aciklama = ""
    kur = 0
    kullaniciadi = ""