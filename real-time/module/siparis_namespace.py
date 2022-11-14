from flask_socketio import Namespace,emit


class SiparisNamespace(Namespace):

    def on_connect(self):
        pass
    
    def on_disconnect(self):
        pass

    def on_siparis_degisim(self,data):
        emit('siparis_degisim_emit',data)