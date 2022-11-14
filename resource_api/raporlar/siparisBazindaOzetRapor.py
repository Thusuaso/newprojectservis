from helpers import SqlConnect,TarihIslemler
from models.raporlar import SiparisOzetModel,SiparisOzetSchema,SevkiyatOzetSchema,SevkiyatOzetModel,SiparisBazindaOzetModel,SiparisBazindaOzetSchema




class SiparisBazindaOzetRapor:
    
    def __init__(self):

        self.data = SqlConnect().data

    
    def getSiparisBazindaAyListesiBuYil(self):

        result = self.data.getList(
           
          """
             select 

                    Month(s.SiparisTarihi) as AY,
                    sum(u.SatisToplam) as FOB,
                    (
                        sum(u.SatisToplam) + sum(s.NavlunSatis) + sum(s.DetayTutar_1)+ sum(s.DetayTutar_2)+ sum(s.DetayTutar_3)+ sum(s.DetayTutar_4)
                    ) as DDP,

                    sum(u.SatisToplam) - (sum(u.SatisToplam) + sum(s.NavlunSatis) + sum(s.DetayTutar_1)+ sum(s.DetayTutar_2)+ sum(s.DetayTutar_3)+ sum(s.DetayTutar_4)) as FARK



                from 

                SiparisUrunTB u inner join SiparislerTB s on s.SiparisNo = u.SiparisNo

                WHERE YEAR(s.SiparisTarihi) = YEAR(GETDATE()) 

                group by MONTH(s.SiparisTarihi)
                order by Month(s.SiparisTarihi)  
           """
        ) 

        liste = list()

        for item in result:
            model = SiparisBazindaOzetModel()
            model.aylar = item.AY
            model.fob = item.FOB
            model.ddp = item.DDP
            model.fark = item.FARK
            

            liste.append(model)

        schema = SiparisBazindaOzetSchema(many=True)
       
        return schema.dump(liste)

        
    def getSiparisBazindaAyListesiGecenYil(self):

        result = self.data.getList(
           
          """
             select 

                    Month(s.SiparisTarihi) as AY,
                    sum(u.SatisToplam) as FOB,
                    (
                        sum(u.SatisToplam) + sum(s.NavlunSatis) + sum(s.DetayTutar_1)+ sum(s.DetayTutar_2)+ sum(s.DetayTutar_3)+ sum(s.DetayTutar_4)
                    ) as DDP,

                    sum(u.SatisToplam) - (sum(u.SatisToplam) + sum(s.NavlunSatis) + sum(s.DetayTutar_1)+ sum(s.DetayTutar_2)+ sum(s.DetayTutar_3)+ sum(s.DetayTutar_4)) as FARK



                from 

                SiparisUrunTB u inner join SiparislerTB s on s.SiparisNo = u.SiparisNo

                WHERE YEAR(s.SiparisTarihi) = YEAR(GETDATE()) - 1

                group by MONTH(s.SiparisTarihi)
                order by Month(s.SiparisTarihi)  
           """
        ) 

        liste = list()

        for item in result:
            model = SiparisBazindaOzetModel()
            model.aylar = item.AY
            model.fob = item.FOB
            model.ddp = item.DDP
            model.fark = item.FARK
            

            liste.append(model)

        schema = SiparisBazindaOzetSchema(many=True)
       
        return schema.dump(liste)

    
    def getSiparisBazindaAyListesiOncekiYil(self):

        result = self.data.getList(
           
          """
             select 

                    Month(s.SiparisTarihi) as AY,
                    sum(u.SatisToplam) as FOB,
                    (
                        sum(u.SatisToplam) + sum(s.NavlunSatis) + sum(s.DetayTutar_1)+ sum(s.DetayTutar_2)+ sum(s.DetayTutar_3)+ sum(s.DetayTutar_4)
                    ) as DDP,

                    sum(u.SatisToplam) - (sum(u.SatisToplam) + sum(s.NavlunSatis) + sum(s.DetayTutar_1)+ sum(s.DetayTutar_2)+ sum(s.DetayTutar_3)+ sum(s.DetayTutar_4)) as FARK



                from 

                SiparisUrunTB u inner join SiparislerTB s on s.SiparisNo = u.SiparisNo

                WHERE YEAR(s.SiparisTarihi) = YEAR(GETDATE()) - 2

                group by MONTH(s.SiparisTarihi)
                order by Month(s.SiparisTarihi)  
           """
        ) 

        liste = list()

        for item in result:
            model = SiparisBazindaOzetModel()
            model.aylar = item.AY
            model.fob = item.FOB
            model.ddp = item.DDP
            model.fark = item.FARK
            

            liste.append(model)

        schema = SiparisBazindaOzetSchema(many=True)
       
        return schema.dump(liste)
