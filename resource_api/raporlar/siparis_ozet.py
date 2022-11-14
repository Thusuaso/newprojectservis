from helpers import SqlConnect,TarihIslemler
from models.raporlar import SiparisOzetModel,SiparisOzetSchema,SevkiyatOzetSchema,SevkiyatOzetModel



class SiparisOzetListeler:

    def __init__(self):

        self.data = SqlConnect().data

    
    def getSiparisAyOzetList(self):

        result = self.data.getList(
           
          """
             select  
            MONTH(s.SiparisTarihi) as Ay,  
             Year(GetDate())-1 as yil  
             from  
  
            SiparislerTB s  
            where YEAR(s.SiparisTarihi) = Year(GetDate())-1 
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            group by MONTH(s.SiparisTarihi)  
            order by MONTH(s.SiparisTarihi) asc  
           """
        ) 

        liste = list()

        for item in result:
            model = SiparisOzetModel()
            model.id = item.Ay
            model.ay = item.Ay 
            model.yil = item.yil
            model.ay_adi = self.__getAy(model.ay)
            model.oncekiyil_toplam, model.oncekiyil_mal_bedeli = self.__getAyOzet_oncekiYilToplam(model.ay)
            model.gecenyil_toplam, model.gecenyil_mal_bedeli = self.__getAyOzet_gecenYilToplam(model.ay)
            model.buyil_toplam, model.buyil_mal_bedeli = self.__getAyOzet_buYilToplam(model.ay)
            model.fark = ((model.buyil_toplam  - model.gecenyil_toplam) / model.gecenyil_toplam) * 100
            
            
           
            #model.fark = round(model.fark - 100,2)
            
            liste.append(model)

        schema = SiparisOzetSchema(many=True)
       
        return schema.dump(liste)

   

    def __getAy(self,ay):

        if ay == 1 :
            return "Ocak"
        if ay == 2 :
            return "Şubat"
        if ay == 3 :
            return "Mart"
        if ay == 4 :
            return "Nisan"
        if ay == 5 :
            return "Mayıs"
        if ay == 6 :
            return "Haziran"
        if ay == 7 :
            return "Temmuz"
        if ay == 8 :
            return "Ağustos"
        if ay == 9 :
            return "Eylül"
        if ay == 10 :
            return "Ekim"
        if ay == 11 :
            return "Kasım"
        if ay == 12 :
            return "Aralık"
        
    def __getAyOzet_gecenYilToplam(self,ay):

        result = self.data.getStoreList( 
          
          """ 
             select  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.YuklemeTarihi,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
             
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.SiparisTarihi) = Year(GetDate())-1  
            and s.MusteriID in (Select m.ID from MusterilerTB m  
           where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            and Month(s.SiparisTarihi)=?
          group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3 ,s.MusteriID,s.TeslimTurID, s.YuklemeTarihi  
          """

            ,(ay)
        )

        navlun = 0
        diger_1 = 0
        diger_2 = 0
        diger_3 = 0
      
        mal_bedeli = 0
        a = 0

        for item in result:
          if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
              
          else:  

            if item.NavlunSatis != None:
                navlun += item.NavlunSatis 
            if item.DetayTutar_1 != None:
                diger_1 += item.DetayTutar_1
            if item.DetayTutar_2 != None:
                diger_2 += item.DetayTutar_2
            if item.DetayTutar_3 != None:
                diger_3 += item.DetayTutar_3 
              
            if item.SatisToplam != None:
                mal_bedeli += item.SatisToplam

            toplam = navlun + diger_1 + diger_2 + diger_3  + mal_bedeli

        return toplam , mal_bedeli

    def __getAyOzet_oncekiYilToplam(self,ay):

        result = self.data.getStoreList( 
          
          """ 
             select  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.YuklemeTarihi,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
             
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.SiparisTarihi) = Year(GetDate())-2  
            and s.MusteriID in (Select m.ID from MusterilerTB m  
           where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            and Month(s.SiparisTarihi)=?
          group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3 ,s.MusteriID,s.TeslimTurID, s.YuklemeTarihi  
          """

            ,(ay)
        )

        navlun = 0
        diger_1 = 0
        diger_2 = 0
        diger_3 = 0
      
        mal_bedeli = 0
        a = 0

        for item in result:
          if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
              
          else:  

            if item.NavlunSatis != None:
                navlun += item.NavlunSatis 
            if item.DetayTutar_1 != None:
                diger_1 += item.DetayTutar_1
            if item.DetayTutar_2 != None:
                diger_2 += item.DetayTutar_2
            if item.DetayTutar_3 != None:
                diger_3 += item.DetayTutar_3 
              
            if item.SatisToplam != None:
                mal_bedeli += item.SatisToplam

            toplam = navlun + diger_1 + diger_2 + diger_3  + mal_bedeli

        return toplam , mal_bedeli    

    def __getAyOzet_buYilToplam(self,ay):

        result = self.data.getStoreList( 
          
           """
             SELECT  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.YuklemeTarihi,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
             
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.SiparisTarihi) = Year(GetDate())  
            and s.MusteriID in (Select m.ID from MusterilerTB m  
     
            where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            and Month(s.SiparisTarihi)=?
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.TeslimTurID, s.YuklemeTarihi  
           """

            ,(ay)
        )

        navlun = 0
        diger_1 = 0
        diger_2 = 0
        diger_3 = 0
        toplam = 0
        mal_bedeli = 0
        a = 0

        for item in result:
          if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
              
          else:  

            if item.NavlunSatis != None:
                navlun += item.NavlunSatis 
            if item.DetayTutar_1 != None:
                diger_1 += item.DetayTutar_1
            if item.DetayTutar_2 != None:
                diger_2 += item.DetayTutar_2
            if item.DetayTutar_3 != None:
                diger_3 += item.DetayTutar_3 
            
            if item.SatisToplam != None:
                mal_bedeli += item.SatisToplam

            toplam = navlun + diger_1 + diger_2 + diger_3  + mal_bedeli

        return toplam , mal_bedeli

    def getSevkiyatAyOzetList(self):

        result = self.data.getList(
           
            """ 
            select  
            MONTH(s.SiparisTarihi) as Ay  
    
            from  
            SiparislerTB s  
            where YEAR(s.SiparisTarihi) = Year(GetDate())-1  
            and s.SiparisDurumID=3  
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            group by MONTH(s.SiparisTarihi)   
            order by MONTH(s.SiparisTarihi) asc  
            """
        ) 

        liste = list()

        for item in result:
            model = SevkiyatOzetModel()
            model.id = item.Ay
            
            model.ay = item.Ay 
            model.ay_adi = self.__getAy(model.ay)
            model.gecenyil_toplam, model.gecenyil_mal_bedeli = self.__getAyOzet_SevkiyatgecenYilToplam(model.ay)
            model.oncekiyil_toplam, model.oncekiyil_mal_bedeli = self.__getAyOzet_SevkiyatoncekiYilToplam(model.ay)
            model.buyil_toplam, model.buyil_mal_bedeli = self.__getAyOzet_SevkiyatbuYilToplam(model.ay)

            model.fark = ((model.buyil_toplam  - model.gecenyil_toplam) / model.gecenyil_toplam)* 100 
           
            #model.fark = round(model.fark - 100,2)
            liste.append(model)

        schema = SevkiyatOzetSchema(many=True)
        
        return schema.dump(liste) 

    def __getAyOzet_SevkiyatgecenYilToplam(self,ay):

        result = self.data.getStoreList(

          """
            SELECT  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
             
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim    
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.YuklemeTarihi) = Year(GetDate())-1  
             and s.SiparisDurumID=3  
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            and Month(s.YuklemeTarihi)=?
  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,  s.MusteriID,s.TeslimTurID  
           """,(ay)
        )

        navlun = 0
        diger_1 = 0
        diger_2 = 0
        diger_3 = 0
        diger_4 = 0
        mal_bedeli = 0

        for item in result:

            if item.NavlunSatis != None:
                navlun += item.NavlunSatis 
            if item.DetayTutar_1 != None:
                diger_1 += item.DetayTutar_1
            if item.DetayTutar_2 != None:
                diger_2 += item.DetayTutar_2
            if item.DetayTutar_3 != None:
                diger_3 += item.DetayTutar_3
                 
            if item.SatisToplam != None:
                mal_bedeli += item.SatisToplam

        toplam = navlun + diger_1 + diger_2 + diger_3  + mal_bedeli
       
        return toplam,mal_bedeli  

    def __getAyOzet_SevkiyatoncekiYilToplam(self,ay):

        result = self.data.getStoreList(

          """
            SELECT  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
             
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim    
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.YuklemeTarihi) = Year(GetDate())-2  
             and s.SiparisDurumID=3  
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            and Month(s.YuklemeTarihi)=?
  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,  s.MusteriID,s.TeslimTurID  
           """,(ay)
        )

        navlun = 0
        diger_1 = 0
        diger_2 = 0
        diger_3 = 0
        diger_4 = 0
        mal_bedeli = 0

        for item in result:

            if item.NavlunSatis != None:
                navlun += item.NavlunSatis 
            if item.DetayTutar_1 != None:
                diger_1 += item.DetayTutar_1
            if item.DetayTutar_2 != None:
                diger_2 += item.DetayTutar_2
            if item.DetayTutar_3 != None:
                diger_3 += item.DetayTutar_3
                 
            if item.SatisToplam != None:
                mal_bedeli += item.SatisToplam

        toplam = navlun + diger_1 + diger_2 + diger_3  + mal_bedeli
       
        return toplam,mal_bedeli            
        
    def __getAyOzet_SevkiyatbuYilToplam(self,ay):

        result = self.data.getStoreList(
             """
            SELECT  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
              
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.YuklemeTarihi) = Year(GetDate())  
            and s.SiparisDurumID=3  
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            and Month(s.YuklemeTarihi)=?
  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3 ,s.MusteriID,s.TeslimTurID   
             """,(ay)
           
        )
        navlun = 0
        toplam = 0
        diger_1 = 0
        diger_2 = 0
        diger_3 = 0
      
        mal_bedeli = 0

        for item in result:

            if item.NavlunSatis != None:
                navlun += item.NavlunSatis 
            if item.DetayTutar_1 != None:
                diger_1 += item.DetayTutar_1
            if item.DetayTutar_2 != None:
                diger_2 += item.DetayTutar_2
            if item.DetayTutar_3 != None:
                diger_3 += item.DetayTutar_3 
              
            if item.SatisToplam != None:
                mal_bedeli += item.SatisToplam

        toplam = navlun + diger_1 + diger_2 + diger_3  + mal_bedeli

        return toplam ,mal_bedeli
        
    def __set(self):
        pass