from marshmallow import Schema,fields


class MarketingSchema(Schema):
    marketing = fields.String()
    fobToplam = fields.Float()
    cfrToplam = fields.Float()
class MarketingModel:
    marketing = ""
    fobToplam = 0
    cfrToplam = 0
class BdDepoSchema(Schema):
    ay = fields.String()
    cfrToplam = fields.Float()
    fobToplam = fields.Float()
    
    
class BdDepoModel:
    ay = ""
    cfrToplam = 0
    fobToplam = 0
    
class AylikYuklemeSchema(Schema):
    ay = fields.String()
    fobToplam = fields.Float()
    cfrToplam  = fields.Float()
    
class AylikYuklemeModel:
    ay = ""
    fobToplam = 0
    cfrToplam = 0
    
class MarketingAyrintiSchema(Schema):
    musteri = fields.String()
    marketing = fields.String()
    toplamFob = fields.Float()
    toplamCfr = fields.Float()
    
class MarketingAyrintiModel:
    musteri = ""
    marketing = ""
    toplamFob = 0
    toplamCfr = 0
    
    
class MarketingMonthLoadModel:
    month = ""
    monthNum = 0
    fob = 0
    ddp = 0
    
class MarketingMonthLoadSchema(Schema):
    
    month = fields.String()
    monthNum = fields.Int()
    fob = fields.Float()
    ddp = fields.Float()
    
    
class MarketingMonthLoadAyrintiModel:
    siparisNo = ""
    fob = 0
    navlun = 0
    detay1 = 0
    detay2 = 0
    detay3 = 0
    detay4 = 0
    ddp = 0
    
class MarketingMonthLoadAyrintiSchema(Schema):
    
    siparisNo = fields.String()
    fob = fields.Float()
    navlun = fields.Float()
    detay1 = fields.Float()
    detay2 = fields.Float()
    detay3 = fields.Float()
    detay4 = fields.Float()
    ddp = fields.Float()
    
class PoBazindaYillikSchema(Schema):
    po = fields.String()
    fob = fields.Float()
    ddp = fields.Float()
    teslim = fields.String()
    firma = fields.String()
    tarih = fields.String()
class PoBazindaYillikModel:
    po = ""
    fob = 0
    ddp = 0
    teslim = ""
    firma = ""
    tarih = ""