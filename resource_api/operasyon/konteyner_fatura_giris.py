from helpers import SqlConnect,DegisiklikMain,MailService
from models.operasyon.konteyner_listesi import *
from resource_api.finans.guncel_kur import DovizListem
import datetime
class KonteynerFaturalar:

    def __init__(self):

        self.data = SqlConnect().data

    
    def getKonteynerList(self):
        
        result = self.data.getList(

            """
            select * from FirmalarTB
            """
        )

        liste = list()
        
        for item in result:
            model = KonteynerIslemModel()
            model.firma_adi = item.FirmaAdi
            model.Firma_id = item.ID  
                      
            liste.append(model)

        schema = KonteynerIslemSchema(many=True)

        return schema.dump(liste)

    def getSiparisList(self):

        result = self.data.getList(

            """
            select SiparisNo from SiparislerTB where year(SiparisTarihi) >= 2020 order by SiparisTarihi desc
            """
        )

        liste = list()

        for item in result:
            model = KonteynerIslemModel()
            
            model.siparisno = item.SiparisNo
          
           

            liste.append(model)

        schema = KonteynerIslemSchema(many=True)

        return schema.dump(liste)   

    def getKonteynerModel(self,urunId):

        result = self.data.getStoreList(

            """
            Select ID from KonteynerDigerFaturalarKayitTB where  FaturaNo=?
            """,(urunId)
        )

        liste = list()

        for item in result:
            model = KonteynerIslemModel()
            
            model.id = item.ID
            liste.append(model)
       
        schema = KonteynerIslemSchema(many=True)
      

        return schema.dump(liste)

    def getFormIslem(self,fatura_id,tur,siparis_no):
         
         result = self.data.getStoreList(
              """
             select 
                f.ID  as dosya_id, 
                f.Tutar , 
                f.SiparisNo ,
                k.FaturaNo ,
                k.Kur ,
				k.ID as fatura_id,
                k.FirmaID,
                f.FaturaKayitID,
                f.SiparisFaturaTurID , 
                f.YuklemeEvrakID,
                (select f.FirmaAdi from FirmalarTB f where f.ID=k.FirmaID) as firma_Adi
                from SiparisFaturaKayitTB f , KonteynerDigerFaturalarKayitTB k 
                where k.FaturaNo + '.pdf'= f.EvrakAdi
                and k.ID = f.FaturaKayitID and k.ID=? and f.SiparisFaturaTurID=? and f.SiparisNo=?
        """,(fatura_id,tur,siparis_no)
         )
         liste = list()

         for item in result :
             model =KonteynerIslemModel()
             model.id = item.fatura_id
             model.dosya_id = item.dosya_id
             model.Firma_id = item.FirmaID
             model.firma_adi = item.firma_Adi
             model.siparisno =  item.SiparisNo
             model.faturaNo = item.FaturaNo
             model.Tutar_tl = item.Kur * item.Tutar
             model.kur = item.Kur
             model.Tutar_dolar = item.Tutar
             

             liste.append(model)
        
         schema =    KonteynerIslemSchema(many=True)
         return schema.dump(liste)

    def konteynerKaydet(self,item):
        forMat = '%d-%m-%Y'
        item['tarih'] = datetime.datetime.strptime(item['tarih'], forMat)
        item['tarih'] = item['tarih'].date()
        try:
            self.data.update_insert(
                """
                INSERT INTO KonteynerDigerFaturalarKayitTB (FirmaID, Tarih, FaturaNo,Kur,KayitTarihi)    values
                (?,?,?,?,?)
                """,(item['Firma_id'],item['tarih'],item['faturaNo'],item['kur'],item['tarih'])
            )
           
            self.__urunId(item)
            
            now = datetime.datetime.now()
            
            self.masraflarSendMail(item,item['siparisno'],now)
            info = 'Huseyin Konteyner Fatura Girişi Yaptı.'
            DegisiklikMain('Huseyin',info)
            return True
        except Exception as e:
            print('konteynerKaydet  Hata : ',str(e))
        return False

    def masraflarSendMail(self,item,siparisNo,nowDate):
        body = """
        <table >
       
            <tr style ="background-color: #f2f2f2;">
                <th style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Sipariş No
                </th>
                <th style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Fatura Detayı
                </th>
                <th style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Fatura No
                </th>
                <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Tutar ($)
                </th>
                 <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 150px;">
                Kur
                </th>
            </tr>
        """
            
        body += f"""
    
        <tr style ="background-color: #ddd;">
            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
            {siparisNo}
            </td>
            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
            {item['fatura_tur_list']['name']}
            </td>
            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
            {item['faturaNo']}
            </td>
            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
            {item['Tutar_dolar']}
            </td>
            <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
            {item['kur']} 
            </td>
            
        </tr>
    
    
        """
            
        body = body + "</table>"
        
        
        MailService(siparisNo + " Sipariş No " + str(nowDate) + ' Tarihinde Konteynır Fatura Girişi', "bilgiislem@mekmar.com",body)
        MailService(siparisNo + " Sipariş No " + str(nowDate) + ' Tarihinde Konteynır Fatura Girişi', "info@mekmar.com",body)
        
        
    def __urunId(self,item):
        
        kontrol = self.data.getStoreList("select count(*) as durum from KonteynerDigerFaturalarKayitTB where FaturaNo=?",item['faturaNo'])[0].durum
       
        urunId = None 
        if kontrol > 0:
            urunId = self.data.getStoreList("Select ID from KonteynerDigerFaturalarKayitTB where  FaturaNo=?",item['faturaNo'])[0].ID 
           
           
            self.getKonteynerModel(item['faturaNo'])
          
        else:
           
         print('urun id çalıştı')

        return item     

    def KonteynerDosyaGuncelle(self , item) :
         try :
           
            evrak = item['faturaNo']+'.pdf'
           
           
            self.data.update_insert(
                """
                  update SiparisFaturaKayitTB  set Tutar=? ,EvrakAdi=?, SiparisNo=?  where  ID=?
                """,
                (
                    item['Tutar_dolar'] ,evrak,item['siparisno'], item['dosya_id']
                )

            )
           
            self.data.update_insert(
                """
                  update KonteynerDigerFaturalarKayitTB  set FirmaID=? ,FaturaNo=?, Kur=?  where  ID=?
                """,
                (item['Firma_id'] ,item['faturaNo'],item['kur'], item['id'])
            )
            return True
         except Exception as e:
            print('Konteyner Dosya Güncelleme Hata : ',str(e))
            return False   

    def KonteynerDosyaKaydet(self,item):
        try:
       
            
            kullaniciid = self.data.getStoreList(
                    """
                    Select ID from KullaniciTB
                    where KullaniciAdi=?
                    """,(item['kullaniciAdi'])
                )[0].ID
           
            if (item['fatura_tur_list']['id'] == 7) : 
                yukleme_evrak = 70
            else :
                yukleme_evrak = 50

                
            forMat = '%d-%m-%Y'
            item['tarih'] = datetime.datetime.strptime(item['tarih'], forMat)
            item['tarih'] = item['tarih'].date()
            self.data.update_insert(
                """
                INSERT INTO SiparisFaturaKayitTB (
                    Tarih,
                    FaturaKayitID,
                    SiparisFaturaTurID, 
                    SiparisNo,
                    Tutar,
                    EvrakDurum,
                    YuklemeEvrakID,
                    YuklemeEvrakDurumID,
                    EvrakYuklemeTarihi,
                    EvrakAdi ,KullaniciID
                    )   
                     values
                    (?,?,?, ?,?,?,?,?,?,?,?)
                """,(item['tarih'],item['urunID'],item['fatura_tur_list']['id'],item['siparisno'],item['Tutar_dolar'],1,yukleme_evrak,2,item['tarih'],item['faturaNo']+'.pdf' , kullaniciid)
            )
            info = 'Huseyin Konteyner Fatura Dosyası Girişi Yaptı.'
            DegisiklikMain('Huseyin',info)
            return True
        except Exception as e:
            print('KonteynerDosyaKaydet Hata : ',str(e))
            return False    

  

   

   
