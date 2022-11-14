from marshmallow import Schema,fields


class HatirlatmaSchema(Schema):
    id = fields.Int() 
    tarih = fields.String()
    sonTarih = fields.String()
    musteriAdi = fields.String()
    ulkeAdi = fields.String()

class HatirlatmaModel:
    id = None 
    tarih = ""
    sonTarih=""
    musteriAdi = ""
    ulkeAdi = ""
    
