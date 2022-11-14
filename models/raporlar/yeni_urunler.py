from marshmallow import Schema,fields


class SiteYeniUrunlerSchema(Schema):

    id = fields.Int()
    urunadi = fields.String()
    foto = fields.String()
    kategoriadi = fields.String()

class SiteYeniUrunlerModel:

    id = None 
    urunadi = ""
    foto = ""
    kategoriadi = ""

class YeniSiparisSchema(Schema):

    id = fields.Int()
    order = fields.String()
    fob = fields.Float()
    ddp =  fields.Float()
    toplam = fields.Float()
    durum = fields.Float()
    link = fields.String()

class YeniSiparisModel:

    id = None
    order = ""
    fob = 0
    ddp =  0  
    toplam = 0
    durum = 0
    link = ""

class AnasayfaSevkiyatSchema(Schema):
  
    Firma = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    total = fields.Float()
    link = fields.String()
    

class AnasayfaSevkiyatModel:

   
    Firma = ""
    miktar = 0
    alis =  0  
    total = 0
    link = ""

  

class AnasayfaHepsiSevkiyatSchema(Schema):
  
    Firma = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    total = fields.Float()
    

class AnasayfaHepsiSevkiyatModel:

   
    Firma = ""
    miktar = 0
    alis =  0  
    total = 0


class AnasayfaAyrintiSevkiyatSchema(Schema):
  
    aciklama = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    siparis_no = fields.String()
    birim = fields.String()
    

class AnasayfaAyrintiSevkiyatModel:

   
    aciklama = ""
    miktar = 0
    alis =  0  
    siparis_no = ""
    birim = ""

class AnasayfaAyrintiHepsiSevkiyatSchema(Schema):
  
    aciklama = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    siparis_no = fields.String()
    birim = fields.String()
    

class AnasayfaAyrintiHepsiSevkiyatModel:

   
    aciklama = ""
    miktar = 0
    alis =  0  
    siparis_no = ""
    birim = ""

class AnasayfaAyrintiUretimSchema(Schema):
  
    aciklama = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    siparis_no = fields.String()
    birim = fields.String()
    

class AnasayfaAyrintiUretimModel:

   
    aciklama = ""
    miktar = 0
    alis =  0  
    siparis_no = ""
    birim = ""

class AnasayfaAyrintiHepsiUretimSchema(Schema):
  
    aciklama = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    siparis_no = fields.String()
    birim = fields.String()
    

class AnasayfaAyrintiHepsiUretimModel:

   
    aciklama = ""
    miktar = 0
    alis =  0  
    siparis_no = ""
    birim = ""
class AnasayfaUreticiSchema(Schema):
  
    Firma = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    total = fields.Float()
    

class AnasayfaUreticiModel:

    Firma = ""
    miktar = 0
    alis =  0  
    total = 0

class AnasayfaHepsiUreticiSchema(Schema):
  
    Firma = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    total = fields.Float()
    
class AnasayfaHepsiUreticiModel:
    
    Firma = ""
    miktar = 0
    alis =  0  
    total = 0

class AnasayfaMusteriSchema(Schema):
  
    Firma = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    total = fields.Float()
    

class AnasayfaMusteriModel:

    Firma = ""
    miktar = 0
    alis =  0  
    total = 0

class AnasayfaHepsiMusteriSchema(Schema):
  
    Firma = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    total = fields.Float()
    
class AnasayfaHepsiModel:
    
    Firma = ""
    miktar = 0
    alis =  0  
    total = 0

class AnasayfaAyrintiMusteriSchema(Schema):
  
    Firma = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    total = fields.Float()
    siparis_no = fields.String()
    aciklama = fields.String()
    birim = fields.String()
    
    

class AnasayfaAyrintiMusteriModel:

    Firma = ""
    miktar = 0
    alis =  0  
    total = 0  
    siparis_no = ""       
    aciklama = ""
    birim = "" 

class AnasayfaHepsiAyrintiMusteriSchema(Schema):
  
    Firma = fields.String()
    miktar = fields.Float()
    alis =  fields.Float()
    total = fields.Float()
    siparis_no = fields.String()
    aciklama = fields.String()
    birim = fields.String()
    
class AnasayfaHepsiAyrintiMusteriModel:

    Firma = ""
    miktar = 0
    alis =  0  
    total = 0     
    siparis_no = ""       
    aciklama = ""
    birim = "" 

class AnasayfaHepsiSiparisSchema(Schema):
  
    tarih = fields.Date()
    siparisNo = fields.String()
    musteriadi = fields.String()
    satistoplam  = fields.Float()
    teslim =  fields.String()
    navlun = fields.Float()
    detay1 = fields.Float()
    detay2 = fields.Float()
    detay3 = fields.Float()
    detay4 = fields.Float()
    
class AnasayfaHepsiSiparisModel:

    tarih= None
    siparisNo = ""
    musteriadi = ""
    teslim = ""
    satistoplam =  0  
    navlun = 0     
    detay1 = 0      
    detay2 = 0 
    detay3 = 0    
    detay4 = 0                             