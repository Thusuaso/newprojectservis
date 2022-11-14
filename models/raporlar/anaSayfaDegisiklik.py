from marshmallow import Schema,fields

class AnaSayfaDegisiklikSchema(Schema):
    degisiklikYapan = fields.String()
    yapilanDegisiklik = fields.String()
    degisiklikTarihi = fields.String()
    year = fields.String()
    month = fields.String()
    day = fields.String()

class AnaSayfaDegisiklikModel:
    degisiklikYapan = ""
    yapilanDegisiklik = ""
    degisiklikTarihi = ""
    year = ""
    month = ""
    day = ""
    
class UretimUrunlerSchema(Schema):
    kategori = fields.String()
    urunAdi = fields.String()
    yuzey = fields.String()
    en = fields.String()
    boy = fields.String()
    kenar = fields.String()
    sipMiktari = fields.Float()
    uretimMiktar = fields.Float()
    uretilmesiGereken = fields.Float()
    background = fields.String()
    urunKartId = fields.Int()
    siparisNo = fields.String()

    
class UretimUrunlerModel(Schema):
    kategori = ""
    urunAdi = ""
    yuzey = ""
    en = ""
    boy = ""
    kenar = ""
    sipMiktari = 0
    uretimMiktar = 0
    uretilmesiGereken = 0
    background = ""
    urunKartId = 0
    siparisNo = ""
