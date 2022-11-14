from models.siparisler_model import TeslimTurSchema,TeslimTurModel
from helpers import SqlConnect


class TeslimTur:

    def __init__(self):
        self.data = SqlConnect().data

    def getTeslimTurList(self):
        result = self.data.getList("Select * from SiparisTeslimTurTB where ID>4")

        teslimList = list()

        for item in result:

            model = TeslimTurModel()
            model.id = item.ID
            model.teslimTurAdi = item.TeslimTur
            teslimList.append(model)

        schema = TeslimTurSchema(many=True)
        return schema.dump(teslimList)

        