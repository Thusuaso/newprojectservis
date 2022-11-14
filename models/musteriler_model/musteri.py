from marshmallow import Schema,fields



class MusteriSchema(Schema):

    id = fields.Int()
    musteri_adi = fields.String()
    unvan = fields.String()
    adres = fields.String()
    ulke_adi = fields.String()
    ulke_id = fields.Int()
    logo = fields.String()
    marketing = fields.String()
    aktif = fields.Boolean()
    sira = fields.Int()
    mt_no = fields.Int()
    musteri_temsilci_id = fields.Int()
    satisci = fields.Int()
    kullanici_id = fields.Int()
    mail_adresi = fields.String()
    telefon = fields.String()
    devir = fields.Boolean()
    ozel = fields.Boolean()
    selectOncelik = fields.String()
    satisci=fields.String()
    takip = fields.Boolean()
    notlar = fields.String()

class MusteriModel:
    id = None
    musteri_adi = ""
    unvan = ""
    adres = ""
    ulke_adi = ""
    ulke_id = None
    logo = ""
    marketing = ""
    aktif = True
    sira = 0
    mt_no = 2
    musteri_temsilci_id = None
    satisci = None
    kullanici_id = None
    mail_adresi = ""
    telefon = ""
    devir = False
    ozel = False
    selectOncelik = ""
    satisci=""
    takip=False
    notlar = ""

class MusteriSiparisSchema(Schema):

    id = fields.Int()
    Yil = fields.String()
    Total = fields.Float()
    

class MusteriSiparisModel:
    id = None
    Yil = ""
    Total = 0
   
class MusteriSiparisAyrintiSchema(Schema):

    SiparisNo = fields.String()
    Satisci = fields.String()
    Operasyon = fields.String()
    

class MusteriSiparisAyrintiModel:

    SiparisNo = ""
    Satisci = ""
    Operasyon = ""
