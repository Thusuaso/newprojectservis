from flask import Flask, render_template
from flask_socketio import SocketIO,emit,send
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app,logger=True, engineio_logger=True,cors_allowed_origins="*")

@socketio.on('connect')
def connect():
    emit('başarıyla bağlandı',broadcast=True)
    
@socketio.on('urunkart_yeni_event')
def urunkart_yeni_event(data):
    emit('urunkart_yeni_emit',data,broadcast=True)


@socketio.on('urunkart_guncelleme_event')
def urunkart_guncelleme_event(data):
    emit('urunkart_guncelleme_emit',data,broadcast=True)
    
@socketio.on('urunKartiSilmeEvent')
def urunKartiSilmeEvent():
    emit('urunkart_silme_emit',broadcast=True)

@socketio.on('anaSayfaDegisiklikEvent')
def anaSayfaDegisiklikEvent(data):
    emit('anaSayfaDegisiklikEmit',data,broadcast=True)

@socketio.on('tahsilat_kayitdegisim_event')
def tahsilat_kayitdegisim_event(siparisno):
    emit('tahsilat_kayitdegisim_emit',siparisno,broadcast=True)

@socketio.on('musteri_kayitdegisim_event')
def musteri_kayitdegisim_event():
    emit('musteri_kayitdegisim_emit',broadcast=True)
    
@socketio.on('siparisler_list_event')
def siparisler_list_event():
    emit('siparisler_list_emit',broadcast=True)    


@socketio.on('numunetahsilat_kayitdegisim_event')
def numunetahsilat_kayitdegisim_event():
    emit('numunetahsilat_kayitdegisim_emit',broadcast=True)
    
@socketio.on('teklif_degisim_event')
def teklif_degisim_event():
    emit('teklif_degisim_emit',broadcast=True)
    
@socketio.on('tedarikci_degisim_event')
def tedarikci_degisim_event():
    emit('tedarikci_list_emit',broadcast=True)

@socketio.on('bildirimler_update_event')
def bildirimler_update_event():
    emit('bildirimler_update_emit',broadcast=True)

@socketio.on('stock_list_event')
def stock_list_event():
    emit('stock_list_emit',broadcast=True)
@socketio.on('mekmar_com_galleria_list_event')
def mekmar_com_galleria_list_event():
    emit('mekmar_com_galleria_list_emit',broadcast=True)

@socketio.on('isf_form_load_event')
def isf_form_load_event():
    emit('isf_form_load_emit',broadcast=True)
    
@socketio.on('send_message_home_event')
def send_message_home_event(info):
    print("send_message_home_event",info)
    emit('send_message_home_emit',info,broadcast=True)
    



if __name__ == '__main__':
    socketio.run(app,port=5001)