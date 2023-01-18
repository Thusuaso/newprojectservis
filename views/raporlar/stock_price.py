from models.raporlar import SiparisGiderTurModel,SiparisGiderTurSchema
from helpers import SqlConnect 

class StockPrice:
    def __init__(self):
        self.data = SqlConnect().data
        
    def add(self,data):
        try:
            self.data.update_insert("""
                                        update UrunKartTB SET Price=? where ID=?
                                    
                                    """,(data['price'],data['productId']))
            return True
        
        except Exception as e:
            print('StockPrice add hata',str(e))
            return False