from helpers import SqlConnect,TarihIslemler
from models.efesfinans import EfesMusteriAyrintiSchema,EfesMusteriAyrintiModel
from models.efesfinans import EfesMusteriOdemeSchema,EfesMusteriOdemeModel
from models.efesfinans import EfesMusteriOdemeSecimSchema,EfesMusteriOdemeSecimModel


class EfesMusteriAyrinti:

    def __init__(self,musteriid):

        self.data = SqlConnect().data
        self.musteri_id = musteriid

    def getKonteynerAyrintiList(self):

        yukleme_list = self.__yuklenenler()
        
        for item in self.__uretilenler():

            yukleme_list.append(item)

        schema = EfesMusteriAyrintiSchema(many=True)
       
        return schema.dump(yukleme_list)
    
    def __yuklenenler(self):

        tarihIslem = TarihIslemler()
        result = self.data.getStoreList(

            """
            select
            s.ID,
            s.SiparisNo,
            s.YuklemeTarihi,
            s.Vade,
            m.FirmaAdi,
            s.MusteriID,
            s.NavlunSatis,
            s.DetayTutar_1,
            s.DetayTutar_2,
            s.DetayTutar_3,
           
            (
            select Sum(Tutar) from OdemelerTB o where o.SiparisNo=s.SiparisNo
            and s.MusteriID=m.ID
            ) as Odeme,
            (
              select Sum(SatisToplam) from SiparisUrunTB u where u.SiparisNo=s.SiparisNo
            ) as UrunBedeli        
            from
            SiparislerTB s,MusterilerTB m
            where
            s.MusteriID=m.ID
            and m.ID=?
            and s.SiparisDurumID=3
            and s.FaturaKesimTurID=2
            and YEAR(s.YuklemeTarihi) > 2018
            order by s.YuklemeTarihi desc
            """,(self.musteri_id)
        )

        liste = list()
       
        for item in result:
            
            model = EfesMusteriAyrintiModel()
            model.id = item.ID 
            model.musteriadi = item.FirmaAdi
            model.musteri_id = item.MusteriID
            model.siparisno = item.SiparisNo 
            model.tip = "Yükleme"           
            if item.YuklemeTarihi != None:
                model.yuklemetarihi = tarihIslem.getDate(item.YuklemeTarihi).strftime("%d-%m-%Y")               
            if item.Vade != None:
                model.vade = tarihIslem.getDate(item.Vade).strftime("%d-%m-%Y")

            navlun = 0 
            tutar_1 = 0
            tutar_2 = 0
            tutar_3 = 0
           
            urun_bedel = 0
            odeme = 0

            if item.NavlunSatis != None:
                navlun = item.NavlunSatis
            if item.DetayTutar_1 != None:
                tutar_1 = item.DetayTutar_1
            if item.DetayTutar_2 != None:
                tutar_2 = item.DetayTutar_2
            if item.DetayTutar_3 != None:
                tutar_3 = item.DetayTutar_3
               
            if item.UrunBedeli != None:
                urun_bedel = item.UrunBedeli
            if item.Odeme != None:
                odeme = item.Odeme

            model.toplam = navlun + tutar_1 + tutar_2 + tutar_3  + urun_bedel
            
            model.kalan = model.toplam - odeme

            liste.append(model)

        return liste  

    def __uretilenler(self):

        tarihIslem = TarihIslemler()
        result = self.data.getStoreList(

            """
            select
            s.ID,
            s.SiparisNo,
            s.YuklemeTarihi,
            s.Vade,
            m.FirmaAdi,
            s.MusteriID,
            s.Pesinat,
            (
            select Sum(Tutar) from OdemelerTB o where o.SiparisNo=s.SiparisNo
            and s.MusteriID=m.ID
            ) as Odeme,
            (
            select Sum(SatisToplam) from SiparisUrunTB u where u.SiparisNo=s.SiparisNo
            ) as UrunBedeli
            from
            SiparislerTB s,MusterilerTB m
            where
            s.MusteriID=m.ID
            and m.ID=?
            and s.FaturaKesimTurID=2
            and s.Pesinat > 0
            and YEAR(s.YuklemeTarihi) > 2018
            and s.SiparisDurumID in (1,2)
            """,(self.musteri_id)
        )

        liste = list()
       
        for item in result:
            
            model = EfesMusteriAyrintiModel()
            model.id = item.ID 
            model.musteriadi = item.FirmaAdi
            model.musteri_id = item.MusteriID
            model.siparisno = item.SiparisNo 
            model.tip = "Üretim"
            if item.YuklemeTarihi != None:
                model.yuklemetarihi = tarihIslem.getDate(item.YuklemeTarihi).strftime("%d-%m-%Y")
            if item.Vade != None:
                model.vade = tarihIslem.getDate(item.Vade).strftime("%d-%m-%Y")

           
            odeme = 0

            if item.Odeme != None:
                odeme = item.Odeme

            model.toplam = item.Pesinat
            model.kalan = model.toplam - odeme

            liste.append(model)

        return liste      

    def getOdemeListesi(self):

        tarihIslem = TarihIslemler()
        result = self.data.getStoreList(

            """
            select
            o.Tarih,
            sum(o.Tutar) as Tutar
            from
            OdemelerTB o
            where o.MusteriID=?
            and o.SiparisNo in
            (
            Select s.SiparisNo from SiparislerTB s
            where s.SiparisNo=o.SiparisNo
             and s.FaturaKesimTurID=2
            and s.MusteriID=?
            ) and YEAR(o.Tarih) > 2018
            group by o.Tarih
            order by o.Tarih asc
                        """,(self.musteri_id,self.musteri_id)
        )

        liste = list()

        key = 1

        for item in result:
          
            model = EfesMusteriOdemeModel()
            model.id = key
            if item.Tarih != None:
                model.tarih = tarihIslem.getDate(item.Tarih).strftime("%d-%m-%Y")

            model.tutar = item.Tutar         
            liste.append(model)

            key += 1

        schema = EfesMusteriOdemeSchema(many=True)
       
        return schema.dump(liste)

    def getOdemeSecimPoList(self,tarih):
        

        result = self.data.getStoreList(
            """
            select
            o.ID,
            o.SiparisNo,
            o.Tutar,
            o.Aciklama,
            o.Masraf
            from
            OdemelerTB o
            where o.MusteriID=?
            and o.Tarih=?
            and o.SiparisNo in
            (
            Select s.SiparisNo from SiparislerTB s
            where s.SiparisNo=o.SiparisNo
             and s.FaturaKesimTurID=2
            and s.MusteriID=o.MusteriID
            ) 
            """,(self.musteri_id,tarih)
        )

        liste = list()

        for item in result:

            model = EfesMusteriOdemeSecimModel()
            model.id = item.ID
            model.siparisno = item.SiparisNo
            model.tutar = item.Tutar
            model.aciklama = item.Aciklama
            model.masraf = item.Masraf
            liste.append(model)

        schema = EfesMusteriOdemeSecimSchema(many=True)

        return schema.dump(liste)

          
