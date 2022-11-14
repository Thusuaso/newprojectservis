from marshmallow import Schema,fields



class OcakDetaySchema(Schema): 

    
 
    tarih = fields.String()
    kasano = fields.Int()
    adet = fields.Integer()
    mt2 = fields.Float()
    cikisno = fields.String()
    ocakAdi = fields.String()
    kategori = fields.String()
    urunadi = fields.String()
    en = fields.String()
    boy = fields.String()
    kenar = fields.String()
    yuzeyislem = fields.String()    
   


class OcakDetayModel:

  
    tarih = ""
    kasano = 0
    adet = 0
    mt2 = 0
    cikisno = ""
    ocakAdi = ""
    kategori = ""
    urunadi = ""
    en = ""
    boy = ""
    kenar = ""
    yuzeyislem = ""   


    
       
   
   