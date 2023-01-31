from views.siparisler import SiparisGiris
from flask_restful import Resource,request

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
    
class ContainerAddApi(Resource):
    def post(self):
        data = request.get_json()
        
        siparis = SiparisGiris()
        result = siparis.setContainerAdd(data)
        return result
    
class ContainerAmountApi(Resource):
    def get(self,sipNo):
        siparis = SiparisGiris()
        result = siparis.getContainerAmount(sipNo)
        return result
