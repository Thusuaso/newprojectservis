from marshmallow import fields,Schema


class EfesPesinatIslemSchema(Schema):

    id = fields.Int()
    musteri_id = fields.Int()
    siparis_no = fields.String()
    tutar = fields.Float()
    musteri_adi = fields.String()
    tarih = fields.String()
    masraf = fields.Float()


class EfesPesinatIslemModel:

    id = None 
    musteri_id = None 
    siparis_no = ""
    tutar = 0
    musteri_adi = ""
    tarih = ""
    masraf = 0