from marshmallow import Schema,fields

from dataQuery.generalQuery import Siparisler,SiparisUrun,Musteriler,Tedarikci,UrunKart,Urunler,Olculer,Uretim

import helpers.dateConvert as dateConvert
import helpers.metotSure as metotSure

from models.siparisler import SiparislerSchema

class SiparisListeViews:
    
    """
    rapor_tipi 3 parametre alacak
    ***uretim***
    ***bekleyen***
    ***sevk***
    """
    @metotSure.sure_hesapla_Kwargs
    def __init__(self,rapor_tipi):

        if rapor_tipi == "uretim":
            self.dtSiparisList = Siparisler().getUretimList()

        if rapor_tipi == "bekleyen":
            self.dtSiparisList = Siparisler().getBekleyenList()
        if rapor_tipi == "sevk":
            self.dtSiparisList = Siparisler().getSevkiyatList()
        
        self.dtSiparisUrun = SiparisUrun()
        self.dtMusteri = Musteriler()
        self.dtUrunKart = UrunKart()
        self.urunList = Urunler().getList()
        self.dtOlcu = Olculer()
        self.dtTedarikci = Tedarikci()
        self.dtUretim = Uretim()

        self.siparisListesi = list()
        
    @metotSure.sure_hesapla_Args
    def loadList(self):
       sira = 1
       for sp in self.dtSiparisList:

           siparis = {
               "siparisNo" : sp.SiparisNo,
               "siparisTarihi" : dateConvert.getDate(sp.SiparisTarihi),
               "musteriAdi" : self.dtMusteri.getMusteriAdi(sp.MusteriID),
               "sure" : 0,
               "sira" : sira,
               "siparisUrunler" : list()
            }
           uretimList = self.dtUretim.getUretimList(sp.SiparisNo)
           for ur in self.dtSiparisUrun.getSiparisUrunList(sp.SiparisNo):

               uretim_filter = filter(lambda x: x.UrunKartID == ur.UrunKartID, uretimList)
               urunKartSingleList = self.dtUrunKart.getUrunKart(ur.UrunKartID)

               en,boy,kenar = self.dtOlcu.getOlcuBilgi(urunKartSingleList)
              
               siparisUrun = {
                   "uretimAciklama" : ur.UretimAciklama,
                   "tedarikciAdi" : self.dtTedarikci.getTedarikciAdi(ur.TedarikciID),
                    "urun" : {
                          "en" : en,
                          "boy" : boy,
                          "kenar" : kenar
                    },
                   "birimFiyat" : float(ur.SatisFiyati),
                   "toplamTutar" : float(ur.SatisToplam),                
                   "uretimMiktari" : float(self.dtUretim.getUretimMiktar(uretim_filter))
                   
               }
               siparis['siparisUrunler'].append(siparisUrun)
           
           self.siparisListesi.append(siparis)

           sira = sira + 1
    
    def getJsonList(self):
        schema = SiparislerSchema(many=True)
        
        jsonList = schema.dump(self.siparisListesi)

        return jsonList
       
          

            








        

