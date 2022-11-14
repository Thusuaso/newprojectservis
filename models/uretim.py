from marshmallow import Schema,fields


class UretimSchema(Schema):
    id = fields.Int()
    tarih = fields.Date()
    kasaNo = fields.Int()
    urunKartId = fields.Int()
    tedarikciId = fields.Int()
    urunBirimId = fields.Int()
    urunOcakId = fields.Int()
    adet = fields.Float()
    kutuAdet = fields.Int()
    miktar = fields.Float()
    sqm_miktar = fields.Float()
    ozelMiktar = fields.Float()
    aciklama = fields.String()
    uretimTurId = fields.Int()
    uretimTurAciklama = fields.String()
    urunDurumId = fields.Int()
    siparisAciklama = fields.String()
    kutu = fields.Boolean()
    duzenleyen = fields.String()
    kasalayan = fields.String()
    disarda = fields.Boolean()
    etiketDurum = fields.Boolean()
    kullaniciId = fields.Int()
    siraNo = fields.Int()


class UretimModel:
    id = None
    tarih = None
    kasaNo = None
    urunKartId = None
    tedarikciId = None
    urunBirimId = None
    urunOcakId = None
    adet = 0
    kutuAdet = None
    miktar = 0
    sqm_miktar = 0
    ozelMiktar = 0
    aciklama = ""
    uretimTurId = None
    uretimTurAciklama = ""
    urunDurumId = None
    siparisAciklama = ""
    kutu = False
    duzenleyen = ""
    kasalayan = ""
    disarda = False
    etiketDurum = False
    kullaniciId = None
    siraNo = None