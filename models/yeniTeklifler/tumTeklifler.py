from marshmallow import Schema,fields


class TumTekliflerSchema(Schema):
    id = fields.Int()
    teklifno = fields.Int()
    teklifid = fields.Int()
    tarih = fields.String()
    kullaniciadi = fields.String()
    musteriadi = fields.String()
    ulkeadi = fields.String()
    kategoriadi = fields.String()
    urunadi = fields.String()
    kalinlik = fields.String()
    enboy = fields.String()
    islemadi = fields.String() 
    fobfiyat = fields.Float()
    tekliffiyat = fields.Float()
    birim = fields.String()
    year = fields.String()

class TumTekliflerModel:
    id = None 
    teklifno = 0
    teklifid = None 
    tarih = ""
    kullaniciadi = ""
    musteriadi = ""
    ulkeadi= ""
    kategoriadi = ""
    urunadi = ""
    kalinlik = ""
    enboy = ""
    islemadi = ""
    fobfiyat = ""
    tekliffiyat = 0 
    birim = ""
    year = ""
