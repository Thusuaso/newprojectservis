from flask import request,jsonify
import jwt
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        try:
            token = kwargs['token']
        except:
            token = request.args.get('token') or \
                request.form.get('token')
        if not token:
            return jsonify({'message' : 'token bulunamadı'})
        try :
            data = jwt.decode(token,'1LAM1vvkeAmzxfRaCSbTksDnZNVsE1jrV6')
        except:
            return jsonify({'message' : 'token bulunamadı'})
        return f(*args,**kwargs)
    return decorated