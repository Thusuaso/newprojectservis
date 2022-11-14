from resource_api.numuneler.numuneliste import NumuneListe
from resource_api.numuneler.numune_ayrinti import NumuneAyrinti

from flask_restful import Resource
from flask import jsonify,request


class NumuneListApi(Resource):

    def get(self,yil):

        islem = NumuneListe()

        data = {

            "numune_list" : islem.getNumuneList(yil)
           
           
        }

        return jsonify(data)

class NumuneAyrintiListApi(Resource): 

    def get(self,po):

        numune = NumuneAyrinti(po)
       
        data = {

            "numune_list" : numune.getNumuneAyrintiList()
        
        }

        return jsonify(data)   

