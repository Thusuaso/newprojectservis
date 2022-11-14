from models.raporlar import SiparisGiderTurModel,SiparisGiderTurSchema
from helpers import SqlConnect 


class SiparisGiderTur:

    def __init__(self):
        self.data = SqlConnect().data 

    def getGiderTurList(self):

        liste = list()

        result = self.data.getList("Select * from SiparisEkstraGiderTurTB")

        for item in result:

            model = SiparisGiderTurModel()

            model.id = item.ID 
            model.giderTur = item.GiderTur

            liste.append(model)

        schema = SiparisGiderTurSchema(many=True)

        return schema.dump(liste) 