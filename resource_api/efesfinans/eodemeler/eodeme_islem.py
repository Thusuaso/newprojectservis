from models.efesfinans.eodemeler import *
from helpers import SqlConnect,TarihIslemler


class EfesOdemeIslem:

    def __init__(self):

        self.data = SqlConnect().data


    def getOdemeListesi(self,yil,ay):

        tarihIslem = TarihIslemler()
        result = self.data.getStoreList(

            """
            select          
            o.Tarih,
            m.FirmaAdi,
            sum(o.Tutar) as Tutar
            ,s.SiparisNo
            from
            OdemelerTB o,MusterilerTB m,SiparislerTB s
            where
            o.MusteriID=m.ID
            and s.MusteriID = m.ID
			and s.SiparisNo = o.SiparisNo
			and s.MusteriID=m.ID
			and s.FaturaKesimTurID=2
            and Year(o.Tarih)=? and Month(o.Tarih)=?
            group by o.Tarih,m.FirmaAdi,s.SiparisNo
            order by o.Tarih desc
            """,(yil,ay)
        )

        liste = list()
        id = 1
        for item in result:

            model = EfesOdemeListeModel()

            model.id = id
            if item.Tarih != None:
                model.tarih = tarihIslem.getDate(item.Tarih).strftime("%d-%m-%Y")
            
            model.musteriadi = item.FirmaAdi
            model.siparisno = item.SiparisNo
            model.tutar = item.Tutar

            liste.append(model)

            id += 1

        schema = EfesOdemeListeSchema(many=True)

        return schema.dump(liste)

    def getYilListesi(self):

        result = self.data.getList(
            """
            select
            Year(Tarih) as Yil
            from
            OdemelerTB
            group by Year(Tarih)
            order by Year(Tarih) desc
            """
        )

        id = 1

        liste = list()

        for item in result:

            model = EfesOdemeYilModel()
            model.id = id 
            model.yil = item.Yil

            liste.append(model)

            id += 1

        schema = EfesOdemeYilSchema(many=True)

        return schema.dump(liste)

    def getAyListesi(self,yil):

        result = self.data.getStoreList(
            """
            select
            Month(Tarih) as Ay
            from
            OdemelerTB
            where Year(Tarih)=?
            group by Month(Tarih)
            order by Month(Tarih) desc
            """,(yil)
        )

        liste = list()

        id = 1

        for item in result:

            model = EfesOdemeAyModel()
            model.id = id
            model.ay = item.Ay
            model.ay_str = self.__getAyStr(model.ay)

            liste.append(model)

        schema = EfesOdemeAySchema(many=True)

        return schema.dump(liste)

     
    def __getAyStr(self,ay):

        aylar = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']

        return aylar[ay - 1]

 



