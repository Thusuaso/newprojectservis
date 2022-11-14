from helpers import SqlConnect
from models.finans import FinansAnaSayfaModel,FinansAnaSayfaSchema
from openpyxl import *
import shutil

class YeniMusteriAnaIslem:

    def __init__(self):

        self.data = SqlConnect().data


    def getFinansMusteriler(self): #guncel yıl için 

        result = self.data.getList(
            """
              select 
			  m.FirmaAdi , 
			  m.ID ,
			  m.Ulke,
			  m.Marketing , 
			  (Select k.KullaniciAdi from KullaniciTB k  where k.ID = m.MusteriTemsilciId) as temsilci 
			  from MusterilerTB m
              where  m.Mt_No=2
               and m.ID not in (6,34)

            """
        )
       
        liste = list()
        for item in result:
            
         if self.__KapanmayanBedeller(item.ID) > 10   : 
            
            model = FinansAnaSayfaModel()
            
            model.bakiye = self.__KapanmayanBedeller(item.ID)
            model.id = item.ID 
            model.musteriadi = item.FirmaAdi
            model.ulke = item.Ulke
            model.marketing = item.Marketing
            model.temsilci = item.temsilci
            liste.append(model)

        
        schema = FinansAnaSayfaSchema(many=True)
    
        return schema.dump(liste)
       
        
       
    def __KapanmayanBedeller(self,musteriid):

        result = self.data.getStoreList(
            """
            select 
               s.SiparisNo,
               dbo.Get_Siparis_Bakiye_Tutar(s.SiparisNo) as kalan,
			   (select Sum(SatisToplam) from SiparisUrunTB su where su.SiparisNo=s.SiparisNo)+  
              dbo.Get_SiparisNavlun(s.SiparisNo) as Dtp
			
          
          from
               SiparislerTB s 
          where
               s.MusteriID=?
              and s.SiparisDurumID =3
		  	  and   dbo.Get_Siparis_Bakiye_Tutar(s.SiparisNo) > 10

            """,(musteriid)
        )
       
        toplam = 0
        for item in result : 
           toplam += item.Dtp
        return toplam    