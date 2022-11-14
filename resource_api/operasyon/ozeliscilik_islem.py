from helpers import SqlConnect
from models.operasyon.nakliyelistesi import *
from flask import jsonify,request
from flask_restful import Resource
import datetime
class OzelIscilikIslem:

    def __init__(self):

        self.data = SqlConnect().data

   
    def __evrakId(self,item):

        try:
           
         
            harf = ["A", "B", "C", "Ç" ,"D" ,"E", "F", "G", "Ğ", "H", "İ", "I", "J" ,"K" ,"L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T" ,"U", "Ü", "V", "Y", "Z"]
            kontrol = self.data.getStoreList("Select count(*) as durum from YeniOzelIscilikTB where SiparisNo=?",item['siparisno'])[0].durum 
            
            if kontrol == 0:
                id = "3X"
            else : 
                 id = "3X-"+harf[kontrol] 
            self.data.update_insert(
                """
                INSERT INTO YeniOzelIscilikTB (EvrakID, SiparisNo, EvrakAdi)    values
                (?,?,?)
                """,( id ,item['siparisno'],item['evrak'])
            )
            

            return True
        except Exception as e:
            print('__evrakId Hata : ',str(e))
            return False  


    def  OzelIscilikDosyaKaydet(self,item):
        try:
            bugun = datetime.date.today()
            kullaniciid = self.data.getStoreList(
                    """
                    Select ID from KullaniciTB
                    where KullaniciAdi=?
                    """,(item['kullaniciAdi'])
                )[0].ID
           
           
            self.__evrakId(item)
            harf = ["A", "B", "C", "Ç" ,"D" ,"E", "F", "G", "Ğ", "H", "İ", "I", "J" ,"K" ,"L", "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T" ,"U", "Ü", "V", "Y", "Z"]
            evrak_id = self.__evrakIdKontrol(item)
            if evrak_id==1: evrak_id ="3X"
            else : 
             evrak_id ="3X" + harf[evrak_id]
            self.data.update_insert(
                """
                INSERT INTO SiparisFaturaKayitTB (
                    Tarih,
                    FaturaKayitID,
                    SiparisFaturaTurID, 
                    SiparisNo,
                    Tutar,
                   
                    YuklemeEvrakID,
                    YeniEvrakID,
                    YuklemeEvrakDurumID,
                    EvrakYuklemeTarihi,
                    EvrakAdi  ,
                    KullaniciID
                    
                   
                   )   
                     values
                    (?,?,?,?,?,?,?,?,?,?,?)
                """,(bugun,0,0,item['siparisno'],0,40,evrak_id,2,bugun,item['evrak'],kullaniciid)
            )
          
            return True
        except Exception as e:
            print('OzelIscilikDosyaKaydet Hata : ',str(e))
            return False 

    def __evrakIdKontrol(self,item):

           kontrol = self.data.getStoreList("Select count(*) as durum from YeniOzelIscilikTB where SiparisNo=?   ",item['siparisno'])[0].durum 
           
           return kontrol
     
            

class OzelIscilikDosyaKaydet(Resource):

    def post(self):

        ozel = request.get_json()

        islem = OzelIscilikIslem()
        result = islem.OzelIscilikDosyaKaydet(ozel)

        return jsonify({'Status' : result})
