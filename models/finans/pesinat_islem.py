from marshmallow import fields,Schema


class PesinatIslemSchema(Schema):

    id = fields.Int()
    musteri_id = fields.Int()
    siparis_no = fields.String()
    tutar = fields.Float()
    musteri_adi = fields.String()
    tarih = fields.String()
    masraf = fields.Float()
    aciklama = fields.String()
    temsilci_mail = fields.String()
    marketing = fields.String()
    kur = fields.Float()


class PesinatIslemModel:

    id = None 
    musteri_id = None 
    siparis_no = ""
    tutar = 0
    musteri_adi = ""
    tarih = ""
    masraf = 0
    aciklama = ""
    temsilci_mail = ""
    marketing = ""
    kur = 0