from marshmallow import Schema,fields

class NakliyeListeSchema(Schema):
    
    id = fields.Int() 
    siparis_no = fields.String()
    firma_adi = fields.String()
    Firma_id = fields.Int()
    faturaNo = fields.String()
    Tutar_tl = fields.Float()
    kur = fields.Float()
    Tutar_dolar = fields.Float()
    tarih = fields.Date()
    link = fields.String()
    
    
class NakliyeListeModel:
    id = None 
    siparis_no = ""
    firma_adi = ""
    Firma_id = 0
    faturaNo = ""
    Tutar_tl = 0
    kur = 0
    Tutar_dolar = 0
    tarih = None
    link = ""
    
class NakliyeIslemSchema(Schema):
    
    
    id = fields.Int() 
    firma_adi = fields.String()
    Firma_id = fields.Int()
    siparisno = fields.String()
    faturaNo = fields.String()
    Tutar_tl = fields.Float()
    kur = fields.Float()
    Tutar_dolar = fields.Float()
    tarih = fields.Date()
   
    
    
class NakliyeIslemModel:
    id = None 
    firma_adi = ""
    Firma_id = 0
    siparisno = ""
    faturaNo = ""
    Tutar_tl = 0
    kur = 0
    Tutar_dolar = 0
    tarih = None
  


   