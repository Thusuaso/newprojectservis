from marshmallow import fields,Schema


class OdemelerListSchema(Schema):

    Id = fields.Integer()
    tutar = fields.Float()
    musteri_adi = fields.String()


class OdemelerListModel:

    Id = 0
    tutar = 0
    musteri_adi = ""
   
class OdemelerListAyrintiSchema(Schema):
    tarih = fields.String()
    po = fields.String()
    odenenTutar = fields.Float()
    
class OdemelerListAyrintiModel():
    tarih = ""
    po = ""
    odenenTutar = 0