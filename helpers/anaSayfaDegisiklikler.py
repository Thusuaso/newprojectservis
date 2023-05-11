from helpers import SqlConnect,TarihIslemler
import datetime
from views.raporlar.dashboard.dashboard import DashboardNew

class DegisiklikMain:
    def __init__(self):
        self.data = SqlConnect().data
        
    def setYapilanDegisiklikBilgisi(self,username,info):
        try:
            now = datetime.datetime.now()
            self.data.update_insert("""
                                        insert into AnaSayfaYapılanDegisiklikler(DegisiklikYapan,YapılanDegisiklik,DegisiklikTarihi) VALUES(?,?,?)
                                    
                                    """,(username,info,now))
        except Exception as e:
            print("siparisBilgisiKaydet hatalı",str(e))
            return False
        
    def setMaliyetDegisiklik(self,islem_adi,degisiklik_yapan,siparis_no,yukleme_tarihi):
        try:
                
            now = datetime.datetime.now()
            yuklenen = DashboardNew().getDashboardYuklenenSiparisYillikMekmar()
            siparis = DashboardNew().getDashboardGelenSiparisYillikMekmar()
            self.data.update_insert("""
                                        insert into MaliyetAnaliziDegisikliklerTB(DegisiklikTarihi,YuklemeTarihi,SiparisNo,IslemAdi,DegisiklikYapan,YuklenenBuAyHaric,YuklenenYilSonuTahmin,SiparisBuAyHaric,SiparisYilSonuTahmin) VALUES(?,?,?,?,?,?,?,?,?)
                                    
                                    """,(now,yukleme_tarihi,siparis_no,islem_adi,degisiklik_yapan,yuklenen[0]['gelenSiparisFob'],yuklenen[0]['gelenSiparisYilSonuTahmini'],siparis[0]['gelenSiparisFob'],siparis[0]['gelenSiparisYilSonuTahmini']))
        except Exception as e:
            print('setMaliyetDegisiklik hata',str(e))
            return False