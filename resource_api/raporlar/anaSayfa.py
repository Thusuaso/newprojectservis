from helpers import SqlConnect
from flask_restful import Resource
from flask import jsonify
from resource_api.raporlar.finans import Finans
from resource_api.raporlar.uretim import Uretim
from resource_api.raporlar.sevkiyat import Sevkiyat
from resource_api.raporlar.teklifler import TeklifRapor
from resource_api.raporlar.finansListe import FinansListe
import datetime
import locale

class SiparisOzet(Resource):
    def get(self):
        rapor = AnaSayfaRaporlar()

        gelenAylik,gelenAylikHepsi,gelenAylikEfes,gelenAylikEfesHepsi,farkMekmarAy,farkHepsiAy,farkMekmarYil,farkHepsiYil,ay,ay_int= rapor.getAylikGelenSiparisToplami()
       
        gelenYillik,gelenYillikHepsi,gelenEfes,gelenEfesHepsi,mekmarFarkYil,hepsiFarkYil,mekmarFarkAy,hepsiFarkAy,yil = rapor.getYillikGelenSiparisToplami()

        yuklenenAylik,yuklenenAylikHepsi,yuklenenAylikEfes,yuklenenAylikEfesHepsi,yfarkMekmarAy,yfarkHepsiAy,yfarkMekmarYil,yfarkHepsiYil = rapor.getAylikYuklenenSiparisToplami()
        yuklenenYillik,yuklenenYillikHepsi,yuklenenEfes,yuklenenEfesHepsi,ymekmarFarkYil,yhepsiFarkYil,ymekmarFarkAy,yhepsiFarkAy = rapor.getYillikYuklenenSiparisToplami()

        ortlamaMekmarAy,ortalamaHepsiAy,ortalamaMekmarYillik,ortalamaHepsiYillik ,ortalamaEfesAy,ortalamaEfesHepsiAy ,ortalamaEfesYillik,ortalamaEfesHepsiYillik = rapor.getAylikOrtalama()
        yortlamaMekmarAy,yortalamaHepsiAy,yortalamaMekmarYillik,yortalamaHepsiYillik , yortlamaEfesAy,yortalamaEfesHepsiAy,yortalamaEfesYillik,yortalamaEfesHepsiYillik= rapor.getYillikOrtalama()
     
        GecenDdp,GecenDdpHepsi = rapor.getGecenYillikDtp() 
        GecenFob,GecenFobHepsi = rapor.getGecenYillikFob() 

        BuDdp,BuDdpHepsi = rapor.getBuYillikDtp() 
        BuFob,BuFobHepsi = rapor.getBuYillikFob()
      
        alacakAylik,alacakAylikHepsi = rapor.getAylikAlacak()
        alacakYillik,alacakYillikHepsi = rapor.getYillikAlacak()

        grafikRaporMekmar = rapor.getsiparisGrafikRapor()
        grafikRaporHepsi = rapor.getsiparisGrafikRaporHepsi()

        siparisUretimMekmar,siparisUretimHepsi = rapor.getUretimList()

        musteriUretimMekmar,musteriUretimHepsi = rapor.getMusteriUretimList()

        sevkiyatIslem = Sevkiyat()

        siparisYuklenenMekmar = sevkiyatIslem.getSevkiyatMekmarList()
        siparisYuklenenHepsi = sevkiyatIslem.getSevkiyatHepsiList()

        grafikYuklenenMekmar = sevkiyatIslem.getGrafikMekmarList()
        grafikYuklenenHepsi = sevkiyatIslem.getGrafikHepsiList()

        teklifRapor = TeklifRapor()

        teklifAylikList = teklifRapor.getTeklifAylikList()
        teklifYillikList = teklifRapor.getTeklifYillikList()
        teklifGrafikRapor = teklifRapor.getGrafikRapor()

       # finansListe = FinansListe()

        #mekmarFinansListe = finansListe.mekmarList()
        #hepsiFinansListe = finansListe.hepsiList()

        data = {

            'gelenSiparisOzet' :{

                'aylik' : {
                    
                    'mekmar' : gelenAylik,
                    'hepsi' : gelenAylikHepsi,
                    'gelenAylikEfes' :  gelenAylikEfes,
                    'gelenAylikEfesHepsi': gelenAylikEfesHepsi,
                    'farkMekmarAy' : farkMekmarAy,
                    'farkHepsiAy' : farkHepsiAy,
                    'farkMekmarYil' : farkMekmarYil,
                    'farkHepsiYil' : farkHepsiYil,
                    'ay' : ay,
                    'ay_int' : ay_int ,
                    'ortlamaMekmarAy' : ortlamaMekmarAy,
                    'ortalamaHepsiAy' : ortalamaHepsiAy,
                    'ortalamaMekmarYillik' :ortalamaMekmarYillik,
                    'ortalamaHepsiYillik' : ortalamaHepsiYillik,
                    'ortalamaEfesAy' : ortalamaEfesAy,
                    'ortalamaEfesHepsiAy' : ortalamaEfesHepsiAy,
                    'ortalamaEfesYillik' :ortalamaEfesYillik,
                    'ortalamaEfesHepsiYillik' : ortalamaEfesHepsiYillik

                           
                     
                },
                'yillik' : {
                   
                    'mekmar' : gelenYillik,
                    'hepsi' : gelenYillikHepsi,
                    'gelenEfes' :  gelenEfes,
                    'gelenEfesHepsi': gelenEfesHepsi,
                    'mekmarFarkYil' : mekmarFarkYil,
                    'hepsiFarkYil' : hepsiFarkYil,
                    'mekmarFarkAy' : mekmarFarkAy,
                    'hepsiFarkAy' : hepsiFarkAy,
                     'yil' : yil,
                     
                     'yortlamaMekmarAy' : yortlamaMekmarAy,
                     'yortalamaHepsiAy' : yortalamaHepsiAy,
                     'yortalamaMekmarYillik' :yortalamaMekmarYillik,
                     'yortalamaHepsiYillik' : yortalamaHepsiYillik,
                     'yortlamaEfesAy' : yortlamaEfesAy,
                     'yortalamaEfesHepsiAy' : yortalamaEfesHepsiAy,
                     'yortalamaEfesYillik' :yortalamaEfesYillik,
                     'yortalamaEfesHepsiYillik' : yortalamaEfesHepsiYillik,
                     'GecenFob' : GecenFob ,
                     'GecenFobHepsi' : GecenFobHepsi,
                     'BuFob' : BuFob ,
                     'BuFobHepsi' : BuFobHepsi
                }         
            },
            'yuklenenSiparisOzet' : {

                'aylik' : {
                   
                    'mekmar' : yuklenenAylik,
                    'hepsi' : yuklenenAylikHepsi,
                    'yuklenenAylikEfes' : yuklenenAylikEfes,
                    'yuklenenAylikEfesHepsi' : yuklenenAylikEfesHepsi,
                    'farkMekmarAy' : yfarkMekmarAy,
                    'farkHepsiAy' : yfarkHepsiAy,
                    'farkMekmarYil' : yfarkMekmarYil,
                    'farkHepsiYil' : yfarkHepsiYil
                },
                'yillik' : {
                    
                    'mekmar' : yuklenenYillik,
                    'hepsi' : yuklenenYillikHepsi,
                    'yuklenenEfes' : yuklenenEfes,
                    'yuklenenEfesHepsi' : yuklenenEfesHepsi,
                    'mekmarFarkYil' : ymekmarFarkYil,
                    'hepsiFarkYil' : yhepsiFarkYil,
                    'mekmarFarkAy' : ymekmarFarkAy,
                    'hepsiFarkAy' : yhepsiFarkAy,
                    'GecenDdp' : GecenDdp,
                    'GecenDdpHepsi' : GecenDdpHepsi,
                    'BuDdp' : BuDdp,
                    'BuDdpHepsi' : BuDdpHepsi
                }
            },
            'yuklenenSiparisAlacak':{

                'aylik' : {
                    
                    'mekmar' : alacakAylik,
                    'hepsi' : alacakAylikHepsi
                },
                'yillik' : {
                    
                    'mekmar' : alacakYillik,
                    'hepsi' : alacakYillikHepsi
                }
            },
            'siparisGrafikRapor' : {

                'mekmar' : grafikRaporMekmar,
                'hepsi' : grafikRaporHepsi
            },
            'siparisUretim' : {

                'mekmar' : siparisUretimMekmar,
                'hepsi' : siparisUretimHepsi
            },
            'siparisYuklenen' :{

                'mekmar' : siparisYuklenenMekmar,
                'hepsi' : siparisYuklenenHepsi
            },
            'siparisYuklenenGrafik' : {

                'mekmar' : grafikYuklenenMekmar,
                'hepsi' : grafikYuklenenHepsi
            },
            'teklifRapor' : {

                'aylik' : teklifAylikList,
                'yillik' : teklifYillikList,
                'grafik' : teklifGrafikRapor
            },
            #'finansRapor' :{

              #  'mekmar': mekmarFinansListe,
              #  'hepsi' : hepsiFinansListe
           # },
            'musteriUretim' : {

                'mekmar' : musteriUretimMekmar,
                'hepsi' : musteriUretimHepsi
            }
        }
        
        return jsonify(data)



