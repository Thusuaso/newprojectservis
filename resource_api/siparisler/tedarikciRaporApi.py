from flask_restful import Resource
from flask import jsonify,request
from resource_api.siparisler.tedarikcicsiparis import TedarikciIcSiparisListe
from resource_api.siparisler.tedarikciurunlist import TedarikciSiparisUrunListe

class WoTedarikcilerApi(Resource): 

    def get(self):

        islem = TedarikciIcSiparisListe()
      
        siparisTeslimTur = islem.getTedarikciTeslimTurList()
        siparisFaturaTur = islem.getTedariciFaturaTurList()
   
        
        data = {

            "siparisTeslimTur" : siparisTeslimTur,
            "siparisFaturaTur" :siparisFaturaTur
            
          }

        return jsonify(data)

class TedarikciAyrintiListApi(Resource):

    def get(self,siparisno):
        
        islem = TedarikciSiparisUrunListe(siparisno)

        tedarikciUrunliste = islem.getTedarikciSiparisAyrintiList()
        tedarikciliste = islem.getTedarikciSiparisTedarikciAyrintiList()

     
     

        data = {

            "tedarikciUrunliste" : tedarikciUrunliste,
            "tedarikciliste" : tedarikciliste
            
        }


        return jsonify(data)      