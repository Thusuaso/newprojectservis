from views.siparisler.listeler import SiparisListe
from flask_restful import Resource

class SiparisUrun(Resource):
    def get(self,siparisNo):

        siparis = SiparisListe(2)

        result = siparis.getSiparisUrun(siparisNo)

        return result