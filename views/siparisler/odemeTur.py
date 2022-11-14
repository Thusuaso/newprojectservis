from models.siparisler_model import OdemeTurSchema,OdemeTurModel
from helpers import SqlConnect

class OdemeTur:

    def __init__(self):
        self.data = SqlConnect().data

    def getOdemeTurList(self):
        result = self.data.getList("Select * from SiparisOdemeTurTB")

        odemeList = list()

        for item in result:
            model = OdemeTurModel()
            model.id = item.ID
            model.odemeTurAdi = item.OdemeTur

            odemeList.append(model)

        schema = OdemeTurSchema(many=True)
        return schema.dump(odemeList)