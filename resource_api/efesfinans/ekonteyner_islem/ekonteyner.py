from resource_api.efesfinans.ekonteyner_islem.esiparisler import Siparisler
from models.efesfinans import EfesFinansAnaSayfaModel,EfesFinansAnaSayfaSchema,EfesFinansGelenOdemelerSchema,EfesFinansGelenOdemelerModel
from resource_api.efesfinans.ekonteyner_islem.eodemeler import EfesOdemeler
from helpers import SqlConnect,TarihIslemler



class EfesKonteyner:

    def __init__(self,yil):

        siparis = Siparisler(yil)

        self.siparis_list = siparis.siparis_list
        self.eski_siparis_list = siparis.eski_siparis_list
        self.pesinat_list = siparis.pesinat_listesi
        self.bekleyen_listesi = siparis.bekleyen_listesi
        self.odeme = EfesOdemeler(yil)


    def getKonteynerList(self):

        groupList = set(map(lambda x:(x['musteriadi'],x['musteriid']),self.siparis_list))
        eski_groupList = set(map(lambda x:(x['musteriadi'],x['musteriid']),self.eski_siparis_list))
        

        liste = list()

        for item in groupList:
            model = self.__getModel(item[0],item[1])
            model.id = item[1] 
            model.musteriadi = item[0]
            
            liste.append(model)
        """
        for item in self.pesinat_list: 

            if self.__getMusteriKontrol(item['musteriid'],liste) == False:
                model = EfesFinansAnaSayfaModel()
                model.id = item['musteriid']
                model.musteriadi = item['musteriadi']
                model.pesinat = item['pesinat']
                model.genel_bakiye = model.pesinat * -1

                liste.append(model)
        """

        for item in eski_groupList:
            if self.__getMusteriKontrol(item[1],liste) == False:
                
                model = self.__getModel_Eski(item[0],item[1])
                model.id = item[1] 
                model.musteriadi = item[0]                 
                liste.append(model)
             
        for item in self.bekleyen_listesi:
            
            if self.__getMusteriKontrol(item['musteriid'],liste) == False:
                model = EfesFinansAnaSayfaModel()
                model.id = item['musteriid']
                model.musteriadi = item['musteriadi']
                model.pesinat = float(item['pesinat'])
                model.genel_bakiye = model.pesinat
                liste.append(model)
        
        
        _liste = list()
        
        
        for item in liste:
            model = self.__getBekleyenPesinat(item)
            if model != None:
                _liste.append(model)
        

        
        
        for item in liste:

            for bekleyen in self.bekleyen_listesi:
                try:
                    if item.id == bekleyen['musteriid']:
                        if item.genel_bakiye < 8:
                            item.pesinat = bekleyen['pesinat']
                            #item.genel_bakiye += item.pesinat
                            
                except Exception as e:
                    print('Bekleyen Listesi Hata : ', bekleyen)
                    print('Hata Kodu : ',str(e))
        

        for item in _liste:
            if self.__getMusteriKontrol(item.id,liste) == False:
                liste.append(item)

        
        for item in liste:

            if item.pesinat > 0:
                item.pesinat = float(item.pesinat) - float(item.eski_pesinat)

            item.bakiye = (float(item.devir + item.ciro) - float(item.odenen))
            pesinatlar = float(item.eski_pesinat) + float(item.pesinat)
            item.genel_bakiye = float(item.bakiye) - pesinatlar
        

        schema = EfesFinansAnaSayfaSchema(many=True)

        return schema.dump(liste)


    def __getBekleyenPesinat(self,data):

        model = None

        for item in self.bekleyen_listesi:
            try:
                if item['musteriid'] == data.id and data.genel_bakiye < 8:
                    model = EfesFinansAnaSayfaModel()
                    model.id = item['musteriid']
                    model.musteriadi = item['musteriadi']
                    model.pesinat = float(item['pesinat'])
                    model.genel_bakiye =  model.pesinat * -1
            except:
                print('__getBekleyenPesinat Hata : ',data)
                

        return model
        


    def __getMusteriKontrol(self,musteriid,liste):

        kontrol = False 

        result = list(filter(lambda x:x.id == musteriid,liste))
       
        if len(result) > 0:
            kontrol = True

        return kontrol



    def __getModel(self,musteriadi,musteriid):
        

        model = EfesFinansAnaSayfaModel()
        ciro = 0
        top = 0
        kalan = 0
        masraf = 0
        for item in self.siparis_list:
            
            if musteriid == item['musteriid']:
                top = float(item['navlunsatis']) + float(item['detaytutar_1']) + float(item['detaytutar_2']) + float(item['detaytutar_3'])  + float(item['urunbedel'])
                ciro +=  (float(item['navlunsatis']) + float(item['detaytutar_1']) + float(item['detaytutar_2']) + float(item['detaytutar_3']) + float(item['urunbedel']))
                if item['Odemeler'] == None :
                   item['Odemeler'] = 0
                if top - item['Odemeler'] > 10 : 
                  masraf +=top
                  kalan += top - item['Odemeler']
                else :
                 masraf = masraf
        model.kapanmayan_siparis = masraf 
        model.kapanmayan_kalan = kalan
                
        model.ciro = ciro
        top = 0
        kalan = 0
        masraf = 0
        for item in self.eski_siparis_list:
            if musteriadi == item['musteriadi']:
                top = float(item['navlunsatis']) + float(item['detaytutar_1']) + float(item['detaytutar_2']) + float(item['detaytutar_3'])  + float(item['urunbedel'])
                model.devir += float(item['navlunsatis']) + float(item['detaytutar_1']) + float(item['detaytutar_2']) + float(item['detaytutar_3']) +  float(item['urunbedel'])
                model.eski_pesinat = self.odeme.getEskiPesinat(musteriid)
                if item['Odemeler'] == None :
                   item['Odemeler'] = 0
                if top - item['Odemeler'] > 10 : 
                  masraf +=top
                  kalan += top - item['Odemeler']
                else :
                 masraf = masraf
        
        model.kapanmayan_siparis += masraf 
        model.kapanmayan_kalan += kalan
        eski_odenen = float(self.odeme.getOdeme_GecenYil(musteriid))
        model.devir = model.devir - eski_odenen
        model.eski_pesinat = self.odeme.getEskiPesinat(musteriid)
        model.odenen = float(self.odeme.getOdeme(musteriid))
        model.pesinat = float(self.odeme.getPesinat(musteriid))
        model.kapanmayan_odenen = model.kapanmayan_siparis - model.kapanmayan_kalan

        #model.bakiye = (float(model.ciro) + float(model.devir) ) - float(model.odenen)
        #model.genel_bakiye = float(model.bakiye) - float(model.pesinat)
        

        return model

    def __getModel_Eski(self,musteriadi,musteriid):
        
        model = EfesFinansAnaSayfaModel()
        top = 0
        kalan = 0
        masraf = 0
        for item in self.eski_siparis_list:
            if musteriadi == item['musteriadi']:
                top = float(item['navlunsatis']) + float(item['detaytutar_1']) + float(item['detaytutar_2']) + float(item['detaytutar_3'])  + float(item['urunbedel'])
                model.devir += item['navlunsatis'] + item['detaytutar_1'] + item['detaytutar_2'] + item['detaytutar_3'] +   item['urunbedel']
                if item['Odemeler'] == None :
                   item['Odemeler'] = 0
                if top - item['Odemeler'] > 10 : 
                  masraf +=top
                  kalan += top - item['Odemeler']
                else :
                 masraf = masraf
        
        model.kapanmayan_siparis = masraf 
        model.kapanmayan_kalan = kalan         
        model.odenen = self.odeme.getOdeme(musteriid)        
        eski_odenen = self.odeme.getOdeme_GecenYil(musteriid)
        model.eski_pesinat = self.odeme.getEskiPesinat(musteriid)
        model.devir = model.devir - eski_odenen 
        model.kapanmayan_odenen = model.kapanmayan_siparis - model.kapanmayan_kalan
        if musteriadi == 'Nijerya-Balogun':
            model.devir = 0
            
        """
        if model.odenen < 0 :
            model.bakiye = model.devir + model.odenen
        else:
            model.bakiye = model.devir - model.odenen
        
        model.genel_bakiye = float(model.bakiye) - float(model.eski_pesinat)
        """

        
      

        return model

class EfesGelenOdemeler:
    def __init__(self):
        self.data = SqlConnect().data
    def getGelenOdemelerList(self):
        liste = list()
        result = self.data.getList("""
                                    select 

                                sum(o.Tutar) as GelenOdeme,
                                YEAR(o.Tarih) as Tarih
                                
                                


                            from SiparislerTB s,OdemelerTB o where s.FaturaKesimTurID=2 and s.SiparisNo=o.SiparisNo
                            group by YEAR(o.Tarih)
                            order by YEAR(o.Tarih) desc    
                        """)
        for item in result:
            model = EfesFinansGelenOdemelerModel()
            model.yil=item.Tarih
            model.gelen_odeme=item.GelenOdeme
            liste.append(model)
        
        schema = EfesFinansGelenOdemelerSchema(many=True)

        return schema.dump(liste)
        
