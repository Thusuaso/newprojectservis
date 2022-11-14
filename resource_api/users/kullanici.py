from resource_api.users.kullanici_guncelleme import Kullanicilar
from flask_restful import Resource
from flask import jsonify,request


class UserPassGuncelleApi(Resource):

    def post(self):
        
        item = request.get_json()
        islem = Kullanicilar()

        result = islem.setKullaniciPassGuncelleme(item)

        return jsonify({'status' : result})