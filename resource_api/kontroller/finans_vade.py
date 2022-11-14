from helpers import MailService,SqlConnect,TarihIslemler
import datetime


class FinansVade:

    def __init__(self):

        self.data = SqlConnect().data

    
    def vadeKontrol(self):

        tarihIslem = TarihIslemler()
        result = self.data.getList(
            """
           select  
                m.FirmaAdi  ,
                dbo.Get_Siparis_Bakiye_Tutar(s.SiparisNo) as tutar,
                s.SiparisNo,
                s.Vade,
                (select k.MailAdres from KullaniciTB k where s.SiparisSahibi = k.ID) as MailAdres,
				s.VadeKalanSureOn,
				s.VadeKalanSureBes,
				s.VadeKalanSureBir
                
                from  
                SiparislerTB s,MusterilerTB m  
                where   
                s.MusteriID = m.ID  
                and s.SiparisDurumID=3  
                and s.Vade is not null  
                and dbo.Get_Siparis_Bakiye_Tutar(s.SiparisNo)>0  
                group by m.FirmaAdi  ,s.SiparisNo,s.Vade,s.SiparisSahibi,s.VadeKalanSureOn,s.VadeKalanSureBes,s.VadeKalanSureBir
            """
        )
        
        
        body = ""        
        subject = "Vadesi Yaklaşan Sipariş Bildirimi"
        for item in result:
            vade = tarihIslem.getDate(item.Vade).strftime("%d-%m-%Y")
            bugun = datetime.date.today()
            sontarih_str = vade.split('-')
          
            sontarih = datetime.date(int(sontarih_str[2]),int(sontarih_str[1]),int(sontarih_str[0]))
            kalan_sure = (sontarih - bugun).days
            kalanSureOn=item.VadeKalanSureOn
            kalanSureBes =item.VadeKalanSureBes
            kalanSureBir = item.VadeKalanSureBir
            if kalan_sure ==10 and kalanSureOn == None:
                
                body = f"""
                        <ul>
                            <li> {item.FirmaAdi} / {item.SiparisNo} / {vade}  / {item.tutar}</li>
                        </ul>
                       """
                self.data.update_insert("""
                                            update SiparislerTB SET VadeKalanSureOn=? WHERE SiparisNo=?
                                        
                                        
                                        """,(1,item.SiparisNo))
                MailService(subject,item.MailAdres,body)
                  #  MailService(subject,"mehmet@mekmer.com",body)
                MailService(subject,"huseyin@mekmarmarble.com",body)
                MailService(subject,"bilgiislem@mekmar.com",body)

                
            elif kalan_sure == 5 and kalanSureBes==None:
                body = f"""
                        <ul>
                            <li> {item.FirmaAdi} / {item.SiparisNo} / {vade}  / {item.tutar}</li>
                        </ul>
                       """
                self.data.update_insert("""
                                            update SiparislerTB SET VadeKalanSureBes=? WHERE SiparisNo=?
                                        
                                        
                                        """,(1,item.SiparisNo))
                MailService(subject,item.MailAdres,body)
                  #  MailService(subject,"mehmet@mekmer.com",body)
                MailService(subject,"huseyin@mekmarmarble.com",body)
                MailService(subject,"bilgiislem@mekmar.com",body)

            elif kalan_sure==1 and kalanSureBir==None:
                body = f"""
                        <ul>
                            <li> {item.FirmaAdi} / {item.SiparisNo} / {vade}  / {item.tutar}</li>
                        </ul>
                       """
                self.data.update_insert("""
                                            update SiparislerTB SET VadeKalanSureBir=? WHERE SiparisNo=?
                                        
                                        
                                        """,(1,item.SiparisNo))
                MailService(subject,item.MailAdres,body)
                  #  MailService(subject,"mehmet@mekmer.com",body)
                MailService(subject,"huseyin@mekmarmarble.com",body)
                MailService(subject,"bilgiislem@mekmar.com",body)

                

     

  