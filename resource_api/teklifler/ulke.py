from views.teklifler import Ulke
from flask_restful import Resource


class UlkeResource(Resource):

    def get(self):

        ulke = Ulke()

        result = ulke.getUlkeList()

        return result
