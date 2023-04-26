from models.siparisler_model import FaturaKesimTurSchema,FaturaKesimTurModel
from helpers import SqlConnect

class FaturaKesimTur():

    def __init__(self):
        self.data = SqlConnect().data

    def getFaturaKesimTurList(self):
        result = self.data.getList("Select * from FaturaKesilmeTB")

        odemeList = list()

        for item in result:
            model = FaturaKesimTurModel()
            if(item.ID==2):
                continue
            else:
                model.id = item.ID
                model.faturaKesimTurAdi = item.FaturaAdi
                odemeList.append(model)

        schema = FaturaKesimTurSchema(many=True)
      
        return schema.dump(odemeList)