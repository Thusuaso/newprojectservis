from flask_restful import Resource
from views.siparisler.listeler import SiparisListe
class SiparisListResource(Resource):
    def get(self,siparisDurum,yil):

        siparis = SiparisListe(siparisDurum)

        #result = siparis.getSiparisList()
        result = siparis.getSiparisUrunList(yil)
        
        return result

class SiparisHepsiListResource(Resource):
    def get(self,siparisDurum):

        siparis = SiparisListe(siparisDurum)

        #result = siparis.getSiparisList()
       
        result2= siparis.getSiparisUrunHepsiList()
        
        return result2      
       

