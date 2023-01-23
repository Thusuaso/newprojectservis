

import urllib.request,ssl # Websitesinden veri cekmek ve ssl sertifikasini es gecmek
import xml.etree.ElementTree as ET # Xml yapisini ayristirmak
import datetime

class DovizListem:

    def __init__(self):

        pass

    def getDovizKurListe(self,yil,ay,gun):
        # SSl sertifikasi hatalarini engellemek
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        x = datetime.datetime.now()
        nowDay = x.strftime('%d')
        xy = datetime.datetime(int(yil),int(ay),int(gun))
        if (xy.strftime("%A") == "Saturday"):
            gun = str(int(gun) - 1)
            

        if(int(nowDay) == int(gun)):
            
            return
        else:
            if len(gun) ==1:
                gun = "0" + gun
            if len(ay) ==1:
                ay = "0"+ ay
        
           
        # URL = "https://www.tcmb.gov.tr/kurlar/202111/02112021.xml"
        URL = "https://www.tcmb.gov.tr/kurlar/"+yil+ay+"/"+gun+ay+yil+".xml"
    
        dolar = 0
        # Websitesinden veri cekmek
        body = urllib.request.urlopen(URL,context=ctx)
        data = body.read().decode()

        # Xml dosyasini ayristirmak
        xml = ET.fromstring(data)
        for currency in xml:
            for child in currency:
                if(child.tag == "BanknoteSelling" and currency.get("Kod") == "USD"):
                    dolar = float(child.text)
                
            
                else:
                    continue
        return format(dolar)
        
        


        

        