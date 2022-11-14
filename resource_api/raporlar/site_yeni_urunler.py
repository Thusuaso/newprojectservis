from models.raporlar import SiteYeniUrunlerModel,SiteYeniUrunlerSchema,YeniSiparisSchema,YeniSiparisModel
from helpers import SqlConnect


class SiteYeniUrunler:

    def __init__(self):
        self.data = SqlConnect().data

    def __getEvrakYukleKontrol(self,siparisNo):

        result_1 = self.data.getStoreList(
            """
            select SiparisNo from SiparisFaturaKayitTB where YuklemeEvrakID=2 and SiparisNo=?
            """,(siparisNo)
           )
       
        var = len(result_1)-1 
        return  var
    def getYeniUrunList(self):

        liste = list()

        result = self.data.getList(
            """
            select
            p.urunid,
            p.urunadi_en,
            (
            Select kategoriadi_en from MekmarCom_Kategoriler k 
            where k.Id=p.kategori_id
            ) as kategoriadi,
            (
            select
            'https://mekmar-image.fra1.digitaloceanspaces.com/products/' + f.name + '.' + f.uzanti
            from
            MekmarCom_Fotolar f where f.urunid=p.urunid and f.sira=1
            )  as foto_link
            from 
            MekmarCom_Products p
            where p.urunadi_fr='' and p.yayinla=1
            order by Id desc

            """
        )

        for item in result:

            model = SiteYeniUrunlerModel()
            model.id = item.urunid 
            model.urunadi = item.urunadi_en
            model.foto = item.foto_link
            model.kategoriadi = item.kategoriadi

            liste.append(model)

        
        schema = SiteYeniUrunlerSchema(many=True)

        return schema.dump(liste)

    def getYeniSiparisList(self):    ##hepsi

        liste = list()

        result = self.data.getList(
            """
            select 
            sum(u.SatisToplam) as fob,
            s.SiparisNo,
            s.NavlunSatis,
            s.DetayTutar_1,
            s.DetayTutar_2,
            s.DetayTutar_3
         
            from
            SiparislerTB s , SiparisUrunTB u 
            where s.SiparisNo = u.SiparisNo
            and Year(s.SiparisTarihi)=Year(GetDate())
            and Month(s.SiparisTarihi)= MONTH(GetDate())
            AND s.SiparisDurumID!=1
            group by s.SiparisNo,s.NavlunSatis,
            s.DetayTutar_1,
            s.DetayTutar_2,
            s.DetayTutar_3
          

            """
        )
       
      
        ID = 0
        Toplam = 0
        navlun = 0
        detay1 = 0 
        detay2 = 0 
        detay3 = 0
      
        for item in result:
  
            model = YeniSiparisModel()
            ID += 1
            model.id = ID
            model.order = item.SiparisNo
            model.fob = item.fob
            model.ddp = item.NavlunSatis +  item.DetayTutar_1 +   item.DetayTutar_2 +   item.DetayTutar_3 
            Toplam = item.fob + model.ddp
            model.toplam = Toplam
            model.link =  f"https://file-service.mekmar.com/file/download/2/{item.SiparisNo}"
            model.durum = self.__getEvrakYukleKontrol(item.SiparisNo)
           
            liste.append(model)

        
        schema = YeniSiparisSchema(many=True)
      
        return schema.dump(liste)  

    def getYeniSiparisMekmarList(self):   

        liste = list()

        result = self.data.getList(
            """
            select 
            sum(u.SatisToplam) as fob,
            s.SiparisNo,
            s.NavlunSatis,
            s.DetayTutar_1,
            s.DetayTutar_2,
            s.DetayTutar_3
            
            from
            SiparislerTB s , SiparisUrunTB u , MusterilerTB m 
            where s.SiparisNo = u.SiparisNo
            and Year(s.SiparisTarihi)=Year(GetDate())
            and Month(s.SiparisTarihi)= MONTH(GetDate())
            and  m.ID=s.MusteriID
			and m.Marketing='Mekmar'
            AND s.SiparisDurumID!=1
            group by s.SiparisNo,s.NavlunSatis,
            s.DetayTutar_1,
            s.DetayTutar_2,
            s.DetayTutar_3
          

            """
        )
       
      
        ID = 0
        Toplam = 0
        navlun = 0
        detay1 = 0 
        detay2 = 0 
        detay3 = 0
      
        for item in result:
  
            model = YeniSiparisModel()
            ID += 1
            model.id = ID
            model.order = item.SiparisNo
            model.fob = item.fob
            model.ddp = item.NavlunSatis +  item.DetayTutar_1 +   item.DetayTutar_2 +   item.DetayTutar_3 
            Toplam = item.fob + model.ddp
            model.toplam = Toplam
            model.link =  f"https://file-service.mekmar.com/file/download/2/{item.SiparisNo}"
            model.durum = self.__getEvrakYukleKontrol(item.SiparisNo)
            
            liste.append(model)

        
        schema = YeniSiparisSchema(many=True)
        
        return schema.dump(liste)              
