from helpers import SqlConnect
from models.raporlar.logs import LogsMaliyetSchema,LogsMaliyetModel
from models.raporlar.anaSayfaDegisiklik import AnaSayfaDegisiklikSchema,AnaSayfaDegisiklikModel

class LogsMaliyet:
    def __init__(self):
        self.data = SqlConnect().data
        
    def getLogsMaliyet(self,year):
        try:
            result = self.data.getStoreList("""
                                                select 


                                                *,
                                                YEAR(DegisiklikTarihi) as Year,
                                                Month(DegisiklikTarihi) as Month,
                                                Day(DegisiklikTarihi) as Day


                                            from MaliyetAnaliziDegisikliklerTB
                                            where YEAR(DegisiklikTarihi) = ?
											order by DegisiklikTarihi desc
                                       
                                       """,(year))
            
            liste = list()
            for item in result:
                model = LogsMaliyetModel()
                model.id = item.ID
                model.kayit_tarihi = item.DegisiklikTarihi
                model.siparis_no = item.SiparisNo
                model.yukleme_tarihi = item.YuklemeTarihi
                model.info = item.IslemAdi
                model.kayit_kisi = item.DegisiklikYapan
                model.yil = item.Year
                model.ay = item.Month
                model.gun = item.Day
                liste.append(model)
            schema = LogsMaliyetSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getLogsMaliyet',str(e))
            return False
        
    def getAnaSayfaDegisiklikAll(self,year):
        try:
            result = self.data.getStoreList("""
                                        select										
                                            DegisiklikYapan,
                                            YapılanDegisiklik,
                                            DegisiklikTarihi,
                                            YEAR(DegisiklikTarihi) as Year,
                                            Month(DegisiklikTarihi) as Month,
                                            Day(DegisiklikTarihi) as Day
                                        from AnaSayfaYapılanDegisiklikler
										where YEAR(DegisiklikTarihi) =?
                                        order by ID desc
                                       
                                       """,(year))
            
            liste = list()
            for item in result:
                model = AnaSayfaDegisiklikModel()
                model.degisiklikYapan = item.DegisiklikYapan
                model.yapilanDegisiklik = item.YapılanDegisiklik
                model.year = item.Year
                model.month = item.Month
                model.day = item.Day
                liste.append(model)
                
            schema = AnaSayfaDegisiklikSchema(many=True)

            return schema.dump(liste)
        
        except Exception as e:
            print("getAnaSayfaDegisiklik hata",str(e))
            return False
    
    def getYearList(self):
        try:
            result = self.data.getList("""
                                       select										
                                            YEAR(DegisiklikTarihi) as Year
                                        from AnaSayfaYapılanDegisiklikler
                                        group by Year(DegisiklikTarihi)
                                        order by YEAR(DegisiklikTarihi)  desc
                                       """)
            liste = list()
            for item in result:
                model = AnaSayfaDegisiklikModel()
                model.year = item.Year
                liste.append(model)
                
            schema = AnaSayfaDegisiklikSchema(many=True)

            return schema.dump(liste)
        except Exception as e:
            print('__getYear hata',str(e))
            return False
    
   