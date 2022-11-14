from helpers import SqlConnect
import datetime
from models.raporlar.allOrders import *
class AllOrders:
    
    def __init__(self):
        self.data = SqlConnect().data
        
    def getAllOrders(self):
        try:
            result = self.data.getList("""
                                            select 
                                                s.ID,s.SiparisNo,s.MusteriID,(select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as Musteri
                                            
                                            from 
                                            
                                                SiparislerTB s 
                                            where 
                                                s.SiparisDurumID=2
                                       """)
            liste = list()
            for item in result:
                model = AllOrdersModel()
                model.id = item.ID
                model.siparisNo = item.SiparisNo
                model.musteriId = item.MusteriID
                model.musteri = item.Musteri
                liste.append(model)
            schema = AllOrdersSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print("Siparişler Tüm Liste",str(e))
            return False
