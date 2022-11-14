from views.siparisler import TeslimTur
from flask_restful import Resource

class TeslimTurList(Resource):
    def get(self):
        teslimTur = TeslimTur()

        result = teslimTur.getTeslimTurList()

        return result
        