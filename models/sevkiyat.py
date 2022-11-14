from marshmallow import Schema,fields


class SevkiyatSchema(Schema):
    id = fields.Int()
    tarih = fields.Date()
    cikisTur = fields.String()
    kasaNo = fields.Int()
    uretimId = fields.Int()
    musteriId = fields.Int()
    birimFiyat = fields.Float()
    toplam = fields.Float()
    cikisNo = fields.String()
    raporDurum = fields.Boolean()
    kullaniciId = fields.Int()


class SevkiyatModel:
    id = None
    tarih = None
    cikisTur = ""
    kasaNo = None
    uretimId = None
    musteriId = None
    birimFiyat = 0
    toplam = 0
    cikisNo = ""
    raporDurum = True
    kullaniciId = None
    
        

        