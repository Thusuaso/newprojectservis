

import urllib.request,ssl # Websitesinden veri cekmek ve ssl sertifikasini es gecmek
import xml.etree.ElementTree as ET # Xml yapisini ayristirmak

import datetime
class DovizListem:

    def __init__(self):

        pass

    def getDovizKurListe(self,yil,ay,gun):
        is_day = datetime.datetime(yil,ay,gun)
        is_day = is_day.strftime("%a")
        now = datetime.datetime.now()
        nowgun = now.strftime("%d")
        if int(nowgun) == int(gun):
            gun = int(gun) - 1
            is_day2 = datetime.datetime(yil,ay,gun)
            is_day2 = is_day2.strftime("%a")
            
            
            if(is_day2 == 'Sun'):
                gun = int(gun) - 2
            else:
                gun = int(gun)
        
        
        
        if is_day == 'Sat':
            gun = gun - 1
        
        
        yil = str(yil)
        ay = str(ay)
        gun = str(gun)
        # SSl sertifikasi hatalarini engellemek
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        if len(gun) ==1:
            gun = "0"+ gun
        if len(ay) ==1:
            ay = "0"+ ay
       # URL = "https://www.tcmb.gov.tr/kurlar/202111/02112021.xml"
        URL = "https://www.tcmb.gov.tr/kurlar/"+yil+ay+"/"+gun+ay+yil+".xml"
       
        cross_dolar = 0
        # Websitesinden veri cekmek
        body = urllib.request.urlopen(URL,context=ctx)
        data = body.read().decode()
        # Xml dosyasini ayristirmak
        xml = ET.fromstring(data)
        for currency in xml:
         for child in currency:
            if (child.tag == 'CrossRateOther' and currency.get("Kod") == "EUR"):
                cross_dolar = float(child.text)
                print(cross_dolar)
        
            else:
             continue
        return format(cross_dolar)
    




        

        