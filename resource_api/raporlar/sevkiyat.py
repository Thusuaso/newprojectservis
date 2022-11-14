from helpers import SqlConnect
from models.raporlar import *

class Sevkiyat:

    def __init__(self):
        self.data = SqlConnect().data
        self.sevkiyatListe = list()
        self.sevkiyatListeHepsi = list()
        self.grafikMekmarList = list()
        self.grafikHepsiList = list()


    def getSevkiyatMekmarList(self):

        self.__sevkiyatListYukleMekmar()
        yeniList = sorted(self.sevkiyatListe[0:10],key=lambda x:x['miktar'],reverse=True)
        self.__grafikMekmarListYukle(yeniList)
        sevkToplam = 0
        filterToplam = 0
        for item in self.sevkiyatListe:
            sevkToplam += item['miktar']
        for item in yeniList:
            filterToplam += item['miktar']

        fark = sevkToplam - filterToplam

        if fark > 0:

            item = {

                'firma' : '.....',
                'miktar' : fark
            }

            yeniList.append(item)
      
        return sorted(self.__sevkiyatListYukleMekmar(), key=lambda x:x['miktar'],reverse=True)

    def getSevkiyatHepsiList(self):

        self.__sevkiyatYukleHepsi()
        yeniList = sorted(self.sevkiyatListeHepsi[0:10],key=lambda x:x['miktar'],reverse=True)
        self.__grafikHepsiListYukle(yeniList)
        sevkToplam = 0
        filterToplam = 0
        for item in self.sevkiyatListeHepsi:
            sevkToplam += item['miktar']
        for item in yeniList:
            filterToplam += item['miktar']

        fark = sevkToplam - filterToplam

        if fark > 0:

            item = {

                'firma' : '.....',
                'miktar' : fark
            }

            yeniList.append(item)
           
        return  sorted(self.__sevkiyatYukleHepsi(), key=lambda x:x['miktar'],reverse=True)

    def getGrafikMekmarList(self):
        return self.grafikMekmarList

    def getGrafikHepsiList(self):
        return self.grafikHepsiList

    def __grafikMekmarListYukle(self,veri):
        labels = list()
        datasets = list()

        renkler = ['#fffa97','#80daeb','#3c8447','#9ad3be','#ffb5b5','#ff7f50','#a4def5','#cd5c5c','#00bb7e','#2f4860']

        key = 0
        yeniVeri = veri
        #labels.append('Tedarikçiler')
        data = list()
        for item in yeniVeri:
            labels.append(item['firma'])
            data.append(float(item['miktar']))

            key += 1

        dataset = {

            'label' : 'Tedarikçiler',
            'backgroundColor': '#42A5F5',
            'data' : data
        }
        datasets.append(dataset)
        lineData = {

            'labels' : labels,
            'datasets' : datasets
        }

        self.grafikMekmarList = lineData
       
        
    
    def __grafikHepsiListYukle(self,veri):
        labels = list()
        datasets = list()

        renkler = ['#fffa97','#80daeb','#3c8447','#9ad3be','#ffb5b5','#ff7f50','#a4def5','#cd5c5c','#00bb7e','#2f4860']

        key = 0
        yeniVeri = veri
        #labels.append('Tedarikçiler')
        data = list()
        for item in yeniVeri:
            labels.append(item['firma'])
            data.append(float(item['miktar']))

            key += 1

        dataset = {

            'label' : 'Tedarikçiler',
            'backgroundColor': '#42A5F5',
            'data' : data
        }
        datasets.append(dataset)
        lineData = {

            'labels' : labels,
            'datasets' : datasets
        }

        self.grafikHepsiList = lineData

        
    
    def __sevkiyatListYukleMekmar(self):
        
        #sadece mekmar olanlar
        result_1 = self.data.getList(
           
         """
                          select       
            t.FirmaAdi,    
            sum( ub.Miktar) as Miktar,    
            u.AlisFiyati    
       
            from    
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,UretimTB ub,    
            MusterilerTB m    
            where    
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID    
            and s.SiparisDurumID=3    
            and Year(s.YuklemeTarihi)=Year(GetDate())    
            and ub.SiparisAciklama = s.SiparisNo    
            and ub.UrunKartID=u.UrunKartID and t.ID=ub.TedarikciID    
            and m.ID=s.MusteriID     
            and u.UrunBirimID= 1    
             and m.Marketing='Mekmar'  
            group by t.FirmaAdi,u.AlisFiyati    
            order by t.FirmaAdi asc    
         
         """
        )
        liste = list()
        miktartop = 0 
        alistop = 0
        amount = 0
        j = len(result_1)-1
        item = 0
        k = 0 
        m = 0
        while item <= j  :
            model = AnasayfaSevkiyatModel()
            m = 0
            i = 0
            miktartop = 0 
            alistop = 0
            amount = 0
            for item1 in result_1:
                if result_1[i].FirmaAdi == result_1[item].FirmaAdi:  
                    miktartop = miktartop + item1.Miktar
                    if item1.AlisFiyati !=None: 
                     alistop = alistop + item1.AlisFiyati
                     amount = amount + (item1.Miktar * item1.AlisFiyati)
                    else: 
                        item1.AlisFiyati =0
                        alistop = alistop + item1.AlisFiyati
                        amount = amount + (item1.Miktar * item1.AlisFiyati)
                    i +=1
                    m +=1
                else :  i +=1
            model.Firma = result_1[item].FirmaAdi
            model.miktar =miktartop
            model.alis = alistop
            model.total = amount
            item = item + m
            if i <j : i +=1    
            liste.append(model)

        
        schema = AnasayfaSevkiyatSchema(many=True)
        
        return  schema.dump(liste)

        #ilk listenin yüklenmesi
      #  for item in result_1:   
           # veri = {

                  #  'firma' : item.FirmaAdi,
                  #  'miktar' : float(item.Miktar)
                #}
         
      
           # self.sevkiyatListe.append(veri)
    
        result_2 = self.data.getList(  
            """
           select   
            t.FirmaAdi,
            sum( ub.Miktar) as Miktar,
			u.AlisFiyati
			
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,UretimTB ub,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=Year(GetDate())
            and ub.SiparisAciklama = s.SiparisNo
            and ub.UrunKartID=u.UrunKartID and t.ID=ub.TedarikciID
            and m.ID=s.MusteriID 
            and u.UrunBirimID= 1 
            group by t.FirmaAdi,u.AlisFiyati
            order by t.FirmaAdi asc
            """
        )
        liste = list()
        miktartop = 0 
        alistop = 0
        j = len(result_1)-1
        item = 0
        k = 0 
        m = 0
        while item <= j  :
            model = AnasayfaSevkiyatModel()
            m = 0
            i = 0
            miktartop = 0 
            alistop = 0
            for item1 in result_1:
                if result_1[i].FirmaAdi == result_1[item].FirmaAdi:  
                    miktartop = miktartop + item1.Miktar
                    alistop = alistop + item1.AlisFiyati
                    i +=1
                    m +=1
                else :  i +=1
            model.Firma = result_1[item].FirmaAdi
            model.miktar =miktartop
            model.alis = alistop
            item = item + m
            if i <j : i +=1    
            liste.append(model)
        schema = AnasayfaSevkiyatSchema(many=True)
        
        return  schema.dump(liste)
      #  for item in result_2:
           #  veri = {

              #  'firma' : item.FirmaAdi,
              #  'miktar' : float(item.Miktar)
           # }

             #self.__sevkiyatKontrol(veri)

    def __sevkiyatKontrol(self,veri):
        durum = True 

        for item in self.sevkiyatListe:
            if item['firma'] == veri['firma']:
                durum = False
                item['miktar'] += veri['miktar']

        if durum == True:
            self.sevkiyatListe.append(veri)


    def __sevkiyatYukleHepsi(self):
        
        #sadece m2 olanlar
        result_1 = self.data.getList(
               
        """
             select     
            t.FirmaAdi,  
            sum( ub.Miktar) as Miktar,  
             u.AlisFiyati  
     
            from  
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,UretimTB ub,  
            MusterilerTB m  
            where  
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID  
            and s.SiparisDurumID=3  
            and Year(s.YuklemeTarihi)=Year(GetDate())  
            and ub.SiparisAciklama = s.SiparisNo  
            and ub.UrunKartID=u.UrunKartID and t.ID=ub.TedarikciID  
            and m.ID=s.MusteriID   
            and u.UrunBirimID= 1   
            group by t.FirmaAdi,u.AlisFiyati  
            order by t.FirmaAdi asc  
        """
        )
        liste = list()
        miktartop = 0 
        alistop = 0
        j = len(result_1)-1
        item = 0
        k = 0 
        m = 0
        while item <= j  :
            model = AnasayfaHepsiSevkiyatModel()
            m = 0
            i = 0
            amount = 0
            miktartop = 0 
            alistop = 0
            for item1 in result_1:
                if result_1[i].FirmaAdi == result_1[item].FirmaAdi:  
                    miktartop = miktartop + item1.Miktar
                    if item1.AlisFiyati !=None:
                     alistop = alistop + item1.AlisFiyati
                     amount = amount + (item1.Miktar * item1.AlisFiyati)
                    else :  
                       item1.AlisFiyati == 0
                       alistop = alistop + item1.AlisFiyati
                       amount = amount + (item1.Miktar * item1.AlisFiyati)
                    i +=1
                    m +=1
                else :  i +=1
            model.Firma = result_1[item].FirmaAdi
            model.miktar =miktartop
            model.alis = alistop
            model.total = amount
            item = item + m
            if i <j : i +=1    
            liste.append(model)
        schema = AnasayfaHepsiSevkiyatSchema(many=True)
        
        return  schema.dump(liste)
        #ilk listenin yüklenmesi

      #  for item in result_1:

       #     veri = {

                #'firma' : item.FirmaAdi,
                #'miktar' : float(item.Miktar)
           # }

           # self.sevkiyatListeHepsi.append(veri)

        #m2 haricindeki birimlerin alınması
        result_2 = self.data.getList(
            """
            Select   
            t.FirmaAdi,
            Sum(ub.Miktar) as Miktar
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,UretimTB ub,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=3 and u.UrunBirimID != 1
            and Year(s.YuklemeTarihi)=Year(GetDate())
            and ub.OzelMiktar is not null
            and ub.SiparisAciklama = s.SiparisNo
            and ub.UrunKartID=u.UrunKartID and t.ID=ub.TedarikciID
            and m.ID=s.MusteriID 
            group by t.FirmaAdi
            order by Sum(ub.Miktar) desc
            """
        )
        liste = list()
        miktartop = 0 
        alistop = 0
        j = len(result_1)-1
        item = 0
        k = 0 
        m = 0
        while item <= j  :
            model = AnasayfaSevkiyatModel()
            m = 0
            i = 0
            miktartop = 0 
            alistop = 0
            for item1 in result_1:
                if result_1[i].FirmaAdi == result_1[item].FirmaAdi:  
                    miktartop = miktartop + item1.Miktar
                    alistop = alistop + item1.AlisFiyati
                    i +=1
                    m +=1
                else :  i +=1
            model.Firma = result_1[item].FirmaAdi
            model.miktar =miktartop
            model.alis = alistop
            item = item + m
            if i <j : i +=1    
            liste.append(model)
        schema = AnasayfaSevkiyatSchema(many=True)
        
        return  schema.dump(liste)
    #    for item in result_2:
            # veri = {

              #  'firma' : item.FirmaAdi,
               # 'miktar' : float(item.Miktar)
           # }

            # self.__sevkiyatKontrolHepsi(veri)


    def __sevkiyatKontrolHepsi(self,veri):
        durum = True 

        for item in self.sevkiyatListeHepsi:
            if item['firma'] == veri['firma']:
                durum = False
                item['miktar'] += veri['miktar']

        if durum == True:
            self.sevkiyatListeHepsi.append(veri)

    def getSevkiyatAyrintiListYukleMekmar(self,firmaadi):
        
        #sadece mekmar olanlar
        result_1 = self.data.getStoreList(
            """
            select   
            t.FirmaAdi,
            sum( ub.Miktar) as Miktar,
			s.SiparisNo,
			u.AlisFiyati,
			(select ut.BirimAdi from UrunBirimTB ut where ut.ID=u.UrunBirimID) as birim,
		    u.MusteriAciklama
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,UretimTB ub,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=Year(GetDate())
            and ub.SiparisAciklama = s.SiparisNo
            and ub.UrunKartID=u.UrunKartID and t.ID=ub.TedarikciID
            and m.ID=s.MusteriID and m.Marketing in ('Mekmar') 
            and t.FirmaAdi = ?
         
            group by t.FirmaAdi,u.AlisFiyati,s.SiparisNo,u.UrunBirimID, u.MusteriAciklama
            order by  s.SiparisNo asc, birim asc

            """,(firmaadi)
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaAyrintiSevkiyatModel()
            model.aciklama = item.MusteriAciklama
            model.miktar = item.Miktar
            model.alis = item.AlisFiyati
            model.siparis_no = item.SiparisNo
            model.birim = item.birim
            liste.append(model)

         

        
        schema = AnasayfaAyrintiSevkiyatSchema(many=True)
        
        return  schema.dump(liste)

    def getSevkiyatAyrintiListYukleHepsi(self,firmaadi):
        
        #sadece mekmar olanlar
        result_1 = self.data.getStoreList(
            """
            select   
            t.FirmaAdi,
            sum( ub.Miktar) as Miktar,
			s.SiparisNo,
			u.AlisFiyati,
			(select ut.BirimAdi from UrunBirimTB ut where ut.ID=u.UrunBirimID) as birim,
		    u.MusteriAciklama
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,UretimTB ub,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=3
            and Year(s.YuklemeTarihi)=Year(GetDate())
            and ub.SiparisAciklama = s.SiparisNo
            and ub.UrunKartID=u.UrunKartID and t.ID=ub.TedarikciID
            and m.ID=s.MusteriID 
            and t.FirmaAdi = ?
         
            group by t.FirmaAdi,u.AlisFiyati,s.SiparisNo,u.UrunBirimID, u.MusteriAciklama
            order by  s.SiparisNo asc , birim asc

            """,(firmaadi)
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaAyrintiHepsiSevkiyatModel()
            model.aciklama = item.MusteriAciklama
            model.miktar = item.Miktar
            model.alis = item.AlisFiyati
            model.siparis_no = item.SiparisNo
            model.birim = item.birim
            liste.append(model)

         

        
        schema = AnasayfaAyrintiHepsiSevkiyatSchema(many=True)
        
        return  schema.dump(liste)




 
