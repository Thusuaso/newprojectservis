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

class NumuneFinansAnaListeModel:
    id = None
    musteriadi = ""
    kuryeAlis = 0
    kuryeSatis = 0
    TL_Alis = 0
    TL_Satis = 0
    Euro_Alis = 0
    Euro_Satis = 0
    

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
