from resource_api.maliyet_raporlar.maliyet_rapor_islem import MaliyetRaporIslem,MaliyetRaporIslem_Yil
from resource_api.maliyet_raporlar.maliyet_zaman import MaliyeZamanIslem
from resource_api.maliyet_raporlar.excel_cikti import ExcelCiktiIslem
from resource_api.maliyet_raporlar.maliyet_ayrintim import MaliyetRaporuAyrinti
from flask_restful import Resource
from flask import request,send_file,jsonify


class MaliyetRaporIslemApi(Resource):

    def get(self,yil,ay):

        islem = MaliyetRaporIslem(yil,ay)

        maliyet_listesi = islem.getMaliyetListesi()

        return maliyet_listesi

class MaliyetRaporIslemYilApi(Resource):
    
    def get(self,yil):

        islem = MaliyetRaporIslem_Yil(yil)

        maliyet_listesi = islem.getMaliyetListesi()

        return maliyet_listesi

class MaliyetRaporYilListApi(Resource):

    def get(self):

        islem = MaliyeZamanIslem()

        yil_listesi = islem.getYilListesi()

        return yil_listesi

class MaliyetRaporIslemAyListesi(Resource):

    def get(self,yil): 

        islem = MaliyeZamanIslem()

        ay_listesi = islem.getAyListesi(yil)

        return ay_listesi

class MaliyetRaporuAyrintiApi(Resource):

    def get(self,siparisno): 
        islem = MaliyetRaporuAyrinti()

        maliyet = islem.getMaliyetAyrintiList(siparisno)

        banka = islem.getBankaAyrintiList(siparisno)

        data = {

            "maliyet" : maliyet,
            "banka" : banka
           
        }

        return jsonify(data)
               

class MaliyetRaporExcelApi(Resource):

    def post(self):

        data_list = request.get_json()

        islem = ExcelCiktiIslem()

        result = islem.maliyet_rapor_ciktisi(data_list)

        return jsonify({'status' : result})

    def get(self):

        excel_path = 'resource_api/maliyet_raporlar/dosyalar/ayo_maliyet_listesi.xlsx'

        return send_file(excel_path,as_attachment=True)

