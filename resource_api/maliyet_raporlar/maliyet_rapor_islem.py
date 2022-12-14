from resource_api.maliyet_raporlar.siparisler import Siparisler,Siparisler_Yil
from resource_api.maliyet_raporlar.urunler import Urunler,Urunler_Yil
from resource_api.maliyet_raporlar.odemeler import Odemeler
from resource_api.maliyet_raporlar.masraflar import Masraflar,Masraflar_Yil
from models.ozel_maliyet import OzelMaliyetListeSchema,OzelMaliyetListeModel,TedarikciFaturaSchema,TedarikciFaturaModel
from helpers import SqlConnect

class MaliyetRaporIslem:

    def __init__(self,yil,ay):

        self.siparisler = Siparisler(yil,ay).siparis_listesi
        self.urunler = Urunler(yil,ay)
        self.odemeler = Odemeler()
        self.masraflar = Masraflar(yil,ay)
        data = SqlConnect().data
        self.dtTedarikci_group_result = data.getStoreList(
            """
            select
            u.TedarikciID,
            u.SiparisNo
            from
            SiparisUrunTB u
            where
            u.TedarikciID not in (1,123) and 
            u.SiparisNo in (
            Select s.SiparisNo from SiparislerTB s,MusterilerTB m
            where s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and m.Marketing='Mekmar'
            and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=?
            and Month(s.YuklemeTarihi)=?
            )
            group by u.TedarikciID,u.SiparisNo
            """,(yil,ay)
        )

        self.dtDisFaturaList = data.getList(

            """
                select 
           
            u.TedarikciID ,
            s.SiparisNo
            from SiparisUrunTedarikciFormTB u , SiparisFaturaKayitTB s
             where s.SiparisNo=u.SiparisNo and U.TedarikciID not in (1,123) AND YuklemeEvrakID=3  
              group by u.TedarikciID ,s.SiparisNo
           
            """

        )
        self.dtOzeliscilikFaturaList = data.getList(

            """
            select * from SiparisFaturaKayitTB where YuklemeEvrakID=40
            """

        )
        self.dtMekmarFaturaList = data.getList(

            """
            select 
            s.EvrakAdi ,
            u.TedarikciID ,
            s.SiparisNo
            from SiparisUrunTedarikciFormTB u , SiparisFaturaKayitTB s
             where s.SiparisNo=u.SiparisNo and YuklemeEvrakID=3 and u.TedarikciID=1  
              group by u.TedarikciID , s.EvrakAdi,s.SiparisNo
            """

        )

        self.dtMekmozFaturaList = data.getList(

            """
             select 
            s.EvrakAdi ,
            u.TedarikciID ,
            s.SiparisNo
            from SiparisUrunTedarikciFormTB u , SiparisFaturaKayitTB s
             where s.SiparisNo=u.SiparisNo and YuklemeEvrakID=3 and u.TedarikciID=123  
              group by u.TedarikciID , s.EvrakAdi,s.SiparisNo
            """

        )
        self.dtDovizKur = data.getList(
            """
           select k.Kur , s.SiparisNo from SiparisFaturaKayitTB s ,KonteynerDigerFaturalarKayitTB k where k.ID = s.FaturaKayitID
            """
        )
        self.dtTedarikciForm = data.getList(
            """
             select * from SiparisUrunTedarikciFormTB

            """
        )
        self.dtTedarikciFatura = data.getList(
            """
             select * from Tedarikci_Siparis_FaturaTB

            """
        )
        self.dtTedarikciTum = data.getList(
            """
         
             select TedarikciID ,SiparisNo from SiparisUrunTB where  TedarikciID not in (1,123) group by SiparisNo, TedarikciID

            """
        )
    def getMaliyetListesi(self):
        liste = list()
        for item in self.siparisler:
            urun_model = self.urunler.getUrunModel(item.siparis_no)
          
            item.toplam_bedel += urun_model.toplam_bedel
            item.mekmar_alim = urun_model.mekmar_alim
            item.mekmoz_alim = urun_model.mekmoz_alim
            item.dis_alim = urun_model.dis_alim
            item.banka_masrafi = self.odemeler.getOdemeBankaMasrafi(item.siparis_no)
            item.odeme_tarihi = self.odemeler.getOdemeTarih(item.siparis_no) 
            item.odenen_try_tutar , item.odenen_usd_tutar =  self.odemeler.getOdemeBankaTRY(item.siparis_no)
            if item.odenen_try_tutar != 0 and item.odenen_usd_tutar != 0 : 
              item.ortalama_kur =  item.odenen_try_tutar / item.odenen_usd_tutar
            item.odenen_toplam_tutar = self.odemeler.getOdenenToplamMasrafi(item.siparis_no)   
            item.ozel_iscilik_evrak = list() #urun_model.ozel_iscilik_evrak      
            item.mekmar_alim_evrak = list() #urun_model.mekmar_alim_evrak
            item.mekmoz_alim_evrak = list() #urun_model.mekmoz_alim_evrak
            item.dis_alim_evrak = list() #urun_model.dis_alim_evrak
            item.dis_alim_tedarikci = list()
            item.tedarikci_sayisi_evrak = list()
            if item.toplam_bedel <= item.odenen_toplam_tutar : # e??er toplam gelen para sipari?? bedelini e??it veya gelen para dah butukse bu dosya kapanm??st??r deriz
                item.dosya_kapanma_date = item.odeme_tarihi # ??deme_tarihi son gelen paran??n tarihiydi . e??er yukardaki ko??ulu sa??larsa bu sipari?? en son su tar??hte ??demeyi yapt?? ve borcu bitti deriz son tarih ise bizim kapanma tar??h??m??z olur .
            else :
                 item.dosya_kapanma_date =  '-'    #eger hala alacakl??ysak 21ACC01-2 de oldugu gibi dosyas?? kapanmam??st??r ve tar??h?? - ile g??ster deriz .
            
            """
            if item.siparis_no =='21AAC02-2' : #birde bu negatif mevzusu var toplamlarda m?? sorun var
                 item.dosya_kapanma_date =  '11-11-2021'
            """
            fatura_sayisi = 0
            

            for fat in self.dtTedarikci_group_result:
                if fat.SiparisNo == item.siparis_no:
                    fatura_sayisi += 1

            for ted_fatura in self.dtDisFaturaList:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/3/{item.siparis_no}"
                   
                    item.dis_alim_evrak.append(model)

            for ted_fatura in self.dtTedarikciFatura:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/40/{item.siparis_no}"
                   
                    item.dis_alim_tedarikci.append(model)    
            
            for ted_fatura in self.dtTedarikciTum:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/40/{item.siparis_no}"
                   
                    item.tedarikci_sayisi_evrak.append(model)            

            for ted_fatura in self.dtMekmarFaturaList:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/3/{item.siparis_no}"
                   
                    item.mekmar_alim_evrak.append(model)

            for ted_fatura in self.dtOzeliscilikFaturaList:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                    model.id = ted_fatura.ID
                    model.link = f"https://file-service.mekmar.com/file/download/40/{item.siparis_no}"
                    model.evrak_adi = ted_fatura.SiparisNo
                    item.ozel_iscilik_evrak.append(model) 

                     
            
            for ted_fatura in self.dtMekmozFaturaList:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/3/{item.siparis_no}"
                    
                    item.mekmoz_alim_evrak.append(model)

            item.mekmar_alim_evrak_sayisi = len(item.mekmar_alim_evrak)
            item.mekmoz_alim_evrak_sayisi = len(item.mekmoz_alim_evrak)
            item.dis_alim_evrak_sayisi = len(item.dis_alim_evrak)
            item.dis_alim_tedarikci_sayisi = len(item.dis_alim_tedarikci)
            item.tedarikci_sayisi  = len(item.tedarikci_sayisi_evrak)
            item.ozel_iscilik_sayisi = len(item.ozel_iscilik_evrak)

            item.dis_alim_fatura_sayisi = fatura_sayisi

            masraf_model = self.masraflar.getMasrafModel(item.siparis_no)

      

            item.gumruk = masraf_model.gumruk
            item.liman = masraf_model.liman
            item.doviz_kur = self.odemeler.getOdenenKur(item.siparis_no) 
            item.nakliye = masraf_model.nakliye
            item.ilaclama = masraf_model.ilaclama
            item.lashing = masraf_model.lashing
            item.booking = masraf_model.booking
            item.spazlet = masraf_model.spazlet
            
            
            item.navlun_evrak = masraf_model.navlun_evrak
            item.gumruk_evrak = masraf_model.gumruk_evrak
            item.nakliye_evrak = masraf_model.nakliye_evrak
            item.ilaclama_evrak = masraf_model.ilaclama_evrak
            item.liman_evrak = masraf_model.liman_evrak
            item.lashing_evrak = masraf_model.lashing_evrak
            item.booking_evrak = masraf_model.booking_evrak
            item.spazlet_evrak = masraf_model.spazlet_evrak
            
            
            item.satis_faturasi = masraf_model.satis_faturasi
            item.masraf_toplam += (
                item.mekmar_alim + item.mekmoz_alim + item.dis_alim + item.nakliye + item.gumruk + item.lashing + item.booking + item.spazlet + 
                item.ilaclama + item.liman + item.navlun + item.pazarlama + item.banka_masrafi 
                 + item.diger_masraflar+item.ozel_iscilik+item.kurye_masrafi + item.sigorta
            )

            if(item.dosya_kapanma_date == '-'):
                item.kar_zarar = 0
            else:
                item.kar_zarar = item.toplam_bedel - item.masraf_toplam
                if item.toplam_bedel != 0 and item.kar_zarar != 0:
                    
                    item.kar_zarar_tl_yuzdesi = round(((item.kar_zarar / item.toplam_bedel ) * 100),2)
                else:
                    item.kar_zarar_tl_yuzdesi = 0 
                
            if item.dosya_kapanma_date == '-':
                item.kar_zarar_tl = 0
                item.kar_zarar_tl_yuzdesi = 0
            else:
                
                if item.doviz_kur !=0 and item.doviz_kur != None:
                    item.kar_zarar_tl =  item.kar_zarar * item.doviz_kur

            if len(item.navlun_evrak) > 0 and item.navlun_satis <= 0:
                item.navlun_kontrol = False


          
            liste.append(item)


        schema = OzelMaliyetListeSchema(many=True)

        return schema.dump(liste)
 

