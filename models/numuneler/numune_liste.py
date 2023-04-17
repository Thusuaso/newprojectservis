from marshmallow import Schema,fields

class NumuneListeSchema(Schema):
    id = fields.Int()
    tarih = fields.String()
    temsilci = fields.String()
    musteriadi = fields.String()
    numuneNo = fields.String()
    kategori = fields.String()
    kategori_id = fields.Int()
    miktar = fields.Float()
    birim = fields.String()
    sira = fields.Int()
    m2 = fields.Float()
    adet = fields.Float()
    mt = fields.Float()
    ton = fields.Float()
    aciklama = fields.String()
    odeme_durum = fields.Boolean()
    link=fields.String()
    gonderi_tipi = fields.String()
    banka_secimi = fields.String()
    gelenBedel = fields.Float()
    usdAlis = fields.Float()
    usdSatis = fields.Float()
    euroAlis = fields.Float()
    euroSatis = fields.Float()
    tlAlis = fields.Float()
    tlSatis = fields.Float()

   
class NumuneListeModel:
    id = None 
    tarih = ""
    temsilci = ""
    musteriadi = ""
    numuneNo = ""
    kategori = ""
    kategori_id = 0
    miktar = 0
    birim = ""
    sira  = 0
    m2 = 0
    adet = 0
    mt = 0
    ton = 0
    aciklama = ""
    odeme_durum = False
    link=""
    gonderi_tipi = ""
    banka_secimi = ""
    gelenBedel = 0
    usdAlis = 0
    usdSatis = 0
    euroAlis = 0
    euroSatis = 0
    tlAlis = 0
    tlSatis = 0

     

