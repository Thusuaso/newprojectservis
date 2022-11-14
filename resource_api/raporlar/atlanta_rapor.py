from helpers import SqlConnect,TarihIslemler
from models.raporlar.atlanta_rapor import *



class AtlantaYuklemeListeler:

    def __init__(self):

        self.data = SqlConnect().data

    
    def getYuklemeRaporAylik(self,yil,ay):

        result = self.data.getStoreList(
            """
              select  
            s.YuklemeTarihi,  
            s.SiparisNo,  
            m.FirmaAdi as MusteriAdi,  
            (select Sum(SatisToplam) from SiparisUrunTB su where su.SiparisNo=s.SiparisNo) as Fob,  
            (select Sum(SatisToplam) from SiparisUrunTB su where su.SiparisNo=s.SiparisNo)+  
            dbo.Get_SiparisNavlun(s.SiparisNo) as Dtp,  
            'Konteyner' as Tur,m.Marketing,
			s.MusteriID
			
            from  
            SiparislerTB s,MusterilerTB m  
            where Year(YuklemeTarihi)=?
        
            and m.ID=s.MusteriID  
            and (s.depo_yukleme=1 or m.ID=3444)
		
            and Month(YuklemeTarihi)=?
            and m.Marketing is not null  
           
            union  
            select  
            s.Tarih as YuklemeTarihi,  
            s.CikisNo as SiparisNo,  
            m.FirmaAdi as MusteriAdi,  
            Sum(Toplam) as Fob  
            ,Sum((s.BirimFiyat+7.5)*u.Miktar) as Dtp,  
            'Depo' as Tur,m.Marketing,
			s.MusteriID
            from  
            SevkiyatTB s,MusterilerTB m,UretimTB u  
            where s.MusteriID=m.ID and u.KasaNo=s.KasaNo  
            and Year(s.Tarih)=?
            and m.Mt_No=1  
			and Month(s.Tarih)=?
            group by  
            s.Tarih,s.CikisNo,m.FirmaAdi,m.Marketing,s.MusteriID


            
            
            """,(yil,ay,yil,ay)
        ) 

        liste = list()

        for item in result:
            model = YuklemeAylikModel()
            model.yukleme_tarihi = item.YuklemeTarihi
            model.siparis_no = item.SiparisNo
            model.musteri_adii = item.MusteriAdi
            model.fob = item.Fob
            model.dtp = item.Dtp
            model.tur = item.Tur
            model.marketing = item.Marketing
            model.musteriID = item.MusteriID
            liste.append(model)

        schema = YuklemeAylikSchema(many=True)

        return schema.dump(liste)

    def getYuklemeRaporAylikMusteriBazinda(self,yil,ay):

        result = self.data.getStoreList(
            """
             select  
                 m.ID as MusteriId,  
                 m.FirmaAdi as MusteriAdi,  
                  m.Marketing, 
				  
				(  
                   Select Sum(SatisToplam) from SiparislerTB s, SiparisUrunTB u where s.SiparisNo=u.SiparisNo  
                   and s.SiparisDurumID=3 and s.MusteriID=m.ID and Year(YuklemeTarihi)=?  and MONTH(YuklemeTarihi) =?  and  (s.depo_yukleme=1 or m.ID=3444) and s.SiparisDurumID=3
                ) 
                    
                as Fob, 
                
                (  
                   Select Sum(SatisToplam) from SiparislerTB s, SiparisUrunTB u where s.SiparisNo=u.SiparisNo  
                   and s.SiparisDurumID=3 and s.MusteriID=m.ID and Year(YuklemeTarihi)=? and MONTH(YuklemeTarihi) =? and  (s.depo_yukleme=1 or m.ID=3444) and s.SiparisDurumID=3
                )  +  
                (  
                    Select Sum(s.NavlunSatis + s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 ) from SiparislerTB s  
                    where s.MusteriID=m.ID and YEAR(s.YuklemeTarihi)=? and MONTH(s.YuklemeTarihi) =?  and  (s.depo_yukleme=1 or m.ID=3444) and s.SiparisDurumID=3
                )  
                as Dtp 
                from  
                MusterilerTB m,YeniTeklif_UlkeTB u  
                where 
                u.Id = m.UlkeId  
              
                order by  m.FirmaAdi asc
            """,(yil,ay,yil,ay,yil,ay)
        ) 

        liste = list()

        for item in result:
            model = YuklemeAylikModel()
           
            if item.Fob != None and item.Fob !=0 :

                model.musteri_adii = item.MusteriAdi
            
                model.fob = item.Fob
                model.dtp = item.Dtp
            
                model.marketing = item.Marketing
                liste.append(model)

        schema = YuklemeAylikSchema(many=True)

        return sorted(schema.dump(liste), key=lambda x:x['dtp'],reverse=True)

    def getYuklemeRaporYillik(self,yil,ay):

        result = self.data.getStoreList(
            """
             select  
                 m.ID as MusteriId,  
                 m.FirmaAdi as MusteriAdi,  
                  m.Marketing, 
				  
				(  
                   Select Sum(SatisToplam) from SiparislerTB s, SiparisUrunTB u where s.SiparisNo=u.SiparisNo  
                   and s.SiparisDurumID=3 and s.MusteriID=m.ID and Year(YuklemeTarihi)=?  and MONTH(YuklemeTarihi) <=?  and  (s.depo_yukleme=1 or m.ID=3444) and s.SiparisDurumID=3
                ) 
                    
                as Fob, 
                
                (  
                   Select Sum(SatisToplam) from SiparislerTB s, SiparisUrunTB u where s.SiparisNo=u.SiparisNo  
                   and s.SiparisDurumID=3 and s.MusteriID=m.ID and Year(YuklemeTarihi)=? and MONTH(YuklemeTarihi) <=? and  (s.depo_yukleme=1 or m.ID=3444) and s.SiparisDurumID=3
                )  +  
                (  
                    Select Sum(s.NavlunSatis + s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 ) from SiparislerTB s  
                    where s.MusteriID=m.ID and YEAR(s.YuklemeTarihi)=? and MONTH(s.YuklemeTarihi) <=?  and  (s.depo_yukleme=1 or m.ID=3444)and s.SiparisDurumID=3
                )  
                    
                as Dtp 
               
                from  
                MusterilerTB m,YeniTeklif_UlkeTB u  
                where 
                u.Id = m.UlkeId  
                
               
            """,(yil,ay,yil,ay,yil,ay)
        ) 
        
        liste = list()
         
       
        for item in result:
          
            model = YuklemeYillikModel()
           
            if item.Fob != None and item.Fob !=0 :

                model.musteri_adi = item.MusteriAdi
            
                model.fob = item.Fob
                model.dtp = item.Dtp
                model.musteriID = item.MusteriId
                model.marketing = item.Marketing
                liste.append(model)

        schema = YuklemeYillikSchema(many=True) 

        return sorted(schema.dump(liste), key=lambda x:x['dtp'],reverse=True)

  
 

   

   
                       
           
    
        
    def __set(self):
        pass