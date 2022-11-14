from helpers import SqlConnect
from models.raporlar import *


class TeklifRapor:

    def __init__(self):
        self.data = SqlConnect().data
        self.proformaYillikList = self.data.getList(
            """
            select 
            k.KullaniciAdi,
            count(*) as TeklifSayisi
            from
            YeniTeklifTB t,KullaniciTB k
            where
            t.KullaniciId = k.ID
            and t.Proforma_Cloud=1 and Year(Tarih)=Year(GetDate())           
            group by k.KullaniciAdi
            order by count(*) desc
            """
        )

        self.proformaAylikList = self.data.getList(
            """
            select 
            k.KullaniciAdi,
            count(*) as TeklifSayisi
            from
            YeniTeklifTB t,KullaniciTB k
            where
            t.KullaniciId = k.ID
            and t.Proforma_Cloud=1 and Year(Tarih)=Year(GetDate())
            and Month(Tarih)=Month(GetDate())
            group by k.KullaniciAdi
            order by count(*) desc
            """
        )

        self.grafikRapor = list()

    
    def getTeklifAylikList(self):

        result = self.data.getList(
            """
            select 
            k.KullaniciAdi,
            count(*) as TeklifSayisi
            from
            YeniTeklifTB t,KullaniciTB k
            where
            t.KullaniciId = k.ID
            and t.TakipEt=1 and Year(Tarih)=Year(GetDate())
            and Month(Tarih)=Month(GetDate())
            group by k.KullaniciAdi
            order by count(*) desc
            """
        )

        liste = list()
        id = 1
        for item in result:
            model = TeklifRaporModel()
            model.id = id 
            model.adi = item.KullaniciAdi 
            model.teklifSayisi = item.TeklifSayisi
            model.proformaSayisi = self.__getProformaSayisiAylik(model.adi)

            liste.append(model)

        schema = TeklifRaporSchema(many=True)

        return schema.dump(liste)

    def getTeklifAylikAyrintiList(self,kullaniciAdi):

        result = self.data.getStoreList(
            """
            select 
                t.Id,
                k.KullaniciAdi,
				(select m.MusteriAdi from YeniTeklif_MusterilerTB m where m.Id=t.MusteriId) as musteri,
				t.Proforma_Cloud_Dosya,
				t.Numune_Cloud_Dosya,
				t.Teklif_Cloud_Dosya
             from
                YeniTeklifTB t,KullaniciTB k
            where
                t.KullaniciId = k.ID
                and t.TakipEt=1 and Year(Tarih)=Year(GetDate())
                and Month(Tarih)=Month(GetDate())
                and k.KullaniciAdi = ?
            group by 
                k.KullaniciAdi,
                t.MusteriId,
                t.Proforma_Cloud_Dosya,
                t.Numune_Cloud_Dosya,
                t.Teklif_Cloud_Dosya,
                t.Id
            order by count(*) desc
            """,(kullaniciAdi)
        )

        liste = list()
        id = 0 
        for item in result:
            model = TeklifAyrintiRaporModel()
            model.id = id
            model.musteri = item.musteri
            model.proforma_cloud_dosya = f"https://file-service.mekmar.com/file/download/teklif/proforma/{item.Id}/{item.Proforma_Cloud_Dosya}"
            model.numune_cloud_dosya =f"https://file-service.mekmar.com/file/download/teklif/teklifNumune/{item.Id}/{item.Numune_Cloud_Dosya}"
            model.teklif_cloud_dosya = f"https://file-service.mekmar.com/file/download/teklif/teklifDosya/{item.Id}/{item.Teklif_Cloud_Dosya}"
            model.proforma = item.Proforma_Cloud_Dosya
            model.numune = item.Numune_Cloud_Dosya
            model.teklif = item.Teklif_Cloud_Dosya
            id = id +1

            liste.append(model)

        schema = TeklifAyrintiRaporSchema(many=True)

        return schema.dump(liste)   

    def getTeklifYillikList(self):

        result = self.data.getList(
            """
            select 
            k.KullaniciAdi,
            count(*) as TeklifSayisi
            from
            YeniTeklifTB t,KullaniciTB k
            where
            t.KullaniciId = k.ID
            and  Year(Tarih)=Year(GetDate())           
            group by k.KullaniciAdi
            order by count(*) desc
            """
        )

        liste = list()
        id = 1

        #grafik rapor için
        labels = list()
        datasets = list()
        data = list()
        for item in result:
            model = TeklifRaporModel()
            model.id = id 
            model.adi = item.KullaniciAdi 
            model.teklifSayisi = item.TeklifSayisi
            model.proformaSayisi = self.__getProformaSayisiYillik(model.adi)

            liste.append(model)

            labels.append(model.adi)
            data.append(model.teklifSayisi)

        dataset = {

            'label' : 'Personel',
            'backgroundColor' : '#80daeb',
            'data' : data
        }

        datasets.append(dataset)

        linerData = {

            'labels' : labels,
            'datasets' : datasets
        }

        self.grafikRapor = linerData

        schema = TeklifRaporSchema(many=True)

        return schema.dump(liste)

    def getGrafikRapor(self):

        return self.grafikRapor

    def __getProformaSayisiAylik(self,kullaniciAdi):

        proforma = 0

        for item in self.proformaAylikList:
            if kullaniciAdi == item.KullaniciAdi:
                proforma += item.TeklifSayisi

        return proforma

    def __getProformaSayisiYillik(self,kullaniciAdi):

        proforma = 0

        for item in self.proformaYillikList:
            if kullaniciAdi == item.KullaniciAdi:
                proforma += item.TeklifSayisi

        return proforma
    