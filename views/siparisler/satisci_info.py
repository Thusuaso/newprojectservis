from helpers import SqlConnect
from models.siparisler_model import *
class SatisciInfo:
    def __init__(self):
        self.data = SqlConnect().data
        
    def getSiparisSatisciInfo(self):
        
        try:
            
            result = self.data.getList("""
                                            select 

                                                s.SiparisNo as Po,
                                                s.ID,
                                                s.SiparisSahibi as SatisciId,
                                                s.Operasyon as OperasyonId,
                                                (select k.KullaniciAdi from KullaniciTB k where k.ID = s.SiparisSahibi) as SiparisSahibi,
                                                (select k.KullaniciAdi from KullaniciTB k where k.ID = s.Operasyon) as Operasyon



                                            from SiparislerTB s
                                            where
                                                s.SiparisDurumID=2 and s.FaturaKesimTurID=1
                                            order by s.ID desc
                                       
                                       """)
            
            liste = list()
            for item in result:
                model = SatisciInfoModel()
                model.id = item.ID
                model.po = item.Po
                model.satisci_id = item.SatisciId
                model.satisci_adi = item.SiparisSahibi
                model.operasyon_id = item.OperasyonId
                model.operasyon_adi = item.Operasyon
                liste.append(model)
            schema = SatisciInfoSchema(many = True)
            return schema.dump(liste)
        except Exception as e:
            print('getSiparisSatisciInfo hata',str(e))
            return False
        
    def getSiparisSatisciOzet(self):
        try:
            
            result = self.data.getList("""
                                            select 

 												count(s.Operasyon) as OpCount,
												(select k.KullaniciAdi from KullaniciTB k where k.ID = s.Operasyon) as OperasyonAdi



                                            from SiparislerTB s
                                            where
                                                s.SiparisDurumID=2 and s.FaturaKesimTurID=1
											group by s.Operasyon

                                       
                                       """)
            
            liste = list()
            for item in result:
                model = SatisciInfoOzetModel()
                model.ad = item.OperasyonAdi
                model.adet = item.OpCount
                liste.append(model)
            schema = SatisciInfoOzetSchema(many = True)
            return schema.dump(liste)
        except Exception as e:
            print('getSiparisSatisciInfo hata',str(e))
            return False
        
    def getSiparisSahibiOzet(self):
        try:
            
            result = self.data.getList("""
                                            select 
 												count(s.SiparisSahibi) as SpCount,
												(select k.KullaniciAdi from KullaniciTB k where k.ID = s.SiparisSahibi) as SiparisciAdi
                                            from SiparislerTB s
                                            where
                                                s.SiparisDurumID=2 and s.FaturaKesimTurID=1
											group by s.SiparisSahibi
                                       """)
            
            liste = list()
            for item in result:
                model = SatisciInfoOzetModel()
                model.ad = item.SiparisciAdi
                model.adet = item.SpCount
                liste.append(model)
            schema = SatisciInfoOzetSchema(many = True)
            return schema.dump(liste)
        except Exception as e:
            print('getSiparisSatisciInfo hata',str(e))
            return False
        
    def setSatisciInfo(self,po,ss,op):
        try:
            
            self.data.update_insert("""
                                        update SiparislerTB SET Operasyon=?,SiparisSahibi=? where SiparisNo=?
                                    
                                    """,(op,ss,po))
            return True
        except Exception as e:
            return False