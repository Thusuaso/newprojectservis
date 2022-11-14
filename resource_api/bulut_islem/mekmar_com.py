from resource_api.bulut_islem.bulutIslem import BulutIslem
from flask_restful import Resource
from flask import request,jsonify


class TestRaporIslem(Resource):
   
    def post(self):

        file = request.files['file']

        space_path = 'test-reports/'

        bulutIslem = BulutIslem()
        
        result = bulutIslem.dosyaGonderPdf(space_path,file)

        return jsonify({'status' : result})