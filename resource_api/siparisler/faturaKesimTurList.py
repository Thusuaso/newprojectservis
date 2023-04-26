from views.siparisler import FaturaKesimTur
from flask_restful import Resource

class FaturaKesimTurList(Resource):
    def get(self):

        faturaTur = FaturaKesimTur()

        result = faturaTur.getFaturaKesimTurList()
      
        return result