from models.satisci import *
from helpers import SqlConnect,TarihIslemler
from openpyxl import *
import shutil


class SatisciAyrinti:

    def __init__(self):

        self.data = SqlConnect().data

    def getAyrintiList(self,musteri_adi):

      
        result = self.data.getStoreList(
            """
             
        select k.KullaniciAdi,
                a.ID,
                a.MusteriAdi,
                a.Satisci_Cloud,
                a.Satisci_Cloud_Dosya,
                a.Aciklama,
                a.Baslik,
                a.Hatirlatma_Notu,
                a.Hatirlatma_Tarih,
                a.Tarih
       from SatisciAyrintiTB a , KullaniciTB k where k.ID = a.Temsilci and
            a.MusteriAdi = ?
            """,(musteri_adi)
        )

        
        liste = list()
        sira = 1
       
        for item in result:
            model = MusteriAyrintiModel()
            model.sira = sira
            sira = sira + 1
            model.id = item.ID
            model.musteriadi =item.MusteriAdi
            model.aciklama = item.Aciklama
            model.baslik = item.Baslik
            model.satisci_cloud = item.Satisci_Cloud
            model.satisci_cloud_dosya = item.Satisci_Cloud_Dosya
            model.hatirlatmaTarihi = item.Hatirlatma_Tarih
            model.hatirlatma_notu = item.Hatirlatma_Notu
            model.temsilci = item.KullaniciAdi
            model.tarih_giris = item.Tarih
            liste.append(model)

        schema = MusteriAyrintiSchema(many=True)

        return schema.dump(liste)

    def getTeklifAyrintiList(self,musteri_adi):
        result2 = self.data.getStoreList("""
                                            select


                                                yt.Aciklama as Aciklama


                                            from YeniTeklifTB yt,YeniTeklif_MusterilerTB ym
                                            where
                                            yt.MusteriId = ym.Id and

                                            ym.MusteriAdi=?
                                         
                                         
                                         """,(musteri_adi))
        
        liste = list()
        for item in result2:
            model = TeklifMusteriModel()
            model.aciklama = item.Aciklama
            liste.append(model)
        
        schema = TeklifMusteriSchema(many=True)
        return schema.dump(liste)
        
        
