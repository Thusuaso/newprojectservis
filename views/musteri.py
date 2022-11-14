from models import MusterilerModel,MusterilerSchema,UlkeyeGoreMusteriSchema,UlkeyeGoreMusteriModel,UlkeyeGoreMusteriAyrintiSchema,UlkeyeGoreMusteriAyrintiModel
from helpers import SqlConnect


class Musteri:
    def __init__(self):
        self.data = SqlConnect().data

    def getMusteriList(self):

        result = self.data.getList("Select * from MusterilerTB")

        musteriList = list()

        for item in result:

            model = MusterilerModel()

            model.id = item.ID 
            model.firmaAdi = item.FirmaAdi 
            model.ulke = item.Ulke
            model.ulkeId = item.UlkeId 

            musteriList.append(model)

        schema = MusterilerSchema(many=True)

        return schema.dump(musteriList)

    def getUlkeyeGoreMusteriList(self,year):
        try:
            result = self.data.getStoreList("""
                                                select 
                                                    count(m.UlkeId) as SiparisSayisi,
                                                    m.UlkeId as UlkeId,
                                                    (select yu.UlkeAdi from YeniTeklif_UlkeTB yu where yu.Id = m.UlkeId) as UlkeAdi

                                                from MusterilerTB m
                                                    inner join SiparislerTB s on s.MusteriID = m.ID
                                                where YEAR(s.SiparisTarihi) = ?
                                                group by m.UlkeId
                                            
                                            """,(year))
            liste = list()
            for item in result:
                model = UlkeyeGoreMusteriModel()
                model.siparisSayisi = item.SiparisSayisi
                model.ulkeId = item.UlkeId
                model.ulkeAdi = item.UlkeAdi
                liste.append(model)
            schema = UlkeyeGoreMusteriSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getUlkeyeGoreMusteriList',str(e))
            return False
        
    def getUlkeyeGoreMusteriListAyrintiSip(self,year,ulkeId):
        try:
            halihazirdakisip = self.data.getStoreList("""
                                                            select 
                                                                s.SiparisTarihi as SiparisTarihi,
                                                                s.SiparisNo as SiparisNo,
                                                                m.FirmaAdi as FirmaAdi
                                                            from SiparislerTB s
                                                                inner join MusterilerTB m on m.ID = s.MusteriID
                                                            where m.UlkeId=? and YEAR(s.SiparisTarihi) = ? and s.SiparisDurumID=2 
                                                      
                                                      
                                                      """,(ulkeId,year))

            liste = list()
            for item in halihazirdakisip:
                model = UlkeyeGoreMusteriAyrintiModel()
                model.siparisTarihi = item.SiparisTarihi
                model.siparisNo = item.SiparisNo
                model.firmaAdi = item.FirmaAdi
                liste.append(model)

            schema = UlkeyeGoreMusteriAyrintiSchema(many=True)
            return schema.dump(liste)
            
        except Exception as e:
            print('getUlkeyeGoreMusteriListAyrinti',str(e))
            return False
        
    def getUlkeyeGoreMusteriListAyrintiYuk(self,year,ulkeId):
        try:
            yuklenenSip = self.data.getStoreList("""
                                                    select 
                                                                s.SiparisTarihi as SiparisTarihi,
                                                                s.SiparisNo as SiparisNo,
                                                                m.FirmaAdi as FirmaAdi,
                                                                s.YuklemeTarihi as YuklemeTarihi
                                                            from SiparislerTB s
                                                                inner join MusterilerTB m on m.ID = s.MusteriID
                                                            where m.UlkeId=? and YEAR(s.SiparisTarihi) = ? and s.SiparisDurumID=3
                                                 
                                                 
                                                 """,(ulkeId,year))
            liste = list()

            for item2 in yuklenenSip:
                model = UlkeyeGoreMusteriAyrintiModel()
                model.siparisTarihi = item2.SiparisTarihi
                model.siparisNo = item2.SiparisNo
                model.firmaAdi = item2.FirmaAdi
                model.yuklemeTarihi = item2.YuklemeTarihi
                liste.append(model)
            schema = UlkeyeGoreMusteriAyrintiSchema(many=True)
            
            return schema.dump(liste)
            
        except Exception as e:
            print('getUlkeyeGoreMusteriListAyrintiYuk',str(e))
            return False