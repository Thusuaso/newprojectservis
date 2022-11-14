from helpers import SqlConnect
from models.operasyon.nakliyelistesi import *
from flask import jsonify,request
from flask_restful import Resource
import datetime

class DenizcilikIslem:

    def __init__(self):

        self.data = SqlConnect().data

   

    def denizcilikKaydet(self,item):
        
     
        try:
           
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
            if(item['birlesik']) : 
               id = 401
            else : id = 402

            kontrol = self.data.getStoreList("Select count(*) as durum from YeniDenizcilikFaturaTB where SiparisNo=?",item['siparisno'])[0].durum 
            
            if kontrol == 0:
                if(item['birlesik']) : 
                  id = 401
                else : id = 402  
                
            else : 
                 if(item['birlesik']) : 
                   id = 401
                 else : id = 402 + kontrol
               
            self.data.update_insert(
                """
                INSERT INTO YeniDenizcilikFaturaTB (EvrakID, SiparisNo, EvrakAdi)    values
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
           
            print("Denizcili Urun ")

        return urunId

    def  denizcilikDosyaKaydet(self,item):
        try:
            bugun = datetime.date.today()
            kullaniciid = self.data.getStoreList(
                    """
                    Select ID from KullaniciTB
                    where KullaniciAdi=?
                    """,(item['kullaniciAdi'])
                )[0].ID
           
            print("DenizcilikDosyaKaydet",item)
            self.__evrakId(item)
            evrak_id = self.__evrakIdKontrol(item)
            
            urunID = self.__urunId(item)
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
                    EvrakAdi ,
                    KullaniciID
                    )   
                     values
                    (?,?,?, ?,?,?,?,?,?,?,?,?)
                """,(item['tarih'],urunID,9,item['siparisno'],item['Tutar_dolar'],1,50,evrak_id , 2,item['tarih'],item['faturaNo']+'.pdf' , kullaniciid)
            )
          
            return True
        except Exception as e:
            print('DenizcilikDosyaKaydet Hata : ',str(e))
            return False 

    def __evrakIdKontrol(self,item):

           kontrol = self.data.getStoreList("Select EvrakID as durum from YeniDenizcilikFaturaTB where SiparisNo=?  and EvrakAdi=?  ",(item['siparisno'],item['faturaNo']))[0].durum 
           print("__evrakIdKontrol",kontrol)
           return kontrol
     

class DenizcilikEvrakKaydet(Resource): 
    
    def post(self):

        tedarikci = request.get_json()

        islem = DenizcilikIslem()
        result = islem.denizcilikKaydet(tedarikci)
        
        return jsonify({'Status' : result})             

class DenizcilikDosyaKaydet(Resource):

    def post(self):

        tedarikci = request.get_json()

        islem = DenizcilikIslem()
        result = islem.denizcilikDosyaKaydet(tedarikci)

        return jsonify({'Status' : result})
