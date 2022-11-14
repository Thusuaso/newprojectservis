from marshmallow import Schema,fields


class SiparisKalemSchema(Schema):
    id = fields.Int()
    urunkartid = fields.Int()
    tedarikciid = fields.Int()
    uretim = fields.Float()
    siparis = fields.Float()
    tedarikciadi = fields.String()
    icerik = fields.String()
    navlunsatis = fields.Int()
    teslimturu = fields.String()
class SiparisKalemModel:

    id = None 
    urunkartid = None 
    tedarikciid = None 
    uretim = 0 
    siparis = 0 
    tedarikciadi = ""
    icerik = ""
    navlunsatis=0
    teslimturu = ""