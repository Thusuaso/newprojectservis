from flask_restful import Resource
from flask import request,send_file,jsonify
from views.raporlar.maliyet_hatalari import MaliyetHatalari
class MaliyetHataRaporIslemApi(Resource):
    def get(self):
        islem = MaliyetHatalari()
        liste = islem.getMaliyetHatalariListe()
        return jsonify(liste)
    def post(self):
        data = request.get_json()
        islem = MaliyetHatalari()
        status = islem.save(data)
        return {'status':status}
        
    def put(self):
        data = request.get_json()
        islem = MaliyetHatalari()
        status = islem.update(data)
        return {'status':status}
    
class MaliyetHataRaporModelApi(Resource):
    def get(self):
        islem = MaliyetHatalari()
        result = islem.getModel()
        return jsonify(result)

class MaliyetHataRaporDeleteApi(Resource):
    def delete(self,id):
        islem = MaliyetHatalari()
        status = islem.delete(id)
        return jsonify({'status':status})