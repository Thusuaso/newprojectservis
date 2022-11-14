from marshmallow import Schema,fields


class EskiTekliflerSchema(Schema):
    id = fields.Int()
    tarih = fields.String()
    teklifno = fields.String()
    kullaniciadi = fields.String()
    ulkeadi = fields.String()
    musteriadi = fields.String()
    teklifdurum = fields.String()
    fiyatveren = fields.String()
    kategoriadi = fields.String()
    urunadi = fields.String()
    islemadi = fields.String()
    ebat = fields.String()
    fiyat = fields.Float()

class EskiTekliflerModel:
    id = None 
    tarih = ""
    teklifno = ""
    kullaniciadi = ""
    ulkeadi = ""
    musteriadi = ""
    teklifdurum = ""
    fiyatveren = ""
    kategoriadi = ""
    urunadi = ""
    islemadi = ""
    ebat = ""
    fiyat = 0
