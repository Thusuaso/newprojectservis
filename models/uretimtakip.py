
from marshmallow import Schema,fields


class UretimTakipSchema(Schema):
    id = fields.Int()
    siparis_no = fields.String()
    miktar = fields.Int()
    urun_birimi = fields.String()
    tedarikci = fields.String()
    uretim_acıklama = fields.String()
    urunadi = fields.String()
    yuzeyadi = fields.String()
    en = fields.String()
    boy = fields.String()
    kenar = fields.String()
    siparis_sahibi = fields.String()
   
class UretimTakipModel:
    id = None
    siparis_no = ""
    miktar = 0
    urun_birimi = ""
    tedarikci = ""
    uretim_acıklama = ""
    urunadi = ""
    yuzeyadi = ""
    en =""
    boy = ""
    kenar = ""
    siparis_sahibi = ""





    


    kutu = False
    duzenleyen = ""
    kasalayan = ""
    disarda = False
    etiketDurum = False
    kullaniciId = None
    siraNo = None