from flask import jsonify,request
from flask_restful import Resource
from views.raporlar.mekmarRaporlari import *
class MekmarUlkeRaporuApi(Resource):
    def get(self,year):
        islem = MekmarRaporlari()
        result = islem.getUlkeRaporlari(year)
        return jsonify(result)

class MekmarUlkeRaporuAyrintiApi(Resource):
    def get(self,ulke_id,year):
        islem = MekmarRaporlari()
        result = islem.getUlkeRaporlariAyrinti(ulke_id,year)
        return jsonify(result)
    
class MekmarMusteriRaporuApi(Resource):
    def get(self,year):
        islem = MekmarRaporlari()
        result = islem.getMusteriRaporlari(year)
        return result
    
class MekmarMusteriRaporuAyrintiApi(Resource):
    def get(self,musteri_id,year):
        islem = MekmarRaporlari()
        result = islem.getMusteriRaporlariAyrinti(musteri_id,year)
        return jsonify(result)    

    
class MekmarTedarikciRaporuApi(Resource):
    def get(self,year):
        islem = MekmarRaporlari()
        result = islem.getTedarikciRaporlari(year)
        return result
    
    
class MekmarTedarikciRaporuAyrintiApi(Resource):
    def get(self,tedarikci_id,year):
        islem = MekmarRaporlari()
        result = islem.getTedarikciAyrintiRaporlari(tedarikci_id,year)
        return jsonify(result)