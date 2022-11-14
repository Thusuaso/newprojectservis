from helpers import SqlConnect



class Finans:

    def __init__(self):
        self.data = SqlConnect().data

    def getYillilAlacakOzet(self):
        
        localMasraf,localMasrafHepsi = self.__getYillik_SiparisLocalMasraflar()
        urunBedeli,urunBedeliHepsi = self.__getYillik_SiparisUrunBedeli()
        odeme,odemeHepsi = self.__getYillik_SiparisOdemeler()

        mekmar = (localMasraf + urunBedeli) - odeme
        hepsi = (localMasrafHepsi + urunBedeliHepsi) - odemeHepsi

        return mekmar,hepsi

    def getAylikAlacakOzet(self):
        
        localMasraf,localMasrafHepsi = self.__getAylik_SiparisLocalMasraflar()
        urunBedeli,urunBedeliHepsi = self.__getAylik_SiparisUrunBedeli()
        odeme,odemeHepsi = self.__getAylik_SiparisOdemeler()

        mekmar = (localMasraf + urunBedeli) - odeme
        hepsi = (localMasrafHepsi + urunBedeliHepsi) - odemeHepsi

        return mekmar,hepsi

    def __getYillik_SiparisLocalMasraflar(self):

        result_1 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(NavlunSatis + DetayTutar_1 + DetayTutar_2 + DetayTutar_3 ) as LocalMasraf
            from
            SiparislerTB s,MusterilerTB m
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and m.Marketing in ('Mekmar','BD','SU')
            group by Year(s.YuklemeTarihi)
            """
        )
        result_2 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(NavlunSatis + DetayTutar_1 + DetayTutar_2 + DetayTutar_3 ) as LocalMasraf
            from
            SiparislerTB s,MusterilerTB m
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())            
            group by Year(s.YuklemeTarihi)
            """
        )

        tutar = 0
        tutarHepsi = 0

        if len(result_1) == 1:
            tutar = float(result_1[0].LocalMasraf)
        
        if len(result_2) == 1:
            tutarHepsi = float(result_2[0].LocalMasraf)

        return tutar,tutarHepsi

    def __getYillik_SiparisUrunBedeli(self):

        result_1 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as UrunBedeli
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and m.Marketing in ('Mekmar','BD','SU') and u.SiparisNo=s.SiparisNo
            group by Year(s.YuklemeTarihi)
            """
        )

        result_2 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as UrunBedeli
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and u.SiparisNo=s.SiparisNo
            group by Year(s.YuklemeTarihi)
            """
        )

        tutar = 0
        tutarHepsi = 0

        if len(result_1) == 1:
            tutar = float(result_1[0].UrunBedeli)
        if len(result_2) == 1:
            tutarHepsi = float(result_2[0].UrunBedeli)

        return tutar,tutarHepsi

    def __getYillik_SiparisOdemeler(self):

        result_1 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(o.Tutar) as Odeme
            from
            SiparislerTB s,MusterilerTB m,OdemelerTB o
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and m.Marketing in ('Mekmar','BD','SU') and o.SiparisNo=s.SiparisNo
            group by Year(s.YuklemeTarihi)
            """
        )

        result_2 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(o.Tutar) as Odeme
            from
            SiparislerTB s,MusterilerTB m,OdemelerTB o
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and o.SiparisNo=s.SiparisNo
            group by Year(s.YuklemeTarihi)
            """
        )

        tutar = 0
        tutarHepsi = 0

        if len(result_1) == 1:
            tutar = float(result_1[0].Odeme)
        
        if len(result_2) == 1:
            tutarHepsi = float(result_2[0].Odeme)

        return tutar,tutarHepsi

    def __getAylik_SiparisLocalMasraflar(self):

        result_1 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(NavlunSatis + DetayTutar_1 + DetayTutar_2 + DetayTutar_3 ) as LocalMasraf
            from
            SiparislerTB s,MusterilerTB m
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and Month(s.YuklemeTarihi)=Month(GetDate())
            and m.Marketing in ('Mekmar','BD','SU')
            group by Year(s.YuklemeTarihi)
            """
        )

        result_2 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(NavlunSatis + DetayTutar_1 + DetayTutar_2 + DetayTutar_3 ) as LocalMasraf
            from
            SiparislerTB s,MusterilerTB m
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and Month(s.YuklemeTarihi)=Month(GetDate())
            group by Year(s.YuklemeTarihi)
            """
        )

        tutar = 0
        tutarHepsi = 0

        if len(result_1) == 1:
            if result_1[0].LocalMasraf != None:
                tutar = float(result_1[0].LocalMasraf)

        if len(result_2) == 1:
            if result_2[0].LocalMasraf != None:
                tutarHepsi = float(result_2[0].LocalMasraf)

        return tutar,tutarHepsi

    def __getAylik_SiparisUrunBedeli(self):

        result_1 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as UrunBedeli
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and Month(s.YuklemeTarihi)=Month(GetDate())
            and m.Marketing in ('Mekmar','BD','SU') and u.SiparisNo=s.SiparisNo
            group by Year(s.YuklemeTarihi)
            """
        )

        result_2 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as UrunBedeli
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and Month(s.YuklemeTarihi)=Month(GetDate())
            and u.SiparisNo=s.SiparisNo
            group by Year(s.YuklemeTarihi)
            """
        )

        tutar = 0
        tutarHepsi = 0

        if len(result_1) == 1:
            tutar = float(result_1[0].UrunBedeli)

        if len(result_2) == 1:
            tutarHepsi = float(result_2[0].UrunBedeli)

        return tutar,tutarHepsi

    def __getAylik_SiparisOdemeler(self):

        result_1 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(o.Tutar) as Odeme
            from
            SiparislerTB s,MusterilerTB m,OdemelerTB o
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and Month(s.YuklemeTarihi)=Month(GetDate())
            and m.Marketing in ('Mekmar','BD','SU') and o.SiparisNo=s.SiparisNo
            group by Year(s.YuklemeTarihi)
            """
        )

        result_2 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(o.Tutar) as Odeme
            from
            SiparislerTB s,MusterilerTB m,OdemelerTB o
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=year(Getdate())
            and Month(s.YuklemeTarihi)=Month(GetDate())
            and o.SiparisNo=s.SiparisNo
            group by Year(s.YuklemeTarihi)
            """
        )

        tutar = 0
        tutarHepsi = 0

        if len(result_1) == 1:
            tutar = float(result_1[0].Odeme)

        if len(result_2) == 1:
            tutarHepsi = float(result_2[0].Odeme)

        return tutar,tutarHepsi

    