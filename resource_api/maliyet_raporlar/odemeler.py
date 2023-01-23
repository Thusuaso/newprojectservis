from helpers import SqlConnect,TarihIslemler
from models.ozel_maliyet import OzelMaliyetListeModel
from resource_api.finans.guncel_kur import DovizListem

class Odemeler:

    def __init__(self):

        self.data = SqlConnect().data

        self.dtOdemeler = self.data.getList( # bu liste ödemeleri gösterir

            """
                  Select
            o.Tarih,
            o.SiparisNo, 
            o.Masraf,
			sum(o.Tutar) as tutar,
            o.Kur
            from
            OdemelerTB o,MusterilerTB m
            where m.ID=o.MusteriID and m.Marketing='Mekmar'
            and o.SiparisNo in (
                Select s.SiparisNo from SiparislerTB s
                where s.SiparisNo=o.SiparisNo
                and s.MusteriID=m.ID
                and s.SiparisDurumID=3  
				
                     
            )            
			group by o.Tarih , o.SiparisNo,  o.Masraf , o.Kur
            order by o.Tarih asc
         
           
            """
        )

        self.odeme_listesi = list()

        self.__odemeListesiOlustur()
        
    def __odemeListesiOlustur(self):

        tarihIslem = TarihIslemler()
        for item in self.dtOdemeler:

            model = OzelMaliyetListeModel()
            
            if item.Tarih != None:
                model.odeme_tarihi = tarihIslem.getDate(item.Tarih).strftime("%d-%m-%Y")
            model.siparis_no = item.SiparisNo 

            if item.Masraf != None:
                model.banka_masrafi = item.Masraf
            if item.Kur != None :
                model.doviz_kur = item.Kur    
            if item.tutar != None:
                 model.odenen_toplam_tutar = item.tutar
                 

                 self.odeme_listesi.append(model)

    def getOdemeBankaMasrafi(self,siparisno):

        masraf = 0
        
        for item in self.odeme_listesi:            

            if siparisno == item.siparis_no:
                masraf += item.banka_masrafi

        return masraf

    def getOdemeBankaTRY(self,siparisno):

        odeme = 0
        usd_odeme = 0
        
        for item in self.odeme_listesi:            
           
            if siparisno == item.siparis_no:
              
                odeme += item.doviz_kur * item.odenen_toplam_tutar
                usd_odeme += item.odenen_toplam_tutar

        return odeme,usd_odeme

    def getOdemeTarih(self,siparisno):

        tarih = ''

        for item in self.odeme_listesi:

            if siparisno == item.siparis_no:
                tarih = item.odeme_tarihi # bu tarihte en son gelen paranın tarihi gösterir

        return tarih
                 
    def getOdenenToplamMasrafi(self,siparisno):

        toplam_odeme = 0
        
        for item in self.odeme_listesi:            

            if siparisno == item.siparis_no:
                toplam_odeme += item.odenen_toplam_tutar

        return toplam_odeme      

    def getOdenenKur(self,siparisno,odenen,year,month,day):
        doviz_kur = 0
       
        if odenen > 0:
             
            for item in self.odeme_listesi:            
            
                if siparisno == item.siparis_no:
                    doviz_kur = item.doviz_kur
            
                        

        
            return (doviz_kur)
        else:
            doviz = DovizListem()
            dovizKur = doviz.getDovizKurListe(str(year),str(month),str(day))
            return dovizKur


