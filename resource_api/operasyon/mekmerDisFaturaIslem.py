from flask_restful import Resource
from flask import request,send_file,jsonify
from models.operasyon.mekmerDisFatura import *
from helpers import SqlConnect
class MekmerDisFaturaModelApi(Resource):
    def get(self):
        
        islem = MekmerDisFatura()
        result = islem.getMekmerDisFaturaModel()
        return result
    
class MekmerDisFaturaIslemApi(Resource):
    def post(self):
        data = request.get_json()
        islem = MekmerDisFatura()
        status = islem.kaydet(data)
        dataList = islem.getMekmerDisFaturaList()
        return jsonify({'status':status,'dataList':dataList})
    
class MekmerDisFaturaIslemGuncelleApi(Resource):
    def post(self):
        data = request.get_json()
        islem = MekmerDisFatura()
        status = islem.guncelle(data)
        dataList = islem.getMekmerDisFaturaList()
        return jsonify({'status':status,'dataList':dataList})
    
class MekmerDisFaturaListApi(Resource):
    def get(self):
        islem = MekmerDisFatura()
        result = islem.getMekmerDisFaturaList()
        return jsonify(result)
    
class MekmerDisFaturaKaydetApi(Resource):
    def get(self,id,evrakAdi):
        print(id,evrakAdi)
        islem = MekmerDisFatura()
        result = islem.setMekmerDisFaturaKaydet(id,evrakAdi)
        return jsonify(result)    

class MekmerDisFatura:
    def __init__(self):
        self.data = SqlConnect().data
    
    def getMekmerDisFaturaModel(self):
        
        model = MekmerDisFaturaModel()
        schema = MekmerDisFaturaSchema()
        
        return schema.dump(model)
    
    def kaydet(self,data):
        try:
            self.data.update_insert("""
                                        insert into 
                                        MekmerDisFaturaTB
                                        (Tarih,FirmaAdi,Aciklama,Tutar_Tl,Tutar_Dolar,Kur) 
                                        VALUES(
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?,
                                            ?)
                                   
                                   """,(data["tarih"],
                                        data["firmaAdi"],
                                        data["aciklama"],
                                        data["tutarTl"],
                                        data["tutarDolar"],
                                        data["kur"]))
            return True
        except Exception as e:
            print("MekmerDisFatura kaydet", str(e))
            return False
        
    def guncelle(self,data):
        try:
            self.data.update_insert("""
                                        update
                                        MekmerDisFaturaTB
                                        SET Tarih=?,FirmaAdi=?,Aciklama=?,Tutar_Tl=?,Tutar_Dolar=?,Kur=?
                                        WHERE ID=?
                                   
                                   """,(data["tarih"],
                                        data["firmaAdi"],
                                        data["aciklama"],
                                        data["tutarTl"],
                                        data["tutarDolar"],
                                        data["kur"],
                                        data["id"]
                                   
                                   )
                                )
            return True
        except Exception as e:
            print("MekmerDisFatura guncelle", str(e))
            return False
    
    def getMekmerDisFaturaList(self):
        try:
            result = self.data.getList("""
                                        Select * from 
                                        MekmerDisFaturaTB
                                   
                                   """
                                )
            liste = list()
            for item in result:
                model = MekmerDisFaturaModel()
                model.id = item.ID
                model.tarih = item.Tarih
                model.firmaAdi = item.FirmaAdi
                model.aciklama = item.Aciklama
                model.tutarDolar = item.Tutar_Dolar
                model.tutarTl = item.Tutar_Tl
                model.kur = item.Kur
                model.fileName = item.FileName
                model.fileLink = item.FileLink
                liste.append(model)
            
            schema = MekmerDisFaturaSchema(many=True)
            return schema.dump(liste)
        
        except Exception as e:
            print("getMekmerDisFaturaList ", str(e))

    def setMekmerDisFaturaKaydet(self,id,evrakAdi):
        try:
            link = "https://file-service.mekmar.com/file/download/mekmerDisFatura/" + str(id) + '/' + evrakAdi
            
            self.data.update_insert("""update MekmerDisFaturaTB SET FileLink =? where ID=?""",(link,id))
            return True
        except Exception as e:
            print("getMekmerDisFaturaList ", str(e))
            return False
    