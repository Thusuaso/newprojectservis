from marshmallow import Schema,fields

class MkRaporlarSevkSipSchema(Schema):
    po = fields.String()
    tarih = fields.String()
    siparisfob = fields.Float()
    siparisddp = fields.Float()
    yuklenenfob = fields.Float()
    yuklenenddp = fields.Float()
    teslimtur = fields.String()
    musteriadi = fields.String()
    siparistarihi = fields.String()
    yuklemetarihi = fields.String()
    total = fields.Float()
class MkRaporlarSevkSipModel:
    po = ""
    tarih = ""
    fob = 0
    ddp = 0
    siparisfob = 0
    siparisddp = 0 
    yuklenenfob = 0
    yuklenenddp = 0
    teslimtur = ""
    musteriadi = ""
    siparistarihi = ""
    yuklemetarihi = ""
    total = 0
    