from marshmallow import Schema,fields


class UrunKayitSchema(Schema):
    id = fields.Int()
    tarih = fields.Date()
    teklifId = fields.Int()
    kategoriId = fields.Int()
    urunId = fields.Int()
    enBoyId = fields.Int()
    yuzeyIslemId = fields.Int()
    kalinlikId = fields.Int()
    fobFiyat = fields.Float()
    teklifFiyat = fields.Float()
    birim = fields.String()


class UrunKayitModel:
    id = None
    tarih = None
    teklifId = None
    kategoriId = None
    urunId = None
    enBoyId =  None
    yuzeyIslemId = None
    kalinlikId = None
    fobFiyat = 0
    teklifFiyat = 0
    birim = ""

    
        



        