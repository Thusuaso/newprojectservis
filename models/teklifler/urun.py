from marshmallow import Schema,fields
from models.teklifler.ebat import EbatSchema

class UrunSchema(Schema):
    id = fields.String()
    urunAdi = fields.String()
    sira = fields.Int()
    ebatlar = fields.Nested(EbatSchema,many=True)
    yuzeyIslem = fields.String()

class UrunModel:

    id = None
    urunAdi = ""
    sira = None
    ebatlar = list()
    yuzeyIslem = ""

   
