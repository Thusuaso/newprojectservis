from helpers import SqlConnect
from models.raporlar import *
from flask import jsonify
import math
class CeyreklikRaporlar:
    def __init__(self,year):
        self.sql = SqlConnect().data
        #Yuklemeler
        self.satislar = self.sql.getStoreList("""
                                                select 
                                                    MONTH(s.YuklemeTarihi) as Month,
                                                    sum(su.SatisToplam) as SatisToplami

                                                from SiparislerTB s
                                                    inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo
                                                    inner join MusterilerTB m on m.ID = s.MusteriID

                                                where
                                                    YEAR(s.YuklemeTarihi) = ? and s.SiparisDurumID=3  and m.Marketing='Mekmar'
                                                group by MONTH(s.YuklemeTarihi)
                                                order by MONTH(s.YuklemeTarihi)
                                              
                                              """,(year))
        self.digerler = self.sql.getStoreList("""
                                                select 

                                                sum(s.NavlunSatis) as NavlunSatis,
                                                sum(s.DetayTutar_1) + sum(s.DetayTutar_2) +sum(s.DetayTutar_3) + sum(s.DetayTutar_4) + sum(s.EvrakGideri)  + sum(s.sigorta_Tutar)  as EkTutarlar ,
                                                sum(s.NavlunAlis) as NavlunAlis,
                                                sum(s.DetayAlis_1) + sum(s.DetayAlis_2) + sum(s.DetayAlis_3)   + sum(s.Komisyon) as Masraflar,
                                                MONTH(s.YuklemeTarihi) as Month


                                                from SiparislerTB s
                                                inner join MusterilerTB m on m.ID= s.MusteriID

                                                where
                                                YEAR(s.YuklemeTarihi) = ? and s.SiparisDurumID=3 and m.Marketing='Mekmar'
                                                group by MONTH(s.YuklemeTarihi)
                                                order by MONTH(s.YuklemeTarihi)
                                              
                                              """,(year))
        self.satislarStatistic = self.sql.getStoreList("""
                                                            select 
                                                        MONTH(s.YuklemeTarihi) as Month,
                                                        sum(su.SatisToplam) as SatisToplami,
                                                        su.SiparisNo

                                                        from SiparislerTB s
                                                        inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo
                                                        inner join MusterilerTB m on m.ID=s.MusteriID

                                                        where
                                                        YEAR(s.YuklemeTarihi) = ? and s.SiparisDurumID=3 and m.Marketing='Mekmar'
                                                        group by su.SiparisNo,MONTH(s.YuklemeTarihi)
                                                        order by MONTH(s.YuklemeTarihi)
                                                       
                                                       
                                                       
                                                       """,(year))
        self.digerlerStatistic = self.sql.getStoreList("""
                                                            select 

                                                                s.NavlunSatis as NavlunSatis,
                                                                (s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 + s.DetayTutar_4 + s.EvrakGideri + s.İlaclamaGideri + s.sigorta_Tutar)  as EkTutarlar,
                                                                s.NavlunAlis as NavlunAlis,
                                                                (s.DetayAlis_1 + s.DetayAlis_2 + s.DetayAlis_3  + s.Komisyon) as Masraflar,
                                                                MONTH(s.YuklemeTarihi) as Month,
                                                                s.SiparisNo as SiparisNo


                                                            from SiparislerTB s
																inner join MusterilerTB m on m.ID=s.MusteriID

                                                            where
                                                                YEAR(s.YuklemeTarihi) = ? and s.SiparisDurumID=3 and m.Marketing='Mekmar'
                                                            order by MONTH(s.YuklemeTarihi)
                                                       
                                                       
                                                       """,(year))
        
        #Siparisler
        self.siparisler = self.sql.getStoreList("""
                                                    select 
                                                    MONTH(s.SiparisTarihi) as Month,
                                                    sum(su.SatisToplam) as SatisToplami

                                                from SiparislerTB s
                                                    inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo
                                                    inner join MusterilerTB m on m.ID = s.MusteriID

                                                where
                                                    YEAR(s.SiparisTarihi) = ? and s.SiparisDurumID in (2,3) and m.Marketing='Mekmar'
                                                group by MONTH(s.SiparisTarihi)
                                                order by MONTH(s.SiparisTarihi)
                                                
                                                
                                                """,(year))
        self.digerlerSiparisler = self.sql.getStoreList("""
                                                            select 

                                                sum(s.NavlunSatis) as NavlunSatis,
                                                sum(s.DetayTutar_1) + sum(s.DetayTutar_2) +sum(s.DetayTutar_3) + sum(s.DetayTutar_4) + sum(s.EvrakGideri)  + sum(s.sigorta_Tutar)  as EkTutarlar ,
                                                sum(s.NavlunAlis) as NavlunAlis,
                                                sum(s.DetayAlis_1) + sum(s.DetayAlis_2) + sum(s.DetayAlis_3)   + sum(s.Komisyon) as Masraflar,
                                                MONTH(s.SiparisTarihi) as Month


                                                from SiparislerTB s
                                                inner join MusterilerTB m on m.ID= s.MusteriID

                                                where
                                                YEAR(s.SiparisTarihi) = ? and s.SiparisDurumID in (2,3) and m.Marketing='Mekmar'
                                                group by MONTH(s.SiparisTarihi)
                                                order by MONTH(s.SiparisTarihi)

                                                        
                                                        """,(year))
        self.siparislerStatistic = self.sql.getStoreList("""
                                                            select 
                                                        MONTH(s.SiparisTarihi) as Month,
                                                        sum(su.SatisToplam) as SatisToplami,
                                                        su.SiparisNo

                                                        from SiparislerTB s
                                                        inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo
                                                        inner join MusterilerTB m on m.ID=s.MusteriID

                                                        where
                                                        YEAR(s.SiparisTarihi) = ? and s.SiparisDurumID in (2,3) and m.Marketing='Mekmar'
                                                        group by su.SiparisNo,MONTH(s.SiparisTarihi)
                                                        order by MONTH(s.SiparisTarihi)
                                                         
                                                         
                                                         """,(year))
        self.digerlerStatisticSiparisler = self.sql.getStoreList("""
                                                                 select 

                                                                s.NavlunSatis as NavlunSatis,
                                                                (s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 + s.DetayTutar_4 + s.EvrakGideri + s.İlaclamaGideri + s.sigorta_Tutar)  as EkTutarlar,
                                                                s.NavlunAlis as NavlunAlis,
                                                                (s.DetayAlis_1 + s.DetayAlis_2 + s.DetayAlis_3  + s.Komisyon) as Masraflar,
                                                                MONTH(s.SiparisTarihi) as Month,
                                                                s.SiparisNo as SiparisNo


                                                            from SiparislerTB s
																inner join MusterilerTB m on m.ID=s.MusteriID

                                                            where
                                                                YEAR(s.SiparisTarihi) = ? and s.SiparisDurumID in (2,3) and m.Marketing='Mekmar'
                                                            order by MONTH(s.SiparisTarihi)
                                                                 
                                                                 """,(year))
        
        
        
        self.genelToplamBirinciCeyrek = 0
        self.genelToplamİkinciCeyrek = 0
        self.genelToplamUcuncuCeyrek = 0
        self.genelToplamDorduncuCeyrek = 0
        self.quartersDataOne = []
        self.quartersDataTwo = []
        self.quartersDataThree = []
        self.quartersDataFour = []
        
    def getCeyreklikYear(self):
        try:
            self.genelToplamBirinciCeyrek = 0
            self.genelToplamİkinciCeyrek = 0
            self.genelToplamUcuncuCeyrek = 0
            self.genelToplamDorduncuCeyrek = 0
            self.quartersDataOne = []
            self.quartersDataTwo = []
            self.quartersDataThree = []
            self.quartersDataFour = []
            liste = list()
            for item in self.satislar:
                model = CeyreklikRaporlarModel()
                model.ay = item.Month
                model.ayStr = self.__getMonth(item.Month)
                model.satisToplami = self.__NoneTypeControl(item.SatisToplami)
                navlunSatis,navlunAlis,ekTutarlar,masraflar = self.__digerleri(item.Month)
                model.navlunSatis = self.__NoneTypeControl(navlunSatis)
                model.navlunAlis = self.__NoneTypeControl(navlunAlis)
                model.ekTutarlar = self.__NoneTypeControl(ekTutarlar)
                model.masraflar = self.__NoneTypeControl(masraflar) 
                model.genelToplam = (self.__NoneTypeControl(item.SatisToplami) + self.__NoneTypeControl(navlunSatis) + self.__NoneTypeControl(ekTutarlar)) - (self.__NoneTypeControl(masraflar) + self.__NoneTypeControl(navlunAlis))
                if(item.Month==1 or item.Month ==2 or item.Month == 3):
                    self.quartersDataOne.append(model.genelToplam)
                    self.genelToplamBirinciCeyrek += model.genelToplam
                elif(item.Month==4 or item.Month ==5 or item.Month == 6):
                    self.quartersDataTwo.append(model.genelToplam)
                    
                    self.genelToplamİkinciCeyrek += model.genelToplam
                elif(item.Month==7 or item.Month ==8 or item.Month == 9):
                    self.quartersDataThree.append(model.genelToplam)
                    
                    self.genelToplamUcuncuCeyrek += model.genelToplam
                elif(item.Month==10 or item.Month ==11 or item.Month == 12):
                    self.quartersDataFour.append(model.genelToplam)
                    
                    self.genelToplamDorduncuCeyrek += model.genelToplam
                    
            
                     
                
                liste.append(model)
            
            schema = CeyreklikRaporlarSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getCeyreklikYear hata',str(e))
            return False
  
    
    def getChartModel(self):
            if(self.genelToplamBirinciCeyrek==0):
                labels = ['1.Çeyrek']
            elif self.genelToplamİkinciCeyrek == 0:
                labels = ['1.Çeyrek']
            elif self.genelToplamUcuncuCeyrek == 0:
                labels = ['1.Çeyrek','2.Çeyrek']
            elif self.genelToplamDorduncuCeyrek == 0:
                labels = ['1.Çeyrek','2.Çeyrek','3.Çeyrek']
            else:
                labels = ['1.Çeyrek','2.Çeyrek','3.Çeyrek','4.Çeyrek']
                
            chartData = {
                    'labels':labels,
                    'datasets':[
                        {
                            'data':[int(self.genelToplamBirinciCeyrek),int(self.genelToplamİkinciCeyrek),int(self.genelToplamUcuncuCeyrek),int(self.genelToplamDorduncuCeyrek)],
                            'backgroundColor':["#42A5F5","#66BB6A","#FFA726","#CC0000"],
                            'hoverBackgroundColor':["#64B5F6","#81C784","#FFB74D","#dc4e4e"]
                            
                        }
                    ]
                }

            
            return chartData
    
    def getStatistics(self):
        
        for item in self.satislarStatistic:
            navlunSatis,navlunAlis,ekTutarlar,masraflar = self.__digerleriStatistics(item.SiparisNo)
            genelToplam = (self.__NoneTypeControl(item.SatisToplami) + self.__NoneTypeControl(navlunSatis) + self.__NoneTypeControl(ekTutarlar)) - (self.__NoneTypeControl(masraflar) + self.__NoneTypeControl(navlunAlis))
            if(item.Month==1 or item.Month ==2 or item.Month == 3):
                self.quartersDataOne.append(genelToplam)
            elif(item.Month==4 or item.Month ==5 or item.Month == 6):
                self.quartersDataTwo.append(genelToplam)
                
            elif(item.Month==7 or item.Month ==8 or item.Month == 9):
                self.quartersDataThree.append(genelToplam)
                
            elif(item.Month==10 or item.Month ==11 or item.Month == 12):
                self.quartersDataFour.append(genelToplam)
                
                
        
                    
            
            
        
        
        
        
        
        
        statisticList = list()
        model = QuartersDataStatisticsModel()
        if(self.genelToplamBirinciCeyrek == 0):
            model.ortalamaOne = 0
        else:
            model.ortalamaOne = self.genelToplamBirinciCeyrek / len(self.quartersDataOne)
        if(self.genelToplamİkinciCeyrek == 0):
            model.ortalamaTwo = 0
        else:
            model.ortalamaTwo = self.genelToplamİkinciCeyrek / len(self.quartersDataTwo)
        if(self.genelToplamUcuncuCeyrek == 0):
            model.ortalamaThree = 0
        else:
            model.ortalamaThree = self.genelToplamUcuncuCeyrek / len(self.quartersDataThree)
        if(self.genelToplamDorduncuCeyrek == 0):
            model.ortalamaFour = 0
        else:
            model.ortalamaFour = self.genelToplamDorduncuCeyrek / len(self.quartersDataFour)
            
        # if len(self.quartersDataOne) > 0:
        #     model.medyanOne = self.quartersDataOne.sort()[int(len(self.quartersDataOne) / 2)]
        # if len(self.quartersDataTwo) >0:
        #     model.medyanTwo = self.quartersDataTwo.sort()[int(len(self.quartersDataTwo) / 2)]
        # if len(self.quartersDataThree)>0:
        #     model.medyanThree = self.quartersDataThree.sort()[int(len(self.quartersDataThree) / 2)]
        # if len(self.quartersDataFour) >0:
        #     model.medyanFour = self.quartersDataFour.sort()[int(len(self.quartersDataFour) / 2)]
        
        quartersOneStdTop = 0
        quartersTwoStdTop = 0
        quartersThreeStdTop = 0
        quartersFourStdTop = 0
        
        if len(self.quartersDataOne) == 0:
            model.stdOne = 0
            model.varyansOne = 0
        else:
            for item in self.quartersDataOne:
                quartersOneStdTop += (float(item - model.ortalamaOne) ** 2)
            
            model.varyansOne = quartersOneStdTop / len(self.quartersDataOne)
            model.stdOne = math.sqrt(model.varyansOne)
        
        if len(self.quartersDataTwo) == 0:
            model.stdTwo = 0
            model.varyansTwo = 0
        else:
            for item in self.quartersDataTwo:
                quartersTwoStdTop += (item - model.ortalamaTwo) ** 2
                
            model.varyansTwo = quartersTwoStdTop / len(self.quartersDataTwo)
            model.stdTwo = math.sqrt(model.varyansTwo)
        
        if len(self.quartersDataThree) == 0:
            model.stdThree = 0
            model.varyansThree = 0
        else:
            for item in self.quartersDataThree:
                quartersThreeStdTop += (item - model.ortalamaThree) ** 2
                
            model.varyansThree = quartersThreeStdTop / len(self.quartersDataThree)
            model.stdThree = math.sqrt(model.varyansThree)
        
        if len(self.quartersDataFour) == 0:
            model.stdFour = 0
            model.varyansFour = 0
        else:
            
            for item in self.quartersDataFour:
                quartersFourStdTop += (item - model.ortalamaFour) ** 2
                
            model.varyansFour = quartersFourStdTop / len(self.quartersDataFour)
            model.stdFour = math.sqrt(model.varyansFour)
        
        
        toplamSatisSayisi = len(self.quartersDataOne) + len(self.quartersDataTwo) + len(self.quartersDataThree) + len(self.quartersDataFour)
        if(toplamSatisSayisi != 0):
            
            model.yuzdeOne = (len(self.quartersDataOne) / toplamSatisSayisi) * 100
        else:
            model.yuzdeOne = 0
        if(toplamSatisSayisi != 0):
            
            model.yuzdeTwo = (len(self.quartersDataTwo) / toplamSatisSayisi) * 100
        else:
            model.yuzdeTwo = 0
        
        if(toplamSatisSayisi != 0):
            
            model.yuzdeThree = (len(self.quartersDataThree) / toplamSatisSayisi) * 100
        else:
            model.yuzdeThree = 0
        
        if(toplamSatisSayisi != 0):
            
            model.yuzdeFour = (len(self.quartersDataFour) / toplamSatisSayisi) * 100
        else:
            model.yuzdeFour = 0
            
        
        
        
        
        

        
        
        statisticList.append(model)
        schema = QuartersDataStatisticsSchema(many=True)
        return schema.dump(statisticList)


    def getCeyreklikYearSiparisler(self):
        try:
            self.genelToplamBirinciCeyrek = 0
            self.genelToplamİkinciCeyrek = 0
            self.genelToplamUcuncuCeyrek = 0
            self.genelToplamDorduncuCeyrek = 0
            self.quartersDataOne = []
            self.quartersDataTwo = []
            self.quartersDataThree = []
            self.quartersDataFour = []
            liste = list()
            for item in self.siparisler:
                model = CeyreklikRaporlarModel()
                model.ay = item.Month
                model.ayStr = self.__getMonth(item.Month)
                model.satisToplami = self.__NoneTypeControl(item.SatisToplami)
                navlunSatis,navlunAlis,ekTutarlar,masraflar = self.__digerleriSiparisler(item.Month)
                model.navlunSatis = self.__NoneTypeControl(navlunSatis)
                model.navlunAlis = self.__NoneTypeControl(navlunAlis)
                model.ekTutarlar = self.__NoneTypeControl(ekTutarlar)
                model.masraflar = self.__NoneTypeControl(masraflar) 
                model.genelToplam = (self.__NoneTypeControl(item.SatisToplami) + self.__NoneTypeControl(navlunSatis) + self.__NoneTypeControl(ekTutarlar)) - (self.__NoneTypeControl(masraflar) + self.__NoneTypeControl(navlunAlis))
                if(item.Month==1 or item.Month ==2 or item.Month == 3):
                    self.quartersDataOne.append(model.genelToplam)
                    self.genelToplamBirinciCeyrek += model.genelToplam
                elif(item.Month==4 or item.Month ==5 or item.Month == 6):
                    self.quartersDataTwo.append(model.genelToplam)
                    
                    self.genelToplamİkinciCeyrek += model.genelToplam
                elif(item.Month==7 or item.Month ==8 or item.Month == 9):
                    self.quartersDataThree.append(model.genelToplam)
                    
                    self.genelToplamUcuncuCeyrek += model.genelToplam
                elif(item.Month==10 or item.Month ==11 or item.Month == 12):
                    self.quartersDataFour.append(model.genelToplam)
                    
                    self.genelToplamDorduncuCeyrek += model.genelToplam
                    
            
                     
                
                liste.append(model)
            
            schema = CeyreklikRaporlarSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getCeyreklikYear hata',str(e))
            return False
    
    def getChartModelSiparisler(self):
            if(self.genelToplamBirinciCeyrek==0):
                labels = ['1.Çeyrek']
            elif self.genelToplamİkinciCeyrek == 0:
                labels = ['1.Çeyrek']
            elif self.genelToplamUcuncuCeyrek == 0:
                labels = ['1.Çeyrek','2.Çeyrek']
            elif self.genelToplamDorduncuCeyrek == 0:
                labels = ['1.Çeyrek','2.Çeyrek','3.Çeyrek']
            else:
                labels = ['1.Çeyrek','2.Çeyrek','3.Çeyrek','4.Çeyrek']
                
            chartData = {
                    'labels':labels,
                    'datasets':[
                        {
                            'data':[int(self.genelToplamBirinciCeyrek),int(self.genelToplamİkinciCeyrek),int(self.genelToplamUcuncuCeyrek),int(self.genelToplamDorduncuCeyrek)],
                            'backgroundColor':["#42A5F5","#66BB6A","#FFA726","#CC0000"],
                            'hoverBackgroundColor':["#64B5F6","#81C784","#FFB74D","#dc4e4e"]
                            
                        }
                    ]
                }

            
            return chartData
    
    def getStatisticsSiparisler(self):

        for item in self.siparislerStatistic:
            navlunSatis,navlunAlis,ekTutarlar,masraflar = self.__digerleriStatisticsSiparisler(item.SiparisNo)
            genelToplam = (self.__NoneTypeControl(item.SatisToplami) + self.__NoneTypeControl(navlunSatis) + self.__NoneTypeControl(ekTutarlar)) - (self.__NoneTypeControl(masraflar) + self.__NoneTypeControl(navlunAlis))
            if(item.Month==1 or item.Month ==2 or item.Month == 3):
                self.quartersDataOne.append(genelToplam)
            elif(item.Month==4 or item.Month ==5 or item.Month == 6):
                self.quartersDataTwo.append(genelToplam)
                
            elif(item.Month==7 or item.Month ==8 or item.Month == 9):
                self.quartersDataThree.append(genelToplam)
                
            elif(item.Month==10 or item.Month ==11 or item.Month == 12):
                self.quartersDataFour.append(genelToplam)
                
                
        statisticList = list()
        model = QuartersDataStatisticsModel()
        if(self.genelToplamBirinciCeyrek == 0):
            model.ortalamaOne = 0
        else:
            model.ortalamaOne = self.genelToplamBirinciCeyrek / len(self.quartersDataOne)
        if(self.genelToplamİkinciCeyrek == 0):
            model.ortalamaTwo = 0
        else:
            model.ortalamaTwo = self.genelToplamİkinciCeyrek / len(self.quartersDataTwo)
        if(self.genelToplamUcuncuCeyrek == 0):
            model.ortalamaThree = 0
        else:
            model.ortalamaThree = self.genelToplamUcuncuCeyrek / len(self.quartersDataThree)
        if(self.genelToplamDorduncuCeyrek == 0):
            model.ortalamaFour = 0
        else:
            model.ortalamaFour = self.genelToplamDorduncuCeyrek / len(self.quartersDataFour)
            
        # if len(self.quartersDataOne) > 0:
        #     model.medyanOne = self.quartersDataOne.sort()[int(len(self.quartersDataOne) / 2)]
        # if len(self.quartersDataTwo) >0:
        #     model.medyanTwo = self.quartersDataTwo.sort()[int(len(self.quartersDataTwo) / 2)]
        # if len(self.quartersDataThree)>0:
        #     model.medyanThree = self.quartersDataThree.sort()[int(len(self.quartersDataThree) / 2)]
        # if len(self.quartersDataFour) >0:
        #     model.medyanFour = self.quartersDataFour.sort()[int(len(self.quartersDataFour) / 2)]
        
        quartersOneStdTop = 0
        quartersTwoStdTop = 0
        quartersThreeStdTop = 0
        quartersFourStdTop = 0
        
        if len(self.quartersDataOne) == 0:
            model.stdOne = 0
            model.varyansOne = 0
        else:
            for item in self.quartersDataOne:
                quartersOneStdTop += (float(item - model.ortalamaOne) ** 2)
            
            model.varyansOne = quartersOneStdTop / len(self.quartersDataOne)
            model.stdOne = math.sqrt(model.varyansOne)
        
        if len(self.quartersDataTwo) == 0:
            model.stdTwo = 0
            model.varyansTwo = 0
        else:
            for item in self.quartersDataTwo:
                quartersTwoStdTop += (item - model.ortalamaTwo) ** 2
                
            model.varyansTwo = quartersTwoStdTop / len(self.quartersDataTwo)
            model.stdTwo = math.sqrt(model.varyansTwo)
        
        if len(self.quartersDataThree) == 0:
            model.stdThree = 0
            model.varyansThree = 0
        else:
            for item in self.quartersDataThree:
                quartersThreeStdTop += (item - model.ortalamaThree) ** 2
                
            model.varyansThree = quartersThreeStdTop / len(self.quartersDataThree)
            model.stdThree = math.sqrt(model.varyansThree)
        
        if len(self.quartersDataFour) == 0:
            model.stdFour = 0
            model.varyansFour = 0
        else:
            
            for item in self.quartersDataFour:
                quartersFourStdTop += (item - model.ortalamaFour) ** 2
                
            model.varyansFour = quartersFourStdTop / len(self.quartersDataFour)
            model.stdFour = math.sqrt(model.varyansFour)
        
        
        toplamSatisSayisi = len(self.quartersDataOne) + len(self.quartersDataTwo) + len(self.quartersDataThree) + len(self.quartersDataFour)
        if(toplamSatisSayisi != 0):
            
            model.yuzdeOne = (len(self.quartersDataOne) / toplamSatisSayisi) * 100
        else:
            model.yuzdeOne = 0
        if(toplamSatisSayisi != 0):
            
            model.yuzdeTwo = (len(self.quartersDataTwo) / toplamSatisSayisi) * 100
        else:
            model.yuzdeTwo = 0
        
        if(toplamSatisSayisi != 0):
            
            model.yuzdeThree = (len(self.quartersDataThree) / toplamSatisSayisi) * 100
        else:
            model.yuzdeThree = 0
        
        if(toplamSatisSayisi != 0):
            
            model.yuzdeFour = (len(self.quartersDataFour) / toplamSatisSayisi) * 100
        else:
            model.yuzdeFour = 0
            
        
        
        
        
        

        
        
        statisticList.append(model)
        schema = QuartersDataStatisticsSchema(many=True)
        return schema.dump(statisticList)

    
    
    
    
    


    def __digerleriSiparisler(self,month):
        try:
            for item in self.digerlerSiparisler:
                if(item.Month == month):
                    
                    return self.__NoneTypeControl(item.NavlunSatis),self.__NoneTypeControl(item.NavlunAlis),self.__NoneTypeControl(item.EkTutarlar),self.__NoneTypeControl(item.Masraflar)
                else:
                    continue
        except Exception as e:
            print('__navlun hata',str(e))
            return False






    def __digerleri(self,month):
        try:
            for item in self.digerler:
                if(item.Month == month):
                    
                    return self.__NoneTypeControl(item.NavlunSatis),self.__NoneTypeControl(item.NavlunAlis),self.__NoneTypeControl(item.EkTutarlar),self.__NoneTypeControl(item.Masraflar)
                else:
                    continue
        except Exception as e:
            print('__navlun hata',str(e))
            return False
       
    def __digerleriStatistics(self,siparisNo):
        try:
            for item in self.digerlerStatistic:
                if(item.SiparisNo == siparisNo):
                    
                    return self.__NoneTypeControl(item.NavlunSatis),self.__NoneTypeControl(item.NavlunAlis),self.__NoneTypeControl(item.EkTutarlar),self.__NoneTypeControl(item.Masraflar)
                else:
                    return 0,0,0,0
        except Exception as e:
            print('__navlun hata',str(e))
            return False
        
    def __digerleriStatisticsSiparisler(self,siparisNo):
        try:
            
            for item in self.digerlerStatisticSiparisler:
                if(item.SiparisNo == siparisNo):
                    return self.__NoneTypeControl(item.NavlunSatis),self.__NoneTypeControl(item.NavlunAlis),self.__NoneTypeControl(item.EkTutarlar),self.__NoneTypeControl(item.Masraflar)
                else:
                    return 0,0,0,0
        except Exception as e:
            print('__navlun hata',str(e))
            return False
      
       
       
        
    def __getMonth(self,month):
        monthList = {
            1:'Ocak',2:'Şubat',3:'Mart',4:'Nisan',5:'Mayıs',6:'Haziran',7:'Temmuz',8:'Ağustos',9:'Eylül',10:'Ekim',11:'Kasım',12:'Aralık'
        }
        return monthList[month]
        
    def __NoneTypeControl(self,val):
        if(val == None):
            return 0
        else:
            return val


