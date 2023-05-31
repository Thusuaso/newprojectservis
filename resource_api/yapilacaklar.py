from flask_restful import Resource
from flask import jsonify,request
from views.yapilacaklar import * 
class YapilacaklarModelApi(Resource):
    def get(self):
        islem = Yapilacaklar()
        model = islem.getYapilacaklarModel()
        return jsonify(model)
    
class YapilacaklarListApi(Resource):
    def get(self,userId):
        islem = Yapilacaklar()
        yapilmadi = islem.getYapilacaklarYapilmadiList(userId)
        yapildi = islem.getYapilacaklarYapildiList(userId)
        data = {
                    'yapilmadi':yapilmadi,
                    'yapildi':yapildi,
                }
        return jsonify(data)
    
class YapilacaklarListAllApi(Resource):
    def get(self):
        islem = Yapilacaklar()
        yapilmadi = islem.getYapilacaklarYapilmadiListAll()
        yapildi = islem.getYapilacaklarYapildiListAll()
        data = {
            'yapilmadi':yapilmadi,
            'yapildi':yapildi
        }
        return jsonify(data)
        
    
class YapilacaklarListGorevVerenApi(Resource):
    def get(self,userId):
        islem = Yapilacaklar()
        yapilmadi = islem.getYapilacaklarYapilmadiGorevVerenList(userId)
        yapildi = islem.getYapilacaklarYapildiGorevVerenList(userId)    
        data = {
                    'yapilmadi':yapilmadi,
                    'yapildi':yapildi,
                }
        return jsonify(data)

    
class YapilacaklarKullanicilarListApi(Resource):
    def get(self):
        islem = Yapilacaklar()
        users = islem.getYapilacaklarKullanicilarList()
        return jsonify(users)
class YapilacaklarIslemApi(Resource):
    def post(self):
        data = request.get_json()
        islem = Yapilacaklar()
        status = islem.save(data)
        return {'status':status}
    
    def put(self):
        data = request.get_json()
        islem = Yapilacaklar()
        status = islem.update(data)
        return {'status':status}
    
class YapilacaklarYapildiStatusApi(Resource):
    def post(self):
        data = request.get_json()
        islem = Yapilacaklar()
        status = islem.setYapilacaklarYapildi(data)
        return {'status':status}
    
class YapilacaklarDeleteApi(Resource):
    def get(self,id):
        islem = Yapilacaklar()
        status = islem.setYapilacaklarDelete(id)
        return {'status':status}