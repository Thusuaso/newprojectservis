from views.siparisler import faturaKesimTur
from flask_restful import Resource

class FaturaKesimTurList(Resource):
    def get(self):

        faturaTur = faturaKesimTur()

        result = faturaTur.getFaturaKesimTurList()
      
        return result