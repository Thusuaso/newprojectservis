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