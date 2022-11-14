from models.temsilciSatislari.temsilciSatislari import *
from helpers import SqlConnect 

class TemsilciSatislari:
    def __init__(self,username):
        self.data = SqlConnect().data
        self.usernameId = self.data.getStoreList("""
                                                    select ID,KullaniciAdi from KullaniciTB where KullaniciAdi =?
                                               """,(username))[0][0]
        self.odemeler = self.data.getList("""
                                                    select 
                                                        sum(o.Tutar) as Tutar,
                                                        o.SiparisNo
                                                    from OdemelerTB o
                                                    group by o.SiparisNo
                                               
                                               """)
        self.navlunveDigerleri = self.data.getList("""
                                                    select NavlunSatis,DetayTutar_1,DetayTutar_2,DetayTutar_3,SiparisNo from SiparislerTB
                                                   
                                                   """)
        self.yuklenmemis = self.data.getStoreList("""
                                            select 

                                                sum(su.SatisToplam) as SatisToplam,
                                                su.SiparisNo,
                                                s.SiparisTarihi,
												s.SiparisSahibi,
												s.Operasyon

                                            from SiparislerTB s 
                                                inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                            where 

                                                 s.SiparisDurumID = 2 and (s.SiparisSahibi=? or s.Operasyon = ?)
                                            group by 
                                                su.SiparisNo,
                                                s.SiparisTarihi,
												s.SiparisSahibi,
												s.Operasyon
                                       
                                       """,(self.usernameId,self.usernameId))
        self.yuklenmemisGelenBedel = self.data.getStoreList("""
                                                                select 
                                                                    s.SiparisTarihi,
                                                                    s.SiparisNo,
                                                                    o.Tutar as YuklenmemisBedel,
                                                                    o.Tarih as GelenBedelTarihi,
                                                                    s.SiparisSahibi,
																	s.Operasyon
                                                                from SiparislerTB s 
                                                                    inner join OdemelerTB o on s.SiparisNo = o.SiparisNo
                                                                where 
                                                                     s.SiparisDurumID = 2 and (s.SiparisSahibi=? or s.Operasyon = ?)
                                                            
                                                            """,(self.usernameId,self.usernameId))
        
        self.yuklenmis = self.data.getStoreList("""
                                            select 

                                            sum(su.SatisToplam) as SatisToplam,
                                            su.SiparisNo,
                                            s.SiparisTarihi,
                                            s.YuklemeTarihi,
                                            s.SiparisSahibi,
                                            s.Operasyon

                                            from SiparislerTB s 
                                            inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo 

                                            where 

                                             s.SiparisDurumID = 3 and (s.SiparisSahibi=? or s.Operasyon = ?)
                                            group by 
                                            su.SiparisNo,
                                            s.SiparisTarihi,
                                            s.YuklemeTarihi,
											s.SiparisSahibi,
											s.Operasyon
                                       
                                       """,(self.usernameId,self.usernameId))
        self.yuklenmisGelenBedel = self.data.getStoreList("""
                                                                select 
										
                                                s.SiparisTarihi,
												s.SiparisNo,
												o.Tutar as YuklenmisBedel,
                                                o.Tarih as GelenBedelTarihi,
                                                s.SiparisSahibi,
                                                s.Operasyon

                                            from SiparislerTB s 
                                                inner join OdemelerTB o on s.SiparisNo = o.SiparisNo

                                            where 

                                                 s.SiparisDurumID = 3 and (s.SiparisSahibi=? or s.Operasyon = ?)
                                                            
                                                            """,(self.usernameId,self.usernameId))
        self.yuklenmemisAylikSiparis = self.data.getStoreList("""
                                                                select 
                                                                sum(su.SatisToplam) as SatisToplamiFob,
                                                                sum(su.Miktar) as SatisMiktari,
                                                                Month(s.SiparisTarihi) as Ay
                                                            from SiparislerTB s
                                                                inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                                            where
                                                                (s.SiparisSahibi = ? or s.Operasyon = ?) and YEAR(s.SiparisTarihi)=2022 and  s.SiparisDurumID=2

                                                            group by 
                                                                MONTH(s.SiparisTarihi)
                                                              
                                                              """,(self.usernameId,self.usernameId))
        self.yuklenmisAylikSiparis = self.data.getStoreList("""
                                                                select 
                                                                sum(su.SatisToplam) as SatisToplamiFob,
                                                                sum(su.Miktar) as SatisMiktari,
                                                                Month(s.SiparisTarihi) as Ay
                                                            from SiparislerTB s
                                                                inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                                            where
                                                                (s.SiparisSahibi = ? or s.Operasyon = ?) and YEAR(s.SiparisTarihi)=2022 and  s.SiparisDurumID=3

                                                            group by 
                                                                MONTH(s.SiparisTarihi)
                                                              
                                                              """,(self.usernameId,self.usernameId))
        self.tamamiAylikSiparis = self.data.getStoreList("""
                                                                select 
                                                                sum(su.SatisToplam) as SatisToplamiFob,
                                                                sum(su.Miktar) as SatisMiktari,
                                                                Month(s.SiparisTarihi) as Ay
                                                            from SiparislerTB s
                                                                inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                                            where
                                                                (s.SiparisSahibi = ? or s.Operasyon = ?) and YEAR(s.SiparisTarihi)=2022

                                                            group by 
                                                                MONTH(s.SiparisTarihi)
                                                              
                                                              """,(self.usernameId,self.usernameId))
    def getTemsilciSiparisleriYuklenmemis(self):
        try:
            
            liste = list()
            for item in self.yuklenmemis:
                model = TemsilciSatislariModel()
                model.siparisTarihi = item.SiparisTarihi
                if self.usernameId == item.SiparisSahibi and self.usernameId != item.Operasyon:
                    model.siparisNo = item.SiparisNo + ' (S)'
                elif self.usernameId == item.Operasyon and self.usernameId != item.SiparisSahibi:
                    model.siparisNo = item.SiparisNo + ' (O)'
                elif self.usernameId == item.SiparisSahibi and self.usernameId == item.Operasyon:
                    model.siparisNo = item.SiparisNo + ' (S&O)'
                
                
                
                model.siparisTotal = item.SatisToplam + self.getTemsilciSiparisleriNavlunveDigerleri(item.SiparisNo)
                model.yuklemeTarihi = 0
                model.gelenOdemeler = self.getTemsilciSiparisleriOdemeler(item.SiparisNo)
                
                liste.append(model)
            schema = TemsilciSatislariSchema(many=True)
            return schema.dump(liste)
                
        except Exception as e:
            print("getTemsilciSiparisleriYuklenmemis hata",str(e))
            return False
    def __noneTypeError(self,value):
        if(value == None):
            return 0
        else:
            return value
    def getTemsilciSiparisleriYuklenmis(self):
        try:
            
            
            
            liste = list()
            
            for item in self.yuklenmis:
                model = TemsilciSatislariModel()

                
                if (item.SatisToplam + self.getTemsilciSiparisleriNavlunveDigerleri(item.SiparisNo) == self.getTemsilciSiparisleriOdemeler(item.SiparisNo)  or ((item.SatisToplam + self.getTemsilciSiparisleriNavlunveDigerleri(item.SiparisNo)) - self.__noneTypeError(self.getTemsilciSiparisleriOdemeler(item.SiparisNo))) < 10 ):
                    continue
                else:
                    model.siparisTarihi = item.SiparisTarihi
                    if self.usernameId == item.SiparisSahibi and self.usernameId != item.Operasyon:
                        model.siparisNo = item.SiparisNo + ' (S)'
                    elif self.usernameId == item.Operasyon and self.usernameId != item.SiparisSahibi:
                        model.siparisNo = item.SiparisNo + ' (O)'
                    elif self.usernameId == item.SiparisSahibi and self.usernameId == item.Operasyon:
                        model.siparisNo = item.SiparisNo + ' (S&O)'
                    model.siparisTotal = item.SatisToplam + self.getTemsilciSiparisleriNavlunveDigerleri(item.SiparisNo)
                    model.yuklemeTarihi = item.YuklemeTarihi
                    model.gelenOdemeler = self.getTemsilciSiparisleriOdemeler(item.SiparisNo)
                    if model.gelenOdemeler == None:
                        model.odenecekKalanBedel = model.siparisTotal
                    else:
                        if model.siparisTotal - model.gelenOdemeler>5:
                            model.odenecekKalanBedel = model.siparisTotal - model.gelenOdemeler
                        
                    if model.odenecekKalanBedel<0:
                        model.background = '#ff8861'
                    elif model.odenecekKalanBedel>0: 
                        model.background = '#70face'
                        

                    
                        
                    liste.append(model)
            schema = TemsilciSatislariSchema(many=True)
            return schema.dump(liste)
                
        except Exception as e:
            print("getTemsilciSiparisleriYuklenmis hata",str(e))
            return False
    def getTemsilciSiparisleriYuklenmemisGelenBedel(self):
        try:
            liste = list()
            for item in self.yuklenmemisGelenBedel:
                model = TemsilciSatislariModel()
                model.siparisTarihi = item.SiparisTarihi
                if self.usernameId == item.SiparisSahibi and self.usernameId != item.Operasyon:
                    model.siparisNo = item.SiparisNo + ' (S)'
                elif self.usernameId == item.Operasyon and self.usernameId != item.SiparisSahibi:
                    model.siparisNo = item.SiparisNo + ' (O)'
                elif self.usernameId == item.SiparisSahibi and self.usernameId == item.Operasyon:
                    model.siparisNo = item.SiparisNo + ' (S&O)'
                model.yuklenmemisGelenBedel = item.YuklenmemisBedel
                model.gelenBedelTarihi = item.GelenBedelTarihi
               
                liste.append(model)
                
                
            
            schema = TemsilciSatislariSchema(many=True)
            
            return schema.dump(liste)

                
        except Exception as e:
            print("getTemsilciSiparisleriYuklenmemisGelenBedel hata",str(e))
            return False
    def getTemsilciSiparisleriYuklenmisGelenBedel(self):
        try:
            liste = list()
            for item in self.yuklenmisGelenBedel:
                model = TemsilciSatislariModel()
                model.siparisTarihi = item.SiparisTarihi
                if self.usernameId == item.SiparisSahibi and self.usernameId != item.Operasyon:
                    model.siparisNo = item.SiparisNo + ' (S)'
                elif self.usernameId == item.Operasyon and self.usernameId != item.SiparisSahibi:
                    model.siparisNo = item.SiparisNo + ' (O)'
                elif self.usernameId == item.SiparisSahibi and self.usernameId == item.Operasyon:
                    model.siparisNo = item.SiparisNo + ' (S&O)'
                model.yuklenmemisGelenBedel = item.YuklenmisBedel
                model.gelenBedelTarihi = item.GelenBedelTarihi
                
                liste.append(model)
                
                
            
            schema = TemsilciSatislariSchema(many=True)
            
            return schema.dump(liste)

                
        except Exception as e:
            print("getTemsilciSiparisleriYuklenmemisGelenBedel hata",str(e))
            return False 
    def getTemsilciAylikYapilanSatislar(self):
        try:
            liste = list()
            
            for item in self.yuklenmemisAylikSiparis:
                model = TemsilciSatislariModel()
                model.ay = self.getMonth(item.Ay)
                model.aylikUretimdekiSiparisBedel = item.SatisToplamiFob
                model.aylikUretimdekiSiparisMiktar = item.SatisMiktari
                liste.append(model)
            schema = TemsilciSatislariSchema(many=True)
            return schema.dump(liste)
                
        except Exception as e:
            print('getTemsilciAylikYapilanSatislar hata',str(e))
            return False
    def getTemsilciAylikYapilanYuklemeler(self):
        try:
            liste = list()
            
            for item in self.yuklenmisAylikSiparis:
                model = TemsilciSatislariModel()
                model.ay = self.getMonth(item.Ay)
                model.aylikUretimdekiSiparisBedel = item.SatisToplamiFob
                model.aylikUretimdekiSiparisMiktar = item.SatisMiktari
                liste.append(model)
            schema = TemsilciSatislariSchema(many=True)
            return schema.dump(liste)
                
        except Exception as e:
            print('getTemsilciAylikYapilanYuklemeler hata',str(e))
            return False
    def getTemsilciAylikTumSiparisler(self):
        try:
            liste = list()
            
            for item in self.tamamiAylikSiparis:
                model = TemsilciSatislariModel()
                model.ay = self.getMonth(item.Ay)
                model.aylikUretimdekiSiparisBedel = item.SatisToplamiFob
                model.aylikUretimdekiSiparisMiktar = item.SatisMiktari
                liste.append(model)
            schema = TemsilciSatislariSchema(many=True)
            return schema.dump(liste)
                
        except Exception as e:
            print('getTemsilciAylikTumSiparisler hata',str(e))
            return False
    
    
    def getMonth(self,month):
        monthList = {
            1:'Ocak',2:'Şubat',3:'Mart',4:'Nisan',5:'Mayıs',6:'Haziran',7:'Temmuz',8:'Ağustos',9:'Eylül',10:'Ekim',11:'Kasım',12:'Aralık'
        }
        return monthList[month]
    
    def getTemsilciSiparisleriOdemeler(self,siparisNo):
        for item in self.odemeler:
            if item.SiparisNo == siparisNo:
                if item.Tutar == None:
                    return 0
                else:
                    return item.Tutar

        
    def getTemsilciSiparisleriNavlunveDigerleri(self,siparisNo):
        for item in self.navlunveDigerleri:
            value = 0
            if item.SiparisNo == siparisNo:
                value = item.NavlunSatis+item.DetayTutar_1+item.DetayTutar_2+item.DetayTutar_3
                if value != None:                    
                    return value
                else:
                    return 0
            
