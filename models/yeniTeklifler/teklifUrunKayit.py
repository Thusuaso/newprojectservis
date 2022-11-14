from marshmallow import Schema,fields


class TeklifUrunKayitSchema(Schema):
    id = fields.Int()
    tarih = fields.String()
    teklifId = fields.Int()
    kategoriId = fields.Int()
    urunId = fields.Int()
    enBoyId = fields.Int()
    yuzeyIslemId = fields.Int()
    kalinlikId = fields.Int()
    fobFiyat = fields.Float()
    teklifFiyat = fields.Float()
    birim = fields.String()
    #custom field
    kategoriAdi = fields.String()
    yuzeyIslem = fields.String()
    urunAdi = fields.String()
    enBoy = fields.String()
    kalinlik = fields.String()
    yuklemeTipi = fields.String()



class TeklifUrunKayitModel:
    id = None 
    tarih = ""
    teklifId = None 
    kategoriId = None 
    urunId = None 
    enBoyId = None 
    yuzeyIslemId = None 
    kalinlikId = None 
    fobFiyat = 0
    teklifFiyat = 0
    birim = ""
    #custon field
    kategoriAdi = ""
    yuzeyIslem = ""
    urunAdi = ""
    enBoy = ""
    kalinlik = ""
    yuklemeTipi = ""