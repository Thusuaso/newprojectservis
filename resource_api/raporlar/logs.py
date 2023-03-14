from flask import jsonify,request
from flask_restful import Resource
from views.raporlar import LogsMaliyet
class LogsMaliyetApi(Resource):
    def get(self,year):
        
        islem = LogsMaliyet()
        maliyet = islem.getLogsMaliyet(year)
        digerleri = islem.getAnaSayfaDegisiklikAll(year)
        yilList = islem.getYearList()
        data = {
            'maliyet':maliyet,
            'digerleri':digerleri,
            'yilList':yilList
        }
        return jsonify(data)