from helpers import MailService,SqlConnect,TarihIslemler
import datetime


class SiparisTahminiYukleme:

    def __init__(self):

        self.data = SqlConnect().data

    
    def tahminiTarihKontrol(self):

        tarihIslem = TarihIslemler()
        result = self.data.getList(
            """
           select
            s.ID,
            s.SiparisNo,
           
            (select k.MailAdres from KullaniciTB k where k.ID=s.SiparisSahibi ) as MailAdres,   
			 (select k.MailAdres from KullaniciTB k where k.ID=s.Operasyon ) as MailAdresOperasyon, 
            (select k.KullaniciAdi from KullaniciTB k where k.ID=s.SiparisSahibi ) as Sorumlu,
			 (select k.KullaniciAdi from KullaniciTB k where k.ID=s.Operasyon ) as Operasyon,
            s.TahminiYuklemeTarihi
           
            from
            SiparislerTB s,MusterilerTB m
            where s.MusteriID=m.ID
            and s.SiparisDurumID=2 
			
            order by s.ID desc
            """
        )

        
        body = ""        
        subject = " Yükleme Tarihi Yaklaşan Sipariş  Bildirimi"
        for item in result:
            tarih = tarihIslem.getDate(item.TahminiYuklemeTarihi).strftime("%d-%m-%Y")
            bugun = datetime.date.today()
            sontarih_str = tarih.split('-')
            
            sontarih = datetime.date(int(sontarih_str[2]),int(sontarih_str[1]),int(sontarih_str[0]))
            kalan_sure = (sontarih - bugun).days

            if kalan_sure ==10  or kalan_sure ==5 or kalan_sure ==1 :
                
                body = f"""
                        <ul>
                            <li> {item.MusteriAdi} / {item.SiparisNo} / {tarih} </li>
                        </ul>
                       """
                if self.__mailKontrol(item.Sorumlu,item.Operasyon,item.SiparisNo,bugun) == True:

                    MailService(subject,"bilgiislem@mekmar.com",body)


        self.etaBosKontrol()

    


    def __mailKontrol(self,kullaniciadi,siparisno,tarih):

        bugun = datetime.date.today()
        durum = self.data.getStoreList(
            """
            select count(*) as durum from MusteriEtaTakipTB where 
            KullaniciAdi=? and SiparisNo=? and Tarih=?
            """,
            (kullaniciadi,siparisno,bugun)
        )[0].durum

        if durum > 0:
            return False 
        else:
            #daha önce kayıt varsa silinmesi
            self.data.update_insert(
                """
                delete from MusteriEtaTakipTB where SiparisNo=?
                """,
                (siparisno)
            )
            self.data.update_insert(
                """
                insert into MusteriEtaTakipTB (KullaniciAdi,Tarih,SiparisNo)
                values
                (?,?,?) 
                """,
                (kullaniciadi,tarih,siparisno)
            )

            return True

    

     
       


