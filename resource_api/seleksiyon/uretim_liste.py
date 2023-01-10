from models.seleksiyon import UretimListeModel,UretimListeSchema
from helpers import SqlConnect,TarihIslemler



class UretimListe:
    def __init__(self):
        self.data = SqlConnect().data

        self.urunbirimlist = self.data.getList(
            """
            select * from UrunBirimTB
            """
        )

    def getUretimList(self):

        result = self.data.getList(
            """
            select  
            u.ID as Id,  
            u.KasaNo as kasano,  
            u.Tarih as tarih,  
            (select k.KategoriAdi from KategoriTB k where k.ID=uk.KategoriID) as kategori,  
            (select o.OcakAdi from UrunOcakTB o where o.ID=u.UrunOcakID) as ocak,  
            (select t.FirmaAdi from TedarikciTB t where t.ID=u.TedarikciID) as tedarikci,  
            dbo.Get_UrunAdi(uk.ID) as urunadi,  
            dbo.Get_KenarIslem(uk.ID) as kenarislem,  
            dbo.Get_Olcu_Boy(uk.ID) as boy,  
            dbo.Get_Olcu_En(uk.ID) as en,  
            dbo.Get_Olcu_Kenar(uk.ID) as kenar,  
            u.KutuAdet as kutuadet,  
            dbo.GetUretim_Miktar(u.Miktar,u.OzelMiktar) as miktar,  
            u.Miktar,  
            u.Adet as kasa_adet,  
            u.SiparisAciklama as siparisaciklama,  
            u.TedarikciID as tedarikci_id,  
            u.UrunBirimID as birim_id,  
            u.Aciklama,  
            u.UrunKartID,  
            u.Disarda,
            u.Kutu,
			u.Bagli,
            u.Bulunamadi
            from  
            UretimTB u,UrunKartTB uk  
            where  
            u.UrunDurumID=1 and uk.ID=u.UrunKartID  
            and u.TedarikciID is not null and u.Bulunamadi != 1
            order by u.KasaNo desc  
            """
          
        )

        liste = list()
        tarihIslem = TarihIslemler() 
        for item in result:

            model = UretimListeModel()
            model.id = item.Id 
            model.kasa_no = item.kasano
            model.tarih = tarihIslem.getDate(item.tarih).strftime("%d-%m-%Y")
            model.kategori = item.kategori 
            model.ocak = item.ocak 
            model.tedarikci = item.tedarikci 
            model.urunadi = item.urunadi 
            model.kenarislem = item.kenarislem 
            model.boy = item.boy
            model.en = item.en 
            model.kenar = item.kenar 
            model.kutuadet = item.kutuadet 
            model.m2 = float(item.miktar)
            model.miktar = item.Miktar
            model.siparisaciklama = item.siparisaciklama 
            model.tedarikci_id = item.tedarikci_id 
            model.birim_id = item.birim_id
            model.aciklama = item.Aciklama
            model.kasaadet = item.kasa_adet
            model.urunkartid = item.UrunKartID
            model.disarda = item.Disarda
            model.kutu = item.Kutu
            model.bulunamayan = item.Bulunamadi
            if item.Kutu == True:
                model.kutu = 1
            else:  
                model.kutu = 0
                
            if item.Bagli == True:
                model.bagli = 1
            else:  
                model.bagli = 0
            
            if model.birim_id == 2:
                model.adet = float(item.Miktar)
            if model.birim_id == 3:
                model.mt = float(item.Miktar)
            if model.birim_id == 4:
                model.ton = float(item.Miktar)
            if model.birim_id == 5:
                model.sqft = float(item.Miktar)
            


            liste.append(model)

        schema = UretimListeSchema(many=True)
       
        return schema.dump(liste)

    def getUretim(self,kasano):

        item = self.data.getStoreList(
            """
            select
            u.ID as Id,
            u.KasaNo as kasano,
            u.Tarih as tarih,
            (select k.KategoriAdi from KategoriTB k where k.ID=uk.KategoriID) as kategori,
            (select o.OcakAdi from UrunOcakTB o where o.ID=u.UrunOcakID) as ocak,
            (select t.FirmaAdi from TedarikciTB t where t.ID=u.TedarikciID) as tedarikci,
            dbo.Get_UrunAdi(uk.ID) as urunadi,
            dbo.Get_KenarIslem(uk.ID) as kenarislem,
            dbo.Get_Olcu_Boy(uk.ID) as boy,
            dbo.Get_Olcu_En(uk.ID) as en,
            dbo.Get_Olcu_Kenar(uk.ID) as kenar,
            u.KutuAdet as kutuadet,
            dbo.GetUretim_Miktar(u.Miktar,u.OzelMiktar) as miktar,
            u.Miktar,
            u.Adet as kasa_adet,
            u.SiparisAciklama as siparisaciklama,
            u.TedarikciID as tedarikci_id,
            u.UrunBirimID as birim_id,
            u.Aciklama,
            u.UrunKartID ,
            u.Disarda,
            u.Bulunamadi,
            u.Kutu
            from
            UretimTB u,UrunKartTB uk
            where
            u.UrunDurumID=1 and uk.ID=u.UrunKartID
            and u.TedarikciID is not null and u.KasaNo=?
            order by u.KasaNo desc
            """,(kasano)
        )[0]

        tarihIslem = TarihIslemler()  

        model = UretimListeModel()
        model.id = item.Id 
        model.kasa_no = item.kasano
        model.tarih = tarihIslem.getDate(item.tarih).strftime("%d-%m-%Y")
        model.kategori = item.kategori 
        model.ocak = item.ocak 
        model.tedarikci = item.tedarikci 
        model.urunadi = item.urunadi 
        model.kenarislem = item.kenarislem 
        model.boy = item.boy
        model.en = item.en 
        model.kenar = item.kenar 
        model.kutuadet = item.kutuadet 
        model.m2 = float(item.miktar)
        model.siparisaciklama = item.siparisaciklama 
        model.tedarikci_id = item.tedarikci_id 
        model.birim_id = item.birim_id
        model.aciklama = item.Aciklama
        model.urunkartid = item.UrunKartID
        model.kasaadet = item.kasa_adet
        model.disarda = item.Disarda
        model.bulunamayan = item.Bulunamadi
        model.kutu = item.Kutu
        if model.birim_id == 2:
           model.adet = float(item.Miktar)
        if model.birim_id == 3:
           model.mt = float(item.Miktar)
        if model.birim_id == 4:
           model.ton = float(item.Miktar)
        if model.birim_id == 5:
           model.sqft = float(item.Miktar)

        schema = UretimListeSchema()
      
        return schema.dump(model)

    def getUretimKasaList(self,str_kasalar):

        result = self.data.getList(
            f"""
            select
            u.ID as Id,
            u.KasaNo as kasano,
            u.Tarih as tarih,
            (select k.KategoriAdi from KategoriTB k where k.ID=uk.KategoriID) as kategori,
            (select o.OcakAdi from UrunOcakTB o where o.ID=u.UrunOcakID) as ocak,
            (select t.FirmaAdi from TedarikciTB t where t.ID=u.TedarikciID) as tedarikci,
            dbo.Get_UrunAdi(uk.ID) as urunadi,
            dbo.Get_KenarIslem(uk.ID) as kenarislem,
            dbo.Get_Olcu_Boy(uk.ID) as boy,
            dbo.Get_Olcu_En(uk.ID) as en,
            dbo.Get_Olcu_Kenar(uk.ID) as kenar,
            u.KutuAdet as kutuadet,
            dbo.GetUretim_Miktar(u.Miktar,u.OzelMiktar) as miktar,
            u.Miktar,
            u.Adet as kasa_adet,
            u.SiparisAciklama as siparisaciklama,
            u.TedarikciID as tedarikci_id,
            u.UrunBirimID as birim_id,
            u.Aciklama,
            u.Disarda
            from
            UretimTB u,UrunKartTB uk
            where
            u.UrunDurumID=1 and uk.ID=u.UrunKartID
            and u.TedarikciID is not null and u.KasaNo in {str_kasalar}
            order by u.KasaNo desc
            """
        )

        liste = list()
        tarihIslem = TarihIslemler()
        for item in result:

            model = UretimListeModel()
            model.id = item.Id 
            model.kasa_no = item.kasano
            model.tarih = tarihIslem.getDate(item.tarih).strftime("%d-%m-%Y")
            model.kategori = item.kategori 
            model.ocak = item.ocak 
            model.tedarikci = item.tedarikci 
            model.urunadi = item.urunadi 
            model.kenarislem = item.kenarislem 
            model.boy = item.boy
            model.en = item.en 
            model.kenar = item.kenar 
            model.kutuadet = item.kutuadet 
            model.m2 = float(item.miktar)
            model.siparisaciklama = item.siparisaciklama 
            model.tedarikci_id = item.tedarikci_id 
            model.birim_id = item.birim_id
            model.aciklama = item.Aciklama
            model.kasaadet = item.kasa_adet
            model.disarda = item.Disarda
            if model.birim_id == 2:
                model.adet = float(item.Miktar)
            if model.birim_id == 3:
                model.mt = float(item.Miktar)
            if model.birim_id == 4:
                model.ton = float(item.Miktar)
            if model.birim_id == 5:
                model.sqft = float(item.Miktar)
            


            liste.append(model)

        schema = UretimListeSchema(many=True)
        
        return schema.dump(liste)

    
    def setCrateAll(self,data):
        try:
            po = data['po']
            products = data['products']
            product_id = data['product_id']
            for item in products:
                self.data.update_insert("""
                                            update UretimTB SET SiparisAciklama=?, Aciklama=?,UrunKartID=?,UretimTurID=2 where KasaNo=?
                                        
                                        """,(po,po,product_id,item['kasa_no']))
            return True
        except Exception as e:
            print('setCrateAll hata',str(e))
            return False
 