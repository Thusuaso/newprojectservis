from helpers import SqlConnect


class EfesOdemeler:

    def __init__(self,yil):

        self.data = SqlConnect().data
        
        self.dtOdemeList = self.data.getStoreList(

            """
            select
            o.SiparisNo,
            o.MusteriID,
            o.Tutar 
            from OdemelerTB o
            where Year(o.Tarih)=?
            and o.SiparisNo in 
            (
                Select s.SiparisNo from SiparislerTB s where s.SiparisNo=o.SiparisNo
                and s.SiparisDurumID=3 and s.FaturaKesimTurID=2
            )
            """,(yil)
        )

        self.dtEskiOdemeList = self.data.getStoreList(

            """
            select
            o.SiparisNo,
            o.MusteriID,
            o.Tutar 
            from OdemelerTB o
            where Year(o.Tarih)<?
            and o.SiparisNo in 
            (
                Select s.SiparisNo from SiparislerTB s where s.SiparisNo=o.SiparisNo
                and s.SiparisDurumID=3 and s.FaturaKesimTurID=2
                
            )
            """,(yil)
        )

        self.dtPesinatList = self.data.getStoreList(
            """
            select
            o.Tutar,
            o.MusteriID
            from
            OdemelerTB o,SiparislerTB s
            where
            s.SiparisNo=o.SiparisNo
            and s.SiparisDurumID in (1,2) and s.FaturaKesimTurID=2
            and Year(o.Tarih)=?
            """,(yil)
        )
       
        self.dtEskiPesinatList = self.data.getStoreList(
            """
            select
            o.SiparisNo,
            o.MusteriID,
            o.Tutar
            from
            OdemelerTB o
            where
            o.SiparisNo in
            (
            Select s.SiparisNo from SiparislerTB s where
            s.SiparisNo=o.SiparisNo and s.SiparisDurumID in (1,2) and s.FaturaKesimTurID=2
            )
            and Year(o.Tarih)<?
            """,(yil)
        )

    def getOdeme(self,musteriid):

        odeme_toplam = float(0)

        for item in self.dtOdemeList:

            if musteriid == item.MusteriID and item.Tutar != None:
                odeme_toplam += float(item.Tutar)

        return odeme_toplam

    def getOdeme_GecenYil(self,musteriid):

        odeme_toplam = float(0)

        for item in self.dtEskiOdemeList:

            if musteriid == item.MusteriID and item.Tutar != None:
                odeme_toplam += float(item.Tutar)

        return odeme_toplam

    def getPesinat(self,musteriid):

        odeme_toplam = float(0)

        for item in self.dtPesinatList:

            if musteriid == item.MusteriID and item.Tutar != None :
                odeme_toplam += float(item.Tutar)

        return odeme_toplam

    def getEskiPesinat(self,musteri_id):

        tutar = 0
       
        for item in self.dtEskiPesinatList:
            if item.MusteriID == musteri_id:
                tutar += item.Tutar

        
        return tutar