from views.siparisler.listeler import UrunBirim
from flask_restful import Resource

class UrunBirimList(Resource):
    def get(self):

        urunBirim = UrunBirim()

        result = urunBirim.getUrunBirimList()

        return result