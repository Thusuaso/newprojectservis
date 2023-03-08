from helpers import SqlConnect
from models.operasyon.nakliyelistesi import *
from flask import jsonify,request
from flask_restful import Resource
import datetime
class TedarikciIslem:

    def __init__(self):

        self.data = SqlConnect().data

   

    def tedarikciKaydet(self,item):
     
        try:
            kullaniciid = self.data.getStoreList(
                    """
                    Select ID from KullaniciTB
                    where KullaniciAdi=?
                    """,(item['kullaniciAdi'])
                )[0].ID
            self.data.update_insert(
                """
                INSERT INTO Tedarikci_Siparis_FaturaTB (FaturaNo, FaturaDurum, TedarikciID, SiparisNo,KullaniciID)    values
                (?,?,?,?,?)
                """,(item['FaturaNo'],0,item['tedarikci_id'],item['siparisno'],kullaniciid)
            )
           
            self.__evrakId(item)
            return True
        except Exception as e:
            print('tedarikciKaydet  Hata : ',str(e))
        return False


    def __evrakId(self,item):

        try:
            id = 101
         

            kontrol = self.data.getStoreList("Select count(*) as durum from YeniTedarikciFaturaTB where SiparisNo=?",item['siparisno'])[0].durum 
            
            if kontrol == 0:
                id = 101
            else : 
                id = kontrol +101   
            self.data.update_insert(
                """
                INSERT INTO YeniTedarikciFaturaTB (EvrakID, SiparisNo, EvrakAdi)    values
                (?,?,?)
                """,( id ,item['siparisno'],item['evrak'])
            )
            

            return True
        except Exception as e:
            print('__evrakId Hata : ',str(e))
            return False  


    def  TedarikciDosyaKaydet(self,item):
        try:
            bugun = datetime.date.today()
            kullaniciid = self.data.getStoreList(
                    """
                    Select ID from KullaniciTB
                    where KullaniciAdi=?
                    """,(item['kullaniciAdi'])
                )[0].ID
           
            evrak_id = self.__evrakIdKontrol(item)
            self.data.update_insert(
                """
                INSERT INTO SiparisFaturaKayitTB (
                    Tarih,
                    FaturaKayitID,
                    SiparisFaturaTurID, 
                    SiparisNo,
                    Tutar,
                   
                    YuklemeEvrakID,
                    YuklemeEvrakDurumID,
                    EvrakYuklemeTarihi,
                    EvrakAdi  ,
                    KullaniciID,
                    
                    YeniEvrakID
                   )   
                     values
                    (?,?,?,?,?,?,?,?,?,?,?)
                """,(bugun,0,0,item['siparisno'],0,30,2,bugun,item['evrak'],kullaniciid, evrak_id+101)
            )
          
            return True
        except Exception as e:
            print('TedarikciDosyaKaydet Hata : ',str(e))
            return False 

    def __evrakIdKontrol(self,item):

           kontrol = self.data.getStoreList("Select count(*) as durum from YeniTedarikciFaturaTB where SiparisNo=?   ",item['siparisno'])[0].durum 
           
           return kontrol
     
    def getTedarikciEvrakKontrol(self,tedarikci,siparis_no):
        try:
            tedarikci = tedarikci + '.pdf'
            result = self.data.getStoreList("""
                                                select 

                                                    count(SiparisNo) as TedarikciEvrakSayisi

                                                from YeniTedarikciFaturaTB
                                                where SiparisNo=? and EvrakAdi= ?
                                            """,(siparis_no,tedarikci))
            if result[0].TedarikciEvrakSayisi != 0:
                return True
            else:
                return False
        except Exception as e:
            print('getTedarikciEvrakKontrol hata',str(e))
            return False
    

class TedarikciEvrakKaydet(Resource): 
    
    def post(self):

        tedarikci = request.get_json()

        islem = TedarikciIslem()
        result = islem.tedarikciKaydet(tedarikci)
        
        return jsonify({'Status' : result})             

class TedarikciDosyaKaydet(Resource):

    def post(self):

        tedarikci = request.get_json()

        islem = TedarikciIslem()
        result = islem.TedarikciDosyaKaydet(tedarikci)

        return jsonify({'Status' : result})
    
class TedarikciEvrakKontrolApi(Resource):
    def get(self,tedarikci,siparis_no):
        islem = TedarikciIslem()
        result = islem.getTedarikciEvrakKontrol(tedarikci,siparis_no)
        return result
        
