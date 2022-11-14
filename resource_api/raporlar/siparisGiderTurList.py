from views.raporlar import SiparisGiderTur
from flask_restful import Resource 

class SiparisGiderTurList(Resource):
    def get(self):

        siparis = SiparisGiderTur()

        result = siparis.getGiderTurList() 

        return result