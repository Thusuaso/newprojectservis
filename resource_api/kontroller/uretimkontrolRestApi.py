from flask import jsonify
from flask_restful import Resource
from resource_api.kontroller.uretim_takip_mail import UretimTakipMail


 
class UretimTakipIslem(Resource):

   def get(self):
        
        islem = UretimTakipMail() 
        
        result = False
        
        try:
            islem.uretimKontrol()
            result = True 
        except:
            result = False

        return jsonify({'status' : result})


class TedarikciTakipIslem(Resource):
   def get(self):

        islem = UretimTakipMail()
        
        result = False

        try:
            islem.tedarikciKontrol()
            result = True 
        except:
            result = False

        return jsonify({'status' : result})     



    