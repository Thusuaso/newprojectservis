from marshmallow import Schema,fields
from models.teklifler.ulke import UlkeSchema

class MusteriSchema(Schema):
    id = fields.Int()
    musteriAdi = fields.String()
    ulke = fields.Nested(UlkeSchema)



class MusteriModel:
    id = None
    musteriAdi = ""
    ulke = {}

   