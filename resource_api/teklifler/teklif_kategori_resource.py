from flask_restful import Resource
from views.teklifler.kategori import Kategori


class TeklifKategoriResource(Resource):

    def get(self):

        kategori = Kategori()

        result = kategori.listeYukle()

        return result