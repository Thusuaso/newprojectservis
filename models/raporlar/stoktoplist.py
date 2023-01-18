from marshmallow import Schema,fields



class StokTopSchema(Schema): 

    
 
    ebattop = fields.String()
    kategoritop = fields.String()
    tedarikci_aditop = fields.String()
    yuzey_islemtop = fields.String()
    urun_aditop = fields.String()
    kututop = fields.Int()
    urunkart_idtop = fields.Int()
    kasa_adettop = fields.Int()
    tedarikci_idtop = fields.Int()
   


class StokTopModel:

  
    ebattop =  ""
    kategoritop =  ""
    tedarikci_aditop =  ""
    yuzey_islemtop = ""
    urun_aditop = ""
    kututop = 0
    urunkart_idtop = 0
    kasa_adettop = 0
    tedarikci_idtop = 0
   

class StokEbatSchema(Schema):
    ebat = fields.String()
    kasaadet = fields.Int()

class StokEbatModel:
    ebat = ""
    kasaadet = 0
    
    
    
class StokAnaListeSchema(Schema):
    ebat = fields.String()
    kasaSayisi = fields.Integer()
    yuzeyIslem = fields.String()
    urunAdi = fields.String()
    tedarikciAdi = fields.String()
    en = fields.String()
    boy = fields.String()
    kenar = fields.String()
    miktar = fields.Float()
    urunKartId = fields.Int()
    ocak = fields.String()
    price = fields.Float()

class StokAnaListeModel:
    ebat = ""
    kasaSayisi = 0
    yuzeyIslem = ""
    urunAdi = ""
    tedarikciAdi=""
    en = ""
    boy = ""
    kenar = ""
    miktar = 0
    urunKartId = 0
    ocak = ""
    price = 0