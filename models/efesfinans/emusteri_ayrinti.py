from marshmallow import Schema,fields


class EfesMusteriAyrintiSchema(Schema):

    id = fields.Int()
    musteriadi = fields.String()
    musteri_id = fields.Int()
    siparisno = fields.String()
    yuklemetarihi = fields.String()
    tip = fields.String()
    toplam = fields.Float()
    kalan = fields.Float()
    vade = fields.String()

class EfesMusteriAyrintiModel:
    id = None
    musteriadi = ""
    musteri_id = None
    siparisno = ""
    yuklemetarihi = ""
    tip = ""
    toplam = 0
    kalan = 0
    vade = ""
    