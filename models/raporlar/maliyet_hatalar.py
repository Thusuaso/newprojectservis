from marshmallow import Schema,fields

class MaliyetHatalarSchema(Schema):
    id = fields.Int()
    hata = fields.String()
    maliyet = fields.Float()
    kullanici_adi = fields.String()
    kullanici_id = fields.Int()
    tarih = fields.String()
class MaliyetHatalarModel:
    id = 0
    hata = ""
    maliyet = 0
    kullanici_adi = ""
    kullanici_id = 0
    tarih = ""
    