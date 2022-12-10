from marshmallow import Schema,fields

class MekmerDisFaturaSchema(Schema):
    
    id = fields.Int() 
    tarih = fields.Date()
    firmaAdi = fields.String()
    tutarDolar = fields.Float()
    tutarTl = fields.Float()
    kur = fields.Float()
    aciklama = fields.String()
    fileName = fields.String()
    fileLink = fields.String()
    
    
class MekmerDisFaturaModel:
    id = None 
    tarih = None
    firmaAdi = ""
    tutarDolar = 0
    tutarTl = 0
    kur = 0
    aciklama = ""
    fileName = ""
    fileLink = ""
