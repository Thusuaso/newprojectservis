from flask import jsonify,request
from flask_restful import Resource
from views.islemler.mekmar_com_galleria import Galleria
class GalleriaAddApi(Resource):
    def post(self):
        data = request.get_json()
        islem = Galleria()
        result = islem.add(data)
        return jsonify(result)
    
class GalleriaPhotosApi(Resource):
    def get(self,product_id):
        islem = Galleria()
        result = islem.getPhotos(product_id)
        return jsonify(result)
    
class GalleriaPhotosDeleteApi(Resource):
    def get(self,id):
        islem = Galleria()
        result = islem.deletePhotos(id)
        return jsonify(result)
    
class GalleryVideosAddApi(Resource):
    def post(self):
        data = request.get_json()
        islem = Galleria()
        result = islem.videos_add(data)
        return jsonify(result)