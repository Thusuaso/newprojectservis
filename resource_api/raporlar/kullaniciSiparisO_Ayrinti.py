from helpers import SqlConnect,TarihIslemler
from models.raporlar import *



class KullaniciSevSipAyrinti:

    def __init__(self,username):

        self.data = SqlConnect().data
        self.kullaniciId = self.data.getStoreList("Select ID from KullaniciTB where KullaniciAdi=?",(username))[0].ID

    def getBuYilSevkiyatAyrinti(self,ay):

        result = self.data.getStoreList(
            """
            SELECT
	        s.YuklemeTarihi,
            u.SiparisNo,
            sum(u.SatisToplam) as SatisToplam,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
           
			YEAR(s.YuklemeTarihi) as yil ,
			Month(s.YuklemeTarihi) as ay,
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim 
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.YuklemeTarihi) =  Year(GetDate())
            and s.SiparisDurumID=3
            and s.MusteriID in (Select m.ID from MusterilerTB m
            where m.ID=s.MusteriID)
            and s.SiparisSahibi=? 
            and Month(s.YuklemeTarihi) = ?

            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.YuklemeTarihi,s.TeslimTurID
            order by s.YuklemeTarihi asc
            """,(self.kullaniciId ,ay)
        )

        liste = list()
        id = 1
        for item in result:

            model = SevSipAyrintiModel()

            model.id = id
            
            model.tarih = item.YuklemeTarihi
            
            model.siparisnumarasi = item.SiparisNo
            model.satistoplam = item.SatisToplam
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
            
            model.navlun = item.NavlunSatis
            model.musteri = item.musteri
            model.yil = item.yil
            model.ay = item.ay
            model.teslim = item.Teslim


            liste.append(model)

            id += 1

        schema = SevSipAyrintiSchema(many=True)

        return schema.dump(liste)

    def getGecenYilSevkiyatAyrinti(self,ay):

        result = self.data.getStoreList(
            """
          SELECT
	        s.YuklemeTarihi,
            u.SiparisNo,
            s.YuklemeTarihi,
            sum(u.SatisToplam) as SatisToplam,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
          
			YEAR(s.YuklemeTarihi) as yil ,
			Month(s.YuklemeTarihi) as ay,
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim  
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.YuklemeTarihi) =  Year(GetDate())-1
            and s.SiparisDurumID=3
            and s.MusteriID in (Select m.ID from MusterilerTB m
            where m.ID=s.MusteriID  )
            and s.SiparisSahibi=?
            and Month(s.YuklemeTarihi) = ?

            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.YuklemeTarihi,s.TeslimTurID,s.YuklemeTarihi
            order by s.YuklemeTarihi asc
            """,(self.kullaniciId , ay)
        )

        liste = list()
        id = 1
      
        for item in result:

            model = SevSipAyrintiModel()
          
            model.id = id
                
            model.tarih = item.YuklemeTarihi
                
            model.siparisnumarasi = item.SiparisNo
            model.satistoplam = item.SatisToplam
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
            
            model.navlun = item.NavlunSatis
            model.musteri = item.musteri
            model.yil = item.yil
            model.ay = item.ay
            model.teslim = item.Teslim
            id += 1


            liste.append(model)

               
        schema = SevSipAyrintiSchema(many=True)

        return schema.dump(liste)

        


    def getGecenYilSiparisAyrinti(self,ay):

        result = self.data.getStoreList(
            """
              SELECT
            u.SiparisNo,
            sum(u.SatisToplam) as SatisToplam,
            year(s.SiparisTarihi) as yil,
            s.YuklemeTarihi,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
            
            s.SiparisTarihi,
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim  
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.SiparisTarihi) = Year(GetDate())-1
            and s.MusteriID in (Select m.ID from MusterilerTB m
			
            where m.ID=s.MusteriID  )
            and s.SiparisSahibi=?
            and Month(s.SiparisTarihi)= ?
			
			group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID,s.YuklemeTarihi
			order by s.SiparisTarihi asc
            """,(self.kullaniciId ,ay)
        )

        liste = list()
        id = 1
        a = 1
        for item in result:
          model = SevSipAyrintiModel()  
          if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
              
          else:
           

            model.id = id
            
            model.tarih = item.SiparisTarihi
            
            model.siparisnumarasi = item.SiparisNo
            model.satistoplam = item.SatisToplam
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
            
            model.navlun = item.NavlunSatis
            model.musteri = item.musteri
            model.teslim = item.Teslim
            model.yil = item.yil

            liste.append(model)

            id += 1

        schema = SevSipAyrintiSchema(many=True)

        return schema.dump(liste)        
   
    def getBuYilSiparisAyrinti(self,ay):

        result = self.data.getStoreList(
            """
              SELECT
            u.SiparisNo,
            year(s.SiparisTarihi) as yil,
            sum(u.SatisToplam) as SatisToplam,
            s.YuklemeTarihi,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
            
            s.SiparisTarihi,
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim 
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.SiparisTarihi) = Year(GetDate())
            and s.MusteriID in (Select m.ID from MusterilerTB m
			
            where m.ID=s.MusteriID  )
            and s.SiparisSahibi=?
            and Month(s.SiparisTarihi)= ?
		
			group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID,s.YuklemeTarihi
			order by s.SiparisTarihi asc
            """,(self.kullaniciId,ay)
        )

        liste = list()
        id = 1
        a = 1
        for item in result:
           
            model = SevSipAyrintiModel()
            if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                
                  a +=1
              
            else:    
                model.id = id
                
                model.tarih = item.SiparisTarihi
                
                model.siparisnumarasi = item.SiparisNo
                model.satistoplam = item.SatisToplam
                model.detay1 = item.DetayTutar_1
                model.detay2 = item.DetayTutar_2
                model.detay3 = item.DetayTutar_3
                
                model.navlun = item.NavlunSatis
                model.musteri = item.musteri
                model.teslim = item.Teslim
                model.yil = item.yil


                liste.append(model)

                id += 1

        schema = SevSipAyrintiSchema(many=True)

        return schema.dump(liste) 


   