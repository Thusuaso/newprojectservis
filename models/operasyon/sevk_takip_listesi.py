from marshmallow import Schema,fields



class SevkTakipSchema(Schema):
    id = fields.Int()
    siparisno = fields.String()
    pesinat = fields.Float()
    kalan_alacak = fields.Float()
    sevk_tarihi = fields.String()
    konteynerno = fields.String()
    eta = fields.String()
    kalan_sure = fields.Int()
    konsimento = fields.Boolean()
    sorumlusu = fields.String()
    musteriadi = fields.String()
    takip = fields.Boolean()
    line = fields.String()
    sira = fields.Int()
    liman = fields.String()

class SevkTakipModel:
    id = None 
    siparisno = ""
    pesinat = 0 
    kalan_alacak = 0
    sevk_tarihi = ""
    konteynerno = ""
    eta = ""
    kalan_sure = 0
    konsimento = False
    sorumlusu = ""
    musteriadi = ""
    takip = False
    line = ""
    sira = 0
    liman = ""


class FinansTakipSchema(Schema):

    id = fields.Int()
    siparisno = fields.String()
    musteriAdi  = fields.String()
    pesinat = fields.Float()
    diger_odemeler = fields.Float()
    mal_bedeli = fields.Float()
    odenen = fields.Float()
    siparisSahibi = fields.String()
    operasyon = fields.String()
    siparisDurum = fields.String()
    kalan_bedel = fields.Float()
   

class FinansTakipModel:
    id = None 
    siparisno = ""
    musteriAdi  = ""
    pesinat = 0
    diger_odemeler = 0
    mal_bedeli = 0
    odenen = 0
    siparisSahibi = ""
    operasyon = ""
    siparisDurum = ""
    kalan_bedel = 0