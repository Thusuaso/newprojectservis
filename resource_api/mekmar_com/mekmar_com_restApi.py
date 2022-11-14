from resource_api.mekmar_com.musteriler import SiteMusteri
from flask import jsonify,request
from flask_restful import Resource


class SiteMusteriList(Resource):

    def get(self):

        islem = SiteMusteri()

        liste = islem.getMusteriListesi()

        musteri_model = islem.getYeniMusteri()

        data = {

            "musteri_listesi" : liste,
            "musteri_model" : musteri_model
        }

        return jsonify(data) 

class SiteMusteriIslem(Resource):

    def post(self):

        data = request.get_json()

        islem = SiteMusteri()

        result = islem.musteriKaydet(data)

        return jsonify({'status' : result})
    
    def put(self):

        data = request.get_json()

        islem = SiteMusteri()

        result = islem.musteriGuncelle(data)

        return jsonify({'status' : result})

class SiteMusteriSil(Resource):

    def delete(self,id):

        islem = SiteMusteri()

        result = islem.musteriSil(id)

        return jsonify({'status' : result})   

class SiteMusteriDetay(Resource):

    def get(self,id):
        
        islem = SiteMusteri()

        musteri = islem.getMusteri(id)

        return musteri

class SiteYeniMusteri(Resource):

    def get(self):

        islem = SiteMusteri()

        musteri_model = islem.getYeniMusteri()

        return musteri_model
    
