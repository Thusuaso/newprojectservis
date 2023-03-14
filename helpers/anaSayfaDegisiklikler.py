from helpers import SqlConnect,TarihIslemler
import datetime
class DegisiklikMain:
    def __init__(self,username,info):
        self.username = username
        self.info = info
        self.data = SqlConnect().data
        self.setYapilanDegisiklikBilgisi()
        
    def setYapilanDegisiklikBilgisi(self):
        try:
            now = datetime.datetime.now()
            self.data.update_insert("""
                                        insert into AnaSayfaYapılanDegisiklikler(DegisiklikYapan,YapılanDegisiklik,DegisiklikTarihi) VALUES(?,?,?)
                                    
                                    """,(self.username,self.info,now))
        except Exception as e:
            print("siparisBilgisiKaydet hatalı",str(e))
            return False
        
    def setMaliyetDegisiklik(self,islem_adi,degisiklik_yapan,siparis_no,yukleme_tarihi):
        try:
            if(yukleme_tarihi == None or yukleme_tarihi == ""):
                yukleme_tarihi = ""
                
            now = datetime.datetime.now()
            
            self.data.update_insert("""
                                        insert into MaliyetAnaliziDegisikliklerTB(DegisiklikTarihi,YuklemeTarihi,SiparisNo,IslemAdi,DegisiklikYapan) VALUES(?,?,?,?,?)
                                    
                                    """,(now,yukleme_tarihi,siparis_no,islem_adi,degisiklik_yapan))
        except Exception as e:
            print('setMaliyetDegisiklik hata',str(e))
            return False