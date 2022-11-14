from marshmallow import Schema,fields
from models.teklifler.urun import UrunSchema


class KategoriSchema(Schema):
    id = fields.Int()
    kategoriAdi = fields.String()
    urunler = fields.Nested(UrunSchema,many=True)


class KategoriModel:

    id = None
    kategoriAdi = ""
    #custom alan
    urunler = []

    