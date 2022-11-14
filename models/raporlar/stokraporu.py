from marshmallow import Schema,fields



class StokSchema(Schema): 

    
 
    ebat = fields.String()
    kategori = fields.String()
    tedarikci_adi = fields.String()
    yuzey_islem = fields.String()
    urun_adi = fields.String()
    kutu = fields.Int()
    urunkart_id = fields.Int()
    kasa_adet = fields.Int()
    tedarikci_id = fields.Int()
   


class StokModel:

  
    ebat =  ""
    kategori =  ""
    tedarikci_adi =  ""
    yuzey_islem = ""
    urun_adi = ""
    kutu = 0
    urunkart_id = 0
    kasa_adet = 0
    tedarikci_id = 0


class StokEbatSchema(Schema): 

    
 
    ebat = fields.String()
   
   


class StokEbatModel:

  
    ebat =  ""
    
       
   
   