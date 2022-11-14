from helpers import SqlConnect,TarihIslemler
from models.yeniTeklifler import EskiTekliflerModel,EskiTekliflerSchema


class EskiTeklifler:

    def __init__(self):
        self.data = SqlConnect().data
    
    def getEskiTeklifListesi(self):

        tarihIslem = TarihIslemler()

        result = self.data.getList(
            """
                select
                    tu.Id,
                    t.Tarih,
                    t.TeklifNo,
                    k.KullaniciAdi,
                    t.MusteriUlke,
                    t.MusteriAdi,
                    (Select ta.TeklifDurum from TeklifAsamalarTB ta where ta.ID=t.TeklifAsamaID) as teklifdurum,
                    (select kb.KullaniciAdi from KullaniciTB kb where kb.ID=t.FiyatGirisKullaniciID ) as fiyatveren,
                    tu.KategoriAdi,
                    tu.UrunAdi,
                    tu.UrunIslem,
                    tu.Ebat,
                    tu.YeniFiyat
                from
                    TekliflerTB t,KullaniciTB k,TeklifUrunlerTB tu
                where
                    t.KullaniciID=k.ID and tu.TeklifID=k.ID
            """
        )

        liste = list()

        for item in result:

            model = EskiTekliflerModel()
            model.id = item.Id
            model.tarih = tarihIslem.getDate(item.Tarih).strftime("%d-%m-%Y")
            model.teklifno = item.TeklifNo 
            model.kullaniciadi = item.KullaniciAdi 
            model.ulkeadi = item.MusteriUlke
            model.musteriadi = item.MusteriAdi 
            model.teklifdurum = item.teklifdurum
            model.fiyatveren = item.fiyatveren 
            model.kategoriadi = item.KategoriAdi 
            model.urunadi = item.UrunAdi
            model.islemadi = item.UrunIslem
            model.ebat = item.Ebat 
            model.fiyat = item.YeniFiyat 

            liste.append(model)

        schema = EskiTekliflerSchema(many=True)

        return schema.dump(liste)