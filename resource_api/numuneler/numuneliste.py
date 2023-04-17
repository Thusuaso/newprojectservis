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
					n.Euro_Alis as EuroAlis,
					n.Euro_Satis as EuroSatis,
					n.KuryeAlis as UsdAlis,
					n.KuryeSatis as UsdSatis,
					n.TL_Alis as TlAlis,
					n.TL_Satis as TlSatis,
                    (select lower(i.KullaniciAdi)from KullaniciTB i where i.ID=n.NumuneTemsilci) as temsilci,
                    (select i.Image from KullaniciTB i where i.ID=n.NumuneTemsilci) as imageTag,
                    (select kt.Urun from NumuneKategoriTB kt where kt.ID=n.KategoriID) as kategori,
                    (select b.BirimAdi from UrunBirimTB b where b.ID=n.UrunBirimi) as birim,
					n.YuklemeTarihi,
					(select ngt.GonderiAdi from NumuneGonderiTipi ngt where ngt.ID = n.GonderiTipi) as GonderiTipi,
					(select nbc.BankaAdi from NumuneBankaSecim nbc where nbc.ID = n.BankaSecim) as BankaSecimi,
                    (select nod.Tutar from NumuneOdemelerTB nod where nod.NumuneNo = n.NumuneNo) as GelenBedel
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
            model.usdAlis = self.__getFloatControl(item.UsdAlis)
            model.usdSatis = self.__getFloatControl(item.UsdSatis)
            model.euroAlis = self.__getFloatControl(item.EuroAlis)
            model.euroSatis = self.__getFloatControl(item.EuroSatis)
            model.tlAlis = self.__getFloatControl(item.TlAlis)
            model.tlSatis = self.__getFloatControl(item.TlSatis)
           
            model.kategori = item.kategori 
           
            model.miktar = item.Miktar
            model.birim = item.birim
            model.banka_secimi = item.BankaSecimi
            model.gonderi_tipi = item.GonderiTipi
            model.aciklama = item.Aciklama
            model.gelenBedel = self.__getFloatControl(item.GelenBedel)
            if item.temsilci == 'ozlem':
                model.link = 'https://mekmar-image.fra1.digitaloceanspaces.com/personel/avatar5.png'
            elif item.temsilci == 'semih':
                model.link = 'https://mekmar-image.fra1.digitaloceanspaces.com/personel/avatar1.png'
            elif item.temsilci == 'hakan':
                model.link = 'https://mekmar-image.fra1.digitaloceanspaces.com/personel/avatar3.png'
            elif item.temsilci == 'gizem':
                model.link = 'https://mekmar-image.fra1.digitaloceanspaces.com/personel/avatar6.png'
            else:
                model.link = 'https://cdn.mekmarimage.com/personel/250x250/' + item.imageTag
                

            liste.append(model)

        schema = NumuneListeSchema(many=True)
     
        return schema.dump(liste)

    def __getFloatControl(self,value):
        if(value == None):
            return 0
        else:
            return value
   