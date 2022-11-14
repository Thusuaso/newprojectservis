from marshmallow import Schema,fields

class KullaniciSchema(Schema):
    id = fields.Int()
    kullaniciAdi = fields.String()
    kullaniciSoyAd = fields.String()
    sifre = fields.String()
    mailAdres = fields.String()
    aktif = fields.Boolean()
    teklif = fields.Boolean()
    image = fields.String()
    token = fields.String()
    satisci = fields.Boolean()


class KullaniciModel:
    id = None
    kullaniciAdi = ""
    kullaniciSoyAd = ""
    sifre = ""
    mailAdres = ""
    aktif = True
    teklif = True
    image = ""
    token = ""
    satisci = False
    