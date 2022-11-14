from helpers import SqlConnect,TarihIslemler
from models.raporlar import *
from marshmallow import Schema,fields
class MusBazYilAyrinti:

    def __init__(self):

        self.data = SqlConnect().data
        self.subatSiparisler = []
    
    def getMusSipAyrinti(self,yil,ay):
        resultSatis = self.data.getStoreList(
            """
            select 

                sum(su.SatisToplam) as FOB,
                (select FirmaAdi from MusterilerTB m where m.ID = su.musteriID) as FirmaAdi,
                (select ID from MusterilerTB m where m.ID = su.musteriID) as FirmaID

            from 

                SiparisUrunTB su,SiparislerTB s ,MusterilerTB m

            where 
                su.SiparisNo = s.SiparisNo	and YEAR(s.SiparisTarihi) = ? and MONTH(s.SiparisTarihi) = ? and m.ID = s.MusteriID and m.Marketing='Mekmar'

            group by 
                su.musteriID
            

            """,(yil,ay)
        )
        resultNavlun = self.data.getStoreList(
            """
            select 

                (select FirmaAdi from MusterilerTB m where m.ID = s.MusteriID) as FirmaAdi,
                (select ID from MusterilerTB m where m.ID = s.MusteriID) as FirmaID,
                sum(s.NavlunSatis) as Navlun,
                sum(s.DetayTutar_1) as DETAY1,
                sum(s.DetayTutar_2) as DETAY2,
                sum(s.DetayTutar_3) as DETAY3,
                sum(s.DetayTutar_4) as DETAY4
                

            from 
                SiparislerTB s,MusterilerTB m

            where
                YEAR(s.SiparisTarihi) = ? and MONTH(s.SiparisTArihi) = ? and m.ID = s.MusteriID and m.Marketing='Mekmar'

            group by s.MusteriID
            

            """,(yil,ay)
        )
        
        result = zip(resultSatis,resultNavlun)
        
        
        liste = list()
        for item in result:

            model = MusteriBazindaOzetModel()

            model.musteri = item[0][1]
            model.navlun = item[1][2]
            model.detay1= item[1][3]
            model.detay2 = item[1][4]
            model.detay3 = item[1][5]
            model.detay4 = item[1][6]
            model.fob = item[0][0]
            model.ddp = item[0][0] +  item[1][2] + item[1][3] + item[1][4] +  item[1][5] + item[1][6]
            
            
            liste.append(model)

        
        schema = MusteriBazindaOzetSchema(many=True)

        return schema.dump(liste)
 
    def getMusSipAyrintiToplami(self,yil,ay):
        resultSatis = self.data.getStoreList(
            """
            select 

                sum(su.SatisToplam) as FOB,
                (select FirmaAdi from MusterilerTB m where m.ID = su.musteriID) as FirmaAdi,
                (select ID from MusterilerTB m where m.ID = su.musteriID) as FirmaID

            from 

                SiparisUrunTB su,SiparislerTB s ,MusterilerTB m

            where 
                su.SiparisNo = s.SiparisNo	and YEAR(s.SiparisTarihi) = ? and MONTH(s.SiparisTarihi) <= ? and m.ID = s.MusteriID and m.Marketing='Mekmar'

            group by 
                su.musteriID
            

            """,(yil,ay)
        )
        resultNavlun = self.data.getStoreList(
            """
            select 

                (select FirmaAdi from MusterilerTB m where m.ID = s.MusteriID) as FirmaAdi,
                (select ID from MusterilerTB m where m.ID = s.MusteriID) as FirmaID,
                sum(s.NavlunSatis) as Navlun,
                sum(s.DetayTutar_1) as DETAY1,
                sum(s.DetayTutar_2) as DETAY2,
                sum(s.DetayTutar_3) as DETAY3,
                sum(s.DetayTutar_4) as DETAY4
                

            from 
                SiparislerTB s,MusterilerTB m

            where
                YEAR(s.SiparisTarihi) = ? and MONTH(s.SiparisTArihi) <= ? and m.ID = s.MusteriID and m.Marketing='Mekmar'

            group by s.MusteriID
            

            """,(yil,ay)
        )
        SiparisToplami = zip(resultSatis,resultNavlun)
        liste = list()
        for item in SiparisToplami:

            model = MusteriBazindaOzetModel()

            model.musteri = item[0][1]
            model.navlun = item[1][2]
            model.detay1= item[1][3]
            model.detay2 = item[1][4]
            model.detay3 = item[1][5]
            model.detay4 = item[1][6]
            model.fob = item[0][0]
            model.ddp = item[0][0] +  item[1][2] + item[1][3] + item[1][4] +  item[1][5] + item[1][6]
            
            
            liste.append(model)

        
        schema = MusteriBazindaOzetSchema(many=True)

        return schema.dump(liste)
    
    def getMusteriBazindaSiparisAyrintiBuYil(self):
        resultFOB = self.data.getList(
            """
            select 
                sum(su.SatisToplam) as FOB,
                MONTH(s.SiparisTarihi) as AY
            from 
                SiparisUrunTB su,SiparislerTB s ,MusterilerTB m

            where
                su.SiparisNo = s.SiparisNo and YEAR(s.SiparisTarihi) = YEAR(GETDATE()) and su.musteriID = m.ID and m.Marketing = 'Mekmar'

            group by 
                MONTH(s.SiparisTarihi)
            

            """
        )
        resultNavlun = self.data.getList(
            """
            select 
                sum(s.NavlunSatis) as Navlun,
                sum(s.DetayTutar_1) as DETAY1,
                sum(s.DetayTutar_2) as DETAY2,
                sum(s.DetayTutar_3) as DETAY3,
                sum(s.DetayTutar_4) as DETAY4,

                MONTH(s.SiparisTarihi) as AY
            from 
                SiparislerTB s ,MusterilerTB m

            where
                YEAR(s.SiparisTarihi) = YEAR(GETDATE()) and s.musteriID = m.ID and m.Marketing = 'Mekmar'

            group by 
                MONTH(s.SiparisTarihi)
            

            """
        )
        
        result = zip(resultFOB,resultNavlun)
        liste = list()

        for item in result:

            model = MusteriBazindaOzetModel()

            model.ay = item[0][1]
            model.fob = item[0][0]
            model.ddp = item[0][0] + item[1][0] + item[1][1] + item[1][2] + item[1][3] + item[1][4]
            model.fark = item[1][0] + item[1][1] + item[1][2] + item[1][3] + item[1][4]
            
            
            liste.append(model)


        schema = MusteriBazindaOzetSchema(many=True)

        return schema.dump(liste)


    
class MusteriBazindaOzetSchema(Schema):
    ay = fields.String()
    fob = fields.Integer()
    ddp = fields.Integer()
    musteri = fields.String()
    navlun = fields.Integer()
    detay1 = fields.Integer()
    detay2 = fields.Integer()
    detay3 = fields.Integer()
    detay4 = fields.Integer()
    fark = fields.Integer()
    
    
class MusteriBazindaOzetModel():
    ay=''
    fob = 0
    ddp = 0
    musteri = ""
    navlun=0
    detay1=0
    detay2=0
    detay3=0
    detay4=0
    fark=0