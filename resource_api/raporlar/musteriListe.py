from helpers import SqlConnect,TarihIslemler
from models.raporlar import *
from models.operasyon import *
import datetime


class MusteriListesi:

    def __init__(self,username):

        self.data = SqlConnect().data
        self.kullaniciId = self.data.getStoreList("Select ID from KullaniciTB where KullaniciAdi=?",(username))[0].ID

  

    def getMusteriSiparis(self):
        liste = list()

        result = self.data.getStoreList(
            """
             select  
                 m.ID as MusteriId,  
                 m.FirmaAdi as MusteriAdi,  
                 u.UlkeAdi,  
                 u.Png_Flags as UlkeLogo,  
                (  
                   Select Sum(SatisToplam) from SiparislerTB s, SiparisUrunTB u where s.SiparisNo=u.SiparisNo  
                   and s.SiparisDurumID=3 and s.MusteriID=m.ID and Year(YuklemeTarihi)=Year(GetDate())  
                )  +  
                (  
                    Select Sum(s.NavlunSatis + s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 ) from SiparislerTB s  
                    where s.MusteriID=m.ID and YEAR(s.YuklemeTarihi)=Year(GetDate())  
                )  
                    
                as BuYilCiro,  
                (  
                    Select Sum(SatisToplam) from SiparislerTB s, SiparisUrunTB u where s.SiparisNo=u.SiparisNo  
                    and s.SiparisDurumID=3 and s.MusteriID=m.ID and Year(YuklemeTarihi)=Year(GetDate())-1  
                ) +  
                (  
                    Select Sum(s.NavlunSatis + s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 ) from SiparislerTB s  
                    where s.MusteriID=m.ID and YEAR(s.YuklemeTarihi)=Year(GetDate())-1
                )  
                    as GecenYilCiro,  
                (  
                    Select Sum(SatisToplam) from SiparislerTB s, SiparisUrunTB u where s.SiparisNo=u.SiparisNo  
                    and s.SiparisDurumID=3 and s.MusteriID=m.ID and Year(YuklemeTarihi)=Year(GetDate())-2  
                ) +  
                (  
                    Select Sum(s.NavlunSatis + s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 ) from SiparislerTB s  
                    where s.MusteriID=m.ID and YEAR(s.YuklemeTarihi)=Year(GetDate())-2  
                )  
                    as OncekiYilCiro,  
                (  
                    Select Sum(SatisToplam) from SiparislerTB s, SiparisUrunTB u where s.SiparisNo=u.SiparisNo  
                    and s.SiparisDurumID=3 and s.MusteriID=m.ID  
                ) +  
                (  
                    Select Sum(s.NavlunSatis + s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 ) from SiparislerTB s  
                    where s.MusteriID=m.ID   
                )   
                    
                as GenelCiro  
                from  
                MusterilerTB m,YeniTeklif_UlkeTB u  
                where m.MusteriTemsilciId=?
                and m.Marketing in ('Mekmar','MQ') and u.Id = m.UlkeId  
                order by GenelCiro desc
 
               """,(self.kullaniciId)
          )

        liste = list()
        
        for item in result:

            model = KullaniciModel()

            model.musteri_id = item.MusteriId
            model.musteri = item.MusteriAdi
            model.ulkeAdi = item.UlkeAdi
            model.logo = item.UlkeLogo
            model.BuYil = item.BuYilCiro
            model.GecenYil = item.GecenYilCiro
            model.OncekiYil = item.OncekiYilCiro
            model.Toplam = item.GenelCiro
           
           

            liste.append(model)

           

        schema = KullaniciSchema(many=True)

        return schema.dump(liste)    
        
    def getKullaniciAySiparisAyrinti(self):

        result1 = self.data.getStoreList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
            MONTH(s.SiparisTarihi) as Ay,
			m.FirmaAdi,
			s.SiparisNo,
			s.YuklemeTarihi,
			(select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi ) as temsilci,
            s.FaturaKesimTurID
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			and s.SiparisSahibi = ?
            and MONTH(s.SiparisTarihi)=Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo,s.SiparisSahibi,s.FaturaKesimTurID
            """,(self.kullaniciId)
        )
        result2 = self.data.getStoreList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
            MONTH(s.SiparisTarihi) as Ay,
			m.FirmaAdi,
			s.SiparisNo,
			s.YuklemeTarihi,
			(select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi ) as temsilci,
            s.FaturaKesimTurID
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			and s.SiparisSahibi = ?
            and MONTH(s.SiparisTarihi)< Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo,s.SiparisSahibi,s.FaturaKesimTurID
            """,(self.kullaniciId)
        )
        result3 = self.data.getStoreList(
            """
           select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam )
            as FobTutar,
			s.NavlunSatis ,
			s.DetayTutar_1 ,
			s.DetayTutar_2 ,
			s.DetayTutar_3 ,
           
            s.SiparisNo,
			(select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi) as temsilci,
            s.FaturaKesimTurID
			
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            
			and s.SiparisSahibi = ?
            and Year(s.YuklemeTarihi)= Year(GetDate())
		
            and MONTH(s.YuklemeTarihi)=Month(GetDate())
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,
			s.DetayTutar_1 ,
			s.DetayTutar_2 ,
			s.DetayTutar_3 ,  s.SiparisNo,s.SiparisSahibi,s.FaturaKesimTurID
            """,(self.kullaniciId)
        )
        result4 = self.data.getStoreList(
            """
           select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam )
            as FobTutar,
			s.NavlunSatis ,
			s.DetayTutar_1 ,
			s.DetayTutar_2 ,
			s.DetayTutar_3 ,
            
            s.SiparisNo,
			(select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi) as temsilci,
			s.FaturaKesimTurID
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            
			and s.SiparisSahibi = ?
            and Year(s.YuklemeTarihi)= Year(GetDate())
		
            and MONTH(s.YuklemeTarihi) < Month(GetDate())
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,
			s.DetayTutar_1 ,
			s.DetayTutar_2 ,
			s.DetayTutar_3 ,s.SiparisNo, s.SiparisSahibi,s.FaturaKesimTurID
            """,(self.kullaniciId)
        )
        result5 = self.data.getStoreList(
            """
           select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam )
            as FobTutar,
			s.NavlunSatis ,
			s.DetayTutar_1 ,
			s.DetayTutar_2 ,
			s.DetayTutar_3 ,
            
            s.SiparisNo,
			(select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi) as temsilci,
			s.FaturaKesimTurID
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            
			and s.SiparisSahibi = ?
            and Year(s.YuklemeTarihi)= Year(GetDate())-1
		
            and MONTH(s.YuklemeTarihi) <= Month(GetDate())
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,
			s.DetayTutar_1 ,
			s.DetayTutar_2 ,
			s.DetayTutar_3 , s.SiparisNo, s.SiparisSahibi,s.FaturaKesimTurID
            """,(self.kullaniciId)
        )
        result6 = self.data.getStoreList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
            MONTH(s.SiparisTarihi) as Ay,
			m.FirmaAdi,
			s.SiparisNo,
			s.YuklemeTarihi,
			(select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi ) as temsilci,
            s.FaturaKesimTurID
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())-1
			and s.SiparisSahibi = ?
            and MONTH(s.SiparisTarihi)<=Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo,s.SiparisSahibi,s.FaturaKesimTurID
            """,(self.kullaniciId)
        )
        liste = list()
        a = 0
       
        R3Aylik = 0
        R4Aylik = 0
        R7Aylik = 0
        R8Aylik = 0
        navlun = 0
        detay1 = 0
        detay2 = 0
        detay3 = 0
        
        navlunyil = 0
        detay1yil = 0
        detay2yil = 0
        detay3yil = 0
        navlun1yil = 0
        detay2yil = 0
        detay3yil = 0
        
       
        model = AnasayfaSiparisModel()

        for item in result1:

            if ( item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
            else:  
                if item.FobTutar != None:
                 model.fobAy += float(item.FobTutar)
                if item.FaturaKesimTurID ==2 :
                  model.EfesFobAy += float(item.FobTutar) 
                


        for item in result2:
            
            if (item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None) :
                  a +=1
            else:  
                if item.FobTutar != None:
                 model.FobYil += float(item.FobTutar) 
                if item.FaturaKesimTurID ==2 :
                  model.EfesFobYil += float(item.FobTutar)   

        for item in result3:
           if item.NavlunSatis != None:
                 navlun = item.NavlunSatis
           if item.DetayTutar_1 != None:
                detay1 = item.DetayTutar_1
           if item.DetayTutar_2 != None:
                detay2 = item.DetayTutar_2
           if item.DetayTutar_3 != None:
                detay3 = item.DetayTutar_3   
                 
           model.DdpAy += item.FobTutar  + navlun + detay1 + detay2 + detay3      
           if item.FaturaKesimTurID ==2 :
                 model.EfesDdpAy += item.FobTutar  + navlun + detay1 + detay2 + detay3   

        for item in result4:
           if item.NavlunSatis != None:
                 navlunyil = item.NavlunSatis
           if item.DetayTutar_1 != None:
                detay1yil = item.DetayTutar_1
           if item.DetayTutar_2 != None:
                detay2yil = item.DetayTutar_2
           if item.DetayTutar_3 != None:
                detay3yil = item.DetayTutar_3 
                   
           model.DdpYil += item.FobTutar  + navlunyil + detay1yil + detay2yil + detay3yil 
           if item.FaturaKesimTurID ==2 :
                 model.EfesDdpYil += item.FobTutar  + navlunyil + detay1yil + detay2yil + detay3yil    


        for item in result5:
           if item.NavlunSatis != None:
                 navlun1yil = item.NavlunSatis
           if item.DetayTutar_1 != None:
                detay1yil = item.DetayTutar_1
           if item.DetayTutar_2 != None:
                detay2yil = item.DetayTutar_2
           if item.DetayTutar_3 != None:
                detay3yil = item.DetayTutar_3  
                
           model.R14A += item.FobTutar  + navlun1yil + detay2yil + detay3yil  

        for item in result6:

            if (item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
            else:  
                if item.FobTutar != None:
                 model.R14B += float(item.FobTutar)
              
                

           
        liste.append(model)

           

       

        schema = AnasayfaSiparisSchema(many=True)
      
        return schema.dump(liste)   


    def getKullaniciTakipListesi(self):
        tarihIslem = TarihIslemler()
        result1 = self.data.getStoreList(
            """
            select
            s.ID,
            s.SiparisNo,
            m.FirmaAdi as MusteriAdi,
            s.Pesinat,
            NavlunSatis + DetayTutar_1 + DetayTutar_2 + DetayTutar_3  as Navlun,
            ( Select Sum(o.Tutar) from OdemelerTB o where o.SiparisNo=s.SiparisNo ) as Odemeler,
            (Select Sum(u.SatisToplam) from SiparisUrunTB u where u.SiparisNo=s.SiparisNo) as MalBedeli,
            (select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi ) as Sorumlu,
            s.Eta,
            s.KonteynerNo,
            s.YuklemeTarihi,
            s.KonsimentoDurum,
            s.Line,
            s.AktarmaLimanAdi
            from
            SiparislerTB s,MusterilerTB m
            where s.MusteriID=m.ID
            and s.SiparisDurumID=3 and Takip=1
			and ( s.SiparisSahibi = ?  or s.Operasyon = ? )
            order by s.ID desc
            """,(self.kullaniciId , self.kullaniciId)
        )
       
        liste = list()
        sira =1
        for item in result1:

            navlun = 0
            odemeler = 0
            mal_bedeli = 0
            sevk_tarihi = ""
            eta = ""
            model = SevkTakipModel()

            if item.Navlun != None:
                navlun = item.Navlun 
            
            if item.Odemeler != None:
                odemeler = item.Odemeler 
            
            if item.MalBedeli != None:
                mal_bedeli = item.MalBedeli
            model.sira = sira
            sira += 1
            if item.Eta != None: 
                try:
                    eta = tarihIslem.getDate(item.Eta).strftime("%d-%m-%Y")
                    bugun = datetime.date.today()
                    sontarih_str = eta.split('-')
                   
                    sontarih = datetime.date(int(sontarih_str[2]),int(sontarih_str[1]),int(sontarih_str[0]))
                    model.kalan_sure = (sontarih - bugun).days
                except Exception as e :
                    print('eta hatası : ', str(e))

            if item.YuklemeTarihi != None:
                sevk_tarihi = tarihIslem.getDate(item.YuklemeTarihi).strftime("%d-%m-%Y")

            
            model.id = item.ID 
            model.siparisno = item.SiparisNo 
            model.pesinat = item.Pesinat 
            model.kalan_alacak = (navlun + mal_bedeli) - odemeler
            model.sevk_tarihi = sevk_tarihi
            model.konteynerno = item.KonteynerNo 
            model.eta = eta
            model.sorumlusu = item.Sorumlu
            model.musteriadi = item.MusteriAdi
            model.konsimento = item.KonsimentoDurum
            model.line = item.Line
            model.liman = item.AktarmaLimanAdi

            liste.append(model)

        schema = SevkTakipSchema(many=True)

        return schema.dump(liste)             

    def getKullaniciSiparisYilAyrinti(self):
        
        
        result_1 = self.data.getStoreList(
            """
             SELECT
	        s.SiparisTarihi,
            u.SiparisNo,
            sum(u.SatisToplam) as SatisToplam,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
            
            s.YuklemeTarihi,
			YEAR(s.SiparisTarihi) as yil ,
			Month(s.SiparisTarihi) as ay,
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim 
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.SiparisTarihi) =  Year(GetDate())
            
            and s.MusteriID in (Select m.ID from MusterilerTB m
            where m.ID=s.MusteriID  and s.SiparisSahibi=? and m.Marketing!='Seleksiyon')
            and Month(s.SiparisTarihi) < Month(GetDate())
			
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID, s.YuklemeTarihi
            order by s.SiparisTarihi desc

            """,(self.kullaniciId)
        )
        liste = list()
        a = 0
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            if ( item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None):
                  a +=1
            else:          
                model.tarih = item.SiparisTarihi
                model.siparisNo = item.SiparisNo
                model.musteriadi = item.musteri
                model.satistoplam = item.SatisToplam
                model.navlun = item.NavlunSatis
                model.detay1 = item.DetayTutar_1
                model.detay2 = item.DetayTutar_2
                model.detay3 = item.DetayTutar_3
                
                model.teslim = item.Teslim
                liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste) 

    def getKullaniciSiparisAyAyrinti(self):
        
        
        result_1 = self.data.getStoreList(
            """
             SELECT
	        s.SiparisTarihi,
            u.SiparisNo,
            sum(u.SatisToplam) as SatisToplam,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
           
            s.YuklemeTarihi,
			YEAR(s.SiparisTarihi) as yil ,
			Month(s.SiparisTarihi) as ay,
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim 
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.SiparisTarihi) =  Year(GetDate())
            
            and s.MusteriID in (Select m.ID from MusterilerTB m
            where m.ID=s.MusteriID  and s.SiparisSahibi=? and m.Marketing!='Seleksiyon')
            and Month(s.SiparisTarihi) = Month(GetDate())
			
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID, s.YuklemeTarihi
            order by s.SiparisTarihi desc

            """,(self.kullaniciId)
        )
        liste = list()
        a = 0
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None) :
                  a +=1
            else:          
                model.tarih = item.SiparisTarihi
                model.siparisNo = item.SiparisNo
                model.musteriadi = item.musteri
                model.satistoplam = item.SatisToplam
                model.navlun = item.NavlunSatis
                model.detay1 = item.DetayTutar_1
                model.detay2 = item.DetayTutar_2
                model.detay3 = item.DetayTutar_3
                
                model.teslim = item.Teslim
                liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste)  


    def getKullaniciSevkAyAyrinti(self):
        
        
        result_1 = self.data.getStoreList( ## efes - mekmar - gelen ay sevk
            """
              SELECT
	        s.YuklemeTarihi,
            u.SiparisNo,
            sum(u.SatisToplam) as SatisToplam,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
		    
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim 
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.YuklemeTarihi) =  Year(GetDate())
           
            and s.MusteriID in (Select m.ID from MusterilerTB m
            where m.ID=s.MusteriID and s.SiparisSahibi=? and m.Marketing!='Seleksiyon')
            and Month(s.YuklemeTarihi) = Month(GetDate())
		    and s.SiparisDurumID=3
			
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.YuklemeTarihi,s.TeslimTurID
            order by s.YuklemeTarihi desc

            """,(self.kullaniciId)
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.YuklemeTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
           
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste)    

    def getKullaniciSevkYilAyrinti(self):
        
        
        result_1 = self.data.getStoreList( ## efes - mekmar - gelen ay sevk
            """
              SELECT
	        s.YuklemeTarihi,
            u.SiparisNo,
            sum(u.SatisToplam) as SatisToplam,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
		    
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim 
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.YuklemeTarihi) =  Year(GetDate())
            and s.SiparisDurumID=3
            and s.MusteriID in (Select m.ID from MusterilerTB m
            where m.ID=s.MusteriID and s.SiparisSahibi=?  and m.Marketing!='Seleksiyon')
            and Month(s.YuklemeTarihi) < Month(GetDate())
			
			
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.YuklemeTarihi,s.TeslimTurID
            order by s.YuklemeTarihi desc

            """,(self.kullaniciId)
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.YuklemeTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
            
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste)             
               


 