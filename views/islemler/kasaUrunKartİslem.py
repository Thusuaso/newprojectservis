from models import *
from helpers import SqlConnect,TarihIslemler,DegisiklikMain
from resource_api.raporlar.uretim_rapor import UretimRapor
class KasaUrunKart:

    def __init__(self):
        self.data = SqlConnect().data

    def guncelle(self,kasaNo,urunKartId,username):
        
        try:
            
            self.data.update_insert("""
                                        update UretimTB SET UrunKartID =? WHERE KasaNo=?
                                    
                                    
                                    """,(urunKartId,kasaNo))
            info = username + ', ' + 'Kasa Ürün Bilgisi Değiştirdi.'
            DegisiklikMain().setYapilanDegisiklikBilgisi(username,info)
            islem = UretimRapor()
            result = islem.getUretimListesiHepsi()
            print('KasaUrunKart guncelle başarılı')
            return {'status':True,'datas':result}
        except Exception as e:
            print("KasaUrunKart guncelle hata",str(e))
            return False

 