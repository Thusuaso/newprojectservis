from marshmallow import Schema,fields


class TedarikciSchema(Schema):
    id = fields.Int()
    firmaAdi = fields.String()
    vergiNo = fields.String()
    telefon = fields.String()
    mailAdres = fields.String()
    il = fields.String()
    notlar = fields.String()
    kullaniciId = fields.Int()


class TedarikciModel:

    id = None
    firmaAdi = ""
    vergiNo = ""
    telefon = ""
    mailAdres = ""
    notlar = ""
    kullaniciId = None

   
