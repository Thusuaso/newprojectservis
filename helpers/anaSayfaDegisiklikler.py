from helpers import SqlConnect,TarihIslemler
import datetime
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
            
            self.data.update_insert("""
                                        insert into MaliyetAnaliziDegisikliklerTB(DegisiklikTarihi,YuklemeTarihi,SiparisNo,IslemAdi,DegisiklikYapan) VALUES(?,?,?,?,?)
                                    
                                    """,(now,yukleme_tarihi,siparis_no,islem_adi,degisiklik_yapan))
        except Exception as e:
            print('setMaliyetDegisiklik hata',str(e))
            return False