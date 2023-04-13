

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
        nowMonth = x.strftime('%m')
        xy = datetime.datetime(int(yil),int(ay),int(gun))
        
        if(int(gun) == int(nowDay)):
            gun = int(gun) -1
        
        if (xy.strftime("%A") == "Saturday"):
            gun = str(int(gun) - 1)
        if len(gun) == 1:
            gun = "0" + str(gun)
            
        if len(ay) == 1:
            ay = "0"+ str(ay)

        
        else:
            
            if len(str(gun)) ==1:
                gun = "0" + str(gun)
                
            if len(ay) ==1:
                ay = "0"+ str(ay)
          
        if(int(nowDay) == int(gun) and int(ay) == int(nowMonth)):
            
            
            return
                
        
    
        # URL = "https://www.tcmb.gov.tr/kurlar/202111/02112021.xml"
        URL = "https://www.tcmb.gov.tr/kurlar/"+str(yil)+str(ay)+"/"+str(gun)+str(ay)+str(yil)+".xml"

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
        
        


        

        