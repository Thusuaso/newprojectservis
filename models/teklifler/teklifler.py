from marshmallow import Schema,fields


class TekliflerSchema(Schema):
    id = fields.Int()
    tarih = fields.Date()
    hatirlatmaTarihi = fields.Date()
    musteriId = fields.Int()
    aciklama = fields.String()
    cfr = fields.Boolean()
    fob = fields.Boolean()
    dtp = fields.Boolean()
    fca = fields.Boolean()
    goruldu = fields.Boolean()
    kullaniciId = fields.Int()
    takipEt = fields.Boolean()
    kaynakYeri = fields.String()
    teklifYeri = fields.String()
    saritasNot = fields.String()
    hatirlatmaAciklama = fields.String()
    hatirlatmaId = fields.Int()
    dosyaAdi = fields.String()
    satis = fields.Boolean()
    numune_Giris_Tarihi = fields.Date()
    numune_Hatirlatma_Tarihi = fields.Date()
    numune_Tracking_No = fields.String()
    numune_Odenen_Tutar = fields.Float()
    numune_Musteriden_Alinan = fields.Float()
    proforma_Po_No = fields.String()
    proforma_Tarih = fields.Date()
    proforma_Tutar = fields.Float()
    teklif_Cloud = fields.Boolean()
    teklif_Cloud_Dosya = fields.String()
    proforma_Cloud = fields.Boolean()
    proforma_Cloud_Dosya = fields.String()
    numune_Cloud = fields.Boolean()
    numune_Cloud_Dosya = fields.String()
    teklifOncelik = fields.String()



class TekliflerModel:
    id = None
    tarih = None
    hatirlatmaTarihi = None
    musteriId = None
    aciklama = ""
    cfr = False
    fob = False
    dtp = False
    fca = False
    goruldu = False
    kullaniciId = None
    takipEt = False
    kaynakYeri = ""
    teklifYeri = ""
    saritasNot = ""
    hatirlatmaAciklama = ""
    hatirlatmaId = None
    dosyaAdi = ""
    satis = False
    numune_Giris_Tarihi = None
    numune_Hatirlatma_Tarihi = None
    numune_Tracking_No = ""
    numune_Odenen_Tutar = 0
    numune_Musteriden_Alinan = 0
    proforma_Po_No = ""
    proforma_Tarih = None
    proforma_Tutar = 0
    teklif_Cloud = False
    teklif_Cloud_Dosya = ""
    proforma_Cloud = False
    proforma_Cloud_Dosya = ""
    numune_Cloud = False
    numune_Cloud_Dosya = ""
    teklifOncelik = ""