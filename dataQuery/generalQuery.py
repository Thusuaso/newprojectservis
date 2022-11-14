from helpers.sqlConnect import SqlConnect


class Siparisler(SqlConnect):
    
    #Üretim Listesi
    def getUretimList(self):
        return self.data.getList("Select * from SiparislerTB where SiparisDurumID=2")
    #Bekleyen Listesi
    def getBekleyenList(self):
        return self.data.getList("Select * from SiparislerTB where SiparisDurumID=1")
    #Sevkiyat Listesi
    def getSevkiyatList(self):
        return self.data.getList("Select * from SiparislerTB where SiparisDurumID=3")

class SiparisUrun(SqlConnect):
    
    def __init__(self):
        SqlConnect.__init__(self)
        self.siparisUrunListesi = list()
        dtList =  self.data.getList("Select * from SiparisUrunTB")

        for item in dtList:
            self.siparisUrunListesi.append(item)

    def getSiparisUrunList(self,siparisNo):
        result = filter(lambda x: x.SiparisNo == siparisNo, self.siparisUrunListesi)

        return result


class Musteriler(SqlConnect):

    def __init__(self):
        SqlConnect.__init__(self)

        self.musteriList = list()

        dtList = self.data.getList("Select * from MusterilerTB")

        for item in dtList:
            self.musteriList.append(item)
       

    def getMusteriAdi(self,musteriId):
        musteriAdi = ""
        for item in filter(lambda x: x.ID == musteriId , self.musteriList):
            musteriAdi = item.FirmaAdi
        return musteriAdi


class Tedarikci(SqlConnect):

    def __init__(self):
        SqlConnect.__init__(self)
        self.tedarikciList = list()
        dtList = self.data.getList("Select * from TedarikciTB")

        for item in dtList:
            self.tedarikciList.append(item)

    def getTedarikciAdi(self,id):
    
        tedarikciAdi = ''

        for item in filter(lambda x: x.ID == id, self.tedarikciList):
            tedarikciAdi = item.FirmaAdi
        
        return tedarikciAdi

class UrunKart(SqlConnect):

    def __init__(self):
        SqlConnect.__init__(self)
        self.urunKartList = list()

        dtList = self.data.getList("Select * from UrunKartTB")

        for item in dtList:
            self.urunKartList.append(item)

    def getUrunKart(self,urunKartId):

        return filter(lambda x: x.ID == urunKartId , self.urunKartList) 
    

class Urunler(SqlConnect):
    def getList(self):
        return self.data.getList("Select * from UrunlerTB")


class Olculer(SqlConnect):
    
    def __init__(self):
        SqlConnect.__init__(self)
        self.olcuList = list()
        dtList = self.data.getList("Select * from OlculerTB")

        for item in dtList:
            self.olcuList.append(item)
      
    def getOlcuBilgi(self,urunKartList):
        en = ''
        boy = ''
        kenar = ''
        
        for item in urunKartList:
            olcuId = item.OlcuID            
            for olcu in filter(lambda x: x.ID == olcuId,self.olcuList):
                en = olcu.En
                boy = olcu.Boy
                kenar = olcu.Kenar
            
        return en,boy,kenar


class Uretim(SqlConnect):
    
    def __init__(self):
        SqlConnect.__init__(self)
        self.uretimList = list()
        result = self.data.getList(
            """
            Select u.Miktar,u.UrunKartID,u.SiparisAciklama from UretimTB u,SiparisUrunTB su,SiparislerTB s where 
            u.UrunKartID = su.UrunKartID and u.SiparisAciklama = s.SiparisNo and
            s.SiparisNo = su.SiparisNo and s.SiparisDurumID=2 and u.Miktar is not NULL
            """
        )

        for item in result:
            self.uretimList.append(item)

    def getUretimList(self,siparisNo):    
       
        liste = list()
        result = filter(lambda x: x.SiparisAciklama == siparisNo, self.uretimList)
        for item in result :
            liste.append(item)
        print('Üretim List : ', liste)
        return liste

    def getUretimMiktar(self,uretim_filter):
        miktar = 0

        for item in uretim_filter:
            miktar += item.Miktar
        print('Üretim Miktarı : ', miktar)
        return miktar

class YuzeyIslem(SqlConnect):
    def __init__(self):
        SqlConnect.__init__(self)
        self.yuzeyIslemList = list()
        
        dtList = self.data.getList("Select * from YuzeyKenarTB")

        for item in dtList:
            self.yuzeyIslemList.append(item)

    
    def getYuzeyIslemAdi(self,yuzeyId):

        yuzeyAdi = ''

        for item in filter(lambda x: x.ID == yuzeyId, self.yuzeyIslemList):
            yuzeyAdi = item.YuzeyIslemAdi

        return yuzeyAdi


class Kategori(SqlConnect):

    def __init__(self):
        SqlConnect.__init__(self)

        self.kategoriList = list()

        dtList = self.data.getList("Select * from KategoriTB")

        for item in dtList:
            self.kategoriList.append(item)

    def getKategoriAdi(self,kategoriId):

        kategoriAdi = ''

        for item in filter(lambda x: x.ID == kategoriId,self.kategoriList):
            kategoriAdi = item.KategoriAdi

        return kategoriAdi






#class add