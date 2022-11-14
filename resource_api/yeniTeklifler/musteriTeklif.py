from helpers import SqlConnect
from models.yeniTeklifler import MusteriModel,MusteriSchema,UlkeModel,UlkeSchema
from flask_restful import Resource
from flask import jsonify,request


class MusteriListApi(Resource):
    def get(self):

        musteri = MusteriTeklif()

        musteriList = musteri.getMusteriList()
        ulkeList = musteri.getUlkeList()

        return jsonify({ 'musteriList' : musteriList,'ulkeList' : ulkeList })

class MusteriDetaApi(Resource):

    def get(self,musteriid):

        musteri = MusteriTeklif()

        musteriDetay = musteri.getMusteri(musteriid)
       

        return musteriDetay

class MusteriYeniModel(Resource):

    def get(self):

        musteri = MusteriTeklif()

        return musteri.getYeniMusteriModel()

        

class MusteriTeklifIslemApi(Resource):

    def post(self):

        data = request.get_json()

        musteri = MusteriTeklif()

        status = musteri.musteriGuncelle(data)
        musteriDetay = musteri.getMusteri(data['id'])

        return jsonify({'status' : status, 'musteriDetay' : musteriDetay})



class MusteriTeklif:
    def __init__(self):

        self.data = SqlConnect().data

    def getMusteriList(self):
        result = self.data.getList(
            """
            select
            m.Id,
            m.MusteriAdi,
            u.UlkeAdi,
            u.Id as UlkeId,
            u.Png_Flags,
            u.Icon_Flags,
            (Select count(*) from YeniTeklifTB where MusteriId=m.Id) as TeklifSayisi
            from
            YeniTeklif_MusterilerTB m,YeniTeklif_UlkeTB u
            where
            m.UlkeId=u.Id
            order by (Select count(*) from YeniTeklifTB where MusteriId=m.Id) desc
            """
        )

        liste = list()

        for item in result:
            model = MusteriModel()
            model.id = item.Id 
            model.musteriAdi = item.MusteriAdi 
            model.ulke = UlkeModel()
            model.ulke.id = item.UlkeId
            model.ulke.ulkeAdi = item.UlkeAdi
            model.ulke.pngFlags = '../../assets/country-logo/' +  str(item.Png_Flags)
            model.ulke.iconFlags = item.Icon_Flags
            model.teklifSayisi = item.TeklifSayisi

            liste.append(model)

        schema = MusteriSchema(many=True)

        return schema.dump(liste)

    def getMusteri(self,musteriid):
        item = self.data.getStoreList(
            """
            select
            m.Id,
            m.MusteriAdi,
            u.UlkeAdi,
            u.Png_Flags,
            u.Icon_Flags,
            u.Id as UlkeId,
            (Select count(*) from YeniTeklifTB where MusteriId=m.Id) as TeklifSayisi
            from
            YeniTeklif_MusterilerTB m,YeniTeklif_UlkeTB u
            where
            m.UlkeId=u.Id and m.Id=?
            order by (Select count(*) from YeniTeklifTB where MusteriId=m.Id) desc
            """,(musteriid)
        )[0]

        model = MusteriModel()
        model.id = item.Id 
        model.musteriAdi = item.MusteriAdi 
        model.ulke = UlkeModel()
        model.ulke.id = item.UlkeId
        model.ulke.ulkeAdi = item.UlkeAdi
        model.ulke.pngFlags =  '../../assets/country-logo/' +  str(item.Png_Flags)
        model.ulke.iconFlags = item.Icon_Flags
        model.teklifSayisi = item.TeklifSayisi

        schema = MusteriSchema()

        return schema.dump(model)

    def getYeniMusteriModel(self):

        musteri = MusteriModel()

        schema = MusteriSchema()

        return schema.dump(musteri)

    def getUlkeList(self):

        result = self.data.getList(
            """
            Select * from YeniTeklif_UlkeTB

            """
        )

        liste = list()

        for item in result:
            model = UlkeModel()
            model.id = item.Id 
            model.ulkeAdi = item.UlkeAdi 
            model.pngFlags = '../../assets/country-logo/' +  str(item.Png_Flags)
            model.iconFlags = item.Icon_Flags

            liste.append(model)

        schema = UlkeSchema(many=True)

        return schema.dump(liste)

    def musteriGuncelle(self,musteri):

        try:
            self.data.update_insert(
                """
                update YeniTeklif_MusterilerTB set MusteriAdi=?,UlkeId=?
                where Id=?
                """,
                (
                    musteri['musteriAdi'],
                    musteri['ulkeId'],
                    musteri['id']
                )
            )

            return True
        except Exception as e:
            print('musteriGuncelle Hata : ', str(e))
            return False

    