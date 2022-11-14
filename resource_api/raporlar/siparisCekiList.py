from views.raporlar import SiparisCeki
from flask_restful import Resource

class SiparisCekiList(Resource):
    def get(self,siparisNo):

        siparis = SiparisCeki()

        result = siparis.getCekiList(siparisNo)

        return result