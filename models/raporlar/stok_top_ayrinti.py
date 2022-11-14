from marshmallow import Schema,fields



class StokTopAyrintiSchema(Schema): 

    id = fields.Int()
    tedarikci_aditop  = fields.String()
    kategoritop  = fields.String()
    tarihtop  = fields.Date()
    kasanotop  = fields.Int()
    urunaditop  = fields.String()
    ocakaditop  = fields.String()
    yuzeyislemtop  = fields.String()
    entop  = fields.String()
    boytop  = fields.String()
    kenartop  = fields.String()
    adettop  = fields.Int()
    miktartop  = fields.Float()
    birimaditop = fields.String()
    uretimaciklamatop = fields.String()
    kutuadettop  = fields.Int()
    sira = fields.Int()
    durum = fields.String()
    aciklama = fields.String()

class StokTopAyrintiModel:

    id = None
    tedarikci_aditop  = ""
    kategoritop  = ""
    tarihtop  = None
    kasanotop  = 0
    urunaditop  = ""
    ocakaditop  = ""
    yuzeyislemtop  = ""
    entop  = ""
    boytop  = ""
    kenartop  = ""
    adettop  = 0
    miktartop  = 0
    sira = 0
    birimaditop = ""
    uretimaciklamatop = ""
    kutuadettop  = 0
    durum = ""
    aciklama  = ""
   
   