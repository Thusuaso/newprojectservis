from models.teklifler import UlkeModel,UlkeSchema
from helpers.sqlConnect import SqlConnect

class Ulke:
    def __init__(self):

        self.data = SqlConnect().data

    
    def getUlkeList(self):

        dtUlkeList = self.data.getList("Select * from YeniTeklif_UlkeTB")

        ulkeList = list()

        for item in dtUlkeList:

            ulke = UlkeModel()
            ulke.id = item.Id
            ulke.ulkeAdi = item.UlkeAdi
            ulke.png_Flags = '/static/mekmar/country-logo/' + str(item.Png_Flags)

            ulkeList.append(ulke)

        
        schema = UlkeSchema(many=True)

        ulkeList_Json = schema.dump(ulkeList)

        return ulkeList_Json

