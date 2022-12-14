
from models.raporlar import yukleme
from models.siparisler_model import SiparisGirisSchema,SiparisGirisModel
from models.siparisler_model.siparisGirisUrun import SiparisGirisUrunModel
from models import SiparislerModel
from helpers import SqlConnect,TarihIslemler
from helpers import MailService,DegisiklikMain
import datetime
from resource_api.finans.caprazkur import DovizListem
from views.raporlar import AnaSayfaDegisiklik
from views.shared.degisiklikTahmin import DegisiklikTahmin
class SiparisGiris:
    
    def __init__(self):
        self.data = SqlConnect().data
        
        self.iscilikList = self.data.getList(
            """
            Select s.SiparisNo,s.UrunKartId,t.FirmaAdi,s.Tutar from
            SiparisEkstraGiderlerTB s,TedarikciTB t
            where s.TedarikciID=t.ID
            """
        )

    def getSiparisModel(self):
        model = SiparisGirisModel()
        schema = SiparisGirisSchema()

        return schema.dump(model)
        
    def getSiparis(self,siparisNo):
        model = SiparisGirisModel()

        model.siparis = self.__getSiparis(siparisNo)
        
        model.siparisUrunler = self.__getSiparisUrunler(siparisNo)
        model.proformaBilgileri = model.siparis

        schema = SiparisGirisSchema()

        return schema.dump(model)

    def __getMarketing(self,musteriId):
        result = self.data.getStoreList(
            """
             select * from MusterilerTB where ID=?
            """,(musteriId)
        )[0]
        return result.Marketing

    def __getSiparis(self,siparisNo):
        tarihIslem = TarihIslemler()
        result = self.data.getStoreList(
            """
            Select
            *,
            (Select Sum(u.SatisToplam) from SiparisUrunTB u 
            where u.SiparisNo=s.SiparisNo) as MalBedeli
            from
            SiparislerTB s
            where s.SiparisNo=?
            """,(siparisNo)
        )[0]

        model = SiparislerModel()

        model.id = result.ID
        model.siparisNo = result.SiparisNo
        model.siparisTarihi = tarihIslem.getDate(result.SiparisTarihi).strftime("%d-%m-%Y")
        if result.TahminiYuklemeTarihi != None:
         model.TahminiyuklemeTarihi = tarihIslem.getDate(result.TahminiYuklemeTarihi).strftime("%d-%m-%Y")
        model.odemeTurId = result.OdemeTurID
        model.faturaKesimTurId = result.FaturaKesimTurID
        model.liman = result.AktarmaLimanAdi
        model.teslimTurId = result.TeslimTurID 
        model.musteriId = result.MusteriID
        model.pesinat = result.Pesinat 
        model.navlunFirma = result.NavlunFirma 
        model.navlunMekmarNot = result.NavlunMekmarNot
        model.ulkeId = result.UlkeId
        model.depo = result.depo_yukleme
        model.sigorta_id = result.sigorta_id
        if result.NavlunAlis != None: 
            model.navlunAlis = result.NavlunAlis
        if result.NavlunSatis != None: 
            model.navlunSatis = result.NavlunSatis 
        model.kullaniciId = result.KullaniciID 
        model.siparisDurumId = result.SiparisDurumID 
        model.uretimAciklama = result.UretimAciklama 
        model.sevkiyatAciklama = result.SevkiyatAciklama
        model.finansAciklama  = result.FinansAciklama 
        model.odemeAciklama = result.OdemeAciklama
        model.siparisSahibi = result.SiparisSahibi
        model.operasyon = result.Operasyon
        model.finansman = result.Finansman
        model.iade = result.Iade
        if model.siparisDurumId == 3:
            model.yuklemeTarihi = tarihIslem.getDate(result.YuklemeTarihi).strftime("%d-%m-%Y")
        model.faturaNo = result.FaturaNo 
        model.siparisFaturaNo = result.SiparisFaturaNo       
        if result.Vade != None:
            model.vade = tarihIslem.getDate(result.Vade).strftime("%d-%m-%Y")
        model.ulke = result.Ulke 
        if result.Komisyon != None:
            model.komisyon = result.Komisyon
        model.detayAciklama_1 = result.DetayAciklama_1
        model.detayAciklama_2 = result.DetayAciklama_2
        model.detayAciklama_3 = result.DetayAciklama_3
        model.detayAciklama_4 = result.DetayAciklama_4
        model.detayMekmarNot_1 = result.DetayMekmarNot_1
        model.detayMekmarNot_2 = result.DetayMekmarNot_2
        model.detayMekmarNot_3 = result.DetayMekmarNot_3
        model.iscilikTutar = self.__getIscilikTutar(result.SiparisNo)
        if result.MalBedeli != None:
            model.malBedeli = result.MalBedeli
        model.odemeAciklama =  result.OdemeAciklama
        if result.DetayTutar_1 != None:
            model.detayTutar_1 = result.DetayTutar_1
        if result.DetayTutar_2 != None:
            model.detayTutar_2 = result.DetayTutar_2
        if result.DetayTutar_3 != None:
            model.detayTutar_3 = result.DetayTutar_3
        if result.DetayTutar_4 != None:
            model.detayTutar_4 = result.DetayTutar_4    
        if result.DetayAlis_1 != None:
            model.detayAlis_1 = result.DetayAlis_1
        if result.DetayAlis_2 != None:
            model.detayAlis_2 = result.DetayAlis_2
        if result.DetayAlis_3 != None:
            model.detayAlis_3 = result.DetayAlis_3
        if result.EvrakGideri != None:
            model.evrakGideri = result.EvrakGideri 
        if result.sigorta_Tutar != None:
            model.sigorta_tutar = result.sigorta_Tutar     
        if result.sigorta_tutar_satis !=None:
            model.sigorta_tutar_satis = result.sigorta_tutar_satis
        model.konteynerAyrinti = result.KonteynerAyrinti
        model.konteynerNo = result.KonteynerNo
        if result.??laclamaGideri != None:
            model.ilaclamaGideri = result.??laclamaGideri
       
        if result.Eta != None:
            model.eta = tarihIslem.getDate(result.Eta).strftime("%d-%m-%Y")
        model.digerTutarToplam = model.detayTutar_1 + model.detayTutar_2 + model.detayTutar_3 
        model.mekus_masraf = model.detayTutar_4
        model.genelToplam = model.navlunSatis + model.malBedeli + model.digerTutarToplam

       
        return model

    def __getSiparisUrunler(self,siparisNo):

        result = self.data.getStoreList(
            """
            select
            *,
            (Select t.FirmaAdi from TedarikciTB t where t.ID=s.TedarikciID) as TedarikciAdi,
            (Select u.BirimAdi from UrunBirimTB u where u.ID=s.UrunBirimID) as urunbirimadi,
            dbo.Get_UrunAdi(s.UrunKartID) as UrunAdi,
            dbo.Get_Olcu_En(s.UrunKartID) as En,
            dbo.Get_Olcu_Boy(s.UrunKartID) as Boy,
            dbo.Get_Olcu_Kenar(s.UrunKartID) as Kenar,
            dbo.Get_KenarIslem(s.UrunKartID) as YuzeyIslem,
             (select m.Marketing from SiparislerTB a , MusterilerTB m  where a.SiparisNo=s.SiparisNo and m.ID=a.MusteriID ) as musteri,
            s.UrunKartID
            from
            SiparisUrunTB s
            where s.SiparisNo=?
            order by s.SiraNo asc
            """,(siparisNo)
        )

        siparisList = list()

        for item in result:

            model = SiparisGirisUrunModel()

            model.id = item.ID 
            model.iscilik = self.__getIscilik(siparisNo,item.UrunKartID)
            model.siparisNo = item.SiparisNo 
            model.tedarikciId = item.TedarikciID 
            model.urunKartId = item.UrunKartID 
            model.urunBirimId = item.UrunBirimID 
            model.urunbirimAdi = item.urunbirimadi 
            model.miktar = item.Miktar 
            model.ozelMiktar = item.OzelMiktar 
            model.kasaAdet = item.KasaAdet 
            model.satisFiyati = item.SatisFiyati 
            model.satisToplam = item.SatisToplam 
            model.uretimAciklama = item.UretimAciklama 
            model.musteriAciklama = item.MusteriAciklama 
            model.pazarlama = item.musteri
            model.notlar = item.Notlar 
            model.kullaniciId = item.KullaniciID 
            model.alisFiyati = item.AlisFiyati 
            model.alisFiyati_Tl = item.AlisFiyati_TL
            model.siraNo = item.SiraNo 
            model.tedarikciAdi = item.TedarikciAdi
            m2,mt,ton,adet = self.__getMiktar(model.urunBirimId,model.miktar)
            model.m2 = m2
            model.mt = mt 
            model.ton = item.Ton
            model.adet = adet 
            model.urunAdi = item.UrunAdi
            model.en = item.En 
            model.boy = item.Boy 
            model.kenar = item.Kenar 
            model.yuzeyIslem = item.YuzeyIslem
            siparisList.append(model)

        return siparisList

    def __getMiktar(self,urunBirim,miktar):

        m2 = 0
        mt = 0
        ton = 0
        adet = 0

        if urunBirim == 1:
            m2 = miktar 
        if urunBirim == 2:
            adet = miktar 
        if urunBirim == 3:
            mt = miktar
        if urunBirim == 4:
            ton = miktar

        return m2,mt,ton,adet
    
    def siparisKaydet(self,urunler,siparis):
       
      siparisKayitDurum = self.__siparisDataKayit(siparis)
      if siparisKayitDurum == True:
          
          marketing = self.__getMarketing(siparis['musteriId'])
          
          urunKayitDurum = self.__siparisUrunDataKayit(urunler,siparis['siparisNo'],marketing,siparis['musteriId'])
          if urunKayitDurum == True:
              if(siparis['siparisDurumId']==1 and (siparis['odemeTurId']==1 or siparis['odemeTurId'] ==2) ):
                MailService(siparis['siparisNo'] + " nolu Sipari?? Tahsil Edilmeli", "huseyin@mekmarmarble.com", siparis['siparisNo'] + ' nolu yeni sipari?? bekleyende, tahsilat??n?? ger??ekle??tirip ??retime al??n??z!') 

              self.mailGonderInsert(siparis,siparis['siparisNo']) #yeni sipari?? i??in
              info = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' ' +  'Sipari??ini Girdi.'
              DegisiklikMain(siparis['kayit_kisi'],info)
              islem = AnaSayfaDegisiklik()
              anaSayfaDegisiklikList = islem.getAnaSayfaDegisiklik()
              degisiklik = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' Sipari??ini Girdi.'
              degisiklikAlani = 'Sipari??ler'
              islem2 = DegisiklikTahmin()
              now = datetime.datetime.now()
              year = now.strftime("%Y")
              month = now.strftime("%m")
              day = now.strftime("%d")
              hour = now.strftime("%H")
              minute = now.strftime("%M")
              second = now.strftime("%S")
              watch = str(hour) + ' : ' + str(minute) + ' : '  + str(second)
              islem2.kaydet(degisiklik,degisiklikAlani,marketing,year,month,day,watch)
              data = {
                  'status':True,
                  'anaSayfaDegisiklikList':anaSayfaDegisiklikList
              }
              return data
          else:
              self.__siparisDataSil(siparis['siparisNo'])
              self.__siparisUrunDataSilHepsi(siparis['siparisNo'])
              return False
      else:
          self.__siparisDataSil(siparis['siparisNo'])
          return False
    def __birim(self,id):
        if id == 1:
            return 'M2'
        elif id == 2:
            return 'Adet'
        elif id ==3:
            return 'MT'
        elif id == 4:
            return 'Ton'
        elif id == 5:
            return 'Sqft'
    def siparisGuncelle(self,siparis,urunlerYeni,urunlerDegisenler,urunlerSilinenler):
        
        try:
            if(siparis['siparisDurumId']==1 and (siparis['odemeTurId']==1 or siparis['odemeTurId'] ==2) ):
                MailService(siparis['siparisNo'] + " nolu Sipari?? Tahsil Edilmeli", "huseyin@mekmarmarble.com", siparis['siparisNo'] + ' nolu yeni sipari?? bekleyende, tahsilat??n?? ger??ekle??tirip ??retime al??n??z!') 

            for item in urunlerDegisenler:
                item['miktar'] = float(item['miktar'])
            self.__siparisDataGuncelle(siparis)
            
            marketing = self.__getMarketing(siparis['musteriId'])
            
            self.__siparisUrunDataKayit(urunlerYeni,siparis['siparisNo'],marketing,siparis['musteriId'])
            if len(urunlerDegisenler) >= 1 : # ??r??n de??i??tirme 
              
              self.mailGonderUpdate(siparis,urunlerDegisenler,siparis['siparisNo'])
              info = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' ' +  'Sipari?? ??r??n Bilgilerini G??ncelledi.'
              DegisiklikMain(siparis['kayit_kisi'],info)
              
            self.__siparisUrunDataGuncelle(urunlerDegisenler)
            self.__siparisUrunDataSil(urunlerSilinenler)
            
        
            

            if len(urunlerYeni) >= 1 : #yeni ??r??n ekleme
              info = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' ' +  'Yeni ??r??n Ekledi.'
              DegisiklikMain(siparis['kayit_kisi'],info)
              self.mailGonderNew(siparis,urunlerYeni,siparis['siparisNo'])
              
              if(len(urunlerYeni) == 1):
                degisiklik = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' sipari??ine ' + urunlerYeni[0]['uretimAciklama'] + ', ' + str(urunlerYeni[0]['miktar']) +' ' + self.__birim(urunlerYeni[0]['urunBirimId']) + ' $'+str(urunlerYeni[0]['satisFiyati']) +' dan eklemi??tir.'
                degisiklikAlani = 'Sipari??ler'
                islem2 = DegisiklikTahmin()
                pazarlama = ""
                if(siparis['faturaKesimTurId']==1):
                    pazarlama = 'Mekmar'
                if(siparis['faturaKesimTurId']==2):
                    pazarlama = 'Efes'
                if(siparis['faturaKesimTurId']==3):
                    pazarlama = 'Mekmer'
                now = datetime.datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%m")
                day = now.strftime("%d")
                hour = now.strftime("%H")
                minute = now.strftime("%M")
                second = now.strftime("%S")
                watch = str(hour) + ' : ' + str(minute) + ' : ' +  str(second)
                islem2.kaydet(degisiklik,degisiklikAlani,pazarlama,year,month,day,watch)     
              else:
                  for item in urunlerYeni:
                      degisiklik = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' sipari??ine ' + item['uretimAciklama'] + ', ' + str(item['miktar']) +' ' + self.__birim(item['urunBirimId']) + ' $'+str(item['satisFiyati']) +' dan eklemi??tir.'
                      degisiklikAlani = 'Sipari??ler'
                      islem2 = DegisiklikTahmin()
                      pazarlama = ""
                      if(siparis['faturaKesimTurId']==1):
                         pazarlama = 'Mekmar'
                      if(siparis['faturaKesimTurId']==2):
                        pazarlama = 'Efes'
                      if(siparis['faturaKesimTurId']==3):
                          pazarlama = 'Mekmer'
                      now = datetime.datetime.now()
                      year = now.strftime("%Y")
                      month = now.strftime("%m")
                      day = now.strftime("%d")
                      hour = now.strftime("%H")
                      minute = now.strftime("%M")
                      second = now.strftime("%S")
                      watch = str(hour) + ' : ' + str(minute) + ' : ' +  str(second)
                      islem2.kaydet(degisiklik,degisiklikAlani,pazarlama,year,month,day,watch) 
            
            
            elif len(urunlerSilinenler) >= 1 : # ??r??n silindi ise
              info = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' ' +  'Bir ??r??n Kalemi Silindi.'
              DegisiklikMain(siparis['kayit_kisi'],info)
              self.mailGonderDelete(siparis,urunlerSilinenler,siparis['siparisNo']) 
              if(len(urunlerSilinenler) == 1):
                degisiklik = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' sipari??ine ' + urunlerSilinenler[0]['uretimAciklama'] + ', ' + str(urunlerSilinenler[0]['miktar']) +' ' + self.__birim(urunlerSilinenler[0]['urunBirimId']) + ' $'+str(urunlerSilinenler[0]['satisFiyati']) +' dan silinmi??tir.'
                degisiklikAlani = 'Sipari??ler'
                islem2 = DegisiklikTahmin()
                pazarlama = ""
                if(siparis['faturaKesimTurId']==1):
                    pazarlama = 'Mekmar'
                if(siparis['faturaKesimTurId']==2):
                    pazarlama = 'Efes'
                if(siparis['faturaKesimTurId']==3):
                    pazarlama = 'Mekmer'
                now = datetime.datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%m")
                day = now.strftime("%d")
                hour = now.strftime("%H")
                minute = now.strftime("%M")
                second = now.strftime("%S")
                watch = str(hour) + ' : ' + str(minute) + ' : ' +  str(second)
                islem2.kaydet(degisiklik,degisiklikAlani,pazarlama,year,month,day,watch)     
              else:
                  for item in urunlerSilinenler:
                      degisiklik = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' sipari??ine ' + item['uretimAciklama'] + ', ' + str(item['miktar']) +' ' + self.__birim(item['urunBirimId']) + ' $'+str(item['satisFiyati']) +' dan silinmi??tir.'
                      degisiklikAlani = 'Sipari??ler'
                      islem2 = DegisiklikTahmin()
                      pazarlama = ""
                      if(siparis['faturaKesimTurId']==1):
                         pazarlama = 'Mekmar'
                      if(siparis['faturaKesimTurId']==2):
                        pazarlama = 'Efes'
                      if(siparis['faturaKesimTurId']==3):
                          pazarlama = 'Mekmer'
                      now = datetime.datetime.now()
                      year = now.strftime("%Y")
                      month = now.strftime("%m")
                      day = now.strftime("%d")
                      hour = now.strftime("%H")
                      minute = now.strftime("%M")
                      second = now.strftime("%S")
                      watch = str(hour) + ' : ' + str(minute) + ' : ' +  str(second)
                      islem2.kaydet(degisiklik,degisiklikAlani,pazarlama,year,month,day,watch)
            info = siparis['kayit_kisi'].capitalize() + ', ' + siparis['siparisNo'] + ' ' +  'Sipari?? Bilgileri De??i??tirildi.'
            DegisiklikMain(siparis['kayit_kisi'],info)
            islem = AnaSayfaDegisiklik()
            anaSayfaDegisiklikList = islem.getAnaSayfaDegisiklik()
            data = {
                'status':True,
                'anaSayfaDegisiklikList':anaSayfaDegisiklikList
            }
          
            
              
            return data
        except Exception as e:
            print('siparisGuncelle Hata 2 : ',str(e))
            return False
    def dateConvert(self,date_v):
        if (date_v) : 
            forMat = '%d-%m-%Y'
            date_v = datetime.datetime.strptime(date_v, forMat)
            return date_v.date()
        else:
            return None

    def __siparisDataKayit(self,siparis):
        
        try:
            result = self.data.getStoreList("""
                                            select * from SiparislerTB where SiparisNo=?
                                       """,(siparis['siparisNo']))
            if result:
                return False
            else:
                
                s_tarihi = self.dateConvert(siparis['siparisTarihi'])
                t_yukleme_tarihi = self.dateConvert(siparis['TahminiyuklemeTarihi'])
                vade = None 
                if siparis['vade'] != None:
                    vade = self.dateConvert(siparis['vade'])



                self.data.update_insert(
                    """
                    insert into SiparislerTB (
                        SiparisNo,SiparisTarihi,OdemeTurID,TeslimTurID,MusteriID,Pesinat,NavlunFirma,NavlunMekmarNot,NavlunAlis,
                        NavlunSatis,KullaniciID,SiparisDurumID,UretimAciklama,SevkiyatAciklama,FinansAciklama,OdemeAciklama,TahminiYuklemeTarihi,
                        Vade,Ulke,UlkeId,Komisyon,DetayAciklama_1,DetayMekmarNot_1,DetayTutar_1,DetayAlis_1,DetayAciklama_2,DetayMekmarNot_2,
                        DetayTutar_2,DetayAlis_2,DetayAciklama_3,DetayMekmarNot_3,DetayTutar_3,DetayTutar_4,DetayAciklama_4,DetayAlis_3,SiparisSahibi,EvrakGideri,Eta,
                        KonteynerAyrinti,KonteynerNo,TeslimYeri,FaturaKesimTurID,AktarmaLimanAdi,depo_yukleme,sigorta_id,sigorta_Tutar,Operasyon ,Finansman,Iade,sigorta_tutar_satis,MalBedeli
                    )
                    values
                    (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """,(
                        siparis['siparisNo'],s_tarihi,siparis['odemeTurId'],siparis['teslimTurId'],siparis['musteriId'],
                        siparis['pesinat'],siparis['navlunFirma'],siparis['navlunMekmarNot'],siparis['navlunAlis'],siparis['navlunSatis'],
                        siparis['kullaniciId'],siparis['siparisDurumId'],siparis['uretimAciklama'],siparis['sevkiyatAciklama'],
                        siparis['finansAciklama'],siparis['odemeAciklama'],t_yukleme_tarihi,vade,siparis['ulke'],siparis['ulkeId'],siparis['komisyon'],
                        siparis['detayAciklama_1'],siparis['detayMekmarNot_1'],siparis['detayTutar_1'],siparis['detayAlis_1'],
                        siparis['detayAciklama_2'],siparis['detayMekmarNot_2'],siparis['detayTutar_2'],siparis['detayAlis_2'],
                        siparis['detayAciklama_3'],siparis['detayMekmarNot_3'],siparis['detayTutar_3'],siparis['detayTutar_4'],siparis['detayAciklama_4'],siparis['detayAlis_3'],siparis['siparisSahibi'],
                        siparis['evrakGideri'],siparis['eta'],siparis['konteynerAyrinti'],siparis['konteynerNo'],siparis['teslimYeri'],siparis['faturaKesimTurId'],siparis['liman'],siparis['depo'], 
                        siparis['sigorta_id'],siparis['sigorta_tutar'],siparis['operasyon'],siparis['finansman'],siparis['iade'],siparis['sigorta_tutar_satis'],siparis['malBedeli']
                    )
                )
                
                return True
        except Exception as e :
            print('Sipari?? Data Kay??t Hata : ', str(e))
            return False

    def __siparisUrunDataKayit(self,urunler,siparisNo,marketing,musteriid):
            
            
            for item in urunler:
                
                ozelMiktar = self.decimalDegerKontrol(item['ozelMiktar'])
                ton = self.decimalDegerKontrol(item['ton'])
                if(marketing != 'Mekmar'):
                        if (item['tedarikciAdi'] == 'Mekmer' or  item['tedarikciAdi'] == 'Mek-Moz'):
                          item['alisFiyati']  = float(item['satisFiyati'] )* 0.85  
                self.data.update_insert(
                    """
                    insert into SiparisUrunTB (
                        SiparisNo,TedarikciID,UrunKartID,UrunBirimID,Miktar,OzelMiktar,KasaAdet,
                        SatisFiyati,SatisToplam,UretimAciklama,MusteriAciklama,Notlar,
                        AlisFiyati,AlisFiyati_TL,SiraNo,Ton,musteriID
                    )
                    values
                    (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                    """,(
                        siparisNo,item['tedarikciId'],item['urunKartId'],item['urunBirimId'],
                        item['miktar'],ozelMiktar,item['kasaAdet'],item['satisFiyati'],
                        item['satisToplam'],item['uretimAciklama'],item['musteriAciklama'],item['notlar'],
                        item['alisFiyati'],item['alisFiyati_Tl'],item['siraNo'],ton,musteriid
                    )
                )
           
            print('def __siparisUrunDataKayit')
            return True

    def decimalDegerKontrol(self,value):
        try:
            deger = float(value)
            return deger
        except:
            return 0

    def __siparisDataSil(self,siparisNo):

        self.data.update_insert(
            """
            delete from SiparislerTB where SiparisNo=?
            """,(siparisNo)
        )
    
    def __siparisUrunDataSilHepsi(self,siparisNo):

        self.data.update_insert(
            """
            delete from SiparisUrunTB where SiparisNo=?
            """,(siparisNo)
        )
        
    def __siparisUrunDataSil(self,urunler):

        try :
           
            for item in urunler:

                self.data.update_insert(
                    """
                    delete from SiparisUrunTB where ID=?
                    """,(item['id'])
                )
        
              
            return True
        except Exception as e:
            print('__siparisUrunDataSil : Hata : ', str(e))
            return False

    def __siparisDataGuncelle(self,siparis):
        try: 
            vade = None 
            siparis['TahminiyuklemeTarihi'] = self.dateConvert(siparis['TahminiyuklemeTarihi'])
            if siparis['vade'] != None:
                vade = self.dateConvert(siparis['vade']) 

            result = self.data.getStoreList("""
                select dhl from YeniTeklif_UlkeTB WHERE Id = ?

            """,(siparis['ulkeId']))
            cprz_kur_dhl = self.data.getStoreList("""
                    select DhlFiyat from DhlFiyatlari where ID = ?
            """,(result[0]))


            
            if siparis['yuklemeTarihi'] and siparis['teslimTurId'] != 5 and siparis['teslimTurId'] != 6 and siparis['teslimTurId'] !=12 and siparis['musteriId'] != 3444:
                
                yuklemeTarihi = self.dateConvert(siparis['yuklemeTarihi'])
                d = DovizListem()
                gun = yuklemeTarihi.day
                ay = yuklemeTarihi.month
                yil = yuklemeTarihi.year
                capraz_kur = d.getDovizKurListe(yil,ay,gun)
                
                evrak_gider = float(cprz_kur_dhl[0][0]) * float(capraz_kur) * 1.10
                
                evrak_gider = round(evrak_gider,2)
                

            else:
                evrak_gider = 0
            
            result=self.data.update_insert(
                """
                update SiparislerTB set OdemeTurID=?,TeslimTurID=?,Pesinat=?,NavlunFirma=?,NavlunMekmarNot=?,
                NavlunAlis=?,NavlunSatis=?,KullaniciID=?,UretimAciklama=?,SevkiyatAciklama=?,FinansAciklama=?,
                OdemeAciklama=?,TahminiYuklemeTarihi=?, SiparisFaturaNo=?,Vade=?,Ulke=?,UlkeId=?,Komisyon=?,
                DetayAciklama_1=?,DetayMekmarNot_1=?,DetayTutar_1=?,DetayAlis_1=?,
                DetayAciklama_2=?,DetayMekmarNot_2=?,DetayTutar_2=?,DetayAlis_2=?,
                DetayAciklama_3=?,DetayMekmarNot_3=?,DetayTutar_3=?,DetayTutar_4=?,DetayAciklama_4=?,DetayAlis_3=?,SiparisSahibi=?,EvrakGideri=?,
                KonteynerAyrinti=?,KonteynerNo=?,FaturaKesimTurID =? ,AktarmaLimanAdi =? , depo_yukleme=? ,sigorta_id=?,sigorta_Tutar=?, Operasyon =? , 
                Finansman =?, Iade=?,sigorta_tutar_satis=?, MalBedeli=? where SiparisNo=?
                """,(
                    siparis['odemeTurId'],siparis['teslimTurId'],siparis['pesinat'],siparis['navlunFirma'],siparis['navlunMekmarNot'],
                    siparis['navlunAlis'],siparis['navlunSatis'],siparis['kullaniciId'],siparis['uretimAciklama'],siparis['sevkiyatAciklama'],siparis['finansAciklama'],
                    siparis['odemeAciklama'], siparis['TahminiyuklemeTarihi'],siparis['siparisFaturaNo'],vade,siparis['ulke'],siparis['ulkeId'],siparis['komisyon'],
                    siparis['detayAciklama_1'],siparis['detayMekmarNot_1'],siparis['detayTutar_1'],siparis['detayAlis_1'],
                    siparis['detayAciklama_2'],siparis['detayMekmarNot_2'],siparis['detayTutar_2'],siparis['detayAlis_2'],
                    siparis['detayAciklama_3'],siparis['detayMekmarNot_3'],siparis['detayTutar_3'],siparis['detayTutar_4'],siparis['detayAciklama_4'],siparis['detayAlis_3'],
                    siparis['siparisSahibi'],evrak_gider,siparis['konteynerAyrinti'],siparis['konteynerNo'], siparis['faturaKesimTurId'],siparis['liman'],siparis['depo'], siparis['sigorta_id'],
                    siparis['sigorta_tutar'], siparis['operasyon'], siparis['finansman'],siparis['iade'],siparis['sigorta_tutar_satis'],siparis['malBedeli'],siparis['siparisNo']
                )
            )
            
            
            
            if siparis['siparisDurumId'] == 1 and siparis['odemeTurId']  == 3 :
                self.__siparisDurumGuncelle1(siparis['siparisNo']) 
            return True
        except Exception as e:
            print('__siparisDataGuncelle Hata  a : ',str(e))
            return False

    
    def __siparisDurumGuncelle1(self,siparis_no):
       

        try:

            self.data.update_insert(

                """
                update SiparislerTB set SiparisDurumID=2 where SiparisNo=?
                """,(siparis_no)
            )
            
           
            print("beklyen uretime gecti")
          
            return True 
        except Exception as e:
            print('__siparisDurumGuncelle1 Hata : ',str(e))             

    def __siparisUrunDataGuncelle(self,urunler):

        try:
           
            for item in urunler:
                    ton = self.decimalDegerKontrol(item['ton'])
                    if(item['pazarlama'] != 'Mekmar'):
                        if (item['tedarikciAdi'] == 'Mekmer' or  item['tedarikciAdi'] == 'Mek-Moz'):

                             item['AlisFiyati']  =  float(item['satisFiyati'] )* 0.85 
                    
                    self.data.update_insert(
                        """
                        update SiparisUrunTB set TedarikciID=?,UrunKartID=?,UrunBirimID=?,Miktar=?,
                        OzelMiktar=?,KasaAdet=?,SatisFiyati=?,SatisToplam=?,UretimAciklama=?,
                        MusteriAciklama=?,Notlar=?,KullaniciID=?,AlisFiyati=?,AlisFiyati_TL=?,
                        SiraNo=?,Ton=? where ID=?
                        """,(
                            item['tedarikciId'],item['urunKartId'],item['urunBirimId'],item['miktar'],
                            item['ozelMiktar'],item['kasaAdet'],item['satisFiyati'],item['satisToplam'],
                            item['uretimAciklama'],item['musteriAciklama'],item['notlar'],
                            item['kullaniciId'],item['alisFiyati'],item['alisFiyati_Tl'],item['siraNo'],ton,
                            item['id']
                        )
                    )
            
           
            return True
        except Exception as e:
            print('__siparisUrunDataGuncelle Hata : ',str(e))

    def __getIscilik(self,siparisNo,urunKartId):
        iscilik = ''
        for item in filter(lambda x: x.SiparisNo == siparisNo and x.UrunKartId == urunKartId,self.iscilikList):
            iscilik = item.FirmaAdi
        return iscilik

    def __getIscilikTutar(self,siparisNo):

        tutar = 0

        for item in filter(lambda x: x.SiparisNo == siparisNo,self.iscilikList):

            tutar += item.Tutar 
        
        return tutar

    
      
    def mailGonderInsert(self,siparis,siparis_no):
       
        
        result = self.data.getStoreList(
            """
            select 
            s.SiparisTarihi ,
		    s.SiparisDurumID,
            s.ID,
            s.SiparisNo,
            u.Miktar, 
            
            (select BirimAdi from UrunBirimTB t  where t.ID=u.UrunBirimID) as UrunBirimi,
            (select k.FirmaAdi from TedarikciTB k where k.ID=u.TedarikciID) as Tedarikci,
             u.UretimAciklama ,
            (select m.UrunAdi from UrunlerTB m where m.ID = n.UrunID) as urunadi,
            (select y.YuzeyIslemAdi from YuzeyKenarTB y where y.ID=n.YuzeyID) as yuzeyadi ,
            (select o.En  from OlculerTB o where o.ID=n.OlcuID) as En,
            (select o.Boy from OlculerTB o where o.ID=n.OlcuID) as Boy,
            (select o.Kenar  from OlculerTB o where o.ID=n.OlcuID) as Kenar,
		    (select p.KullaniciAdi  from KullaniciTB p where p.ID=s.SiparisSahibi) as SiparisSahibi,
            (select p.MailAdres  from KullaniciTB p where p.ID=s.Operasyon) as SiparisMail
           
            from
            SiparisUrunTB u ,SiparislerTB s ,UrunKartTB n 
            
            where 
            s.SiparisNo= u.SiparisNo 
            and u.UrunKartID = n.ID
		    and (s.SiparisDurumID=2)
            and s.SiparisNo=?
            order by s.SiparisTarihi desc
            """,(siparis_no)
        )
        baslik =  siparis['kayit_kisi'] + " taraf??ndan i??lendi ."
        body = """
        <table >
       
            <tr style ="background-color: #f2f2f2;">
                <th style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 50px;">
                Sipari?? Numaras??
                </th>
                <th style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Tedarik??i
                </th>
                <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                ??r??n Bilgisi 
                </th>
                 <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 150px;">
                ??retim A????klama 
                </th>
                 <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 ??r??n Miktar??
                </th>
                <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 Sipari?? Temsilcisi
                </th>
            </tr>
        """
         
      
        if siparis['siparisDurumId'] == 2:
            for item in result:
            
                body += f"""
            
                <tr style ="background-color: #ddd;">
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                    {item.SiparisNo}
                    </td>
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                    {item.Tedarikci}
                    </td>
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                    {item.urunadi} {item.yuzeyadi} {item.En}x{item.Boy}x{item.Kenar}
                    </td>
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;">
                    {item.UretimAciklama}
                    </td>
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                    {item.Miktar} {item.UrunBirimi} 
                    </td>
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                    {item.SiparisSahibi} 
                    </td>
                    
                </tr>
            
            
                """
            
            body = body + "</table>"
            mekmer = 0
            mekmoz = 0
            diger = 0
        
    
       
        
            for item in result:
                if item.Tedarikci == "Mekmer":
                    
                 mekmer +=1
                    
                if item.Tedarikci == "Mek-Moz":
                    
                    mekmoz +=1

                if item.Tedarikci != "Mek-Moz" and item.Tedarikci != "Mekmer":
                    
                    diger +=1    

            
            
            if  (mekmer >=1 ) and item.SiparisDurumID ==2:

                MailService(siparis_no + " Yeni Sipari?? ", "muhsin@mekmer.com"," "+ baslik + body) #muhsin
            elif (mekmoz>=1) and item.SiparisDurumID == 2:
                MailService(siparis_no + " Yeni Sipari?? ", "muhsin@mekmer.com"," "+ baslik + body) #muhsin
                
            
      
                
            if  (mekmoz + mekmer >=1) and item.SiparisDurumID ==2:
                    MailService(siparis_no + " Yeni Sipari?? ", "mehmet@mekmer.com",  " "+ baslik + body) #Mehmet 
                  
                    
                    
            if  (diger >=1 ) and item.SiparisDurumID ==2:
                    MailService(siparis_no + " Yeni Sipari?? ", "info@mekmar.com",  " " +baslik + body) #gizem
                    
                    
            if item.SiparisSahibi != 'Mehmet'  or item.SiparisSahibi != 'Gizem' : 
                  MailService(siparis_no + " Yeni Sipari?? ",item.SiparisMail , " "+ baslik + body) #sat??s temsilcisi
              

    def mailGonderNew(self,siparis,yeni,siparis_no):
       
        baslik =  siparis['kayit_kisi'] + " taraf??ndan i??lendi ."
       
        body = """
        <table >
       
            <tr style ="background-color: green;">
                <th style ="color: white;background-color: green;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 50px;">
                Sipari?? Numaras??
                </th>
                <th style ="color: white;background-color:green ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Tedarik??i
                </th>
                <th  style ="color: white;background-color: green ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                ??r??n Bilgisi 
                </th>
                 <th  style ="color: white;background-color: green ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 150px;">
                ??retim A????klama 
                </th>
                 <th  style ="color: white;background-color: green ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 ??r??n Miktar??
                </th>
               
            </tr>
        """
         
      
        if siparis['siparisDurumId'] == 2:
            for item in yeni:
                
                body += f"""
               
                <tr style ="background-color: #ddd;">
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                    {siparis_no}
                    </td>
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                   { item['tedarikciAdi'] }
                    </td>
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                   {item['urunAdi']} {item['yuzeyIslem']} {item['en']}x{item['boy']}x{item['kenar']}
                    </td>
                     <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;">
                    {item['uretimAciklama']}
                    </td>
                    <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                    {item['miktar']} {item['urunbirimAdi']} 
                    </td>
                   
                    
                </tr>
            
            
                """
            
            body = body + "</table>"
            mekmer = 0
            mekmoz = 0
            diger = 0
        
    
       
        
            for item in yeni:
                if item['tedarikciAdi'] == "Mekmer":
                    
                 mekmer +=1
                    
                if item['tedarikciAdi'] == "Mek-Moz":
                    
                    mekmoz +=1

                if item['tedarikciAdi'] != "Mek-Moz" and item['tedarikciAdi'] != "Mekmer":
                    
                    diger +=1    

            
            
            if  (mekmer >=1 ) and siparis['siparisDurumId'] ==2 :

              MailService(siparis_no + " Yeni Eklenen Kalemler ", "muhsin@mekmer.com"," "+ baslik + body) #muhsin
            
                
            
      
                
            if  (mekmoz + mekmer >=1) and siparis['siparisDurumId'] ==2 :
                MailService(siparis_no + " Yeni Eklenen Kalemler ", "mehmet@mekmer.com",  " "+ baslik + body) #Mehmet 
            
                    
                    
            if  (diger >=1 ) and siparis['siparisDurumId'] ==2 :
                 MailService(siparis_no + " Yeni Eklenen Kalemler ", "info@mekmar.com",  " " +baslik + body) #gizem
                    
            sahibi , maili = self.__siparisDetayi(siparis_no)        
            if sahibi != 'Mehmet'  or sahibi != 'Gizem': 
                  MailService(siparis_no + " Yeni Eklenen Kalemler ", maili , " "+ baslik + body) #sat??s temsilcisi(self,siparis,siparis_no):  
       
  
       
    def mailGonderUpdate(self,siparis,degisen,siparis_no):
        degismeyen = list()
        if len(degisen)==1:
            
            degismeyen = self.data.getStoreList("""
                                                select 

                                                    s.ID,
                                                    s.SiparisNo,
                                                    s.AlisFiyati,
                                                    s.SatisFiyati,
                                                    s.Miktar,
                                                    s.UretimAciklama,
                                                    s.MusteriAciklama,
                                                    ur.BirimAdi,
                                                    t.FirmaAdi,
                                                    s.musteriID


                                                from 
                                                    SiparisUrunTB s,
                                                    UrunBirimTB ur,
                                                    TedarikciTB t 
                                                where 
                                                    s.ID=? and 
                                                    s.UrunBirimID = ur.ID and 
                                                    s.TedarikciID = t.ID
                                            
                                            """,(degisen[0]['id']) )
        else:
            for i in range(0,len(degisen)):
                degismeyen.append( self.data.getStoreList("""
                                                select 

                                                    s.ID,
                                                    s.SiparisNo,
                                                    s.AlisFiyati,
                                                    s.SatisFiyati,
                                                    s.Miktar,
                                                    s.UretimAciklama,
                                                    s.MusteriAciklama,
                                                    ur.BirimAdi,
                                                    t.FirmaAdi,
                                                    s.musteriID


                                                from 
                                                    SiparisUrunTB s,
                                                    UrunBirimTB ur,
                                                    TedarikciTB t 
                                                where 
                                                    s.ID=? and 
                                                    s.UrunBirimID = ur.ID and 
                                                    s.TedarikciID = t.ID
                                            
                                """,(degisen[i]['id']) ))
        
        
        baslik =  siparis['kayit_kisi'] + " taraf??ndan i??lendi ."
        
        body = """
        <table >
            <tr style ="background-color: orange;">
                <th style ="color: white;background-color: orange;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 50px;">
                Durum
                </th>
                <th style ="color: white;background-color: orange;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 50px;">
                Sipari?? Numaras??
                </th>
                <th style ="color: white;background-color: orange ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Tedarik??i
                </th>
                <th  style ="color: white;background-color: orange ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                ??r??n Bilgisi 
                </th>
                 <th  style ="color: white;background-color: orange ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 150px;">
                ??retim A????klama 
                </th>
                 <th  style ="color: white;background-color: orange ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 ??r??n Miktar??
                </th>
                <th  style ="color: white;background-color: orange ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 Al???? Fiyat??
                </th>
                <th  style ="color: white;background-color: orange ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 Sat???? Fiyat??
                </th>
            </tr>
        """
        
                
            
        

        
        
        if siparis['siparisDurumId'] == 2:
            if len(degisen)==1:
                
                body += f"""
                        <tr style ="background-color: #ddd;">
                            <td style ="border: 1px solid #ddd;background-color:red;color:white;padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                DE??????T??R??LEN ?????????
                                    
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][1]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][8]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][6]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;">
                                {degismeyen[0][5]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][4]} {degismeyen[0][7]} 
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][2]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {float(degismeyen[0][3])}
                            </td>
                        </tr>
                
                
                        """
            else:
                for i in range(0,len(degisen)):
                    body += f"""
                        <tr style ="background-color: #ddd;">
                            <td style ="border: 1px solid #ddd;background-color:red;color:white;padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                DE??????T??R??LEN ?????????
                                    
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {degismeyen[i][0][1]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[i][0][8]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {degismeyen[i][0][6]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;">
                            {degismeyen[i][0][5]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {float(degismeyen[i][0][4])} {degismeyen[i][0][7]} 
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {float(degismeyen[i][0][2])}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {float(degismeyen[i][0][3])}
                            </td>
                        </tr>
                
                
                        """

            sayac = 0
            for item in degisen:
                body += f"""
                    <tr style ="background-color: #ddd;">
                        <td style ="border: 1px solid #ddd;background-color:#2fc289;color:white; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                DE??????EN
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:#ddd;">
                            {siparis_no}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['tedarikciAdi'],sayac,degismeyen,1)}">
                            {item['tedarikciAdi']}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['musteriAciklama'],sayac,degismeyen,7)};">
                            {item['musteriAciklama']}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;background-color:{self.__kontrol(item['uretimAciklama'],sayac,degismeyen,2)}">
                            {item['uretimAciklama']}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['miktar'],sayac,degismeyen,3)}">
                            {float(item['miktar'])} {item['urunbirimAdi']} 
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['alisFiyati'],sayac,degismeyen,5)}">
                            {float(item['alisFiyati'])}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['satisFiyati'],sayac,degismeyen,6)}">
                            {float(item['satisFiyati'])}
                        </td>
                    </tr>
            
            
                """
                sayac += 1
                
            
            body = body + "</table>"
            mekmer = 0
            mekmoz = 0
            diger = 0
        
    
       
        
            for item in degisen:
               
                if item['tedarikciAdi'] == "Mekmer":
                    
                 mekmer +=1
                    
                if item['tedarikciAdi'] == "Mek-Moz":
                    
                    mekmoz +=1

                if item['tedarikciAdi'] != "Mek-Moz" and item['tedarikciAdi'] != "Mekmer":
                    
                    diger +=1    


            if  (mekmer >=1 ) and siparis['siparisDurumId'] == 2 :

              MailService(siparis_no +" D??zenlenen Kalemler ", "muhsin@mekmer.com"," "+ baslik + body) #muhsin
                
            elif (mekmoz>1) and siparis['siparisDurumId'] == 2:
                MailService(siparis_no +" D??zenlenen Kalemler ", "muhsin@mekmer.com"," "+ baslik + body) #muhsin
                


            if  (mekmoz + mekmer >=1) and siparis['siparisDurumId'] ==2 :
                 MailService(siparis_no +" D??zenlenen Kalemler ", "mehmet@mekmer.com",  " "+ baslik + body) #Mehmet
                 

            if  (diger >=1 ) and  siparis['siparisDurumId'] ==2:
                   MailService(siparis_no +" D??zenlenen Kalemler ", "info@mekmar.com",  " " +baslik + body) #gizem
                    
            sahibi , maili = self.__siparisDetayi(siparis_no)     
            if sahibi != 'Mehmet'  or sahibi != 'Gizem': 
                  MailService(siparis_no +" D??zenlenen Kalemler ", maili  , " "+ baslik + body) #sat??s temsilcisi(self,siparis,siparis_no):
        elif siparis['siparisDurumId'] == 3:
            if len(degisen)==1:
                
                body += f"""
                        <tr style ="background-color: #ddd;">
                            <td style ="border: 1px solid #ddd;background-color:red;color:white;padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                DE??????T??R??LEN ?????????
                                    
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][1]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][8]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][6]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;">
                                {degismeyen[0][5]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][4]} {degismeyen[0][7]} 
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[0][2]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {float(degismeyen[0][3])}
                            </td>
                        </tr>
                
                
                        """
            else:
                for i in range(0,len(degisen)):
                    body += f"""
                        <tr style ="background-color: #ddd;">
                            <td style ="border: 1px solid #ddd;background-color:red;color:white;padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                DE??????T??R??LEN ?????????
                                    
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {degismeyen[i][0][1]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                {degismeyen[i][0][8]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {degismeyen[i][0][6]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;">
                            {degismeyen[i][0][5]}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {float(degismeyen[i][0][4])} {degismeyen[i][0][7]} 
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {float(degismeyen[i][0][2])}
                            </td>
                            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                            {float(degismeyen[i][0][3])}
                            </td>
                        </tr>
                
                
                        """
            
            baslik =  siparis['kayit_kisi'] + " taraf??ndan i??lendi ."
            sayac = 0
            for item in degisen:
                body += f"""
                    <tr style ="background-color: #ddd;">
                        <td style ="border: 1px solid #ddd;background-color:#2fc289;color:white; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                                DE??????EN
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:#ddd;">
                            {siparis_no}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['tedarikciAdi'],sayac,degismeyen,1)}">
                            {item['tedarikciAdi']}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['musteriAciklama'],sayac,degismeyen,7)};">
                            {item['musteriAciklama']}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;background-color:{self.__kontrol(item['uretimAciklama'],sayac,degismeyen,2)}">
                            {item['uretimAciklama']}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['miktar'],sayac,degismeyen,3)}">
                            {float(item['miktar'])} {item['urunbirimAdi']} 
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['alisFiyati'],sayac,degismeyen,5)}">
                            {float(item['alisFiyati'])}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;background-color:{self.__kontrol(item['satisFiyati'],sayac,degismeyen,6)}">
                            {float(item['satisFiyati'])}
                        </td>
                    </tr>
            
            
                """
                sayac += 1
            sahibi , maili = self.__siparisDetayi(siparis_no)
            MailService(siparis_no +" D??zenlenen Kalemler ", maili  , " "+ baslik + body) #sat??s temsilcisi(self,siparis,siparis_no):
            
    def degisimKontrol(self,degisen,degismeyen,itemName):

        for i in degisen:
            if itemName=='tedarikciAdi':
                if i[itemName] == self.degismeyenKontrol(degisen,degismeyen,8,i[itemName]):
                    return False
                else:
                    
                    return True
            elif itemName=='uretimAciklama':
                if i[itemName] == self.degismeyenKontrol(degisen,degismeyen,5,i[itemName]):
                    return False
                else:
                    return True
            elif itemName=='miktar':
                if i[itemName] == self.degismeyenKontrol(degisen,degismeyen,4,i[itemName]):
                    return False
                else:
                    
                    return True
            elif itemName=='alisFiyati':
                if i[itemName] == self.degismeyenKontrol(degisen,degismeyen,2,i[itemName]):
                    return False
                else:
                    return True
            elif itemName=='satisFiyati':
                if i[itemName] == self.degismeyenKontrol(degisen,degismeyen,3,i[itemName]):
                    return False
                else:
                    return True
           
    def degismeyenKontrol(self,degisen,degismeyen,value,itemValue):
        if len(degisen)==1:
            if degismeyen[0][value] == itemValue:
                return degismeyen[0][value]
            else:
                return degismeyen[0][value]
        else:
            for i in range(0,len(degisen)):
                if degismeyen[i][0][value] == itemValue:
                    return degismeyen[i][0][value]
                else:
                    return degismeyen[i][0][value]
               
                  
                   
    
    def mailGonderDelete(self,siparis,silinen,siparis_no):
       
        
       
        baslik =  siparis['kayit_kisi'] + " taraf??ndan i??lendi ."
      
        body = """
        <table >
       
            <tr>
                <th style ="color: white;background-color: red;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 50px;">
                Sipari?? Numaras??
                </th>
                <th style ="color: white;background-color: red;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Tedarik??i
                </th>
                <th  style ="color: white;background-color: red;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                ??r??n Bilgisi 
                </th>
                 <th  style ="color: white;background-color: red;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 150px;">
                ??retim A????klama 
                </th>
                 <th  style ="color: white;background-color: red;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 ??r??n Miktar??
                </th>
              
            </tr>
        """
         
        
        if siparis['siparisDurumId'] == 2:
            for item in silinen:
                
                body += f"""
               
                <tr style ="background-color: #ddd;">
                    <td style ="border: 1px solid #ddd;  padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                    {siparis_no}
                    </td>
                    <td style ="border: 1px solid #ddd;   padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                   { item['tedarikciAdi'] }
                    </td>
                    <td style ="border: 1px solid #ddd;   padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                   {item['urunAdi']} {item['yuzeyIslem']} {item['en']}x{item['boy']}x{item['kenar']}
                    </td>
                     <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;">
                    {item['uretimAciklama']}
                    </td>
                    <td style ="border: 1px solid #ddd; padding: 8px;  color:Red ; font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                    {item['miktar']} {item['urunbirimAdi']} 
                    </td>
                   
                    
                </tr>
            
            
                """
            
            body = body + "</table>"
            mekmer = 0
            mekmoz = 0
            diger = 0
        
    
       
        
            for item in silinen:
                if item['tedarikciAdi'] == "Mekmer":
                    
                 mekmer +=1
                    
                if item['tedarikciAdi'] == "Mek-Moz":
                    
                    mekmoz +=1

                if item['tedarikciAdi'] != "Mek-Moz" and item['tedarikciAdi'] != "Mekmer":
                    
                    diger +=1    

            
            
            if  (mekmer >=1 ) and siparis['siparisDurumId'] ==2 :

                 MailService(siparis_no +" Silinen Kalemler " , "muhsin@mekmer.com"," "+ baslik + body) #muhsin
            
            if  (mekmoz + mekmer >=1) and siparis['siparisDurumId'] ==2 :
                    MailService(siparis_no +" Silinen Kalemler " , "mehmet@mekmer.com",  " "+ baslik + body) #Mehmet 
          
                    
                    
            if  (diger >=1 ) and siparis['siparisDurumId'] ==2 :
                    MailService(siparis_no +" Silinen Kalemler " , "info@mekmar.com",  " " +baslik + body) #gizem
                    
            sahibi , maili = self.__siparisDetayi(siparis_no)          
            if sahibi != 'Mehmet'  or sahibi != 'Gizem': 
                  MailService(siparis_no +" Silinen Kalemler " , maili  , " "+ baslik + body) #sat??s temsilcisi(self,siparis,siparis_no):  
        
    def __siparisDetayi(self,siparis_no):     
       
       result = self.data.getStoreList(
            """
        select 
            (select p.KullaniciAdi  from KullaniciTB p where p.ID=s.SiparisSahibi) as SiparisSahibi,
            (select p.MailAdres  from KullaniciTB p where p.ID=s.Operasyon) as SiparisMail
           
        from
            SiparislerTB s 
            
        where 
           
            s.SiparisNo=?
         """,(siparis_no)
        )
       
       for item in result:
        
          return item.SiparisSahibi , item.SiparisMail


    def mailGonderOp(self,username,orderNo,then,now,info):
        baslik =  username + " taraf??ndan " + orderNo + " sipari??inin " + info +  " de??i??tirildi ."
        thenKullanici,nowKullanici = self.__getKullaniciAdi(then,now)
        body = f"""
        <table >
       
            <tr style ="background-color: green;">
                <th  style ="color: white;background-color: green ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 Sipari??
                </th>
                <th  style ="color: white;background-color: green ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 {info} Sahibi Eski
                </th>
                <th  style ="color: white;background-color: green ;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 {info} Sahibi Yeni
                </th>
            </tr>
        """
        body += f"""
            
            <tr style ="background-color: #ddd;">
                <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                {orderNo}
                </td>
                <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                {thenKullanici}
                </td>
                <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                {nowKullanici}
                </td>
                
            </tr>
        
        
            """
            
        body = body + "</table>"
           
        thenMail,nowMail = self.__getMailAdress(then,now)
            
        MailService(orderNo + " " + info + " sahibi de??i??ti ", thenMail , " "+ baslik + body) #sat??s temsilcisi(self,siparis,siparis_no): 
        MailService(orderNo + " " + info + " sahibi de??i??ti ", nowMail , " "+ baslik + body) #sat??s temsilcisi(self,siparis,siparis_no): 
 
             
	
    def __kontrol(self,item,sayac,degismeyen,durum):
        if len(degismeyen)== 1:
            
            if durum == 1:
                
                if item != degismeyen[sayac][8]:
                    return "red"
                else:
                    return "#ddd"
            elif durum == 2:
                
                if item != degismeyen[sayac][5]:
                    return "red"
                else:
                    return "#ddd"
            elif durum == 3:
                
                if float(item) != float(degismeyen[sayac][4]):
                    degisiklik = str(degismeyen[sayac][1]) + ' sipari??inin ' + str(degismeyen[sayac][5]) + ' kaleminin miktar?? ' + str(round(degismeyen[sayac][4],2)) + ' ' + str(degismeyen[sayac][7]) +  ' ==> ' + str(item)  + ' ' + str(degismeyen[sayac][7]) +  ' e de??i??tirildi'
                    degisiklikAlani = 'Sipari??ler'
                    fatura = str(self.__getMarketing(degismeyen[sayac][9]))
                    islem2 = DegisiklikTahmin()
                    now = datetime.datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")
                    day = now.strftime("%d")
                    hour = now.strftime("%H")
                    minute = now.strftime("%M")
                    second = now.strftime("%S")
                    watch = str(hour) + ' : ' + str(minute) + ' : ' + str(second)
                    islem2.kaydet(degisiklik,degisiklikAlani,fatura,year,month,day,watch)
                    return "red"
                else:
                    return "#ddd"
            elif durum == 4:
                if item != degismeyen[sayac][7]:
                    return "red"
                else:
                    return "yellow"
            elif durum == 5:
                if float(item) != float(degismeyen[sayac][2]):
                    degisiklik = str(degismeyen[sayac][1]) + ' sipari??inin ' + str(degismeyen[sayac][5]) + ' kaleminin al???? fiyat?? ' +  '$' + str(round(degismeyen[sayac][2],2))+ ' ==> ' + '$' + str(item) +  ' e de??i??tirildi'
                    degisiklikAlani = 'Sipari??ler'
                    fatura = str(self.__getMarketing(degismeyen[sayac][9]))
                    islem2 = DegisiklikTahmin()
                    now = datetime.datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")
                    day = now.strftime("%d")
                    hour = now.strftime("%H")
                    minute = now.strftime("%M")
                    second = now.strftime("%S")
                    watch = str(hour) + ' : ' + str(minute) + ' : ' + str(second)
                    islem2.kaydet(degisiklik,degisiklikAlani,fatura,year,month,day,watch)
                    return "red"
                else:
                    return "#ddd"
            elif durum == 6:
                
                if float(item) != float(degismeyen[sayac][3]):
                    degisiklik = str(degismeyen[sayac][1]) + ' sipari??inin ' + str(degismeyen[sayac][5]) + ' kaleminin sat???? fiyat?? ' + '$' +  str(round(degismeyen[sayac][3],2))+ ' ==> '  + '$' + str(item) +  ' e de??i??tirildi'
                    degisiklikAlani = 'Sipari??ler'
                    fatura = str(self.__getMarketing(degismeyen[sayac][9]))
                    islem2 = DegisiklikTahmin()
                    now = datetime.datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")
                    day = now.strftime("%d")
                    hour = now.strftime("%H")
                    minute = now.strftime("%M")
                    second = now.strftime("%S")
                    watch = str(hour) + ' : ' + str(minute) + ' : ' + str(second)
                    islem2.kaydet(degisiklik,degisiklikAlani,fatura,year,month,day,watch)
                    return "red"
                else:
                    return "#ddd"
            elif durum == 7:
                if item != degismeyen[sayac][6]:
                    
                    return "red"
                else:
                    return "#ddd"
        else:
            if durum == 1:
                
                if item != degismeyen[sayac][0][8]:
                    return "red"
                else:
                    return "#ddd"
            elif durum == 2:
                
                if item != degismeyen[sayac][0][5]:
                    return "red"
                else:
                    return "#ddd"
            elif durum == 3:
                
                if float(item) != float(degismeyen[sayac][0][4]):
                    degisiklik = str(degismeyen[sayac][0][1]) + ' sipari??inin ' + str(degismeyen[sayac][0][5]) + ' kaleminin miktar?? ' +  str(round(degismeyen[sayac][0][4],2)) + ' ' + str(degismeyen[sayac][0][7]) + ' ==> ' +  str(item) + ' ' +str(degismeyen[sayac][0][7]) + ' e de??i??tirildi'
                    degisiklikAlani = 'Sipari??ler'
                    fatura = str(self.__getMarketing(degismeyen[sayac][0][9]))
                    islem2 = DegisiklikTahmin()
                    now = datetime.datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")
                    day = now.strftime("%d")
                    hour = now.strftime("%H")
                    minute = now.strftime("%M")
                    second = now.strftime("%S")
                    watch = str(hour) + ' : ' + str(minute) + ' : ' + str(second)
                    islem2.kaydet(degisiklik,degisiklikAlani,fatura,year,month,day,watch)
                    return "red"
                else:
                    return "#ddd"
            elif durum == 4:
                if item != degismeyen[sayac][0][7]:
                    return "red"
                else:
                    return "#ddd"
            elif durum == 5:
                if float(item) != float(degismeyen[sayac][0][2]):
                    degisiklik = str(degismeyen[sayac][0][1]) + ' sipari??inin ' + str(degismeyen[sayac][0][5]) + ' kaleminin al???? fiyat?? ' + '$' + str(round(degismeyen[sayac][0][2],2))+ ' ==> ' + '$' + str(item) +   ' e de??i??tirildi'
                    degisiklikAlani = 'Sipari??ler'
                    fatura = str(self.__getMarketing(degismeyen[sayac][0][9]))
                    
                    islem2 = DegisiklikTahmin()
                    now = datetime.datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")
                    day = now.strftime("%d")
                    hour = now.strftime("%H")
                    minute = now.strftime("%M")
                    second = now.strftime("%S")
                    watch = str(hour) + ' : ' + str(minute) + ' : ' + str(second)
                    islem2.kaydet(degisiklik,degisiklikAlani,fatura,year,month,day,watch)
                    return "red"
                else:
                    return "#ddd"
            elif durum == 6:
                if float(item) != float(degismeyen[sayac][0][3]):
                    degisiklik = str(degismeyen[sayac][0][1]) + ' sipari??inin ' + str(degismeyen[sayac][0][5]) + ' kaleminin sat???? fiyat?? ' + '$' + str(round(degismeyen[sayac][0][3]))+ ' ==> '  + '$' + str(item) +  ' e de??i??tirildi'
                    degisiklikAlani = 'Sipari??ler'
                    fatura = str(self.__getMarketing(degismeyen[sayac][0][9]))
                    
                    islem2 = DegisiklikTahmin()
                    now = datetime.datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")
                    day = now.strftime("%d")
                    hour = now.strftime("%H")
                    minute = now.strftime("%M")
                    second = now.strftime("%S")
                    watch = str(hour) + ' : ' + str(minute) + ' : ' + str(second)
                    islem2.kaydet(degisiklik,degisiklikAlani,fatura,year,month,day,watch)
                    return "red"
                else:
                    return "#ddd"
            elif durum == 7:
                    if item != degismeyen[sayac][0][6]:
                        return "red"
                    else:
                        return "#ddd"
            
       
    def opChange(self,datas):
        info = datas['username'].capitalize() + ', ' + datas['orderNo'] + ' ' + datas['info']  + '  Degi??tirdi.'
        DegisiklikMain(datas['username'],info)
        self.mailGonderOp(datas['username'],datas['orderNo'],datas['then'],datas['now'],datas['info'])
        

    def __getMailAdress(self,then,now):
        thenMail = self.data.getStoreList("""
                                             select MailAdres from KullaniciTB where ID=?
                                          """,(then))
        nowMail = self.data.getStoreList("""
                                            select MailAdres from KullaniciTB where ID=?
                                         """,(now))
        
        return thenMail[0].MailAdres,nowMail[0].MailAdres
    
    def __getKullaniciAdi(self,then,now):
        thenKullaniciAdi = self.data.getStoreList("""
                                                   select KullaniciAdi from KullaniciTB where ID=?
                                                  
                                                  """,(then))
        nowKullaniciAdi = self.data.getStoreList("""
                                                   select KullaniciAdi from KullaniciTB where ID=?
                                                  
                                                  """,(now))
        return thenKullaniciAdi[0].KullaniciAdi,nowKullaniciAdi[0].KullaniciAdi
    
    
    def getchangeOdemeBilgisi(self,siparisNo,odemeTur):
        try:
            
            self.data.update_insert("""
                                        update SiparislerTB SET SiparisDurumID=1 where SiparisNo=?
                                    
                                    """,(siparisNo))
            self.data.update_insert("""
                                        update SiparislerTB SET OdemeTurID=? where SiparisNo=?
                                    
                                    """,(odemeTur,siparisNo))
            return True
        except Exception as e:
            print('getchangeOdemeBilgisi hata',str(e))
            return False
        
    def getchangeOdemeBilgisiEx(self,siparisNo,odemeTur):
        try:
            
            self.data.update_insert("""
                                        update SiparislerTB SET SiparisDurumID=2 where SiparisNo=?
                                    
                                    """,(siparisNo))
            self.data.update_insert("""
                                        update SiparislerTB SET OdemeTurID=? where SiparisNo=?
                                    
                                    """,(odemeTur,siparisNo))
            return True
        except Exception as e:
            print('getchangeOdemeBilgisi hata',str(e))
            return False