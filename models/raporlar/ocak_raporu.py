from marshmallow import Schema,fields



class OcakSchema(Schema): 

    
 
    ocakAdi = fields.String()
    mt2 = fields.Float()
    mt = fields.Float()
    adet = fields.Int()
    kasaSayisi = fields.Int()
   


class OcakModel:

  
    ocakAdi =  ""
    mt2 = 0
    mt = 0
    adet = 0
    kasaSayisi = 0



    
       
   
   