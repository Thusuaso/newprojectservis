from helpers.mongoDb import MongoDb
from helpers import SqlConnect
from openpyxl import *


class Model:
    urunid = None 
    onerilenurunid = None

data = MongoDb().data

sqlServer = SqlConnect().data

mongoOnerilerUrunler = data.onerilenuruns.find({})



def urunkayit(urunid,onerilenurunid):
    try:
        sqlServer.update_insert(
            """
            insert into MekmarCom_OnerilenUrunler (urunid,onerilenurunid)
           values
           (?,?)
           """,(urunid,onerilenurunid)
        )
        return True 
    except:
        return False
    


for item in mongoOnerilerUrunler:
    urunid = int(item['urunid'])
    onerilenurunid = int(item['benzerurunid'])  
    resutl = urunkayit(urunid,onerilenurunid)

print('İşlem Tamamlandı')
    


