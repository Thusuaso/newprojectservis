from models.finans import PesinatIslemSchema,PesinatIslemModel
from helpers import SqlConnect


class PesinatIslemListe:

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
            (Select Sum(o.Tutar) from OdemelerTB o where o.SiparisNo=s.SiparisNo) as Odenen,
            (select k.MailAdres from KullaniciTB k where s.SiparisSahibi = k.ID) as Mail,
			 m.Marketing

            from
            SiparislerTB s,MusterilerTB m
            where
            s.SiparisDurumID in (1,2)
            and s.Pesinat >0
            and m.ID = s.MusteriID
            group by s.SiparisNo,s.MusteriID,m.FirmaAdi,m.Marketing,s.siparisSahibi,s.SiparisTarihi
            order by s.SiparisTarihi desc

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

                model = PesinatIslemModel()
                model.id = id 
                model.musteri_adi = item.FirmaAdi 
                model.musteri_id = item.MusteriID
                model.siparis_no = item.SiparisNo 
                model.tutar = round(kalan_tutar,2)
                model.temsilci_mail = item.Mail
                model.marketing = item.Marketing
                
                liste.append(model)

                id += 1

            kalan_tutar = 0

        schema = PesinatIslemSchema(many=True)

        return schema.dump(liste)