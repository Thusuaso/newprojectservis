from views.siparisler import SiparisGiris
from flask_restful import Resource

class SiparisGirisModel(Resource):
    def get(self,siparisNo):

        siparis = SiparisGiris()

        result = siparis.getSiparis(siparisNo)

        return result

class SiparisGirisBosModel(Resource):
    def get(self):

        siparis = SiparisGiris()

        result = siparis.getSiparisModel()

        return result
