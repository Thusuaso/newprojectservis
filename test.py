import urllib.request,ssl # Websitesinden veri cekmek ve ssl sertifikasini es gecmek
import xml.etree.ElementTree as ET # Xml yapisini ayristirmak

# SSl sertifikasi hatalarini engellemek
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ay = "11"
yil = "2021"
gun ="2"
bosluk ="/"
URL = "https://www.tcmb.gov.tr/kurlar/202111/02112021.xml"
dolar,euro = 0,0

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
    



# Xml dosyasini ayristirmak

    

    
    
print(" {} ".format(dolar))