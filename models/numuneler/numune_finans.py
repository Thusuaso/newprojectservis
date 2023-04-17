from marshmallow import Schema,fields


class NumuneFinansAnaListeSchema(Schema):
    id = fields.Int()
    musteriadi = fields.String()
    kuryeAlis = fields.Float()
    kuryeSatis = fields.Float()
    TL_Alis = fields.Float()
    TL_Satis = fields.Float()
    Euro_Alis = fields.Float()
    Euro_Satis = fields.Float()
    gelenBedel = fields.Float()
class NumuneFinansAnaListeModel:
    id = None
    musteriadi = ""
    kuryeAlis = 0
    kuryeSatis = 0
    TL_Alis = 0
    TL_Satis = 0
    Euro_Alis = 0
    Euro_Satis = 0
    gelenBedel = 0
    

class NumuneFinansAyrintiSchema(Schema):

    id = fields.Int()
    orderno = fields.String()
    tarih = fields.String()
    sevktarihi = fields.String()
    musteri_id = fields.Int()
    kuryeAlis = fields.Float()
    kuryeSatis = fields.Float()
    TL_Alis = fields.Float()
    TL_Satis = fields.Float()
    Euro_Alis = fields.Float()
    Euro_Satis = fields.Float()
    odeme = fields.String()
    banka = fields.String()
    numune_tarihi = fields.String()

class NumuneFinansAyrintiModel:
    id = None
    orderno = ""
    tarih = ""
    sevktarihi = ""
    musteri_id = None
    kuryeAlis = 0
    kuryeSatis = 0
    TL_Alis = 0
    TL_Satis = 0
    Euro_Alis = 0
    Euro_Satis = 0
    odeme = ""
    banka = ""
    numune_tarihi = ""
    

class NumuneFinansBankaSchema(Schema):
     bedel = fields.Float() # $
     bedel_tl = fields.Float() #tl
     bedel_euro = fields.Float() #euro
     banka = fields.String()

class NumuneFinansBankaModel:  

     bedel = 0
     bedel_tl = 0
     bedel_euro = 0
     banka = ""

class NumuneYilSchema(Schema):

    id = fields.Int()
    yil = fields.Int()

class NumuneYilModel:

    id = None
    yil = 0
    
    
class NumuneBankayaGelenAyrintiSchema(Schema):
    id = fields.Int()
    bedel_dolar = fields.Float()
    bedel_euro = fields.Float()
    bedel_tl = fields.Float()
    banka_adi = fields.String()
    numune_no = fields.String()
    musteri_adi = fields.String()
    numune_tarihi = fields.String()
    bankaya_gelen_tarih = fields.String()
    
class NumuneBankayaGelenAyrintiModel:
    id = 0
    bedel_dolar = 0
    bedel_euro = 0
    bedel_tl = 0
    banka_adi = ""
    numune_no = ""
    musteri_adi = ""
    numune_tarihi = ""
    bankaya_gelen_tarih = ""