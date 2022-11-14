from marshmallow import Schema,fields


class KasaListesiSchema(Schema):

    id = fields.Int()
    kasano = fields.Int()
    birimfiyat = fields.Float()
    toplam = fields.Float()

    #custom alanlar
    urunadi = fields.String()
    yuzeyislem = fields.String()
    ebat = fields.String()
    miktar = fields.Float()
    birimadi = fields.String()
    kasa_secim = fields.Boolean()
    tedarikci_id = fields.Int()

class KasaListesiModel:
    id = None 
    kasano = fields.Int()
    birimfiyat = 0 
    toplam = 0 

    #custom alanlar
    urunadi = ""
    yuzeyislem = ""
    ebat = ""
    miktar = 0
    birimadi = ""
    kasa_secim = False
    tedarikci_id = None