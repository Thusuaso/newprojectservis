from helpers import SqlConnect,TarihIslemler
from models.raporlar import *
from marshmallow import Schema,fields


class UlkeBazindaSevkiyat:
    def __init__(self):

        self.data = SqlConnect().data


    def getUlkeBazindaSevkiyat(self):
        
        result = self.data.getList("""
                          
                            select 

                                m.UlkeId,
                                (select yu.UlkeAdi from YeniTeklif_UlkeTB yu where m.UlkeId=yu.Id) as UlkeAdi,
                                sum(s.Toplam) as Sevkiyat



                            from 


                                MusterilerTB m 
                                inner join SevkiyatTB s on s.MusteriID = m.ID
                            where
                                m.Marketing = 'Mekmar'


                            group by m.UlkeId
                            order by sum(s.Toplam) desc
                          
                          
                          """)
        liste = list()
        for item in result:

            model = UlkeBazindaSevkiyatModel()

            model.ulkeid = item.UlkeId
            model.ulkeadi = item.UlkeAdi
            model.toplamsevkiyat = item.Sevkiyat
            
            
            liste.append(model)

        
        schema = UlkeBazindaSevkiyatSchema(many=True)

        return schema.dump(liste)
    def getUlkeBazindaSevkiyatYear(self,year):
        result = self.data.getStoreList("""
                          
                            select 

                                m.UlkeId,
                                (select yu.UlkeAdi from YeniTeklif_UlkeTB yu where m.UlkeId=yu.Id) as UlkeAdi,
                                sum(s.Toplam) as Sevkiyat



                            from 


                                MusterilerTB m 
                                inner join SevkiyatTB s on s.MusteriID = m.ID
                            where
                                m.Marketing = 'Mekmar' and
                                YEAR(s.Tarih) = ?



                            group by m.UlkeId
                            order by sum(s.Toplam) desc
                          
                          
                          """,(year))
        liste = list()
        for item in result:

            model = UlkeBazindaSevkiyatModel()

            model.ulkeid = item.UlkeId
            model.ulkeadi = item.UlkeAdi
            model.toplamsevkiyat = item.Sevkiyat
            
            
            liste.append(model)

        
        schema = UlkeBazindaSevkiyatSchema(many=True)

        return schema.dump(liste)


class UlkeBazindaSevkiyatSchema(Schema):
    ulkeid = fields.Integer()
    ulkeadi = fields.String()
    toplamsevkiyat = fields.Integer()

    
    
class UlkeBazindaSevkiyatModel():
    
    ulkeid = 0
    ulkeadi = ''
    toplamsevkiyat = 0