from marshmallow import fields,Schema


class KategoriSchema(Schema):
    id = fields.Int()
    kategoriAdi = fields.String()
    sira = fields.Int()

class KategoriModel:
    id = None 
    kategoriAdi = ""
    sira = 0