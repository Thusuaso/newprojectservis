from helpers import SqlConnect
from models import istatistiklerModel,istatistiklerSchema
import datetime
class Istatistikler:
    def __init__(self):
        self.data = SqlConnect().data
        self.nowSql = """
                            select 
                                count(s.MusteriID) as SumOrder,
                                (select m.FirmaAdi from MusterilerTB m where m.ID = s.MusteriID) as Customer,
                                (select yu.UlkeAdi from YeniTeklif_UlkeTB yu where yu.Id = s.UlkeId) as Country,
                                s.MusteriID as MusteriID
                            from 

                                SiparislerTB s


                            where
                                YEAR(s.SiparisTarihi) = ?
                            group by
                                YEAR(s.SiparisTarihi),s.MusteriID,s.UlkeId
                        """
        self.date = datetime.datetime.now()
        self.nowDate = self.date.year
        self.now = self.data.getStoreList(self.nowSql,(self.nowDate))
        self.oneYearAgo = self.data.getStoreList(self.nowSql,(self.nowDate - 1))
        self.twoYearAgo = self.data.getStoreList(self.nowSql,(self.nowDate - 2))
        self.threeYearAgo = self.data.getStoreList(self.nowSql,(self.nowDate - 3))
        
    def getNewCustomerDataList(self):
        newCustomerNow = list()
        oldCustomerNow =list()
        newCustomerOneYearAgo = list()
        oldCustomerOneYearAgo = list()
        newCustomerTwoYearAgo = list()
        oldCustomerTwoYearAgo = list()
        newCustomerThreeYearAgo = list()
        oldCustomerThreeYearAgo = list()
        for item in self.now:
            if(self.getTwoYearCustomerControl(item.Customer) or self.getThreeYearCustomerControl(item.Customer) or self.getOneYearCustomerControl(item.Customer)):
                oldCustomerNow.append({'sumOrder':item.SumOrder,'musteriAdı':item.Customer,'ulke':item.Country})
            
            else:
                newCustomerNow.append({'sumOrder':item.SumOrder,'musteriAdı':item.Customer,'ulke':item.Country})
        
        for item in self.oneYearAgo:
            if(self.getNowCustomerControl(item.Customer) or self.getThreeYearCustomerControl(item.Customer) or self.getTwoYearCustomerControl(item.Customer)):
                 oldCustomerOneYearAgo.append({'sumOrder':item.SumOrder,'musteriAdı':item.Customer,'ulke':item.Country})

            else:
                 newCustomerOneYearAgo.append({'sumOrder':item.SumOrder,'musteriAdı':item.Customer,'ulke':item.Country})

        for item in self.twoYearAgo:
            if(self.getNowCustomerControl(item.Customer) or self.getOneYearCustomerControl(item.Customer) or self.getThreeYearCustomerControl(item.Customer)):
                 oldCustomerTwoYearAgo.append({'sumOrder':item.SumOrder,'musteriAdı':item.Customer,'ulke':item.Country})

            else:
                 newCustomerTwoYearAgo.append({'sumOrder':item.SumOrder,'musteriAdı':item.Customer,'ulke':item.Country})
        
        for item in self.threeYearAgo:
            if(self.getNowCustomerControl(item.Customer) or self.getOneYearCustomerControl(item.Customer) or self.getTwoYearCustomerControl(item.Customer)):
                 newCustomerThreeYearAgo.append({'sumOrder':item.SumOrder,'musteriAdı':item.Customer,'ulke':item.Country})

            else:
                 oldCustomerThreeYearAgo.append({'sumOrder':item.SumOrder,'musteriAdı':item.Customer,'ulke':item.Country})
        customerData = {
            'newCustomerNow':newCustomerNow,
            'oldCustomerNow':oldCustomerNow,
            'newCustomerOneYearAgo' : newCustomerOneYearAgo,
            'oldCustomerOneYearAgo' : oldCustomerOneYearAgo,
            'newCustomerTwoYearAgo' : newCustomerTwoYearAgo,
            'oldCustomerTwoYearAgo' : oldCustomerTwoYearAgo,
            'newCustomerThreeYearAgo' : newCustomerThreeYearAgo,
            'oldCustomerThreeYearAgo' : oldCustomerThreeYearAgo
        }
        return customerData

    
        
    
    
    def getNowCustomerControl(self,customerID):
        for item in self.now:
            if item.Customer == customerID:
                return True 
    def getOneYearCustomerControl(self,customerID):
        for item in self.oneYearAgo:
            if item.Customer == customerID:
                return True 
    def getTwoYearCustomerControl(self,customerID):
        for item in self.twoYearAgo:
            if item.Customer == customerID:
                return True
    def getThreeYearCustomerControl(self,customerID):
        for item in self.threeYearAgo:
            if item.Customer == customerID:
                return True 
    
        
        