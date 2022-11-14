from marshmallow import Schema,fields


class YapilacakIslerSchema(Schema):
    id = fields.Int()
    siparisId = fields.Int()
    tarih = fields.Date()
    konu = fields.String()
    yapilacakIs = fields.String()
    kullaniciId = fields.Int()
    takipKullaniciId = fields.Int()
    renk = fields.Int()
    yapildi = fields.Boolean()


class YapilacakIslerModel:

    id = None
    siparisId = None
    tarih = None
    konu = ""
    yapilacakIs = ""
    kullaniciId = None
    takipKullaniciId = None
    renk = ""
    yapildi = False

    