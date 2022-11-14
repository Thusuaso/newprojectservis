from views.teklifler import Musteriler
from flask_restful import Resource


class MusteriResource(Resource):

    def get(self):
        musteri = Musteriler()

        result = musteri.getMusteriler()

        return result
