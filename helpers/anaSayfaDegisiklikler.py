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