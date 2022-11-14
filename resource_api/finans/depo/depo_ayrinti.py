from models.finans import DepoAyrintiSchema,DepoAyrintiModel
from helpers import SqlConnect,TarihIslemler
from openpyxl import *
import shutil


class DepoAyrinti:

    def __init__(self):

        self.data = SqlConnect().data

    def getAyrintiList(self,musteriid):

        tarihIslem = TarihIslemler()
        result = self.data.getStoreList(
            """
            select
            s.Id,
            s.OrderNo,
            s.Date,
            s.ShippingDate,
            s.PaymentDate,
            s.KalanBorc,
            s.Notes,
            (
            Select sum(u.Total) from YeniDepoSatisUrunlerTB u
            where u.OrderNo=s.OrderNo
            ) as Toplam,
            (
            Select sum(u.Total) from YeniDepoSatisUrunlerTB u
            where u.OrderNo=s.OrderNo and s.PaymentDate is not null
            and s.Shipped=1
            ) as Odenen
            from
            YeniDepoSatisTB s
            where
            s.CustomersId=?
            and s.Shipped=1
             and s.PaymentDate  is not  null  
            order by s.Date desc
            """,(musteriid)
        )

        liste = list()
        for key in self.__konteynerKapananList(musteriid) :
              liste.append(key)
        for item in result:
         
            model = DepoAyrintiModel()
           
            model.id = item.Id
            model.orderno = "PO#"+ item.OrderNo
            model.notlar = item.Notes
            model.status = "DEPO"

            if item.Date != None:
                model.tarih = tarihIslem.getDate(item.Date).strftime("%d-%m-%Y")
            
            if item.ShippingDate != None:
                model.sevktarihi = tarihIslem.getDate(item.ShippingDate).strftime("%d-%m-%Y")

            if item.PaymentDate != None:
                model.odemetarihi = tarihIslem.getDate(item.PaymentDate).strftime("%d-%m-%Y")
            
            if item.Odenen != None:
                model.odenen = float(item.Odenen)

            if item.Toplam != None:
                model.toplam = float(item.Toplam)

            if item.KalanBorc != None:
                model.bakiye = item.KalanBorc
            else :     
                model.bakiye = model.toplam - model.odenen

            liste.append(model)
        
        schema = DepoAyrintiSchema(many=True)

        return schema.dump(liste)

    def getOdemeAyrintiList(self,musteriid):

        tarihIslem = TarihIslemler()
        result = self.data.getStoreList(
            """
             select
            s.Id,
            s.OrderNo,
            s.Date,
            s.ShippingDate,
            s.PaymentDate,
            s.KalanBorc,
            s.Notes,
            (
            Select sum(u.Total) from YeniDepoSatisUrunlerTB u
            where u.OrderNo=s.OrderNo 
            ) as Toplam,
            (
            Select sum(u.Total) from YeniDepoSatisUrunlerTB u
            where u.OrderNo=s.OrderNo and s.PaymentDate is not null
            and s.Shipped=1 
            ) as Odenen
            from
            YeniDepoSatisTB s
            where
           s.CustomersId=? and 
          s.PaymentDate  is  null  
          order by s.Date desc

            """,(musteriid)
        )

        liste = list()
        
        for item in result:
            model = DepoAyrintiModel()
            model.id = item.Id
            model.orderno =  "PO#" + item.OrderNo
            model.notlar = item.Notes

            if item.Date != None:
                model.tarih = tarihIslem.getDate(item.Date).strftime("%d-%m-%Y")
            
            if item.ShippingDate != None:
                model.sevktarihi = tarihIslem.getDate(item.ShippingDate).strftime("%d-%m-%Y")

            if item.PaymentDate != None:
                model.odemetarihi = tarihIslem.getDate(item.PaymentDate).strftime("%d-%m-%Y")
            model.status = "DEPO"
            if item.Odenen != None:
                model.odenen = float(item.Odenen)

            if item.Toplam != None:
                model.toplam = float(item.Toplam)

            if item.KalanBorc != None:
                model.bakiye = float(item.KalanBorc)
            else :
             model.bakiye = model.toplam

            liste.append(model)

        for key in self.__konteynerList(musteriid):
              liste.append(key)
        schema = DepoAyrintiSchema(many=True)

        return schema.dump(liste)     

   

    def __konteynerList(self , musteriid):   #kalan
      
     if musteriid == 1 : 
         musteriid = 3446

     elif musteriid == 3 : 
          musteriid = 2400
     elif musteriid == 4 : 
          musteriid = 1373     

     result = self.data.getStoreList(
            """
              select 
               s.SiparisNo,
			   s.SiparisTarihi,
			   s.YuklemeTarihi,
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
     tarihIslem = TarihIslemler()      
     liste = list()
     for item in result : 
          model = DepoAyrintiModel()
          model.orderno = "PO#" +item.SiparisNo
          model.id = musteriid
          model.status = "KONTEYNER"

          if item.SiparisTarihi != None:
                model.tarih = tarihIslem.getDate(item.SiparisTarihi).strftime("%d-%m-%Y")
            
          if item.YuklemeTarihi != None:
                model.sevktarihi = tarihIslem.getDate(item.YuklemeTarihi).strftime("%d-%m-%Y")

          if item.Dtp != None and item.kalan !=None :
                 model.odenen = float(item.Dtp) - float(item.kalan)
                 model.toplam = float(item.Dtp)
                 model.bakiye = item.kalan
          
          liste.append(model)
      

     return liste

    def __konteynerKapananList(self , musteriid):   #kapanan
      
     if musteriid == 1 : 
         musteriid = 3446

     elif musteriid == 3 : 
          musteriid = 2400
     elif musteriid == 4 : 
          musteriid = 1373     

     result = self.data.getStoreList(
            """
               select 
               s.SiparisNo,
			   s.SiparisTarihi,
			   s.YuklemeTarihi,
			   (select top 1 o.Tarih from OdemelerTB o where o.SiparisNo = s.SiparisNo  order by  o.Tarih desc) odenmeTarihi,
               dbo.Get_Siparis_Bakiye_Tutar(s.SiparisNo) as kalan,
			   (select Sum(SatisToplam) from SiparisUrunTB su where su.SiparisNo=s.SiparisNo)+  
               dbo.Get_SiparisNavlun(s.SiparisNo) as Dtp
			   from
                SiparislerTB s 
                where
                s.MusteriID=?
                and s.SiparisDurumID =3
		  	    and   dbo.Get_Siparis_Bakiye_Tutar(s.SiparisNo) < 10
                order by  s.YuklemeTarihi desc


            """,(musteriid)
        )
     tarihIslem = TarihIslemler()      
     liste = list()
     for item in result : 
          model = DepoAyrintiModel()
          model.orderno = "PO#" +item.SiparisNo
          model.id = musteriid
          model.status = "KONTEYNER"
        
          if item.SiparisTarihi != None:
                model.tarih = tarihIslem.getDate(item.SiparisTarihi).strftime("%d-%m-%Y")
            
          if item.YuklemeTarihi != None:
                model.sevktarihi = tarihIslem.getDate(item.YuklemeTarihi).strftime("%d-%m-%Y")
          
          if item.odenmeTarihi != None:
                model.odemetarihi = tarihIslem.getDate(item.odenmeTarihi).strftime("%d-%m-%Y")

          if item.Dtp != None and item.kalan !=None :
                 model.odenen = float(item.Dtp) - float(item.kalan)
                 model.toplam = float(item.Dtp)
                 model.bakiye = item.kalan
          
          liste.append(model)
      

     return liste 

