from flask import request,jsonify
from flask_restful import Resource
from views import Notification
class NotificationIslemApi(Resource):
    def post(self):
        data = request.get_json()
        islem = Notification()
        status = islem.save(data)
        return {'status':status}
    def put(self):
        data = request.get_json()
class NotificationListApi(Resource):
    def get(self,id):
        islem = Notification()
        liste = islem.getList(id)
        
        return {'liste':liste}
    
class NotificationIslemAnsweredApi(Resource):
    def post(self):
        data = request.get_json()
        islem = Notification()
        status = islem.answeredsave(data)
        return {'status':status}
class NotificationIslemFollowApi(Resource):
    def post(self):
        data = request.get_json()
        islem = Notification()
        status = islem.setFollow(data)
        return {'status':status}
    
class NotificationIslemFollowAnsweredApi(Resource):
    def post(self):
        data = request.get_json()
        islem = Notification()
        status = islem.setFollowAnswered(data)
        return {'status':status}
        
    


