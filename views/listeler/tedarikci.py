from helpers import SqlConnect
from models import TedarikciSchema,TedarikciModel


class Tedarikci:
    def __init__(self):
        self.data =  SqlConnect().data


    def getTedarikciSiparisList(self):
       
        result = self.data.getList('Select * from TedarikciTB')

        tedarikciList = list()

        for item in result:
            model = TedarikciModel()
            model.id = item.ID
            model.firmaAdi = item.FirmaAdi

            tedarikciList.append(model)

        schema = TedarikciSchema(many=True)

        return schema.dump(tedarikciList)
