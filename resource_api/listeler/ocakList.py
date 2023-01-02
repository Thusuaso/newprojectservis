from views.siparisler.listeler import OcakList
from flask_restful import Resource

class OcakListApi(Resource):
    def get(self):

        ocakList = OcakList()

        result = ocakList.getOcakList()

        return result