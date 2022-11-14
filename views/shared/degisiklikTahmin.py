from helpers.sqlConnect import SqlConnect
from models.dashboard.gelenSiparis import *
class DegisiklikTahmin:
    def __init__(self):
        self.sql = SqlConnect().data
        
    def kaydet(self,degisiklik,degisiklikAlani,fatura,yil,ay,gun,saat):
        try:
            self.sql.update_insert("""
                                        insert into TahminiDegisiklikAlani(Degisiklik,DegisiklikBolge,Fatura,Yil,Ay,Gun,Saat) VALUES(?,?,?,?,?,?,?)
                                   
                                   """,(degisiklik,degisiklikAlani,fatura,yil,ay,gun,saat))
            return True
        except Exception as e:
            print('DegisiklikTahmin kaydet',str(e))
            return False
        
    def getDegisiklikTahmin(self):
        try:
            result = self.sql.getList("""
                                select * from TahminiDegisiklikAlani where Fatura = 'Mekmar' order by ID desc
                             
                             """)
            liste = list()
            for item in result:
                model = TahminiDegisiklikModel()
                model.degisiklik = item.Degisiklik
                model.degisiklikAlani = item.DegisiklikBolge
                model.year = item.Yil
                model.month = item.Ay
                model.day = item.Gun
                model.watch = item.Saat
                liste.append(model)
            schema = TahminiDegisiklikSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getDegisiklikTahmin hata',str(e))
            return False