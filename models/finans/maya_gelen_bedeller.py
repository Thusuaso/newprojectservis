from marshmallow import Schema,fields


class MayaGelenBedellerSchema(Schema):
    id = fields.Int()
    tarih = fields.String()
    numuneTarihi = fields.String()
    numuneYuklemeTarihi = fields.String()
    po = fields.String()
    banka = fields.String()
    tutar = fields.Float()
    masraf = fields.Float()
    musteriAdi = fields.String()
    
    
    
class MayaGelenBedellerModel:
    id = 0
    tarih = ""
    numuneTarihi = ""
    numuneYuklemeTarihi = ""
    po = ""
    banka = ""
    tutar = 0
    masraf = 0
    musteriAdi = ""
    
    