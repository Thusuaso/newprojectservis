from helpers import SqlConnect
from models.raporlar import MusteriListeModel,MusteriListeSchema


class FinansListe:
    def __init__(self):        
        self.data = SqlConnect().data


    def mekmarList(self):

        result = self.data.getList(
            """
            select
            m.ID as MusteriId,
			m.FirmaAdi as MusteriAdi,
			Sum(s.NavlunSatis + s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 ) as CifBedel,
			(
			 Select
			 Sum(u.SatisToplam)
			 from
			 SiparislerTB st,SiparisUrunTB u
			 where st.SiparisNo=u.SiparisNo
			 and st.MusteriID=m.ID and st.SiparisDurumID=3
			) as UrunBedeli,
            (
			Select
			Sum(o.Tutar)
           
			from
			SiparislerTB so,OdemelerTB o
			where so.SiparisNo=o.SiparisNo and so.MusteriID=m.ID
            and so.SiparisDurumID=3

			) as OdemeBedeli,
             (select sum(o.Tutar) from SiparislerTB st ,OdemelerTB o where SiparisDurumID=2 and st.MusteriID=m.ID and o.SiparisNo=st.SiparisNo and  Year(o.Tarih)< Year(GetDate()))as eski ,
			(select sum(o.Tutar) from SiparislerTB st ,OdemelerTB o where SiparisDurumID=2 and st.MusteriID=m.ID and o.SiparisNo=st.SiparisNo and  Year(o.Tarih)= Year(GetDate()))as yeni 
            from
            SiparislerTB s,MusterilerTB m
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and m.Marketing in ('Mekmar','SU')
			group by m.ID,m.FirmaAdi
            """
        )

        liste = list()

        for item in result:

                model = MusteriListeModel()
                model.id = item.MusteriId 
                model.musteriAdi = item.MusteriAdi 
                model.Yenipesinat = item.yeni
                model.Eskipesinat = item.eski
                model.siparisBedel = float(item.CifBedel) + float(item.UrunBedeli)
                urunBedel = float(item.UrunBedeli)
                odeme = 0

                if item.OdemeBedeli != None:
                    odeme = float(item.OdemeBedeli)
                    model.odeme = float(item.OdemeBedeli)
                model.bakiye = (model.siparisBedel ) - odeme
                if model.bakiye !=0 : 
                   liste.append(model)

        schema = MusteriListeSchema(many=True)

        yeniList = sorted(liste,key=lambda x:x.bakiye,reverse=True)
        
       
        return schema.dump(yeniList)

    def hepsiList(self):

        result = self.data.getList(
            """
            select
            m.ID as MusteriId,
			m.FirmaAdi as MusteriAdi,
			Sum(s.NavlunSatis + s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 ) as CifBedel,
			(
			 Select
			 Sum(u.SatisToplam)
			 from
			 SiparislerTB st,SiparisUrunTB u
			 where st.SiparisNo=u.SiparisNo
			 and st.MusteriID=m.ID and st.SiparisDurumID=3
			) as UrunBedeli,
            (
			Select
			Sum(o.Tutar)
			from
			SiparislerTB so,OdemelerTB o
			where so.SiparisNo=o.SiparisNo and so.MusteriID=m.ID
            and so.SiparisDurumID=3
			) as OdemeBedeli,
              (select sum(o.Tutar) from SiparislerTB st ,OdemelerTB o where SiparisDurumID=2 and st.MusteriID=m.ID and o.SiparisNo=st.SiparisNo and  Year(o.Tarih)< Year(GetDate()))as eski ,
			(select sum(o.Tutar) from SiparislerTB st ,OdemelerTB o where SiparisDurumID=2 and st.MusteriID=m.ID and o.SiparisNo=st.SiparisNo and  Year(o.Tarih)= Year(GetDate()))as yeni 
            from
            SiparislerTB s,MusterilerTB m
            where
            s.MusteriID=m.ID and s.SiparisDurumID=3
            and m.Marketing in ('Mekmar','SU','Ghana','İç Piyasa')
			group by m.ID,m.FirmaAdi
            """
        )

        liste = list()
        kontrol = 0
        for item in result:

                model = MusteriListeModel()
                model.id = item.MusteriId 
                model.musteriAdi = item.MusteriAdi 
                model.Yenipesinat = item.yeni
                model.Eskipesinat = item.eski
                siparisBedel = float(item.CifBedel)
                urunBedel = float(item.UrunBedeli)
                odeme = 0

                if item.OdemeBedeli != None:
                    odeme = float(item.OdemeBedeli)

                model.bakiye = (siparisBedel + urunBedel) - odeme

                liste.append(model)

        schema = MusteriListeSchema(many=True)

        yeniList = sorted(liste,key=lambda x:x.bakiye,reverse=True)

      #  toplam = 0
      #  filterToplam = 0

        #  for item in liste:
          #    toplam += item.bakiye

        #  for item in yeniList:
            #  filterToplam += item.bakiye 

        #  fark = toplam - filterToplam

       #   if fark > 0:
          #    model = MusteriListeModel()
           #   model.id = 0
            #  model.musteriAdi = '.....'
           #   model.bakiye = fark

        yeniList.append(model)

       
        return schema.dump(yeniList)

        

