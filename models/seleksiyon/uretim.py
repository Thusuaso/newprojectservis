from marshmallow import Schema,fields
from models.seleksiyon import SiparisAyrintiModel,SiparisAyrintiSchema

class UretimSchema(Schema):
    id = fields.Int()
    tarih = fields.String()
    kasano = fields.Int()
    urunkartid = fields.Int()
    tedarikciid = fields.Int()
    urunbirimid = fields.Int()
    urunocakid = fields.Int()
    adet = fields.Float()
    kutuadet = fields.Int()
    kasaadet = fields.Int()
    kutuiciadet = fields.Int()
    miktar = fields.Float()
    ozelmiktar = fields.Float()
    sqm_miktar = fields.Float()
    aciklama = fields.String()
    uretimturid = fields.String()
    uretimturaciklama = fields.String()
    urundurumid = fields.Int()
    siparisaciklama = fields.String()
    kutu = fields.Boolean()
    bagli=fields.Boolean()
    duzenleyen = fields.String()
    kasalayan =  fields.String()
    disarda = fields.Boolean()
    etiketdurum = fields.Boolean()
    kullaniciid = fields.Int()
    sirano = fields.Int()
    kayit_tur = fields.String()
    kutuiciadet = fields.Int()
    tanim = fields.String()
    bulunamayan=fields.Boolean()
    #custom alanlar
    kategoriadi = fields.String()
    ebat = fields.String()
    urunadi = fields.String()
    kenarislem = fields.String()
    sipariskart = fields.Nested(SiparisAyrintiSchema())


class UretimModel:
    id = None
    tarih = ""
    kasano = None
    urunkartid = None
    tedarikciid = None
    urunbirimid = None
    urunocakid = None
    adet = 0
    kutuadet = 0
    kutuiciadet = 0
    kasaadet = 0
    miktar = 0
    ozelmiktar = 0
    sqm_miktar = 0
    aciklama = ""
    uretimturid = ""
    uretimturaciklama = ""
    urundurumid = None
    siparisaciklama = ""
    kutu = False
    bagli=False
    duzenleyen = ""
    kasalayan = ""
    disarda = False
    etiketdurum = False
    kullaniciid = None
    sirano = None
    #custom alanlar
    kategoriadi = ""
    ebat = ""
    kenarislem = ""
    urunadi = ""
    kayit_tur = ""
    kutuiciadet = 0
    sipariskart = SiparisAyrintiModel()
    tanim = ""
    bulunamayan=False
    
class UretimFazlaMiSchema(Schema):
    siparismiktari = fields.Float()
    uretimtoplami = fields.Float()
    
class UretimFazlaMiModel:
    siparismiktari = 0
    uretimtoplami = 0