class TemsilciSatislariDetay:
    def __init__(self,username):
        self.data = SqlConnect().data
        self.usernameId = self.data.getStoreList("""
                                                    select ID,KullaniciAdi from KullaniciTB where KullaniciAdi =?
                                               """,(username))[0][0]
    def getSatislarTamamiAylikDetay(self,ay):
        try:
            ay = self.getMonthID(ay)
            satislarAylikTamamiDetay = self.data.getStoreList("""

                                                               select 
                                                                    sum(su.SatisToplam) as SatisToplamiFob,
                                                                    sum(su.Miktar) as SatisMiktari,
                                                                    s.SiparisNo
                                                                    
                                                                from SiparislerTB s
                                                                    inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                                                where
                                                                    (s.SiparisSahibi = ? or s.Operasyon = ?) and YEAR(s.SiparisTarihi)=2022 and MONTH(s.SiparisTarihi)=?

                                                                group by 
                                                                    s.SiparisNo
                                                               
                                                               """,(self.usernameId,self.usernameId,ay))
            liste = list()
            for item in satislarAylikTamamiDetay:
                model = TemsilciSatislariModel()
                model.aylikSiparisTamamiBedel = item.SatisToplamiFob
                model.aylikSiparisTamamiMiktar = item.SatisMiktari
                model.siparisNo = item.SiparisNo
                liste.append(model)
            schema = TemsilciSatislariSchema(many=True)

            return schema.dump(liste)
        except Exception as e:
            print('getSatislarTamamiAylikDetay hata',str(e))
            return False
    
    

    def getMonthID(self,month):
        monthList = {
            'Ocak':1,'Şubat':2,'Mart':3,'Nisan':4,'Mayıs':5,'Haziran':6,'Temmuz':7,'Ağustos':8,'Eylül':9,'Ekim':10,'Kasım':11,'Aralık':12
        }
        return monthList[month]
    
    def getSatislarAylikDetay(self,ay):
        try:
            ay = self.getMonthID(ay)
            satislarAylikTamamiDetay = self.data.getStoreList("""

                                                               select 
                                                                    sum(su.SatisToplam) as SatisToplamiFob,
                                                                    sum(su.Miktar) as SatisMiktari,
                                                                    s.SiparisNo
                                                                    
                                                                from SiparislerTB s
                                                                    inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                                                where
                                                                    (s.SiparisSahibi = ? or s.Operasyon = ?) and YEAR(s.SiparisTarihi)=2022 and MONTH(s.SiparisTarihi)=? and s.SiparisDurumID=2

                                                                group by 
                                                                    s.SiparisNo
                                                               
                                                               """,(self.usernameId,self.usernameId,ay))
            liste = list()
            for item in satislarAylikTamamiDetay:
                model = TemsilciSatislariModel()
                model.aylikSiparisTamamiBedel = item.SatisToplamiFob
                model.aylikSiparisTamamiMiktar = item.SatisMiktari
                model.siparisNo = item.SiparisNo
                liste.append(model)
            schema = TemsilciSatislariSchema(many=True)

            return schema.dump(liste)
        except Exception as e:
            print('getSatislarAylikDetay hata',str(e))
            return False
    
    def getYuklemelerAylikDetay(self,ay):
        try:
            ay = self.getMonthID(ay)
            satislarAylikTamamiDetay = self.data.getStoreList("""

                                                               select 
                                                                    sum(su.SatisToplam) as SatisToplamiFob,
                                                                    sum(su.Miktar) as SatisMiktari,
                                                                    s.SiparisNo
                                                                    
                                                                from SiparislerTB s
                                                                    inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                                                where
                                                                    (s.SiparisSahibi = ? or s.Operasyon = ?) and YEAR(s.SiparisTarihi)=2022 and MONTH(s.SiparisTarihi)=? and s.SiparisDurumID=3

                                                                group by 
                                                                    s.SiparisNo
                                                               
                                                               """,(self.usernameId,self.usernameId,ay))
            liste = list()
            for item in satislarAylikTamamiDetay:
                model = TemsilciSatislariModel()
                model.aylikSiparisTamamiBedel = item.SatisToplamiFob
                model.aylikSiparisTamamiMiktar = item.SatisMiktari
                model.siparisNo = item.SiparisNo
                liste.append(model)
            schema = TemsilciSatislariSchema(many=True)

            return schema.dump(liste)
        except Exception as e:
            print('getSatislarAylikDetay hata',str(e))
            return False
    
            

