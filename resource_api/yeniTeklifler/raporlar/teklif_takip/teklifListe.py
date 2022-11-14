from helpers import SqlConnect
from resource_api.yeniTeklifler.raporlar.shared import Aylar,Renkler


class TeklifListe:
    def __init__(self):
        self.data = SqlConnect().data
        self.aylar = Aylar()
        self.grafikRapor = self.__getGrafikOlustur()
        self.renkler = Renkler().getRenkList()

    
    def getGrafikRaporHepsi(self):

        labels = list()
        datasets = list()

        grafikData = self.grafikRapor

        groupAyList = self.data.getList(
            """
            select
            Month(t.Tarih) as Ay
            from
            YeniTeklifTB t,KullaniciTB k
            where t.TakipEt=1 and k.ID=t.KullaniciId
            and Year(t.Tarih)=Year(GetDate())
            group by MONTH(t.Tarih)
            order by Month(t.Tarih) asc
            """
        )
      
        groupTemsilci = set(map(lambda x:x['temsilciAdi'],grafikData))
       
        indeks = 0
        for item in groupTemsilci:
           
            
            
            if item =="Gizem":
                 self.renkler[indeks] = 'black'
              
            if item =="Fatih":
                 self.renkler[indeks] = '#302e75'   
            if item =="Ozlem":
                 self.renkler[indeks] = '#ad3d47'  
              
            if item =="Hakan":
                self.renkler[indeks] = '#a2c4c9'        
            model = {

                'label' : item,
                'backgroundColor' : self.renkler[indeks],
                'data' : list()
            }
            datasets.append(model)

            indeks +=1
       
        labels.append("Ocak")
        for item in groupAyList:
            
            labels.append(self.aylar.getAyAdi(item.Ay))
       
        for ay in labels:

            for item in datasets:

                teklifSayisi = self.__getTeklifSayisi(ay,item['label'])
                if ay == 'Ocak':
                    teklifSayisi += self.__getGecenYilToplamTeklif(item['label'])
                item['data'].append(teklifSayisi)

               


        return labels,datasets

    def getOncelikGrafikRapor(self):

        data_kullanici_list = self.data.getList(
            """
            select
            k.KullaniciAdi
            from
            YeniTeklifTB t,KullaniciTB k
            where t.TakipEt=1 and k.ID=t.KullaniciId
            group by k.KullaniciAdi

            """
        )

        kullanici_veri_data = self.data.getList(
            """
            select
            k.KullaniciAdi,
            t.TeklifOncelik,
            count(*) as oncelik_deger
            from
            YeniTeklifTB t,KullaniciTB k
            where t.TakipEt=1 and k.ID=t.KullaniciId
            group by k.KullaniciAdi,t.TeklifOncelik
            order by count(*) desc

            """
        )

        labels = list()
        datasets = list()

        label = ""
        backgroundColor = ""

        for item in data_kullanici_list:
            
            if item.KullaniciAdi == "Gizem":
                backgroundColor = "black"
            
            

            if item.KullaniciAdi == "Ozlem":
                backgroundColor = "#ad3d47"

            if item.KullaniciAdi == "Fatih":
                backgroundColor = "#302e75"

            if item.KullaniciAdi == "Hakan":
                backgroundColor = "#a2c4c9"

            label = item.KullaniciAdi 

            a_veri = self.__getOncelikKullaniciTeklifSayisi(label,'A',kullanici_veri_data)
            b_veri = self.__getOncelikKullaniciTeklifSayisi(label,'B',kullanici_veri_data)
            c_veri = self.__getOncelikKullaniciTeklifSayisi(label,'C',kullanici_veri_data)

            data = list()
            data.append(a_veri)
            data.append(b_veri)
            data.append(c_veri)

            dataset = {

                "backgroundColor" : backgroundColor,
                "label" : label,
                "data" : data
            }

            datasets.append(dataset)
            
        labels.append("A")
        labels.append("B")
        labels.append("C")

        return datasets,labels       
            

    def __getOncelikKullaniciTeklifSayisi(self,kullaniciadi,oncelik,data_list):

        sayi = 0

        for item in data_list:

            if kullaniciadi == item.KullaniciAdi and oncelik == item.TeklifOncelik:

                sayi = int(item.oncelik_deger)

        
        return sayi

        
    def __getGrafikOlustur(self):

        result = self.data.getList(
            """
            select
            t.KullaniciId,
            k.KullaniciAdi,
            Year(t.Tarih) as Yil,
            Month(t.Tarih) as Ay,
            count(*) as TeklifSayisi
            from
            YeniTeklifTB t,KullaniciTB k
            where t.TakipEt=1 and k.ID=t.KullaniciId            
            group by t.KullaniciId,k.KullaniciAdi,
            year(t.Tarih),MONTH(t.Tarih)
            order by count(*) desc,Year(t.Tarih) desc

            """
        )

        dataList = list()
        label = ""
        backgroundColor = ""
        for item in result:
          
            
            if item.KullaniciAdi == "Gizem":
                backgroundColor = "black"
            
            

            if item.KullaniciAdi == "Ozlem":
                backgroundColor = "#ad3d47"

            

            

            if item.KullaniciAdi == "Fatih":
                backgroundColor = "#302e75" 
   
            
            if item.KullaniciAdi == "Hakan":
                backgroundColor = "#a2c4c9" 
        label = item.KullaniciAdi    

        for item in result:
           
            
            model = {

                'ay' : item.Ay,
                'yil' : item.Yil,
                'ayAdi' : self.aylar.getAyAdi(item.Ay),
                'temsilciAdi' :  item.KullaniciAdi,
                'teklifSayisi' : item.TeklifSayisi,
                "backgroundColor" : backgroundColor,
                 "label" : label
            }

            dataList.append(model)


        return sorted(dataList,key=lambda x:x['ay'],reverse=False) 

    def __getTeklifSayisi(self,ayAdi,temsilci):

        teklif = 0
        for item in self.grafikRapor:

            if item['yil'] > 2019 and  item['ayAdi'] == ayAdi and item['temsilciAdi'] == temsilci:
                teklif = item['teklifSayisi']
        

        return teklif

    def __getGecenYilToplamTeklif(self,temsilciAdi):
        teklif = 0
        for item in self.grafikRapor:
            if item['yil'] < 2020 and  item['temsilciAdi'] == temsilciAdi:
                teklif += item['teklifSayisi']

        return teklif



