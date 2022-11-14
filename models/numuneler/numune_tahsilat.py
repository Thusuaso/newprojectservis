from marshmallow import Schema,fields


class NumuneTahsilatSchema(Schema):

    id = fields.Int()
    siparisno = fields.String()
    tarih = fields.String()
    musteriadi = fields.String()
    musteri_id = fields.Int()
    tutar = fields.Float()
    tutar_tl = fields.Float()
    tutar_euro = fields.Float()
    masraf = fields.Float()
    aciklama = fields.String()
    kullaniciadi = fields.String()
    banka = fields.String()

class NumuneTahsilatModel:
    id = None
    siparisno = ""
    tarih = ""
    musteriadi = ""
    musteri_id = None
    tutar = 0
    tutar_tl = 0
    tutar_euro = 0

    masraf = 0
    aciklama = ""
    kullaniciadi = ""
    banka = ""