from views.raporlar import SiparisMasraf
from flask_restful import Resource

class SiparisMasrafList(Resource):
    def get(self,siparisNo):

        siparis = SiparisMasraf()

        result = siparis.getMasrafListesi(siparisNo)

        return result