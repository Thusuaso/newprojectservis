from flask_restful import Resource
from views.raporlar.temsilciSatislari import TemsilciSatislari,TemsilciSatislariDetay
from flask import jsonify
class TemsilciSatislariApi(Resource):
    def get(self,username):

        satislar = TemsilciSatislari(username)

        yuklenmemis = satislar.getTemsilciSiparisleriYuklenmemis()
        yuklenmemisGelenBedel = satislar.getTemsilciSiparisleriYuklenmemisGelenBedel()
        yuklenmis = satislar.getTemsilciSiparisleriYuklenmis()
        yuklenmisGelenBedel = satislar.getTemsilciSiparisleriYuklenmisGelenBedel()
        
        aylikYapilanSatis = satislar.getTemsilciAylikYapilanSatislar()
        aylikYapilanYukleme = satislar.getTemsilciAylikYapilanYuklemeler()
        aylikYapilanTumSatis = satislar.getTemsilciAylikTumSiparisler()
        
        
        data={
            'yuklenmemis':yuklenmemis,
            'yuklenmis':yuklenmis,
            'yuklenmemisGelenBedel':yuklenmemisGelenBedel,
            'yuklenmisGelenBedel':yuklenmisGelenBedel,
            'aylikYapilanSatis':aylikYapilanSatis,
            'aylikYapilanYukleme':aylikYapilanYukleme,
            'aylikYapilanTumSatis':aylikYapilanTumSatis
            }
        
        return jsonify(data)

class TemsilciSatislariApiDetayTamami(Resource):
    def get(self,ay,username):
        
        satislar = TemsilciSatislariDetay(username)
        result = satislar.getSatislarTamamiAylikDetay(ay)
        
        return jsonify(result)
    
class TemsilciSatislariApiDetaySatislar(Resource):
    
        def get(self,ay,username):
        
            satislar = TemsilciSatislariDetay(username)
            result = satislar.getSatislarAylikDetay(ay)
            
            return jsonify(result)
        
class TemsilciSatislariApiDetayYuklemeler(Resource):
    
        def get(self,ay,username):
        
            satislar = TemsilciSatislariDetay(username)
            result = satislar.getYuklemelerAylikDetay(ay)
            
            return jsonify(result)

