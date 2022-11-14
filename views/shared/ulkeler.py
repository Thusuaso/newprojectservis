from models.shared import UlkelerSchema,UlkelerModel
from helpers import SqlConnect

class Ulkeler:

    def __init__(self):
        self.data = SqlConnect().data

    def getUlkeList(self):
        result = self.data.getList("Select * from YeniTeklif_UlkeTB")

        ulkeList = list()

        for item in result:

            model = UlkelerModel()
            model.id = item.Id
            model.ulkeAdi = item.UlkeAdi
            model.logo = item.Png_Flags

            ulkeList.append(model)
        
        schema = UlkelerSchema(many=True)
        return schema.dump(ulkeList)