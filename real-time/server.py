from flask import Flask,jsonify
from flask_cors import CORS,cross_origin
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)

socketio = SocketIO(app)

CORS(app, resources={r'/*': {'origins': '*'}})
socketio = SocketIO(app, cors_allowed_origins="*", engineio_logger=True)

@socketio.on('connect')
def user_connect():
    print('Kullanıcı Bağlandı')


@socketio.on('siparis_iscilik_event',namespace='/siparis')
def siparis_iscilik_event(data):
    socketio.emit('siparis_iscilik_emit',data,broadcast=True,namespace='/siparis')



if __name__ == '__main__':
    socketio.run(app,port=5001,debug=True)