from helpers.sqlConnect import SqlConnect
from models.teklifler import MusteriModel,MusteriSchema,UlkeModel


class Musteriler(SqlConnect):
    def __init__(self):
        self.data = SqlConnect().data
       

    def getMusteriler(self):
        dtMusteriler = self.data.getList("Select * from YeniTeklif_MusterilerTB")
        dtUlkeList = self.data.getList("Select * from YeniTeklif_UlkeTB")
        musteriList = list()

        for item in dtMusteriler:
            musteri = MusteriModel()

            musteri.id = item.Id
            musteri.musteriAdi = item.MusteriAdi
            ulke_model = UlkeModel()
            for ulke in filter(lambda x : x.Id == item.UlkeId,dtUlkeList):
                
                ulke_model.id = ulke.Id
                ulke_model.ulkeAdi = ulke.UlkeAdi
                ulke_model.png_Flags = '/static/mekmar/country-logo/' + str(ulke.Png_Flags)

            musteri.ulke = ulke_model
            musteriList.append(musteri)

        
        schema = MusteriSchema(many=True)
        
        return schema.dump(musteriList)

           

