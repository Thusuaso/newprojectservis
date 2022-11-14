from marshmallow import Schema,fields
from models.new_sevkiyat.kasa_listesi import KasaListesiModel,KasaListesiSchema


class SevkiyatSchema(Schema):

    id = fields.Int()
    siparisno = fields.String()
    musteriid = fields.Int()
    cikistarihi = fields.String()
    faturano = fields.String()
    takip = fields.Boolean()
    etahatirlatmasure = fields.Int()
    kullaniciid = fields.Int()
    kasalistesi = fields.Nested(KasaListesiSchema(many=True))
    
class SevkiyatModel:
    id = None 
    siparisno = ""
    musteriid = None
    cikistarihi = ""
    faturano = ""
    takip = False
    etahatirlatmasure = 5
    kullaniciid = None
    kasalistesi = KasaListesiModel()

