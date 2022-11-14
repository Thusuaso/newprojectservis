from helpers import SqlConnect
from models.finans.odemelerList import OdemelerListSchema,OdemelerListModel,OdemelerListAyrintiSchema,OdemelerListAyrintiModel
class Odemeler:
    def __init__(self):
        self.data = SqlConnect().data
    def getOdemelerList(self):
        result = self.data.getList("""
                                   
                                        select 
                                        sum(o.Tutar) as Tutar,(select m.FirmaAdi from MusterilerTB m where m.ID = o.MusteriID) as MusteriAdi,o.MusteriID as ID
                                        from 
                                        OdemelerTB o 
                                        where YEAR(o.Tarih)>=2020 group by o.MusteriID
                                        order by sum(o.Tutar) desc
                                   
                                   
                                   """)
        liste = list()
        for item in result:
            model = OdemelerListModel()
            model.Id = item[2]
            model.musteri_adi = item[1]
            model.tutar = float(item[0])
            liste.append(model)
        
        schema = OdemelerListSchema(many=True)

        return schema.dump(liste)
    
    def getOdemelerListAyrinti(self,musteriId):
        
        result = self.data.getStoreList("""
                                            select  
                                                o.Tarih,
                                                o.SiparisNo,
                                                o.Tutar 
                                            from 
                                                OdemelerTB o 
                                            where 
                                                o.MusteriID= ? and 
                                                YEAR(Tarih) >=2020
                                            order by
                                                Tarih desc
                                        """,(musteriId))
        
        liste = list()
        for item in result:
            
            model = OdemelerListAyrintiModel()
            model.tarih = item.Tarih
            model.po = item.SiparisNo
            model.odenenTutar = item.Tutar
            liste.append(model)
            
        schema = OdemelerListAyrintiSchema(many=True)

        return schema.dump(liste)
            
            
            
        
         
