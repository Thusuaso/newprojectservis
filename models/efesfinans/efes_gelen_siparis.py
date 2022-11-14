from marshmallow import Schema,fields

class EfesGelenSipSchema(Schema):
    id = fields.Float()
    siparisNo = fields.String()
    siparisSahibi = fields.String()
    operasyon = fields.String()
    siparisTarihi = fields.String()
    siparisYuklemeTarihi = fields.String()
    musteri = fields.String()
    siparisDurum = fields.String()
    
    
class EfesGelenSipModel:
    id = 0
    siparisNo = ""
    siparisSahibi = ""
    operasyon = ""
    siparisTarihi = ""
    siparisYuklemeTarihi = ""
    musteri = ""
    siparisDurum = ""
    
    
class EfesGelenSipAyrintiSchema(Schema):
    id = fields.Float()
    satisToplami = fields.Float()
    satisFiyati = fields.Float()
    miktar = fields.Float()
    urunBirim = fields.String()
    kategori = fields.String()
    yuzey = fields.String()
    urunAdi = fields.String()
    en = fields.String()
    boy = fields.String()
    kenar = fields.String()

    
    
class EfesGelenSipAyrintiModel:
    id = 0
    satisToplami = 0
    satisFiyati =0
    miktar = 0
    urunBirim = ""
    kategori = ""
    yuzey = ""
    urunAdi = ""
    en = ""
    boy = ""
    kenar = ""