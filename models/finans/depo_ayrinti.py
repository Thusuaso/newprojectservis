from marshmallow import Schema,fields


class DepoAyrintiSchema(Schema):
    id = fields.Int()
    orderno = fields.String()
    tarih = fields.String()
    sevktarihi = fields.String()
    odemetarihi = fields.String()
    notlar = fields.String()
    toplam = fields.Float()
    odenen = fields.Float()
    bakiye = fields.Float()
    kalan  = fields.Float()
    status = fields.String()

class DepoAyrintiModel:
    id = None
    orderno = ""
    tarih = ""
    sevktarihi = ""
    odemetarihi = ""
    notlar = ""
    toplam = float(0)
    odenen = float(0)
    bakiye = float(0)
    kalan = 0
    status = ""