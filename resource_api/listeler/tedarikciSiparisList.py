from views.listeler import Tedarikci
from flask_restful import Resource

class TedarikciSiparisList(Resource):
    def get(self):

        tedarikci = Tedarikci()

        result = tedarikci.getTedarikciSiparisList()

        return result