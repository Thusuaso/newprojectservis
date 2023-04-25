from flask_restful import Resource
from views.siparisler import SatisciInfo
class SiparisSatisciInfoApi(Resource):
    def get(self):
        
        islem = SatisciInfo()
        result = islem.getSiparisSatisciInfo()
        return result