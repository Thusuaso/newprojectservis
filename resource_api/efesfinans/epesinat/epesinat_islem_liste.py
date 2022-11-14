from models.efesfinans import EfesPesinatIslemSchema,EfesPesinatIslemModel
from helpers import SqlConnect


class EfesPesinatIslemListe:

    def __init__(self):

        self.data = SqlConnect().data 

    def getPesinatIslemListe(self):

        result = self.data.getList(
            """
            select
            s.SiparisNo,
            m.FirmaAdi,
            s.MusteriID,
            Sum(s.Pesinat) as Pesinat,
            (Select Sum(o.Tutar) from OdemelerTB o where o.SiparisNo=s.SiparisNo) as Odenen
            from
            SiparislerTB s,MusterilerTB m
            where
            s.SiparisDurumID in (1,2)
            and s.Pesinat >0
            and m.ID = s.MusteriID
            and s.FaturaKesimTurID=2
            and YEAR(s.SiparisTar)> 2018
            group by s.SiparisNo,s.MusteriID,m.FirmaAdi
            """
        )

        liste = list()

        id = 1
        for item in result:

            pesinat = float(item.Pesinat)
            odenen = 0

            if item.Odenen != None :
                odenen = float(item.Odenen)

            kalan_tutar = pesinat - odenen

            if kalan_tutar > 0:

                model = EfesPesinatIslemModel()
                model.id = id 
                model.musteri_adi = item.FirmaAdi 
                model.musteri_id = item.MusteriID
                model.siparis_no = item.SiparisNo 
                model.tutar = kalan_tutar

                liste.append(model)

                id += 1

            kalan_tutar = 0

        schema = EfesPesinatIslemSchema(many=True)

        return schema.dump(liste)