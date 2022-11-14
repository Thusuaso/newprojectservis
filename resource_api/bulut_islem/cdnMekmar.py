from resource_api.bulut_islem.bulutIslem import BulutIslem
from flask_restful import Resource
from flask import request,jsonify

class MekmarCdnApi(Resource):
   
     def put(self):
        result = True
        try:
            fileList = request.files.getlist('file')
            islem = BulutIslem()
            #fotoIslem = FotoIslem()
            for item in fileList:
                islem.dosyaKayit(item)
                #fotoIslem.fotoKayit(item.filename)
            result = True 
        except Exception as e:
            print('MekmarProductCloud Hata : ',str(e))
            result = False 
        
        return jsonify({'status' : result})
