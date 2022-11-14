from helpers import MailService, SqlConnect, TarihIslemler

import datetime


class UretimTakipMail:

    def __init__(self):
        self.data = SqlConnect().data
     

    def uretimKontrol(self):
        result = self.data.getList(
            """ 
              select 
                s.SiparisTarihi ,
                s.SiparisDurumID,
                s.ID,
                s.SiparisNo,
                u.Miktar,   
                (select BirimAdi from UrunBirimTB t  where t.ID=u.UrunBirimID) as UrunBirimi,
                (select k.FirmaAdi from TedarikciTB k where k.ID=u.TedarikciID) as Tedarikci,
                u.UretimAciklama ,
                (select m.UrunAdi from UrunlerTB m where m.ID = n.UrunID) as urunadi,
                (select y.YuzeyIslemAdi from YuzeyKenarTB y where y.ID=n.YuzeyID) as yuzeyadi ,
                (select o.En  from OlculerTB o where o.ID=n.OlcuID) as En,
                (select o.Boy from OlculerTB o where o.ID=n.OlcuID) as Boy,
                (select o.Kenar  from OlculerTB o where o.ID=n.OlcuID) as Kenar,
                (select p.KullaniciAdi  from KullaniciTB p where p.ID=s.SiparisSahibi) as SiparisSahibi
              
                from
                SiparisUrunTB u ,SiparislerTB s ,UrunKartTB n 
                
                where 
                s.SiparisNo= u.SiparisNo 
                and u.UrunKartID = n.ID
                and (s.SiparisDurumID=2)
                and s.KayitTarihi = CURRENT_TIMESTAMP
                order by s.SiparisTarihi desc
          
           """
        )
      
        body = """
        <table >
            <tr style ="background-color: #f2f2f2;">
                <th style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 50px;">
                Sipariş Numarası
                </th>
                <th style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Tedarikçi
                </th>
                <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                Ürün Bilgisi 
                </th>
                 <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 150px;">
                Üretim Açıklama 
                </th>
                 <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 Ürün Miktarı
                </th>
                
                <th  style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                 Sipariş Temsilcisi
                </th>
            </tr>
        """
         

        for item in result:
          
            body += f"""
           
            <tr style ="background-color: #ddd;">
                <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                   {item.SiparisNo}
                </td>
                <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                  {item.Tedarikci}
                </td>
                <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                  {item.urunadi} {item.yuzeyadi} {item.En}x{item.Boy}x{item.Kenar}
                </td>
                 <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 150px;">
                  {item.UretimAciklama}
                </td>
                 <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                  {item.Miktar} {item.UrunBirimi} 
                </td>
                 <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                  {item.SiparisSahibi} 
                </td>
            </tr>
           
          
              """
         
        body = body + "</table>"
        for item in result:
     
              MailService("Yeni Sipariş - Mekmer", "arifeekirgiz@hotmail.com", body)
              MailService("Yeni Sipariş - Mekmer", "bilgiislem@mekmar.com", body)
           

    def tedarikciKontrol(self):

       
        result = self.data.getList(
            """
            select
		       s.SiparisNo,
		       s.SiparisTarihi,
		       DATEADD(day,+4 ,SiparisTarihi) AS "birhafta"
           from
           SiparisUrunTB u ,SiparislerTB s 
           where 
           s.SiparisNo= u.SiparisNo 
           and (s.SiparisDurumID=2)
           and u.TedarikciID = 32
		       and   Year(DATEADD(day,+4 ,SiparisTarihi)) = Year(GetDate())
		       and   Month(DATEADD(day,+4,SiparisTarihi)) = month(GetDate())
		       and   day(DATEADD(day,+4,SiparisTarihi)) = day(GetDate())
		       group by s.SiparisNo,s.SiparisTarihi
           order by s.SiparisTarihi desc
				
            """
        )
        body = "" 
        for item in result:
         body = f"""
                        <ul>
                            <li style ="color: Red; font-weight: bold; ">  {item.SiparisNo}  </li> Siparişinde  tedarikçisi ayarlanmayan kalem(-ler) mevcuttur , lütfen kontrol ediniz . 
                        </ul>
                       """
       
        MailService("Tedarikçi Ayarlanmamış Sipariş Bildirimi", "info@mekmar.com", body)
      

               
   
  