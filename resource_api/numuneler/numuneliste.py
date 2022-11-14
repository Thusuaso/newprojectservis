from models.numuneler import *
from helpers import SqlConnect,TarihIslemler

class NumuneListe:
    def __init__(self):
        self.data = SqlConnect().data

       

    def getNumuneList(self,yil):

        result = self.data.getStoreList(
            """
              select
                    n.NumuneNo,
                    n.Miktar,
                
                    n.NumuneTarihi,
                    m.MusteriAdi,
                    n.Aciklama,
                    (select lower(i.KullaniciAdi)from KullaniciTB i where i.ID=n.NumuneTemsilci) as temsilci,
                    (select i.Image from KullaniciTB i where i.ID=n.NumuneTemsilci) as imageTag,
                    
                    (select kt.Urun from NumuneKategoriTB kt where kt.ID=n.KategoriID) as kategori,
                    

                    (select b.BirimAdi from UrunBirimTB b where b.ID=n.UrunBirimi) as birim
                from  NumunelerTB n , YeniTeklif_MusterilerTB m
                 where n.MusteriID=m.Id and year( n.NumuneTarihi) = ?
                
              order by n.NumuneTarihi DESC
            """,(yil)
        )

        liste = list()
        tarihIslem = TarihIslemler() 
        for item in result:

            model = NumuneListeModel()
            model.numuneNo = item.NumuneNo
            model.tarih = tarihIslem.getDate(item.NumuneTarihi).strftime("%d-%m-%Y")
            model.temsilci= item.temsilci
            model.musteriadi = item.MusteriAdi
           
           
            model.kategori = item.kategori 
           
            model.miktar = item.Miktar
            model.birim = item.birim
           
            model.aciklama = item.Aciklama
            if item.temsilci == 'ozlem':
                model.link = 'https://cdn.mekmarimage.com/personel/250x250/ozlem2.jpeg'
            elif item.temsilci == 'semih':
                pass
            else:
                model.link = 'https://cdn.mekmarimage.com/personel/250x250/' + item.imageTag
                

            liste.append(model)

        schema = NumuneListeSchema(many=True)
     
        return schema.dump(liste)

   
   