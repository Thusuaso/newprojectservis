from marshmallow import Schema,fields
from models import *
from models.siparisler_model.siparisGirisUrun import SiparisGirisUrunSchema,SiparisGirisUrunModel


class SiparisGirisSchema(Schema):    
    siparis = fields.Nested(SiparislerSchema())
    siparisUrunler = fields.Nested(SiparisGirisUrunSchema(many=True))   
    proformaBilgileri = fields.Nested(SiparislerSchema())
    urunModel = fields.Nested(SiparisGirisUrunSchema)
    

class SiparisGirisModel:   
    siparis = SiparislerModel()
    siparisUrunler = list()  
    proformaBilgileri = SiparislerModel()
    urunModel = SiparisGirisUrunModel()
    
    
class ContainerAmountSchema(Schema):
    container_amount = fields.Int()
    
class ContainerAmountModel:
    container_amount = 0