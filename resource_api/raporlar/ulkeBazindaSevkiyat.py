from helpers import SqlConnect,TarihIslemler
from models.raporlar import *
from marshmallow import Schema,fields


class UlkeBazindaSevkiyat:
    def __init__(self):

        self.data = SqlConnect().data
        self.masraflar = []
        self.masraflarAyrinti = []

    def getUlkeBazindaSevkiyat(self):
        
        result = self.data.getList("""
                          
                            select 

                            sum(su.SatisToplam) as Sevkiyat,
                            (
                                select yu.UlkeAdi from YeniTeklif_UlkeTB yu where yu.Id = m.UlkeId
                            ) as UlkeAdi,
                            m.UlkeId

                        from MusterilerTB m 
                        inner join SiparislerTB s on s.MusteriID = m.ID
                        inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                        where s.SiparisDurumID=3 and YEAR(s.YuklemeTarihi) = YEAR(GETDATE())

                        group by m.UlkeId
                        order by sum(su.SatisToplam) desc
                          
                          
                          """)
        self.masraflar = self.data.getList("""
                                            select 

                                            sum(s.NavlunSatis) + sum(s.DetayTutar_1) + sum(s.DetayTutar_2) + sum(s.DetayTutar_3) + sum(s.DetayTutar_4) as Masraflar ,
                                            (
                                                select yu.UlkeAdi from YeniTeklif_UlkeTB yu where yu.Id = m.UlkeId
                                            ),
                                            m.UlkeId

                                        from MusterilerTB m 
                                        inner join SiparislerTB s on s.MusteriID = m.ID
                                        where s.SiparisDurumID=3 and YEAR(s.YuklemeTarihi) = YEAR(GETDATE())

                                        group by m.UlkeId
                                        order by sum(s.NavlunSatis),sum(s.DetayTutar_1),sum(s.DetayTutar_2),sum(s.DetayTutar_3),sum(s.DetayTutar_4)
                                           """)
        
        liste = list()
        for item in result:

            model = UlkeBazindaSevkiyatModel()

            model.ulkeid = item.UlkeId
            model.ulkeadi = item.UlkeAdi
            model.toplamsevkiyat = item.Sevkiyat + self.__getMasraflar(item.UlkeId)
            
            
            liste.append(model)

        
        schema = UlkeBazindaSevkiyatSchema(many=True)

        return schema.dump(liste)
    def getUlkeBazindaSevkiyatYear(self,year):
        result = self.data.getStoreList("""
                          
                            select 

                            sum(su.SatisToplam) as Sevkiyat,
                            (
                                select yu.UlkeAdi from YeniTeklif_UlkeTB yu where yu.Id = m.UlkeId
                            ) as UlkeAdi,
                            m.UlkeId

                        from MusterilerTB m 
                        inner join SiparislerTB s on s.MusteriID = m.ID
                        inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                        where s.SiparisDurumID=3 and YEAR(s.YuklemeTarihi) = ? and m.Marketing='Mekmar'

                        group by m.UlkeId
                        order by sum(su.SatisToplam) desc
                          
                          
                          """,(year))
        self.masraflar = self.data.getStoreList("""
                                            select 

                                            sum(s.NavlunSatis) + sum(s.DetayTutar_1) + sum(s.DetayTutar_2) + sum(s.DetayTutar_3) + sum(s.DetayTutar_4) as Masraflar ,
                                            (
                                                select yu.UlkeAdi from YeniTeklif_UlkeTB yu where yu.Id = m.UlkeId
                                            ),
                                            m.UlkeId

                                        from MusterilerTB m 
                                        inner join SiparislerTB s on s.MusteriID = m.ID
                                        where s.SiparisDurumID=3 and YEAR(s.YuklemeTarihi) = ? and m.Marketing='Mekmar'

                                        group by m.UlkeId
                                        order by sum(s.NavlunSatis),sum(s.DetayTutar_1),sum(s.DetayTutar_2),sum(s.DetayTutar_3),sum(s.DetayTutar_4)
                                           """,(year))
        
        liste = list()
        for item in result:

            model = UlkeBazindaSevkiyatModel()

            model.ulkeid = item.UlkeId
            model.ulkeadi = item.UlkeAdi
            model.toplamsevkiyat = item.Sevkiyat +  self.__getMasraflar(item.UlkeId)
            
            
            liste.append(model)

        
        schema = UlkeBazindaSevkiyatSchema(many=True)

        return schema.dump(liste)

    def getUlkeBazindaSevkiyatAyrinti(self,ulkeId,year):
        try:
            result = self.data.getStoreList("""
                                                select 

                                                    sum(su.SatisToplam) as Sevkiyat,
                                                    s.SiparisNo as SiparisNo

                                                from MusterilerTB m 
                                                inner join SiparislerTB s on s.MusteriID = m.ID
                                                inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                                where s.SiparisDurumID=3 and YEAR(s.YuklemeTarihi) = ? and m.UlkeId=? and m.Marketing='Mekmar'
                                                group by s.SiparisNo
                                                order by sum(su.SatisToplam) desc
                                            
                                            
                                            """,(year,ulkeId))
            self.masraflarAyrinti = self.data.getStoreList("""
                                                select 

                                                    s.SiparisNo as SiparisNo,
                                                    s.NavlunSatis,
                                                    s.DetayTutar_1,
                                                    s.DetayTutar_2,
                                                    s.DetayTutar_3,
                                                    s.DetayTutar_4


                                                from MusterilerTB m 
                                                inner join SiparislerTB s on s.MusteriID = m.ID
                                                where s.SiparisDurumID=3 and YEAR(s.YuklemeTarihi) = ? and m.UlkeId=? and m.Marketing='Mekmar'

                                               
                                               """,(year,ulkeId))
            liste = list()
            for item in result:
                model = UlkeBazindaSevkiyatAyrintiModel()
                model.siparisNo = item.SiparisNo
                model.fob = item.Sevkiyat
                navlun,detay1,detay2,detay3,detay4 = self.__getMasraflarAyrinti(item.SiparisNo)
                model.navlun = navlun
                model.detay1 = detay1
                model.detay2 = detay2
                model.detay3 = detay3
                model.detay4 = detay4
                model.ddp = item.Sevkiyat + navlun + detay1 + detay2 + detay3 + detay4
                liste.append(model)
                
            schema = UlkeBazindaSevkiyatAyrintiSchema(many=True)
            return schema.dump(liste)
                
        except Exception as e:
            print("getUlkeBazindaSevkiyatAyrinti hata",str(e))
            return False
    
    def getUlkeBazindaSevkiyatYearsList(self):
        try:
            result = self.data.getList("""
                                    select 

                                        YEAR(YuklemeTarihi) as Year


                                    from SiparislerTB 


                                    group by YEAR(YuklemeTarihi)
                                    order by YEAR(YuklemeTarihi) desc
                              
                              """)
            liste = list()
            for item in result:
                if (item.Year != None):
                    
                    model = UlkeBazindaSevkiyatYearsModel()
                    model.year = item.Year
                    liste.append(model)
            schema = UlkeBazindaSevkiyatYearsSchema(many=True)
            return schema.dump(liste)
                
        except Exception as e:
            print('getUlkeBazindaYears hata',str(e))    
    
    def __getMasraflarAyrinti(self,siparisNo):
        for item in self.masraflarAyrinti:
            if item.SiparisNo != siparisNo:
                continue
            else:
                return self.__none(item.NavlunSatis),self.__none(item.DetayTutar_1),self.__none(item.DetayTutar_2),self.__none(item.DetayTutar_3),self.__none(item.DetayTutar_4)
    
    def __getMasraflar(self,ulkeId):
        for item in self.masraflar:
            if item.UlkeId != ulkeId:
                continue
            else:
                return self.__none(item.Masraflar)
            
            
    def __none(self,value):
        if value == None:
            return 0
        else:
            return value
            

class UlkeBazindaSevkiyatSchema(Schema):
    ulkeid = fields.Integer()
    ulkeadi = fields.String()
    toplamsevkiyat = fields.Integer() 
class UlkeBazindaSevkiyatModel():
    
    ulkeid = 0
    ulkeadi = ''
    toplamsevkiyat = 0
    
    
class UlkeBazindaSevkiyatYearsSchema(Schema):
    year = fields.Int()
    
class UlkeBazindaSevkiyatYearsModel:
    year = 0
    
class UlkeBazindaSevkiyatAyrintiSchema(Schema):
    siparisNo = fields.String()
    fob = fields.Float()
    navlun = fields.Float() 
    detay1 = fields.Float()
    detay2 = fields.Float()
    detay3 = fields.Float()
    detay4 = fields.Float()
    ddp = fields.Float()
class UlkeBazindaSevkiyatAyrintiModel():
    siparisNo = ""
    fob = 0
    navlun = 0
    detay1 = 0
    detay2 = 0
    detay3 = 0
    detay4 = 0
    ddp = 0