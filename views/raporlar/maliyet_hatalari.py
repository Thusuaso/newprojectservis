from models.raporlar.maliyet_hatalar import *
from helpers import SqlConnect

class MaliyetHatalari():
    def __init__(self):
        self.data = SqlConnect().data
    
    def getModel(self):
        model = MaliyetHatalarModel()
        schema = MaliyetHatalarSchema()
        return schema.dump(model)
    
    def getMaliyetHatalariListe(self):
        try:
            result = self.data.getList("""
                                        select * from MaliyetHatalariTB
                                       """)
            liste = list()
            for item in result:
                model = MaliyetHatalarModel()
                model.id = item.ID
                model.hata = item.Hata
                model.maliyet = item.Maliyet
                model.kullanici_adi = item.KullaniciAdi
                model.kullanici_id = item.KullaniciId
                model.tarih = item.Tarih
                liste.append(model)
            schema = MaliyetHatalarSchema(many=True)
            return schema.dump(liste)
            
        except Exception as e:
            print('getMaliyetHatalariListe hata',str(e))
            return False

    def save(self,data):
        try:
            self.data.update_insert("""
                                        insert into MaliyetHatalariTB(Hata,Maliyet,KullaniciId,KullaniciAdi,Tarih) VALUES(?,?,?,?,?)
                                    """,(data['hata'],data['maliyet'],data['kullanici_id'],data['kullanici_adi'],data['tarih']))
            return True
                
        except Exception as e:
            print('Maliyet Save Hata',str(e))
            return False
        
    def update(self,data):
        try:
            self.data.update_insert("""
                                        update MaliyetHatalariTB SET Hata=?,Maliyet=?,KullaniciId=?,KullaniciAdi=? WHERE ID=?
                                    """,(data['hata'],data['maliyet'],data['kullanici_id'],data['kullanici_adi'],data['id']))
            return True
        except Exception as e:
            print('Maliyet Update Hata',str(e))
            return False

    def delete(self,id):
        try:
            self.data.update_insert("""
                                        delete MaliyetHatalariTB WHERe ID=?
                                    """,(id))
            return True
        except Exception as e:
            print('MaliyetHatalari delete',str(e))
            return False