from helpers import SqlConnect
from models.raporlar import SiparisMasrafSchema,SiparisMasrafModel


class SiparisMasraf:

    def __init__(self):
        self.data = SqlConnect().data
        self.firmalar = self.data.getList("Select * from FirmalarTB")
        self.digerFaturalar = self.data.getList("Select * from KonteynerDigerFaturalarKayitTB")
        self.nakliyeFaturalar = self.data.getList("Select * from NakliyeFaturaKayitTB")
        self.evrakListesi = self.data.getList("Select * from YuklemeEvraklarTB")
        self.iscilikListesi = self.data.getList("Select * from SiparisEkstraGiderlerTB")
      
      
    
    def getMasrafListesi(self,siparisNo):
        masraflar = list()
        result = self.data.getStoreList(
           """   
               select *from
                (
                SELECT  sf.siparisNo, sf.Tutar as tut,sf.SiparisFaturaTurID ,sf.Aciklama ,sf.FaturaKayitID  FROM SiparisFaturaKayitTB sf where sf.Tutar>0
              
                )
                SiparisFaturaKayitTB where   SiparisFaturaKayitTB.SiparisNo=?

        
           """



            , (siparisNo))
        result2 = self.data.getStoreList(

            """
             select * ,(Select t.FirmaAdi from TedarikciTB t where t.ID=f.TedarikciID )  as firma
              from SiparisEkstraGiderlerTB f
               where f.SiparisNo=?
          
            """,(siparisNo)
        )
        for item in result2:
              model = SiparisMasrafModel()
              model.tur = "Özel İşçilik"
              model.aciklama = item.firma
              model.tutar = item.Tutar
              masraflar.append(model)
        for item in result:
            model = SiparisMasrafModel()
          
           
            if item.SiparisFaturaTurID == 73:
                model.tur = "İlaçlama Faturası"
                model.tutar = item.tut
                model.aciklama = self.__getFirmaAdi(item.FaturaKayitID)
            if item.SiparisFaturaTurID == 7:
                model.tutar = item.tut
                model.tur = "Gümrük Faturası"
                model.aciklama = self.__getFirmaAdi(item.FaturaKayitID)
            if item.SiparisFaturaTurID == 11:
                model.tutar = item.tut
                model.tur = "Nakliye Faturası"
                model.aciklama = self.__getNakliyeFirmaAdi(item.FaturaKayitID)
                
            if item.SiparisFaturaTurID == 13:
                model.tutar = item.tut
                model.tur = "Navlun"
                model.aciklama = self.__getFirmaAdi(item.FaturaKayitID)
            if item.SiparisFaturaTurID == 9:
                model.tutar = item.tut
                model.tur = "Liman Masrafı"
                model.aciklama = self.__getFirmaAdi(item.FaturaKayitID)
            masraflar.append(model)

      
        schema = SiparisMasrafSchema(many=True)
        
        return schema.dump(masraflar)
            


    def __getFirmaAdi(self,faturaId):
        firmaId = None
        for item in filter(lambda x: x.ID == faturaId,self.digerFaturalar):
            firmaId = item.FirmaID
        
        firmaAdi = ''
        for item in filter(lambda x:x.ID == firmaId,self.firmalar):
            firmaAdi = item.FirmaAdi
        return firmaAdi

   

  

     
      
     

    def __getNakliyeFirmaAdi(self,faturaId):
        firmaId = None
        for item in filter(lambda x: x.ID == faturaId,self.nakliyeFaturalar):
            firmaId = item.FirmaID
        
        firmaAdi = ''
        for item in filter(lambda x:x.ID == firmaId,self.firmalar):
            firmaAdi = item.FirmaAdi
        return firmaAdi
    
    def __getEvrakAdi(self,evrakId):

        evrakAdi = ''
        for item in filter(lambda x: x.ID == evrakId,self.evrakListesi):
            evrakAdi = item.Aciklama
        
        return evrakAdi

    
        
        
            
            
        




    