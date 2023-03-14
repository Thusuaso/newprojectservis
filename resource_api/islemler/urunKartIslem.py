from flask_restful import Resource
from flask import request,jsonify
from views.islemler import UrunKart
from views.islemler import KasaUrunKart
class UrunKartIslem(Resource):

    def post(self):

        kart = request.get_json()

        urunKart = UrunKart()

        result = urunKart.kaydet(kart)

        return jsonify(result)

    def put(self):

        kart = request.get_json()

        urunKart = UrunKart()

        result = urunKart.guncelle(kart)

        return jsonify(result)
    
class UrunKartModel(Resource):
    def get(self,urunKartId):

        urunKart = UrunKart()
        result = urunKart.getUrunKart(urunKartId)

        return result
    
class UrunKartSilModel(Resource):
    
    def delete(self,urunKartId,username):
        
        urunKart = UrunKart()
        status = urunKart.getUrunKartSil(urunKartId,username)

        return jsonify({'status' : status})
    
    

class UrunKartBosModel(Resource):
    def get(self):

        urunKart = UrunKart()

        result = urunKart.getUrunKartModel()

        return result
    
class KasaUrunKartGuncellemeApi(Resource):
    def put(self,kasaNo,urunKartId,username):

        islem = KasaUrunKart()
        result = islem.guncelle(kasaNo,urunKartId,username)
        return result

class UrunKartDetayList(Resource):
    def get(self,urunKartId):

        urunKart = UrunKart()

        result = urunKart.getUrunKartDetayListe(urunKartId)

        return result

class UrunKartDetayListYeni(Resource):
    def get(self):

        urunKart = UrunKart()

        result = urunKart.getUrunKartDetayListeYeni()

        return result