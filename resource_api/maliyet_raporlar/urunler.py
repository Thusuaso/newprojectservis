from helpers import SqlConnect
from models.ozel_maliyet import OzelMaliyetListeModel,TedarikciFaturaSchema,TedarikciFaturaModel
 

class Urunler:

    def __init__(self,yil,ay):

        self.data = SqlConnect().data

        self.dtUrunler = self.data.getStoreList(
            """
            select
            u.SiparisNo,
            u.SatisToplam,
            (u.AlisFiyati * u.Miktar) as AlisToplam,
            u.TedarikciID
            from
            SiparisUrunTB u

            where
            u.SiparisNo in
            (
            Select s.SiparisNo from SiparislerTB s,MusterilerTB m
            where s.MusteriID=m.ID and u.SiparisNo=s.SiparisNo
            and s.SiparisDurumID=3 and m.Marketing='Mekmar'
            and Year(s.YuklemeTarihi)=? 
            and Month(s.YuklemeTarihi)=?
            )

            """,(yil,ay)
        )

        self.dtFaturalar = self.data.getList(

            """
            select * from Tedarikci_Siparis_FaturaTB
            """

        )
        
        self.urunler_listesi = list()

        self.__urunListesiOlustur()
    #Mekmer Id 1 Mekmoz ıd 123

    def __urunListesiOlustur(self):

        for item in self.dtUrunler:

            model = OzelMaliyetListeModel()
            model.siparis_no = item.SiparisNo
            model.dis_alim_fatura_list = self.__getDisAlimFaturaSayisi(item.TedarikciID,item.SiparisNo)
            if item.AlisToplam != None:
                if item.TedarikciID == 1 or item.TedarikciID == 123:
                    if item.TedarikciID == 1:
                        model.mekmar_alim = item.AlisToplam
                        model.mekmar_alim_evrak = self.__getMekmarFatura(item.SiparisNo)
                    if item.TedarikciID == 123:
                        model.mekmoz_alim = item.AlisToplam
                        model.mekmoz_alim_evrak = self.__getMekmozFatura(item.SiparisNo)
                else:
                    model.dis_alim = item.AlisToplam

                    
                    
                model.dis_alim_evrak = self.__getDisFirmaFaturalar(item.SiparisNo,item.TedarikciID)


            if item.SatisToplam != None:
                model.toplam_bedel = item.SatisToplam

            self.urunler_listesi.append(model)
          
    def getUrunModel(self,siparisNo):

        model = OzelMaliyetListeModel()

        for item in self.urunler_listesi:

            if siparisNo == item.siparis_no:
                model.toplam_bedel += item.toplam_bedel
                model.mekmar_alim += item.mekmar_alim
                model.mekmoz_alim += item.mekmoz_alim
                model.dis_alim += item.dis_alim
                #model.mekmar_alim_evrak = item.mekmar_alim_evrak
                #model.mekmoz_alim_evrak = item.mekmoz_alim_evrak
                #model.dis_alim_evrak = item.dis_alim_evrak
                model.dis_alim_fatura_sayisi = item.dis_alim_fatura_sayisi

                

        return model      

    def __getDisAlimFaturaSayisi(self,tedarikci_id,siparis_no):
    
        liste = list()

        for item in self.dtUrunler:
            
            if siparis_no == item.SiparisNo:
                if item.TedarikciID != 1 or item.TedarikciID != 123:
                    liste.append(item)

        return liste

    def __getDisFirmaFaturalar(self,siparis_no,tedarikci_id):

        liste = list()
        id = 1
        for item in self.dtFaturalar:

            if item.SiparisNo == siparis_no and item.TedarikciID == tedarikci_id:
                 model = TedarikciFaturaModel()
                 model.id = id
                 model.link = f"https://file-service.mekmar.com/file/tedarikci/download/30/{siparis_no}/{item.FaturaNo}.pdf"
                 model.evrak_adi = item.FaturaNo
                 liste.append(model)
        
        return liste
    
    def __getMekmarFatura(self,siparis_no):

        link = ''

        for item in self.dtFaturalar:

            if item.TedarikciID == 1 and item.SiparisNo == siparis_no:
                link = f"https://file-service.mekmar.com/file/tedarikci/download/30/{siparis_no}/{item.FaturaNo}.pdf"

        return link

    def __getMekmozFatura(self,siparis_no):

        link = ''

        for item in self.dtFaturalar:

            if item.TedarikciID == 123 and item.SiparisNo == siparis_no:
                link = f"https://file-service.mekmar.com/file/tedarikci/download/30/{siparis_no}/{item.FaturaNo}.pdf"

        return link


