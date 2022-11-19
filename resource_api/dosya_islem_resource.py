from flask_restful import Resource
import os
from flask import Flask, request, abort, jsonify, send_from_directory


product_path ='products/'
class DosyaIslemResource(Resource):

    def get(self,path):
       dowload_directory = 'dosyalar/'

       return send_from_directory(dowload_directory,path,as_attachment=True)
    

class ProductImage(Resource):

    def get(self,imageName):

        return send_from_directory(product_path,imageName,as_attachment=True)

    def post(self,imageName):
        
       
        if 'file' in request.files:
            file = request.files['file']
            file.save(os.path.join(product_path,imageName))

class ProductImageList(Resource):

    def get(self):

        """Endpoint to list files on the server."""
        image_path = 'products/'
        files = []
        for filename in os.listdir(image_path):
            path = os.path.join(image_path, filename)
            if os.path.isfile(path):
                files.append(filename)
        return jsonify(files)