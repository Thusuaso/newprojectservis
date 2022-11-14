from flask import Flask,jsonify
from flask_cors import CORS,cross_origin
from flask_socketio import SocketIO, send, emit,join_room

app = Flask(__name__)

socketio = SocketIO(app)

CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", engineio_logger=True)



@socketio.on('connect')
def connect():
    print('User Başarıyla Bağlandı')

#işçilik güncelleme
@socketio.on('siparis_iscilik_event')
def siparis_iscilik_event(data):
    socketio.emit('siparis_iscilik_emit',data,broadcast=True)
    
#yeni sipariş sisteme girdiğinde
@socketio.on('siparis_yeni_event')
def siparis_yeni_event(value):
    socketio.emit('siparis_yeni_emit',value,broadcast=True)

@socketio.on('siparis_guncelleme_event')
def siparis_guncelleme_event(guncellemeData):
    socketio.emit('siparis_guncelleme_emit',guncellemeData,broadcast=True)

@socketio.on('urunkart_yeni_event')
def urunkart_yeni_event(data):
    socketio.emit('urunkart_yeni_emit',data,broadcast=True)

@socketio.on('urunkart_guncelleme_event')
def urunkart_guncelleme_event(data):
    socketio.emit('urunkart_guncelleme_emit',data,broadcast=True)
    
@socketio.on('urunkart_silme_event')
def urunkart_silme_event(data):
    socketio.emit('urunkart_silme_emit',data,broadcast=True)

@socketio.on('teklif_yeni_event')
def teklif_yeni_event(username):
    socketio.emit('teklif_yeni_emit',username,broadcast=True)

@socketio.on('teklif_guncelleme_event')
def teklif_guncelleme_event(username):
    socketio.emit('teklif_guncelleme_emit',username,broadcast=True)

@socketio.on('teklif_sil_event')
def teklif_sil_event():
    socketio.emit('teklif_sil_emit',broadcast=True)

@socketio.on('seleksiyon_yenikayit_event')
def seleksiyon_yenikayit_event(uretim_data):
    socketio.emit('seleksiyon_yenikayit_emit',uretim_data,broadcast=True)

@socketio.on('seleksiyon_kayitguncelle_event')
def seleksiyon_kayitguncelle_event(uretim_data):
    socketio.emit('seleksiyon_kayitguncelle_emit',uretim_data,broadcast=True)


@socketio.on('seleksiyon_kayitsil_event')
def seleksiyon_kayitsil_event(kasa_id):

    socketio.emit('seleksiyon_kayitsil_emit',kasa_id,broadcast=True)

@socketio.on('seleksiyon_siparisdegisim_event')
def seleksiyon_siparisdegisim_event(siparis_data):
    socketio.emit('seleksiyon_siparisdegisim_emit',siparis_data,broadcast=True)

@socketio.on('seleksiyon_coklukayit_event')
def seleksiyon_coklukayit_event(kasa_list):
    socketio.emit('seleksiyon_coklukayit_emit',kasa_list,broadcast=True)

@socketio.on('tahsilat_kayitdegisim_event')
def tahsilat_kayitdegisim_event(siparisno):
    
    socketio.emit('tahsilat_kayitdegisim_emit',siparisno,broadcast=True)

@socketio.on('musteri_kayitdegisim_event')
def musteri_kayitdegisim_event():
    socketio.emit('musteri_kayitdegisim_emit',broadcast=True)

@socketio.on('anaSayfaDegisiklikEvent')
def anaSayfaDegisiklikEvent(data):
    
    socketio.emit('anaSayfaDegisiklikEmit',data,broadcast=True)

@socketio.on('urunKartiSilmeEvent')
def urunKartiSilmeEvent(data):
    socketio.emit('urun_kart_silme_emit',data,broadcast=True)

@socketio.on('tedarikciListesiEvent')
def tedarikciListesiEvent(data):
    socketio.emit('tedarikciListesiEmit',data,broadcast=True)


@socketio.on('satisciAnaSayfaEvent')
def satisciAnaSayfaEvent(data):
    socketio.emit('satisciAnaSayfaEmit',data,broadcast=True)


if __name__ == '__main__':
    socketio.run(app,port=5001,debug=True)