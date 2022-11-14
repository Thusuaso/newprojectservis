from helpers import SqlConnect,TarihIslemler
from models.efesfinans.efes_gelen_siparis import *
import datetime
class EfesGelenSiparisBilgileri:
    def __init__(self):
        self.data = SqlConnect().data

    def getEfesGelenSiparisBilgileri(self):
        try:
            result = self.data.getList("""
                                            select 
                                                s.ID,
                                                s.SiparisNo,
                                                s.Pesinat,
                                                (select m.FirmaAdi from MusterilerTB m where m.ID = s.MusteriID) as Firma,
                                                (select k.KullaniciAdi from KullaniciTB k where k.ID = s.SiparisSahibi) as SiparisSahibi,
                                                (select k.KullaniciAdi from KullaniciTB k where k.ID = s.Operasyon) as Operasyon,
                                                s.SiparisTarihi as SiparisTarihi,
                                                s.YuklemeTarihi as YuklemeTarihi,
                                                (select sd.Durum from SiparisDurumTB sd where sd.ID = s.SiparisDurumID) as SiparisDurum
                                                


                                            from 
                                                SiparislerTB s

                                            where 

                                                s.FaturaKesimTurID=2 and 
                                                (YEAR(s.YuklemeTarihi) = YEAR(GETDATE()) or YEAR(s.SiparisTarihi) = YEAR(GETDATE()))
                                       
                                       
                                       """)
            liste = list()
            for item in result:
                model = EfesGelenSipModel()
                model.id = item.ID
                model.siparisNo = item.SiparisNo
                model.musteri = item.Firma
                model.siparisTarihi = item.SiparisTarihi
                model.siparisYuklemeTarihi = item.YuklemeTarihi
                model.siparisSahibi = item.SiparisSahibi
                model.operasyon = item.Operasyon
                model.siparisDurum = item.SiparisDurum
                
                liste.append(model)
            schema = EfesGelenSipSchema(many=True)
            return schema.dump(liste)
            

        except Exception as e:
            print('getEfesGelenSiparisBilgileri hata',str(e))
    
    def getEfesGelenSiparisBilgileriAll(self):
        try:
            result = self.data.getList("""
                                            select 
                                                s.ID,
                                                s.SiparisNo,
                                                s.Pesinat,
                                                (select m.FirmaAdi from MusterilerTB m where m.ID = s.MusteriID) as Firma,
                                                (select k.KullaniciAdi from KullaniciTB k where k.ID = s.SiparisSahibi) as SiparisSahibi,
                                                (select k.KullaniciAdi from KullaniciTB k where k.ID = s.Operasyon) as Operasyon,
                                                s.SiparisTarihi as SiparisTarihi,
                                                s.YuklemeTarihi as YuklemeTarihi,
                                                (select sd.Durum from SiparisDurumTB sd where sd.ID = s.SiparisDurumID) as SiparisDurum
                                                


                                            from 
                                                SiparislerTB s

                                            where 

                                                s.FaturaKesimTurID=2
                                       
                                       
                                       """)
            liste = list()
            for item in result:
                model = EfesGelenSipModel()
                model.id = item.ID
                model.siparisNo = item.SiparisNo
                model.musteri = item.Firma
                model.siparisTarihi = item.SiparisTarihi
                model.siparisYuklemeTarihi = item.YuklemeTarihi
                model.siparisSahibi = item.SiparisSahibi
                model.operasyon = item.Operasyon
                model.siparisDurum = item.SiparisDurum
                
                liste.append(model)
            schema = EfesGelenSipSchema(many=True)
            return schema.dump(liste)
            

        except Exception as e:
            print('getEfesGelenSiparisBilgileriAll hata',str(e))
    
    
    
    def getEfesGelenSiparisBilgileriAyrinti(self,siparisNo):
        try:
            result = self.data.getStoreList("""
                                            select 
                                                su.ID as ID,
                                                su.SatisToplam as SatisToplam,
                                                su.SatisFiyati as SatisFiyati,
                                                su.Miktar as Miktar,
                                                (select urb.BirimAdi from UrunBirimTB urb where urb.ID = su.UrunBirimID) as UrunBirim,
                                                (select k.KategoriAdi from KategoriTB k where k.ID = urk.KategoriID) as Kategori,
                                                (select yk.YuzeyIslemAdi from YuzeyKenarTB yk where yk.ID = urk.YuzeyID) as Yuzey,
                                                (select uk.UrunAdi from UrunlerTB uk where uk.ID = urk.UrunID) as UrunAdi,
                                                (select ol.En from OlculerTB ol where ol.ID = urk.OlcuID) as En,
                                                (select ol.Kenar from OlculerTB ol where ol.ID = urk.OlcuID) as Kenar,
                                                (select ol.Boy from OlculerTB ol where ol.ID = urk.OlcuID) as Boy
                                            from
                                                SiparisUrunTB su
                                                inner join UrunKartTB urk on urk.ID = su.UrunKartID
                                            where SiparisNo=?
                                       
                                       
                                       """,siparisNo)
            liste = list()
            for item in result:
                model = EfesGelenSipAyrintiModel()
                model.id = item.ID
                model.satisToplami = item.SatisToplam
                model.satisFiyati = item.SatisFiyati
                model.miktar = item.Miktar
                model.urunBirim = item.UrunBirim
                model.kategori = item.Kategori
                model.yuzey = item.Yuzey
                model.urunAdi = item.UrunAdi
                model.en = item.En
                model.boy = item.Boy
                model.kenar = item.Kenar
                
                
                liste.append(model)
            schema = EfesGelenSipAyrintiSchema(many=True)
            return schema.dump(liste)
            

        except Exception as e:
            print('getEfesGelenSiparisBilgileri hata',str(e))
    
    