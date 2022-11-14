from marshmallow import Schema,fields


class TeklifRaporSchema(Schema):
    id = fields.Int()
    adi = fields.String()
    teklifSayisi = fields.Int()
    proformaSayisi = fields.Int()


class TeklifRaporModel:
    id = None 
    adi = ""
    teklifSayisi = 0
    proformaSayisi = 0

class TeklifAyrintiRaporSchema(Schema):
    id = fields.Int()
    musteri = fields.String()
    proforma_cloud_dosya =fields.String()
    numune_cloud_dosya =fields.String()
    teklif_cloud_dosya =fields.String()
    proforma =fields.String()
    numune =fields.String()
    teklif =fields.String()
  

class TeklifAyrintiRaporModel:
   id = None 
   musteri = ""
   proforma_cloud_dosya = ""
   numune_cloud_dosya = ""
   teklif_cloud_dosya = ""
   proforma = ""
   numune = ""
   teklif = ""