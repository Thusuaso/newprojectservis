from helpers import SqlConnect,TarihIslemler
import datetime


class Kullanicilar:
    
    def __init__(self):
        self.data = SqlConnect().data
        
        
    def setKullaniciPassGuncelleme(self,item):
        
         
        try:
            self.data.update_insert(
                """
                update KullaniciTB SET YSifre=? where KullaniciAdi=?
                """,(
                    item['userPassword'],item['username']
                )
            )

            return True

        except Exception as e:
            print('Kullanici Sifre Guncelleme Hata : ',str(e))
            return False    