class MaliyetRaporIslem_Yil: # hepsi butonna bas??ld??g??nda bu alan ??al??????r . 

    def __init__(self,yil):

        self.siparisler = Siparisler_Yil(yil).siparis_listesi
        self.urunler = Urunler_Yil(yil)
        self.odemeler = Odemeler()
        self.masraflar = Masraflar_Yil(yil)
        
      
    
     
        data = SqlConnect().data
        self.dtTedarikci_group_result = data.getStoreList(
            """
            select
            u.TedarikciID,
            u.SiparisNo
            from
            SiparisUrunTB u
            where
            u.TedarikciID not in (1,123) and 
            u.SiparisNo in (
            Select s.SiparisNo from SiparislerTB s,MusterilerTB m
            where s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and m.Marketing='Mekmar'
            and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=?
          
            )
            group by u.TedarikciID,u.SiparisNo
            """,(yil)
        )

        self.dtDisFaturaList = data.getList(

            """
                select 
           
            u.TedarikciID ,
            s.SiparisNo
            from SiparisUrunTedarikciFormTB u , SiparisFaturaKayitTB s
             where s.SiparisNo=u.SiparisNo and U.TedarikciID not in (1,123) AND YuklemeEvrakID=3  
              group by u.TedarikciID ,s.SiparisNo
           
            """

        )
        self.dtOzeliscilikFaturaList = data.getList(

            """
            select * from SiparisFaturaKayitTB where YuklemeEvrakID=40
            """

        )
        self.dtMekmarFaturaList = data.getList(

            """
            select 
            s.EvrakAdi ,
            u.TedarikciID ,
            s.SiparisNo
            from SiparisUrunTedarikciFormTB u , SiparisFaturaKayitTB s
             where s.SiparisNo=u.SiparisNo and YuklemeEvrakID=3 and u.TedarikciID=1  
              group by u.TedarikciID , s.EvrakAdi,s.SiparisNo
            """

        )

        self.dtMekmozFaturaList = data.getList(

            """
             select 
            s.EvrakAdi ,
            u.TedarikciID ,
            s.SiparisNo
            from SiparisUrunTedarikciFormTB u , SiparisFaturaKayitTB s
             where s.SiparisNo=u.SiparisNo and YuklemeEvrakID=3 and u.TedarikciID=123  
              group by u.TedarikciID , s.EvrakAdi,s.SiparisNo
            """

        )
        self.dtDovizKur = data.getList(
            """
           select k.Kur , s.SiparisNo from SiparisFaturaKayitTB s ,KonteynerDigerFaturalarKayitTB k where k.ID = s.FaturaKayitID
            """
        )
        self.dtTedarikciForm = data.getList(
            """
             select * from SiparisUrunTedarikciFormTB

            """
        )
        self.dtTedarikciFatura = data.getList(
            """
             select * from Tedarikci_Siparis_FaturaTB

            """
        )
        self.dtTedarikciTum = data.getList(
            """
         
             select TedarikciID ,SiparisNo from SiparisUrunTB where  TedarikciID not in (1,123) group by SiparisNo, TedarikciID

            """
        )
    def getMaliyetListesi(self):

        liste = list()

        for item in self.siparisler:
         
            urun_model = self.urunler.getUrunModel(item.siparis_no)
          
            item.toplam_bedel += urun_model.toplam_bedel
            item.mekmar_alim = urun_model.mekmar_alim
            item.mekmoz_alim = urun_model.mekmoz_alim
            item.dis_alim = urun_model.dis_alim
            item.banka_masrafi = self.odemeler.getOdemeBankaMasrafi(item.siparis_no)
            item.odeme_tarihi = self.odemeler.getOdemeTarih(item.siparis_no)
            item.odenen_try_tutar , item.odenen_usd_tutar =  self.odemeler.getOdemeBankaTRY(item.siparis_no)
            if item.odenen_try_tutar != 0 and item.odenen_usd_tutar != 0 : 
              item.ortalama_kur =  item.odenen_try_tutar / item.odenen_usd_tutar
            item.odenen_toplam_tutar = self.odemeler.getOdenenToplamMasrafi(item.siparis_no)   
            item.ozel_iscilik_evrak = list() #urun_model.ozel_iscilik_evrak      
            item.mekmar_alim_evrak = list() #urun_model.mekmar_alim_evrak
            item.mekmoz_alim_evrak = list() #urun_model.mekmoz_alim_evrak
            item.dis_alim_evrak = list() #urun_model.dis_alim_evrak
            item.dis_alim_tedarikci = list()
            item.tedarikci_sayisi_evrak = list()
            if item.toplam_bedel <= item.odenen_toplam_tutar :
                item.dosya_kapanma_date = item.odeme_tarihi
            else :
                 item.dosya_kapanma_date =  '-'   
            fatura_sayisi = 0


            for fat in self.dtTedarikci_group_result:
                if fat.SiparisNo == item.siparis_no:
                    fatura_sayisi += 1

            for ted_fatura in self.dtDisFaturaList:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/3/{item.siparis_no}"
                   
                    item.dis_alim_evrak.append(model)

            for ted_fatura in self.dtTedarikciFatura:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/40/{item.siparis_no}"
                   
                    item.dis_alim_tedarikci.append(model)    
            
            for ted_fatura in self.dtTedarikciTum:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/40/{item.siparis_no}"
                   
                    item.tedarikci_sayisi_evrak.append(model)            

            for ted_fatura in self.dtMekmarFaturaList:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/3/{item.siparis_no}"
                   
                    item.mekmar_alim_evrak.append(model)

            for ted_fatura in self.dtOzeliscilikFaturaList:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                    model.id = ted_fatura.ID
                    model.link = f"https://file-service.mekmar.com/file/download/40/{item.siparis_no}"
                    model.evrak_adi = ted_fatura.SiparisNo
                    item.ozel_iscilik_evrak.append(model) 

                     
            
            for ted_fatura in self.dtMekmozFaturaList:
                if ted_fatura.SiparisNo == item.siparis_no:
                    model = TedarikciFaturaModel()
                    model = TedarikciFaturaModel()
                   
                    model.link =  f"https://file-service.mekmar.com/file/download/3/{item.siparis_no}"
                    
                    item.mekmoz_alim_evrak.append(model)

            item.mekmar_alim_evrak_sayisi = len(item.mekmar_alim_evrak)
            item.mekmoz_alim_evrak_sayisi = len(item.mekmoz_alim_evrak)
            item.dis_alim_evrak_sayisi = len(item.dis_alim_evrak)
            item.dis_alim_tedarikci_sayisi = len(item.dis_alim_tedarikci)
            item.tedarikci_sayisi  = len(item.tedarikci_sayisi_evrak)
            item.ozel_iscilik_sayisi = len(item.ozel_iscilik_evrak)

            item.dis_alim_fatura_sayisi = fatura_sayisi

            masraf_model = self.masraflar.getMasrafModel(item.siparis_no)



            item.gumruk = masraf_model.gumruk
            item.liman = masraf_model.liman
            item.lashing = masraf_model.lashing
            item.booking = masraf_model.booking
            item.spazlet = masraf_model.spazlet
            
            
            
            item.doviz_kur = self.odemeler.getOdenenKur(item.siparis_no) 
            item.nakliye = masraf_model.nakliye
            item.ilaclama = masraf_model.ilaclama
            item.navlun_evrak = masraf_model.navlun_evrak
            item.gumruk_evrak = masraf_model.gumruk_evrak
            item.nakliye_evrak = masraf_model.nakliye_evrak
            item.ilaclama_evrak = masraf_model.ilaclama_evrak
            item.liman_evrak = masraf_model.liman_evrak
            item.lashing_evrak = masraf_model.lashing_evrak
            item.booking_evrak = masraf_model.booking_evrak
            item.spazlet_evrak = masraf_model.spazlet_evrak
            
            
            
            item.satis_faturasi = masraf_model.satis_faturasi
            item.masraf_toplam += (
                item.mekmar_alim + item.mekmoz_alim + item.dis_alim + item.nakliye + item.gumruk + item.lashing + 
                item.booking +item.spazlet +
                item.ilaclama + item.liman + item.navlun + item.pazarlama + item.banka_masrafi 
                 + item.diger_masraflar+item.ozel_iscilik+item.kurye_masrafi
            )
            
            if(item.dosya_kapanma_date == '-'):
                item.kar_zarar = 0
            else:
                item.kar_zarar = item.toplam_bedel - item.masraf_toplam
                if item.toplam_bedel !=0 and item.kar_zarar != 0:
                    
                    item.kar_zarar_tl_yuzdesi = round(((item.kar_zarar / item.toplam_bedel ) * 100),2)
                else:
                    item.kar_zarar_tl_yuzdesi = 0
            
 
            if(item.dosya_kapanma_date == '-'):
                item.kar_zarar_tl = 0
            else:
                
                if item.doviz_kur !=0 and item.doviz_kur != None:
                    item.kar_zarar_tl =  item.kar_zarar * item.doviz_kur

            if len(item.navlun_evrak) > 0 and item.navlun_satis <= 0:
                item.navlun_kontrol = False
            
            
            


          
            liste.append(item)

        
        schema = OzelMaliyetListeSchema(many=True)

        return schema.dump(liste)







