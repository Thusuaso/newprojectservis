from models.raporlar import SiparisCekiModel,SiparisCekiSchema
from helpers import SqlConnect


class SiparisCeki:

    def __init__(self):
        self.data = SqlConnect().data

    def getCekiList(self,siparisNo):

        cekiList = list()
        result = self.data.getStoreList("{call PytService_Siparis_CekiListesi3(?)}",(siparisNo))
      
        sira = 1
        for item in result:

            model = SiparisCekiModel()
            model.id = item.ID
            model.sira = sira 
            model.adet = item.Adet 
            model.birimAdi = item.BirimAdi 
            model.boy = item.Boy 
            model.en = item.En 
            model.kasaNo = item.KasaNo 
            model.kategoriAdi = item.KategoriAdi 
            model.kenar = item.Kenar 
            model.kutuAdet =  item.KutuAdet 
            model.miktar = item.Miktar 
            model.tedarikciAdi = item.TedarikciAdi 
            model.urunAdi = item.UrunAdi 
            model.yuzeyIslem = item.YuzeyIslem
            model.urunKart = item.UrunKartID 
            
            cekiList.append(model)

            sira += 1

        schema = SiparisCekiSchema(many=True)

        return schema.dump(cekiList)

