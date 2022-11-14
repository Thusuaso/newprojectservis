from marshmallow import Schema,fields


class IscilikSchema(Schema):
    id = fields.Int()
    tarih = fields.String()
    siparisNo = fields.String()
    urunKartId = fields.Int()    
    tedarikciId = fields.Int()
    siparisEkstraGiderTurId = fields.Int()
    aciklama = fields.String()
    tutar = fields.Float()

    #custom alanlar
    tedarikciAdi = fields.String()

class IscilikModel:
    id = None 
    tarih = ""
    siparisNo = ""
    urunKartId = None     
    tedarikciId = None 
    siparisEkstraGiderTurId = None 
    aciklama = ""
    tutar = 0
    tedarikciAdi = ""