class Urunler_Yil:

    def __init__(self,yil):

        self.data = SqlConnect().data

        self.dtUrunler = self.data.getStoreList(
            """
            select
            u.SiparisNo,
            u.SatisToplam,
            (u.AlisFiyati * u.Miktar) as AlisToplam,
            u.TedarikciID
            from
            SiparisUrunTB u

            where
            u.SiparisNo in
            (
            Select s.SiparisNo from SiparislerTB s,MusterilerTB m
            where s.MusteriID=m.ID and u.SiparisNo=s.SiparisNo
            and s.SiparisDurumID=3 and m.Marketing='Mekmar'
            and Year(s.YuklemeTarihi)=?             
            )

            """,(yil)
        )

        self.dtFaturalar = self.data.getList(

            """
            select * from Tedarikci_Siparis_FaturaTB
            """

        )

        self.urunler_listesi = list()

        self.__urunListesiOlustur()
    #Mekmer Id 1 Mekmoz ıd 123

    def __urunListesiOlustur(self):

        for item in self.dtUrunler:

            model = OzelMaliyetListeModel()
            model.siparis_no = item.SiparisNo
            model.dis_alim_fatura_sayisi = self.__getDisAlimFaturaSayisi(item.TedarikciID,item.SiparisNo)            
            if item.AlisToplam != None:
                if item.TedarikciID == 1 or item.TedarikciID == 123:
                    if item.TedarikciID == 1:
                        model.mekmar_alim = item.AlisToplam
                        model.mekmar_alim_evrak = self.__getMekmarFatura(item.SiparisNo)
                    if item.TedarikciID == 123:
                        model.mekmoz_alim = item.AlisToplam
                        model.mekmoz_alim_evrak = self.__getMekmozFatura(item.SiparisNo)
                else:
                    model.dis_alim = item.AlisToplam
                    model.dis_alim_evrak =  self.__getDisFirmaFaturalar(item.SiparisNo,item.TedarikciID)
                    

            if item.SatisToplam != None:
                model.toplam_bedel = item.SatisToplam

            self.urunler_listesi.append(model)
           
    
    def getUrunModel(self,siparisNo):

        model = OzelMaliyetListeModel()

        for item in self.urunler_listesi:
            if siparisNo == item.siparis_no:
                model.toplam_bedel += item.toplam_bedel
                model.mekmar_alim += item.mekmar_alim
                model.mekmoz_alim += item.mekmoz_alim
                model.dis_alim += item.dis_alim
                model.mekmar_alim_evrak = item.mekmar_alim_evrak
                model.mekmoz_alim_evrak = item.mekmoz_alim_evrak
                model.dis_alim_evrak = item.dis_alim_evrak
                model.dis_alim_fatura_sayisi += item.dis_alim_fatura_sayisi

                

        return model 

    def __getDisAlimFaturaSayisi(self,tedarikci_id,siparis_no):

        fatura_sayisi = 0

        for item in self.dtUrunler:
           
            if siparis_no == item.SiparisNo:
                if item.TedarikciID != 1 or item.TedarikciID != 123:

                    fatura_sayisi += 1

        return fatura_sayisi




    def __getDisFirmaFaturalar(self,siparis_no,tedarikci_id):

        liste = list()
        id = 1
       
        for item in self.dtFaturalar:

            if item.SiparisNo == siparis_no and item.TedarikciID == tedarikci_id:
                 model = TedarikciFaturaModel()
                 model.id = id
                 model.link = f"https://file-service.mekmar.com/file/tedarikci/download/30/{siparis_no}/{item.FaturaNo}.pdf"
                 model.evrak_adi = item.FaturaNo
                 liste.append(model)
                 
        
        return liste
    
    def __getMekmarFatura(self,siparis_no):

        link = ''

        for item in self.dtFaturalar:

            if item.TedarikciID == 1 and item.SiparisNo == siparis_no:
                link = f"https://file-service.mekmar.com/file/tedarikci/download/30/{siparis_no}/{item.FaturaNo}.pdf"

        return link

    def __getMekmozFatura(self,siparis_no):

        link = ''

        for item in self.dtFaturalar:

            if item.TedarikciID == 123 and item.SiparisNo == siparis_no:
                link = f"https://file-service.mekmar.com/file/tedarikci/download/30/{siparis_no}/{item.FaturaNo}.pdf"

        return link
    

    
    