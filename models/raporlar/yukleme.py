from marshmallow import Schema,fields,validate


class YuklemeAylikSchema(Schema):

   yukleme_tarihi = fields.String()
   siparis_no = fields.String()
   musteri_adii = fields.String()
   fob = fields.Float()
   dtp = fields.Float()
   tur = fields.String()
   marketing = fields.String()

class YuklemeAylikModel:

    yukleme_tarihi = ""
    siparis_no = "" 
    musteri_adii = ""
    fob = 0
    dtp = 0
    tur = ""
    marketing = ""

class YuklemeYillikSchema(Schema):

   yukleme_tarihi = fields.String()
   siparis_no = fields.String()
   musteri_adi = fields.String()
   fob = fields.Float()
   dtp = fields.Float()
   tur = fields.String()
   marketing = fields.String()
 
class YuklemeYillikModel:

    yukleme_tarihi = ""
    siparis_no = "" 
    musteri_adi = ""
    fob = 0
    dtp = 0
    tur = ""
    marketing = ""   

class SayimYillikSchema(Schema):

   marketing = fields.String()
   yukleme_sayisi = fields.Int()
   yukleme_sayisiay = fields.Int()

class SayimYillikModel:

   marketing = "" 
   yukleme_sayisi = 0 
   yukleme_sayisiay = 0

class SayimAylikSchema(Schema):

   marketing = fields.String()
   yukleme_sayisi = fields.Int()
  
class SayimAylikModel:

   marketing = "" 
   yukleme_sayisi = 0 

class YuklemeAySchema(Schema):
    id = fields.Int()
    ay = fields.Int()
    ay_str = fields.String()

class YuklemeAyModel:
    id = None
    ay = 0
    ay_str = ""        
     
class YuklemeyilSchema(Schema):
    id = fields.Int()
    yil = fields.Int()
    

class YuklemeYilModel:

    id = None
    yil = 0    


    
