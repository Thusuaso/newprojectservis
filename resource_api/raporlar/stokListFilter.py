from flask_restful import Resource
from flask import jsonify,request,send_file
from views.stokListFilter import StokListFilter
class StokListFilterApi(Resource):

    def get(self):
        stok = StokListFilter()

        liste = stok.getStokListFilter()


        return liste
class StokListFilterAyrintiApi(Resource):
    def get(self,urunKartId):
        stok = StokListFilter()
        liste = stok.getStokListFilterAyrinti(urunKartId)
        return liste
    
