from views.shared import Ulkeler
from flask_restful import Resource
class UlkeList(Resource):
    def get(self):
        ulke = Ulkeler()

        result = ulke.getUlkeList()

        return result