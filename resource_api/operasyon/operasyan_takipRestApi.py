from resource_api.operasyon.sevk_takip_listesi import SevkTakip
from flask_restful import Resource
from flask import jsonify,request


class SevkTakipListesi(Resource):

    def get(self):

        islem = SevkTakip()

        sevk_takip_listesi = islem.getSevkListesi()

        return sevk_takip_listesi

class SevkTakipDusenlerListesi(Resource):

    def get(self):

        islem = SevkTakip()

        sevk_dusen_listesi = islem.getTakiptenDusenler()

        return sevk_dusen_listesi

class SevkTakipDetay(Resource):

    def get(self,id):

        islem = SevkTakip()

        sevk_takip = islem.getSevkDetay(id)

        return sevk_takip

class SevkTakipIslem(Resource):

    def put(self):

        item = request.get_json()

        islem = SevkTakip()

        result = islem.sevkDetayGuncelle(item)

        return jsonify({'status' : result})