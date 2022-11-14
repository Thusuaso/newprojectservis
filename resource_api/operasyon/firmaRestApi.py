from flask_restful import Resource
from flask import jsonify,request
from resource_api.operasyon.firmalar import Listeler

class EvrakFirmaListe(Resource):

    def get(self): 

        islem = Listeler()

        liste = islem.getFirmaListe()

        return liste

class EvrakFirmaIslem(Resource):

    def post(self):

        data = request.get_json()

        islem = Listeler()

        result = islem.firmaKaydet(data)

        return jsonify({'status' : result}) 
        
class FirmaModelIslem(Resource):

    def get(self):

        islem = Listeler()

        firma_model = islem.getFirmaModel()

        return firma_model
              