from resource_api.finans.konteyner_islem.odemelerList import Odemeler
from flask_restful import Resource

class OdemelerListesiApi(Resource):
    def get(self):

        odemeler = Odemeler()

        odemeler_list = odemeler.getOdemelerList()

        return odemeler_list
    
class OdemelerListesiAyrintiApi(Resource):
    def get(self,musteriId):
        
        odemeler = Odemeler()
        
        odemeler_ayrinti_list = odemeler.getOdemelerListAyrinti(musteriId)
        
        return odemeler_ayrinti_list
        
