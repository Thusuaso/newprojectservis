from marshmallow import Schema,fields,validate


class OrderSchema(Schema):
    id = fields.Int()
    birim = fields.String()
    miktar = fields.Float()
    ozelMiktar = fields.Int()
    ton = fields.Int()
    en = fields.String()
    boy = fields.String()
    kenar = fields.String()
    kategori = fields.String()
    urunAdi = fields.String()
    yuzey = fields.String()
    boyut = fields.String()
    uretimAdet = fields.Int()
    uretimMiktari = fields.Float()
    kalanMiktar = fields.Float()
    kalanAdet = fields.Float()    
    kalanBilgisi = fields.String()
    kalanRenk = fields.String()
    fontColor = fields.String()
    birimBackground = fields.String()
class OrderModel:
    
    id = 0
    birim = ""
    miktar = 0
    ozelMiktar = 0
    ton = 0
    en = ""
    boy = ""
    kenar= ""
    kategori = ""
    urunAdi = ""
    yuzey = ""
    boyut = ""
    uretimAdet = 0
    uretimMiktari = 0
    kalanMiktar = 0
    kalanAdet = 0
    kalanBilgisi = ""
    kalanRenk = ""
    fontColor = ""
    birimBackground = ""
    
    
    
class MusteriBazindaUretimModel:
    musteriAdi = ""
    marketing = ""
    ulkeAdi = ""
    satisToplamiBuYil =  0
    satisToplamiGecenYil =  0
    satisToplamiOncekiYil =  0
    satisToplamiOnDokuzYil=0
    toplam = 0
    toplamCfr = 0


class MusteriBazindaUretimSchema(Schema):
    musteriAdi = fields.String()
    marketing = fields.String()
    ulkeAdi = fields.String()
    satisToplamiBuYil =  fields.Float()
    satisToplamiGecenYil =  fields.Float()
    satisToplamiOncekiYil =  fields.Float()
    satisToplamiOnDokuzYil = fields.Float()
    toplam = fields.Float()
    toplamCfr = fields.Float()
    

    