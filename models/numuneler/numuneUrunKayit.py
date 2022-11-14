from marshmallow import Schema,fields


class NumuneUrunKayitSchema(Schema):
    id = fields.Int()
    numuneNo = fields.String()
    
    kategoriId = fields.Int()
    
    miktar = fields.Float()
    
    urunBirim = fields.String()
    urunBirim_id = fields.Int()
    urunAciklama = fields.String()
    musteriAciklama = fields.String()
    sira = fields.Int()
    kategoriAdi = fields.String()
    
    m2 = fields.Float()
    adet = fields.Float()
    mt = fields.Float()
    ton = fields.Float()
    detayTutar1 = fields.Float()
    detayAlis1 = fields.Float()
    detayTutar2 = fields.Float()
    detayTutar3 = fields.Float()



class NumuneUrunKayitModel:
    id = None 
    numuneNo =""
   
    kategoriId = None
   
   
    miktar = 0
    
    urunBirim = ""
    urunBirim_id = None
    urunAciklama = ""
    musteriAciklama = ""
    sira = 0
    kategoriAdi = ""
   
    m2 = 0
    adet = 0
    mt = 0
    ton = 0
    detayTutar1  = 0
    detayAlis1 = 0
    detayTutar2 = 0
    detayTutar3 = 0 