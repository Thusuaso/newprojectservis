from helpers import SqlConnect,TarihIslemler
from models.efesfinans.efes_gelen_yuklenen import *
import datetime
class EfesGelenvYuklenen:
    def __init__(self):
        self.data = SqlConnect().data
        self.tumSatislar = self.data.getList("""
                                                        select

                                                            sum(su.SatisToplam) as SatisToplami,
                                                            YEAR(s.SiparisTarihi) as Yil
                                                            
                                                        from
                                                            SiparislerTB s
                                                            inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                                        where
                                                             s.FaturaKesimTurID=2

                                                        group by
                                                            YEAR(s.SiparisTarihi)
                                                            
                                                        order by
                                                            YEAR(s.SiparisTarihi) desc

                                                      
                                                      """)
        self.yuklenmemisSatislar = self.data.getList("""
                                            select

                                                sum(su.SatisToplam) as SatisToplami,
                                                YEAR(s.SiparisTarihi) as Yil
                                                
                                            from
                                                SiparislerTB s
                                                inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                            where
                                                 s.FaturaKesimTurID=2 and s.SiparisDurumID=2

                                            group by
                                                YEAR(s.SiparisTarihi)
                                       
                                       """)
        self.yuklenmisSatislar = self.data.getList("""
                                                    select

                                                        sum(su.SatisToplam) as SatisToplami,
                                                        YEAR(s.YuklemeTarihi) as Yil
                                                        
                                                    from
                                                        SiparislerTB s
                                                        inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo

                                                    where
                                                         s.FaturaKesimTurID=2 and s.SiparisDurumID=3

                                                    group by
                                                        YEAR(s.YuklemeTarihi)
                                                 """)
        self.yuklenmisSatislarNavlun = self.data.getList("""
                                                            select sum(s.NavlunSatis) as Navlun,
                                                            YEAR(s.YuklemeTarihi) as Yil
                                                            from 
                                                            SiparislerTB s 
                                                            where  
                                                            s.FaturaKesimTurID=2 and 
                                                            s.SiparisDurumID=3 
                                                            group by YEAR(s.YuklemeTarihi)
                                                        
                                                        """)
        self.tumSatislarNavlun = self.data.getList("""
                                                        select sum(s.NavlunSatis) as Navlun,
                                                            YEAR(s.SiparisTarihi) as Yil
                                                            from 
                                                            SiparislerTB s 
                                                            where  
                                                            s.FaturaKesimTurID=2 and YEAR(s.SiparisTarihi) >=2020
                                                            group by YEAR(s.SiparisTarihi)
                                                   """)
    def getEfesGelenvYuklenen(self):
        try:
            liste = list()
            for item in self.tumSatislar:
                
                model = EfesGelenYuklenenModel()
                model.yil = item.Yil
                model.tumSatislarFob = item.SatisToplami
                model.tumSatislar = item.SatisToplami + self.getTumSatislarNavlun(item.Yil)
                if model.yil == datetime.datetime.now().year:
                    model.tahminiTumSatislar = (model.tumSatislar / datetime.datetime.now().month) * 12
                else:
                    model.tahminiTumSatislar = model.tumSatislar
                
                    
                
                model.yuklenmemisSatislar = self.getYuklenmemisSatislar(item.Yil)
                model.yuklenmisSatislar = self.getYuklenmisSatislar(item.Yil) + self.getYuklenmisSatislarNavlun(item.Yil)
                if model.yuklenmisSatislar == None:
                    model.yuklenmemisSatislar = 0
                model.yil=item.Yil
                liste.append(model)
            schema = EfesGelenYuklenenSchema(many=True)
            return schema.dump(liste)
            

        except Exception as e:
            print('getEfesGelenvYuklenen hata',str(e))
        
    def getYuklenmemisSatislar(self,yil):
        for item in self.yuklenmemisSatislar:
            if item.Yil == yil:
                return item.SatisToplami
            
    def getYuklenmisSatislar(self,yil):
        for item in self.yuklenmisSatislar:
            if item.Yil == yil:
                return item.SatisToplami
            
    def getYuklenmisSatislarNavlun(self,yil):
        for item in self.yuklenmisSatislarNavlun:
            if item.Yil == yil:
                return item.Navlun
            
    def getTumSatislarNavlun(self,yil):
        for item in self.tumSatislarNavlun:
            if item.Yil == yil:
                return item.Navlun