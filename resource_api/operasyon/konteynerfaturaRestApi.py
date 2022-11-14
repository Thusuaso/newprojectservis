from flask_restful import Resource
from flask import jsonify,request
from resource_api.operasyon.konteyner_fatura_list import KonteynerHepsiListesi

class KonteynerListe(Resource):

    def get(self): 

        islem = KonteynerHepsiListesi()

        liste = islem.getHepsi()

        return liste