from marshmallow import Schema,fields


class MusterilerSchema(Schema):
    id = fields.Int()
    firmaAdi = fields.String()
    unvan = fields.String()
    adres = fields.String()
    ulke = fields.String()
    ulkeId = fields.String()
    etiket = fields.String()
    aktif = fields.Boolean()
    sira = fields.Int()
    mt_No = fields.Int()
    musteriTemsilciId = fields.Int()
    kullaniciId = fields.Int()
    mailAdresi = fields.String()
    telefon = fields.String()
    devir = fields.Boolean()
    ozel = fields.Boolean()

class MusterilerModel:
        id = None
        firmaAdi = ""
        unvan = ""
        adres = ""
        ulke = ""
        ulkeId = None
        etiket = ""
        aktif = True
        sira = 0
        mt_No = 0
        musteriTemsilciId = None
        kullaniciId = None
        mailAdresi = ""
        telefon = ""
        devir = False
        ozel = False


class UlkeyeGoreMusteriSchema(Schema):
    siparisSayisi = fields.Int()
    ulkeId = fields.Int()
    ulkeAdi = fields.String()

class UlkeyeGoreMusteriModel:
    siparisSayisi = 0
    ulkeId = 0
    ulkeAdi = ""
    
class UlkeyeGoreMusteriAyrintiSchema(Schema):
    siparisTarihi = fields.String()
    siparisNo = fields.String()
    firmaAdi = fields.String()
    yuklemeTarihi = fields.String()

class UlkeyeGoreMusteriAyrintiModel:
    siparisTarihi = ""
    siparisNo = ""
    firmaAdi = ""
    yuklemeTarihi = ""

        