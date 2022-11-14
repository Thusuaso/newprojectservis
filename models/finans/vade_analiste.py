from marshmallow import Schema,fields


class VadeAnaListeSchema(Schema):

    firmaAdi = fields.String()
    tutar = fields.Float()
    siparis_no = fields.String()
    vade_tarih = fields.String()
  

class VadeAnaListeModel:
    
    firmaAdi = ""
    tutar = 0
    siparis_no = ""
    vade_tarih = ""
  