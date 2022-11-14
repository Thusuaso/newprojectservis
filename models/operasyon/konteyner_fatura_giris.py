from marshmallow import Schema,fields
from models.operasyon.konteyner_fatura_liste import FaturaListeSchema,FaturaListeModel
from models.operasyon.konteyner_firma import FirmaListeSchema,FirmaListeModel
from models.operasyon.konteyner_siparis import SiparisListeSchema,SiparisListeModel


class FaturaListeHepsiSchema(Schema):
    faturaList = fields.Nested(FaturaListeSchema(many=True))
    firmaList = fields.Nested(FirmaListeSchema(many=True))
    siparisList = fields.Nested(SiparisListeSchema(many=True))
    
   
   

class FaturaListeHepsiModel:

    faturaList = list()
    firmaList = list()
    siparisList = list()
    
   
    
