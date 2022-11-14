from helpers import SqlConnect,TarihIslemler
from models.yeniTeklifler import TumTekliflerSchema,TumTekliflerModel 
from resource_api.yeniTeklifler.teklifIslem import TeklifIslem

class TumTeklifler:

    def __init__(self):

        self.data = SqlConnect().data

    def getTumTeklifList(self):

        result = self.data.getList(
            """
            select
            uk.Id,
            t.Id as teklifid,
            t.Sira as TeklifNo,
            t.Tarih,
            k.KullaniciAdi,
            m.MusteriAdi,
            u.UlkeAdi,
            (select kt.KategoriAdi from YeniTeklif_KategorilerTB kt where kt.Id=uk.KategoriId) as kategoriadi,
            ( select yu.UrunAdi from YeniTeklif_UrunlerTB yu where yu.Id= uk.UrunId) as urunadi,
            (select ok.Kalinlik from YeniTeklif_Olcu_KalinlikTB ok where ok.id=uk.KalinlikId ) as kalinlik,
            (select e.EnBoy from YeniTeklif_Olcu_EnBoyTB e where e.id=uk.EnBoyId) as enboy,
            (Select y.IslemAdi from YeniTeklif_YuzeyIslemTB y where y.Id=uk.YuzeyIslemId) as islemadi,
            uk.FobFiyat,
            uk.TeklifFiyat,
            uk.Birim,
			YEAR(t.Tarih) Yil
            from
            YeniTeklifTB t,KullaniciTB k,YeniTeklif_MusterilerTB m,
            YeniTeklif_UlkeTB u,YeniTeklif_UrunKayitTB uk
            where
            t.KullaniciId = k.ID and m.Id = t.MusteriId 
            and u.Id=m.UlkeId and uk.TeklifId=t.Id
            order by t.Tarih desc
            """
        )

        liste = list()
        tarihIslem = TarihIslemler()

        for item in result:

            model = TumTekliflerModel()
            model.id = item.Id 
            model.teklifid = item.teklifid 
            model.teklifno = item.TeklifNo 
            model.tarih = tarihIslem.getDate(item.Tarih).strftime("%d-%m-%Y")
            model.kullaniciadi = item.KullaniciAdi 
            model.musteriadi = item.MusteriAdi 
            model.ulkeadi = item.UlkeAdi 
            model.kategoriadi = item.kategoriadi 
            model.urunadi = item.urunadi 
            model.kalinlik = item.kalinlik
            model.enboy = item.enboy 
            model.islemadi = item.islemadi 
            model.fobfiyat = item.FobFiyat
            model.tekliffiyat = item.TeklifFiyat 
            model.birim = item.Birim
            model.year = item.Yil

            liste.append(model)

        schema = TumTekliflerSchema(many=True)

        return schema.dump(liste)
    
    
    
    def setEnBoyOlcu(self,dat):
        try:
            self.data.update_insert("""
                                        insert into YeniTeklif_Olcu_EnBoyTB(EnBoy) VALUES(?)
                                    
                                    """,(dat['olcu']))
            islem = TeklifIslem()
            result = islem.getEnBoyList()
            
            return True,result
        except Exception as e:
            print('setEnBoyOlcu hata',str(e))
            return False