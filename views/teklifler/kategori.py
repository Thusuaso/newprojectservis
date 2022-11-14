from models.teklifler import KategoriModel,KategoriSchema,EbatModel,EbatSchema,UrunModel,UrunSchema
from helpers.mongoDb import MongoDb


class Kategori:
    def __init__(self):
        self.data = MongoDb().data

    
    def listeYukle(self):

        result = self.data.kategoris.find({}) 
        
        schema = KategoriSchema(many=True)

        liste = list()
        for item in result:
            kategori = KategoriModel()
            kategori.kategoriAdi = item['kategoriadi_en']
            kategori.id = item['kategori_id']

            kategori.urunler = self.__getUrunList(kategori.id)

            liste.append(kategori)

            

        kategoriSchema =  schema.dump(liste)

        return kategoriSchema

    def __getUrunList(self,kategoriId):
        urunList = list()

        dtUrunList = self.data.products.find({"kategori_id" : kategoriId})

        for item in dtUrunList:
            urun = UrunModel()
            urun.id = item['urunid']
            urun.urunAdi = item['urunadi_en']
            urun.sira = item['sira']
            urun.ebatlar = self.__getEbatList(urun.id)
            urun.yuzeyIslem = self.__getKenarIslem(urun.id)
            urunList.append(urun)

        return urunList

    def __getEbatList(self,urunid):
        liste = list()

        dtEbatList = self.data.ebatlars.find({"urunid" : urunid})

        for item in dtEbatList:
            ebat = EbatModel()
            ebat.ebat = item['ebat']
            ebat.id = item['_id']
            ebat.fiyat = 0
            ebat.birim = ""


            try:
                ebat.fiyat = item['fiyat']
                ebat.birim = item['birim']
            except:
                pass
            ebat.getEbat = ebat.ebat + " - " + str(ebat.fiyat) + "$"
            liste.append(ebat)

        return liste

    def __getKenarIslem(self,urunid):

        kenarislem = self.data.kenarislems.find_one({"urunid" : urunid})

        if kenarislem == None:
            return ""

        return kenarislem['islemadi']


        

        