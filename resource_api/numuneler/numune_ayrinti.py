from helpers import SqlConnect,TarihIslemler
from models.numuneler import *

class NumuneAyrinti:

    def __init__(self,po):

        self.data = SqlConnect().data
        self.numune_no = po
       

    def getNumuneAyrintiList(self):
        
         result = self.data.getStoreList(
            """
              select

                *,
                (select m.MusteriAdi from YeniTeklif_MusterilerTB m where n.MusteriID=m.Id ) as  MusteriAdi,
                (select k.Urun from NumuneKategoriTB k where k.ID=n.KategoriID) as KategoriAdi,
                (select u.BirimAdi from UrunBirimTB u where u.ID= n.UrunBirimi) as BirimAdi,
                (select g.GonderiAdi from NumuneGonderiTipi g where g.ID=n.GonderiTipi) as GonnderiAdi,
                (select b.BankaAdi from NumuneBankaSecim b where b.ID=N.BankaSecim) as BankaAdi
                from NumunelerTB n 
                where n.NumuneNo=? 
            """,(self.numune_no)
         )
         
         liste = list()
         tarihIslem = TarihIslemler() 
         for item in result:

            model = NumuneModel()
            model.numuneNo = item.NumuneNo
            model.tarih = tarihIslem.getDate(item.NumuneTarihi).strftime("%d-%m-%Y")
          
            model.temsilci = item.NumuneTemsilci
            
            model.musteriadi = item.MusteriAdi
            model.musteriId = item.MusteriID
            model.kategoriAdi = item.KategoriAdi 
            model.kategoriId = item.KategoriID
            model.gonderiId = item.GonderiTipi
            model.bankaId = item.BankaSecim
            model.kuryeAlis = item.KuryeAlis
            model.kuryeSatis = item.KuryeSatis
            model.TL_Alis = item.TL_Alis
            model.TL_Satis = item.TL_Satis  

            model.Euro_Alis = item.Euro_Alis
            model.Euro_Satis = item.Euro_Satis 
            
            model.urunBirim = item.BirimAdi
            model.Miktar = item.Miktar
            model.urunBirimId = item.UrunBirimi
            if item.BirimAdi != None:
                if item.BirimAdi == 'M2' :
                    
                    model.m2 = item.Miktar
                if item.BirimAdi == 'Adet' :
                    model.adet = item.Miktar 
                if item.BirimAdi == 'Mt' :
                    model.mt = item.Miktar  
                if item.BirimAdi == 'Ton' :
                    model.ton = item.Miktar              

           


            liste.append(model)
        
         schema = NumuneSchema(many=True)
        
         return schema.dump(liste)
          
