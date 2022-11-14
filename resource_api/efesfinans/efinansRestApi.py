from resource_api.efesfinans.ekonteyner_islem.ekonteyner import EfesKonteyner,EfesGelenOdemeler
from resource_api.efesfinans.ekonteyner_islem.emusteri_ayrinti import EfesMusteriAyrinti
from resource_api.efesfinans.ekonteyner_islem.etahsilat_islem import EfesTahsilatIslem
from resource_api.efesfinans.eodemeler.eodeme_islem import EfesOdemeIslem
from resource_api.efesfinans.epesinat.epesinat_islem_liste import EfesPesinatIslemListe
from resource_api.efesfinans.ekonteyner_islem.excel_cikti import ExcelCiktiIslem
from resource_api.efesfinans.ekonteyner_islem.efesGelenSiparisBilgileri import *
from flask_restful import Resource
from flask import jsonify,request,send_file
from resource_api.efesfinans.ekonteyner_islem import EfesGelenvYuklenen



class EfesKonteynerAnaListe(Resource): 

    def get(self,yil):

        konteyner = EfesKonteyner(yil)
       

        konteyner_list = konteyner.getKonteynerList()
        

        data = {

            "konteyner_list" : konteyner_list,
           
        }

        return jsonify(data)
class EfesKonteynerGelenOdemelerYil(Resource):
    def get(self):
        gelenOdemeler = EfesGelenOdemeler()
        gelenOdemelerList = gelenOdemeler.getGelenOdemelerList()
        data = {
            'gelenOdemelerList':gelenOdemelerList
        }
        return jsonify(data)

class EfesMusteriAyrintiListApi(Resource):

    def get(self,musteriid):

        islem = EfesMusteriAyrinti(musteriid)

        ayrinti_list = islem.getKonteynerAyrintiList()
        odeme_liste = islem.getOdemeListesi()#anasayfadaki tahsilat listesi

        data = {

            "ayrinti_list" : ayrinti_list,
            "odeme_liste" : odeme_liste
        }


        return jsonify(data)

class EfesMusteriOdemeSecimList(Resource):

    def get(self,musteri_id,tarih):

        islem = EfesMusteriAyrinti(musteri_id)

        secim_list = islem.getOdemeSecimPoList(tarih)

        return secim_list

class EfesTahsilatIslemList(Resource):

    def get(self,musteriid,siparisno):

        islem = EfesTahsilatIslem()

        musteri_list = islem.getEfesTahsilatList(musteriid,siparisno)
        musteri_data = islem.getEfesTahsilatModel(musteriid,siparisno)

        data = {

            "musteri_list" : musteri_list,
            "musteri_data" : musteri_data
        }

        return jsonify(data)

class EfesMusteriOdemeListesiApi(Resource):

    def get(self,yil,ay):

        islem = EfesOdemeIslem()

        odeme_listesi = islem.getOdemeListesi(yil,ay)

        return odeme_listesi    

class EfesMusteriOdemeYilListesiApi(Resource):

    def get(self):

        islem = EfesOdemeIslem()

        yil_listesi = islem.getYilListesi()

        return yil_listesi

class EfesMusteriOdemeAyListesi(Resource):

    def get(self,yil):

        islem = EfesOdemeIslem()

        ay_listesi = islem.getAyListesi(yil)

        return ay_listesi       

class EfesPesinatIslemListeApi(Resource):

    def get(self):

        pesinat_islem_listesi = EfesPesinatIslemListe().getPesinatIslemListe() #verileri yazdırdık 

        return pesinat_islem_listesi

    def post(self):

        data = request.get_json()

        result = EfesPesinatIslemListe().pesinat_kaydet(data)

        return jsonify({'status' : result})

class EfesKonteynerExcelCiktiApi(Resource):

    def post(self):

        data_list = request.get_json()

        islem = ExcelCiktiIslem()

        result = islem.konteynerCikti(data_list)

        return jsonify({'status' : result})

    def get(self):

        excel_path = 'resource_api/efesfinans/ekonteyner_islem/dosyalar/Konteyner.xlsx'

        return send_file(excel_path,as_attachment=True)      

class EfesTahsilatExcelCiktiApi(Resource):

    def post(self):

        data_list = request.get_json()

        islem = ExcelCiktiIslem()

        result = islem.tahsilatCikti(data_list)

        return jsonify({'status' : result})

    def get(self):

        excel_path = 'resource_api/efesfinans/ekonteyner_islem/dosyalar/Tahsilat.xlsx'

        return send_file(excel_path,as_attachment=True)     


class EfesGelenSiparisvYuklenenler(Resource):
    def get(self):
        islem = EfesGelenvYuklenen()
        result = islem.getEfesGelenvYuklenen()
        return jsonify(result)
    
class EfesGelenSiparisBilgileriApi(Resource):
    def get(self):
        islem = EfesGelenSiparisBilgileri()
        result = islem.getEfesGelenSiparisBilgileri()
        return jsonify(result)
    

class EfesGelenSiparisBilgileriAllApi(Resource):
    def get(self):
        islem = EfesGelenSiparisBilgileri()
        result = islem.getEfesGelenSiparisBilgileriAll()
        return jsonify(result)    

    
class EfesGelenSiparisBilgileriAyrintiApi(Resource):
    def get(self,siparisNo):
        islem = EfesGelenSiparisBilgileri()
        result = islem.getEfesGelenSiparisBilgileriAyrinti(siparisNo)
        return jsonify(result)
        



















