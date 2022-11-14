from resource_api.musteriler.musteri_liste import MusteriIslem,MusteriSiparisIslem,MusteriSiparisAyrintiCardIslem
from resource_api.musteriler.musteri_detay import MusteriDetayIslem
from flask_restful import Resource
from flask import jsonify,request,send_file


class MusteriListeApi(Resource):

    def get(self):

        islem = MusteriIslem()

        musteri_listesi = islem.getMusteriListesi()


        return musteri_listesi

class MusteriSiparisListesiApi(Resource):
    def get(self):

        islem = MusteriSiparisIslem()
        musteri_siparis_listesi = islem.getMusteriSiparisListesi()
        return musteri_siparis_listesi

class MusteriSiparisAyrintiCardApi(Resource):
    def get(self):

        islem = MusteriSiparisAyrintiCardIslem()
        musteri_ayrinti_card_list = islem.getMusteriSiparisAyrintiCard()
        return musteri_ayrinti_card_list

class MusteriDetayApi(Resource):

    def get(self,id):
        islem = MusteriDetayIslem()

        musteri_detay = islem.getMusteriDetay(id)
        siparis_ozet  = islem.getSiparisBedeliDetay(id)
        temsilci_list = islem.getTemsilciList()
        ulke_list  = islem.getUlkeList()

        data = {

            "musteri_detay" : musteri_detay,
            "siparis_ozet" : siparis_ozet ,
            "temsilci_list" : temsilci_list,
            "ulke_list" : ulke_list
        }


        return jsonify(data)

class MusteriSiparisAyrintApi(Resource):

    def get(self,yil,id):

        islem = MusteriDetayIslem()

        siparis_detay = islem.getSiparisAyrintiDetay(yil,id)
      

        data = {

            "siparis_detay" : siparis_detay,
           
        }


        return jsonify(data)       

class MusteriYeniModelApi(Resource):

    def get(self):

        islem = MusteriDetayIslem()

        musteri_model = islem.getYeniMusteriModel()

        temsilci_list = islem.getTemsilciList()
        ulke_list  = islem.getUlkeList()

        data = {

            "musteri_model" : musteri_model,
            "temsilci_list" : temsilci_list,
            "ulke_list" : ulke_list
        }


        return jsonify(data)

class MusteriKayitIslemApi(Resource):

    def post(self):

        data = request.get_json()

        islem = MusteriDetayIslem()

        result = islem.musteriKaydet(data)

        return jsonify({'status' : result})

    def put(self):

        data = request.get_json()

        islem = MusteriDetayIslem()

        result = islem.musteriGuncelle(data)

        return jsonify({'status' : result})

class MusteriKayitSilmeApi(Resource):

    def delete(self,id):

        islem = MusteriDetayIslem()

        result = islem.musteriSilme(id)

        return jsonify({'status' : result})

class MusteriListesiYazdirmaApi(Resource):
    def post(self):
        data_list = request.get_json()
        

        islem = MusteriIslem()
        result = islem.excelCiktiAl(data_list)
        return jsonify({'status' : result})


    def get(self):

        excel_path = 'resource_api/musteriler/dosyalar/musteriDetayListesi.xlsx'

        return send_file(excel_path,as_attachment=True)


class CustomerChangeFollowApi(Resource):
    def get(self,customer,follow):
        islem = MusteriIslem()
        result = islem.setCustomerFollowing(customer,follow)
        
        return jsonify(result)