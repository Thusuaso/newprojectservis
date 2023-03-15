from helpers import SqlConnect,TarihIslemler,MailService
from models.raporlar import *
from models.operasyon import *
import datetime


class Uretim:

    def __init__(self):
        self.data = SqlConnect().data
        self.uretimListe = list()
        self.uretimListeHepsi = list()
        self.musteriListMekmar = list()
        self.musteriListHepsi = list()
        

    def getUretimMekmarList(self):

        self.__uretimListYukleMekmar()
        yeniList = sorted(self.uretimListe[0:10],key=lambda x:x['miktar'],reverse=True)
        uretimToplam = 0
        filterToplam = 0
        for item in self.uretimListe:
            uretimToplam += item['miktar']

        for item in yeniList:
            filterToplam += item['miktar']

        fark = uretimToplam - filterToplam
        if fark > 0:
            item = {
                'firma' : '.....',
                'miktar' : fark
            }
            yeniList.append(item)
        return  sorted(self.__uretimListYukleMekmar(), key=lambda x:x['miktar'],reverse=True)

    def getUretimHepsiList(self):

        self.__uretimListYukleHepsi()
        yeniList = sorted(self.uretimListeHepsi[0:10],key=lambda x:x['miktar'],reverse=True)
        uretimToplam = 0
        filterToplam = 0
        for item in self.uretimListeHepsi:
            uretimToplam += item['miktar']

        for item in yeniList:
            filterToplam += item['miktar']

        fark = uretimToplam - filterToplam
        if fark > 0:
            item = {
                'firma' : '.....',
                'miktar' : fark
            }
            yeniList.append(item)
        return  sorted(self.__uretimListYukleHepsi(), key=lambda x:x['miktar'],reverse=True)

    def getMusteriUretimMekmarList(self):

        #liste yükle
        self.__uretimListMusteriMekmar()

        yeniList = sorted(self.musteriListMekmar[0:10],key=lambda x: x['miktar'],reverse=True)

        toplam = 0
        filterToplam = 0

        for item in self.musteriListMekmar:
            toplam += item['miktar']

        for item in yeniList:
            filterToplam += item['miktar']

        fark = toplam - filterToplam 

        if fark > 0:
            item = {
                'firma' : '.....',
                'miktar' : fark
            }

            yeniList.append(item)

        return  sorted(self.__uretimListMusteriMekmar(), key=lambda x:x['miktar'],reverse=True)

    def getMusteriUretimHepsiList(self):

        #liste yükle
        self.__uretimListMusteriHepsi()

        yeniList = sorted(self.musteriListHepsi[0:10],key=lambda x: x['miktar'],reverse=True)

        toplam = 0
        filterToplam = 0

        for item in self.musteriListHepsi:
            toplam += item['miktar']

        for item in yeniList:
            filterToplam += item['miktar']

        fark = toplam - filterToplam 

        if fark > 0:
            item = {
                'firma' : '.....',
                'miktar' : fark
            }

            yeniList.append(item)

        return  sorted(self.__uretimListMusteriHepsi(), key=lambda x:x['miktar'],reverse=True)
    
    def __uretimListYukleMekmar(self):
        
        #sadece m2 olanlar
        result_1 = self.data.getList(
             """ 
            select     
            t.FirmaAdi,  
            Sum(u.Miktar) as Miktar,  
            u.AlisFiyati  
            from  
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,  
            MusterilerTB m  
            where  
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID  
            and s.SiparisDurumID=2 and u.UrunBirimID=1  
            
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID  
            and Year(s.SiparisTarihi)=Year(GetDate())  
            and m.ID=s.MusteriID and m.Marketing in ('Mekmar')  
            group by t.FirmaAdi,u.AlisFiyati  
            order by  t.FirmaAdi asc  

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
            model = AnasayfaUreticiModel()
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
                    else :
                      item1.AlisFiyati = 0  
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

        
        schema = AnasayfaUreticiSchema(many=True)
        
        return  schema.dump(liste)

        #ilk listenin yüklenmesi

     #   for item in result_1:

          #  veri = {

              #  'firma' : item.FirmaAdi,
             #   'miktar' : float(item.Miktar)
            #}

         #   self.uretimListe.append(veri)

        #m2 haricindeki birimlerin alınması
        result_2 = self.data.getList(
            """
            Select   
            t.FirmaAdi,
            Sum(u.Miktar) as Miktar
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=2 and u.UrunBirimID != 1
            and u.OzelMiktar is not null
           
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID
            and m.ID=s.MusteriID and m.Marketing in ('Mekmar','BD','SU')
            group by t.FirmaAdi
           
            """
        )

        for item in result_2:
             veri = {

                'firma' : item.FirmaAdi,
                'miktar' : float(item.Miktar)
            }

             self.__uretimListKontrol(veri)

    def __uretimListKontrol(self,veri):
        durum = True 

        for item in self.uretimListe:
            if item['firma'] == veri['firma']:
                durum = False
                item['miktar'] += veri['miktar']

        if durum == True:
            self.uretimListe.append(veri)


    def __uretimListYukleHepsi(self):
        
        #sadece m2 olanlar
        result_1 = self.data.getList(
            """ 
             select     
            t.FirmaAdi,  
            Sum(u.Miktar) as Miktar,  
            u.AlisFiyati  
            from  
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,  
            MusterilerTB m  
            where  
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID  
            and s.SiparisDurumID=2 and u.UrunBirimID=1  
             
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID  
            and Year(s.SiparisTarihi)=Year(GetDate())  
            and m.ID=s.MusteriID   
            group by t.FirmaAdi,u.AlisFiyati  
            order by  t.FirmaAdi asc  

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
            model = AnasayfaHepsiUreticiModel()
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
                    else :
                      item1.AlisFiyati = 0    
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

        
        schema = AnasayfaHepsiUreticiSchema(many=True)
        
        return  schema.dump(liste)


        #ilk listenin yüklenmesi

       # for item in result_1:

         #   veri = {

            #    'firma' : item.FirmaAdi,
            #    'miktar' : float(item.Miktar)
       #     }

          #  self.uretimListeHepsi.append(veri)

        #m2 haricindeki birimlerin alınması
        result_2 = self.data.getList(
            """
            Select   
            t.FirmaAdi,
            Sum(u.Miktar) as Miktar
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=2 and u.UrunBirimID != 1
            and u.OzelMiktar is not null
         
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID
            and m.ID=s.MusteriID 
            group by t.FirmaAdi
            order by Sum(u.Miktar) desc
            """
        )

        for item in result_2:
             veri = {

                'firma' : item.FirmaAdi,
                'miktar' : float(item.Miktar)
            }

             self.__uretimListKontrolHepsi(veri)


    def __uretimListKontrolHepsi(self,veri):
        durum = True 

        for item in self.uretimListeHepsi:
            if item['firma'] == veri['firma']:
                durum = False
                item['miktar'] += veri['miktar']

        if durum == True:
            self.uretimListeHepsi.append(veri)

    def __uretimListMusteriMekmar(self):
         #sadece m2 olanlar
        result_1 = self.data.getList(
             """ 
                  select     
                m.FirmaAdi,  
                Sum(u.Miktar) as Miktar,  
               u.AlisFiyati  
                from  
                SiparislerTB s,SiparisUrunTB u,TedarikciTB t,  
                MusterilerTB m  
                where  
                s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID  
                and s.SiparisDurumID=2 and u.UrunBirimID=1  
                
               and Year(s.SiparisTarihi)=Year(GetDate())  
                and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID  
                and m.ID=s.MusteriID   
                and m.Marketing ='Mekmar'  
                group by m.FirmaAdi,u.AlisFiyati  
                order by    m.FirmaAdi asc  
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
            model = AnasayfaMusteriModel()
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
                    else :  
                         item1.AlisFiyati = 0 
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

        
        schema = AnasayfaMusteriSchema(many=True)
        
        return  schema.dump(liste)
        #ilk listenin yüklenmesi

      #  for item in result_1:

        #    veri = {

            #    'firma' : item.FirmaAdi,
            #    'miktar' : float(item.Miktar)
           # }

           # self.musteriListMekmar.append(veri)

        #m2 haricindeki birimlerin alınması
        result_2 = self.data.getList(
            """
            Select   
            m.FirmaAdi,
            Sum(u.Miktar) as Miktar
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=2 and u.UrunBirimID != 1
            and u.OzelMiktar is not null
          
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID
            and m.ID=s.MusteriID and m.Marketing in ('Mekmar','BD','SU')
            group by m.FirmaAdi
            order by Sum(u.Miktar) desc
            """
        )

        for item in result_2:
             veri = {

                'firma' : item.FirmaAdi,
                'miktar' : float(item.Miktar)
            }

             self.__musteriListMekmarKontrol(veri)

    def __musteriListMekmarKontrol(self,veri):
        durum = True 

        for item in self.musteriListMekmar:
            if item['firma'] == veri['firma']:
                durum = False
                item['miktar'] += veri['miktar']

        if durum == True:
            self.musteriListMekmar.append(veri)


    def __uretimListMusteriHepsi(self):
         #sadece m2 olanlar
        result_1 = self.data.getList(
           """ 
            select     
            m.FirmaAdi,  
            Sum(u.Miktar) as Miktar,  
            u.AlisFiyati  
            from  
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,  
            MusterilerTB m  
            where  
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID  
            and s.SiparisDurumID=2 and u.UrunBirimID=1  
           
           and Year(s.SiparisTarihi)=Year(GetDate())  
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID  
            and m.ID=s.MusteriID   
            group by m.FirmaAdi,u.AlisFiyati  
            order by    m.FirmaAdi asc  
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
            model = AnasayfaHepsiModel()
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
                        item1.AlisFiyati = 0
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

        
        schema = AnasayfaHepsiMusteriSchema(many=True)
        
        return  schema.dump(liste)
        #ilk listenin yüklenmesi

       # for item in result_1:

           # veri = {

              #  'firma' : item.FirmaAdi,
             #   'miktar' : float(item.Miktar)
         #  }

            #self.musteriListHepsi.append(veri)

        #m2 haricindeki birimlerin alınması
        result_2 = self.data.getList(
            """
            Select   
            m.FirmaAdi,
            Sum(u.Miktar) as Miktar
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=2 and u.UrunBirimID != 1
            and u.OzelMiktar is not null
            
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID
            and m.ID=s.MusteriID and m.Marketing in ('Mekmar','BD','SU','Ghana','İç Piyasa')
            group by m.FirmaAdi
            order by Sum(u.Miktar) desc
            """
        )

        for item in result_2:
             veri = {

                'firma' : item.FirmaAdi,
                'miktar' : float(item.Miktar)
            }

             self.__musteriListHepsiKontrol(veri)

    def __musteriListHepsiKontrol(self,veri):
        durum = True 

        for item in self.musteriListHepsi:
            if item['firma'] == veri['firma']:
                durum = False
                item['miktar'] += veri['miktar']

        if durum == True:
            self.musteriListHepsi.append(veri)

    def getUretimAyrintiListYukleMekmar(self,firmaadi):
        
        #sadece mekmar olanlar
        result_1 = self.data.getStoreList(
            """
             select   
            t.FirmaAdi,
            Sum(u.Miktar) as Miktar,
			s.SiparisNo,
            u.AlisFiyati,
			(select ut.BirimAdi from UrunBirimTB ut where ut.ID = u.UrunBirimID) as birim,
			u.MusteriAciklama
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=2 
            
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID
			 and Year(s.SiparisTarihi)=Year(GetDate())
            and m.ID=s.MusteriID and m.Marketing in ('Mekmar')
			and t.FirmaAdi=?
            group by t.FirmaAdi,u.AlisFiyati,u.MusteriAciklama,s.SiparisNo,u.UrunBirimID
            order by  t.FirmaAdi asc , birim asc

            """,(firmaadi)
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaAyrintiUretimModel()
            model.aciklama = item.MusteriAciklama
            model.miktar = item.Miktar
            model.alis = item.AlisFiyati
            model.siparis_no = item.SiparisNo
            model.birim = item.birim
            liste.append(model)

         

        
        schema = AnasayfaAyrintiUretimSchema(many=True)
        
        return  schema.dump(liste)

    def getUretimAyrintiListYukleHepsi(self,firmaadi):
        
        #sadece mekmar olanlar
        result_1 = self.data.getStoreList(
            """
             select   
            t.FirmaAdi,
            Sum(u.Miktar) as Miktar,
			s.SiparisNo,
            u.AlisFiyati,
			(select ut.BirimAdi from UrunBirimTB ut where ut.ID = u.UrunBirimID) as birim,
			u.MusteriAciklama
            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=2
          
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID
			and Year(s.SiparisTarihi)=Year(GetDate())
            and m.ID=s.MusteriID 
			and t.FirmaAdi=?
            group by t.FirmaAdi,u.AlisFiyati,u.MusteriAciklama,s.SiparisNo,u.UrunBirimID
            order by  t.FirmaAdi asc, birim asc

            """,(firmaadi)
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaAyrintiHepsiUretimModel()
            model.aciklama = item.MusteriAciklama
            model.miktar = item.Miktar
            model.alis = item.AlisFiyati
            model.siparis_no = item.SiparisNo
            model.birim = item.birim
            liste.append(model)

         

        
        schema = AnasayfaAyrintiHepsiUretimSchema(many=True)
       
        return  schema.dump(liste)

    def getMusteriAyrintiListYukleMekmar(self,firmaadi):
        
        #sadece mekmar olanlar
        result_1 = self.data.getStoreList(
            """
            select   
            m.FirmaAdi,
            Sum(u.Miktar) as Miktar,
			u.AlisFiyati,
			s.SiparisNo,
			 u.MusteriAciklama,
			(select ut.BirimAdi from UrunBirimTB ut where ut.ID=u.UrunBirimID) as birim

            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=2 
            
		    and Year(s.SiparisTarihi)=Year(GetDate())
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID
            and m.ID=s.MusteriID 
            and m.Marketing ='Mekmar'
			and m.FirmaAdi =?
            group by m.FirmaAdi,u.AlisFiyati,s.SiparisNo,u.UrunBirimID,u.MusteriAciklama
            order by  m.FirmaAdi asc , birim asc

            """,(firmaadi)
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaAyrintiMusteriModel()
            model.aciklama = item.MusteriAciklama
            model.miktar = item.Miktar
            model.alis = item.AlisFiyati
            model.siparis_no = item.SiparisNo
            model.birim = item.birim
            liste.append(model)

         

        
        schema = AnasayfaAyrintiMusteriSchema(many=True)
        
        return  schema.dump(liste)

    def getMusteriAyrintiListYukleHepsi(self,firmaadi):
        
        #sadece mekmar olanlar
        result_1 = self.data.getStoreList(
            """
            select   
            m.FirmaAdi,
            Sum(u.Miktar) as Miktar,
			u.AlisFiyati,
			s.SiparisNo,
			 u.MusteriAciklama,
			(select ut.BirimAdi from UrunBirimTB ut where ut.ID=u.UrunBirimID) as birim

            from
            SiparislerTB s,SiparisUrunTB u,TedarikciTB t,
            MusterilerTB m
            where
            s.SiparisNo=u.SiparisNo and u.TedarikciID=t.ID
            and s.SiparisDurumID=2 
          
		    and Year(s.SiparisTarihi)=Year(GetDate())
            and u.UrunKartID=u.UrunKartID and t.ID=u.TedarikciID
            and m.ID=s.MusteriID 
           
			and m.FirmaAdi =?
            group by m.FirmaAdi,u.AlisFiyati,s.SiparisNo,u.UrunBirimID,u.MusteriAciklama
            order by  m.FirmaAdi asc,birim asc

            """,(firmaadi)
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiAyrintiMusteriModel()
            model.aciklama = item.MusteriAciklama
            model.miktar = item.Miktar
            model.alis = item.AlisFiyati
            model.siparis_no = item.SiparisNo
            model.birim = item.birim
            liste.append(model)
  
        schema = AnasayfaHepsiAyrintiMusteriSchema(many=True)
        
        return  schema.dump(liste) 

    def getGelenSipYilListYukleHepsi(self):
        
        
        result_1 = self.data.getList(
            """
            SELECT  
             s.SiparisTarihi,  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
             
            s.YuklemeTarihi,  
             YEAR(s.SiparisTarihi) as yil ,  
             Month(s.SiparisTarihi) as ay,  
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.SiparisTarihi) =  Year(GetDate())  
              
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID )  
            and Month(s.SiparisTarihi) < Month(GetDate())  
  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID, s.YuklemeTarihi  
            order by s.SiparisTarihi desc  
            """
        )
        liste = list()
        a = 0
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
                  
            else:          
                model.tarih = item.SiparisTarihi
                model.siparisNo = item.SiparisNo
                model.musteriadi = item.musteri
                model.satistoplam = item.SatisToplam
                model.navlun = item.NavlunSatis
                model.detay1 = item.DetayTutar_1
                model.detay2 = item.DetayTutar_2
                model.detay3 = item.DetayTutar_3
               
                model.teslim = item.Teslim
                liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste) 

    def getGelenSipAyEfesYukleHepsi(self):
        
        
        result_1 = self.data.getList( ## efes - hepsi - gelen aylık siparisler
           """ 
            SELECT  
            s.SiparisTarihi,  
            u.SiparisNo,  
              
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
              
             YEAR(s.SiparisTarihi) as yil ,  
             Month(s.SiparisTarihi) as ay,  
            s.YuklemeTarihi,  
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.SiparisTarihi) =  Year(GetDate())  
              
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID )  
            and Month(s.SiparisTarihi) = Month(GetDate())  
            and s.FaturaKesimTurID=2  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID,s.YuklemeTarihi  
            order by s.SiparisTarihi desc  
           """
        )
        liste = list()
        a = 0
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None) :
                  a +=1
            else:
                model.tarih = item.SiparisTarihi
                model.siparisNo = item.SiparisNo
                model.musteriadi = item.musteri
                model.satistoplam = item.SatisToplam
                model.navlun = item.NavlunSatis
                model.detay1 = item.DetayTutar_1
                model.detay2 = item.DetayTutar_2
                model.detay3 = item.DetayTutar_3
                
                model.teslim = item.Teslim
                liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste)     

    def getGelenSipAyListYukleHepsi(self):
        
        
        result_1 = self.data.getList(
            
           """
            SELECT  
            s.SiparisTarihi,  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
             
            s.YuklemeTarihi,  
           YEAR(s.SiparisTarihi) as yil ,  
           Month(s.SiparisTarihi) as ay,  
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.SiparisTarihi) =  Year(GetDate())  
              
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID )  
            and Month(s.SiparisTarihi) = Month(GetDate())  
  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID,s.YuklemeTarihi  
            order by s.SiparisTarihi desc  
           """
        )
        liste = list()
        a = 0 
       
        for item in result_1:
          if ( item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
          else:      
            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.SiparisTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
           
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste)  

    def getGelenSipAyEfesYukle(self):
        
        
        result_1 = self.data.getList( ## efes - mekmar - gelen aylık siparisler
         
          """ 
            SELECT  
            s.SiparisTarihi,  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
              
            YEAR(s.SiparisTarihi) as yil ,  
            Month(s.SiparisTarihi) as ay,  
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.SiparisTarihi) =  Year(GetDate())  
             
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            and Month(s.SiparisTarihi) = Month(GetDate())  
            and s.FaturaKesimTurID=2  
     
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID  
            order by s.SiparisTarihi desc  
          """
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.SiparisTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
           
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste)
   
    def getGelenSipYilEfesYukle(self):
        
        
        result_1 = self.data.getList( ## efes - mekmar - gelen yil siparisler
          
           """ 
            SELECT  
             s.SiparisTarihi,  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
              
          YEAR(s.SiparisTarihi) as yil ,  
           Month(s.SiparisTarihi) as ay,  
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.SiparisTarihi) =  Year(GetDate())  
             
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID and m.Marketing='Mekmar')  
            and Month(s.SiparisTarihi) < Month(GetDate())  
            and s.FaturaKesimTurID=2  
     
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID  
            order by s.SiparisTarihi desc   
           """
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.SiparisTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
            
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste) 

    def getGelenSipYilEfesYukleHepsi(self):
        
        
        result_1 = self.data.getList( ## efes - mekmar - gelen yil siparisler
           """
            SELECT  
             s.SiparisTarihi,  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
             
            YEAR(s.SiparisTarihi) as yil ,  
            Month(s.SiparisTarihi) as ay,  
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.SiparisTarihi) =  Year(GetDate())  
             
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID )  
            and Month(s.SiparisTarihi) < Month(GetDate())  
             and s.FaturaKesimTurID=2  
     
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.SiparisTarihi,s.TeslimTurID  
            order by s.SiparisTarihi desc  

            """
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.SiparisTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
            
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste) 

    def getGelenSevkYilEfesYukleHepsi(self):
        
        
        result_1 = self.data.getList( ## efes - hepsi - gelen yil sevk
            
            """ 
            SELECT  
             s.YuklemeTarihi,  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
              
    
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.YuklemeTarihi) =  Year(GetDate())  
             
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID )  
            and Month(s.YuklemeTarihi) < Month(GetDate())  
           and s.FaturaKesimTurID=2  
            and s.SiparisDurumID=3  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.YuklemeTarihi,s.TeslimTurID  
            order by s.YuklemeTarihi desc  
            """
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.YuklemeTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
            
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste) 

    def getGelenSevkYilEfesYukle(self):
        
        
        result_1 = self.data.getList( ## efes - mekmar - gelen yil sevk
           
           """ 
             SELECT  
            s.YuklemeTarihi,  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
         
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.YuklemeTarihi) =  Year(GetDate())  
             
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID and m.Marketing='Mekmar' )  
            and Month(s.YuklemeTarihi) < Month(GetDate())  
            and s.FaturaKesimTurID=2  
            and s.SiparisDurumID=3  
  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.YuklemeTarihi,s.TeslimTurID  
            order by s.YuklemeTarihi desc  
           """
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.YuklemeTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
           
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste)    

    def getGelenSevkAyEfesYukle(self):
        
        
        result_1 = self.data.getList( ## efes - mekmar - gelen ay sevk
           
           """ 
             SELECT  
           s.YuklemeTarihi,  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
        
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.YuklemeTarihi) =  Year(GetDate())  
             
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID and m.Marketing='Mekmar' )  
            and Month(s.YuklemeTarihi) = Month(GetDate())  
           and s.FaturaKesimTurID=2  
            and s.SiparisDurumID=3  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.YuklemeTarihi,s.TeslimTurID  
            order by s.YuklemeTarihi desc  
           """
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.YuklemeTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
           
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste)  

    def getGelenSevkAyEfesYukleHepsi(self):
        
        
        result_1 = self.data.getList( ## efes  - gelen ay sevk
          
           """ 
            SELECT  
           s.YuklemeTarihi,  
            u.SiparisNo,  
            sum(u.SatisToplam) as SatisToplam,  
            s.DetayTutar_1,  
            s.NavlunSatis,  
            s.DetayTutar_2,  
            s.DetayTutar_3 ,  
        
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,  
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim   
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo   
            where   
            s.SiparisNo=u.SiparisNo  
            and YEAR(s.YuklemeTarihi) =  Year(GetDate())  
             
            and s.MusteriID in (Select m.ID from MusterilerTB m  
            where m.ID=s.MusteriID )  
            and Month(s.YuklemeTarihi) = Month(GetDate())  
           and s.FaturaKesimTurID=2  
           and s.SiparisDurumID=3  
            group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3,s.MusteriID,s.YuklemeTarihi,s.TeslimTurID  
            order by s.YuklemeTarihi desc  
           """
        )
        liste = list()
         
       
        for item in result_1:

            model = AnasayfaHepsiSiparisModel()
            model.tarih = item.YuklemeTarihi
            model.siparisNo = item.SiparisNo
            model.musteriadi = item.musteri
            model.satistoplam = item.SatisToplam
            model.navlun = item.NavlunSatis
            model.detay1 = item.DetayTutar_1
            model.detay2 = item.DetayTutar_2
            model.detay3 = item.DetayTutar_3
            
            model.teslim = item.Teslim
            liste.append(model)
  
        schema = AnasayfaHepsiSiparisSchema(many=True)
        
        return  schema.dump(liste)      
    def mailGonder(self,numuneNo,mailSahibi,tarih):

        islem_aciklamasi=numuneNo + " " + 'Po Sahip Numune Bilgisi'
        mail_konu=numuneNo + " " + 'Po sahip numune girmiş olduğunuz' + "  " +  tarih  +" " + 'tarihine göre ulaşmıştır.Lütfen Kontrol Ediniz.'

        MailService(islem_aciklamasi,mailSahibi,mail_konu)
    def numuneGonderimDurumu(self):
         result = self.data.getList("""
                                            select 
                                            n.NumuneNo,
                                            n.NumuneTemsilci,
                                            DAY(n.YuklemeTarihi) as YuklemeTarihi,
                                            n.YuklemeTarihi as YuklemeTarihiTam,
                                            GETDATE() as Tarih,n.MailGonderiDurumu as MailDurum,
                                            (select k.MailAdres from KullaniciTB k where k.ID=n.NumuneTemsilci) as MailSahibi
                                        from 
                                            NumunelerTB n 
                                        where 
                                            YEAR(n.YuklemeTarihi) = YEAR(GETDATE()) and 
                                            MONTH(n.YuklemeTarihi) >= MONTH(GETDATE()) and
                                            DAY(n.YuklemeTarihi) >= DAY(GETDATE())
                                        """)
        
         for item in result:
            if item.MailDurum == None and item.YuklemeTarihi == datetime.datetime.now().day:
                # self.mailGonder(item.NumuneNo,item.MailSahibi,str(item.YuklemeTarihiTam))
                self.data.update_insert("""
                                            update NumunelerTB SET MailGonderiDurumu=? WHERE NumuneNo=?
                                        
                                        
                                        """,(1,item.NumuneNo))
                print('Mail Başarıyla Gönderildi...')
                
                 
    def getMekmarTakipListesi(self):
        
        self.numuneGonderimDurumu()
        
        tarihIslem = TarihIslemler()
        result1 = self.data.getList(
            """
            select
            s.ID,
            s.SiparisNo,
            m.FirmaAdi as MusteriAdi,
            s.Pesinat,
            NavlunSatis + DetayTutar_1 + DetayTutar_2 + DetayTutar_3  as Navlun,
            ( Select Sum(o.Tutar) from OdemelerTB o where o.SiparisNo=s.SiparisNo ) as Odemeler,
            (Select Sum(u.SatisToplam) from SiparisUrunTB u where u.SiparisNo=s.SiparisNo) as MalBedeli,
            (select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi ) as Sorumlu,
            s.Eta,
            s.KonteynerNo,
            s.YuklemeTarihi,
            s.KonsimentoDurum,
            s.Line,
            s.AktarmaLimanAdi
            from
            SiparislerTB s,MusterilerTB m
            where s.MusteriID=m.ID
            and s.SiparisDurumID=3 and Takip=1
		    and m.Marketing='Mekmar'
            order by s.ID desc
            """
        )
       
        liste = list()
        sira =1
        for item in result1:

            navlun = 0
            odemeler = 0
            mal_bedeli = 0
            sevk_tarihi = ""
            eta = ""
            model = SevkTakipModel()

            if item.Navlun != None:
                navlun = item.Navlun 
            
            if item.Odemeler != None:
                odemeler = item.Odemeler 
            
            if item.MalBedeli != None:
                mal_bedeli = item.MalBedeli
            model.sira = sira
            sira += 1
            if item.Eta != None: 
                try:
                    eta = tarihIslem.getDate(item.Eta).strftime("%d-%m-%Y")
                    bugun = datetime.date.today()
                    sontarih_str = eta.split('-')
                    
                    sontarih = datetime.date(int(sontarih_str[2]),int(sontarih_str[1]),int(sontarih_str[0]))
                    model.kalan_sure = (sontarih - bugun).days
                except Exception as e :
                    print('eta hatası : ', str(e))

            if item.YuklemeTarihi != None:
                sevk_tarihi = tarihIslem.getDate(item.YuklemeTarihi).strftime("%d-%m-%Y")

            
            model.id = item.ID 
            model.siparisno = item.SiparisNo 
            model.pesinat = item.Pesinat 
            model.kalan_alacak = (navlun + mal_bedeli) - odemeler
            model.sevk_tarihi = sevk_tarihi
            model.konteynerno = item.KonteynerNo 
            model.eta = eta
            model.sorumlusu = item.Sorumlu
            model.musteriadi = item.MusteriAdi
            model.konsimento = item.KonsimentoDurum
            model.line = item.Line
            model.liman = item.AktarmaLimanAdi

            liste.append(model)

        schema = SevkTakipSchema(many=True)

        return schema.dump(liste)  

    def getHepsiTakipListesi(self):
        tarihIslem = TarihIslemler()
        result1 = self.data.getList(
            """
            select
            s.ID,
            s.SiparisNo,
            m.FirmaAdi as MusteriAdi,
            s.Pesinat,
            NavlunSatis + DetayTutar_1 + DetayTutar_2 + DetayTutar_3    as Navlun,
            ( Select Sum(o.Tutar) from OdemelerTB o where o.SiparisNo=s.SiparisNo ) as Odemeler,
            (Select Sum(u.SatisToplam) from SiparisUrunTB u where u.SiparisNo=s.SiparisNo) as MalBedeli,
            (select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi ) as Sorumlu,
            s.Eta,
            s.KonteynerNo,
            s.YuklemeTarihi,
            s.KonsimentoDurum,
            s.Line,
            s.AktarmaLimanAdi
            from
            SiparislerTB s,MusterilerTB m
            where s.MusteriID=m.ID
            and s.SiparisDurumID=3 and Takip=1
		   
            order by s.ID desc
            """
        )
       
        liste = list()
        sira =1
        for item in result1:

            navlun = 0
            odemeler = 0
            mal_bedeli = 0
            sevk_tarihi = ""
            eta = ""
            model = SevkTakipModel()

            if item.Navlun != None:
                navlun = item.Navlun 
            
            if item.Odemeler != None:
                odemeler = item.Odemeler 
            
            if item.MalBedeli != None:
                mal_bedeli = item.MalBedeli
            model.sira = sira
            sira += 1
            if item.Eta != None: 
                try:
                    eta = tarihIslem.getDate(item.Eta).strftime("%d-%m-%Y")
                    bugun = datetime.date.today()
                    sontarih_str = eta.split('-')
                    
                    sontarih = datetime.date(int(sontarih_str[2]),int(sontarih_str[1]),int(sontarih_str[0]))
                    model.kalan_sure = (sontarih - bugun).days
                except Exception as e :
                    print('eta hatası : ', str(e))

            if item.YuklemeTarihi != None:
                sevk_tarihi = tarihIslem.getDate(item.YuklemeTarihi).strftime("%d-%m-%Y")

            
            model.id = item.ID 
            model.siparisno = item.SiparisNo 
            model.pesinat = item.Pesinat 
            model.kalan_alacak = (navlun + mal_bedeli) - odemeler
            model.sevk_tarihi = sevk_tarihi
            model.konteynerno = item.KonteynerNo 
            model.eta = eta
            model.sorumlusu = item.Sorumlu
            model.musteriadi = item.MusteriAdi
            model.konsimento = item.KonsimentoDurum
            model.line = item.Line
            model.liman = item.AktarmaLimanAdi

            liste.append(model)

        schema = SevkTakipSchema(many=True)

        return schema.dump(liste)  

                        
                                                
                 
       



 
       

    
