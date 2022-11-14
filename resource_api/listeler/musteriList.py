from views import Musteri
from flask_restful import Resource

class MusteriList(Resource):
    def get(self):

        musteri = Musteri()

        result = musteri.getMusteriList()

        return result
    
class UlkeyeGoreMusteriListApi(Resource):
    def get(self,year):
        musteri = Musteri()
        result = musteri.getUlkeyeGoreMusteriList(year)
        return result
    
class UlkeyeGoreMusteriListAyrintiApi(Resource):
    def get(self,year,ulkeId):
        musteri = Musteri()
        data = musteri.getUlkeyeGoreMusteriListAyrintiSip(year,ulkeId)
        data2 = musteri.getUlkeyeGoreMusteriListAyrintiYuk(year,ulkeId)
        result = {
            'sip':data,
            'yuk':data2
        }        


        return result


        