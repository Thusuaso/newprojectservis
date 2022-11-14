from marshmallow import Schema,fields

class UretimListeSchema(Schema):
    id = fields.Int()
    kasa_no = fields.Int()
    tarih = fields.String()
    kategori = fields.String()
    ocak = fields.String()
    tedarikci = fields.String()
    urunadi = fields.String()
    kenarislem = fields.String()
    boy = fields.String()
    en = fields.String()
    kenar = fields.String()
    kutuadet = fields.Int()
    kasaadet = fields.Float()
    m2 = fields.Float()
    mt = fields.Float()
    ton = fields.Float()
    adet = fields.Float()
    sqft = fields.Float()
    siparisaciklama = fields.String()
    tedarikci_id = fields.Int()
    birim_id = fields.Int()
    aciklama =fields.String()
    urunkartid = fields.Int()
    tanım = fields.String()
    disarda = fields.Boolean()
    kutu = fields.Boolean()
    bagli = fields.Boolean()
    bulunamayan = fields.Boolean()
    miktar= fields.Float()

class UretimListeModel:
    id = None 
    kasa_no = 0 
    tarih = ""
    kategori = "" 
    ocak = ""
    tedarikci = ""
    urunadi = ""
    kenarislem = ""
    boy = ""
    en = ""
    kenar = ""
    kutuadet = 0
    kasaadet = 0
    m2 = 0
    mt = 0 
    ton = 0 
    adet = 0
    sqft = 0
    miktar = 0
    siparisaciklama = ""
    tedarikci_id = None 
    birim_id = None 
    aciklama = ""
    urunkartid = None
    tanim = ""
    disarda = False
    kutu = False
    bagli = False
    bulunamayan=False


     

