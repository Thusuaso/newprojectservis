from helpers import SqlConnect
from models import UrunBirimSchema,UrunBirimModel


class UrunBirim:

    def __init__(self):
        self.data = SqlConnect().data

    
    def getUrunBirimList(self):

        result = self.data.getList("Select * from UrunBirimTB")

        birimListe = list()
        for item in result:

            model = UrunBirimModel()
            model.id = item.ID
            model.birimAdi = item.BirimAdi

            birimListe.append(model)

        schema = UrunBirimSchema(many=True)

        return schema.dump(birimListe)