class AnaSayfaRaporlar:

    def __init__(self):
        self.data = SqlConnect().data
        self.finans = Finans()
        self.uretim = Uretim()
        

    def getAylikGelenSiparisToplami(self):

        result_1 = self.data.getList(
              """ 
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
            MONTH(s.SiparisTarihi) as Ay,
			m.FirmaAdi,
			s.SiparisNo,
			s.YuklemeTarihi
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			
            and MONTH(s.SiparisTarihi)= Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo
            """
        )

        result_2 = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
            MONTH(s.SiparisTarihi) as Ay,
			m.FirmaAdi,
			s.SiparisNo,
			s.YuklemeTarihi
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			
            and MONTH(s.SiparisTarihi)=Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo
            """
        )
        result_3 = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
            MONTH(s.SiparisTarihi) as Ay,
			m.FirmaAdi,
			s.SiparisNo,
			s.YuklemeTarihi
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			and s.FaturaKesimTurID=2
            and MONTH(s.SiparisTarihi)= Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo
            """
        )
        result_4 = self.data.getList(
            """
                select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
            MONTH(s.SiparisTarihi) as Ay,
			m.FirmaAdi,
			s.SiparisNo,
			s.YuklemeTarihi
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			and s.FaturaKesimTurID=2
            and MONTH(s.SiparisTarihi)= Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo
            """
        )
        result_5 = self.data.getList("""select  Month(GetDate()) as Ay,Year(GETDATE()) as Yil from Tarihler""")

        fobTutar = 0
        fobTutarHepsi = 0
        fobEfes = 0
        fobEfesHepsi = 0
        ay = 0
        a = 1
        for item in result_1:
        
            if (item.FirmaAdi == 'Cem-Mer (PEKER)'  and item.YuklemeTarihi == None) :
                 
                  
                  a +=1
            else:  
                fobTutar += float(item.FobTutar)

        for item in result_2:
        
            if (item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None) :
                  a +=1
            else:  
                fobTutarHepsi += float(item.FobTutar)

        for item in result_3:
        
            if (item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None):
                  a +=1
            else:  
                fobEfes += float(item.FobTutar)

        for item in result_4:
        
            if (item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None):
                  a +=1
            else:  
                fobEfesHepsi += float(item.FobTutar)

        

        ayMekmar,ayHepsi = self.__siparisFarklarAylik()
        
        ay =  self.__getAyStr(result_5[0].Ay)
        ay_int = result_5[0].Ay
           
        farkMekmarAy = (fobTutar / ayMekmar) * 100
        farkHepsiAy = (fobTutarHepsi / ayHepsi) * 100
        
        yilMekmar,yilHepsi = self.__siparisFarklarYillik()

        farkMekmarYillik = (fobTutar / yilMekmar) * 100
        farkHepsiYillik = (fobTutarHepsi / yilHepsi) * 100
      
        return fobTutar,fobTutarHepsi,fobEfes,fobEfesHepsi,round(farkMekmarAy,2),round(farkHepsiAy,2),round(farkMekmarYillik,2),round(farkHepsiYillik,2),ay,ay_int

    def getYillikGelenSiparisToplami(self):

        result_1 = self.data.getList( #mekmar için 
        """
        
         select  
            Year(s.SiparisTarihi) as Yil,  
            Sum(u.SatisToplam)  
            as FobTutar,  
            MONTH(s.SiparisTarihi) as Ay,  
            m.FirmaAdi,  
            s.SiparisNo,  
            s.YuklemeTarihi  
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID and m.Marketing in  
            ('Mekmar') and s.SiparisNo=u.SiparisNo  
            and Year(s.SiparisTarihi)= Year(GetDate())  
     
            and MONTH(s.SiparisTarihi)< Month(GetDate())  
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo  

        """
        )

        result_2 = self.data.getList(  #hepsi için
          """
           select  
            Year(s.SiparisTarihi) as Yil,  
            Sum(u.SatisToplam)  
            as FobTutar,  
             MONTH(s.SiparisTarihi) as Ay,  
            m.FirmaAdi,  
            s.SiparisNo,  
            s.YuklemeTarihi  
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo  
            and Year(s.SiparisTarihi)= Year(GetDate())  
     
            and MONTH(s.SiparisTarihi)< Month(GetDate())  
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo  

          """
        )
        
        result_3 = self.data.getList( #efes için
           """
            select  
            Year(s.SiparisTarihi) as Yil,  
            Sum(u.SatisToplam)  
            as FobTutar,  
            MONTH(s.SiparisTarihi) as Ay,  
             m.FirmaAdi,  
             s.SiparisNo,  
            s.YuklemeTarihi  
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID and m.Marketing in  
            ('Mekmar') and s.SiparisNo=u.SiparisNo  
            and Year(s.SiparisTarihi)= Year(GetDate())  
            and s.FaturaKesimTurID=2  
            and MONTH(s.SiparisTarihi)< Month(GetDate())  
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo  

           """
        )
        
        result_4 = self.data.getList( #efes tum
           """
             select  
            Year(s.SiparisTarihi) as Yil,  
            Sum(u.SatisToplam)  
            as FobTutar,  
            MONTH(s.SiparisTarihi) as Ay,  
            m.FirmaAdi,  
            s.SiparisNo,  
           s.YuklemeTarihi  
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo  
            and Year(s.SiparisTarihi)= Year(GetDate())  
            and s.FaturaKesimTurID=2  
            and MONTH(s.SiparisTarihi)< Month(GetDate())  
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi),m.FirmaAdi,s.YuklemeTarihi,s.SiparisNo  
           
           """
        )

        fobTutar = 0
        fobTutarHepsi = 0
        fobEfes = 0
        fobEfesHepsi = 0
        yil = 0
        a = 0 
        
        for item in result_1:
        
            if (item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None):
                  a +=1
            else:  
                fobTutar += float(item.FobTutar)

        for item in result_2:
        
            if (item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None) :
                  a +=1
            else:  
                fobTutarHepsi += float(item.FobTutar)

        for item in result_3:
        
            if (item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None) :
                  a +=1
            else:  
                fobEfes += float(item.FobTutar)

        for item in result_4:
        
            if (item.FirmaAdi == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None) :
                  a +=1
            else:  
                fobEfesHepsi += float(item.FobTutar)        
       

        
        mekmarYil,hepsiYil = self.__siparisFarklarYillik()
        mekmarAy,hepsiAy = self.__siparisFarklarYillikAy()
        yil = datetime.datetime.now().year
        mekmarFarkYil = (fobTutar / mekmarYil ) * 100
        hepsiFarkYil = (fobTutarHepsi / hepsiYil) * 100
        #şimdiye kadar geçen ay toplamı
        mekmarFarkAy = (fobTutar / mekmarAy) * 100
        hepsiFarkAy = (fobTutar / hepsiAy) * 100

     
     
        return fobTutar,fobTutarHepsi,fobEfes,fobEfesHepsi,round(mekmarFarkYil,2),round(hepsiFarkYil,2),round(mekmarFarkAy,2),round(hepsiFarkAy,2),yil


    def getAylikYuklenenSiparisToplami(self):


        result_1 = self.data.getList(
           """
             select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam )  
            as FobTutar,  
            s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
              
            s.SiparisNo  
     
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID and m.Marketing in  
            ('Mekmar') and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
            and Year(s.YuklemeTarihi)= Year(GetDate())  
    
            and MONTH(s.YuklemeTarihi)=Month(GetDate())  
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
              
            s.SiparisNo  
           
           """ #mekmar için 
		
        )
        result_2 = self.data.getList(
           """
           
              select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam )  
            as FobTutar,  
            s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
             
            s.SiparisNo  
     
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
              
  
            and Year(s.YuklemeTarihi)= Year(GetDate())  
    
            and MONTH(s.YuklemeTarihi)=Month(GetDate())  
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3,  
            
            s.SiparisNo  

           """#tum  için 
        )
        result_3 = self.data.getList(

           """
            select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam )  
            as FobTutar,  
            s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
            
            s.SiparisNo  
     
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID and m.Marketing in  
            ('Mekmar') and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
            and s.FaturaKesimTurID = 2  
  
            and Year(s.YuklemeTarihi)= Year(GetDate())  
    
            and MONTH(s.YuklemeTarihi)=Month(GetDate())  
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
            
            s.SiparisNo  
           
           """ #efes  için 
        )
        result_4 = self.data.getList(
            """
            select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam )  
            as FobTutar,  
            s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3,  
              
            s.SiparisNo  
           
     
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
            and s.FaturaKesimTurID = 2  
  
            and Year(s.YuklemeTarihi)= Year(GetDate())  
    
            and MONTH(s.YuklemeTarihi)=Month(GetDate())  
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
             
            s.SiparisNo  
            
            """ #efes tum   
        )

        fobTutar = 0
        fobTutarHepsi = 0
        fobEfes = 0
        fobEfesHepsi = 0
        navlun = 0
        detay1 = 0
        detay2 = 0
        detay3 = 0
      
        navlunhepsi = 0
        detay1hepsi = 0
        detay2hepsi = 0
        detay3hepsi = 0
       
        navlunefes = 0
        detay1efes = 0
        detay2efes = 0
        detay3efes = 0
       
        navlunefeshepsi = 0
        detay1efeshepsi = 0
        detay2efeshepsi = 0
        detay3efeshepsi = 0
        


        for key  in result_1 :
             if key.NavlunSatis != None:
                 navlun = key.NavlunSatis
             if key.DetayTutar_1 != None:
                detay1 = key.DetayTutar_1
             if key.DetayTutar_2 != None:
                detay2 = key.DetayTutar_2
             if key.DetayTutar_3 != None:
                detay3 = key.DetayTutar_3   
              
             fobTutar = fobTutar + float(key.FobTutar) +float(navlun) + float(detay1) + float(detay2) + float(detay3) 

        for key  in result_2 :
             if key.NavlunSatis != None:
                 navlunhepsi = key.NavlunSatis
             if key.DetayTutar_1 != None:
                detay1hepsi = key.DetayTutar_1
             if key.DetayTutar_2 != None:
                detay2hepsi = key.DetayTutar_2
             if key.DetayTutar_3 != None:
                detay3hepsi = key.DetayTutar_3 
               
             fobTutarHepsi = fobTutarHepsi + float(key.FobTutar) +float(navlunhepsi) + float(detay1hepsi) + float(detay2hepsi) + float(detay3hepsi) 
          
        for key  in result_3 :
             if key.NavlunSatis != None:
                 navlunefes = key.NavlunSatis
             if key.DetayTutar_1 != None:
                detay1efes = key.DetayTutar_1
             if key.DetayTutar_2 != None:
                detay2efes = key.DetayTutar_2
             if key.DetayTutar_3 != None:
                detay3efes = key.DetayTutar_3  
                 
             fobEfes = fobEfes + float(key.FobTutar) +float(navlunefes) + float(detay1efes) + float(detay2efes) + float(detay3efes) 
      
        for key  in result_4 :
             if key.NavlunSatis != None:
                 navlunefeshepsi = key.NavlunSatis
             if key.DetayTutar_1 != None:
                detay1efeshepsi = key.DetayTutar_1
             if key.DetayTutar_2 != None:
                detay2efeshepsi = key.DetayTutar_2
             if key.DetayTutar_3 != None:
                detay3efeshepsi = key.DetayTutar_3  

             
             fobEfesHepsi = fobEfesHepsi + float(key.FobTutar) +float(navlunefeshepsi) + float(detay1efeshepsi) + float(detay2efeshepsi) + float(detay3efeshepsi)  

        ayMekmar,ayHepsi = self.__yuklemeFarklarAylik()

        farkMekmarAy = (fobTutar / ayMekmar) * 100
        farkHepsiAy = (fobTutarHepsi / ayHepsi) * 100
        
        yilMekmar,yilHepsi = self.__yuklemeFarklarYillik()

        farkMekmarYillik = (fobTutar / yilMekmar) * 100
        farkHepsiYillik = (fobTutarHepsi / yilHepsi) * 100

        return fobTutar,fobTutarHepsi,fobEfes,fobEfesHepsi,round(farkMekmarAy,2),round(farkHepsiAy,2),round(farkMekmarYillik,2),round(farkHepsiYillik,2)

    def getYillikYuklenenSiparisToplami(self):

        

        result_1 = self.data.getList(
         """
            select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam )  
            as FobTutar,  
            s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
                        
            s.SiparisNo  
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
             
            and Year(s.YuklemeTarihi)= Year(GetDate())  
      and m.Marketing in  
            ('Mekmar')  
            and MONTH(s.YuklemeTarihi)<Month(GetDate())  
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3,  
                        
            s.SiparisNo  
         
         """ #mekmar yuklenen
        )

        result_2 = self.data.getList(
           
             """
                select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam )  
            as FobTutar,  
            s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
                        
            s.SiparisNo  
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
             
            and Year(s.YuklemeTarihi)= Year(GetDate())  
        
            and MONTH(s.YuklemeTarihi)<Month(GetDate())  
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3,  
                        
            s.SiparisNo  
             
             """ #tum yuklenen siparis
        )
        result_3 = self.data.getList(

            """
                select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam )  
            as FobTutar,  
            s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
             
            s.SiparisNo  
     
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID and m.Marketing in  
            ('Mekmar') and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
            and s.FaturaKesimTurID = 2  
            and Year(s.YuklemeTarihi)= Year(GetDate())  
    
            and MONTH(s.YuklemeTarihi)< Month(GetDate())  
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
              
            s.SiparisNo  
            """ #efes yuklenen
        )

        result_4 = self.data.getList(

             """
                   select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam )  
            as FobTutar,  
            s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
             
            s.SiparisNo  
     
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
            and s.FaturaKesimTurID = 2  
            and Year(s.YuklemeTarihi)= Year(GetDate())  
    
            and MONTH(s.YuklemeTarihi)< Month(GetDate())  
            group by Year(s.YuklemeTarihi) ,s.NavlunSatis ,  
            s.DetayTutar_1 ,  
            s.DetayTutar_2 ,  
            s.DetayTutar_3 ,  
             
            s.SiparisNo  
             
             """ #efes yuklenen
        )
        fobTutar = 0
        fobTutarHepsi = 0
        fobEfes = 0
        fobEfesHepsi = 0
        navlun = 0
        detay1 = 0
        detay2 = 0
        detay3 = 0
       
        navlunhepsi = 0
        detay1hepsi = 0
        detay2hepsi = 0
        detay3hepsi = 0
       
        navlunefes = 0
        detay1efes = 0
        detay2efes = 0
        detay3efes = 0
       
        navlunefeshepsi = 0
        detay1efeshepsi = 0
        detay2efeshepsi = 0
        detay3efeshepsi = 0
        

        for key  in result_1 :
             if key.NavlunSatis != None:
                 navlun = key.NavlunSatis
             if key.DetayTutar_1 != None:
                detay1 = key.DetayTutar_1
             if key.DetayTutar_2 != None:
                detay2 = key.DetayTutar_2
             if key.DetayTutar_3 != None:
                detay3 = key.DetayTutar_3  
              
             fobTutar = fobTutar + float(key.FobTutar) +float(navlun) + float(detay1) + float(detay2) + float(detay3) 
            
           
       
        for item  in result_2 :
             if item.NavlunSatis != None:
                 navlunhepsi = item.NavlunSatis
             if item.DetayTutar_1 != None:
                detay1hepsi = item.DetayTutar_1
             if item.DetayTutar_2 != None:
                detay2hepsi = item.DetayTutar_2
             if item.DetayTutar_3 != None:
                detay3hepsi = item.DetayTutar_3  
             
             fobTutarHepsi = fobTutarHepsi + float(item.FobTutar) +float(navlunhepsi) + float(detay1hepsi) + float(detay2hepsi) + float(detay3hepsi) 
           
      
        for item  in result_3 :
             
             if item.NavlunSatis != None:
                 navlunefes = item.NavlunSatis
             if item.DetayTutar_1 != None:
                detay1efes = item.DetayTutar_1
             if item.DetayTutar_2 != None:
                detay2efes = item.DetayTutar_2
             if item.DetayTutar_3 != None:
                detay3efes = item.DetayTutar_3
               
             fobEfes = fobEfes + float(item.FobTutar) +float(navlunefes) + float(detay1efes) + float(detay2efes) + float(detay3efes) 
           

        
        for item  in result_4 :
             if item.NavlunSatis != None:
                 navlunefeshepsi = item.NavlunSatis
             if item.DetayTutar_1 != None:
                detay1efeshepsi = item.DetayTutar_1
             if item.DetayTutar_2 != None:
                detay2efeshepsi = item.DetayTutar_2
             if item.DetayTutar_3 != None:
                detay3efeshepsi = item.DetayTutar_3
             
             fobEfesHepsi = fobEfesHepsi + float(item.FobTutar) + float(navlunefeshepsi)+ float(detay1efeshepsi) + float(detay2efeshepsi) + float(detay3efeshepsi) 

        mekmarYil,hepsiYil = self.__yuklemeFarklarYillik()
        mekmarAy,hepsiAy = self.__yuklemeFarklarYillikAy()
       
        mekmarFarkYil = (fobTutar / mekmarYil ) * 100
        hepsiFarkYil = (fobTutarHepsi / hepsiYil) * 100
        #şimdiye kadar geçen ay toplamı
        mekmarFarkAy =( fobTutar / mekmarAy) * 100
        hepsiFarkAy = (fobTutar / hepsiAy) * 100

        return fobTutar,fobTutarHepsi,fobEfes,fobEfesHepsi,round(mekmarFarkYil,2),round(hepsiFarkYil,2),round(mekmarFarkAy,2),round(hepsiFarkAy,2)

    def getYillikOrtalama(self):

        

        result_1 = self.data.getList(
            """
             select 
	
                sum(su.SatisToplam) as FobTutar
            from
                SiparislerTB s,SiparisUrunTB su

            where
                YEAR(s.YuklemeTarihi) = YEAR(GETDATE()) and 
                MONTH(s.YuklemeTarihi) <= MONTH(GETDATE()) and 
                s.SiparisDurumID=3 and 
                s.SiparisNo = su.SiparisNo and 
                su.musteriID in (select Id from MusterilerTB where Marketing='Mekmar')

            group by 
                YEAR(s.YuklemeTarihi),MONTH(s.YuklemeTarihi)
            
            """ #mekmar yuklenen ortlaması
        )
        result_1_navlun = self.data.getList(
            """
             select 
                sum(s.NavlunSatis) + sum(s.DetayTutar_1) + sum(s.DetayTutar_2) + sum(s.DetayTutar_3) +sum(s.DetayTutar_4)  as Navlun
            from
                SiparislerTB s

            where
                YEAR(s.YuklemeTarihi) = YEAR(GETDATE()) and 
                MONTH(s.YuklemeTarihi) <= MONTH(GETDATE()) and 
                s.SiparisDurumID=3 and 
                s.MusteriID in (select Id from MusterilerTB where Marketing='Mekmar')

            group by 
                YEAR(s.YuklemeTarihi),MONTH(s.YuklemeTarihi)
            
            """ #mekmar yuklenen ortlaması
        )
        
        
        
        result_2 = self.data.getList(
            """
            select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam) + dbo.Yukleme_Aylik_Navlun_Tutar(Year(s.YuklemeTarihi))  
            as FobTutar,  
            Month(GetDate())-1 as Ay  
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID   
            and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
            and Year(s.YuklemeTarihi)= Year(GetDate())  
            and MONTH(s.YuklemeTarihi)< Month(GetDate())  
            group by Year(s.YuklemeTarihi) , MONTH(s.YuklemeTarihi)  
            
            """ #tum  yuklenen ortlaması
        )
        result_3 = self.data.getList(
          """
                   select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam) + dbo.Yukleme_Aylik_Navlun_Tutar(Year(s.YuklemeTarihi))  
            as FobTutar,  
            Month(GetDate())-1 as Ay  
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID and m.Marketing in  
            ('Mekmar') and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
            and s.FaturaKesimTurID = 2  
            and Year(s.YuklemeTarihi)= Year(GetDate())  
            and MONTH(s.YuklemeTarihi)< Month(GetDate())  
            group by Year(s.YuklemeTarihi) , MONTH(s.YuklemeTarihi)  
          
          """ #efes mekmar  yuklenen ortlaması
        )
        result_4 = self.data.getList(
            """
            select  
            Year(s.YuklemeTarihi) as Yil,  
            Sum(u.SatisToplam)   
            as FobTutar,  
            Month(GetDate())-1 as Ay  
            from  
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u  
            where  
            s.MusteriID=m.ID   
            and s.SiparisNo=u.SiparisNo  
            and s.SiparisDurumID = 3  
            and s.FaturaKesimTurID = 2  
            and Year(s.YuklemeTarihi)= Year(GetDate())  
            and MONTH(s.YuklemeTarihi)< Month(GetDate())  
            group by Year(s.YuklemeTarihi) , MONTH(s.YuklemeTarihi)  
            """ #efes   yuklenen ortlaması
        )

        fobTutar = 0
        fobTutarHepsi = 0
        fobEfes = 0
        fobEfesHepsi = 0

        for item in result_1:
            fobTutar += float(item.FobTutar)
        for item in result_1_navlun:
            fobTutar += float(item.Navlun)
            
        for item in result_2:
            fobTutarHepsi = float(item.FobTutar)

        for item in result_3:
            fobEfes += float(item.FobTutar)

        for item in result_4:
            fobEfesHepsi = float(item.FobTutar)    

       
        yortlamaMekmarAy = (fobTutar / datetime.datetime.now().month)
        yortalamaHepsiAy = (fobTutarHepsi / datetime.datetime.now().month )

        yortlamaEfesAy = (fobEfes / datetime.datetime.now().month) 
        yortalamaEfesHepsiAy = (fobEfesHepsi / datetime.datetime.now().month)  
        
        

        yortalamaMekmarYillik = (yortlamaMekmarAy ) * 12
        yortalamaHepsiYillik = (yortalamaHepsiAy ) * 12

        yortalamaEfesYillik = (yortlamaEfesAy ) * 12
        yortalamaEfesHepsiYillik = (yortalamaEfesHepsiAy ) * 12

        return round(yortlamaMekmarAy,2),round(yortalamaHepsiAy,2),round(yortalamaMekmarYillik,2),round(yortalamaHepsiYillik,2),round(yortlamaEfesAy,2),round(yortalamaHepsiAy,2),round(yortalamaEfesYillik,2),round(yortalamaEfesHepsiYillik,2)

    def getGecenYillikDtp(self):
     
        result_1 = self.data.getList(
            """
            select
            Sum(u.SatisToplam) as Ddp,
			s.NavlunSatis ,
			s.DetayTutar_1,
			s.DetayTutar_2,
			s.DetayTutar_3,
           
            s.SiparisNo
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
			 and m.Marketing in
            ('Mekmar')
            and Year(s.YuklemeTarihi) = Year(GetDate())-1
           
            group by Year(s.YuklemeTarihi),s.NavlunSatis ,
			s.DetayTutar_1,
			s.DetayTutar_2,
			s.DetayTutar_3,
           
            s.SiparisNo
            """
        )

        result_2 = self.data.getList(
            """
           select
         
            Sum(u.SatisToplam) as Ddp,
			s.NavlunSatis ,
			s.DetayTutar_1,
			s.DetayTutar_2,
			s.DetayTutar_3,
           
            s.SiparisNo
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi) = Year(GetDate())-1
         
            group by Year(s.YuklemeTarihi),s.NavlunSatis ,
			s.DetayTutar_1,
			s.DetayTutar_2,
			s.DetayTutar_3,
            
            s.SiparisNo
            """
        )
        GecenDdp = 0
        GecenDdpHepsi = 0
        navlun = 0
        detay1 = 0
        detay2 = 0
        detay3 = 0
       
        navlunhepsi = 0
        detay1hepsi = 0
        detay2hepsi = 0
        detay3hepsi = 0
       

        for key  in result_1 :
            if key.NavlunSatis != None:
                navlun = key.NavlunSatis
            if key.DetayTutar_1 != None:
                detay1 = key.DetayTutar_1
            if key.DetayTutar_2 != None:
                detay2 = key.DetayTutar_2
            if key.DetayTutar_3 != None:
                detay3 = key.DetayTutar_3
                
               
            GecenDdp = GecenDdp + float(key.Ddp) +float(navlun) + float(detay1) + float(detay2) + float(detay3) 
        
        for key  in result_2 :
            if key.NavlunSatis != None:
                navlunhepsi = key.NavlunSatis
            if key.DetayTutar_1 != None:
                detay1hepsi = key.DetayTutar_1
            if key.DetayTutar_2 != None:
                detay2hepsi = key.DetayTutar_2
            if key.DetayTutar_3 != None:
                detay3hepsi = key.DetayTutar_3
               
            GecenDdpHepsi = GecenDdpHepsi + float(key.Ddp) +float(navlunhepsi) + float(detay1hepsi) + float(detay2hepsi) + float(detay3hepsi) 

        

        return GecenDdp,GecenDdpHepsi

    def getBuYillikDtp(self):
     
        result_1 = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) + dbo.Yukleme_Yillik_Navlun_Tutar(Year(s.YuklemeTarihi))
            as Ddp
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi) = Year(GetDate())
            group by Year(s.YuklemeTarihi)
            """
        )

        result_2 = self.data.getList(
            """
             select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) + dbo.Yukleme_Yillik_Navlun_Tutar(Year(s.YuklemeTarihi))
            as Ddp
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi) = Year(GetDate())
            group by Year(s.YuklemeTarihi)
            """
        )
        BuDdp = 0
        BuDdpHepsi = 0
        if len(result_1) == 1:
            BuDdp = float(result_1[0].Ddp)

        if len(result_2) == 1:
            BuDdpHepsi = float(result_2[0].Ddp)

        return BuDdp,BuDdpHepsi

    
    def getGecenYillikFob(self):
     
        result_1 = self.data.getList(
            """
           select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) 
            as Fob
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi) = Year(GetDate())-1
            group by Year(s.SiparisTarihi)
            """
        )

        result_2 = self.data.getList(
            """
           select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) 
            as Fob
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
          
            and Year(s.SiparisTarihi) = Year(GetDate())-1
            group by Year(s.SiparisTarihi)
            """
        )
        gecen_peker = self.data.getList(
            """
           select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) 
            as Fob
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and s.MusteriID=7593 and s.YuklemeTarihi is null
            and Year(s.SiparisTarihi) = Year(GetDate())-1
            group by Year(s.SiparisTarihi)
            """
        )

        GecenFob = 0
        GecenFobHepsi = 0

        if len(result_1) == 1:
            GecenFob = float(result_1[0].Fob) - float(gecen_peker[0].Fob)

        if len(result_2) == 1:
            GecenFobHepsi = float(result_2[0].Fob) - float(gecen_peker[0].Fob)

        return GecenFob,GecenFobHepsi

    def getBuYillikFob(self):
     
        result_1 = self.data.getList(
            """
           select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) 
            as Fob
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
          
            and Year(s.SiparisTarihi) = Year(GetDate())
            group by Year(s.SiparisTarihi)
            """
        )

        result_2 = self.data.getList(
            """
           select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) 
            as Fob
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
          
            and Year(s.SiparisTarihi) = Year(GetDate())
            group by Year(s.SiparisTarihi)
            """
        )

        BuFob = 0
        BuFobHepsi = 0

        if len(result_1) == 1:
            BuFob = float(result_1[0].Fob)

        if len(result_2) == 1:
            BuFobHepsi = float(result_2[0].Fob)

        return BuFob,BuFobHepsi   

    def getAylikOrtalama(self):

        result_1 = self.data.getList(
              """ 
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
             Month(GetDate()) as Ay
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			
            and MONTH(s.SiparisTarihi)<= Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi)
            """
        )

        result_2 = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
             Month(GetDate())-1 as Ay
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			
            and MONTH(s.SiparisTarihi)< Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi)
            """
        )
        result_3 = self.data.getList(
              """ 
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
             Month(GetDate())-1 as Ay
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			
            and s.FaturaKesimTurID=2
            and MONTH(s.SiparisTarihi)< Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi)
            """
        )
        result_4 = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam)
            as FobTutar,
             Month(GetDate())-1 as Ay
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())
			
            and s.FaturaKesimTurID=2
            and MONTH(s.SiparisTarihi)< Month(GetDate())
            group by Year(s.SiparisTarihi),MONTH(s.SiparisTarihi)
            """
        )
        fobTutar = 0
        fobTutarHepsi = 0
        fobEfes = 0
        fobEfesHepsi = 0
      

        for item in result_1:
            fobTutar += float(item.FobTutar)
        for item in result_2:
            fobTutarHepsi = float(item.FobTutar)        
        for item in result_3:
            fobEfes += float(item.FobTutar)

        for item in result_4:
            fobEfesHepsi = float(item.FobTutar)    

       
        ortlamaMekmarAy = (fobTutar / datetime.datetime.now().month)

        ortalamaHepsiAy = (fobTutarHepsi / datetime.datetime.now().month) 

        ortalamaEfesAy = (fobEfes / datetime.datetime.now().month) 
        ortalamaEfesHepsiAy = (fobEfesHepsi / datetime.datetime.now().month) 
        

        ortalamaMekmarYillik = (ortlamaMekmarAy ) * 12
        ortalamaHepsiYillik = (ortalamaHepsiAy ) * 12

        ortalamaEfesYillik = (ortalamaEfesAy ) * 12
        ortalamaEfesHepsiYillik = (ortalamaEfesHepsiAy ) * 12

        return round(ortlamaMekmarAy,2),round(ortalamaHepsiAy,2),round(ortalamaMekmarYillik,2),round(ortalamaHepsiYillik,2),round(ortalamaEfesAy,2),round(ortalamaEfesHepsiAy,2),round(ortalamaEfesYillik,2),round(ortalamaEfesHepsiYillik,2)

       
    def getAylikAlacak(self):

        return self.finans.getAylikAlacakOzet()

    def getYillikAlacak(self):

        return self.finans.getYillilAlacakOzet()

    
    def getsiparisGrafikRapor(self):

        aylar = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']

        yeniSiparisResult = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as BuYil,
			Month(s.SiparisTarihi) as Ay,
            Year(s.SiparisTarihi) -1 as OncekiYil,
            Sum(u.SatisToplam) / 1000 as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())   
			and Month(s.SiparisTarihi)<=MONTH(GetDate())         
            group by Year(s.SiparisTarihi),Month(s.SiparisTarihi)
            order by Month(s.SiparisTarihi) asc
            """
        )
        yeniSiparisPekerResult = self.data.getList(
            """
             select
        	Year(s.SiparisTarihi) as BuYil,
			Month(s.SiparisTarihi) as Ay,
            Year(s.SiparisTarihi) -1 as OncekiYil,
            Sum(u.SatisToplam) / 1000 as FobTutar
			
			
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())   
			and Month(s.SiparisTarihi)<=MONTH(GetDate())   
			and s.MusteriID=273 and s.YuklemeTarihi is null
            group by Year(s.SiparisTarihi),Month(s.SiparisTarihi)
            order by Month(s.SiparisTarihi) asc
            """
        )
       
        simdikiData = list()
        siparisler = list()

        labels = list()
        if len(yeniSiparisResult) != 0:
         filterAy = yeniSiparisResult[len(yeniSiparisResult)-1].Ay
        else :
            filterAy = 1
        eskiSiparisResult = self.data.getStoreList(
            """
            select
            Year(s.SiparisTarihi) as BuYil,
			Month(s.SiparisTarihi) as Ay,
            Sum(u.SatisToplam) / 1000 as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate()) -1   
			and Month(s.SiparisTarihi)>=?      
            group by Year(s.SiparisTarihi),Month(s.SiparisTarihi)
            order by Month(s.SiparisTarihi) asc
            """,(filterAy)
        )
        eskiSiparisPekerResult = self.data.getStoreList(
            """
            select
            Year(s.SiparisTarihi) as BuYil,
			Month(s.SiparisTarihi) as Ay,
            Sum(u.SatisToplam) / 1000 as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate()) -1   
			and Month(s.SiparisTarihi)>=?   
            and s.MusteriID=273 and s.YuklemeTarihi is null   
            group by Year(s.SiparisTarihi),Month(s.SiparisTarihi)
            order by Month(s.SiparisTarihi) asc
            """,(filterAy)
        )

        for item in eskiSiparisResult:
            _tutar = str(item.FobTutar).split('.')[0]
            tutar = int(_tutar)
            
            #siparisler.append(float(item.FobTutar))
            ay = item.Ay 
            strAy = aylar[ay-1]
            strYil = str(item.BuYil)
            label =  strAy + '-' + strYil[2] + strYil[3]
            for key in eskiSiparisPekerResult : 
                ay = key.Ay 
                strAy = aylar[ay-1]
                strYil = str(key.BuYil)
                label2 =  strAy + '-' + strYil[2] + strYil[3]
                if key.Ay == item.Ay :
                    item.FobTutar =  item.FobTutar - key.FobTutar
            
            
            item.FobTutar = round(float(item.FobTutar))
            siparisler.append(item.FobTutar)        
            labels.append(label)

        for item in yeniSiparisResult:
            _tutar = str(item.FobTutar).split('.')[0]
            tutar = int(_tutar)
            
                  
            ay = item.Ay 
            strAy = aylar[ay-1]
            strYil = str(item.BuYil)
            label =  strAy + '-' + strYil[2] + strYil[3]
            for key in yeniSiparisPekerResult : 
                ay = key.Ay 
                strAy = aylar[ay-1]
                strYil = str(key.BuYil)
                label2 =  strAy + '-' + strYil[2] + strYil[3]
                if key.Ay == item.Ay :
                    item.FobTutar =  item.FobTutar - key.FobTutar
                    

            
            item.FobTutar = round(float(item.FobTutar))
            siparisler.append(item.FobTutar) 
            labels.append(label)

        yeniYuklenenResult = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as BuYil,
			Month(s.YuklemeTarihi) as Ay,
            Year(s.YuklemeTarihi) -1 as OncekiYil,
            Sum(u.SatisToplam) / 1000 as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.YuklemeTarihi)= Year(GetDate())   
			and Month(s.YuklemeTarihi)<=MONTH(GetDate())
			and s.SiparisDurumID=3         
            group by Year(s.YuklemeTarihi),Month(s.YuklemeTarihi)
            order by Month(s.YuklemeTarihi) asc

            """
        )
        if len(yeniYuklenenResult) != 0 :
         filterYuklenenAy = yeniYuklenenResult[len(yeniYuklenenResult)-1].Ay
        else :
            filterYuklenenAy = 1
        eskiYuklenenResult = self.data.getStoreList(
            """
            select
            Year(s.YuklemeTarihi) as BuYil,
			Month(s.YuklemeTarihi) as Ay,
            Sum(u.SatisToplam) / 1000 as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.YuklemeTarihi)= Year(GetDate()) -1
			and s.SiparisDurumID=3   
			and Month(s.YuklemeTarihi)>=?       
            group by Year(s.YuklemeTarihi),Month(s.YuklemeTarihi)
            order by Month(s.YuklemeTarihi) asc
            """,(filterYuklenenAy)
        )

        yuklenenler = list()
        
        for item in eskiYuklenenResult:
            _tutar = str(item.FobTutar).split('.')[0]
            tutar = int(_tutar)
            an = datetime.datetime.now()
            diger = self.__getAyOzet_MekmarYilToplam(an.year-1,item.Ay)
            
            diger = float(diger)/1000
           # yuklenenler.append(tutar)
            yuklenenler.append(round(diger))
        
        for item in yeniYuklenenResult:
            _tutar = str(item.FobTutar).split('.')[0]
            tutar = int(_tutar)
            an = datetime.datetime.now()
            diger = self.__getAyOzet_MekmarYilToplam(an.year,item.Ay)
            diger = float(diger)/1000
           # yuklenenler.append(tutar)
            yuklenenler.append(round(diger))

        datasets = list()

        datasets.append(
            {
                'label' : 'Siparişler',
                'data' : siparisler,
                'fiil' : False,
                'backgroundColor': '#2f4860',
                'borderColor': '#2f4860'

            }
        )
        datasets.append(
            {
                'label' : 'Yüklenenler',
                'data' : yuklenenler,
                'fiil' : False,
                'backgroundColor': '#00bb7e',
                'borderColor': '#00bb7e'
            }
        )
       
        lineData = {

            'labels' : labels,
            'datasets' : datasets
        }
      
        return lineData


    def getsiparisGrafikRaporHepsi(self):
        aylar = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']

        yeniSiparisResult = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as BuYil,
			Month(s.SiparisTarihi) as Ay,
            Year(s.SiparisTarihi) -1 as OncekiYil,
            Sum(u.SatisToplam) / 1000 as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())   
			and Month(s.SiparisTarihi)<=MONTH(GetDate())         
            group by Year(s.SiparisTarihi),Month(s.SiparisTarihi)
            order by Month(s.SiparisTarihi) asc
            """
        )
        yeniSiparisPekerResult = self.data.getList(
            """
             select
        	Year(s.SiparisTarihi) as BuYil,
			Month(s.SiparisTarihi) as Ay,
            Year(s.SiparisTarihi) -1 as OncekiYil,
            Sum(u.SatisToplam) / 1000 as FobTutar
			
			
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate())   
			and Month(s.SiparisTarihi)<=MONTH(GetDate())   
			and s.MusteriID=273 and s.YuklemeTarihi is null
            group by Year(s.SiparisTarihi),Month(s.SiparisTarihi)
            order by Month(s.SiparisTarihi) asc
            """
         )
        simdikiData = list()
        siparisler = list()

        labels = list()
        if len(yeniSiparisResult) != 0:
         filterAy = yeniSiparisResult[len(yeniSiparisResult)-1].Ay
        else :
            filterAy = 1
        eskiSiparisResult = self.data.getStoreList(
            """
            select
            Year(s.SiparisTarihi) as BuYil,
			Month(s.SiparisTarihi) as Ay,
            Sum(u.SatisToplam) / 1000 as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate()) -1   
			and Month(s.SiparisTarihi)>=?      
            group by Year(s.SiparisTarihi),Month(s.SiparisTarihi)
            order by Month(s.SiparisTarihi) asc
            """,(filterAy)
        )

        eskiSiparisPekerResult = self.data.getStoreList(
            """
            select
            Year(s.SiparisTarihi) as BuYil,
			Month(s.SiparisTarihi) as Ay,
            Sum(u.SatisToplam) / 1000 as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and Year(s.SiparisTarihi)= Year(GetDate()) -1   
			and Month(s.SiparisTarihi)>=?  
            and s.MusteriID=273 and s.YuklemeTarihi is null    
            group by Year(s.SiparisTarihi),Month(s.SiparisTarihi)
            order by Month(s.SiparisTarihi) asc
            """,(filterAy)
        )
        locale.setlocale( locale.LC_ALL, '' )
        for item in eskiSiparisResult:
            _tutar = str(item.FobTutar).split('.')[0]
           
           
            tutar = int(_tutar)
            #siparisler.append(tutar)
           
            
            
            ay = item.Ay 
            strAy = aylar[ay-1]
            strYil = str(item.BuYil)
            label =  strAy + '-' + strYil[2] + strYil[3]
            for key in eskiSiparisPekerResult : 
                ay = key.Ay 
                strAy = aylar[ay-1]
                strYil = str(key.BuYil)
                label2 =  strAy + '-' + strYil[2] + strYil[3]
                if key.Ay == item.Ay :
                    item.FobTutar =  item.FobTutar - key.FobTutar
            item.FobTutar = round(float(item.FobTutar)) 
            siparisler.append(item.FobTutar)       
            labels.append(label)

        for item in yeniSiparisResult:
            _tutar = str(item.FobTutar).split('.')[0]
            tutar = int(_tutar)
           # siparisler.append(tutar) 
            
            for key in yeniSiparisPekerResult : 
                ay = key.Ay 
                strAy = aylar[ay-1]
                strYil = str(key.BuYil)
                label2 =  strAy + '-' + strYil[2] + strYil[3]
                if key.Ay == item.Ay :
                    item.FobTutar =  item.FobTutar - key.FobTutar
            item.FobTutar = round(float(item.FobTutar))        
            siparisler.append(item.FobTutar)
            ay = item.Ay 
            strAy = aylar[ay-1]
            strYil = str(item.BuYil)
            label =  strAy + '-' + strYil[2] + strYil[3]
            labels.append(label)
           
          
        

        yeniYuklenenResult = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as BuYil,
			Month(s.YuklemeTarihi) as Ay,
            Year(s.YuklemeTarihi) -1 as OncekiYil,
            Sum(u.SatisToplam) / 1000 as FobTutar
         
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and Year(s.YuklemeTarihi)= Year(GetDate())   
			and Month(s.YuklemeTarihi)<=MONTH(GetDate())
			and s.SiparisDurumID=3         
            group by Year(s.YuklemeTarihi),Month(s.YuklemeTarihi)
            order by Month(s.YuklemeTarihi) asc

            """
        )
        if len(yeniYuklenenResult) != 0:
         filterYuklenenAy = yeniYuklenenResult[len(yeniYuklenenResult)-1].Ay
        else :
            filterYuklenenAy = 1
        eskiYuklenenResult = self.data.getStoreList(
            """
            select
            Year(s.YuklemeTarihi) as BuYil,
			Month(s.YuklemeTarihi) as Ay,
            Sum(u.SatisToplam) / 1000 as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and Year(s.YuklemeTarihi)= Year(GetDate()) -1
			and s.SiparisDurumID=3   
			and Month(s.YuklemeTarihi)>=?       
            group by Year(s.YuklemeTarihi),Month(s.YuklemeTarihi)
            order by Month(s.YuklemeTarihi) asc
            """,(filterYuklenenAy)
        )

        yuklenenler = list()

        for item in eskiYuklenenResult:
            _tutar = str(item.FobTutar).split('.')[0]
            tutar = int(_tutar)
            #yuklenenler.append(tutar)
            an = datetime.datetime.now()
            diger = self.__getAyOzet_gecenYilToplam(an.year-1,item.Ay)
            diger = float(diger)/1000 
            yuklenenler.append(round(float(diger)))
        
        for item in yeniYuklenenResult:
            _tutar = str(item.FobTutar).split('.')[0]
            tutar = int(_tutar)
           # yuklenenler.append(tutar)
            diger = self.__getAyOzet_gecenYilToplam(an.year,item.Ay)
            diger = float(diger)/1000 
            yuklenenler.append(round(float(diger)))


        ortalama = self.getYillikOrtalama()
        ortalama = ortalama[3]

        
       

        datasets = list()

        datasets.append(
            {
                'label' : 'Siparişler',
                'data' : siparisler,
                'fiil' : False,
                'backgroundColor': '#2f4860',
                'borderColor': '#2f4860'

            }
        )
        datasets.append(
            {
                'label' : 'Yüklenenler',
                'data' : yuklenenler,
                'fiil' : False,
                'backgroundColor': '#00bb7e',
                'borderColor': '#00bb7e'
            }
        )

       
        lineData = {

            'labels' : labels,
            'datasets' : datasets
        }
       
        return lineData




    def __getAyOzet_gecenYilToplam(self,yil,ay):

        result = self.data.getStoreList(
            """
            SELECT
            u.SiparisNo,
            sum(u.SatisToplam) as SatisToplam,
            s.YuklemeTarihi,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
           
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim 
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.YuklemeTarihi) = ? 
            and s.MusteriID in (Select m.ID from MusterilerTB m
			where m.ID=s.MusteriID )
            and Month(s.YuklemeTarihi)=?
            and s.SiparisDurumID=3
			group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3 ,s.MusteriID,s.TeslimTurID, s.YuklemeTarihi


            """,(yil ,ay)
        )

        navlun = 0
        diger_1 = 0
        diger_2 = 0
        diger_3 = 0
      
        mal_bedeli = 0
        a = 0

        for item in result:
          if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
              
          else:  

            if item.NavlunSatis != None:
                navlun += item.NavlunSatis 
            if item.DetayTutar_1 != None:
                diger_1 += item.DetayTutar_1
            if item.DetayTutar_2 != None:
                diger_2 += item.DetayTutar_2
            if item.DetayTutar_3 != None:
                diger_3 += item.DetayTutar_3 
            if item.SatisToplam != None:
                mal_bedeli += item.SatisToplam
           

            toplam = navlun + diger_1 + diger_2 + diger_3  +mal_bedeli

        return toplam     
       
    def __getAyOzet_MekmarYilToplam(self,yil,ay):

        result = self.data.getStoreList(
            """
            SELECT
            u.SiparisNo,
            sum(u.SatisToplam) as SatisToplam,
            s.YuklemeTarihi,
            s.DetayTutar_1,
            s.NavlunSatis,
            s.DetayTutar_2,
            s.DetayTutar_3 ,
           
            (select m.FirmaAdi from MusterilerTB m where m.ID=s.MusteriID) as musteri ,
            (select t.TeslimTur from SiparisTeslimTurTB  t where t.ID=s.TeslimTurID) as Teslim 
            FROM SiparisUrunTB u INNER JOIN SiparislerTB s ON u.SiparisNo=s.SiparisNo 
            where 
            s.SiparisNo=u.SiparisNo
            and YEAR(s.YuklemeTarihi) = ? 
            and s.MusteriID in (Select m.ID from MusterilerTB m
			where m.ID=s.MusteriID and  m.Marketing='Mekmar')
            and Month(s.YuklemeTarihi)=?
            and s.SiparisDurumID=3
			group by u.SiparisNo,s.DetayTutar_1,s.NavlunSatis,s.DetayTutar_2,s.DetayTutar_3 ,s.MusteriID,s.TeslimTurID, s.YuklemeTarihi


            """,(yil ,ay)
        )

        navlun = 0
        diger_1 = 0
        diger_2 = 0
        diger_3 = 0
      
        mal_bedeli = 0
        a = 0

        for item in result:
          if (item.musteri == 'Cem-Mer (PEKER)' and item.YuklemeTarihi == None ) :
                  a +=1
              
          else:  

            if item.NavlunSatis != None:
                navlun += item.NavlunSatis 
            if item.DetayTutar_1 != None:
                diger_1 += item.DetayTutar_1
            if item.DetayTutar_2 != None:
                diger_2 += item.DetayTutar_2
            if item.DetayTutar_3 != None:
                diger_3 += item.DetayTutar_3 
            if item.SatisToplam != None:
                mal_bedeli += item.SatisToplam
           

            toplam = navlun + diger_1 + diger_2 + diger_3  +mal_bedeli

        return toplam  
           
    def getUretimList(self):

        mekmar =  self.uretim.getUretimMekmarList()
        hepsi = self.uretim.getUretimHepsiList()

        return mekmar,hepsi

    def getMusteriUretimList(self):

        mekmar = self.uretim.getMusteriUretimMekmarList()
        hepsi = self.uretim.getMusteriUretimHepsiList()

        return mekmar,hepsi
    
    def __siparisFarklarAylik(self):
        
        gecenAyResultMekmar = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.SiparisTarihi)= Year(GetDate()) - 1
            and MONTH(s.SiparisTarihi)= Month(GetDate())
            group by Year(s.SiparisTarihi)
            """
        )       
        gecenAyResultHepsi = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.SiparisTarihi)= Year(GetDate()) - 1
            and MONTH(s.SiparisTarihi)= Month(GetDate())
            group by Year(s.SiparisTarihi)
            """
        )      
        ayMekmar = 0       
        ayHepsi = 0
      

        if len(gecenAyResultMekmar) == 1:
            ayMekmar = float(gecenAyResultMekmar[0].FobTutar)      
        if len(gecenAyResultHepsi) == 1:
            ayHepsi = float(gecenAyResultHepsi[0].FobTutar)       

        return ayMekmar,ayHepsi

    def __siparisFarklarYillik(self):
        
        
        gecenYilResultMekmar = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.SiparisTarihi)= Year(GetDate()) - 1
            group by Year(s.SiparisTarihi)
            """
        )        
        gecenYilResultHepsi = self.data.getList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.SiparisTarihi)= Year(GetDate()) - 1
            group by Year(s.SiparisTarihi)
            """
        )
      
        yilMekmar = 0     
        yilHepsi = 0
       
        if len(gecenYilResultMekmar) == 1:
            yilMekmar = float(gecenYilResultMekmar[0].FobTutar)       
        if len(gecenYilResultHepsi) == 1:
            yilHepsi = float(gecenYilResultHepsi[0].FobTutar)

        return yilMekmar,yilHepsi

    def __siparisFarklarYillikAy(self):
        
        buAy = datetime.datetime.now().month
        gecenYilResultMekmar = self.data.getStoreList(
            """
            select
            Year(s.SiparisTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.SiparisTarihi)= Year(GetDate()) - 1
            and Month(s.SiparisTarihi)<=?
            group by Year(s.SiparisTarihi)
            """,(buAy)
        )        
        gecenYilResultHepsi = self.data.getStoreList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi)= Year(GetDate()) - 1
            and Month(s.YuklemeTarihi)<=?
            group by Year(s.YuklemeTarihi)
            """,(buAy)
        )
      
        yilMekmar = 0     
        yilHepsi = 0
       
        if len(gecenYilResultMekmar) == 1:
            yilMekmar = float(gecenYilResultMekmar[0].FobTutar)       
        if len(gecenYilResultHepsi) == 1:
            yilHepsi = float(gecenYilResultHepsi[0].FobTutar)

        return yilMekmar,yilHepsi
            
    def __yuklemeFarklarAylik(self):
        
        gecenAyResultMekmar = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi)= Year(GetDate()) - 1
            and MONTH(s.YuklemeTarihi)= Month(GetDate())
            group by Year(s.YuklemeTarihi)
            """
        )       
        gecenAyResultHepsi = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi)= Year(GetDate()) - 1
            and MONTH(s.YuklemeTarihi)= Month(GetDate())
            group by Year(s.YuklemeTarihi)
            """
        )      
        ayMekmar = 0       
        ayHepsi = 0
      

        if len(gecenAyResultMekmar) == 1:
            ayMekmar = float(gecenAyResultMekmar[0].FobTutar)      
        if len(gecenAyResultHepsi) == 1:
            ayHepsi = float(gecenAyResultHepsi[0].FobTutar)       

        return ayMekmar,ayHepsi

    def __yuklemeFarklarYillik(self):
        
        
        gecenYilResultMekmar = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar') and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi)= Year(GetDate()) - 1
            group by Year(s.YuklemeTarihi)
            """
        )        
        gecenYilResultHepsi = self.data.getList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID  and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi)= Year(GetDate()) - 1
            group by Year(s.YuklemeTarihi)
            """
        )
      
        yilMekmar = 0     
        yilHepsi = 0
       
        if len(gecenYilResultMekmar) == 1:
            yilMekmar = float(gecenYilResultMekmar[0].FobTutar)       
        if len(gecenYilResultHepsi) == 1:
            yilHepsi = float(gecenYilResultHepsi[0].FobTutar)

        return yilMekmar,yilHepsi

    def getSiparisUretim(self):
        
        
        result = self.data.getList(
            """
             select  
            s.SiparisTarihi, 
            s.SiparisNo,  
       
            (select Sum(SatisToplam) from SiparisUrunTB su where su.SiparisNo=s.SiparisNo) as Fob,  
            (select Sum(SatisToplam) from SiparisUrunTB su where su.SiparisNo=s.SiparisNo)+  
            dbo.Get_SiparisNavlun(s.SiparisNo) as Dtp
            
            from  
            SiparislerTB s,MusterilerTB m  
            where Year(SiparisTarihi)=Year(GetDate())
            and Month(SiparisTarihi)= MONTH(GetDate())
            and m.ID=s.MusteriID  
			and s.SiparisDurumID=2
            and m.Marketing not in ('Mekmar Numune','Seleksiyon','Warehouse')  
            and m.Marketing is not null  
            and m.ID not in(2400,1349)  
            union  
            select  
            s.Tarih as SiparisTarihi,  
            s.CikisNo as SiparisNo, 
			Sum(Toplam) as Fob 
		
            ,Sum((s.BirimFiyat+7.5)*u.Miktar) as Dtp
           
            from  
            SevkiyatTB s,MusterilerTB m,UretimTB u  
            where s.MusteriID=m.ID and u.KasaNo=s.KasaNo  
            and Year(s.Tarih)=Year(GetDate()) and Month(s.Tarih)= MONTH(GetDate())
            and m.Mt_No=1  
            group by  
            s.Tarih,s.CikisNo,m.FirmaAdi,m.Marketing  
			order by   s.SiparisTarihi  desc
            """
        )        
     
        Order = 0     
        Fob = 0
        Ddp = 0
       
        for item in result:
             Order = item.SiparisNo
             Fob = item.Fob
             Ddp = item.Ddp

       

        return Order,Fob,Ddp

    def __yuklemeFarklarYillikAy(self):
        
        buAy = datetime.datetime.now().month
        gecenYilResultMekmar = self.data.getStoreList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar','BD','SU') and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi)= Year(GetDate()) - 1
            and Month(s.YuklemeTarihi)<=?
            group by Year(s.YuklemeTarihi)
            """,(buAy)
        )        
        gecenYilResultHepsi = self.data.getStoreList(
            """
            select
            Year(s.YuklemeTarihi) as Yil,
            Sum(u.SatisToplam) as FobTutar
            from
            SiparislerTB s,MusterilerTB m,SiparisUrunTB u
            where
            s.MusteriID=m.ID and m.Marketing in
            ('Mekmar','BD','SU','Ghana','İç Piyasa') and s.SiparisNo=u.SiparisNo
            and s.SiparisDurumID = 3
            and Year(s.YuklemeTarihi)= Year(GetDate()) - 1
            and Month(s.YuklemeTarihi)<=?
            group by Year(s.YuklemeTarihi)
            """,(buAy)
        )
      
        yilMekmar = 0     
        yilHepsi = 0
       
        if len(gecenYilResultMekmar) == 1:
            yilMekmar = float(gecenYilResultMekmar[0].FobTutar)       
        if len(gecenYilResultHepsi) == 1:
            yilHepsi = float(gecenYilResultHepsi[0].FobTutar)

        return yilMekmar,yilHepsi

    def __getAyStr(self,ay):

        aylar = ['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']

        return aylar[ay - 1]      
            

class AnasayfaAyrintiSevk(Resource):

    def get(self,firmaadi):

        islem = Sevkiyat()
        islem1 = Uretim()

        ayrinti_listesi = islem.getSevkiyatAyrintiListYukleMekmar(firmaadi) #sevkiyat mekmar
        hepsi_ayrinti_listesi = islem.getSevkiyatAyrintiListYukleHepsi(firmaadi)  #sevkiyat hepsi
        uretim_ayrinti = islem1.getUretimAyrintiListYukleMekmar(firmaadi) #uretim mekmar
        hepsi_uretim_ayrinti = islem1.getUretimAyrintiListYukleHepsi(firmaadi) # uretim hepsi
        musteri_ayrinti_mekmar = islem1.getMusteriAyrintiListYukleMekmar(firmaadi) #musteri mekmar
        musteri_ayrinti_hepsi = islem1.getMusteriAyrintiListYukleHepsi(firmaadi) # musteri hepsi
       

            
        data = {

            "ayrinti_listesi" : ayrinti_listesi,
            "hepsi_ayrinti_listesi" : hepsi_ayrinti_listesi,
            "uretim_ayrinti" : uretim_ayrinti,
            "hepsi_uretim_ayrinti" :hepsi_uretim_ayrinti,
            "musteri_ayrinti_mekmar" : musteri_ayrinti_mekmar,
            "musteri_ayrinti_hepsi" :musteri_ayrinti_hepsi
         
         
        }
       
        return jsonify(data)

class AnasayfaAyrintiTeklifler(Resource):

    def get(self,kullaniciAdi):

        islem = TeklifRapor()
       

        aylik_teklif__ayrinti = islem.getTeklifAylikAyrintiList(kullaniciAdi) #aylik teklif ayrinti_listesi
        

            
        data = {

            "aylik_teklif__ayrinti" : aylik_teklif__ayrinti
         
         
        }
       
        return jsonify(data)   

class AnasayfaAyrintiSiparisler(Resource):

    def get(self):

      
        islem1 = Uretim()

        
        siparis_ayrinti_yil = islem1.getGelenSipYilListYukleHepsi() ##gelen sipariş yıllık - hepsi
        siparis_ayrinti_ay = islem1.getGelenSipAyListYukleHepsi() # aylik - hepsi 
        #efes
        sevk_ay_hepsi_efes= islem1.getGelenSevkAyEfesYukleHepsi()
        sevk_ay_mekmar_efes= islem1.getGelenSevkAyEfesYukle()
        sevk_yil_mekmar_efes= islem1.getGelenSevkYilEfesYukle()
        sevk_yil_hepsi_efes= islem1.getGelenSevkYilEfesYukleHepsi()
        sip_yil_hepsi_efes = islem1.getGelenSipYilEfesYukleHepsi()
        sip_yil_mekmar_efes = islem1.getGelenSipYilEfesYukle()
        sip_ay_mekmar_efes = islem1.getGelenSipAyEfesYukle()
        sip_ay_hepsi_efes= islem1.getGelenSipAyEfesYukleHepsi()
      


            
        data = {

          
            "siparis_ayrinti_yil" : siparis_ayrinti_yil,
            "siparis_ayrinti_ay" : siparis_ayrinti_ay,
            "sevk_ay_hepsi_efes" : sevk_ay_hepsi_efes,
            "sevk_ay_mekmar_efes" : sevk_ay_mekmar_efes,
            "sevk_yil_mekmar_efes" :sevk_yil_mekmar_efes,
            "sevk_yil_hepsi_efes" : sevk_yil_hepsi_efes,
            "sip_yil_hepsi_efes" : sip_yil_hepsi_efes,
            "sip_yil_mekmar_efes" : sip_yil_mekmar_efes,
            "sip_ay_mekmar_efes" : sip_ay_mekmar_efes,
            "sip_ay_hepsi_efes" : sip_ay_hepsi_efes

          }
       
        return jsonify(data)   

class AnasayfaTakipListesi(Resource):

    def get(self):

      
        islem = Uretim()

        
        mekmar_takiplist = islem.getMekmarTakipListesi() 
        hepsi_takiplist = islem.getHepsiTakipListesi() 
       
        data = {

          
            "mekmar_takiplist" : mekmar_takiplist,
            "hepsi_takiplist" : hepsi_takiplist,
         
           }
       
        return jsonify(data)   
         
   
      
         
   
