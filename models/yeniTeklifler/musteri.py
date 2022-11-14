from marshmallow import Schema,fields
from models.yeniTeklifler.ulke import UlkeModel,UlkeSchema


class MusteriSchema(Schema):
    id = fields.Int()
    musteriAdi = fields.String()
    ulkeId = fields.Int()
    ulke = fields.Nested(UlkeSchema())
    teklifSayisi = fields.Int()
class MusteriModel:
    id = None 
    musteriAdi = ""
    ulkeId = None 
    ulke = UlkeModel()
    teklifSayisi = 0