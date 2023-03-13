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


class StokRaporuFilterSchema(Schema):
    sira = fields.Int()
    kasa_no = fields.Int()
    tarih = fields.String()
    kategori_adi = fields.String()
    urun_adi = fields.String()
    yuzey_islem = fields.String()
    olcu = fields.String()
    firma_adi = fields.String()
    ocak_adi = fields.String()
    urun_durum = fields.String()
    siparis_aciklama = fields.String()
    aciklama = fields.String()
    miktar = fields.Float()
    birim_adi = fields.String()
    kutu_adet = fields.Int()
    kutu_ici_adet = fields.Int()
    adet = fields.Int()
    
class StokRaporuFilterModel(Schema):
    sira = 0
    kasa_no = 0
    tarih = ""
    kategori_adi = ""
    urun_adi = ""
    yuzey_islem = ""
    olcu = ""
    firma_adi = ""
    ocak_adi = ""
    urun_durum = ""
    siparis_aciklama = ""
    aciklama = ""
    miktar = 0
    birim_adi = ""
    kutu_adet = 0
    kutu_ici_adet = 0
    adet = 0
    
       
   
   