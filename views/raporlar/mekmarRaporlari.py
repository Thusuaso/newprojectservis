from helpers import SqlConnect
from models.raporlar import *

class MekmarRaporlari:
    def __init__(self):
        self.data = SqlConnect().data
        self.ulkeyeGoreMasraflar = []
        self.musteriyeGoreMasraflar = []
    def getUlkeRaporlari(self,year):
        try:
            result = self.data.getStoreList("""
                                        select 
										count(m.UlkeId) as SipSayisi,
										yu.UlkeAdi,
										sum(s.KonteynirSayisi) as KonteynirSayisi,
										m.UlkeId

                                    from MusterilerTB m
                                    inner join SiparislerTB s on s.MusteriID = m.ID
                                    inner join YeniTeklif_UlkeTB yu on yu.Id = m.UlkeId

                                    where YEAR(s.YuklemeTarihi) = ? and m.Marketing = 'Mekmar'
									group by m.UlkeId,yu.UlkeAdi
                                   """,(year))
            
            liste = list()
            for item in result:
                model = UlkeyeGoreModel()
                model.sip_sayisi = item.SipSayisi
                model.ulke_adi = item.UlkeAdi
                model.ulke_id = item.UlkeId
                model.konteynir_sayisi = item.KonteynirSayisi
                liste.append(model)
            schema = UlkeyeGoreSchema(many=True)
            return schema.dump(liste)
            
        except Exception as e:
            print('getUlkeRaporlari hata',str(e))
            return False

    def getUlkeRaporlariAyrinti(self,ulke_id,year):
        try:
            siparis = self.data.getStoreList("""
                                                select 
													m.FirmaAdi,
                                                    s.SiparisNo,
                                                    sum(su.SatisToplam) as SatisToplam


                                                from MusterilerTB m
                                                inner join SiparislerTB s on s.MusteriID = m.ID
                                                inner join SiparisUrunTB su on su.SiparisNo=  s.SiparisNo

                                                where m.Marketing = 'Mekmar' and m.UlkeId = ? and YEAR(s.YuklemeTarihi) = ?

                                                group by s.SiparisNo,m.FirmaAdi
                                            
                                            """,(ulke_id,year))
            
            self.ulkeyeGoreMasraflar = self.data.getStoreList("""
                                                                select 

                                                                    s.SiparisNo,
                                                                    s.NavlunSatis,
                                                                    s.DetayTutar_1,
                                                                    s.DetayTutar_2,
                                                                    s.DetayTutar_3,
                                                                    s.DetayTutar_4,
                                                                    s.sigorta_tutar_satis


                                                                from MusterilerTB m
                                                                inner join SiparislerTB s on s.MusteriID = m.ID

                                                                where m.Marketing = 'Mekmar' and m.UlkeId = ? and YEAR(s.YuklemeTarihi) = ?
                                                              
                                                              """,(ulke_id,year))
            
            liste  = list()
            for item in siparis:
                model = UlkeyeGoreAyrintiModel()
                model.musteri_adi = item.FirmaAdi
                model.siparis_no = item.SiparisNo
                model.fob_toplami = self.__getNone(item.SatisToplam)
                navlun,detay1,detay2,detay3,detay4,sigorta = self.__getUlkeyeGoreMasraflar(item.SiparisNo)
                model.navlun = self.__getNone(navlun)
                model.detay_1 = self.__getNone(detay1)
                model.detay_2 = self.__getNone(detay2)
                model.detay_3 = self.__getNone(detay3)
                model.detay_4 = self.__getNone(detay4)
                model.sigorta = self.__getNone(sigorta)
                model.dtp_toplami = model.fob_toplami + model.navlun + model.detay_1 + model.detay_2 + model.detay_3 + model.detay_4 + model.sigorta
                liste.append(model)
            schema = UlkeyeGoreAyrintiSchema(many = True)
            return schema.dump(liste)
            
        except Exception as e:
            print('getUlkeRaporlariAyrinti,hata',str(e))
            return False
    
    def __getUlkeyeGoreMasraflar(self,siparisno):
        for item in self.ulkeyeGoreMasraflar:
            if(item.SiparisNo == siparisno):
                return item.NavlunSatis,item.DetayTutar_1,item.DetayTutar_2,item.DetayTutar_3,item.DetayTutar_4,item.sigorta_tutar_satis
            else:
                return 0,0,0,0,0,0
    
    
    def getMusteriRaporlari(self,year):
        try:
            result = self.data.getStoreList("""
                                                select 


                                                    count(m.ID) as YukMusSayisi,
                                                    m.ID,
                                                    m.FirmaAdi,
                                                    yu.UlkeAdi,
                                                    sum(s.KonteynirSayisi) as KonteynirSayisi


                                                from MusterilerTB m
                                                inner join SiparislerTB s on s.MusteriID = m.ID
                                                inner join YeniTeklif_UlkeTB yu on yu.Id = m.UlkeId

                                                where m.Marketing = 'Mekmar' and YEAR(s.YuklemeTarihi) = ?
                                                group by
                                                    m.ID,m.FirmaAdi,yu.UlkeAdi
                                            
                                            
                                            """,(year))
            
            liste = list()
            for item in result:
                model = MusteriyeGoreModel()
                model.id = item.ID
                model.firma_adi = item.FirmaAdi
                model.yuk_mus_sayisi = item.YukMusSayisi
                model.ulke_adi = item.UlkeAdi
                model.konteynir_sayisi = item.KonteynirSayisi
                liste.append(model)
            schema = MusteriyeGoreSchema(many = True)
            return schema.dump(liste)
        except Exception as e:
            print(' getMusteriRaporlari , hata',str(e))
            return False
        
    def getMusteriRaporlariAyrinti(self,musteri_id,year):
        try:
            siparis = self.data.getStoreList("""
                                                select 
													m.FirmaAdi,
                                                    s.SiparisNo,
                                                    sum(su.SatisToplam) as SatisToplam


                                                from MusterilerTB m
                                                inner join SiparislerTB s on s.MusteriID = m.ID
                                                inner join SiparisUrunTB su on su.SiparisNo=  s.SiparisNo

                                                where m.Marketing = 'Mekmar' and m.ID = ? and YEAR(s.YuklemeTarihi) = ?

                                                group by s.SiparisNo,m.FirmaAdi
                                             
                                             """,(musteri_id,year))
            
            self.musteriyeGoreMasraflar = self.data.getStoreList("""
                                                                    select 

                                                                    s.SiparisNo,
                                                                    s.NavlunSatis,
                                                                    s.DetayTutar_1,
                                                                    s.DetayTutar_2,
                                                                    s.DetayTutar_3,
                                                                    s.DetayTutar_4,
                                                                    s.sigorta_tutar_satis


                                                                from MusterilerTB m
                                                                inner join SiparislerTB s on s.MusteriID = m.ID

                                                                where m.Marketing = 'Mekmar' and m.ID = ? and YEAR(s.YuklemeTarihi) = ?

                                                                 """,(musteri_id,year))
            liste = list()
            for item in siparis:
                model = UlkeyeGoreAyrintiModel()
                model.musteri_adi = item.FirmaAdi
                model.siparis_no = item.SiparisNo
                model.fob_toplami = self.__getNone(item.SatisToplam)
                navlun,detay1,detay2,detay3,detay4,sigorta = self.__getMusteriyeGoreMasraflar(item.SiparisNo)
                model.navlun = self.__getNone(navlun)
                model.detay_1 = self.__getNone(detay1)
                model.detay_2 = self.__getNone(detay2)
                model.detay_3 = self.__getNone(detay3)
                model.detay_4 = self.__getNone(detay4)
                model.sigorta = self.__getNone(sigorta)
                model.dtp_toplami = model.fob_toplami + self.__getNone(navlun) + self.__getNone(detay1) + self.__getNone(detay2) + self.__getNone(detay3) + self.__getNone(detay4) + self.__getNone(sigorta)
                liste.append(model)
            schema = UlkeyeGoreAyrintiSchema(many = True)
            return schema.dump(liste)
                
            
        except Exception as e:
            print('getMusteriRaporlariAyrinti ,hata',str(e))
            return False
            
    def __getMusteriyeGoreMasraflar(self,siparis_no):
        for item in self.musteriyeGoreMasraflar:
            if(item.SiparisNo == siparis_no):
                return item.NavlunSatis,item.DetayTutar_1,item.DetayTutar_2,item.DetayTutar_3,item.DetayTutar_4,item.sigorta_tutar_satis
            else:
                return 0,0,0,0,0,0
            
    def __getNone(self,value):
        if value == None:
            return 0
        else:
            return value
    
    def getTedarikciRaporlari(self,year):
        try:
            result = self.data.getStoreList("""
                                    select 


                                        t.ID,
                                        t.FirmaAdi,
                                        sum(su.AlisFiyati * su.Miktar) as Total,
                                        count(t.ID) as YuklenenTedarikci

                                    from TedarikciTB t
                                    inner join SiparisUrunTB su on su.TedarikciID = t.ID
                                    inner join SiparislerTB s on s.SiparisNo= su.SiparisNo
                                    inner join MusterilerTB m on m.ID = s.MusteriID
                                    where YEAR(s.YuklemeTarihi) = ? and m.Marketing = 'Mekmar'

                                    group by 
                                        t.ID,t.FirmaAdi
                                    order by 
                                        Total desc
                                   
                                   """,(year))
            liste=  list()
            for item in result:
                model = TedarikciyeGoreModel()
                model.tedarikci_id = item.ID
                model.firma_adi = item.FirmaAdi
                model.total_alis = item.Total
                model.yuklenen_tedarikci_sayisi = item.YuklenenTedarikci
                liste.append(model)
            schema = TedarikciyeGoreSchema(many= True)
            return schema.dump(liste)
            
        except Exception as e:
            print("getTedarikciRaporlari,hata",str(e))
            return False
        
        
    def getTedarikciAyrintiRaporlari(self,tedarikci_id,year):
        try:
            siparis = self.data.getStoreList("""
                                                select 

                                                    m.FirmaAdi,
                                                    s.SiparisNo,
                                                    sum(su.Miktar * su.AlisFiyati) as AlisToplam


                                                from TedarikciTB t
                                                inner join SiparisUrunTB su on su.TedarikciID = t.ID
                                                inner join SiparislerTB s on s.SiparisNo= su.SiparisNo
                                                inner join MusterilerTB m on m.ID = s.MusteriID

                                                where m.Marketing= 'Mekmar' and YEAR(s.YuklemeTarihi) = ? and t.ID=?

                                                group by s.SiparisNo,m.FirmaAdi
                                             """,(year,tedarikci_id))
            
            liste = list()
            for item in siparis:
                model   = TedarikciyeGoreAyrintiModel()
                model.firma_adi = item.FirmaAdi
                model.siparis_no = item.SiparisNo
                model.alis_toplami = self.__getNone(item.AlisToplam)
                liste.append(model)
                
            schema = TedarikciyeGoreAyrintiSchema(many = True)
            return schema.dump(liste)
        except Exception as e:
            print('getTedarikciAyrintiRaporlari, hata' , str(e))
            return False