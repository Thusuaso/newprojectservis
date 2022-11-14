from views.siparisler import OdemeTur
from flask_restful import Resource

class OdemeTurList(Resource):
    def get(self):

        odemeTur = OdemeTur()

        result = odemeTur.getOdemeTurList()

        return result