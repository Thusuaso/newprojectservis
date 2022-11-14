from marshmallow import Schema,fields

class KategoriSchema(Schema):
    id = fields.Int()
    kategoriAdi = fields.String()
    kullaniciId = fields.Int()


class KategoriModel:
    id = None
    kategoriAdi = ""
    kullaniciId = None
    
    