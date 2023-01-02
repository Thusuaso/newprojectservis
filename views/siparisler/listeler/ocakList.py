from helpers import SqlConnect
from models.siparisler_model.ocaklar import * 
class OcakList:
    def __init__(self):
        self.data = SqlConnect().data
        
    def getOcakList(self):
        try:
            ocakList = self.data.getList("""
                                            select * from UrunOcakTB
                                         
                                         
                                         """)
            liste = list()
            for item in ocakList:
                model = OcakListModel()
                model.id = item.ID
                model.mineName = item.OcakAdi
                liste.append(model)
            schema = OcakListSchema(many=True)
            return schema.dump(liste)
        
        except Exception as e :
            print('',str(e))
            return False