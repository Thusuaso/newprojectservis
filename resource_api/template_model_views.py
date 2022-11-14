from flask_restful import Resource
from flask import jsonify
from models.musteriler import MusterilerModel,MusterilerSchema
from models.kullanici import KullaniciModel,KullaniciSchema
from models.kategori import KategoriSchema,KategoriModel
from models.odemeler import OdemelerModel,OdemelerSchema
from models.olculer import OlculerModel,OlculerSchema
from models.sevkiyat import SevkiyatModel,SevkiyatSchema
from models.siparisler import SiparislerModel,SiparislerSchema
from models.siparisUrun import SiparisUrunModel,SiparisUrunSchema
from models.tedarikci import TedarikciModel,TedarikciSchema
from models.uretim import UretimModel,UretimSchema
from models.urunKart import UrunKartModel,UrunKartSchema
from models.urunler import UrunlerModel,UrunlerSchema
from models.urunOcak import UrunOcakModel,UrunOcakSchema
from models.yuzeyKenar import YuzeyKenarModel,YuzeyKenarSchema

class TemplateModelViews(Resource):

    def get(self,modelName):
        
        if modelName == "musteri" :
            return self.getModel(MusterilerModel(),MusterilerSchema())
        if modelName == "kullanici":
            return self.getModel(KullaniciModel(),KullaniciSchema())
        if modelName == "kategori" :
            return self.getModel(KategoriModel(),KategoriSchema())
        if modelName == "odemeler" :
            return self.getModel(OdemelerModel(),OdemelerSchema())
        if modelName == "olculer" :
            return self.getModel(OlculerModel(),OlculerSchema())
        if modelName == "sevkiyat" : 
            return self.getModel(SevkiyatModel(),SevkiyatSchema())
        if modelName == "siparisler" :
            return self.getModel(SiparislerModel(),SiparislerSchema())
        if modelName == "siparisUrun" :
            return self.getModel(SiparisUrunModel(),SiparisUrunSchema())
        if modelName == "tedarikci" :
            return self.getModel(TedarikciModel(),TedarikciSchema())       
        if modelName == "uretim" :
            return self.getModel(UretimModel(),UretimSchema())
        if modelName == "urunKart" :
            return self.getModel(UrunKartModel(),UrunKartSchema())
        if modelName == "urunler" :
            return self.getModel(UrunlerModel(),UrunlerSchema())
        if modelName == "urunOcak" :
            return self.getModel(UrunOcakModel(),UrunOcakSchema())
        if modelName == "yuzeyKenar" :
            return self.getModel(YuzeyKenarModel(),YuzeyKenarSchema())
 
        

        return jsonify({})


    def getModel(self,model,schema):

        return schema.dump(model)