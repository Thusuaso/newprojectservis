from marshmallow import Schema,fields

class UlkeyeGoreSchema(Schema):
    sip_sayisi = fields.Int()
    ulke_adi = fields.String()
    ulke_id = fields.Int()
    konteynir_sayisi = fields.Int()

class UlkeyeGoreModel:
    sip_sayisi = 0
    ulke_adi = ""
    ulke_id = 0
    konteynir_sayisi = 0
    
    
class UlkeyeGoreAyrintiSchema(Schema):
    musteri_adi = fields.String()
    siparis_no = fields.String()
    fob_toplami = fields.Float()
    navlun = fields.Float()
    detay_1 = fields.Float()
    detay_2 = fields.Float()
    detay_3 = fields.Float()
    detay_4 = fields.Float()
    sigorta = fields.Float()
    dtp_toplami = fields.Float()
    
class UlkeyeGoreAyrintiModel:
    musteri_adi = ""
    siparis_no = ""
    fob_toplami = 0
    navlun = 0
    detay_1 = 0
    detay_2 = 0
    detay_3 = 0
    detay_4 = 0
    sigorta = 0
    dtp_toplami = 0
    
class TedarikciyeGoreAyrintiSchema(Schema):
    firma_adi = fields.String()
    siparis_no = fields.String()
    alis_toplami = fields.Float()
    
class TedarikciyeGoreAyrintiModel:
    firma_adi = ""
    siparis_no = ""
    alis_toplami = 0







    
class MusteriyeGoreSchema(Schema):
    id = fields.Int()
    firma_adi = fields.String()
    yuk_mus_sayisi = fields.Int()
    ulke_adi = fields.String()
    konteynir_sayisi = fields.Int()
    
class MusteriyeGoreModel:
    id = 0
    firma_adi = ""
    yuk_mus_sayisi = 0
    ulke_adi = ""
    konteynir_sayisi = 0
    
class TedarikciyeGoreSchema(Schema):
    tedarikci_id = fields.Int()
    firma_adi = fields.String()
    total_alis = fields.Float()
    yuklenen_tedarikci_sayisi = fields.Int()
    
class TedarikciyeGoreModel:
    tedarikci_id = 0
    firma_adi = ""
    total_alis = 0
    yuklenen_tedarikci_sayisi = 0