from helpers import SqlConnect
from models.operasyon.nakliyelistesi import *
from flask import jsonify,request
from flask_restful import Resource
import datetime

class GumrukIslem:

    def __init__(self):

        self.data = SqlConnect().data

   

    def gumrukKaydet(self,item):
     
        try:
            forMat = '%d-%m-%Y'
            item['tarih'] = datetime.datetime.strptime(item['tarih'], forMat)
            item['tarih'] = item['tarih'].date()
            self.data.update_insert(
                """
                INSERT INTO KonteynerDigerFaturalarKayitTB (FirmaID, Tarih, FaturaNo,Kur,KayitTarihi)    values
                (?,?,?,?,?)
                """,(item['Firma_id'],item['tarih'],item['faturaNo'],item['kur'],item['tarih'])
            )
           
            self.__evrakId(item)
            return True
        except Exception as e:
            print('denizcilikKaydet  Hata : ',str(e))
        return False


    def __evrakId(self,item):

        try:
            id = 301
            kontrol = self.data.getStoreList("Select count(*) as durum from YeniGumIlacFaturaTB where SiparisNo=?",item['siparisno'])[0].durum 
            
            if kontrol == 0:
                id = 301
            else : 
                id = kontrol + 301   
            self.data.update_insert(
                """
                INSERT INTO YeniGumIlacFaturaTB (EvrakID, SiparisNo, EvrakAdi)    values
                (?,?,?)
                """,( id ,item['siparisno'],item['faturaNo'])
            )
            

            return True
        except Exception as e:
            print('__evrakId Hata : ',str(e))
            return False  

    def __urunId(self,item):
        
        kontrol = self.data.getStoreList("select count(*) as durum from KonteynerDigerFaturalarKayitTB where FaturaNo=?",item['faturaNo'])[0].durum
       
        urunId = None 
        if kontrol > 0:
            urunId = self.data.getStoreList("Select ID from KonteynerDigerFaturalarKayitTB where  FaturaNo=?",item['faturaNo'])[0].ID 
           
           
           
          
        else:
           
         print('urun id çalıştı')

        return urunId

    def  gumrukDosyaKaydet(self,item):
        try:
            bugun = datetime.date.today()
            kullaniciid = self.data.getStoreList(
                    """
                    Select ID from KullaniciTB
                    where KullaniciAdi=?
                    """,(item['kullaniciAdi'])
                )[0].ID
           
            print("gumrukDosyaKaydet",item)
            evrak_id = self.__evrakIdKontrol(item)
            urunID = self.__urunId(item)
            if (item['fatura_tur_list']['id'] == 7) : 
                yukleme_evrak = 70
            else :
                yukleme_evrak = 50
            forMat = '%d-%m-%Y'
            item['tarih'] = datetime.datetime.strptime(item['tarih'], forMat)
            item['tarih'] = item['tarih'].date()
            self.data.update_insert(
                """
                INSERT INTO SiparisFaturaKayitTB (
                    Tarih,
                    FaturaKayitID,
                    SiparisFaturaTurID, 
                    SiparisNo,
                    Tutar,
                    EvrakDurum,
                    YuklemeEvrakID,
                    YeniEvrakID,
                    YuklemeEvrakDurumID,
                    EvrakYuklemeTarihi,
                    EvrakAdi ,KullaniciID
                    )   
                     values
                    (?,?,?, ?,?,?,?,?,?,?,?,?)
                """,(item['tarih'],urunID,item['fatura_tur_list']['id'],item['siparisno'],item['Tutar_dolar'],1,yukleme_evrak,evrak_id+301,2,item['tarih'],item['faturaNo']+'.pdf' , kullaniciid)
            )
          
            return True
        except Exception as e:
            print('gumrukDosyaKaydet Hata : ',str(e))
            return False 

    def __evrakIdKontrol(self,item):

           kontrol = self.data.getStoreList("Select count(*) as durum from YeniGumIlacFaturaTB where SiparisNo=?   ",item['siparisno'])[0].durum 
           print("__evrakIdKontrol",kontrol)
           return kontrol
     

class GumrukEvrakKaydet(Resource): 
    
    def post(self):

        gumruk = request.get_json()

        islem = GumrukIslem()
        result = islem.gumrukKaydet(gumruk)
        
        return jsonify({'Status' : result})             

class GumrukDosyaKaydet(Resource):

    def post(self):

        gumruk = request.get_json()

        islem = GumrukIslem()
        result = islem.gumrukDosyaKaydet(gumruk)

        return jsonify({'Status' : result})
